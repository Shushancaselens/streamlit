import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Initialize session state for expanded sections if not exists
if 'expanded_sections' not in st.session_state:
    st.session_state.expanded_sections = {'1'}  # Default first section expanded

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
        cursor: pointer;
    }
    .issue-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
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
    .preview-text {
        color: #6b7280;
        font-size: 0.875rem;
        margin-top: 0.5rem;
    }
    .position-preview {
        margin-top: 1rem;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }
    .arrow-icon {
        color: #9ca3af;
        font-size: 1.5rem;
    }
    .position-label {
        color: rgb(79, 70, 229);
        font-size: 0.875rem;
        font-weight: 500;
        margin-bottom: 0.25rem;
    }
    .position-label.respondent {
        color: rgb(225, 29, 72);
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

def toggle_section(section_id):
    if section_id in st.session_state.expanded_sections:
        st.session_state.expanded_sections.remove(section_id)
    else:
        st.session_state.expanded_sections.add(section_id)

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
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            st.markdown(f"""
                <div class="position-card">
                    {case}
                </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("📋", key=f"copy_{case}"):
                st.write("Copied!")

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
        # Issue header with dropdown
        if st.button(
            f"{arg['issue']} {arg['category']} {'▼' if arg['id'] in st.session_state.expanded_sections else '▶'}",
            key=f"toggle_{arg['id']}",
            use_container_width=True,
            type="secondary"
        ):
            toggle_section(arg['id'])
        
        # Show preview if not expanded
        if arg['id'] not in st.session_state.expanded_sections:
            st.markdown(f"""
                <div class="position-preview">
                    <div>
                        <div class="position-label">Appellant Position</div>
                        <div class="preview-text">{arg['appellant']['mainArgument']}</div>
                    </div>
                    <div>
                        <div class="position-label respondent">Respondent Position</div>
                        <div class="preview-text">{arg['respondent']['mainArgument']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Show full content if expanded
        if arg['id'] in st.session_state.expanded_sections:
            col1, col2 = st.columns(2)
            with col1:
                create_position_section(arg['appellant'], "Appellant")
            with col2:
                create_position_section(arg['respondent'], "Respondent")
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
