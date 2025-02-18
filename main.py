import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Legal Arguments Comparison", layout="wide", initial_sidebar_state="collapsed")

# CSS
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .main-container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
    .main-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #e2e8f0;
        margin: 1rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .evidence-box {
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 0.75rem;
        margin: 0.5rem 0;
        border: 1px solid #e2e8f0;
    }
    .category-tag {
        background-color: #f1f5f9;
        padding: 0.375rem 1rem;
        border-radius: 1.25rem;
        font-size: 0.875rem;
        color: #475569;
        font-weight: 500;
        margin-left: 0.75rem;
    }
    .position-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .appellant-color { color: #4338ca; }
    .respondent-color { color: #be123c; }
    .evidence-id {
        background-color: #e0e7ff;
        color: #4338ca;
        padding: 0.25rem 0.625rem;
        border-radius: 0.5rem;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.75rem;
        display: inline-block;
    }
    .evidence-id-respondent {
        background-color: #ffe4e6;
        color: #be123c;
    }
    .case-law {
        padding: 0.875rem;
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 0.75rem;
        margin: 0.5rem 0;
    }
    .section-title {
        color: #64748b;
        font-size: 0.875rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 1.5rem 0 0.75rem 0;
    }
    button[kind="secondary"] {
        background-color: #e0e7ff !important;
        color: #4338ca !important;
        border-radius: 0.75rem !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
    }
    .stTextInput > div > div > input {
        background-color: white;
        padding: 0.75rem !important;
        border-radius: 0.75rem !important;
        border: 1px solid #e2e8f0 !important;
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
    }
]

def display_party_section(data, party_type):
    color_class = "appellant-color" if party_type == "appellant" else "respondent-color"
    evidence_class = "" if party_type == "appellant" else "evidence-id-respondent"
    
    # Title and Main Argument Combined
    st.markdown(
        f'''
        <div class="evidence-box">
            <div class="position-title {color_class}">{party_type.title()}'s Position</div>
            <div><strong>{data["mainArgument"]}</strong></div>
        </div>
        ''', 
        unsafe_allow_html=True
    )
    
    # Key Arguments
    st.markdown('<div class="section-title">Key Arguments</div>', unsafe_allow_html=True)
    for detail in data["details"]:
        st.markdown(f'<div class="evidence-box">{detail}</div>', unsafe_allow_html=True)
    
    # Evidence
    st.markdown('<div class="section-title">Evidence</div>', unsafe_allow_html=True)
    for evidence in data["evidence"]:
        st.markdown(
            f'<div class="evidence-box">'
            f'<span class="evidence-id {evidence_class}">{evidence["id"]}</span>'
            f'{evidence["desc"]}</div>',
            unsafe_allow_html=True
        )
    
    # Case Law
    st.markdown('<div class="section-title">Case Law</div>', unsafe_allow_html=True)
    for case in data["caselaw"]:
        st.markdown(f'<div class="case-law">{case}</div>', unsafe_allow_html=True)

# Main Application
st.markdown('<h1 style="margin-bottom: 2rem;">Legal Arguments Comparison</h1>', unsafe_allow_html=True)

# Search and Export
col1, col2 = st.columns([3, 1])
with col1:
    search = st.text_input("", placeholder="Search issues, arguments, or evidence...")
with col2:
    if st.button("Export Summary", type="secondary"):
        df = pd.DataFrame([{
            "Issue": arg["issue"],
            "Appellant Position": arg["appellant"]["mainArgument"],
            "Respondent Position": arg["respondent"]["mainArgument"]
        } for arg in argument_data])
        st.download_button(
            "📥 Download CSV",
            df.to_csv(index=False),
            "legal_arguments_summary.csv",
            "text/csv",
            type="secondary"
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
            <h2 style="margin: 0; font-size: 1.5rem; font-weight: 600; color: #1e293b;">
                {arg["issue"]} 
                <span class="category-tag">{arg["category"]}</span>
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("View Details", expanded=arg["id"] == "1"):
        col1, col2 = st.columns(2)
        with col1:
            display_party_section(arg["appellant"], "appellant")
        with col2:
            display_party_section(arg["respondent"], "respondent")
