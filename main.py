import streamlit as st
import pandas as pd
from datetime import datetime, date
import time
import random

# Page configuration
st.set_page_config(
    page_title="Caselens - Legal Research Platform",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'search_history' not in st.session_state:
    st.session_state.search_history = []
if 'bookmarked_cases' not in st.session_state:
    st.session_state.bookmarked_cases = []
if 'current_case' not in st.session_state:
    st.session_state.current_case = None
if 'saved_searches' not in st.session_state:
    st.session_state.saved_searches = [
        {
            "id": "search_1",
            "name": "\"just cause\" + 3 filters",
            "query": "just cause",
            "filters": {"sport": "Football", "matter": "Contract", "outcome": "Any"},
            "saved_date": "2024-07-20",
            "last_run": "2 hours ago",
            "description": "Looking for employment termination precedents in football",
            "results_count": "15 relevant passages in 13 decisions"
        },
        {
            "id": "search_2", 
            "name": "\"transfer disputes\" + 2 filters",
            "query": "transfer disputes",
            "filters": {"sport": "Football", "date_range": "2020-2024"},
            "saved_date": "2024-07-19",
            "last_run": "1 day ago",
            "description": "Research for client consultation",
            "results_count": "8 relevant passages in 5 decisions"
        }
    ]
if 'saved_cases' not in st.session_state:
    st.session_state.saved_cases = [
        {
            "id": "CAS_2020_A_7242",
            "title": "Al Wahda FSC v. Mourad Batna",
            "case_ref": "CAS 2020/A/7242",
            "saved_date": "today",
            "description": "Key precedent for wage disputes. Compare with similar cases.",
            "notes": "Key precedent for wage disputes. Compare with similar cases. Player had valid just cause due to unpaid wages and hostile work environment."
        },
        {
            "id": "CAS_2022_A_8836",
            "title": "Samsunspor v. Brice Dja...",
            "case_ref": "CAS 2022/A/8836",
            "saved_date": "yesterday",
            "description": "Important for understanding burden of proof in just cause cases.",
            "notes": ""
        },
        {
            "id": "CAS_2019_A_6082",
            "title": "Barcelona FC v. Neymar Jr",
            "case_ref": "CAS 2019/A/6082",
            "saved_date": "last week",
            "description": "Release clause jurisprudence - cite in contract review",
            "notes": ""
        }
    ]
if 'case_notes' not in st.session_state:
    st.session_state.case_notes = {}

# Sample case database (expanded)
CASES_DATABASE = [
    {
        "id": "CAS_2013_A_3165",
        "title": "CAS 2013/A/3165",
        "date": "2014-01-14",
        "procedure": "Appeal Arbitration",
        "matter": "Contract",
        "category": "Award",
        "outcome": "Dismissed",
        "sport": "Football",
        "appellants": "FC Volyn",
        "respondents": "Issa Ndoye",
        "president": "Petros Mavroidis",
        "arbitrator1": "Geraint Jones",
        "arbitrator2": "Raymond Hack",
        "summary": "The case involves a contractual dispute between FC Volyn, a Ukrainian football club, and Issa Ndoye, a Senegalese footballer. Ndoye terminated his employment with FC Volyn in June 2011, claiming unpaid salary and contract breach, subsequently bringing a claim before FIFA's Dispute Resolution Chamber (DRC), which ruled in his favor, ordering the club to pay outstanding remuneration and compensation. FC Volyn appealed to the CAS, arguing that Ndoye had no just cause due to his alleged breaches (mainly late returns to training), while Ndoye countered that non-payment constituted just cause and sought increased compensation. Both parties debated applicable law and timing of appeals/counterclaims.",
        "court_reasoning": "The CAS panel found that FIFA regulations take precedence over national law due to the contract's terms and parties' submission to FIFA/CAS jurisdiction. The Club's repeated failure to pay Ndoye's salary for over three months was a substantial breach, constituting just cause for contract termination. Alleged late returns by Ndoye did not nullify this breach, and there was no evidence he agreed to delay payment. Counterclaims by respondents were inadmissible per CAS procedural rules. The compensation set by the FIFA DRC was appropriate.",
        "case_outcome": "The appeal by FC Volyn was dismissed and the FIFA DRC's decision was upheld: FC Volyn must pay Ndoye USD 299,200 in outstanding remuneration and USD 495,000 as compensation. Ndoye's counterclaim for additional damages was ruled inadmissible, and all other requests were dismissed. The panel confirmed that the time limit for appeal had been respected and that FIFA regulations (with Swiss law supplementary) applied.",
        "relevant_passages": [
            {
                "excerpt": "Page 15 - 78. The Commentary on the RSTP states the following with regard to the concept of 'just cause': 'The definition of just cause and whether just cause exists shall be established in accordance with the merits of each particular case.",
                "full_context": "Page 15 - 77. The concept of just cause has been extensively developed through CAS jurisprudence and FIFA regulations. The FIFA Regulations on the Status and Transfer of Players (RSTP) provide the foundational framework for determining when a party may terminate a contract.\n\nPage 15 - 78. The Commentary on the RSTP states the following with regard to the concept of 'just cause': 'The definition of just cause and whether just cause exists shall be established in accordance with the merits of each particular case. Behaviour that is in violation of the terms of an employment contract cannot justify unilateral termination by the other party if such behaviour is of minor importance.'\n\nPage 15 - 79. Furthermore, the Commentary emphasizes that just cause must be of such gravity that the injured party cannot reasonably be expected to continue the employment relationship. This standard has been consistently applied by CAS panels in determining whether contract termination was justified."
            },
            {
                "excerpt": "Page 22 - 89. Non-payment of salary constitutes a breach of contract which may give rise to just cause for the employee to terminate the employment contract.",
                "full_context": "Page 22 - 88. The obligation to pay salary is a fundamental contractual duty in employment relationships. When an employer fails to meet this basic obligation, it strikes at the heart of the employment contract.\n\nPage 22 - 89. Non-payment of salary constitutes a breach of contract which may give rise to just cause for the employee to terminate the employment contract. The CAS has consistently held that when salary payments are delayed for a period exceeding two to three months, this constitutes a substantial breach sufficient to justify termination.\n\nPage 22 - 90. However, the employee must demonstrate that they have given the employer reasonable opportunity to remedy the breach and that the non-payment was not justified by any countervailing circumstances or legitimate disputes over the amount owed."
            },
            {
                "excerpt": "Page 31 - 105. The consistent jurisprudence of CAS establishes that just cause must be of such severity that the injured party cannot reasonably be expected to continue the contractual relationship.",
                "full_context": "Page 31 - 104. In assessing whether just cause exists, CAS panels must weigh all relevant circumstances, including the nature and severity of the breach, the conduct of both parties, and the overall context of the contractual relationship.\n\nPage 31 - 105. The consistent jurisprudence of CAS establishes that just cause must be of such severity that the injured party cannot reasonably be expected to continue the contractual relationship. This objective test requires careful analysis of whether a reasonable person in the same position would consider the breach sufficiently serious to warrant termination.\n\nPage 31 - 106. The Panel notes that minor infractions, isolated incidents, or breaches that can be readily remedied do not typically constitute just cause. The breach must fundamentally undermine the basis of the contractual relationship and make continued performance unreasonable or impossible."
            }
        ],
        "similarity_score": 0.87
    },
    {
        "id": "CAS_2020_A_7242",
        "title": "CAS 2020/A/7242 - Al Wahda FSC v. Mourad Batna",
        "date": "2021-11-23",
        "procedure": "Appeal Arbitration",
        "matter": "Contract",
        "category": "Award",
        "outcome": "Partially Upheld",
        "sport": "Football",
        "appellants": "Al Wahda FSC Company",
        "respondents": "Mourad Batna",
        "president": "Sarah Johnson",
        "arbitrator1": "Michael Peters",
        "arbitrator2": "Lisa Chen",
        "summary": "This case involves Al Wahda FSC Company (UAE club), Mr. Mourad Batna (Moroccan footballer), and Al Jazira FSC (UAE club) regarding the termination of Batna's employment contract. Batna terminated his contract citing overdue wages and abusive conduct by Al Wahda, thereafter signing with Al Jazira. Al Wahda claimed Batna left without just cause, seeking compensation and sanctions.",
        "court_reasoning": "The panel found that Al Wahda's failure to pay wages for extended periods constituted a substantial breach. The hostile work environment and abusive conduct further supported just cause. The club's counterclaims were not substantiated with sufficient evidence.",
        "case_outcome": "Batna's termination was upheld as justified. Al Wahda was ordered to pay outstanding wages. Compensation claims against Batna were dismissed.",
        "relevant_passages": [
            {
                "excerpt": "Page 12 - 45. Persistent non-payment of wages combined with hostile work environment constitutes clear just cause for contract termination.",
                "full_context": "Page 12 - 44. The tribunal must assess not only the financial aspects of the breach but also the overall working conditions and treatment of the employee.\n\nPage 12 - 45. Persistent non-payment of wages combined with hostile work environment constitutes clear just cause for contract termination. When multiple breaches occur simultaneously, they create a cumulative effect that makes continuation of the employment relationship untenable.\n\nPage 12 - 46. The player demonstrated reasonable attempts to resolve issues before termination, which supports the validity of the just cause claim."
            }
        ],
        "similarity_score": 0.92
    }
]

# Custom CSS
st.markdown("""
<style>
    .main-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 24px;
    }
    
    .logo-icon {
        background-color: #6366f1;
        color: white;
        padding: 12px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 48px;
        height: 48px;
    }
    
    .nav-buttons {
        display: flex;
        gap: 8px;
        margin-bottom: 24px;
    }
    
    .nav-button-active {
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
        padding: 12px 20px;
        border-radius: 12px;
        border: none;
        font-weight: 500;
        flex: 1;
        text-align: center;
        font-size: 14px;
        box-shadow: 0 2px 4px rgba(239, 68, 68, 0.2);
    }
    
    .nav-button-inactive {
        background-color: #f8fafc;
        color: #64748b;
        padding: 12px 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        font-weight: 500;
        flex: 1;
        text-align: center;
        font-size: 14px;
    }
    
    .search-item {
        background-color: #f8fafc;
        border-radius: 12px;
        padding: 16px;
        margin: 12px 0;
        border: 1px solid #e2e8f0;
    }
    
    .search-name {
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 6px;
        color: #1e293b;
        line-height: 1.3;
    }
    
    .search-meta {
        font-size: 12px;
        color: #64748b;
        margin-bottom: 8px;
    }
    
    .case-item {
        background-color: #fefce8;
        border: 1px solid #fde047;
        border-radius: 12px;
        padding: 16px;
        margin: 12px 0;
    }
    
    .question-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    
    .current-search-header {
        background-color: #f1f5f9;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    
    .filter-counter {
        font-size: 12px;
        font-weight: 500;
        text-align: right;
        margin-bottom: 12px;
    }
    
    .active-filters {
        color: #3b82f6;
    }
    
    .no-filters {
        color: #6b7280;
    }
    
    div[data-testid="stSelectbox"] > div > div {
        font-size: 14px;
    }
    
    .stExpander > div > div > div > div {
        padding-top: 8px !important;
        padding-bottom: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

def search_cases(query, max_results=20, similarity_threshold=0.5, filters=None):
    """Search cases with comprehensive filters"""
    relevant_cases = []
    for case in CASES_DATABASE:
        # Text matching
        if query.lower() in case['summary'].lower() or query.lower() in case['court_reasoning'].lower():
            # Apply filters if provided
            if filters:
                if filters.get('sport') and filters['sport'] != 'Any' and case['sport'] != filters['sport']:
                    continue
                if filters.get('matter') and filters['matter'] != 'Any' and case['matter'] != filters['matter']:
                    continue
                if filters.get('outcome') and filters['outcome'] != 'Any' and case['outcome'] != filters['outcome']:
                    continue
                if filters.get('procedural') and filters['procedural'] != 'Any' and case['procedure'] != filters['procedural']:
                    continue
                if filters.get('category') and filters['category'] != 'Any' and case['category'] != filters['category']:
                    continue
                # Add more filter logic as needed
            
            if case['similarity_score'] >= similarity_threshold:
                relevant_cases.append(case)
    
    return relevant_cases[:max_results]

def save_current_search(search_name, query, filters, description=""):
    """Save current search with filters"""
    new_search = {
        "id": f"search_{len(st.session_state.saved_searches) + 1}",
        "name": search_name,
        "query": query,
        "filters": filters.copy(),
        "saved_date": datetime.now().strftime("%Y-%m-%d"),
        "last_run": "just now",
        "description": description,
        "results_count": f"Found in this session"
    }
    st.session_state.saved_searches.append(new_search)

def load_saved_search(search_id):
    """Load a saved search"""
    for search in st.session_state.saved_searches:
        if search['id'] == search_id:
            return search
    return None

def save_case(case):
    """Save a case to bookmarks"""
    if not any(saved['id'] == case['id'] for saved in st.session_state.saved_cases):
        saved_case = {
            "id": case['id'],
            "title": f"{case['appellants']} v. {case['respondents']}",
            "case_ref": case['title'],
            "saved_date": "today",
            "description": f"Saved from search results",
            "notes": ""
        }
        st.session_state.saved_cases.append(saved_case)
        st.success("Case saved!")
    else:
        st.info("Case already saved!")

# Sidebar Navigation
with st.sidebar:
    # Modern Logo Design
    st.markdown("""
    <div class="main-header">
        <div class="logo-icon">C</div>
        <h2 style="margin: 0; color: #1e293b; font-weight: 700; font-size: 24px;">caselens</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Modern Navigation Buttons
    st.markdown("""
    <div class="nav-buttons">
        <div class="nav-button-active">🔍 Search</div>
        <div class="nav-button-inactive">📄 Documents</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Clean Divider
    st.markdown("<hr style='margin: 24px 0; border: none; height: 1px; background: #e2e8f0;'>", unsafe_allow_html=True)
    
    # Search Options - Collapsible
    with st.expander("Search Options", expanded=False):
        max_results = st.number_input("Max Results", min_value=1, max_value=100, value=20)
        similarity = st.slider("Similarity Threshold", min_value=0.0, max_value=1.0, value=0.55, step=0.01)
        show_similarity = st.checkbox("Show Similarity Scores")
    
    # Saved Searches - Modern Design (Fixed)
    with st.expander("Saved Searches", expanded=True):
        if len(st.session_state.saved_searches) == 0:
            st.markdown("<p style='color: #64748b; font-size: 14px; text-align: center; padding: 20px 0;'>No saved searches yet</p>", unsafe_allow_html=True)
        else:
            for search in st.session_state.saved_searches:
                # Modern card design with description
                st.markdown(f"""
                <div class="search-item">
                    <div class="search-name">{search['name']}</div>
                    <div class="search-meta">Last run: {search['last_run']}</div>
                    <div style="font-size: 12px; color: #64748b; font-style: italic; margin-top: 4px;">{search.get('description', '')}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Functional buttons only (clean design)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    if st.button("Load", key=f"load_{search['id']}", help="Load this search", use_container_width=True):
                        st.session_state.loaded_search = search
                        st.rerun()
                with col3:
                    if st.button("✕", key=f"delete_{search['id']}", help="Delete search", use_container_width=True):
                        st.session_state.saved_searches = [s for s in st.session_state.saved_searches if s['id'] != search['id']]
                        st.rerun()
    
    # Saved Cases - Modern Design
    with st.expander(f"Saved Cases ({len(st.session_state.saved_cases)})", expanded=False):
        if len(st.session_state.saved_cases) == 0:
            st.markdown("<p style='color: #64748b; font-size: 14px; text-align: center; padding: 20px 0;'>No saved cases yet</p>", unsafe_allow_html=True)
        else:
            for case in st.session_state.saved_cases:
                # Modern case card
                st.markdown(f"""
                <div class="case-item">
                    <div class="search-name">{case['title']}</div>
                    <div class="search-meta">{case['case_ref']} • {case['saved_date']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Compact notes
                notes_key = f"sidebar_notes_{case['id']}"
                current_notes = case.get('notes', '')
                
                notes = st.text_area(
                    "",
                    value=current_notes,
                    key=notes_key,
                    height=50,
                    placeholder="Quick notes...",
                    label_visibility="collapsed"
                )
                
                # Update notes
                if notes != current_notes:
                    case['notes'] = notes
                
                # Action buttons
                col1, col2 = st.columns([4, 1]) 
                with col1:
                    if st.button("View", key=f"view_{case['id']}", help="View case details", use_container_width=True):
                        # Find the full case details from database
                        full_case = None
                        for db_case in CASES_DATABASE:
                            if db_case['id'] == case['id']:
                                full_case = db_case
                                break
                        
                        if full_case:
                            # Set up search to show this case
                            st.session_state.view_case_search = {
                                'query': 'just cause',  # Use a query that would match this case
                                'target_case_id': case['id'],
                                'sport_filter': full_case['sport'],
                                'matter_filter': full_case['matter'],
                                'outcome_filter': full_case['outcome']
                            }
                        st.rerun()
                with col2:
                    if st.button("✕", key=f"remove_{case['id']}", help="Remove from saved"):
                        st.session_state.saved_cases = [c for c in st.session_state.saved_cases if c['id'] != case['id']]
                        st.rerun()

    # Search Filters Section
    st.markdown("<hr style='margin: 24px 0; border: none; height: 1px; background: #e2e8f0;'>", unsafe_allow_html=True)
    
    # Filter counter
    active_filter_count = 0
    filter_keys = ['language_filter', 'matter_filter', 'outcome_filter', 'sport_filter', 'procedural_filter', 
                   'date_filter', 'arbitrators_filter', 'category_filter', 'appellants_filter', 'respondents_filter']
    for key in filter_keys:
        if st.session_state.get(key, 'Any') != 'Any':
            active_filter_count += 1
    
    # Filters header with counter
    st.markdown("**Search Filters**")
    if active_filter_count > 0:
        st.markdown(f'<div class="filter-counter active-filters">{active_filter_count} active filters</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="filter-counter no-filters">0 active filters</div>', unsafe_allow_html=True)
    
    # Filter dropdowns with default values
    language_filter = st.selectbox("Language", ["Any", "English", "French", "German", "Spanish", "Italian"], key="language_filter", index=0)
    date_filter = st.selectbox("Decision Date", ["Any", "Last 6 months", "Last year", "Last 2 years", "Last 5 years"], key="date_filter", index=0)
    
    # Handle temporary filter values for case viewing
    matter_options = ["Any", "Contract", "Transfer", "Doping", "Disciplinary", "Eligibility"]
    if 'temp_matter_filter' in st.session_state:
        temp_matter = st.session_state.temp_matter_filter
        matter_index = matter_options.index(temp_matter) if temp_matter in matter_options else 0
        del st.session_state.temp_matter_filter
    else:
        matter_index = 0
    matter_filter = st.selectbox("Matter", matter_options, key="matter_filter", index=matter_index)
    
    outcome_options = ["Any", "Dismissed", "Upheld", "Partially Upheld", "Rejected", "Accepted"]
    if 'temp_outcome_filter' in st.session_state:
        temp_outcome = st.session_state.temp_outcome_filter
        outcome_index = outcome_options.index(temp_outcome) if temp_outcome in outcome_options else 0
        del st.session_state.temp_outcome_filter
    else:
        outcome_index = 0
    outcome_filter = st.selectbox("Outcome", outcome_options, key="outcome_filter", index=outcome_index)
    
    procedural_filter = st.selectbox("Procedural Types", ["Any", "Appeal Arbitration", "Ordinary Arbitration", "Fast-Track"], key="procedural_filter", index=0)
    
    sport_options = ["Any", "Football", "Basketball", "Tennis", "Swimming", "Athletics"]
    if 'temp_sport_filter' in st.session_state:
        temp_sport = st.session_state.temp_sport_filter
        sport_index = sport_options.index(temp_sport) if temp_sport in sport_options else 0
        del st.session_state.temp_sport_filter
    else:
        sport_index = 0
    sport_filter = st.selectbox("Sport", sport_options, key="sport_filter", index=sport_index)
    
    arbitrators_filter = st.selectbox("Arbitrators", ["Any", "Petros Mavroidis", "Sarah Johnson", "Michael Peters"], key="arbitrators_filter", index=0)
    category_filter = st.selectbox("Category", ["Any", "Award", "Order", "Interim Award"], key="category_filter", index=0)
    appellants_filter = st.selectbox("Appellants", ["Any", "Player", "Club", "National Association"], key="appellants_filter", index=0)
    respondents_filter = st.selectbox("Respondents", ["Any", "Player", "Club", "National Association"], key="respondents_filter", index=0)
    
    # Reset button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Reset All Filters", use_container_width=True, type="secondary"):
        # Clear all filter session state
        all_filter_keys = ['language_filter', 'date_filter', 'matter_filter', 'outcome_filter', 
                          'procedural_filter', 'sport_filter', 'arbitrators_filter', 'category_filter',
                          'appellants_filter', 'respondents_filter']
        for key in all_filter_keys:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# Main Content Area
st.markdown("### CAS Case Law Research")

# Check if we need to show a specific case via search
if 'view_case_search' in st.session_state:
    case_search_params = st.session_state.view_case_search
    default_query = case_search_params['query']
    target_case_id = case_search_params['target_case_id']
    
    # Store desired filter values temporarily
    st.session_state.temp_sport_filter = case_search_params.get('sport_filter', 'Any')
    st.session_state.temp_matter_filter = case_search_params.get('matter_filter', 'Any') 
    st.session_state.temp_outcome_filter = case_search_params.get('outcome_filter', 'Any')
    
    # Clear the search trigger
    del st.session_state.view_case_search
else:
    target_case_id = None
    # Check if a saved search was loaded
    loaded_search = getattr(st.session_state, 'loaded_search', None)
    if loaded_search:
        default_query = loaded_search['query']
        st.session_state.loaded_search = None  # Clear after loading
    else:
        default_query = ""  # Empty by default to save space

# Search Interface
search_query = st.text_input(
    "", 
    value=default_query,
    placeholder="Enter your search query", 
    label_visibility="collapsed",
    key="main_search_input"
)

# Only show save button if there's a search query
if search_query and search_query.strip():
    if st.button("💾 Save Search", help="Save current search and filters"):
        with st.form("save_search_form"):
            st.markdown("**Save Current Search**")
            
            # Count active filters for name suggestion
            active_filters = []
            if st.session_state.get('language_filter', 'Any') != 'Any':
                active_filters.append('Language')
            if st.session_state.get('matter_filter', 'Any') != 'Any':
                active_filters.append('Matter')
            if st.session_state.get('outcome_filter', 'Any') != 'Any':
                active_filters.append('Outcome')
            if st.session_state.get('sport_filter', 'Any') != 'Any':
                active_filters.append('Sport')
            if st.session_state.get('procedural_filter', 'Any') != 'Any':
                active_filters.append('Procedural')
            
            filter_count = len(active_filters)
            search_name = st.text_input("Search Name", value=f'{search_query}')
            search_description = st.text_area("Description (optional)", placeholder="e.g., Research for client consultation")
            
            if st.form_submit_button("Save"):
                filters = {
                    "language": st.session_state.get('language_filter', 'Any'),
                    "matter": st.session_state.get('matter_filter', 'Any'),
                    "outcome": st.session_state.get('outcome_filter', 'Any'),
                    "sport": st.session_state.get('sport_filter', 'Any'),
                    "procedural": st.session_state.get('procedural_filter', 'Any'),
                    "arbitrators": st.session_state.get('arbitrators_filter', 'Any'),
                    "category": st.session_state.get('category_filter', 'Any'),
                    "appellants": st.session_state.get('appellants_filter', 'Any'),
                    "respondents": st.session_state.get('respondents_filter', 'Any'),
                    "date": st.session_state.get('date_filter', 'Any')
                }
                save_current_search(search_name, search_query, filters, search_description)
                st.success("Search saved!")
                st.rerun()

if search_query:
    # Perform search
    filters = {
        "language": st.session_state.get('language_filter', 'Any'),
        "matter": st.session_state.get('matter_filter', 'Any'),
        "outcome": st.session_state.get('outcome_filter', 'Any'),
        "sport": st.session_state.get('sport_filter', 'Any'),
        "procedural": st.session_state.get('procedural_filter', 'Any'),
        "arbitrators": st.session_state.get('arbitrators_filter', 'Any'),
        "category": st.session_state.get('category_filter', 'Any'),
        "appellants": st.session_state.get('appellants_filter', 'Any'),
        "respondents": st.session_state.get('respondents_filter', 'Any'),
        "date": st.session_state.get('date_filter', 'Any')
    }
    results = search_cases(search_query, max_results, similarity, filters)
    
    # Search results summary
    total_passages = sum(len(case.get('relevant_passages', [])) for case in results)
    st.success(f"Found {total_passages} relevant passages in {len(results)} decisions")
    
    # Show message if viewing a specific case
    if target_case_id:
        st.info(f"🎯 Showing search results for your saved case (Case ID: {target_case_id})")
    
    # Display search results with original format
    for case_index, case in enumerate(results):
        # Auto-expand the target case if we're viewing a specific saved case
        if target_case_id is not None and case['id'] == target_case_id:
            should_expand = True
        elif case_index == 0:
            should_expand = True
        else:
            should_expand = False
        
        # Clean case header with bold descriptors (original format)
        case_title = f"**{case['title']}** | 📅 **Date:** {case['date']} | 👥 **Parties:** {case['appellants']} v. {case['respondents']} | 📝 **Matter:** {case['matter']} | 📄 **Outcome:** {case['outcome']} | 🏅 **Sport:** {case['sport']}"
        
        with st.expander(case_title, expanded=should_expand):
            
            st.markdown(f"""
            **Procedure:** {case['procedure']}  
            **Category:** {case['category']}  
            **President:** {case['president']} | **Arbitrators:** {case['arbitrator1']}, {case['arbitrator2']}
            """)
            
            # Relevant Passages - Most important, moved to top (original format)
            st.markdown("### **Relevant Passages**")
            for passage_index, passage in enumerate(case['relevant_passages']):
                passage_unique_key = f"show_more_{case['id']}_{passage_index}_{case_index}"
                
                # Extract page reference and content for excerpt (original logic)
                excerpt_text = passage['excerpt']
                if excerpt_text.startswith('Page'):
                    if '.' in excerpt_text:
                        page_ref = excerpt_text.split(' - ')[0]
                        content = excerpt_text.split('.', 1)[1]
                        
                        # Put page and checkbox on same line (original format)
                        show_more = st.checkbox(f"show more | **{page_ref}**", key=passage_unique_key)
                        
                        if show_more:
                            st.success(passage['full_context'])
                        else:
                            st.success(content.strip())
                    else:
                        st.success(excerpt_text)
                else:
                    show_more = st.checkbox("show more", key=passage_unique_key)
                    if show_more:
                        st.success(passage['full_context'])
                    else:
                        st.success(excerpt_text)
            
            # Summary (original format)
            st.info(f"**Summary:** {case['summary']}")
            
            # Court Reasoning (original format)
            st.warning(f"**Court Reasoning:** {case['court_reasoning']}")
            
            # Case Outcome (original format)
            with st.container():
                st.markdown(f"""
                <div style="
                    background-color: #f0f2f6; 
                    border-radius: 0.5rem; 
                    padding: 0.75rem 1rem;
                    margin: 0.5rem 0 1rem 0;
                    line-height: 1.6;
                ">
                    <strong>Case Outcome:</strong> {case['case_outcome']}
                </div>
                """, unsafe_allow_html=True)
            
            # Save Case + Notes Section (grouped together at the bottom)
            st.markdown("---")
            
            # Save Case Button and Notes side by side
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown("### 📝 Your Case Notes")
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)  # Add spacing to align with header
                if st.button("⭐ Save Case", key=f"save_case_{case['id']}_{case_index}", use_container_width=True):
                    save_case(case)
            
            # Notes text area
            case_notes_key = f"notes_{case['id']}_{case_index}"
            
            # Get existing notes for this case
            existing_notes = ""
            for saved_case in st.session_state.saved_cases:
                if saved_case['id'] == case['id']:
                    existing_notes = saved_case.get('notes', '')
                    break
            
            notes = st.text_area(
                "",
                value=existing_notes,
                placeholder="e.g., Key precedent for wage disputes. Compare with similar cases. Player had valid just cause due to unpaid wages and hostile work environment.",
                key=case_notes_key,
                height=100,
                label_visibility="collapsed"
            )
            
            # Save notes when they change
            if notes != existing_notes:
                # Update notes in saved cases
                for saved_case in st.session_state.saved_cases:
                    if saved_case['id'] == case['id']:
                        saved_case['notes'] = notes
                        break
            
            # AI Question Interface (original format)
            st.markdown("---")
            st.markdown("**Ask a Question About This Case**")
            question_unique_key = f"ai_question_{case['id']}_{case_index}"
            user_question = st.text_area(
                "",
                placeholder="e.g., What was the main legal issue?",
                key=question_unique_key,
                label_visibility="collapsed"
            )
            
            button_unique_key = f"ask_ai_{case['id']}_{case_index}"
            if st.button("Ask Question", key=button_unique_key):
                if user_question:
                    with st.spinner("Analyzing case..."):
                        time.sleep(2)
                        ai_answer = f"Based on the case details, this relates to {case['matter'].lower()} issues in sports arbitration."
                        
                        st.markdown(f"""
                        <div class="question-box">
                            <strong>AI Answer:</strong><br>
                            {ai_answer}
                        </div>
                        """, unsafe_allow_html=True)
else:
    st.info("Enter a search query to begin searching cases.")
