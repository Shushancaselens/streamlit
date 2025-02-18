import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Legal Arguments Comparison", layout="wide", initial_sidebar_state="collapsed")

# CSS Styling
st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
    }
    .main-card {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        margin: 16px 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
    }
    .main-card:hover {
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .evidence-box {
        background-color: #f8fafc;
        padding: 16px;
        border-radius: 12px;
        margin: 8px 0;
        border: 1px solid #e2e8f0;
        transition: all 0.2s ease;
    }
    .evidence-box:hover {
        border-color: #cbd5e1;
        background-color: #fff;
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
        transition: all 0.2s ease;
    }
    .stTextInput > div > div > input {
        background-color: white;
        padding: 16px !important;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
    }
    .stButton button {
        background-color: #e0e7ff !important;
        color: #4338ca !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
    }
    h1, h2, h3, h4 { font-weight: 600 !important; }
</style>
""", unsafe_allow_html=True)

# Data structure
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

def display_party_section(data, party_type):
    color_class = "appellant-color" if party_type == "appellant" else "respondent-color"
    evidence_class = "" if party_type == "appellant" else "evidence-id-respondent"
    
    st.markdown(f'<h3 class="{color_class}">{party_type.title()}\'s Position</h3>', unsafe_allow_html=True)
    
    # Main Argument
    st.markdown(f'<div class="evidence-box"><strong>{data["mainArgument"]}</strong></div>', unsafe_allow_html=True)
    
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
col1, col2 = st.columns([3, 1])
with col1:
    search = st.text_input("", placeholder="Search issues, arguments, or evidence...")
with col2:
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
