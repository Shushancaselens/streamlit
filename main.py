def main():
    # Add sidebar
    with st.sidebar:
        st.title("Dashboard Info")
        st.markdown("""
            This dashboard displays legal arguments and related case law. 
            
            Use the search bar above to find specific cases, arguments, or evidence.
            
            Toggle between Summary and Detailed views to adjust the level of information shown.
        """)
        
        st.markdown("---")
        st.info("For additional help or support, contact the legal team.")
    
    st.title("Legal Arguments Dashboard - Table View")
    
    # Add view toggle
    view_type = st.radio("Select View", ["Detailed Table", "Summary Table"], horizontal=True)
    
    # Search bar and export button in the same row
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        search = st.text_input("", 
                             placeholder="🔍 Search issues, arguments, or evidence...",
                             label_visibility="collapsed")
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
    
    if search:
        search = search.lower()
        mask = df.apply(lambda x: x.astype(str).str.lower().str.contains(search).any(), axis=1)
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
