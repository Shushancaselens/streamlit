import streamlit as st
import pandas as pd

# Custom CSS to match the React design
st.markdown("""
<style>
    .main-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #eee;
        margin: 10px 0;
    }
    .evidence-box {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        margin: 5px 0;
        border: 1px solid #eee;
    }
    .category-tag {
        background-color: #f3f4f6;
        padding: 5px 15px;
        border-radius: 15px;
        font-size: 14px;
        color: #4b5563;
    }
    .appellant-color { color: #4F46E5; }
    .respondent-color { color: #E11D48; }
    .evidence-id {
        background-color: #eef2ff;
        color: #4F46E5;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 12px;
        margin-right: 10px;
    }
    .evidence-id-respondent {
        background-color: #fff1f2;
        color: #E11D48;
    }
    .case-law {
        padding: 10px;
        background-color: white;
        border: 1px solid #eee;
        border-radius: 8px;
        margin: 5px 0;
    }
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
    },
    # Add more cases as needed
]

def display_party_arguments(data, party_type):
    """Display arguments for either appellant or respondent"""
    color_class = "appellant-color" if party_type == "appellant" else "respondent-color"
    evidence_class = "" if party_type == "appellant" else "evidence-id-respondent"
    
    st.markdown(f'<h3 class="{color_class}">{party_type.title()}\'s Position</h3>', unsafe_allow_html=True)
    
    # Main Argument
    st.markdown(f'<div class="evidence-box">{data["mainArgument"]}</div>', unsafe_allow_html=True)
    
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
            f'{evidence["desc"]}'
            f'</div>',
            unsafe_allow_html=True
        )
    
    # Case Law
    st.markdown("#### Case Law")
    for case in data["caselaw"]:
        st.markdown(f'<div class="case-law">{case}</div>', unsafe_allow_html=True)

# Page title
st.title("Legal Arguments Comparison")

# Search functionality
search = st.text_input("Search issues, arguments, or evidence...")

# Copy functionality
if st.button("Copy Summary"):
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
        "text/csv"
    )

# Filter arguments based on search
filtered_arguments = argument_data
if search:
    search_lower = search.lower()
    filtered_arguments = [
        arg for arg in argument_data
        if (search_lower in arg["issue"].lower() or
            search_lower in arg["appellant"]["mainArgument"].lower() or
            search_lower in arg["respondent"]["mainArgument"].lower() or
            any(search_lower in detail.lower() for detail in arg["appellant"]["details"]) or
            any(search_lower in detail.lower() for detail in arg["respondent"]["details"]))
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
            display_party_arguments(arg["appellant"], "appellant")
        
        with col2:
            display_party_arguments(arg["respondent"], "respondent")
        
    st.markdown("<hr>", unsafe_allow_html=True)
