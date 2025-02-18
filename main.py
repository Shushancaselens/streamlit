import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .table-cell {
        padding: 0.75rem;
        border: 1px solid #e5e7eb;
    }
    .evidence-tag {
        background-color: #EEF2FF;
        color: #4338CA;
        padding: 0.25rem 0.5rem;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        margin-right: 0.5rem;
    }
    .case-citation {
        color: #4338CA;
        text-decoration: none;
        cursor: pointer;
    }
    .case-citation:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Reuse the case summary function and argument data from the previous version
def get_case_summary(case_id):
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

# Create a function to format evidence for table display
def format_evidence(evidence_list):
    return ", ".join([f'<span class="evidence-tag">{e["id"]}</span>{e["desc"]}' for e in evidence_list])

# Create a function to format case law with tooltips
def format_case_law(cases):
    formatted_cases = []
    for case in cases:
        summary = get_case_summary(case)
        formatted_cases.append(f'<span class="case-citation" title="{summary}">{case}</span>')
    return ", ".join(formatted_cases)

def create_table_view(filtered_arguments):
    """Create a table view of the legal arguments"""
    # Create DataFrame for table view
    table_data = []
    for arg in filtered_arguments:
        row = {
            "Issue": f"{arg['issue']} ({arg['category']})",
            "Party": "Appellant",
            "Main Argument": arg['appellant']['mainArgument'],
            "Supporting Points": "<br>".join([f"• {point}" for point in arg['appellant']['details']]),
            "Evidence": format_evidence(arg['appellant']['evidence']),
            "Case Law": format_case_law(arg['appellant']['caselaw'])
        }
        table_data.append(row)
        
        # Add respondent row
        row = {
            "Issue": f"{arg['issue']} ({arg['category']})",
            "Party": "Respondent",
            "Main Argument": arg['respondent']['mainArgument'],
            "Supporting Points": "<br>".join([f"• {point}" for point in arg['respondent']['details']]),
            "Evidence": format_evidence(arg['respondent']['evidence']),
            "Case Law": format_case_law(arg['respondent']['caselaw'])
        }
        table_data.append(row)
    
    # Convert to DataFrame
    df = pd.DataFrame(table_data)
    
    # Display table using st.write with HTML formatting
    st.write(
        df.style.format({
            'Supporting Points': lambda x: x,
            'Evidence': lambda x: x,
            'Case Law': lambda x: x
        })
        .set_properties(**{
            'text-align': 'left',
            'white-space': 'pre-wrap',
            'padding': '10px'
        })
        .hide_index()
        .to_html(escape=False, index=False),
        unsafe_allow_html=True
    )

def main():
    st.title("Legal Arguments Dashboard - Table View")
    
    # Add view toggle
    view_type = st.radio("Select View", ["Table View", "Card View"], horizontal=True)
    
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
    
    # Filter arguments based on search
    filtered_arguments = argument_data
    if search:
        search = search.lower()
        filtered_arguments = [
            arg for arg in argument_data
            if (search in arg['issue'].lower() or
                any(search in detail.lower() for detail in arg['appellant']['details']) or
                any(search in detail.lower() for detail in arg['respondent']['details']) or
                any(search in e['desc'].lower() for e in arg['appellant']['evidence']) or
                any(search in e['desc'].lower() for e in arg['respondent']['evidence']))
        ]
    
    if view_type == "Table View":
        create_table_view(filtered_arguments)
    else:
        # Display card view (reuse the original card view code)
        for arg in filtered_arguments:
            with st.expander(f"{arg['issue']} {arg['category']}", expanded=arg['id'] == '1'):
                col1, col2 = st.columns(2)
                with col1:
                    create_position_section(arg['appellant'], "Appellant")
                with col2:
                    create_position_section(arg['respondent'], "Respondent")
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
