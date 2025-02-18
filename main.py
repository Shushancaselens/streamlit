import streamlit as st

# Styles
STREAMLIT_STYLE = """
<style>
    /* Hide Streamlit defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Container adjustments */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
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
    
    /* Headers and sections */
    .section-header {
        font-size: 0.875rem;
        font-weight: 500;
        color: #6b7280;
        margin: 1rem 0 0.5rem 0;
    }
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
</style>
"""

SEARCH_ICON = """
<div class="search-icon">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" 
         stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
    </svg>
</div>
"""

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
    # ... Add other argument data here ...
]

# Helper functions
def filter_arguments(args, search_term):
    """Filter arguments based on search term."""
    if not search_term:
        return args
    
    search_term = search_term.lower()
    
    def matches_search(arg):
        # Check issue and category
        if search_term in arg["issue"].lower() or search_term in arg["category"].lower():
            return True
        
        # Check appellant and respondent details
        for party in ['appellant', 'respondent']:
            if search_term in arg[party]['mainArgument'].lower():
                return True
            
            if any(search_term in detail.lower() for detail in arg[party]['details']):
                return True
            
            if any(search_term in evidence['desc'].lower() for evidence in arg[party]['evidence']):
                return True
            
            if any(search_term in case.lower() for case in arg[party]['caselaw']):
                return True
        
        return False
    
    return [arg for arg in args if matches_search(arg)]

def render_evidence_section(evidence_list, position_type):
    color_class = position_type.lower()
    evidence_html = []
    
    for evidence in evidence_list:
        evidence_html.append(f'''
            <a href="#" class="evidence-link">
                <span class="evidence-id {color_class}">{evidence['id']}</span>
                {evidence['desc']}
            </a>
        ''')
    
    return ''.join(evidence_html)

def render_case_law_section(case_list):
    case_html = []
    
    for case in case_list:
        case_html.append(f'''
            <div class="case-law-item">
                <span>{case}</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" 
                     fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" 
                     stroke-linejoin="round" class="copy-icon">
                    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                    <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                </svg>
            </div>
        ''')
    
    return ''.join(case_html)

def render_position_section(position_data, position_type):
    color_class = position_type.lower()
    
    st.markdown(f"""
        <div class="position-header {color_class}">{position_type}'s Position</div>
        <div class="main-argument">{position_data['mainArgument']}</div>
        
        <div class="section-header">Supporting Points</div>
        <ul class="details-list">
            {''.join(f'<li>{detail}</li>' for detail in position_data['details'])}
        </ul>
        
        <div class="section-header">Evidence</div>
        {render_evidence_section(position_data['evidence'], position_type)}
        
        <div class="section-header">Case Law</div>
        {render_case_law_section(position_data['caselaw'])}
    """, unsafe_allow_html=True)

# Main app
def main():
    # Configure the page
    st.set_page_config(layout="wide", page_title="Legal Arguments Comparison")
    
    # Apply custom styling
    st.markdown(STREAMLIT_STYLE, unsafe_allow_html=True)
    
    # Add search icon
    st.markdown(SEARCH_ICON, unsafe_allow_html=True)
    
    # Search input
    search = st.text_input(
        "", 
        placeholder="Search issues, arguments, or evidence...",
        label_visibility="collapsed"
    )
    
    # Filter and display arguments
    filtered_args = filter_arguments(argument_data, search)
    for arg in filtered_args:
        with st.expander(f"{arg['issue']} ({arg['category']})"):
            cols = st.columns(2)
            with cols[0]:
                render_position_section(arg['appellant'], "Appellant")
            with cols[1]:
                render_position_section(arg['respondent'], "Respondent")

if __name__ == "__main__":
    main()
