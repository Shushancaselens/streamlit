import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
import re

# [Previous imports and code remain the same until argument_data]

def extract_case_year(case_id):
    """Extract year from case identifier"""
    try:
        match = re.search(r'(\d{4})', case_id)
        return int(match.group(1)) if match else None
    except:
        return None

def analyze_cases():
    """Analyze case law patterns and statistics"""
    all_cases = []
    categories = []
    years = []
    
    # Collect all cases and their contexts
    for arg in argument_data:
        category = arg['category']
        # Collect appellant cases
        for case in arg['appellant']['caselaw']:
            all_cases.append({
                'case_id': case,
                'category': category,
                'party': 'appellant',
                'year': extract_case_year(case),
                'summary': get_case_summary(case)
            })
        # Collect respondent cases
        for case in arg['respondent']['caselaw']:
            all_cases.append({
                'case_id': case,
                'category': category,
                'party': 'respondent',
                'year': extract_case_year(case),
                'summary': get_case_summary(case)
            })
    
    return pd.DataFrame(all_cases)

def main():
    st.title("Legal Arguments Dashboard")
    
    # Create tabs for different views
    tab1, tab2 = st.tabs(["Arguments Table", "Case Law Analysis"])
    
    with tab1:
        # [Previous table view code remains the same]
        st.header("Arguments Table")
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
    
    with tab2:
        st.header("Case Law Analysis")
        
        # Get case analysis data
        case_df = analyze_cases()
        
        # Display summary statistics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Cases Cited", len(case_df))
        with col2:
            st.metric("Unique Categories", len(case_df['category'].unique()))
        with col3:
            st.metric("Year Range", f"{case_df['year'].min()} - {case_df['year'].max()}")
        
        # Create visualizations
        st.subheader("Cases by Category")
        category_fig = px.bar(
            case_df['category'].value_counts().reset_index(),
            x='index',
            y='category',
            labels={'index': 'Category', 'category': 'Number of Citations'},
            title="Case Citations by Category"
        )
        st.plotly_chart(category_fig, use_container_width=True)
        
        st.subheader("Cases by Year")
        year_fig = px.histogram(
            case_df,
            x='year',
            title="Case Citations by Year",
            labels={'year': 'Year', 'count': 'Number of Citations'}
        )
        st.plotly_chart(year_fig, use_container_width=True)
        
        # Display case details
        st.subheader("Case Details")
        selected_category = st.selectbox("Filter by Category", ["All"] + list(case_df['category'].unique()))
        
        filtered_df = case_df if selected_category == "All" else case_df[case_df['category'] == selected_category]
        st.dataframe(
            filtered_df[['case_id', 'category', 'party', 'year', 'summary']],
            use_container_width=True,
            column_config={
                "case_id": st.column_config.TextColumn("Case", width="medium"),
                "category": st.column_config.TextColumn("Category", width="small"),
                "party": st.column_config.TextColumn("Cited By", width="small"),
                "year": st.column_config.NumberColumn("Year", width="small"),
                "summary": st.column_config.TextColumn("Summary", width="large")
            }
        )

if __name__ == "__main__":
    main()
