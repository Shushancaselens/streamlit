import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* ... (previous styles remain the same) ... */
    .evidence-link {
        color: #4338ca;
        text-decoration: none;
        transition: all 0.2s;
    }
    .evidence-link:hover {
        color: #3730a3;
        text-decoration: underline;
    }
    .evidence-card {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        margin-bottom: 0.5rem;
        transition: all 0.2s;
    }
    .evidence-card:hover {
        border-color: #818cf8;
        background-color: #f5f7ff;
    }
</style>
""", unsafe_allow_html=True)

# Complete argument data
def get_case_summary(case_id):
    # Database of case summaries remains the same
    case_summaries = {
        "CAS 2019/A/XYZ": "Athlete successfully established jurisdiction based on federation rules explicitly allowing CAS appeals. Court emphasized importance of clear arbitration agreements.",
        "CAS 2019/A/123": "Appeal dismissed due to non-exhaustion of internal remedies. CAS emphasized need to follow proper procedural steps.",
        "CAS 2018/A/456": "Case established precedent for requiring completion of federation's internal processes before CAS jurisdiction.",
        "CAS 2018/A/ABC": "Court found chain-of-custody errors significant enough to invalidate test results. Set standards for sample handling.",
        "CAS 2017/A/789": "Minor procedural defects held insufficient to invalidate otherwise valid test results.",
        "Smith v. Corp Inc. 2021": "Court found lack of documented warnings and positive performance reviews inconsistent with termination for cause.",
        "Jones v. Enterprise Ltd 2020": "Established standards for progressive discipline in employment termination cases.",
        "Brown v. MegaCorp 2022": "Upheld immediate termination where serious misconduct was clearly documented.",
        "Wilson v. Tech Solutions 2021": "Court emphasized importance of contemporaneous documentation of verbal warnings.",
        "TechCo v. Innovate Inc. 2022": "Found patent infringement based on post-publication copying and substantial similarity.",
        "Patent Holdings v. StartUp 2021": "Emphasized importance of timeline evidence in patent infringement cases.",
        "Innovation Corp v. PatentCo 2023": "Independent development defense succeeded with clear pre-dating evidence.",
        "Tech Solutions v. IP Holdings 2022": "Court invalidated overly broad patent claims in software industry.",
        "EcoCorp v. EPA 2022": "Facility compliance upheld based on comprehensive monitoring data and third-party audits.",
        "Green Industries v. State 2021": "Established standards for environmental compliance documentation.",
        "EPA v. Industrial Corp 2023": "Violations found due to inadequate monitoring and delayed incident reporting.",
        "State v. Manufacturing Co. 2022": "Court emphasized importance of timely violation reporting and equipment maintenance."
    }
    return case_summaries.get(case_id, "Summary not available.")

# Argument data remains exactly the same
argument_data = [
    # ... (all previous argument data remains unchanged)
]

def create_position_section(position_data, position_type):
    """Create a section for appellant or respondent position"""
    # Function remains exactly the same
    color = "indigo" if position_type == "Appellant" else "rose"
    
    st.subheader(f"{position_type}'s Position")
    
    # Main Argument
    st.markdown(f"""
        <div class="main-argument">
            <strong>{position_data['mainArgument']}</strong>
        </div>
    """, unsafe_allow_html=True)
    
    # Supporting Points
    st.markdown("##### Supporting Points")
    for detail in position_data['details']:
        st.markdown(f"- {detail}")
    
    # Evidence
    st.markdown("##### Evidence")
    for evidence in position_data['evidence']:
        st.markdown(f"""
            <div class="evidence-card">
                <span class="evidence-tag">{evidence['id']}</span>
                <a href="/evidence/{evidence['id']}" class="evidence-link" target="_blank">
                    {evidence['desc']}
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    # Case Law
    st.markdown("##### Case Law")
    for case in position_data['caselaw']:
        summary = get_case_summary(case)
        st.markdown(f"""
            <div class="position-card">
                <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem;">
                    <div style="flex-grow: 1;">
                        <div style="font-weight: 500; color: #4B5563; margin-bottom: 0.5rem;">
                            {case}
                        </div>
                        <div style="font-size: 0.875rem; color: #6B7280;">
                            {summary}
                        </div>
                    </div>
                    <button onclick="navigator.clipboard.writeText('{case}')" 
                            style="background: none; border: none; cursor: pointer; padding: 0.25rem;">
                        📋
                    </button>
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.title("Dashboard Controls")
        
        # Category filter
        categories = list(set(arg["category"] for arg in argument_data))
        selected_categories = st.multiselect(
            "Filter by Category",
            categories,
            default=categories
        )
        
        # Sort options
        sort_option = st.selectbox(
            "Sort By",
            ["Issue", "Category"]
        )
        
        # Display options
        st.subheader("Display Options")
        show_appellant = st.checkbox("Show Appellant", value=True)
        show_respondent = st.checkbox("Show Respondent", value=True)
        expand_all = st.checkbox("Expand All Cases", value=False)
        
        # Statistics
        st.subheader("Statistics")
        total_cases = len(argument_data)
        st.metric("Total Cases", total_cases)
        st.metric("Selected Categories", len(selected_categories))

    # Main content area
    st.title("Legal Arguments Dashboard")
    
    # Search bar and export button in the same row
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        search = st.text_input("", 
                             placeholder="🔍 Search issues, arguments, or evidence...",
                             label_visibility="collapsed")
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
    
    # Filter arguments based on search and selected categories
    filtered_arguments = [
        arg for arg in argument_data
        if arg["category"] in selected_categories
    ]
    
    if search:
        search = search.lower()
        filtered_arguments = [
            arg for arg in filtered_arguments
            if (search in arg['issue'].lower() or
                any(search in detail.lower() for detail in arg['appellant']['details']) or
                any(search in detail.lower() for detail in arg['respondent']['details']) or
                any(search in e['desc'].lower() for e in arg['appellant']['evidence']) or
                any(search in e['desc'].lower() for e in arg['respondent']['evidence']))
        ]
    
    # Sort arguments
    if sort_option == "Category":
        filtered_arguments = sorted(filtered_arguments, key=lambda x: x["category"])
    else:
        filtered_arguments = sorted(filtered_arguments, key=lambda x: x["issue"])
    
    # Display arguments
    for arg in filtered_arguments:
        with st.expander(f"{arg['issue']} ({arg['category']})", expanded=expand_all):
            # Content when expanded
            if show_appellant and show_respondent:
                col1, col2 = st.columns(2)
                with col1:
                    create_position_section(arg['appellant'], "Appellant")
                with col2:
                    create_position_section(arg['respondent'], "Respondent")
            elif show_appellant:
                create_position_section(arg['appellant'], "Appellant")
            elif show_respondent:
                create_position_section(arg['respondent'], "Respondent")
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
