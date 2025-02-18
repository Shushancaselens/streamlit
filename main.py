import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .stTable {
        font-size: 14px;
    }
    .evidence-tag {
        background-color: #E5E7EB;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 12px;
        color: #4B5563;
    }
    .main-argument {
        font-weight: 500;
        color: #1F2937;
    }
    .details-cell {
        color: #4B5563;
    }
    .evidence-cell {
        color: #4338CA;
    }
    .case-cell {
        color: #1F2937;
    }
</style>
""", unsafe_allow_html=True)

# Reuse the case_summaries and argument_data from the previous version
def get_case_summary(case_id):
    # Database of case summaries (same as before)
    case_summaries = {
        "CAS 2019/A/XYZ": "Athlete successfully established jurisdiction based on federation rules explicitly allowing CAS appeals. Court emphasized importance of clear arbitration agreements.",
        "CAS 2019/A/123": "Appeal dismissed due to non-exhaustion of internal remedies. CAS emphasized need to follow proper procedural steps.",
        # ... (rest of the case summaries)
    }
    return case_summaries.get(case_id, "Summary not available.")

# Reuse argument_data from previous version
argument_data = [
    # ... (same argument data as before)
]

def create_table_data():
    """Convert argument data into a format suitable for a table"""
    table_data = []
    for arg in argument_data:
        # Appellant details
        appellant_details = "\n".join([f"• {detail}" for detail in arg['appellant']['details']])
        appellant_evidence = "\n".join([f"{e['id']}: {e['desc']}" for e in arg['appellant']['evidence']])
        appellant_cases = "\n".join([f"{case}\n{get_case_summary(case)}" for case in arg['appellant']['caselaw']])
        
        # Respondent details
        respondent_details = "\n".join([f"• {detail}" for detail in arg['respondent']['details']])
        respondent_evidence = "\n".join([f"{e['id']}: {e['desc']}" for e in arg['respondent']['evidence']])
        respondent_cases = "\n".join([f"{case}\n{get_case_summary(case)}" for case in arg['respondent']['caselaw']])
        
        table_data.append({
            "Issue": f"{arg['issue']} ({arg['category']})",
            "Appellant Position": arg['appellant']['mainArgument'],
            "Appellant Details": appellant_details,
            "Appellant Evidence": appellant_evidence,
            "Appellant Case Law": appellant_cases,
            "Respondent Position": arg['respondent']['mainArgument'],
            "Respondent Details": respondent_details,
            "Respondent Evidence": respondent_evidence,
            "Respondent Case Law": respondent_cases
        })
    
    return pd.DataFrame(table_data)

def main():
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
        summary_df = df[["Issue", "Appellant Position", "Respondent Position"]]
        st.dataframe(
            summary_df,
            use_container_width=True,
            column_config={
                "Issue": st.column_config.TextColumn("Issue", width="medium"),
                "Appellant Position": st.column_config.TextColumn("Appellant Position", width="large"),
                "Respondent Position": st.column_config.TextColumn("Respondent Position", width="large")
            }
        )
    else:
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "Issue": st.column_config.TextColumn("Issue", width="medium"),
                "Appellant Position": st.column_config.TextColumn("Appellant Position", width="large"),
                "Appellant Details": st.column_config.TextColumn("Appellant Details", width="large"),
                "Appellant Evidence": st.column_config.TextColumn("Appellant Evidence", width="large"),
                "Appellant Case Law": st.column_config.TextColumn("Appellant Case Law", width="large"),
                "Respondent Position": st.column_config.TextColumn("Respondent Position", width="large"),
                "Respondent Details": st.column_config.TextColumn("Respondent Details", width="large"),
                "Respondent Evidence": st.column_config.TextColumn("Respondent Evidence", width="large"),
                "Respondent Case Law": st.column_config.TextColumn("Respondent Case Law", width="large")
            }
        )

if __name__ == "__main__":
    main()
