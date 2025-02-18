import streamlit as st
import pandas as pd
from datetime import datetime

# Configure the page
st.set_page_config(layout="wide", page_title="Legal Arguments Comparison")

# Hide Streamlit's default styles
st.markdown("""
    <style>
        /* Hide hamburger menu */
        #MainMenu {visibility: hidden;}
        
        /* Hide footer */
        footer {visibility: hidden;}
        
        /* Hide default header */
        header {visibility: hidden;}
        
        /* Remove padding */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
        }
        
        /* Remove default streamlit spacing */
        .stButton>button {
            margin: 0;
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            background-color: white !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 1rem !important;
            margin-bottom: 0.5rem !important;
        }
        .streamlit-expanderHeader:hover {
            background-color: #f9fafb !important;
        }
        .streamlit-expanderContent {
            border: none !important;
            background-color: white !important;
        }
        
        /* Custom Container */
        .custom-container {
            background: white;
            border-radius: 1rem;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid #e5e7eb;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        /* Search styling */
        .search-wrapper {
            position: relative;
            margin-bottom: 1.5rem;
        }
        .search-icon {
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            color: #9ca3af;
        }
        .stTextInput>div>div>input {
            padding-left: 3rem !important;
            height: 3rem !important;
            border-radius: 0.75rem !important;
            border-color: #e5e7eb !important;
            font-size: 0.875rem !important;
        }
        .stTextInput>div>div>input:focus {
            box-shadow: 0 0 0 2px #818cf8 !important;
            border-color: transparent !important;
        }
        
        /* Evidence styling */
        .evidence-link {
            display: block;
            padding: 0.75rem;
            border-radius: 0.75rem;
            border: 1px solid #e5e7eb;
            margin-bottom: 0.5rem;
            text-decoration: none;
            color: #111827;
            transition: all 0.2s;
        }
        .evidence-link:hover {
            border-color: #818cf8;
            background-color: #eef2ff;
            color: #4f46e5;
        }
        .evidence-id {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 0.5rem;
            font-size: 0.75rem;
            font-weight: 500;
            margin-right: 0.5rem;
        }
        .evidence-id.appellant {
            background-color: #eef2ff;
            color: #4f46e5;
        }
        .evidence-id.respondent {
            background-color: #fef2f2;
            color: #e11d48;
        }
        
        /* Main argument styling */
        .main-argument {
            background-color: #f9fafb;
            padding: 1rem;
            border-radius: 0.75rem;
            margin-bottom: 1rem;
            font-weight: 500;
        }
        
        /* Details list styling */
        .details-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .details-list li {
            display: flex;
            align-items: flex-start;
            margin-bottom: 0.5rem;
            color: #4b5563;
        }
        .details-list li::before {
            content: "";
            display: inline-block;
            width: 0.375rem;
            height: 0.375rem;
            border-radius: 50%;
            background-color: #9ca3af;
            margin-top: 0.5rem;
            margin-right: 0.75rem;
            flex-shrink: 0;
        }
        
        /* Section headers */
        .section-header {
            font-size: 0.875rem;
            font-weight: 500;
            color: #6b7280;
            margin: 1rem 0 0.5rem 0;
        }
        
        /* Case law styling */
        .case-law-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem;
            border-radius: 0.75rem;
            border: 1px solid #e5e7eb;
            margin-bottom: 0.5rem;
            color: #4b5563;
        }
        
        /* Category tag */
        .category-tag {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: #f3f4f6;
            color: #6b7280;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 500;
            margin-left: 0.75rem;
        }
        
        /* Position headers */
        .position-header {
            font-size: 1.125rem;
            font-weight: 500;
            margin-bottom: 1rem;
        }
        .position-header.appellant {
            color: #4f46e5;
        }
        .position-header.respondent {
            color: #e11d48;
        }
    </style>
""", unsafe_allow_html=True)

# Search icon SVG
search_icon = """
<div class="search-icon">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" 
         stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
    </svg>
</div>
"""

# Add search icon
st.markdown(search_icon, unsafe_allow_html=True)

# Search input
search = st.text_input("", placeholder="Search issues, arguments, or evidence...", 
                      label_visibility="collapsed")

# Define argument data
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

def render_argument_section(position_data, position_type):
    color_class = "appellant" if position_type == "Appellant" else "respondent"
    
    st.markdown(f"""
        <div class="position-header {color_class.lower()}">{position_type}'s Position</div>
        <div class="main-argument">{position_data['mainArgument']}</div>
        
        <div class="section-header">Supporting Points</div>
        <ul class="details-list">
            {''.join(f'<li>{detail}</li>' for detail in position_data['details'])}
        </ul>
        
        <div class="section-header">Evidence</div>
        {''.join(f'''
            <a href="#" class="evidence-link">
                <span class="evidence-id {color_class.lower()}">{evidence['id']}</span>
                {evidence['desc']}
            </a>
        ''' for evidence in position_data['evidence'])}
        
        <div class="section-header">Case Law</div>
        {''.join(f'''
            <div class="case-law-item">
                <span>{case}</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" 
                     fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" 
                     stroke-linejoin="round" class="copy-icon">
                    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                    <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                </svg>
            </div>
        ''' for case in position_data['caselaw'])}
    """, unsafe_allow_html=True)

# Display arguments
for arg in argument_data:
    with st.expander(f"{arg['issue']} ({arg['category']})"):
        cols = st.columns(2)
        with cols[0]:
            render_argument_section(arg['appellant'], "Appellant")
        with cols[1]:
            render_argument_section(arg['respondent'], "Respondent")
