import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
import json

# Set page configuration
st.set_page_config(
    page_title="Legal Analysis Interface",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #f9fafb;
        padding: 0;
    }
    
    /* Card styling */
    .stTabs [data-baseweb="tab-panel"] {
        background-color: white;
        border-radius: 0.5rem;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        padding: 1rem;
        margin-top: 1rem;
    }
    
    /* Headers */
    .header-blue {
        color: #2563eb;
        font-weight: 600;
    }
    .header-red {
        color: #dc2626;
        font-weight: 600;
    }
    
    /* Arguments */
    .argument {
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        overflow: hidden;
    }
    .argument-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem 1rem;
        cursor: pointer;
    }
    .argument-header:hover {
        background-color: #f9fafb;
    }
    .argument-content {
        padding: 1rem;
        background-color: white;
    }
    
    /* Badges */
    .badge {
        font-size: 0.75rem;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
    }
    .badge-blue {
        background-color: #dbeafe;
        color: #1e40af;
    }
    .badge-red {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    .badge-green {
        background-color: #d1fae5;
        color: #065f46;
    }
    .badge-gray {
        background-color: #f3f4f6;
        color: #374151;
    }
    
    /* Table styling */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
    }
    .styled-table th {
        background-color: #f9fafb;
        padding: 0.75rem 1rem;
        text-align: left;
        font-size: 0.875rem;
        color: #6b7280;
        border-bottom: 1px solid #e5e7eb;
    }
    .styled-table td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #e5e7eb;
        font-size: 0.875rem;
    }
    .disputed-row {
        background-color: #fee2e2;
    }
    
    /* View toggle button */
    .view-toggle {
        background-color: #f3f4f6;
        border-radius: 0.375rem;
        padding: 0.25rem;
        display: inline-flex;
    }
    .view-toggle button {
        padding: 0.5rem 0.75rem;
        font-size: 0.875rem;
        font-weight: 500;
        border-radius: 0.25rem;
        border: none;
        cursor: pointer;
    }
    .view-toggle button.active {
        background-color: white;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    }
    .view-toggle button:not(.active) {
        color: #6b7280;
    }
    .view-toggle button:not(.active):hover {
        color: #4b5563;
    }
    
    /* Timeline */
    .timeline-row-disputed {
        background-color: #fee2e2;
    }
    
    /* Column structure */
    .two-column {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }
    
    /* Custom sidebar */
    .sidebar {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }
    
    /* Topic view */
    .topic-header {
        margin-bottom: 1rem;
    }
    .topic-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1f2937;
    }
    .topic-description {
        font-size: 0.875rem;
        color: #6b7280;
    }
    
    /* Custom button */
    .view-button {
        color: #2563eb;
        background: none;
        border: none;
        padding: 0;
        cursor: pointer;
        font-size: 0.875rem;
    }
    .view-button:hover {
        text-decoration: underline;
    }
    
    /* Fix for expander arrow */
    .streamlit-expanderHeader svg {
        color: #6b7280;
    }
    
    /* Panel separation line */
    .panel-divider {
        border-top: 1px solid #e5e7eb;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for expanded arguments and view mode
if 'expanded_arguments' not in st.session_state:
    st.session_state.expanded_arguments = set()
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'default'

# Toggle function for expanding/collapsing arguments
def toggle_argument(arg_id):
    if arg_id in st.session_state.expanded_arguments:
        st.session_state.expanded_arguments.remove(arg_id)
    else:
        st.session_state.expanded_arguments.add(arg_id)

# Function to toggle view mode
def set_view_mode(mode):
    st.session_state.view_mode = mode

# Card container
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h1>Legal Arguments Analysis</h1>', unsafe_allow_html=True)

# Tab navigation
tabs = st.tabs(["Summary of Arguments", "Timeline", "Exhibits"])

# SUMMARY OF ARGUMENTS TAB
with tabs[0]:
    # View mode toggle
    col1, col2 = st.columns([10, 2])
    with col2:
        st.markdown(f"""
        <div class="view-toggle">
            <button class="{'active' if st.session_state.view_mode == 'default' else ''}" onclick="
                const event = new CustomEvent('streamlit:toggleViewMode', {{ detail: 'default' }});
                window.dispatchEvent(event);
            ">Standard View</button>
            <button class="{'active' if st.session_state.view_mode == 'hierarchical' else ''}" onclick="
                const event = new CustomEvent('streamlit:toggleViewMode', {{ detail: 'hierarchical' }});
                window.dispatchEvent(event);
            ">Topic View</button>
        </div>
        
        <script>
            window.addEventListener('streamlit:toggleViewMode', function(e) {{
                const data = {{mode: e.detail}};
                const encoded = new TextEncoder().encode(JSON.stringify(data));
                window.pywebview.api.setViewMode(e.detail);
            }});
        </script>
        """, unsafe_allow_html=True)
        
        # Custom component to handle view mode toggle via JavaScript
        components.html("""
        <script>
        if (window.frameElement) {
            // Check if we're in an iframe
            window.parent.document.addEventListener('streamlit:toggleViewMode', function(e) {
                if (e && e.detail) {
                    // Send to Streamlit
                    window.parent.postMessage({
                        type: 'streamlit:setComponentValue',
                        value: e.detail
                    }, '*');
                }
            });
        }
        </script>
        """, height=0, key='view_mode_handler')
    
    # Definition of argument data
    claimant_arguments = {
        "1": {
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
            "children": [
                {
                    "id": "1.1",
                    "title": "Club Name Analysis",
                    "paragraphs": "20-45"
                },
                {
                    "id": "1.2",
                    "title": "Club Colors Analysis",
                    "paragraphs": "46-65"
                }
            ]
        },
        "2": {
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
            "children": []
        }
    }
    
    respondent_arguments = {
        "1": {
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
            "children": [
                {
                    "id": "1.1",
                    "title": "Club Name Analysis Rebuttal",
                    "paragraphs": "220-240"
                },
                {
                    "id": "1.2",
                    "title": "Club Colors Analysis Rebuttal",
                    "paragraphs": "241-249"
                }
            ]
        },
        "2": {
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
            "children": []
        }
    }
    
    # Topic sections for hierarchical view
    topic_sections = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "argument_ids": ["1"]
        },
        {
            "id": "topic-2",
            "title": "Doping Violation and Chain of Custody",
            "description": "Issues related to doping test procedures and evidence handling",
            "argument_ids": ["2"]
        }
    ]
    
    # Render the argument section
    def render_argument_section(arg_id, arg_data, side):
        # Determine styling based on side
        color = "blue" if side == "claimant" else "red"
        
        # Check if argument is expanded
        is_expanded = arg_id in st.session_state.expanded_arguments
        
        # Create expander for argument
        expander = st.expander(
            f"{arg_id}. {arg_data['title']} (¶{arg_data['paragraphs']})",
            expanded=is_expanded
        )
        
        # Set expander styling based on side
        expander.markdown(f"""
        <script>
            // Apply styling to the last created expander
            var expanders = document.querySelectorAll('.streamlit-expanderHeader');
            var lastExpander = expanders[expanders.length - 1];
            lastExpander.style.backgroundColor = '{color == "blue" ? "#dbeafe" : "#fee2e2"}';
            lastExpander.style.borderRadius = '0.375rem';
            lastExpander.style.borderWidth = '1px';
            lastExpander.style.borderColor = '{color == "blue" ? "#93c5fd" : "#fca5a5"}';
            lastExpander.querySelector('span').style.color = '{color == "blue" ? "#1e40af" : "#b91c1c"}';
        </script>
        """, unsafe_allow_html=True)
        
        with expander:
            # Overview points
            if "overview" in arg_data and arg_data["overview"]["points"]:
                st.markdown("<h5>Key Points</h5>", unsafe_allow_html=True)
                for point in arg_data["overview"]["points"]:
                    st.markdown(f"• {point}")
                st.markdown(f"<small>¶{arg_data['overview']['paragraphs']}</small>", unsafe_allow_html=True)
                st.markdown("<hr>", unsafe_allow_html=True)
            
            # Legal points
            if "legal_points" in arg_data and arg_data["legal_points"]:
                st.markdown("<h5>Legal Points</h5>", unsafe_allow_html=True)
                for point in arg_data["legal_points"]:
                    st.markdown(f"""
                    <div style="background-color: #dbeafe; padding: 0.75rem; border-radius: 0.375rem; margin-bottom: 0.5rem;">
                        <div>
                            <span class="badge badge-blue">Legal</span>
                            {' <span class="badge badge-red">Disputed</span>' if point.get('is_disputed', False) else ''}
                        </div>
                        <p>{point['point']}</p>
                        <div>
                            {''.join([f'<span class="badge badge-blue">{reg}</span> ' for reg in point.get('regulations', [])])}
                            <span class="badge badge-gray">¶{point['paragraphs']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Factual points
            if "factual_points" in arg_data and arg_data["factual_points"]:
                st.markdown("<h5>Factual Points</h5>", unsafe_allow_html=True)
                for point in arg_data["factual_points"]:
                    st.markdown(f"""
                    <div style="background-color: #d1fae5; padding: 0.75rem; border-radius: 0.375rem; margin-bottom: 0.5rem;">
                        <div>
                            <span class="badge badge-green">Factual</span>
                            {f'<span class="badge badge-red">Disputed by {point["source"]}</span>' if point.get('is_disputed', False) else ''}
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.5rem; margin: 0.25rem 0;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                <line x1="3" y1="10" x2="21" y2="10"></line>
                            </svg>
                            <span style="font-size: 0.75rem; color: #6b7280;">{point['date']}</span>
                        </div>
                        <p>{point['point']}</p>
                        <span style="font-size: 0.75rem; color: #6b7280;">¶{point['paragraphs']}</span>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Evidence
            if "evidence" in arg_data and arg_data["evidence"]:
                st.markdown("<h5>Evidence</h5>", unsafe_allow_html=True)
                for ev in arg_data["evidence"]:
                    st.markdown(f"""
                    <div style="background-color: #f3f4f6; padding: 0.75rem; border-radius: 0.375rem; margin-bottom: 0.5rem;">
                        <div style="display: flex; justify-content: space-between;">
                            <div>
                                <p style="font-weight: 500;">{ev['id']}: {ev['title']}</p>
                                <p style="font-size: 0.75rem; color: #6b7280; margin-top: 0.25rem;">{ev['summary']}</p>
                                <div style="margin-top: 0.5rem;">
                                    <span style="font-size: 0.75rem; color: #6b7280;">Cited in: </span>
                                    {''.join([f'<span class="badge badge-gray">¶{cite}</span> ' for cite in ev.get('citations', [])])}
                                </div>
                            </div>
                            <button class="view-button">Link</button>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Case Law
            if "case_law" in arg_data and arg_data["case_law"]:
                st.markdown("<h5>Case Law</h5>", unsafe_allow_html=True)
                for case in arg_data["case_law"]:
                    st.markdown(f"""
                    <div style="background-color: #f3f4f6; padding: 0.75rem; border-radius: 0.375rem; margin-bottom: 0.5rem;">
                        <div style="display: flex; justify-content: space-between;">
                            <div>
                                <div style="display: flex; align-items: center; gap: 0.5rem;">
                                    <p style="font-weight: 500;">{case['case_number']}</p>
                                    <span style="font-size: 0.75rem; color: #6b7280;">¶{case['paragraphs']}</span>
                                </div>
                                <p style="font-size: 0.75rem; color: #6b7280; margin-top: 0.25rem;">{case['title']}</p>
                                <p style="margin-top: 0.5rem;">{case['relevance']}</p>
                                {
                                    f'''
                                    <div style="margin-top: 0.5rem;">
                                        <span style="font-size: 0.75rem; color: #6b7280;">Key Paragraphs: </span>
                                        {''.join([f'<span class="badge badge-gray">¶{para}</span> ' for para in case.get('cited_paragraphs', [])])}
                                    </div>
                                    ''' if 'cited_paragraphs' in case else ''
                                }
                            </div>
                            <button class="view-button">Link</button>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Function to render side-by-side arguments
    def render_argument_pair(claimant_id, respondent_id, level=0):
        claimant_data = claimant_arguments.get(claimant_id)
        respondent_data = respondent_arguments.get(respondent_id)
        
        if not claimant_data or not respondent_data:
            return
        
        # Create columns for side-by-side display
        col1, col2 = st.columns(2)
        
        # Render arguments
        with col1:
            render_argument_section(claimant_id, claimant_data, "claimant")
        
        with col2:
            render_argument_section(respondent_id, respondent_data, "respondent")
        
        # Check if we need to render children
        is_expanded = claimant_id in st.session_state.expanded_arguments
        
        if is_expanded and "children" in claimant_data and "children" in respondent_data:
            # Get children to render
            for i in range(min(len(claimant_data["children"]), len(respondent_data["children"]))):
                c_child = claimant_data["children"][i]
                r_child = respondent_data["children"][i]
                render_argument_pair(c_child["id"], r_child["id"], level + 1)
    
    # Function to render hierarchical view
    def render_hierarchical_view():
        for topic in topic_sections:
            st.markdown(f"""
            <div class="topic-header">
                <div class="topic-title">{topic['title']}</div>
                <div class="topic-description">{topic['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Create columns for headers
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<h3 class="header-blue">Claimant\'s Arguments</h3>', unsafe_allow_html=True)
            with col2:
                st.markdown('<h3 class="header-red">Respondent\'s Arguments</h3>', unsafe_allow_html=True)
            
            # Render argument pairs for this topic
            for arg_id in topic["argument_ids"]:
                render_argument_pair(arg_id, arg_id)
            
            # Add separator between topics
            st.markdown("<hr>", unsafe_allow_html=True)
    
    # Render appropriate view based on mode
    if st.session_state.view_mode == 'default':
        # Standard view with side-by-side arguments
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h3 class="header-blue">Claimant\'s Arguments</h3>', unsafe_allow_html=True)
        with col2:
            st.markdown('<h3 class="header-red">Respondent\'s Arguments</h3>', unsafe_allow_html=True)
        
        # Render each argument pair
        for arg_id in claimant_arguments:
            render_argument_pair(arg_id, arg_id)
    else:
        # Hierarchical view grouped by topics
        render_hierarchical_view()

# TIMELINE TAB
with tabs[1]:
    st.markdown("""
    <div style="display: flex; justify-content: flex-end; margin-bottom: 1rem;">
        <button class="streamlit-button">Copy</button>
        <button class="streamlit-button" style="margin-left: 0.5rem;">Export Data</button>
    </div>
    """, unsafe_allow_html=True)
    
    # Search and filter inputs
    col1, col2 = st.columns([7, 3])
    with col1:
        search = st.text_input("", placeholder="Search events...", label_visibility="collapsed")
    with col2:
        disputed_only = st.checkbox("Disputed events only")
    
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
    if search:
        timeline_data = [item for item in timeline_data if 
                         search.lower() in item["appellant_version"].lower() or 
                         search.lower() in item["respondent_version"].lower()]
    
    if disputed_only:
        timeline_data = [item for item in timeline_data if item["status"] == "Disputed"]
    
    # Create DataFrame
    df = pd.DataFrame(timeline_data)
    
    # Apply styling
    def style_timeline_row(row):
        if row["status"] == "Disputed":
            return ["background-color: #fee2e2"] * len(row)
        return [""] * len(row)
    
    # Create styled table
    styled_df = df.style.apply(style_timeline_row, axis=1)
    
    # Display the table
    st.table(styled_df)

# EXHIBITS TAB
with tabs[2]:
    st.markdown("""
    <div style="display: flex; justify-content: flex-end; margin-bottom: 1rem;">
        <button class="streamlit-button">Copy</button>
        <button class="streamlit-button" style="margin-left: 0.5rem;">Export Data</button>
    </div>
    """, unsafe_allow_html=True)
    
    # Search and filters
    col1, col2, col3 = st.columns([5, 2, 2])
    with col1:
        exhibits_search = st.text_input("", placeholder="Search exhibits...", label_visibility="collapsed")
    with col2:
        party_filter = st.selectbox("", ["All Parties", "Appellant", "Respondent"], label_visibility="collapsed")
    with col3:
        type_filter = st.selectbox("", ["All Types", "contract", "letter", "communication", "statement", "regulations", "schedule"], label_visibility="collapsed")
    
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
    if exhibits_search:
        exhibits_data = [item for item in exhibits_data if 
                         exhibits_search.lower() in item["title"].lower() or 
                         exhibits_search.lower() in item["summary"].lower() or
                         exhibits_search.lower() in item["id"].lower()]
    
    if party_filter != "All Parties":
        exhibits_data = [item for item in exhibits_data if item["party"] == party_filter]
    
    if type_filter != "All Types":
        exhibits_data = [item for item in exhibits_data if item["type"] == type_filter]
    
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
                <th>ACTIONS</th>
            </tr>
        </thead>
        <tbody>
    """, unsafe_allow_html=True)
    
    for item in exhibits_data:
        party_badge_color = "blue" if item["party"] == "Appellant" else "red"
        st.markdown(f"""
        <tr>
            <td>{item['id']}</td>
            <td><span class="badge badge-{party_badge_color}">{item['party']}</span></td>
            <td>{item['title']}</td>
            <td><span class="badge badge-gray">{item['type']}</span></td>
            <td>{item['summary']}</td>
            <td><button class="view-button">View</button></td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("</tbody></table>", unsafe_allow_html=True)

# JavaScript for handling interactions
st.markdown("""
<script>
// Custom view mode toggle handler
document.addEventListener('DOMContentLoaded', function() {
    // Set up event handlers for view mode toggle
    const viewToggleHandler = function(event) {
        if (event.detail) {
            // Send to Python
            const data = {mode: event.detail};
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                value: data
            }, '*');
        }
    };
    
    window.addEventListener('streamlit:toggleViewMode', viewToggleHandler);
});
</script>
""", unsafe_allow_html=True)
