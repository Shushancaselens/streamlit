import streamlit as st
import pandas as pd
from streamlit_searchbox import st_searchbox
import json

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .issue-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }
    .position-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 0.5rem;
    }
    .evidence-tag {
        background-color: #e0e7ff;
        color: #4338ca;
        padding: 0.25rem 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .category-tag {
        background-color: #f3f4f6;
        color: #4b5563;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .divider {
        border-top: 1px solid #e5e7eb;
        margin: 1rem 0;
    }
    .main-argument {
        background-color: #f9fafb;
        padding: 1rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
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
    # Add more cases as needed...
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
            <div class="position-card">
                <span class="evidence-tag">{evidence['id']}</span>
                <span style="margin-left: 0.5rem">{evidence['desc']}</span>
            </div>
        """, unsafe_allow_html=True)
    
    # Case Law
    st.markdown("##### Case Law")
    for case in position_data['caselaw']:
        st.markdown(f"""
            <div class="position-card">
                {case}
                <button onclick="navigator.clipboard.writeText('{case}')" style="float: right">
                    📋
                </button>
            </div>
        """, unsafe_allow_html=True)

def main():
    # Search bar
    search = st.text_input("🔍 Search issues, arguments, or evidence...", 
                          placeholder="Type to search...")
    
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
    
    # Export button
    if st.button("📋 Export Summary"):
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
    
    # Display arguments
    for arg in filtered_arguments:
        st.markdown(f"""
            <div class="issue-card">
                <h2>{arg['issue']} <span class="category-tag">{arg['category']}</span></h2>
            </div>
        """, unsafe_allow_html=True)
        
        # Create two columns for appellant and respondent
        col1, col2 = st.columns(2)
        
        with col1:
            create_position_section(arg['appellant'], "Appellant")
        
        with col2:
            create_position_section(arg['respondent'], "Respondent")
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
