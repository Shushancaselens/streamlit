import streamlit as st
import pandas as pd
from datetime import datetime

# Configure page settings
st.set_page_config(
    page_title="Legal Arguments Comparison",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px;
        border-radius: 4px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #E8F0FE;
    }
    .evidence-box {
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #E0E0E0;
        margin: 4px 0;
    }
    .evidence-box:hover {
        background-color: #F8F9FA;
        border-color: #6C63FF;
    }
    .case-badge {
        background-color: #F3F4F6;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

# Sample data
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
    # Add more cases here...
]

def display_evidence(evidence_list, color):
    for item in evidence_list:
        st.markdown(
            f"""
            <div class="evidence-box" style="border-left: 4px solid {color}">
                <strong style="color: {color}">{item['id']}</strong><br/>
                {item['desc']}
            </div>
            """,
            unsafe_allow_html=True
        )

def display_case_law(cases, color):
    for case in cases:
        st.markdown(
            f"""
            <div class="case-badge" style="color: {color}">
                {case} 📋
            </div>
            """,
            unsafe_allow_html=True
        )

# App header
st.title("⚖️ Legal Arguments Comparison")

# Search functionality
search = st.text_input("🔍 Search issues, arguments, or evidence...", "")

# Filter data based on search
if search:
    filtered_data = [
        arg for arg in argument_data
        if (search.lower() in arg["issue"].lower() or
            search.lower() in arg["appellant"]["mainArgument"].lower() or
            search.lower() in arg["respondent"]["mainArgument"].lower() or
            any(search.lower() in detail.lower() for detail in arg["appellant"]["details"]) or
            any(search.lower() in detail.lower() for detail in arg["respondent"]["details"]) or
            any(search.lower() in ev["desc"].lower() for ev in arg["appellant"]["evidence"]) or
            any(search.lower() in ev["desc"].lower() for ev in arg["respondent"]["evidence"]))
    ]
else:
    filtered_data = argument_data

# Create tabs for different categories
categories = list(set(arg["category"] for arg in filtered_data))
tabs = st.tabs([category.title() for category in categories])

for tab, category in zip(tabs, categories):
    with tab:
        category_data = [arg for arg in filtered_data if arg["category"] == category]
        
        for arg in category_data:
            with st.expander(f"**{arg['issue']}**", expanded=True):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📤 Appellant's Position")
                    st.markdown(f"**Main Argument:**")
                    st.info(arg["appellant"]["mainArgument"])
                    
                    st.markdown("**Supporting Points:**")
                    for point in arg["appellant"]["details"]:
                        st.markdown(f"• {point}")
                    
                    st.markdown("**Evidence:**")
                    display_evidence(arg["appellant"]["evidence"], "#6C63FF")
                    
                    st.markdown("**Case Law:**")
                    display_case_law(arg["appellant"]["caselaw"], "#6C63FF")
                
                with col2:
                    st.subheader("📥 Respondent's Position")
                    st.markdown(f"**Main Argument:**")
                    st.error(arg["respondent"]["mainArgument"])
                    
                    st.markdown("**Supporting Points:**")
                    for point in arg["respondent"]["details"]:
                        st.markdown(f"• {point}")
                    
                    st.markdown("**Evidence:**")
                    display_evidence(arg["respondent"]["evidence"], "#FF6B6B")
                    
                    st.markdown("**Case Law:**")
                    display_case_law(arg["respondent"]["caselaw"], "#FF6B6B")

# Summary table
if st.button("📊 Generate Summary Table"):
    summary_data = []
    for arg in filtered_data:
        summary_data.append({
            "Issue": arg["issue"],
            "Category": arg["category"].title(),
            "Appellant Position": arg["appellant"]["mainArgument"],
            "Respondent Position": arg["respondent"]["mainArgument"]
        })
    
    df = pd.DataFrame(summary_data)
    st.dataframe(df, use_container_width=True)

# Export functionality
if st.download_button(
    label="📥 Export Data",
    data=pd.DataFrame(summary_data).to_csv(index=False),
    file_name=f"legal_arguments_summary_{datetime.now().strftime('%Y%m%d')}.csv",
    mime="text/csv"
):
    st.success("Data exported successfully!")

# Footer
st.markdown("---")
st.markdown("*Last updated: {}*".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
