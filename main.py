import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Legal Arguments Comparison", layout="wide", initial_sidebar_state="collapsed")

# CSS Styling
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .main-card {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        margin: 16px 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
    }
    /* Combined title and argument styling */
    .evidence-box {
        background-color: #f8fafc;
        padding: 16px;
        border-radius: 12px;
        margin: 8px 0;
        border: 1px solid #e2e8f0;
    }
    .main-argument {
        margin-top: 8px;
        font-size: 1.1rem;
    }
    h3 {
        margin: 0 !important;
        padding: 0 !important;
    }
    .category-tag {
        background-color: #f1f5f9;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.875rem;
        color: #475569;
        font-weight: 500;
        margin-left: 12px;
    }
    .appellant-color { color: #4338ca !important; }
    .respondent-color { color: #be123c !important; }
    .evidence-id {
        background-color: #e0e7ff;
        color: #4338ca;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 12px;
    }
    .evidence-id-respondent {
        background-color: #ffe4e6;
        color: #be123c;
    }
    .case-law {
        padding: 14px;
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        margin: 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# Data
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

def display_party_section(data, party_type):
    color_class = "appellant-color" if party_type == "appellant" else "respondent-color"
    evidence_class = "" if party_type == "appellant" else "evidence-id-respondent"
    
    # Combine title and main argument in one container
    st.markdown(f"""
        <div class="evidence-box">
            <h3 class="{color_class}">{party_type.title()}'s Position</h3>
            <div class="main-argument"><strong>{data["mainArgument"]}</strong></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Key Arguments
    st.markdown("#### Key Arguments")
    for detail in data["details"]:
        st.markdown(f'<div class="evidence-box">{detail}</div>', unsafe_allow_html=True)
    
    # Evidence
    st.markdown("#### Evidence")
    for evidence in data["evidence"]:
        st.markdown(
            f'<div class="evidence-box">'
            f'<span class="evidence-id {evidence_class}">{evidence["id"]}</span>'
            f'{evidence["desc"]}</div>',
            unsafe_allow_html=True
        )
    
    # Case Law
    st.markdown("#### Case Law")
    for case in data["caselaw"]:
        st.markdown(f'<div class="case-law">{case}</div>', unsafe_allow_html=True)

# Page Header
st.markdown('<h1>Legal Arguments Comparison</h1>', unsafe_allow_html=True)

# Search and Export
col1, col2 = st.columns([9, 1])
with col1:
    search = st.text_input("", placeholder="Search issues, arguments, or evidence...")
with col1:
    if st.button("Export Summary"):
        df = pd.DataFrame([{
            "Issue": arg["issue"],
            "Appellant Position": arg["appellant"]["mainArgument"],
            "Respondent Position": arg["respondent"]["mainArgument"]
        } for arg in argument_data])
        st.download_button(
            "📥 Download CSV",
            df.to_csv(index=False),
            "legal_arguments_summary.csv",
            "text/csv"
        )

# Filter arguments based on search
filtered_arguments = [
    arg for arg in argument_data
    if not search or any(
        search.lower() in str(value).lower()
        for value in [
            arg["issue"],
            arg["appellant"]["mainArgument"],
            arg["respondent"]["mainArgument"],
            *arg["appellant"]["details"],
            *arg["respondent"]["details"],
            *[e["desc"] for e in arg["appellant"]["evidence"]],
            *[e["desc"] for e in arg["respondent"]["evidence"]]
        ]
    )
]

# Display arguments
for arg in filtered_arguments:
    st.markdown(f"""
        <div class="main-card">
            <h2>{arg["issue"]} <span class="category-tag">{arg["category"]}</span></h2>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("View Details", expanded=arg["id"] == "1"):
        col1, col2 = st.columns(2)
        with col1:
            display_party_section(arg["appellant"], "appellant")
        with col2:
            display_party_section(arg["respondent"], "respondent")
    
    st.markdown("<hr>", unsafe_allow_html=True)
