import streamlit as st
import pandas as pd
from datetime import datetime
import base64

# Set page configuration
st.set_page_config(
    page_title="Legal Arguments Analysis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add custom CSS for styling
def add_custom_css():
    st.markdown("""
    <style>
    /* Main card styling */
    .main-card {
        background-color: white;
        border-radius: 0.5rem;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding-left: 1rem;
        padding-right: 1rem;
        white-space: pre-wrap;
    }
    
    /* Button styling */
    .stButton>button {
        border: 1px solid #e2e8f0;
        background-color: white;
        color: #4b5563;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .stButton>button:hover {
        background-color: #f9fafb;
    }
    
    .button-active {
        background-color: #3b82f6 !important;
        color: white !important;
    }
    
    /* Hide toggle buttons but keep them functional */
    button[data-testid="baseButton-secondary"]:has(div:contains("Toggle")) {
        position: absolute;
        opacity: 0;
        height: 1px;
        width: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border-width: 0;
    }
    
    /* Argument sections */
    .argument-header {
        background-color: #f9fafb;
        padding: 0.75rem 1rem;
        border-radius: 0.375rem;
        cursor: pointer;
        margin-bottom: 0.5rem;
        border: 1px solid #e5e7eb;
    }
    
    .argument-header:hover {
        background-color: #f3f4f6;
    }
    
    .claimant-color {
        color: #2563eb;
        border-color: #bfdbfe;
    }
    
    .respondent-color {
        color: #dc2626;
        border-color: #fecaca;
    }
    
    /* Tag styling */
    .tag {
        display: inline-block;
        padding: 0.125rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        font-weight: 500;
        margin-right: 0.25rem;
    }
    
    .tag-blue {
        background-color: #dbeafe;
        color: #1e40af;
    }
    
    .tag-red {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    
    .tag-green {
        background-color: #dcfce7;
        color: #166534;
    }
    
    .tag-gray {
        background-color: #f3f4f6;
        color: #4b5563;
    }
    
    /* Card components */
    .card-component {
        background-color: #f9fafb;
        border-radius: 0.375rem;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* Timeline and exhibits tables */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .styled-table th {
        background-color: #f9fafb;
        color: #6b7280;
        font-size: 0.875rem;
        font-weight: 600;
        text-align: left;
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #e5e7eb;
    }
    
    .styled-table td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #e5e7eb;
        font-size: 0.875rem;
    }
    
    .styled-table tr:hover {
        background-color: #f9fafb;
    }
    
    /* Disputed row styling */
    .disputed-row {
        background-color: #fee2e2;
    }
    
    /* Hierarchical view topic section */
    .topic-section {
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1.5rem;
        background-color: white;
        border: 1px solid #e5e7eb;
    }
    
    .topic-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.25rem;
    }
    
    .topic-description {
        font-size: 0.875rem;
        color: #6b7280;
        margin-bottom: 1rem;
    }

    /* Remove default Streamlit margins and padding */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        max-width: 95%;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for maintaining state across reruns
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'default'
if 'expanded_args' not in st.session_state:
    st.session_state.expanded_args = {}

# Apply custom CSS
add_custom_css()

# Main page header
st.markdown("<h1 style='font-size: 1.5rem; margin-bottom: 1rem;'>Legal Arguments Analysis</h1>", unsafe_allow_html=True)

# Tab navigation
tabs = ["Summary of Arguments", "Timeline", "Exhibits"]
tab = st.tabs(tabs)

with tab[0]:  # Summary of Arguments
    # View mode toggle
    col1, col2, col3 = st.columns([6, 2, 2])
    with col3:
        toggle_cols = st.columns(2)
        with toggle_cols[0]:
            standard_btn = st.button("Standard View", key="standard_view")
            if standard_btn:
                st.session_state.view_mode = 'default'
        with toggle_cols[1]:
            topic_btn = st.button("Topic View", key="topic_view")
            if topic_btn:
                st.session_state.view_mode = 'hierarchical'
    
    # Function to render an argument section
    def render_argument_section(id, title, paragraphs, side, level=0, 
                                overview=None, legal_points=None, factual_points=None, 
                                evidence=None, case_law=None):
        expanded = st.session_state.expanded_args.get(f"{side}_{id}", False)
        
        # Define colors based on side
        color_class = "claimant-color" if side == "claimant" else "respondent-color"
        primary_color = "#2563eb" if side == "claimant" else "#dc2626"
        
        # Header with expand/collapse control
        header_html = f"""
        <div class="argument-header {color_class}">
            <div style="display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">{id}. {title}</span>
                <span class="tag tag-{color_class.split('-')[0]}" style="font-size: 0.75rem;">¶{paragraphs}</span>
            </div>
        </div>
        """
        st.markdown(header_html, unsafe_allow_html=True)
        
        # Handle click through Streamlit buttons (hidden with CSS styling)
        if st.button(f"Toggle {id}", key=f"toggle_{side}_{id}", help=f"Expand/collapse {title}"):
            st.session_state.expanded_args[f"{side}_{id}"] = not st.session_state.expanded_args.get(f"{side}_{id}", False)
            st.rerun()
        
        # Content (only shown if expanded)
        if expanded:
            with st.container():
                # Overview points
                if overview and overview.get('points'):
                    st.markdown("<h6 style='font-size: 0.875rem; font-weight: 600; margin-bottom: 0.5rem;'>Key Points</h6>", unsafe_allow_html=True)
                    for point in overview['points']:
                        st.markdown(f"<div style='display: flex; align-items: center; margin-bottom: 0.25rem;'>"
                                   f"<div style='width: 0.375rem; height: 0.375rem; border-radius: 9999px; background-color: {primary_color}; margin-right: 0.5rem;'></div>"
                                   f"<span style='font-size: 0.875rem;'>{point}</span>"
                                   f"</div>", unsafe_allow_html=True)
                
                # Legal points
                if legal_points and len(legal_points) > 0:
                    st.markdown("<h6 style='font-size: 0.875rem; font-weight: 600; margin-top: 1rem; margin-bottom: 0.5rem;'>Legal Points</h6>", unsafe_allow_html=True)
                    for point in legal_points:
                        st.markdown(f"""
                        <div class="card-component" style="background-color: #dbeafe;">
                            <div style="display: flex; gap: 0.5rem; margin-bottom: 0.25rem;">
                                <span class="tag tag-blue">Legal</span>
                                {"<span class='tag tag-red'>Disputed</span>" if point.get('isDisputed') else ""}
                            </div>
                            <p style="font-size: 0.875rem; margin-bottom: 0.5rem;">{point['point']}</p>
                            <div style="display: flex; flex-wrap: wrap; gap: 0.25rem;">
                                {' '.join([f'<span class="tag tag-blue">{reg}</span>' for reg in point.get('regulations', [])])}
                                <span style="font-size: 0.75rem; color: #6b7280;">¶{point.get('paragraphs', '')}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Factual points
                if factual_points and len(factual_points) > 0:
                    st.markdown("<h6 style='font-size: 0.875rem; font-weight: 600; margin-top: 1rem; margin-bottom: 0.5rem;'>Factual Points</h6>", unsafe_allow_html=True)
                    for point in factual_points:
                        st.markdown(f"""
                        <div class="card-component" style="background-color: #dcfce7;">
                            <div style="display: flex; gap: 0.5rem; margin-bottom: 0.25rem;">
                                <span class="tag tag-green">Factual</span>
                                {"<span class='tag tag-red'>Disputed by " + point.get('source', '') + "</span>" if point.get('isDisputed') else ""}
                            </div>
                            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;">
                                <span style="font-size: 0.75rem; color: #6b7280;">{point.get('date', '')}</span>
                            </div>
                            <p style="font-size: 0.875rem; margin-bottom: 0.25rem;">{point['point']}</p>
                            <span style="font-size: 0.75rem; color: #6b7280;">¶{point.get('paragraphs', '')}</span>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Evidence
                if evidence and len(evidence) > 0:
                    st.markdown("<h6 style='font-size: 0.875rem; font-weight: 600; margin-top: 1rem; margin-bottom: 0.5rem;'>Evidence</h6>", unsafe_allow_html=True)
                    for item in evidence:
                        st.markdown(f"""
                        <div class="card-component">
                            <div style="display: flex; justify-content: space-between;">
                                <div>
                                    <p style="font-size: 0.875rem; font-weight: 500;">{item.get('id', '')}: {item.get('title', '')}</p>
                                    <p style="font-size: 0.75rem; color: #6b7280; margin-top: 0.25rem;">{item.get('summary', '')}</p>
                                    <div style="margin-top: 0.5rem;">
                                        <span style="font-size: 0.75rem; color: #6b7280;">Cited in: </span>
                                        {' '.join([f'<span class="tag tag-gray">¶{cite}</span>' for cite in item.get('citations', [])])}
                                    </div>
                                </div>
                                <button style="background: none; border: none; color: #2563eb; cursor: pointer;">
                                    <span style="font-size: 0.875rem;">View</span>
                                </button>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Case Law
                if case_law and len(case_law) > 0:
                    st.markdown("<h6 style='font-size: 0.875rem; font-weight: 600; margin-top: 1rem; margin-bottom: 0.5rem;'>Case Law</h6>", unsafe_allow_html=True)
                    for item in case_law:
                        st.markdown(f"""
                        <div class="card-component">
                            <div style="display: flex; justify-content: space-between;">
                                <div>
                                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                                        <p style="font-size: 0.875rem; font-weight: 500;">{item.get('caseNumber', '')}</p>
                                        <span style="font-size: 0.75rem; color: #6b7280;">¶{item.get('paragraphs', '')}</span>
                                    </div>
                                    <p style="font-size: 0.75rem; color: #6b7280; margin-top: 0.25rem;">{item.get('title', '')}</p>
                                    <p style="font-size: 0.875rem; margin-top: 0.5rem;">{item.get('relevance', '')}</p>
                                    {f'''
                                    <div style="margin-top: 0.5rem;">
                                        <span style="font-size: 0.75rem; color: #6b7280;">Key Paragraphs: </span>
                                        {' '.join([f'<span class="tag tag-gray">¶{para}</span>' for para in item.get('citedParagraphs', [])])}
                                    </div>
                                    ''' if item.get('citedParagraphs') else ''}
                                </div>
                                <button style="background: none; border: none; color: #2563eb; cursor: pointer;">
                                    <span style="font-size: 0.875rem;">View</span>
                                </button>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

    # Define the argument data
    claimant_sporting_succession = {
        "id": "1",
        "title": "Sporting Succession",
        "paragraphs": "15-18",
        "side": "claimant",
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
                "isDisputed": False,
                "regulations": ["CAS 2016/A/4576"],
                "paragraphs": "15-17"
            }
        ],
        "factual_points": [
            {
                "point": "Continuous operation under same name since 1950",
                "date": "1950-present",
                "isDisputed": False,
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
                "caseNumber": "CAS 2016/A/4576",
                "title": "Criteria for sporting succession",
                "relevance": "Establishes key factors for succession",
                "paragraphs": "45-48",
                "citedParagraphs": ["45", "46", "47"]
            }
        ]
    }
    
    respondent_sporting_succession = {
        "id": "1",
        "title": "Sporting Succession Rebuttal",
        "paragraphs": "200-218",
        "side": "respondent",
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
                "isDisputed": False,
                "regulations": ["CAS 2017/A/5465"],
                "paragraphs": "203-205"
            }
        ],
        "factual_points": [
            {
                "point": "Operations ceased between 1975-1976",
                "date": "1975-1976",
                "isDisputed": True,
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
                "caseNumber": "CAS 2017/A/5465",
                "title": "Operational continuity requirement",
                "relevance": "Establishes primacy of operational continuity",
                "paragraphs": "211-213",
                "citedParagraphs": ["212"]
            }
        ]
    }
    
    claimant_doping = {
        "id": "2",
        "title": "Doping Violation Chain of Custody",
        "paragraphs": "70-125",
        "side": "claimant",
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
                "isDisputed": False,
                "regulations": ["WADA Code 2021", "International Standard for Testing"],
                "paragraphs": "73-75"
            }
        ]
    }
    
    respondent_doping = {
        "id": "2",
        "title": "Doping Chain of Custody Defense",
        "paragraphs": "250-290",
        "side": "respondent",
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
                "isDisputed": False,
                "regulations": ["CAS 2019/A/6148"],
                "paragraphs": "253-255"
            }
        ]
    }

    # Topic view data
    topic_sections = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "claimant_args": claimant_sporting_succession,
            "respondent_args": respondent_sporting_succession
        },
        {
            "id": "topic-2",
            "title": "Doping Violation and Chain of Custody",
            "description": "Issues related to doping test procedures and evidence handling",
            "claimant_args": claimant_doping,
            "respondent_args": respondent_doping
        }
    ]

    # Default view (standard side-by-side)
    if st.session_state.view_mode == 'default':
        st.markdown("""
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1rem;">
            <div>
                <h2 style="font-size: 1.125rem; font-weight: 600; color: #2563eb; margin-bottom: 1rem;">Claimant's Arguments</h2>
            </div>
            <div>
                <h2 style="font-size: 1.125rem; font-weight: 600; color: #dc2626; margin-bottom: 1rem;">Respondent's Arguments</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Argument pair 1: Sporting Succession
        cols1 = st.columns(2)
        with cols1[0]:
            render_argument_section(**claimant_sporting_succession)
        with cols1[1]:
            render_argument_section(**respondent_sporting_succession)
            
        # Argument pair 2: Doping
        cols2 = st.columns(2)
        with cols2[0]:
            render_argument_section(**claimant_doping)
        with cols2[1]:
            render_argument_section(**respondent_doping)
    
    # Hierarchical Topic View
    else:
        for topic in topic_sections:
            st.markdown(f"""
            <div class="topic-section">
                <div class="topic-title">{topic['title']}</div>
                <div class="topic-description">{topic['description']}</div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1rem; padding: 0 1rem;">
                    <div>
                        <h3 style="font-size: 1rem; font-weight: 600; color: #2563eb; margin-bottom: 0.5rem;">Claimant's Arguments</h3>
                    </div>
                    <div>
                        <h3 style="font-size: 1rem; font-weight: 600; color: #dc2626; margin-bottom: 0.5rem;">Respondent's Arguments</h3>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Render the argument pair
            cols = st.columns(2)
            with cols[0]:
                render_argument_section(**topic['claimant_args'])
            with cols[1]:
                render_argument_section(**topic['respondent_args'])
            
            st.markdown("</div>", unsafe_allow_html=True)

with tab[1]:  # Timeline
    # Action buttons
    col1, col2, col3 = st.columns([8, 2, 2])
    with col2:
        st.button("Copy", key="copy_timeline")
    with col3:
        st.button("Export Data", key="export_timeline")
    
    # Search and filter
    search_cols = st.columns([4, 2, 6])
    with search_cols[0]:
        search_events = st.text_input("", placeholder="Search events...", label_visibility="collapsed")
    with search_cols[1]:
        st.button("Filter", key="filter_button")
    with search_cols[2]:
        show_disputed = st.checkbox("Disputed events only", key="show_disputed")

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
        }
    ]

    # Filter timeline data
    filtered_timeline = timeline_data
    if search_events:
        filtered_timeline = [item for item in filtered_timeline if 
                            search_events.lower() in item["appellant_version"].lower() or 
                            search_events.lower() in item["respondent_version"].lower()]
    if show_disputed:
        filtered_timeline = [item for item in filtered_timeline if item["status"] == "Disputed"]

    # Display timeline table
    st.markdown("""
    <table class="styled-table">
        <thead>
            <tr>
                <th>DATE</th>
                <th>APPELLANT'S VERSION</th>
                <th>RESPONDENT'S VERSION</th>
                <th>STATUS</th>
            </tr>
        </thead>
        <tbody>
    """, unsafe_allow_html=True)
    
    for item in filtered_timeline:
        disputed_class = "disputed-row" if item["status"] == "Disputed" else ""
        status_color = "color: #dc2626;" if item["status"] == "Disputed" else "color: #059669;"
        
        st.markdown(f"""
        <tr class="{disputed_class}">
            <td>{item["date"]}</td>
            <td>{item["appellant_version"]}</td>
            <td>{item["respondent_version"]}</td>
            <td style="{status_color}">{item["status"]}</td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("</tbody></table>", unsafe_allow_html=True)

with tab[2]:  # Exhibits
    # Action buttons
    col1, col2, col3 = st.columns([8, 2, 2])
    with col2:
        st.button("Copy", key="copy_exhibits")
    with col3:
        st.button("Export Data", key="export_exhibits")
    
    # Search and filters
    search_cols = st.columns([4, 3, 3])
    with search_cols[0]:
        search_exhibits = st.text_input("", placeholder="Search exhibits...", label_visibility="collapsed")
    with search_cols[1]:
        party_filter = st.selectbox("", options=["All Parties", "Appellant", "Respondent"], label_visibility="collapsed")
    with search_cols[2]:
        type_filter = st.selectbox("", options=["All Types", "contract", "letter", "communication", "statement", "regulations", "schedule"], label_visibility="collapsed")

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

    # Filter exhibits data
    filtered_exhibits = exhibits_data
    if search_exhibits:
        filtered_exhibits = [item for item in filtered_exhibits if 
                            search_exhibits.lower() in item["title"].lower() or 
                            search_exhibits.lower() in item["summary"].lower() or 
                            search_exhibits.lower() in item["id"].lower()]
    if party_filter != "All Parties":
        filtered_exhibits = [item for item in filtered_exhibits if item["party"] == party_filter]
    if type_filter != "All Types":
        filtered_exhibits = [item for item in filtered_exhibits if item["type"] == type_filter]

    # Display exhibits table
    st.markdown("""
    <table class="styled-table">
        <thead>
            <tr>
                <th>EXHIBIT ID</th>
                <th>PARTY</th>
                <th>TITLE</th>
                <th>TYPE</th>
                <th>SUMMARY</th>
                <th style="text-align: right;">ACTIONS</th>
            </tr>
        </thead>
        <tbody>
    """, unsafe_allow_html=True)
    
    for item in filtered_exhibits:
        party_class = "tag-blue" if item["party"] == "Appellant" else "tag-red"
        
        st.markdown(f"""
        <tr>
            <td>{item["id"]}</td>
            <td><span class="tag {party_class}">{item["party"]}</span></td>
            <td>{item["title"]}</td>
            <td><span class="tag tag-gray">{item["type"]}</span></td>
            <td>{item["summary"]}</td>
            <td style="text-align: right;"><a href="#" style="color: #2563eb; text-decoration: none;">View</a></td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("</tbody></table>", unsafe_allow_html=True)
