def visualize(data, unique_id="", sidebar_values=None):
    # Defensive: ensure data is always a dict with "events"
    if isinstance(data, list):
        events = data
    elif isinstance(data, dict) and "events" in data:
        events = data["events"]
    else:
        st.error("Invalid data format for visualize()")
        st.stop()
    
    # st.markdown("### 🔍 Search Events")
    search_query = ""
    st.markdown("\n")
    st.markdown("\n")
    search_query = st.text_input("", placeholder="Search...", label_visibility="collapsed", key=f"search_input_{unique_id}")
    st.markdown("\n")
    st.markdown("\n")
    # Use passed sidebar values or create new ones
    if sidebar_values is None:
        start_date, end_date, show_only_with_submissions, show_only_with_both_submissions, selected_case, selected_doc_types, selected_entity_names = show_sidebar(events, unique_id)
    else:
        start_date, end_date, show_only_with_submissions, show_only_with_both_submissions, selected_case, selected_doc_types, selected_entity_names = sidebar_values
    
    # Filter events
    filtered_events = events
    
    # Apply case name filter
    if selected_case and selected_case != "All Events":
        filtered_events = [event for event in filtered_events 
                        if event.get("case_name") == selected_case]
    
    # Apply document type filter
    if selected_doc_types and len(selected_doc_types) > 0:
        filtered_events = [event for event in filtered_events 
                        if (event.get("doc_type", "evidence") if not isinstance(event.get("doc_type"), tuple) else event.get("doc_type", ("evidence",))[0]) in selected_doc_types]
    
    # Apply entity name filter
    if selected_entity_names and len(selected_entity_names) > 0:
        filtered_events = [event for event in filtered_events 
                        if all(selected_name in [entity.get("name") for entity in event.get("named_entities", []) if isinstance(entity, dict)]
                               for selected_name in selected_entity_names)]
    # If no entity names are selected, show all events (no filtering)
    

    
    # Apply search filter
    if search_query:
        filtered_events = [event for event in filtered_events 
                        if search_query.lower() in event["event"].lower()]
    
    # Apply date filter
    filtered_events = [
        event for event in filtered_events
        if parse_date(event["date"]) and start_date <= parse_date(event["date"]).date() <= end_date
    ]
    
    # Apply submissions filter if toggle is on
    if show_only_with_submissions:
        filtered_events = [
            event for event in filtered_events
            if (event.get("claimant_arguments") or event.get("respondent_arguments"))
        ]
    
    # Apply both submissions filter if that toggle is on
    if show_only_with_both_submissions:
        filtered_events = [
            event for event in filtered_events
            if (event.get("claimant_arguments") and event.get("respondent_arguments") and 
                len(event.get("claimant_arguments", [])) > 0 and len(event.get("respondent_arguments", [])) > 0)
        ]
        
    
    # Sort events by date
    filtered_events = sorted(filtered_events, key=lambda x: parse_date(x["date"]) or datetime.min)

    # Check if any events were found
    if not filtered_events:
        st.warning("⚠️ No events found with the provided filter combination. Please try adjusting your filters.")
        return filtered_events

    # Display events
    for event_key, event in enumerate(filtered_events):
        date_formatted = format_date(event["date"])
        
        # Create expander for each event
        # Add CSS to increase expander font size
        st.markdown("""
            <style>
            .st-emotion-cache-br351g p {
                font-size: 15px !important;
            }
            .st-emotion-cache-vlxhtx {
                gap: 0.5rem !important;
            }
            </style>
        """, unsafe_allow_html=True)

        # Highlight named entities in event title
        highlighted_event = highlight_named_entities_in_event(event['event'], event.get('named_entities', []))
        with st.expander(f"**:blue-background[:blue[{event['date']}]]** | {highlighted_event}"):
            # Calculate citation counts
            claimant_count = len(event.get("claimant_arguments", []))
            respondent_count = len(event.get("respondent_arguments", []))
            doc_count = len(event.get("pdf_name", []))
            # total_count = claimant_count + respondent_count + doc_count
            total_count = doc_count
            
            # Determine if each party has addressed this event
            has_claimant = claimant_count > 0
            has_respondent = respondent_count > 0
            
            # Citations counter and party badges
            # Build the badges dynamically based on who addressed the event
            badges = []
            if has_claimant:
                badges.append('<span class="badge badge-active-claimant">Claimant</span>')
            if has_respondent:
                badges.append('<span class="badge badge-active-respondent">Respondent</span>')
            
            case_name_html = ""
            if "case_name" in event and event["case_name"]:
                case_name_html = f"""<span style="font-size: 12px; text-transform: uppercase; color: #757575; font-weight: 500; margin-right: 10px;">Proceedings:</span> <span class='badge badge-active-case'>{event['case_name']}</span>"""
            
            badges_html = ''.join(badges) if badges else '<span class="badge badge-inactive">Not Addressed</span>'

            st.markdown(f"""
            <div class="citation-counter">
                <div class="counter-box">
                    <span class="counter-value">{total_count}</span>
                    <span class="counter-label">Sources</span>
                </div>
                <div style="border-left: 1px solid #ddd; height: 24px; margin: 0 16px;"></div>
                {case_name_html}
                <div style="border-left: 1px solid #ddd; height: 24px; margin: 0 16px;"></div>
                <span style="font-size: 12px; text-transform: uppercase; color: #757575; font-weight: 500; margin-right: 10px;">Addressed by:</span>
                {badges_html}
            </div>
            """, unsafe_allow_html=True)
            
            # Supporting Documents section
            if event.get("pdf_name") or event.get("doc_sum"):
                st.markdown("##### Supporting Documents")
                # st.write(event)
                
                # Create sets to track unique documents and their summaries
                seen_docs = set()
                doc_sum_dict = {}

                # Pair documents with their summaries and remove duplicates
                for i, (pdf_name, doc_name) in enumerate(zip(event.get("pdf_name", []), event.get("doc_name", []))):
                    if doc_name not in seen_docs:
                        seen_docs.add(doc_name)
                        doc_sum_dict[pdf_name] = {
                            'pdf_name': pdf_name,
                            'doc_name': doc_name,
                            'doc_sum': event.get("doc_sum", [""])[i] if i < len(event.get("doc_sum", [])) else "",
                            'source_text': event.get("source_text", [""])[i] if i < len(event.get("source_text", [])) else "",
                            'page': int(event.get("page", ["0"])[i]) if i < len(event.get("page", [])) and event.get("page", ["0"])[i].isdigit() else 0,
                        }

                # Display unique documents
                for supporting_doc_key, (pdf_name, details) in enumerate(doc_sum_dict.items()):
                    # Remove timestamp suffix from PDF name using regex
                    pdf_name = re.sub(r'_\d{8}_\d{6}\.pdf$', '', pdf_name)
                    st.markdown(f"""
                    <div class="document-card">
                        <div style="font-size: 14px; font-weight: 700; margin-bottom: 8px;">{html.escape(pdf_name or "Unknown document")}</div>
                        <div style="font-size: 14px; color: #616161; margin-top: 4px;"><b>Summary:</b> {html.escape(details["doc_sum"] or "No summary available")}</div>
                        <div style="font-size: 14px; color: #616161; margin-top: 4px; background-color: #1c83e11a; padding: 8px; border-radius: 4px;"><span style="font-weight: 700;">Citation: </span><span>{html.escape(pdf_name or "Unknown document")}, page {details["page"]}.</span></div>
                        <div style="font-size: 14px; color: #616161; margin-top: 4px; background-color: #d1fae5; padding: 8px; border-radius: 4px;"><span style="font-weight: 700;">Source: </span><span>{html.escape(details["source_text"] or "No source text available")}</span></div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    popover_col_1, popover_col_2 = st.columns([3, 1])
                    
                    key=f"{event_key}_{supporting_doc_key}_{pdf_name}_{generate_random_string()}"

                    with popover_col_1.popover("View Document", use_container_width=True):
                        # Search for PDF in base folder and subfolders
                        
                        retrieve_pdf(base_folder, details, key)

                    with popover_col_2:
                        download_pdf(base_folder, details, key)
                       
                    # with popover_col_3:
                    #     @st.fragment
                    #     def on_copy_click_button(text):
                    #         def on_copy_click(text):
                    #             clipboard.copy(text)
                    #             st.toast("Text copied to clipboard!", icon="📋")

                    #         st.button("📋 Copy Source", key=f"copy_source_{key}", on_click=on_copy_click, args=(text,), use_container_width=True)
                    #     on_copy_click_button(f"""Page {details["page"]}: {details["source_text"]}""")
            
            # Submissions section
            if event.get("claimant_arguments") or event.get("respondent_arguments"):
                st.markdown("##### Submissions")
                
                # Two-column layout for claimant and respondent
                col1, col2 = st.columns(2)
                
                # Claimant submissions
                with col1:
                    st.markdown("<div class='claimant-header'>Claimant</div>", unsafe_allow_html=True)
                    
                    if event.get("claimant_arguments"):
                        for arg in event["claimant_arguments"]:
                            st.markdown(f"""
                            <div class="document-card">
                                <div style="font-weight: 500;">Page {arg['page']}</div>
                                <div style="font-size: 14px; color: #616161; margin-top: 4px;">{arg['source_text']}</div>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.markdown("<div style='color: #BDBDBD; font-style: italic;'>No claimant submissions</div>", unsafe_allow_html=True)
            
                # Respondent submissions
                with col2:
                    st.markdown("<div class='respondent-header'>Respondent</div>", unsafe_allow_html=True)
                    
                    if event.get("respondent_arguments"):
                        for arg in event["respondent_arguments"]:
                            st.markdown(f"""
                            <div class="document-card">
                                <div style="font-weight: 500;">Page {arg['page']}</div>
                                <div style="font-size: 14px; color: #616161; margin-top: 4px;">{arg['source_text']}</div>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.markdown("<div style='color: #BDBDBD; font-style: italic;'>No respondent submissions</div>", unsafe_allow_html=True)
    return filtered_events
