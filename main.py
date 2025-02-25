import streamlit as st
import pandas as pd
from datetime import datetime
import json
import base64
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(
    page_title="Legal Arguments Analysis",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS to match the original design
st.markdown("""
<style>
    /* Card styling */
    .stApp {
        background-color: #f9fafb;
    }
    .card {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .card-title {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 16px;
    }
    
    /* Tab styling */
    .tab-container {
        display: flex;
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 24px;
    }
    .tab {
        padding: 12px 24px;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
    }
    .tab-active {
        border-bottom: 2px solid #3b82f6;
        color: #3b82f6;
    }
    .tab-inactive {
        color: #6b7280;
    }
    
    /* Argument styling */
    .argument-header {
        display: flex;
        align-items: center;
        padding: 12px 16px;
        border-radius: 8px;
        cursor: pointer;
        margin-bottom: 8px;
    }
    .claimant-header {
        background-color: #eff6ff;
        border: 1px solid #bfdbfe;
    }
    .respondent-header {
        background-color: #fef2f2;
        border: 1px solid #fecaca;
    }
    .argument-title {
        font-size: 14px;
        font-weight: 500;
        margin-left: 8px;
    }
    .argument-content {
        padding: 16px;
        background-color: white;
        border-radius: 0 0 8px 8px;
        margin-bottom: 16px;
    }
    
    /* Timeline styling */
    .timeline-row {
        border-bottom: 1px solid #e5e7eb;
    }
    .timeline-row:hover {
        background-color: #f9fafb;
    }
    .status-undisputed {
        color: #16a34a;
    }
    .status-disputed {
        color: #dc2626;
    }
    .timeline-row-disputed {
        background-color: #fef2f2;
    }
    
    /* Button styling */
    .st-bx {
        border-radius: 6px;
    }
    .st-cc {
        border-radius: 6px;
    }
    
    /* Tag styling */
    .tag {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        margin-right: 4px;
    }
    .tag-blue {
        background-color: #eff6ff;
        color: #1e40af;
    }
    .tag-red {
        background-color: #fef2f2;
        color: #b91c1c;
    }
    .tag-green {
        background-color: #f0fdf4;
        color: #166534;
    }
    .tag-gray {
        background-color: #f3f4f6;
        color: #4b5563;
    }
    
    /* Exhibit styling */
    .exhibit-row {
        border-bottom: 1px solid #e5e7eb;
        padding: 12px 0;
    }
    .exhibit-row:hover {
        background-color: #f9fafb;
    }
    .party-appellant {
        background-color: #eff6ff;
        color: #1e40af;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
    }
    .party-respondent {
        background-color: #fef2f2;
        color: #b91c1c;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
    }
    
    /* Checkbox styling */
    .st-cc {
        margin-right: 8px;
    }
    
    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Topic view styling */
    .topic-header {
        margin-bottom: 16px;
    }
    .topic-title {
        font-size: 18px;
        font-weight: 600;
        color: #1f2937;
    }
    .topic-description {
        font-size: 14px;
        color: #6b7280;
    }
    
    /* Custom header columns */
    .header-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        margin-bottom: 16px;
    }
    .claimant-header-col {
        color: #1e40af;
        font-size: 16px;
        font-weight: 600;
    }
    .respondent-header-col {
        color: #b91c1c;
        font-size: 16px;
        font-weight: 600;
    }
    
    /* Buttons in line */
    .button-container {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 16px;
    }
    .button-container button {
        margin-left: 8px;
    }
    
    /* View toggle buttons */
    .view-toggle {
        display: flex;
        background-color: #f3f4f6;
        border-radius: 6px;
        padding: 4px;
        width: fit-content;
        margin-left: auto;
        margin-bottom: 16px;
    }
    .view-toggle-button {
        padding: 6px 12px;
        font-size: 14px;
        border-radius: 4px;
        border: none;
        background: none;
        cursor: pointer;
    }
    .view-toggle-active {
        background-color: white;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "arguments"
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "default"
if 'expanded_arguments' not in st.session_state:
    st.session_state.expanded_arguments = {}

# Data for the application
def load_data():
    # Timeline data
    timeline_data = [
        { 
            "date": "2023-01-15", 
            "appellant_version": "Contract signed with Club", 
            "respondent_version": "—", 
            "status": "Undisputed" 
        },
        { 
            "date": "2023-03-20", 
            "appellant_version": "Player received notification of exclusion from team", 
            "respondent_version": "—", 
            "status": "Undisputed" 
        },
        { 
            "date": "2023-03-22", 
            "appellant_version": "Player requested explanation", 
            "respondent_version": "—", 
            "status": "Undisputed" 
        },
        { 
            "date": "2023-04-01", 
            "appellant_version": "Player sent termination letter", 
            "respondent_version": "—", 
            "status": "Undisputed" 
        },
        { 
            "date": "2023-04-05", 
            "appellant_version": "—", 
            "respondent_version": "Club rejected termination as invalid", 
            "status": "Undisputed" 
        },
        { 
            "date": "2023-04-10", 
            "appellant_version": "Player was denied access to training facilities", 
            "respondent_version": "—", 
            "status": "Disputed" 
        },
        { 
            "date": "2023-04-15", 
            "appellant_version": "—", 
            "respondent_version": "Club issued warning letter", 
            "status": "Undisputed" 
        },
        { 
            "date": "2023-05-01", 
            "appellant_version": "Player filed claim with FIFA", 
            "respondent_version": "—", 
            "status": "Undisputed" 
        },
    ]
    
    # Exhibits data
    exhibits_data = [
        {
            "id": "C-1",
            "party": "Appellant",
            "title": "Employment Contract",
            "type": "contract",
            "summary": "Employment contract dated 15 January 2023 between Player and Club"
        },
        {
            "id": "C-2",
            "party": "Appellant",
            "title": "Termination Letter",
            "type": "letter",
            "summary": "Player's termination letter sent on 1 April 2023"
        },
        {
            "id": "C-3",
            "party": "Appellant",
            "title": "Email Correspondence",
            "type": "communication",
            "summary": "Email exchanges between Player and Club from 22-30 March 2023"
        },
        {
            "id": "C-4",
            "party": "Appellant",
            "title": "Witness Statement",
            "type": "statement",
            "summary": "Statement from team captain confirming Player's exclusion"
        },
        {
            "id": "R-1",
            "party": "Respondent",
            "title": "Club Regulations",
            "type": "regulations",
            "summary": "Internal regulations of the Club dated January 2022"
        },
        {
            "id": "R-2",
            "party": "Respondent",
            "title": "Warning Letter",
            "type": "letter",
            "summary": "Warning letter issued to Player on 15 April 2023"
        },
        {
            "id": "R-3",
            "party": "Respondent",
            "title": "Training Schedule",
            "type": "schedule",
            "summary": "Team training schedule for March-April 2023"
        }
    ]
    
    # Topic sections data
    topic_sections = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "arguments": [
                {
                    "id": "1",
                    "claimant": {
                        "title": "Sporting Succession",
                        "paragraphs": "15-18",
                        "overview": {
                            "points": [
                                "Analysis of multiple established criteria",
                                "Focus on continuous use of identifying elements",
                                "Public recognition assessment"
                            ],
                            "paragraphs": "15-16"
                        },
                        "legal_points": [
                            {
                                "point": "CAS jurisprudence establishes criteria for sporting succession",
                                "is_disputed": False,
                                "regulations": ["CAS 2016/A/4576"],
                                "paragraphs": "15-17"
                            }
                        ],
                        "factual_points": [
                            {
                                "point": "Continuous operation under same name since 1950",
                                "date": "1950-present",
                                "is_disputed": False,
                                "paragraphs": "18-19"
                            }
                        ],
                        "evidence": [
                            {
                                "id": "C-1",
                                "title": "Historical Registration Documents",
                                "summary": "Official records showing continuous name usage",
                                "citations": ["20", "21", "24"]
                            }
                        ],
                        "case_law": [
                            {
                                "case_number": "CAS 2016/A/4576",
                                "title": "Criteria for sporting succession",
                                "relevance": "Establishes key factors for succession",
                                "paragraphs": "45-48",
                                "cited_paragraphs": ["45", "46", "47"]
                            }
                        ],
                        "sub_arguments": []
                    },
                    "respondent": {
                        "title": "Sporting Succession Rebuttal",
                        "paragraphs": "200-218",
                        "overview": {
                            "points": [
                                "Challenge to claimed continuity of operations",
                                "Analysis of discontinuities in club operations",
                                "Dispute over public recognition factors"
                            ],
                            "paragraphs": "200-202"
                        },
                        "legal_points": [
                            {
                                "point": "CAS jurisprudence requires operational continuity not merely identification",
                                "is_disputed": False,
                                "regulations": ["CAS 2017/A/5465"],
                                "paragraphs": "203-205"
                            }
                        ],
                        "factual_points": [
                            {
                                "point": "Operations ceased between 1975-1976",
                                "date": "1975-1976",
                                "is_disputed": True,
                                "source": "Claimant",
                                "paragraphs": "206-207"
                            }
                        ],
                        "evidence": [
                            {
                                "id": "R-1",
                                "title": "Federation Records",
                                "summary": "Records showing non-participation in 1975-1976 season",
                                "citations": ["208", "209", "210"]
                            }
                        ],
                        "case_law": [
                            {
                                "case_number": "CAS 2017/A/5465",
                                "title": "Operational continuity requirement",
                                "relevance": "Establishes primacy of operational continuity",
                                "paragraphs": "211-213",
                                "cited_paragraphs": ["212"]
                            }
                        ],
                        "sub_arguments": []
                    }
                }
            ]
        },
        {
            "id": "topic-2",
            "title": "Doping Violation and Chain of Custody",
            "description": "Issues related to doping test procedures and evidence handling",
            "arguments": [
                {
                    "id": "2",
                    "claimant": {
                        "title": "Doping Violation Chain of Custody",
                        "paragraphs": "70-125",
                        "overview": {
                            "points": [
                                "Analysis of sample collection and handling procedures",
                                "Evaluation of laboratory testing protocols",
                                "Assessment of chain of custody documentation"
                            ],
                            "paragraphs": "70-72"
                        },
                        "legal_points": [
                            {
                                "point": "WADA Code Article 5 establishes procedural requirements",
                                "is_disputed": False,
                                "regulations": ["WADA Code 2021", "International Standard for Testing"],
                                "paragraphs": "73-75"
                            }
                        ],
                        "factual_points": [],
                        "evidence": [],
                        "case_law": [],
                        "sub_arguments": []
                    },
                    "respondent": {
                        "title": "Doping Chain of Custody Defense",
                        "paragraphs": "250-290",
                        "overview": {
                            "points": [
                                "Defense of sample collection procedures",
                                "Validation of laboratory testing protocols",
                                "Completeness of documentation"
                            ],
                            "paragraphs": "250-252"
                        },
                        "legal_points": [
                            {
                                "point": "Minor procedural deviations do not invalidate results",
                                "is_disputed": False,
                                "regulations": ["CAS 2019/A/6148"],
                                "paragraphs": "253-255"
                            }
                        ],
                        "factual_points": [],
                        "evidence": [],
                        "case_law": [],
                        "sub_arguments": []
                    }
                }
            ]
        }
    ]
    
    return timeline_data, exhibits_data, topic_sections

timeline_data, exhibits_data, topic_sections = load_data()

# Main card container
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">Legal Arguments Analysis</div>', unsafe_allow_html=True)

# Tab navigation
with st.container():
    col1, col2, col3, col4 = st.columns([2, 2, 2, 6])
    
    with col1:
        if st.button("Summary of Arguments", 
                    key="summary_tab", 
                    help="View legal arguments analysis",
                    use_container_width=True,
                    type="secondary" if st.session_state.active_tab != "arguments" else "primary"):
            st.session_state.active_tab = "arguments"
            st.rerun()
    
    with col2:
        if st.button("Timeline", 
                    key="timeline_tab", 
                    help="View case timeline",
                    use_container_width=True,
                    type="secondary" if st.session_state.active_tab != "timeline" else "primary"):
            st.session_state.active_tab = "timeline"
            st.rerun()
    
    with col3:
        if st.button("Exhibits", 
                    key="exhibits_tab", 
                    help="View case exhibits",
                    use_container_width=True,
                    type="secondary" if st.session_state.active_tab != "exhibits" else "primary"):
            st.session_state.active_tab = "exhibits"
            st.rerun()
    
    with col4:
        if st.session_state.active_tab in ["timeline", "exhibits"]:
            col_a, col_b = st.columns([5, 1])
            with col_b:
                st.download_button(
                    "Export Data",
                    data=json.dumps(timeline_data if st.session_state.active_tab == "timeline" else exhibits_data),
                    file_name=f"{st.session_state.active_tab}_data.json",
                    mime="application/json",
                )

# Add horizontal line
st.markdown('<hr style="margin-bottom: 20px; margin-top: 10px; border-color: #e5e7eb;">', unsafe_allow_html=True)

# Arguments Tab
if st.session_state.active_tab == "arguments":
    # View toggle
    col1, col2, col3 = st.columns([6, 3, 3])
    with col3:
        st.write('<div class="view-toggle">', unsafe_allow_html=True)
        cols = st.columns(2)
        with cols[0]:
            if st.button("Standard View", 
                        key="standard_view",
                        type="secondary" if st.session_state.view_mode != "default" else "primary",
                        use_container_width=True):
                st.session_state.view_mode = "default"
                st.rerun()
        with cols[1]:
            if st.button("Topic View", 
                        key="topic_view",
                        type="secondary" if st.session_state.view_mode != "hierarchical" else "primary",
                        use_container_width=True):
                st.session_state.view_mode = "hierarchical"
                st.rerun()
        st.write('</div>', unsafe_allow_html=True)
    
    # Default View (Standard)
    if st.session_state.view_mode == "default":
        # Headers
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h2 style="font-size: 18px; font-weight: 600; color: #1e40af;">Claimant\'s Arguments</h2>', unsafe_allow_html=True)
        with col2:
            st.markdown('<h2 style="font-size: 18px; font-weight: 600; color: #b91c1c;">Respondent\'s Arguments</h2>', unsafe_allow_html=True)
        
        # Handle argument expansion
        def toggle_argument(arg_id):
            if arg_id in st.session_state.expanded_arguments:
                st.session_state.expanded_arguments.pop(arg_id)
            else:
                st.session_state.expanded_arguments[arg_id] = True
        
        # Render argument components
        def render_overview_points(points, paragraphs):
            with st.container():
                st.markdown(f"""
                <div style="background-color: #f3f4f6; border-radius: 8px; padding: 16px; margin-bottom: 16px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <h6 style="font-size: 14px; font-weight: 500;">Key Points</h6>
                        <span style="font-size: 12px; background-color: #dbeafe; color: #1e40af; padding: 4px 8px; border-radius: 4px;">¶{paragraphs}</span>
                    </div>
                    <ul style="list-style-type: none; padding-left: 0; margin: 0;">
                        {"".join([f'<li style="display: flex; align-items: center; margin-bottom: 8px;"><div style="width: 6px; height: 6px; border-radius: 50%; background-color: #3b82f6; margin-right: 8px;"></div><span style="font-size: 14px; color: #4b5563;">{point}</span></li>' for point in points])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        
        def render_legal_point(point, is_disputed, regulations, paragraphs):
            with st.container():
                st.markdown(f"""
                <div style="background-color: #eff6ff; border-radius: 8px; padding: 12px; margin-bottom: 8px;">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                        <span style="font-size: 12px; padding: 2px 8px; background-color: #dbeafe; color: #1e40af; border-radius: 4px;">Legal</span>
                        {f'<span style="font-size: 12px; padding: 2px 8px; background-color: #fee2e2; color: #b91c1c; border-radius: 4px;">Disputed</span>' if is_disputed else ''}
                    </div>
                    <p style="font-size: 14px; color: #4b5563; margin-bottom: 8px;">{point}</p>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                        {"".join([f'<span style="font-size: 12px; background-color: #dbeafe; padding: 4px 8px; border-radius: 4px;">{reg}</span>' for reg in regulations])}
                        <span style="font-size: 12px; color: #6b7280; margin-left: 4px;">¶{paragraphs}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        def render_factual_point(point, date, is_disputed, source, paragraphs):
            with st.container():
                st.markdown(f"""
                <div style="background-color: #f0fdf4; border-radius: 8px; padding: 12px; margin-bottom: 8px;">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                        <span style="font-size: 12px; padding: 2px 8px; background-color: #dcfce7; color: #166534; border-radius: 4px;">Factual</span>
                        {f'<span style="font-size: 12px; padding: 2px 8px; background-color: #fee2e2; color: #b91c1c; border-radius: 4px;">Disputed by {source}</span>' if is_disputed else ''}
                    </div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                        <span style="font-size: 12px; color: #6b7280;">{date}</span>
                    </div>
                    <p style="font-size: 14px; color: #4b5563; margin-bottom: 8px;">{point}</p>
                    <span style="font-size: 12px; color: #6b7280; display: block;">¶{paragraphs}</span>
                </div>
                """, unsafe_allow_html=True)
        
        def render_evidence(id, title, summary, citations):
            with st.container():
                st.markdown(f"""
                <div style="background-color: #f3f4f6; border-radius: 8px; padding: 12px; margin-bottom: 8px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div>
                            <p style="font-size: 14px; font-weight: 500; margin-bottom: 4px;">{id}: {title}</p>
                            <p style="font-size: 12px; color: #6b7280; margin-bottom: 8px;">{summary}</p>
                            <div>
                                <span style="font-size: 12px; color: #6b7280;">Cited in: </span>
                                {"".join([f'<span style="font-size: 12px; background-color: #e5e7eb; border-radius: 4px; padding: 2px 8px; margin-left: 4px;">¶{cite}</span>' for cite in citations])}
                            </div>
                        </div>
                        <button style="background: none; border: none; color: #6b7280; padding: 4px;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                        </button>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        def render_case_law(case_number, title, relevance, paragraphs, cited_paragraphs):
            with st.container():
                st.markdown(f"""
                <div style="background-color: #f3f4f6; border-radius: 8px; padding: 12px; margin-bottom: 8px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <p style="font-size: 14px; font-weight: 500; margin-bottom: 4px;">{case_number}</p>
                                <span style="font-size: 12px; color: #6b7280;">¶{paragraphs}</span>
                            </div>
                            <p style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">{title}</p>
                            <p style="font-size: 14px; color: #4b5563; margin-bottom: 8px;">{relevance}</p>
                            {f'''
                            <div>
                                <span style="font-size: 12px; color: #6b7280;">Key Paragraphs: </span>
                                {"".join([f'<span style="font-size: 12px; background-color: #e5e7eb; border-radius: 4px; padding: 2px 8px; margin-left: 4px;">¶{para}</span>' for para in cited_paragraphs])}
                            </div>
                            ''' if cited_paragraphs else ''}
                        </div>
                        <button style="background: none; border: none; color: #6b7280; padding: 4px;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                        </button>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        def render_argument_content(argument, side):
            if argument.get("overview") and argument["overview"].get("points"):
                st.markdown(f'<h6 style="font-size: 14px; font-weight: 500; margin-bottom: 8px;">Key Points</h6>', unsafe_allow_html=True)
                render_overview_points(argument["overview"]["points"], argument["overview"]["paragraphs"])
            
            if argument.get("legal_points") and len(argument["legal_points"]) > 0:
                st.markdown(f'<h6 style="font-size: 14px; font-weight: 500; margin-bottom: 8px;">Legal Points</h6>', unsafe_allow_html=True)
                for point in argument["legal_points"]:
                    render_legal_point(
                        point["point"], 
                        point.get("is_disputed", False), 
                        point.get("regulations", []), 
                        point.get("paragraphs", "")
                    )
            
            if argument.get("factual_points") and len(argument["factual_points"]) > 0:
                st.markdown(f'<h6 style="font-size: 14px; font-weight: 500; margin-bottom: 8px;">Factual Points</h6>', unsafe_allow_html=True)
                for point in argument["factual_points"]:
                    render_factual_point(
                        point["point"], 
                        point.get("date", ""), 
                        point.get("is_disputed", False), 
                        point.get("source", ""), 
                        point.get("paragraphs", "")
                    )
            
            if argument.get("evidence") and len(argument["evidence"]) > 0:
                st.markdown(f'<h6 style="font-size: 14px; font-weight: 500; margin-bottom: 8px;">Evidence</h6>', unsafe_allow_html=True)
                for item in argument["evidence"]:
                    render_evidence(
                        item["id"], 
                        item["title"], 
                        item.get("summary", ""), 
                        item.get("citations", [])
                    )
            
            if argument.get("case_law") and len(argument["case_law"]) > 0:
                st.markdown(f'<h6 style="font-size: 14px; font-weight: 500; margin-bottom: 8px;">Case Law</h6>', unsafe_allow_html=True)
                for item in argument["case_law"]:
                    render_case_law(
                        item["case_number"], 
                        item["title"], 
                        item.get("relevance", ""), 
                        item.get("paragraphs", ""), 
                        item.get("cited_paragraphs", [])
                    )
        
        # Render arguments for default view
        for topic in topic_sections:
            for argument_pair in topic["arguments"]:
                arg_id = argument_pair["id"]
                claimant_arg = argument_pair["claimant"]
                respondent_arg = argument_pair["respondent"]
                
                cols = st.columns(2)
                
                # Claimant side
                with cols[0]:
                    claimant_expanded = arg_id in st.session_state.expanded_arguments
                    
                    # Argument header
                    claimant_header = f"""
                    <div class="argument-header claimant-header" id="claimant-{arg_id}">
                        <span>{'▼' if claimant_expanded else '▶'}</span>
                        <span class="argument-title">{arg_id}. {claimant_arg['title']}</span>
                        <span style="margin-left: auto; font-size: 12px; background-color: rgba(59, 130, 246, 0.1); color: #3b82f6; padding: 2px 8px; border-radius: 12px;">¶{claimant_arg['paragraphs']}</span>
                    </div>
                    """
                    
                    if st.markdown(claimant_header, unsafe_allow_html=True):
                        toggle_argument(arg_id)
                        st.rerun()
                    
                    # Expanded content
                    if claimant_expanded:
                        with st.container():
                            st.markdown('<div class="argument-content">', unsafe_allow_html=True)
                            render_argument_content(claimant_arg, "claimant")
                            st.markdown('</div>', unsafe_allow_html=True)
                
                # Respondent side
                with cols[1]:
                    respondent_expanded = arg_id in st.session_state.expanded_arguments
                    
                    # Argument header
                    respondent_header = f"""
                    <div class="argument-header respondent-header" id="respondent-{arg_id}">
                        <span>{'▼' if respondent_expanded else '▶'}</span>
                        <span class="argument-title">{arg_id}. {respondent_arg['title']}</span>
                        <span style="margin-left: auto; font-size: 12px; background-color: rgba(239, 68, 68, 0.1); color: #ef4444; padding: 2px 8px; border-radius: 12px;">¶{respondent_arg['paragraphs']}</span>
                    </div>
                    """
                    
                    if st.markdown(respondent_header, unsafe_allow_html=True):
                        toggle_argument(arg_id)
                        st.rerun()
                    
                    # Expanded content
                    if respondent_expanded:
                        with st.container():
                            st.markdown('<div class="argument-content">', unsafe_allow_html=True)
                            render_argument_content(respondent_arg, "respondent")
                            st.markdown('</div>', unsafe_allow_html=True)
    
    # Hierarchical View (Topic View)
    else:
        for topic in topic_sections:
            # Topic header
            st.markdown(f"""
            <div class="topic-header">
                <div class="topic-title">{topic['title']}</div>
                <div class="topic-description">{topic['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Column headers
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<h3 class="claimant-header-col">Claimant\'s Arguments</h3>', unsafe_allow_html=True)
            with col2:
                st.markdown('<h3 class="respondent-header-col">Respondent\'s Arguments</h3>', unsafe_allow_html=True)
            
            # Arguments
            for argument_pair in topic["arguments"]:
                arg_id = argument_pair["id"]
                claimant_arg = argument_pair["claimant"]
                respondent_arg = argument_pair["respondent"]
                
                cols = st.columns(2)
                
                # Claimant side
                with cols[0]:
                    claimant_expanded = arg_id in st.session_state.expanded_arguments
                    
                    # Argument header
                    claimant_header = f"""
                    <div class="argument-header claimant-header" id="claimant-{arg_id}">
                        <span>{'▼' if claimant_expanded else '▶'}</span>
                        <span class="argument-title">{arg_id}. {claimant_arg['title']}</span>
                        <span style="margin-left: auto; font-size: 12px; background-color: rgba(59, 130, 246, 0.1); color: #3b82f6; padding: 2px 8px; border-radius: 12px;">¶{claimant_arg['paragraphs']}</span>
                    </div>
                    """
                    
                    if st.markdown(claimant_header, unsafe_allow_html=True):
                        toggle_argument(arg_id)
                        st.rerun()
                    
                    # Expanded content
                    if claimant_expanded:
                        with st.container():
                            st.markdown('<div class="argument-content">', unsafe_allow_html=True)
                            render_argument_content(claimant_arg, "claimant")
                            st.markdown('</div>', unsafe_allow_html=True)
                
                # Respondent side
                with cols[1]:
                    respondent_expanded = arg_id in st.session_state.expanded_arguments
                    
                    # Argument header
                    respondent_header = f"""
                    <div class="argument-header respondent-header" id="respondent-{arg_id}">
                        <span>{'▼' if respondent_expanded else '▶'}</span>
                        <span class="argument-title">{arg_id}. {respondent_arg['title']}</span>
                        <span style="margin-left: auto; font-size: 12px; background-color: rgba(239, 68, 68, 0.1); color: #ef4444; padding: 2px 8px; border-radius: 12px;">¶{respondent_arg['paragraphs']}</span>
                    </div>
                    """
                    
                    if st.markdown(respondent_header, unsafe_allow_html=True):
                        toggle_argument(arg_id)
                        st.rerun()
                    
                    # Expanded content
                    if respondent_expanded:
                        with st.container():
                            st.markdown('<div class="argument-content">', unsafe_allow_html=True)
                            render_argument_content(respondent_arg, "respondent")
                            st.markdown('</div>', unsafe_allow_html=True)
            
            # Add spacing between topics
            st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

# Timeline Tab
elif st.session_state.active_tab == "timeline":
    # Search and filter
    col1, col2, col3 = st.columns([3, 1, 2])
    
    with col1:
        search_term = st.text_input("", placeholder="Search events...", label_visibility="collapsed")
    
    with col2:
        st.button("Filter", key="filter_button", use_container_width=True)
    
    with col3:
        disputed_only = st.checkbox("Disputed events only", key="disputed_only")
    
    # Filter the timeline data
    filtered_timeline = timeline_data
    if search_term:
        filtered_timeline = [
            item for item in filtered_timeline 
            if search_term.lower() in item["appellant_version"].lower() or 
               search_term.lower() in item["respondent_version"].lower()
        ]
    
    if disputed_only:
        filtered_timeline = [item for item in filtered_timeline if item["status"] == "Disputed"]
    
    # Display the timeline table
    st.markdown('<div style="background-color: white; border-radius: 8px; border: 1px solid #e5e7eb; overflow: hidden; margin-top: 16px;">', unsafe_allow_html=True)
    
    # Table header
    st.markdown("""
    <div style="display: grid; grid-template-columns: 15% 35% 35% 15%; background-color: #f9fafb; border-bottom: 1px solid #e5e7eb;">
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: left;">DATE</div>
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: left;">APPELLANT'S VERSION</div>
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: left;">RESPONDENT'S VERSION</div>
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: left;">STATUS</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Table rows
    for item in filtered_timeline:
        row_class = "timeline-row-disputed" if item["status"] == "Disputed" else ""
        status_class = "status-disputed" if item["status"] == "Disputed" else "status-undisputed"
        
        st.markdown(f"""
        <div style="display: grid; grid-template-columns: 15% 35% 35% 15%; border-bottom: 1px solid #e5e7eb;" class="{row_class}">
            <div style="padding: 12px 16px; font-size: 14px; color: #4b5563;">{item["date"]}</div>
            <div style="padding: 12px 16px; font-size: 14px; color: #4b5563;">{item["appellant_version"]}</div>
            <div style="padding: 12px 16px; font-size: 14px; color: #4b5563;">{item["respondent_version"]}</div>
            <div style="padding: 12px 16px; font-size: 14px;" class="{status_class}">{item["status"]}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Exhibits Tab
elif st.session_state.active_tab == "exhibits":
    # Search and filters
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        search_term = st.text_input("", placeholder="Search exhibits...", label_visibility="collapsed")
    
    with col2:
        party_filter = st.selectbox("", ["All Parties", "Appellant", "Respondent"], label_visibility="collapsed")
    
    with col3:
        # Get unique types
        types = ["All Types"] + list(set([item["type"] for item in exhibits_data]))
        type_filter = st.selectbox("", types, label_visibility="collapsed")
    
    # Filter the exhibits data
    filtered_exhibits = exhibits_data
    if search_term:
        filtered_exhibits = [
            item for item in filtered_exhibits 
            if search_term.lower() in item["id"].lower() or 
               search_term.lower() in item["title"].lower() or
               search_term.lower() in item["summary"].lower()
        ]
    
    if party_filter != "All Parties":
        filtered_exhibits = [item for item in filtered_exhibits if item["party"] == party_filter]
    
    if type_filter != "All Types":
        filtered_exhibits = [item for item in filtered_exhibits if item["type"] == type_filter]
    
    # Display the exhibits table
    st.markdown('<div style="background-color: white; border-radius: 8px; border: 1px solid #e5e7eb; overflow: hidden; margin-top: 16px;">', unsafe_allow_html=True)
    
    # Table header
    st.markdown("""
    <div style="display: grid; grid-template-columns: 10% 15% 20% 10% 35% 10%; background-color: #f9fafb; border-bottom: 1px solid #e5e7eb;">
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: left;">EXHIBIT ID</div>
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: left;">PARTY</div>
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: left;">TITLE</div>
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: left;">TYPE</div>
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: left;">SUMMARY</div>
        <div style="padding: 12px 16px; font-size: 14px; font-weight: 500; color: #6b7280; text-align: right;">ACTIONS</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Table rows
    for item in filtered_exhibits:
        party_class = "party-appellant" if item["party"] == "Appellant" else "party-respondent"
        
        st.markdown(f"""
        <div style="display: grid; grid-template-columns: 10% 15% 20% 10% 35% 10%; border-bottom: 1px solid #e5e7eb;">
            <div style="padding: 12px 16px; font-size: 14px; color: #4b5563;">{item["id"]}</div>
            <div style="padding: 12px 16px; font-size: 14px;">
                <span class="{party_class}">{item["party"]}</span>
            </div>
            <div style="padding: 12px 16px; font-size: 14px; color: #4b5563;">{item["title"]}</div>
            <div style="padding: 12px 16px; font-size: 14px;">
                <span style="font-size: 12px; background-color: #f3f4f6; color: #4b5563; padding: 2px 8px; border-radius: 4px;">{item["type"]}</span>
            </div>
            <div style="padding: 12px 16px; font-size: 14px; color: #4b5563;">{item["summary"]}</div>
            <div style="padding: 12px 16px; font-size: 14px; text-align: right;">
                <a href="#" style="color: #3b82f6; text-decoration: none; font-size: 14px;">View</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Close the card container
st.markdown('</div>', unsafe_allow_html=True)
