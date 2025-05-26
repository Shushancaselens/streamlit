def visualize(data, unique_id="", sidebar_values=None):
    # Defensive: ensure data is always a dict with "events"
    if isinstance(data, list):
        events = data
    elif isinstance(data, dict) and "events" in data:
        events = data["events"]
    else:
        st.error("Invalid data format for visualize()")
        st.stop()
    
    # Use passed sidebar values or create new ones
    if sidebar_values is None:
        search_query, start_date, end_date, show_only_with_submissions, show_only_with_both_submissions = show_sidebar(events, unique_id)
    else:
        search_query, start_date, end_date, show_only_with_submissions, show_only_with_both_submissions = sidebar_values
    
    # Filter events
    filtered_events = events
    
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
   
    # Display events
    for event_key, event in enumerate(filtered_events):
        date_formatted = format_date(event["date"])
        
        # Create expander for each event
        with st.expander(f" {event['event']}"):
            # Add case name badge if it exists
            if "case_name" in event:
                st.badge(event["case_name"])
            
            # Calculate citation counts
            claimant_count = len(event.get("claimant_arguments", []))
            respondent_count = len(event.get("respondent_arguments", []))
            doc_count = len(event.get("pdf_name", []))
            total_count = claimant_count + respondent_count + doc_count
            
            # Determine if each party has addressed this event
            has_claimant = claimant_count > 0
            has_respondent = respondent_count > 0
            
            
            # print(event, " >>> ", has_claimant, has_respondent)
            
            # Citations counter and party badges
            # Build the badges dynamically based on who addressed the event
            badges = []
            if has_claimant:
                badges.append('<span class="badge badge-active-claimant">Claimant</span>')
            if has_respondent:
                badges.append('<span class="badge badge-active-respondent">Respondent</span>')
            badges_html = ''.join(badges) if badges else '<span class="badge badge-inactive">Not Addressed</span>'
