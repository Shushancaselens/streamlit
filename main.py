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
        gap: 10px;
        margin-bottom: 20px;
    }
    
    .logo-icon {
        background-color: #4f46e5;
        color: white;
        padding: 8px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 16px;
    }
    
    .question-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    
    .sidebar-section {
        margin-bottom: 25px;
    }
    
    .saved-search-item {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 12px;
        margin: 8px 0;
    }
    
    .saved-case-item {
        background-color: #fefce8;
        border: 1px solid #fde047;
        border-radius: 6px;
        padding: 12px;
        margin: 8px 0;
    }
    
    .current-search-header {
        background-color: #f1f5f9;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    
    .case-metadata {
        display: flex;
        gap: 15px;
        margin: 10px 0;
        font-size: 14px;
    }
    
    .metadata-item {
        display: flex;
        align-items: center;
        gap: 4px;
    }
</style>
""", unsafe_allow_html=True)

def search_cases(query, max_results=20, similarity_threshold=0.5, filters=None):
    """Search cases with filters"""
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
    # Logo
    st.markdown("""
    <div class="main-header">
        <span class="logo-icon">⚖️</span>
        <h2 style="margin: 0; color: #1f2937;">caselens</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation Tabs
    st.markdown("🔍 Search   📚 My Library")
    
    st.markdown("---")
    
    # Saved Searches Section - Collapsible
    with st.expander(f"🔍 Saved Searches ({len(st.session_state.saved_searches)})", expanded=False):
        if len(st.session_state.saved_searches) == 0:
            st.write("No saved searches yet")
        else:
            for search in st.session_state.saved_searches:
                col1, col2, col3 = st.columns([4, 1, 1])
                with col1:
                    st.write(f"**{search['name']}**")
                    st.caption(f"Last run: {search['last_run']}")
                with col2:
                    if st.button("Load", key=f"load_{search['id']}", help="Load this search"):
                        st.session_state.loaded_search = search
                        st.rerun()
                with col3:
                    if st.button("✕", key=f"delete_{search['id']}", help="Delete search"):
                        st.session_state.saved_searches = [s for s in st.session_state.saved_searches if s['id'] != search['id']]
                        st.rerun()
                st.divider()
    
    # Saved Cases Section - Collapsible
    with st.expander(f"⭐ Saved Cases ({len(st.session_state.saved_cases)})", expanded=False):
        if len(st.session_state.saved_cases) == 0:
            st.write("No saved cases yet")
        else:
            for case in st.session_state.saved_cases:
                col1, col2, col3 = st.columns([4, 1, 1])
                with col1:
                    st.write(f"**{case['title']}**")
                    st.caption(f"{case['case_ref']} • {case['saved_date']}")
                with col2:
                    if st.button("View", key=f"view_{case['id']}", help="View case details"):
                        st.info("Case viewing feature coming soon!")
                with col3:
                    if st.button("✕", key=f"remove_{case['id']}", help="Remove from saved"):
                        st.session_state.saved_cases = [c for c in st.session_state.saved_cases if c['id'] != case['id']]
                        st.rerun()
                st.divider()

    st.markdown("---")
    
    # Search Options
    st.markdown("### Search Options")
    
    with st.container():
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown("**Max Results**")
        max_results = st.number_input("", min_value=1, max_value=100, value=20, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown("**Similarity Threshold**")
        similarity = st.slider("", min_value=0.0, max_value=1.0, value=0.55, step=0.01, label_visibility="collapsed")
        st.write(f"Current value: {similarity}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    show_similarity = st.checkbox("Show Similarity Scores ⓘ")

# Main Content Area
st.markdown("### CAS Case Law Research")

# Check if a saved search was loaded
loaded_search = getattr(st.session_state, 'loaded_search', None)
if loaded_search:
    default_query = loaded_search['query']
    default_filters = loaded_search['filters']
    st.session_state.loaded_search = None  # Clear after loading
else:
    default_query = "just cause"
    default_filters = {"sport": "Any", "matter": "Any", "outcome": "Any"}

# Search Interface
search_query = st.text_input(
    "", 
    value=default_query,
    placeholder="Enter your search query", 
    label_visibility="collapsed",
    key="main_search_input"
)

# Filters
col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

with col1:
    sport_filter = st.selectbox(
        "Sport",
        ["Any", "Football", "Basketball", "Tennis", "Swimming"],
        index=0 if default_filters.get('sport') == 'Any' else ["Any", "Football", "Basketball", "Tennis", "Swimming"].index(default_filters.get('sport', 'Any'))
    )

with col2:
    matter_filter = st.selectbox(
        "Matter",
        ["Any", "Contract", "Transfer", "Doping", "Disciplinary"],
        index=0 if default_filters.get('matter') == 'Any' else ["Any", "Contract", "Transfer", "Doping", "Disciplinary"].index(default_filters.get('matter', 'Any'))
    )

with col3:
    outcome_filter = st.selectbox(
        "Outcome",
        ["Any", "Dismissed", "Upheld", "Partially Upheld"],
        index=0 if default_filters.get('outcome') == 'Any' else ["Any", "Dismissed", "Upheld", "Partially Upheld"].index(default_filters.get('outcome', 'Any'))
    )

with col4:
    # Save Search Button
    if st.button("💾 Save Search", help="Save current search and filters"):
        with st.form("save_search_form"):
            st.markdown("**Save Current Search**")
            search_name = st.text_input("Search Name", value=f'"{search_query}" + filters')
            search_description = st.text_area("Description (optional)", placeholder="e.g., Research for client consultation")
            
            if st.form_submit_button("Save"):
                filters = {
                    "sport": sport_filter,
                    "matter": matter_filter, 
                    "outcome": outcome_filter
                }
                save_current_search(search_name, search_query, filters, search_description)
                st.success("Search saved!")
                st.rerun()

if search_query:
    # Current search header
    active_filters = []
    if sport_filter != "Any":
        active_filters.append(f"Sport: {sport_filter}")
    if matter_filter != "Any":
        active_filters.append(f"Matter: {matter_filter}")
    if outcome_filter != "Any":
        active_filters.append(f"Outcome: {outcome_filter}")
    
    filter_text = f" + {len(active_filters)} filters" if active_filters else ""
    
    st.markdown(f"""
    <div class="current-search-header">
        <strong>Current search: "{search_query}"{filter_text}</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Perform search
    filters = {
        "sport": sport_filter,
        "matter": matter_filter,
        "outcome": outcome_filter
    }
    results = search_cases(search_query, max_results, similarity, filters)
    
    # Search results summary
    total_passages = sum(len(case.get('relevant_passages', [])) for case in results)
    st.success(f"Found {total_passages} relevant passages in {len(results)} decisions")
    
    # Display search results
    for case_index, case in enumerate(results):
        # Case header with metadata
        st.markdown(f"### {case['title']} - {case['appellants']} v. {case['respondents']}")
        
        # Metadata row
        st.markdown(f"""
        <div class="case-metadata">
            <span class="metadata-item">📅 {case['date']}</span>
            <span class="metadata-item">📄 {case['matter']}</span>
            <span class="metadata-item">⚽ {case['sport']}</span>
            <span class="metadata-item">{"✅" if case['outcome'] == "Upheld" else "🟡" if case['outcome'] == "Partially Upheld" else "❌"} {case['outcome']}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Case summary
        st.write(case['summary'])
        
        # Save Case Button
        col1, col2 = st.columns([6, 1])
        with col2:
            if st.button("⭐ Save Case", key=f"save_case_{case['id']}_{case_index}"):
                save_case(case)
        
        # Case Notes Section
        st.markdown("### 📝 Your Case Notes")
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
        
        with st.expander("View Full Case Details", expanded=False):
            # Relevant Passages
            st.markdown("### **Relevant Passages**")
            for passage_index, passage in enumerate(case['relevant_passages']):
                passage_unique_key = f"show_more_{case['id']}_{passage_index}_{case_index}"
                
                excerpt_text = passage['excerpt']
                if excerpt_text.startswith('Page'):
                    if '.' in excerpt_text:
                        page_ref = excerpt_text.split(' - ')[0]
                        content = excerpt_text.split('.', 1)[1]
                        
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
            
            # Court Reasoning
            st.warning(f"**Court Reasoning:** {case['court_reasoning']}")
            
            # Case Outcome
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
        
        st.markdown("---")
