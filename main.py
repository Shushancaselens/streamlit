def main():
    st.title("Legal Arguments Dashboard")
    
    # Add tab selection at the top
    tab1, tab2 = st.tabs(["Table View", "Detailed View"])
    
    with tab1:
        st.subheader("Table View")
        # Add view toggle
        view_type = st.radio("Select View", ["Detailed Table", "Summary Table"], horizontal=True)
        
        # Search bar and export button in the same row
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            table_search = st.text_input("", 
                                 placeholder="🔍 Search issues, arguments, or evidence...",
                                 label_visibility="collapsed",
                                 key="table_search")
        with col2:
            if st.button("📋 Export Data", type="primary", use_container_width=True):
                df = create_table_data()
                st.download_button(
                    "Download Full Data",
                    df.to_csv(index=False),
                    "legal_arguments_table.csv",
                    "text/csv",
                    use_container_width=True
                )
        
        # Create and filter table data
        df = create_table_data()
        
        if table_search:
            table_search = table_search.lower()
            mask = df.apply(lambda x: x.astype(str).str.lower().str.contains(table_search).any(), axis=1)
            df = df[mask]
        
        # Display based on view type
        if view_type == "Summary Table":
            summary_df = df[["issue", "appellant_position", "respondent_position"]]
            st.dataframe(
                summary_df,
                use_container_width=True,
                column_config={
                    "issue": st.column_config.TextColumn("Issue", width="medium"),
                    "appellant_position": st.column_config.TextColumn("Appellant Position", width="large"),
                    "respondent_position": st.column_config.TextColumn("Respondent Position", width="large")
                }
            )
        else:
            st.dataframe(
                df,
                use_container_width=True,
                column_config={
                    "issue": st.column_config.TextColumn("Issue", width="medium"),
                    "appellant_position": st.column_config.TextColumn("Appellant Position", width="large"),
                    "appellant_details": st.column_config.TextColumn("Appellant Details", width="large"),
                    "appellant_evidence": st.column_config.TextColumn("Appellant Evidence", width="large"),
                    "appellant_cases": st.column_config.TextColumn("Appellant Case Law", width="large"),
                    "respondent_position": st.column_config.TextColumn("Respondent Position", width="large"),
                    "respondent_details": st.column_config.TextColumn("Respondent Details", width="large"),
                    "respondent_evidence": st.column_config.TextColumn("Respondent Evidence", width="large"),
                    "respondent_cases": st.column_config.TextColumn("Respondent Case Law", width="large")
                }
            )
    
    with tab2:
        st.subheader("Detailed View")
        # Search bar and export button for detailed view
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            detailed_search = st.text_input("", 
                                     placeholder="🔍 Search issues, arguments, or evidence...",
                                     label_visibility="collapsed",
                                     key="detailed_search")
        with col2:
            if st.button("📋 Export Summary", type="primary", use_container_width=True):
                summary_data = []
                for arg in argument_data:
                    summary_data.append({
                        "Issue": arg["issue"],
                        "Appellant Position": arg["appellant"]["mainArgument"],
                        "Respondent Position": arg["respondent"]["mainArgument"]
                    })
                df = pd.DataFrame(summary_data)
                st.download_button(
                    "Download Summary",
                    df.to_csv(index=False),
                    "legal_arguments_summary.csv",
                    "text/csv",
                    use_container_width=True
                )
        
        # Filter arguments based on search
        filtered_arguments = argument_data
        if detailed_search:
            detailed_search = detailed_search.lower()
            filtered_arguments = [
                arg for arg in argument_data
                if (detailed_search in arg['issue'].lower() or
                    any(detailed_search in detail.lower() for detail in arg['appellant']['details']) or
                    any(detailed_search in detail.lower() for detail in arg['respondent']['details']) or
                    any(detailed_search in e['desc'].lower() for e in arg['appellant']['evidence']) or
                    any(detailed_search in e['desc'].lower() for e in arg['respondent']['evidence']))
            ]
        
        # Display arguments
        for arg in filtered_arguments:
            with st.expander(f"{arg['issue']} ({arg['category']})", expanded=arg['id'] == '1'):
                col1, col2 = st.columns(2)
                with col1:
                    create_position_section(arg['appellant'], "Appellant")
                with col2:
                    create_position_section(arg['respondent'], "Respondent")
            
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
