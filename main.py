import streamlit as st
import pandas as pd
from datetime import datetime, date

# Page config
st.set_page_config(
    page_title="CaseLength - Improved UX",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .filter-chip {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        margin: 3px;
        display: inline-block;
        border: 1px solid #93c5fd;
        font-weight: 500;
    }
    
    .filter-chip-removable {
        background-color: #fef3c7;
        color: #92400e;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        margin: 3px;
        display: inline-block;
        border: 1px solid #f59e0b;
        font-weight: 500;
    }
    
    .case-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 20px;
        margin: 12px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .case-card-saved {
        background: #f0fdf4;
        border: 2px solid #22c55e;
        border-radius: 8px;
        padding: 20px;
        margin: 12px 0;
        box-shadow: 0 2px 8px rgba(34,197,94,0.2);
    }
    
    .save-preview {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 16px;
        margin: 12px 0;
    }
    
    .success-message {
        background: #d1fae5;
        border: 1px solid #10b981;
        color: #065f46;
        padding: 12px;
        border-radius: 6px;
        margin: 8px 0;
        font-weight: 600;
    }
    
    .warning-message {
        background: #fef3c7;
        border: 1px solid #f59e0b;
        color: #92400e;
        padding: 8px 12px;
        border-radius: 4px;
        margin: 4px 0;
    }
    
    .active-filters-bar {
        background: #f1f5f9;
        border: 2px solid #3b82f6;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    
    .search-bar {
        background: #ffffff;
        border: 2px solid #3b82f6;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    
    .saved-indicator {
        background: #22c55e;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 14px;
        display: inline-block;
        margin: 8px 0;
    }
    
    .search-results-header {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 16px;
        margin: 16px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'saved_searches' not in st.session_state:
    st.session_state.saved_searches = []
if 'saved_cases' not in st.session_state:
    st.session_state.saved_cases = []
if 'case_notes' not in st.session_state:
    st.session_state.case_notes = {}
if 'show_save_modal' not in st.session_state:
    st.session_state.show_save_modal = False
if 'search_query' not in st.session_state:
    st.session_state.search_query = "just cause"
if 'last_action' not in st.session_state:
    st.session_state.last_action = None

# Sample case data
sample_cases = [
    {
        "case_id": "CAS 2020/A/7242",
        "parties": "Al Wahda F... v. Mourad Bat...",
        "date": "2021-11-23",
        "matter": "Contract",
        "outcome": "Partially upheld",
        "sport": "Football"
    },
    {
        "case_id": "CAS 2022/A/8836",
        "parties": "Samsunspor... v. Brice Dja...",
        "date": "2023-05-08",
        "matter": "Contract",
        "outcome": "Dismissed",
        "sport": "Football"
    },
    {
        "case_id": "CAS 2023/A/9444",
        "parties": "U Craiova... v. Marko Gaji...",
        "date": "2023-10-27",
        "matter": "Contract",
        "outcome": "Dismissed",
        "sport": "Football"
    }
]

# Header
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("**🏛️ caselens**")

st.title("CAS Case Law Research")

# Sidebar filters - IMPROVED CLARITY
with st.sidebar:
    st.header("🔍 Search & Filters")
    
    # Clear current filters section
    st.subheader("🗑️ Quick Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear All", help="Remove all active filters"):
            # Reset all filter values
            for key in st.session_state.keys():
                if key.startswith('filter_'):
                    del st.session_state[key]
            st.rerun()
    with col2:
        if st.button("🔄 Reset", help="Reset search and filters"):
            st.session_state.search_query = ""
            for key in st.session_state.keys():
                if key.startswith('filter_'):
                    del st.session_state[key]
            st.rerun()
    
    # Search Options
    with st.expander("⚙️ Search Options", expanded=False):
        search_type = st.selectbox("Search Type", ["Full Text", "Title Only", "Parties Only"])
    
    # Saved Searches - IMPROVED
    with st.expander("💾 My Saved Searches", expanded=False):
        if st.session_state.saved_searches:
            st.success(f"✅ {len(st.session_state.saved_searches)} saved searches")
            for i, search in enumerate(st.session_state.saved_searches):
                col1, col2 = st.columns([3, 1])
                with col1:
                    if st.button(f"📁 {search['name']}", key=f"load_{i}"):
                        st.session_state.search_query = search['query']
                        st.session_state.last_action = f"Loaded search: {search['name']}"
                        st.rerun()
                with col2:
                    if st.button("🗑️", key=f"delete_{i}", help="Delete this search"):
                        st.session_state.saved_searches.pop(i)
                        st.rerun()
        else:
            st.info("No saved searches yet")
    
    st.markdown("---")
    st.subheader("🎯 Search Filters")
    
    # Language filter
    language = st.selectbox(
        "🌐 Language", 
        ["All Languages", "English", "French", "Spanish"],
        key="filter_language"
    )
    
    # Decision Date filter
    date_range = st.date_input(
        "📅 Decision Date Range",
        value=(date(2020, 1, 1), date(2025, 12, 31)),
        format="YYYY-MM-DD",
        key="filter_date"
    )
    
    # Matter filter
    matter = st.multiselect(
        "📋 Matter Type",
        ["Contract", "Transfer", "Disciplinary", "Doping"],
        default=["Contract"],
        key="filter_matter"
    )
    
    # Outcome filter
    outcome = st.multiselect(
        "🏆 Case Outcome",
        ["Dismissed", "Partially upheld", "Upheld"],
        default=["Partially upheld", "Dismissed"],
        key="filter_outcome"
    )
    
    # Sport filter
    sport = st.multiselect(
        "⚽ Sport",
        ["Football", "Basketball", "Tennis", "Swimming"],
        default=["Football"],
        key="filter_sport"
    )
    
    # Procedural Types
    procedural_types = st.multiselect(
        "⚖️ Procedural Types",
        ["Appeal", "Ordinary", "Expedited"],
        key="filter_procedural"
    )
    
    # Arbitrators
    arbitrators = st.multiselect(
        "👨‍⚖️ Arbitrators",
        ["Prof. Luigi Fumagalli", "Mr Manfred Nan", "Mr Mark Hovell"],
        key="filter_arbitrators"
    )

# Main content area - IMPROVED SEARCH BAR
st.markdown('<div class="search-bar">', unsafe_allow_html=True)
col1, col2 = st.columns([4, 1])
with col1:
    new_search = st.text_input(
        "🔍 **Search Legal Cases**", 
        value=st.session_state.search_query,
        placeholder="Enter search terms (e.g., 'just cause', 'contract termination', 'transfer fees')",
        help="Search across case content, party names, and legal principles"
    )
    if new_search != st.session_state.search_query:
        st.session_state.search_query = new_search

with col2:
    if st.button("🔍 Search", type="primary", use_container_width=True):
        st.session_state.last_action = "Search executed"
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# IMPROVED Active Filters Display
active_filters = []
if matter: active_filters.extend([f"Matter: {m}" for m in matter])
if outcome: active_filters.extend([f"Outcome: {o}" for o in outcome])
if sport: active_filters.extend([f"Sport: {s}" for s in sport])
if procedural_types: active_filters.extend([f"Procedure: {p}" for p in procedural_types])
if arbitrators: active_filters.extend([f"Arbitrator: {a.split()[-1]}" for a in arbitrators])
if language != "All Languages": active_filters.append(f"Language: {language}")

if active_filters:
    st.markdown('<div class="active-filters-bar">', unsafe_allow_html=True)
    st.markdown(f"### 🎯 Active Search Filters ({len(active_filters)})")
    
    # Display filter chips in a more organized way
    filter_html = "<div style='margin: 8px 0;'>"
    for filter_item in active_filters:
        filter_html += f'<span class="filter-chip-removable">{filter_item} ❌</span> '
    filter_html += "</div>"
    
    st.markdown(filter_html, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 2, 4])
    with col1:
        if st.button("🗑️ Clear All Filters", type="secondary"):
            # Clear all multiselect filters
            for key in ['filter_matter', 'filter_outcome', 'filter_sport', 'filter_procedural', 'filter_arbitrators']:
                if key in st.session_state:
                    st.session_state[key] = []
            st.session_state.filter_language = "All Languages"
            st.rerun()
    
    with col2:
        if st.button("💾 Save These Filters", type="secondary"):
            st.session_state.show_save_modal = True
    
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("🎯 **No filters applied** - Showing all cases. Use the sidebar to filter results.")

# Show last action feedback
if st.session_state.last_action:
    st.markdown(f'<div class="success-message">✅ {st.session_state.last_action}</div>', unsafe_allow_html=True)
    # Clear the message after showing it
    st.session_state.last_action = None

# Action buttons row - IMPROVED
col1, col2, col3, col4 = st.columns([2, 2, 2, 4])

with col1:
    if st.button("💾 Save Search", type="secondary", help="Save current search and filters"):
        st.session_state.show_save_modal = True

with col2:
    if st.button("🔄 New Search", help="Clear search and start fresh"):
        st.session_state.search_query = ""
        st.session_state.last_action = "Started new search"
        st.rerun()

with col3:
    # Show saved items count
    saved_count = len(st.session_state.saved_cases)
    if saved_count > 0:
        st.markdown(f"**📌 {saved_count} Saved Cases**")

# Save Search Modal - IMPROVED
if st.session_state.show_save_modal:
    st.markdown("---")
    st.markdown("## 💾 Save Your Search")
    
    # Preview what will be saved - MORE DETAILED
    with st.container():
        st.markdown('<div class="save-preview">', unsafe_allow_html=True)
        st.markdown("### 📋 Search Preview")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**🔍 Search Query:** `{st.session_state.search_query or 'No search terms'}`")
            st.write(f"**📊 Active Filters:** {len(active_filters)} filters applied")
        
        with col2:
            if active_filters:
                st.write("**Filter Details:**")
                for filter_item in active_filters:
                    st.write(f"  • {filter_item}")
            else:
                st.write("**No filters applied** - Will save search query only")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Save form
    col1, col2 = st.columns([3, 1])
    with col1:
        search_name = st.text_input(
            "📝 Search Name:", 
            value=f"Just Cause Research - {datetime.now().strftime('%Y-%m-%d')}",
            help="Give your search a memorable name"
        )
    
    email_alerts = st.checkbox("📧 Send me email alerts for new matching cases")
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if st.button("✅ Save Search", type="primary"):
            # Save the search
            new_search = {
                "name": search_name,
                "query": st.session_state.search_query,
                "filters": active_filters.copy(),
                "created": datetime.now(),
                "email_alerts": email_alerts
            }
            st.session_state.saved_searches.append(new_search)
            st.session_state.show_save_modal = False
            st.session_state.last_action = f"Search '{search_name}' saved successfully!"
            st.rerun()
    
    with col2:
        if st.button("❌ Cancel"):
            st.session_state.show_save_modal = False
            st.rerun()
    
    st.markdown("---")

# Search results summary - IMPROVED
if not st.session_state.show_save_modal:
    st.markdown('<div class="search-results-header">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        st.metric("📄 Found Results", "15 passages")
    with col2:
        st.metric("⚖️ Total Cases", "13 decisions")
    with col3:
        st.metric("📌 Saved Cases", len(st.session_state.saved_cases))
    st.markdown('</div>', unsafe_allow_html=True)

    # General Answer section
    with st.expander("📋 **General Answer: Definition of Just Cause in Football Employment Contracts**", expanded=True):
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
        """)

    # Case results - MUCH IMPROVED SAVED STATUS
    st.markdown("## 📁 Case Results")

    for i, case in enumerate(sample_cases):
        case_key = case['case_id']
        is_saved = case_key in st.session_state.saved_cases
        
        # Use different styling for saved cases
        if is_saved:
            st.markdown('<div class="case-card-saved">', unsafe_allow_html=True)
        else:
            st.markdown('<div class="case-card">', unsafe_allow_html=True)
        
        # Case header with clear saved status
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {case['case_id']}")
            st.write(f"**👥 Parties:** {case['parties']}")
            st.write(f"**📅 Date:** {case['date']} | **📋 Matter:** {case['matter']} | **🏆 Outcome:** {case['outcome']} | **⚽ Sport:** {case['sport']}")
        
        with col2:
            if is_saved:
                # CLEAR saved indicator
                st.markdown('<div class="saved-indicator">✅ SAVED TO MY CASES</div>', unsafe_allow_html=True)
                if st.button(f"🗑️ Remove", key=f"remove_{case_key}", help="Remove from saved cases"):
                    st.session_state.saved_cases.remove(case_key)
                    st.session_state.last_action = f"Removed {case_key} from saved cases"
                    st.rerun()
            else:
                if st.button(f"📌 Save to My Cases", key=f"save_{case_key}", type="primary"):
                    st.session_state.saved_cases.append(case_key)
                    st.session_state.last_action = f"✅ {case_key} saved to your cases!"
                    st.rerun()
        
        # Additional case actions
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(f"📤 Export", key=f"export_{case_key}"):
                st.session_state.last_action = f"Exported {case_key}"
        with col2:
            if st.button(f"🔗 Copy Link", key=f"link_{case_key}"):
                st.session_state.last_action = f"Copied link for {case_key}"
        with col3:
            if st.button(f"📧 Share", key=f"share_{case_key}"):
                st.session_state.last_action = f"Shared {case_key}"
        
        # Case notes section - IMPROVED
        with st.expander(f"📝 **Notes for {case['case_id']}**", expanded=False):
            note_key = f"notes_{case_key}"
            current_note = st.session_state.case_notes.get(note_key, "")
            
            new_note = st.text_area(
                "Add your analysis, key points, or observations:",
                value=current_note,
                key=f"textarea_{note_key}",
                placeholder="Example: This case establishes important precedent for salary disputes...",
                height=100
            )
            
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button(f"💾 Save Notes", key=f"save_notes_{case_key}", type="primary"):
                    st.session_state.case_notes[note_key] = new_note
                    st.session_state.last_action = f"Notes saved for {case_key}"
                    st.rerun()
            
            with col2:
                if current_note:
                    if st.button(f"🗑️ Clear Notes", key=f"clear_notes_{case_key}"):
                        st.session_state.case_notes[note_key] = ""
                        st.session_state.last_action = f"Notes cleared for {case_key}"
                        st.rerun()
            
            with col3:
                if new_note != current_note and new_note:
                    st.warning("⚠️ You have unsaved changes")
                elif current_note:
                    st.success("✅ Notes saved")
                else:
                    st.info("💡 Add notes to save your analysis")
        
        # Case summary
        if case['case_id'] == "CAS 2020/A/7242":
            with st.expander("📖 **Case Summary & Key Findings**", expanded=False):
                st.markdown("""
                **Case Background:**
                This case involves Al Wahda FSC Company (UAE club), Mr. Mourad Batna (Moroccan footballer), and Al Jazira FSC (UAE club) 
                regarding the termination of Batna's employment contract.
                
                **Key Facts:**
                - Batna terminated his contract citing overdue wages and abusive conduct by Al Wahda
                - Subsequently signed with Al Jazira
                - Al Wahda claimed Batna left without just cause, seeking compensation and sanctions
                - Batna and Al Jazira contended the termination was justified due to unpaid salaries and improper conduct
                
                **Legal Significance:**
                - Establishes precedent for just cause determination in football contracts
                - Demonstrates importance of salary payment obligations
                - Shows how club conduct can justify player termination
                """)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")

    # IMPROVED Footer with comprehensive saved items summary
    if st.session_state.saved_cases or st.session_state.saved_searches:
        st.markdown("## 📊 My Legal Research Collection")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.saved_cases:
                st.markdown(f"### 📌 My Saved Cases ({len(st.session_state.saved_cases)})")
                for case_id in st.session_state.saved_cases:
                    note_count = len(st.session_state.case_notes.get(f"notes_{case_id}", ""))
                    note_indicator = f" (📝 {note_count} chars)" if note_count > 0 else ""
                    st.write(f"  • **{case_id}**{note_indicator}")
                
                if st.button("📤 Export All Saved Cases"):
                    st.session_state.last_action = "Exported all saved cases"
                    st.rerun()
        
        with col2:
            if st.session_state.saved_searches:
                st.markdown(f"### 💾 My Saved Searches ({len(st.session_state.saved_searches)})")
                for search in st.session_state.saved_searches:
                    filter_count = len(search.get('filters', []))
                    alert_indicator = " 📧" if search.get('email_alerts') else ""
                    st.write(f"  • **{search['name']}** ({filter_count} filters){alert_indicator}")
                
                if st.button("📤 Export All Searches"):
                    st.session_state.last_action = "Exported all saved searches"
                    st.rerun()
