import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        max-width: 1400px;
        padding: 2rem;
        margin: 0 auto;
    }
    .block-container {
        max-width: 1400px;
        padding: 1rem 2rem;
    }
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
    # Database of case summaries
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
    },
    {
        "id": "2",
        "issue": "Presence of Substance X",
        "category": "substance",
        "appellant": {
            "mainArgument": "Chain-of-custody errors invalidate test results",
            "details": [
                "Sample had a 10-hour delay in transfer",
                "Sealing procedure was not properly documented",
                "Independent expert confirms potential degradation"
            ],
            "evidence": [
                {"id": "C4", "desc": "Lab reports #1 and #2"},
                {"id": "C5", "desc": "Expert Dr. A's statement"},
                {"id": "C6", "desc": "Chain of custody documentation"}
            ],
            "caselaw": ["CAS 2018/A/ABC"]
        },
        "respondent": {
            "mainArgument": "Minor procedural defects do not invalidate results",
            "details": [
                "WADA-accredited lab's procedures ensure reliability",
                "10-hour delay within acceptable limits",
                "No evidence of sample degradation"
            ],
            "evidence": [
                {"id": "R4", "desc": "Lab accreditation documents"},
                {"id": "R5", "desc": "Expert Dr. B's analysis"},
                {"id": "R6", "desc": "Testing protocols"}
            ],
            "caselaw": ["CAS 2017/A/789"]
        }
    },
    {
        "id": "3",
        "issue": "Contract Termination Validity",
        "category": "employment",
        "appellant": {
            "mainArgument": "Termination was wrongful and without cause",
            "details": [
                "No prior warnings were issued before termination",
                "Performance reviews were consistently positive",
                "Termination violated company policy on progressive discipline"
            ],
            "evidence": [
                {"id": "C7", "desc": "Employee performance reviews 2020-2023"},
                {"id": "C8", "desc": "Company handbook on disciplinary procedures"},
                {"id": "C9", "desc": "Email correspondence regarding termination"}
            ],
            "caselaw": ["Smith v. Corp Inc. 2021", "Jones v. Enterprise Ltd 2020"]
        },
        "respondent": {
            "mainArgument": "Termination was justified due to misconduct",
            "details": [
                "Multiple instances of policy violations documented",
                "Verbal warnings were given on several occasions",
                "Final incident warranted immediate termination"
            ],
            "evidence": [
                {"id": "R7", "desc": "Internal incident reports"},
                {"id": "R8", "desc": "Witness statements from supervisors"},
                {"id": "R9", "desc": "Security footage from incident date"}
            ],
            "caselaw": ["Brown v. MegaCorp 2022", "Wilson v. Tech Solutions 2021"]
        }
    },
    {
        "id": "4",
        "issue": "Patent Infringement",
        "category": "intellectual property",
        "appellant": {
            "mainArgument": "Defendant's product violates our patent claims",
            "details": [
                "Product uses identical method described in patent claims",
                "Infringement began after patent publication",
                "Similarities cannot be explained by independent development"
            ],
            "evidence": [
                {"id": "C10", "desc": "Patent documentation and claims analysis"},
                {"id": "C11", "desc": "Technical comparison report"},
                {"id": "C12", "desc": "Expert analysis of defendant's product"}
            ],
            "caselaw": ["TechCo v. Innovate Inc. 2022", "Patent Holdings v. StartUp 2021"]
        },
        "respondent": {
            "mainArgument": "Our technology was independently developed",
            "details": [
                "Development began before patent filing date",
                "Technology uses different underlying mechanism",
                "Patent claims are overly broad and invalid"
            ],
            "evidence": [
                {"id": "R10", "desc": "Development timeline documentation"},
                {"id": "R11", "desc": "Prior art examples"},
                {"id": "R12", "desc": "Technical differentiation analysis"}
            ],
            "caselaw": ["Innovation Corp v. PatentCo 2023", "Tech Solutions v. IP Holdings 2022"]
        }
    },
    {
        "id": "5",
        "issue": "Environmental Compliance",
        "category": "regulatory",
        "appellant": {
            "mainArgument": "Facility meets all environmental standards",
            "details": [
                "All required permits were obtained and maintained",
                "Emissions consistently below regulatory limits",
                "Regular maintenance and monitoring conducted"
            ],
            "evidence": [
                {"id": "C13", "desc": "Environmental impact assessments"},
                {"id": "C14", "desc": "Continuous monitoring data 2021-2023"},
                {"id": "C15", "desc": "Third-party compliance audit reports"}
            ],
            "caselaw": ["EcoCorp v. EPA 2022", "Green Industries v. State 2021"]
        },
        "respondent": {
            "mainArgument": "Significant violations of environmental regulations",
            "details": [
                "Multiple instances of excess emissions recorded",
                "Required monitoring equipment malfunctioned",
                "Failure to report incidents within required timeframe"
            ],
            "evidence": [
                {"id": "R13", "desc": "Violation notices and citations"},
                {"id": "R14", "desc": "Inspector field reports"},
                {"id": "R15", "desc": "Community complaint records"}
            ],
            "caselaw": ["EPA v. Industrial Corp 2023", "State v. Manufacturing Co. 2022"]
        }
    }
]

def create_position_section(position_data, position_type):
    """Create a section for appellant or respondent position"""
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
    
    # Display arguments
    for arg in filtered_arguments:
        with st.expander(f"{arg['issue']} {arg['category']}", expanded=arg['id'] == '1'):
            # Content when expanded
            col1, col2 = st.columns(2)
            with col1:
                create_position_section(arg['appellant'], "Appellant")
            with col2:
                create_position_section(arg['respondent'], "Respondent")
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
