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
def get_case_law_evidence():
    # Database of case law evidence with summaries
    return {
        "CAS 2019/A/XYZ": {
            "summary": "Athlete successfully established jurisdiction based on federation rules explicitly allowing CAS appeals. Court emphasized importance of clear arbitration agreements.",
            "key_evidence": [
                "Federation rules explicitly permitting CAS appeals",
                "Signed arbitration agreement",
                "Complete internal appeals documentation"
            ],
            "key_holdings": [
                "Clear arbitration agreements are enforceable",
                "Federation rules can establish CAS jurisdiction",
                "Proper documentation of consent is crucial"
            ]
        },
        "CAS 2019/A/123": {
            "summary": "Appeal dismissed due to non-exhaustion of internal remedies. CAS emphasized need to follow proper procedural steps.",
            "key_evidence": [
                "Internal appeal procedures documentation",
                "Timeline of appeal process",
                "Federation correspondence"
            ],
            "key_holdings": [
                "Internal remedies must be exhausted",
                "Procedural requirements are mandatory",
                "Timing of appeals is critical"
            ]
        },
        "CAS 2018/A/456": {
            "summary": "Case established precedent for requiring completion of federation's internal processes before CAS jurisdiction.",
            "key_evidence": [
                "Federation's appeal process documentation",
                "Athlete's appeal history",
                "Expert testimony on procedures"
            ],
            "key_holdings": [
                "Federation processes must be completed",
                "Exceptions require extraordinary circumstances",
                "Burden of proof on appellant"
            ]
        },
        "CAS 2018/A/ABC": {
            "summary": "Court found chain-of-custody errors significant enough to invalidate test results. Set standards for sample handling.",
            "key_evidence": [
                "Chain of custody documentation",
                "Laboratory handling procedures",
                "Expert testimony on sample degradation"
            ],
            "key_holdings": [
                "Proper chain of custody is essential",
                "Documentation gaps can invalidate results",
                "Expert testimony heavily weighted"
            ]
        },
        "CAS 2017/A/789": {
            "summary": "Minor procedural defects held insufficient to invalidate otherwise valid test results.",
            "key_evidence": [
                "Laboratory accreditation documents",
                "Test result documentation",
                "Expert analysis of procedures"
            ],
            "key_holdings": [
                "Minor defects don't invalidate results",
                "Overall reliability is key factor",
                "Substantial compliance sufficient"
            ]
        }
    }

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
    
    # Evidence with Case Law Summary
    st.markdown("##### Evidence")
    for evidence in position_data['evidence']:
        # Get related case law summaries
        related_cases = []
        case_law_evidence = get_case_law_evidence()
        for case in position_data['caselaw']:
            if case in case_law_evidence:
                case_evidence = case_law_evidence[case]
                # Check if this evidence is mentioned in the case's key evidence
                if any(evidence['desc'].lower() in key_ev.lower() for key_ev in case_evidence['key_evidence']):
                    related_cases.append({
                        'citation': case,
                        'summary': case_evidence['summary'],
                        'relevant_holding': next((holding for holding in case_evidence['key_holdings'] 
                                               if evidence['desc'].lower() in holding.lower()), 
                                              case_evidence['key_holdings'][0])
                    })
        
        st.markdown(f"""
            <div class="evidence-card">
                <div style="display: flex; flex-direction: column; width: 100%;">
                    <div style="display: flex; gap: 0.75rem; align-items: center; margin-bottom: 0.5rem;">
                        <span class="evidence-tag">{evidence['id']}</span>
                        <a href="/evidence/{evidence['id']}" class="evidence-link" target="_blank">
                            {evidence['desc']}
                        </a>
                    </div>
                    {f'''
                    <div style="margin-top: 0.5rem; padding-top: 0.5rem; border-top: 1px solid #e5e7eb;">
                        <div style="font-weight: 500; color: #4B5563; margin-bottom: 0.5rem;">
                            Related Case Law:
                        </div>
                        {"".join(f"""
                            <div style="margin-bottom: 0.5rem; padding-left: 0.5rem; border-left: 2px solid #e5e7eb;">
                                <div style="font-weight: 500; color: #6B7280; font-size: 0.875rem;">
                                    {case['citation']}
                                </div>
                                <div style="color: #6B7280; font-size: 0.875rem; margin-top: 0.25rem;">
                                    {case['summary']}
                                </div>
                                <div style="color: #4B5563; font-size: 0.875rem; margin-top: 0.25rem;">
                                    <strong>Relevant Holding:</strong> {case['relevant_holding']}
                                </div>
                            </div>
                        """ for case in related_cases)}
                    </div>
                    ''' if related_cases else ''}
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Case Law
    st.markdown("##### Case Law")
    case_law_evidence = get_case_law_evidence()
    
    for case in position_data['caselaw']:
        if case in case_law_evidence:
            evidence = case_law_evidence[case]
            st.markdown(f"""
                <div class="position-card">
                    <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem;">
                        <div style="flex-grow: 1;">
                            <div style="font-weight: 500; color: #4B5563; margin-bottom: 0.5rem;">
                                {case}
                            </div>
                            <div style="font-size: 0.875rem; color: #6B7280; margin-bottom: 0.5rem;">
                                {evidence['summary']}
                            </div>
                            <div style="margin-top: 1rem;">
                                <div style="font-weight: 500; color: #4B5563; margin-bottom: 0.5rem;">
                                    Key Evidence:
                                </div>
                                <ul style="list-style-type: disc; margin-left: 1.5rem; font-size: 0.875rem; color: #6B7280;">
                                    {"".join(f'<li>{item}</li>' for item in evidence['key_evidence'])}
                                </ul>
                            </div>
                            <div style="margin-top: 1rem;">
                                <div style="font-weight: 500; color: #4B5563; margin-bottom: 0.5rem;">
                                    Key Holdings:
                                </div>
                                <ul style="list-style-type: disc; margin-left: 1.5rem; font-size: 0.875rem; color: #6B7280;">
                                    {"".join(f'<li>{item}</li>' for item in evidence['key_holdings'])}
                                </ul>
                            </div>
                        </div>
                        <button onclick="navigator.clipboard.writeText('{case}')" 
                                style="background: none; border: none; cursor: pointer; padding: 0.25rem;">
                            📋
                        </button>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
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
        st.title("Filters")
        
        # Category filter
        categories = list(set(arg["category"] for arg in argument_data))
        selected_categories = st.multiselect(
            "Select Categories",
            categories,
            default=categories
        )
        
        # Party filter
        party_filter = st.radio(
            "View Arguments By",
            ["All", "Appellant Only", "Respondent Only"]
        )
        
        # Date range
        st.markdown("### Case Law Date Range")
        min_year = 2017
        max_year = 2023
        year_range = st.slider(
            "Select Years",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year)
        )
        
        # Statistics
        st.markdown("### Quick Stats")
        st.markdown(f"**Total Cases:** {len(argument_data)}")
        st.markdown(f"**Total Evidence Items:** {sum(len(arg['appellant']['evidence']) + len(arg['respondent']['evidence']) for arg in argument_data)}")
        st.markdown(f"**Total Case Laws Cited:** {sum(len(arg['appellant']['caselaw']) + len(arg['respondent']['caselaw']) for arg in argument_data)}")
        
        # Export options
        st.markdown("### Export Options")
        export_format = st.selectbox(
            "Export Format",
            ["CSV", "Excel", "PDF"]
        )
        if st.button("Export Data", type="primary"):
            st.write(f"Exporting in {export_format} format...")

    # Main content
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
    
    # Filter arguments based on sidebar selections and search
    filtered_arguments = argument_data
    
    # Category filter
    filtered_arguments = [
        arg for arg in filtered_arguments
        if arg['category'] in selected_categories
    ]
    
    # Party filter
    if party_filter == "Appellant Only":
        for arg in filtered_arguments:
            arg['respondent']['details'] = []
            arg['respondent']['evidence'] = []
            arg['respondent']['caselaw'] = []
    elif party_filter == "Respondent Only":
        for arg in filtered_arguments:
            arg['appellant']['details'] = []
            arg['appellant']['evidence'] = []
            arg['appellant']['caselaw'] = []
    
    # Case law year filter
    def get_case_year(case):
        try:
            return int(case.split()[-1])
        except:
            return 0
    
    filtered_arguments = [
        {**arg,
         'appellant': {
             **arg['appellant'],
             'caselaw': [case for case in arg['appellant']['caselaw']
                        if year_range[0] <= get_case_year(case) <= year_range[1]]
         },
         'respondent': {
             **arg['respondent'],
             'caselaw': [case for case in arg['respondent']['caselaw']
                        if year_range[0] <= get_case_year(case) <= year_range[1]]
         }}
        for arg in filtered_arguments
    ]
    
    # Search filter
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
