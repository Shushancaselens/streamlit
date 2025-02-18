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

# Case summaries dictionary
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

# Argument data
argument_data = [
    {
        "id": "1",
        "issue": "CAS Jurisdiction",
        "category": "jurisdiction",
        "appellant": {
            "mainArgument": "CAS Has Authority to Hear This Case",
            "details": [
                "The Federation's Anti-Doping Rules explicitly allow CAS to hear appeals",
                "Athlete has completed all required internal appeal procedures first",
                "Athlete signed agreement allowing CAS to handle disputes"
            ],
            "evidence": [
                {"id": "C1", "desc": "Federation Rules, Art. 60"},
                {"id": "C2", "desc": "Athlete's license containing arbitration agreement"},
                {"id": "C3", "desc": "Appeal submission documents"}
            ],
            "caselaw": ["CAS 2019/A/XYZ"]
        },
        "respondent": {
            "mainArgument": "CAS Cannot Hear This Case Yet",
            "details": [
                "Athlete skipped required steps in federation's appeal process",
                "Athlete missed important appeal deadlines within federation",
                "Must follow proper appeal steps before going to CAS"
            ],
            "evidence": [
                {"id": "R1", "desc": "Federation internal appeals process documentation"},
                {"id": "R2", "desc": "Timeline of appeals process"},
                {"id": "R3", "desc": "Federation handbook on procedures"}
            ],
            "caselaw": ["CAS 2019/A/123", "CAS 2018/A/456"]
        }
    }
]

def create_table_data():
    """Convert argument data into a format suitable for a table"""
    rows = []
    for arg in argument_data:
        # Format details with bullet points
        appellant_details = "\n".join([f"• {detail}" for detail in arg['appellant']['details']])
        appellant_evidence = "\n".join([f"{e['id']}: {e['desc']}" for e in arg['appellant']['evidence']])
        appellant_cases = "\n".join([f"{case}\n{get_case_summary(case)}" for case in arg['appellant']['caselaw']])
        
        respondent_details = "\n".join([f"• {detail}" for detail in arg['respondent']['details']])
        respondent_evidence = "\n".join([f"{e['id']}: {e['desc']}" for e in arg['respondent']['evidence']])
        respondent_cases = "\n".join([f"{case}\n{get_case_summary(case)}" for case in arg['respondent']['caselaw']])
        
        row = {
            "issue": f"{arg['issue']} ({arg['category']})",
            "appellant_position": arg['appellant']['mainArgument'],
            "appellant_details": appellant_details,
            "appellant_evidence": appellant_evidence,
            "appellant_cases": appellant_cases,
            "respondent_position": arg['respondent']['mainArgument'],
            "respondent_details": respondent_details,
            "respondent_evidence": respondent_evidence,
            "respondent_cases": respondent_cases
        }
        rows.append(row)
    
    return pd.DataFrame(rows)

def main():
    # Add sidebar with logo and info
    with st.sidebar:
        # Add the logo SVG
        st.markdown("""
        <svg width="40" height="40" viewBox="0 0 175 175" xmlns="http://www.w3.org/2000/svg">
          <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
            <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
          </mask>
          <g mask="url(#whatsapp-mask)">
            <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
          </g>
        </svg>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.info(
            """
            This dashboard displays legal arguments and related case law.
            """
        )

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

if __name__ == "__main__":
    main()
