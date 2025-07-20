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
    st.session_state.saved_searches = []
if 'case_notes' not in st.session_state:
    st.session_state.case_notes = {}

# Sample case database (expanded)
CASES_DATABASE = [
    {
        "id": "CAS_2020_A_7242",
        "title": "CAS 2020/A/7242",
        "date": "2021-11-23",
        "procedure": "Appeal Arbitration Procedure",
        "matter": "Contract",
        "category": "Award", 
        "outcome": "Partially upheld",
        "sport": "Football",
        "appellants": "Al Wahda FSC Company",
        "respondents": "Mourad Batna, Al Jazira FSC",
        "president": "Mr Mark Hovell",
        "arbitrator1": "Prof. Luigi Fumagalli",
        "arbitrator2": "Mr Manfred Nan",
        "summary": "This case involves Al Wahda FSC Company (UAE club), Mr. Mourad Batna (Moroccan footballer), and Al Jazira FSC (UAE club) regarding the termination of Batna's employment contract. Batna terminated his contract citing overdue wages and abusive conduct by Al Wahda, thereafter signing with Al Jazira. Al Wahda claimed Batna left without just cause, seeking compensation and sanctions, while Batna and Al Jazira contended the termination was justified due to unpaid salaries and improper conduct by Al Wahda.",
        "court_reasoning": "The CAS panel found that FIFA regulations take precedence over national law due to the contract's terms and parties' submission to FIFA/CAS jurisdiction. The Club's repeated failure to pay Batna's salary for over three months was a substantial breach, constituting just cause for contract termination.",
        "case_outcome": "The appeal was partially upheld with mixed results for both parties regarding compensation and sanctions.",
        "relevant_passages": [
            {
                "excerpt": "Page 21 - i. The existence of just cause",
                "full_context": "The existence of just cause must be determined based on the merits and particular circumstances of each case, considering the severity of the breach and whether continued employment is reasonable in good faith."
            }
        ],
        "similarity_score": 0.92
    },
    {
        "id": "CAS_2022_A_8836", 
        "title": "CAS 2022/A/8836",
        "date": "2023-05-08",
        "procedure": "Appeal Arbitration Procedure",
        "matter": "Contract",
        "category": "Award",
        "outcome": "Dismissed", 
        "sport": "Football",
        "appellants": "Samsunspor",
        "respondents": "Brice Dja...",
        "president": "Mr John Smith",
        "arbitrator1": "Prof. Maria Santos",
        "arbitrator2": "Dr. Ahmed Hassan",
        "summary": "Contract dispute involving termination for just cause between Samsunspor and player Brice Dja regarding salary payments and breach of contract terms.",
        "court_reasoning": "The panel determined that the club's failure to pay salary constituted a fundamental breach sufficient for just cause termination.",
        "case_outcome": "The appeal was dismissed and the original decision was upheld.",
        "relevant_passages": [
            {
                "excerpt": "Page 15 - Salary payment obligations are fundamental to employment contracts",
                "full_context": "Non-payment of salary for extended periods constitutes a substantial breach that may justify termination for just cause under FIFA regulations."
            }
        ],
        "similarity_score": 0.85
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
    
    .save-search-card {
        background-color: #f0f9ff;
        border: 1px solid #0ea5e9;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    
    .save-case-card {
        background-color: #fef3c7;
        border: 1px solid #f59e0b;
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
    }
    
    .success-message {
        background-color: #dcfce7;
        border: 1px solid #16a34a;
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
        color: #15803d;
    }
</style>
""", unsafe_allow_html=True)

def search_cases(query, filters, max_results=20, similarity_threshold=0.5):
    """Search cases with filters applied"""
    relevant_cases = []
    
    # Debug information
    debug_info = {
        'query': query,
        'filters': filters,
        'total_cases': len(CASES_DATABASE),
        'matches_found': 0,
        'filter_failures': 0
    }
    
    for case in CASES_DATABASE:
        # Apply text search - check both summary and court_reasoning
        text_match = (query.lower() in case['summary'].lower() or 
                     query.lower() in case['court_reasoning'].lower())
        
        if text_match:
            debug_info['matches_found'] += 1
            
            # Apply filters
            filter_passed = True
            
            if filters.get('sport') and case['sport'] != filters['sport']:
                filter_passed = False
                debug_info['filter_failures'] += 1
            if filters.get('matter') and case['matter'] != filters['matter']:
                filter_passed = False
                debug_info['filter_failures'] += 1
            if filters.get('outcome') and case['outcome'] != filters['outcome']:
                filter_passed = False
                debug_info['filter_failures'] += 1
            
            if filter_passed and case['similarity_score'] >= similarity_threshold:
                relevant_cases.append(case)
    
    # Store debug info in session state for display
    st.session_state.search_debug = debug_info
    
    return relevant_cases[:max_results]

def save_search_dialog():
    """Enhanced save search dialog"""
    st.markdown("""
    <div class="save-search-card">
        <h4>💾 Save This Search</h4>
        <p>Save your search query and all applied filters for quick access later.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("save_search_form"):
        search_name = st.text_input("Search Name", placeholder="e.g., Just Cause in Football Contracts")
        search_notes = st.text_area("Notes about this search (optional)", placeholder="Add any notes about why you saved this search...")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            save_button = st.form_submit_button("💾 Save Search", use_container_width=True)
        with col2:
            if st.form_submit_button("❌ Cancel", use_container_width=True):
                st.rerun()
        
        if save_button and search_name:
            # Create search object with current state - using safe access
            search_object = {
                'id': f"search_{int(time.time())}",
                'name': search_name,
                'query': st.session_state.get('search_query', ''),
                'notes': search_notes,
                'filters': st.session_state.get('current_filters', {}),
                'saved_date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                'results_count': len(st.session_state.get('current_results', []))
            }
            
            # Initialize saved_searches if it doesn't exist
            if 'saved_searches' not in st.session_state:
                st.session_state.saved_searches = []
            
            st.session_state.saved_searches.append(search_object)
            
            st.markdown("""
            <div class="success-message">
                ✅ Search saved successfully! You can find it in the "Saved Searches" section.
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
            st.rerun()

def save_case_dialog(case):
    """Enhanced save case dialog with notes"""
    st.markdown(f"""
    <div class="save-case-card">
        <h4>⭐ Save Case: {case['title']}</h4>
        <p>Add this case to your saved cases with optional notes.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form(f"save_case_form_{case['id']}"):
        case_notes = st.text_area(
            "Case Notes", 
            value=st.session_state.case_notes.get(case['id'], ''),
            placeholder="Add your analysis, thoughts, or reminders about this case...",
            height=100
        )
        
        col1, col2 = st.columns([1, 1])
        with col1:
            save_button = st.form_submit_button("⭐ Save Case", use_container_width=True)
        with col2:
            remove_button = st.form_submit_button("🗑️ Remove", use_container_width=True)
        
        if save_button:
            if case['id'] not in st.session_state.bookmarked_cases:
                st.session_state.bookmarked_cases.append(case['id'])
            st.session_state.case_notes[case['id']] = case_notes
            
            st.markdown("""
            <div class="success-message">
                ✅ Case saved with notes!
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
            st.rerun()
            
        if remove_button:
            if case['id'] in st.session_state.bookmarked_cases:
                st.session_state.bookmarked_cases.remove(case['id'])
            if case['id'] in st.session_state.case_notes:
                del st.session_state.case_notes[case['id']]
            
            st.markdown("""
            <div class="success-message">
                ✅ Case removed from saved cases!
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
            st.rerun()

# Sidebar Navigation
with st.sidebar:
    # Logo
    st.markdown("""
    <div class="main-header">
        <span class="logo-icon">C</span>
        <h2 style="margin: 0; color: #1f2937;">caselens</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    st.markdown("### Navigation")
    page = st.radio(
        "",
        ["🔍 Search", "📄 Documents", "📊 Analytics", "🔖 Bookmarks", "👤 Admin"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    if page == "🔍 Search":
        # Search Options
        st.markdown("### Search Filters")
        
        # Initialize current filters in session state
        if 'current_filters' not in st.session_state:
            st.session_state.current_filters = {}
        
        with st.container():
            st.markdown("**Sport**")
            sport_filter = st.selectbox("", ["All Sports", "Football", "Basketball", "Tennis"], index=0, label_visibility="collapsed")
            if sport_filter != "All Sports":
                st.session_state.current_filters['sport'] = sport_filter
            elif 'sport' in st.session_state.current_filters:
                del st.session_state.current_filters['sport']
        
        with st.container():
            st.markdown("**Matter**")
            matter_filter = st.selectbox("", ["All Matters", "Contract", "Transfer", "Disciplinary"], index=0, label_visibility="collapsed")
            if matter_filter != "All Matters":
                st.session_state.current_filters['matter'] = matter_filter
            elif 'matter' in st.session_state.current_filters:
                del st.session_state.current_filters['matter']
        
        with st.container():
            st.markdown("**Outcome**")
            outcome_filter = st.selectbox("", ["All Outcomes", "Dismissed", "Partially upheld", "Upheld"], index=0, label_visibility="collapsed")
            if outcome_filter != "All Outcomes":
                st.session_state.current_filters['outcome'] = outcome_filter
            elif 'outcome' in st.session_state.current_filters:
                del st.session_state.current_filters['outcome']
        
        # Display active filters
        if st.session_state.current_filters:
            st.markdown("**Active Filters:**")
            for filter_type, value in st.session_state.current_filters.items():
                st.markdown(f"• {filter_type.title()}: {value}")
        
        # Saved Searches Section
        st.markdown("---")
        st.markdown("### Saved Searches")
        
        if st.session_state.saved_searches:
            st.write(f"📁 Found {len(st.session_state.saved_searches)} saved searches")
            
            # Safely create search options with error handling
            search_options = ["Select a saved search..."]
            for s in st.session_state.saved_searches:
                name = s.get('name', 'Unnamed Search')
                saved_date = s.get('saved_date', 'Unknown Date')
                search_options.append(f"{name} ({saved_date})")
            
            selected_search = st.selectbox("Load saved search", search_options, index=0)
            
            if selected_search != "Select a saved search...":
                # Find the selected search
                search_index = search_options.index(selected_search) - 1
                if search_index < len(st.session_state.saved_searches):
                    selected_search_obj = st.session_state.saved_searches[search_index]
                    
                    if st.button("🔄 Load Search"):
                        st.session_state.search_query = selected_search_obj.get('query', '')
                        st.session_state.current_filters = selected_search_obj.get('filters', {})
                        st.success(f"Loaded search: {selected_search_obj.get('name', 'Unnamed Search')}")
                        st.rerun()
        else:
            st.info("No saved searches yet. Save a search to see it here!")

# Main Content Area
if page == "🔍 Search":
    # Search Interface
    st.markdown("### CAS Case Law Research")
    
    # Initialize search_query in session state if not exists
    if 'search_query' not in st.session_state:
        st.session_state.search_query = 'just cause'
    
    # Search query input
    search_query = st.text_input(
        "", 
        value=st.session_state.search_query,
        placeholder="Enter your search query", 
        label_visibility="collapsed",
        key="search_input_main"
    )
    
    # Update session state
    st.session_state.search_query = search_query
    
    # Search and Save buttons
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_button = st.button("🔍 Search", use_container_width=True)
    with col2:
        save_search_button = st.button("💾 Save Search", use_container_width=True)
    with col3:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    
    if clear_button:
        st.session_state.search_query = ""
        st.session_state.current_filters = {}
        st.rerun()
    
    # Save Search Dialog
    if save_search_button:
        save_search_dialog()
    
    # Perform search when there's a query (automatic) or when search button is clicked
    if search_query and (search_button or True):  # Always search when there's a query
        # Perform search
        results = search_cases(search_query, st.session_state.current_filters)
        st.session_state.current_results = results
        
        # Search results summary
        filter_summary = ""
        if st.session_state.current_filters:
            filter_list = [f"{k}: {v}" for k, v in st.session_state.current_filters.items()]
            filter_summary = f" (Filters: {', '.join(filter_list)})"
        
        st.success(f"Found {len(results)} results for '{search_query}'{filter_summary}")
        
        # Debug information (show when no results or in development)
        if len(results) == 0 or st.checkbox("🔍 Show Debug Info"):
            if hasattr(st.session_state, 'search_debug'):
                debug = st.session_state.search_debug
                st.info(f"""
                **Debug Info:**
                - Query: "{debug['query']}"
                - Total cases in database: {debug['total_cases']}
                - Text matches found: {debug['matches_found']}
                - Filter failures: {debug['filter_failures']}
                - Active filters: {debug['filters']}
                """)
                
                # Show what's in the first case for debugging
                if len(CASES_DATABASE) > 0:
                    sample_case = CASES_DATABASE[0]
                    st.info(f"""
                    **Sample Case Data:**
                    - Title: {sample_case['title']}
                    - Summary contains query: {"Yes" if search_query.lower() in sample_case['summary'].lower() else "No"}
                    - Court reasoning contains query: {"Yes" if search_query.lower() in sample_case['court_reasoning'].lower() else "No"}
                    - Sport: {sample_case['sport']}
                    - Matter: {sample_case['matter']}
                    - Outcome: {sample_case['outcome']}
                    """)
        
        if len(results) == 0:
            st.warning("No results found. Try adjusting your search query or filters.")
        else:
            # General Answer Section (if results found)
            with st.expander("📋 General Answer: Definition of Just Cause in Football Employment Contracts", expanded=True):
                st.markdown("""
                **1. General Principle:**
                "Just cause" (or "good cause") is a substantive legal standard under Article 14 of the FIFA Regulations on the Status and Transfer of Players (RSTP) and Article 337(2) of the Swiss Code of Obligations (CO). It permits a party to lawfully terminate an employment contract when its fundamental terms and conditions are no longer respected by the other party.
                
                **2. Requirements for Just Cause:**
                Two main requirements must always be met:
                
                • **Substantive requirement:** There must be a pattern of conduct or an event that renders the continuation of the employment relationship in good faith unreasonable or unconscionable for the party giving notice.
                
                • The breach must be sufficiently serious ("exceptional measure") and supported by objective circumstances, such as a serious breach of trust, which make continued employment unreasonable.
                
                **3. Case-by-case Assessment:**
                The existence and definition of just cause are determined based on the merits and particular circumstances of each case, considering the severity of the breach. Swiss law may be applied subsidiarily if necessary.
                
                **4. Practical Implication:**
                Immediate contract termination for just cause is only accepted under narrow, exceptional circumstances; minor breaches generally do not qualify.
                
                **Summary:**
                Just cause exists only where a party's conduct fundamentally undermines the contractual relationship and makes its continuation unconscionable in good faith. Whether just cause exists is always assessed on a case-by-case basis with reference to FIFA and Swiss legal principles.
                """)
            
            # Display search results
            for case_index, case in enumerate(results):
                # Check if case is saved
                is_saved = case['id'] in st.session_state.bookmarked_cases
                save_icon = "⭐" if is_saved else "☆"
                
                # Case header with save indicator
                case_title = f"{save_icon} **{case['title']}** | 📅 **Date:** {case['date']} | 👥 **Parties:** {case['appellants']} v. {case['respondents']} | 📝 **Matter:** {case['matter']} | 📄 **Outcome:** {case['outcome']} | 🏅 **Sport:** {case['sport']}"
                
                with st.expander(case_title, expanded=(case_index == 0)):
                    
                    st.markdown(f"""
                    **Procedure:** {case['procedure']}  
                    **Category:** {case['category']}  
                    **President:** {case['president']} | **Arbitrators:** {case['arbitrator1']}, {case['arbitrator2']}
                    """)
                    
                    # Save Case Section (prominent placement)
                    col1, col2 = st.columns([3, 1])
                    with col2:
                        save_case_key = f"save_case_{case['id']}_{case_index}"
                        if st.button(f"{save_icon} {'Saved' if is_saved else 'Save Case'}", key=save_case_key, use_container_width=True):
                            st.session_state[f"show_save_dialog_{case['id']}"] = True
                            st.rerun()
                    
                    # Show save dialog if triggered
                    if st.session_state.get(f"show_save_dialog_{case['id']}", False):
                        save_case_dialog(case)
                        # Reset dialog state
                        st.session_state[f"show_save_dialog_{case['id']}"] = False
                    
                    # Show saved notes if case is saved
                    if is_saved and case['id'] in st.session_state.case_notes:
                        notes = st.session_state.case_notes[case['id']]
                        if notes:
                            st.markdown(f"""
                            **📝 Your Notes:**
                            > {notes}
                            """)
                    
                    # Relevant Passages
                    st.markdown("### **Relevant Passages**")
                    for passage_index, passage in enumerate(case['relevant_passages']):
                        passage_unique_key = f"show_more_{case['id']}_{passage_index}_{case_index}"
                        
                        excerpt_text = passage['excerpt']
                        if excerpt_text.startswith('Page'):
                            if '.' in excerpt_text:
                                page_ref = excerpt_text.split(' - ')[0]
                                content = excerpt_text.split('.', 1)[1] if '.' in excerpt_text else excerpt_text.split(' - ', 1)[1]
                                
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
                    
                    # Summary
                    st.info(f"**Summary:** {case['summary']}")
                    
                    # Court Reasoning
                    st.warning(f"**Court Reasoning:** {case['court_reasoning']}")
                    
                    # Case Outcome
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

elif page == "🔖 Bookmarks":
    st.title("🔖 Saved Cases")
    
    if st.session_state.bookmarked_cases:
        st.success(f"You have {len(st.session_state.bookmarked_cases)} saved cases")
        
        for case_id in st.session_state.bookmarked_cases:
            try:
                # Find the case in database
                case = next((c for c in CASES_DATABASE if c['id'] == case_id), None)
                if case:
                    case_title = f"⭐ {case.get('title', 'Unknown Case')} - {case.get('appellants', 'Unknown')} v. {case.get('respondents', 'Unknown')}"
                    with st.expander(case_title, expanded=False):
                        # Show case notes if available
                        if case_id in st.session_state.case_notes and st.session_state.case_notes[case_id]:
                            st.markdown(f"""
                            **📝 Your Notes:**
                            > {st.session_state.case_notes[case_id]}
                            """)
                            st.markdown("---")
                        
                        st.markdown(f"**Date:** {case.get('date', 'Unknown')}")
                        st.markdown(f"**Matter:** {case.get('matter', 'Unknown')}")
                        st.markdown(f"**Outcome:** {case.get('outcome', 'Unknown')}")
                        st.markdown(f"**Summary:** {case.get('summary', 'No summary available')}")
                        
                        if st.button(f"🗑️ Remove from saved", key=f"remove_{case_id}"):
                            st.session_state.bookmarked_cases.remove(case_id)
                            if case_id in st.session_state.case_notes:
                                del st.session_state.case_notes[case_id]
                            st.success("Case removed from saved cases!")
                            st.rerun()
                else:
                    st.warning(f"Case {case_id} not found in database")
            except Exception as e:
                st.error(f"Error loading case {case_id}: {str(e)}")
    else:
        st.info("No saved cases yet. Save cases from your search results to see them here!")

elif page == "📊 Analytics":
    st.title("📊 Legal Analytics Dashboard")
    st.info("Analytics features coming soon.")

elif page == "📄 Documents":
    st.title("📄 Document Library")
    st.info("Upload legal documents for analysis.")

elif page == "👤 Admin":
    st.title("👤 Admin Dashboard")
    st.info("Admin features coming soon.")
