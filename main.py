import streamlit as st
import pandas as pd
from datetime import datetime, date

# Page config
st.set_page_config(
    page_title="CaseLength - Improved UX",
    page_icon="⚖️",
    layout="wide"
)

# Initialize session state
if 'saved_searches' not in st.session_state:
    st.session_state.saved_searches = []
if 'saved_cases' not in st.session_state:
    st.session_state.saved_cases = []
if 'case_notes' not in st.session_state:
    st.session_state.case_notes = {}
if 'show_save_search_modal' not in st.session_state:
    st.session_state.show_save_search_modal = False

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
st.markdown("**🏛️ caselens**")
st.title("CAS Case Law Research")

# Sidebar - original structure
with st.sidebar:
    st.subheader("🔍 Search")
    
    # Search Options
    with st.expander("Search Options"):
        search_type = st.selectbox("Search Type", ["Full Text", "Title Only", "Parties Only"])
    
    # Saved Searches  
    with st.expander("Saved Searches"):
        if st.session_state.saved_searches:
            st.success(f"Found {len(st.session_state.saved_searches)} saved searches")
            
            search_names = ["Select a saved search..."] + [search['name'] for search in st.session_state.saved_searches]
            selected_search = st.selectbox("Choose a saved search to load:", search_names)
            
            if selected_search != "Select a saved search...":
                search_obj = next(s for s in st.session_state.saved_searches if s['name'] == selected_search)
                if st.button(f"Load '{selected_search}'"):
                    st.session_state.search_query = search_obj['query']
                    st.success(f"✅ Loaded: {selected_search}")
                    st.rerun()
        else:
            st.info("No saved searches")
    
    # Search Filters
    st.subheader("Search Filters")
    
    # Calculate active filters
    active_filter_count = 0
    
    # Language
    language = st.selectbox("Language", ["All Languages", "English", "French", "Spanish"])
    if language != "All Languages":
        active_filter_count += 1
    
    # Decision Date
    date_range = st.date_input(
        "Decision Date Range",
        value=(date(2020, 1, 1), date(2025, 12, 31)),
        format="YYYY-MM-DD"
    )
    
    # Matter
    matter = st.multiselect(
        "Matter",
        ["Contract", "Transfer", "Disciplinary", "Doping"],
        default=["Contract"]
    )
    if matter:
        active_filter_count += len(matter)
    
    # Outcome
    outcome = st.multiselect(
        "Outcome", 
        ["Dismissed", "Partially upheld", "Upheld"],
        default=["Partially upheld", "Dismissed"]
    )
    if outcome:
        active_filter_count += len(outcome)
    
    # Procedural Types
    with st.expander("Procedural Types"):
        procedural_types = st.multiselect(
            "Procedural Types",
            ["Appeal", "Ordinary", "Expedited"]
        )
        if procedural_types:
            active_filter_count += len(procedural_types)
    
    # Sport
    with st.expander("Sport"):
        sport = st.multiselect(
            "Sport",
            ["Football", "Basketball", "Tennis", "Swimming"], 
            default=["Football"]
        )
        if sport:
            active_filter_count += len(sport)
    
    # Arbitrators
    with st.expander("Arbitrators"):
        arbitrators = st.multiselect(
            "Arbitrators",
            ["Prof. Luigi Fumagalli", "Mr Manfred Nan", "Mr Mark Hovell"]
        )
        if arbitrators:
            active_filter_count += len(arbitrators)
    
    # Active filters summary
    if active_filter_count > 0:
        st.info(f"🎯 {active_filter_count} active filters")
        if st.button("Clear All Filters"):
            st.rerun()

# Initialize search query
if 'search_query' not in st.session_state:
    st.session_state.search_query = "just cause"

# Main content area
search_query = st.text_input("", value=st.session_state.search_query, placeholder="just cause")

if search_query != st.session_state.search_query:
    st.session_state.search_query = search_query

# Action buttons row
col1, col2, col3 = st.columns([2, 2, 4])

with col1:
    if st.button("💾 Save Search", type="secondary"):
        st.session_state.show_save_search_modal = True

with col2:
    if st.button("🔄 New Search", type="secondary"):
        st.session_state.search_query = ""
        st.rerun()

# Notes about the search
notes_text = st.text_area("Notes about the search", placeholder="Will be saved with new ID")

# IMPROVED Save Search Modal
if st.session_state.show_save_search_modal:
    st.markdown("---")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("💾 Save This Search")
    with col2:
        if st.button("✕ Close", key="close_save_modal"):
            st.session_state.show_save_search_modal = False
            st.rerun()
    
    # Preview what will be saved
    st.info(f"**Search Query:** '{search_query}' | **Active Filters:** {active_filter_count}")
    
    # Save form
    col1, col2 = st.columns([2, 1])
    with col1:
        search_name = st.text_input("Search Name:", value=f"Just Cause Research - {datetime.now().strftime('%Y-%m-%d')}")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("✅ Save Search", type="primary", use_container_width=True):
            # Create filter summary
            filter_summary = []
            if matter: filter_summary.extend([f"Matter: {m}" for m in matter])
            if outcome: filter_summary.extend([f"Outcome: {o}" for o in outcome])
            if sport: filter_summary.extend([f"Sport: {s}" for s in sport])
            if language != "All Languages": filter_summary.append(f"Language: {language}")
            if procedural_types: filter_summary.extend([f"Procedure: {p}" for p in procedural_types])
            if arbitrators: filter_summary.extend([f"Arbitrator: {a}" for a in arbitrators])
            
            new_search = {
                "name": search_name,
                "query": search_query,
                "filters": filter_summary,
                "notes": notes_text,
                "created": datetime.now()
            }
            st.session_state.saved_searches.append(new_search)
            st.session_state.show_save_search_modal = False
            st.success(f"✅ Search '{search_name}' saved successfully!")
            st.rerun()
    
    with col2:
        if st.button("❌ Cancel", use_container_width=True):
            st.session_state.show_save_search_modal = False
            st.rerun()
    
    st.markdown("---")

# Search results summary
if not st.session_state.show_save_search_modal:
    # Show active filters
    if active_filter_count > 0:
        filter_text = []
        if matter: filter_text.append(f"Matter: {', '.join(matter)}")
        if outcome: filter_text.append(f"Outcome: {', '.join(outcome)}")
        if sport: filter_text.append(f"Sport: {', '.join(sport)}")
        if language != "All Languages": filter_text.append(f"Language: {language}")
        
        st.info(f"**🎯 Active Filters ({active_filter_count}):** {' | '.join(filter_text)}")

    # Results summary with saved cases count
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📄 Results", "15 passages")
    with col2:
        st.metric("⚖️ Cases", "13 decisions")  
    with col3:
        st.metric("📌 My Saved", len(st.session_state.saved_cases))

    # General Answer
    with st.expander("General Answer: Definition of Just Cause in Football Employment Contracts", expanded=True):
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

    st.subheader("Found 15 relevant passages in 13 decisions")

    # IMPROVED Case Results - Collapsed by default with unified save system
    for i, case in enumerate(sample_cases):
        case_key = case['case_id']
        is_saved = case_key in st.session_state.saved_cases
        
        # Case header - COLLAPSED by default with key info and save status
        save_status = "✅ SAVED" if is_saved else ""
        case_title = f"{case['case_id']} {save_status} | 👥 {case['parties']} | 📅 {case['date']} | 📋 {case['matter']} | 🏆 {case['outcome']} | ⚽ {case['sport']}"
        
        with st.expander(case_title, expanded=False):
            # UNIFIED Save Case Section at the top
            st.subheader("📌 Case Actions")
            
            col1, col2, col3 = st.columns([2, 2, 2])
            
            with col1:
                if is_saved:
                    if st.button(f"✅ Saved to My Cases", key=f"saved_{case_key}", disabled=True):
                        pass
                    if st.button(f"🗑️ Remove from My Cases", key=f"remove_{case_key}", type="secondary"):
                        st.session_state.saved_cases.remove(case_key)
                        st.success(f"✅ Removed {case_key} from your collection")
                        st.rerun()
                else:
                    if st.button(f"📌 Save to My Cases", key=f"save_{case_key}", type="primary"):
                        st.session_state.saved_cases.append(case_key)
                        st.success(f"✅ {case_key} saved to your collection!")
                        st.rerun()
            
            with col2:
                if st.button(f"📤 Export Case", key=f"export_{case_key}"):
                    st.info(f"Exported {case_key}")
            
            with col3:
                if st.button(f"🔗 Copy Link", key=f"link_{case_key}"):
                    st.info(f"Link copied for {case_key}")
            
            # Case Details
            st.subheader("📋 Case Information")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Parties:** {case['parties']}")
                st.write(f"**Procedure:** Appeal Arbitration Procedure")
                st.write(f"**Category:** Award")
            
            with col2:
                st.write(f"**Date:** {case['date']}")
                st.write(f"**President:** Mr Mark Hovell")
                st.write(f"**Arbitrators:** Prof. Luigi Fumagalli, Mr Manfred Nan")
            
            # Relevant Passages
            st.subheader("📖 Relevant Passages")
            
            with st.expander("Show adjacent sections | Page 21 | Section: i.", expanded=False):
                st.success("**i. The existence of just cause**")
                
                if case['case_id'] == "CAS 2020/A/7242":
                    st.write("**Summary:** This case involves Al Wahda FSC Company (UAE club), Mr. Mourad Batna (Moroccan footballer), and Al Jazira FSC (UAE club) regarding the termination of Batna's employment contract. Batna terminated his contract citing overdue wages and abusive conduct by Al Wahda, thereafter signing with Al Jazira. Al Wahda claimed Batna left without just cause, seeking compensation and sanctions, while Batna and Al Jazira contended the termination was justified due to unpaid salaries and improper conduct by Al Wahda. The Court of")
            
            # UNIFIED Notes System
            st.subheader("📝 My Notes")
            
            note_key = f"notes_{case_key}"
            current_note = st.session_state.case_notes.get(note_key, "")
            
            new_note = st.text_area(
                "Add your analysis and research notes:",
                value=current_note,
                key=f"textarea_{note_key}",
                placeholder="Add your legal analysis, key findings, citations, or observations about this case...",
                height=120,
                help="Notes are automatically linked to this case and preserved when you save the case to your collection."
            )
            
            col1, col2, col3 = st.columns([1, 1, 2])
            
            with col1:
                if st.button("💾 Save Notes", key=f"save_notes_{case_key}", type="primary"):
                    st.session_state.case_notes[note_key] = new_note
                    st.success(f"✅ Notes saved for {case_key}")
                    st.rerun()
            
            with col2:
                if current_note and st.button("🗑️ Clear Notes", key=f"clear_notes_{case_key}"):
                    st.session_state.case_notes[note_key] = ""
                    st.success("✅ Notes cleared")
                    st.rerun()
            
            with col3:
                if new_note != current_note and new_note.strip():
                    st.warning("⚠️ You have unsaved changes")
                elif current_note:
                    st.success("✅ Notes saved")
                else:
                    st.info("💭 Add notes to capture your analysis")

    # My Research Collection Summary
    if st.session_state.saved_cases or st.session_state.saved_searches:
        st.markdown("---")
        st.subheader("📊 My Research Collection")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.saved_cases:
                st.markdown(f"**📌 Saved Cases ({len(st.session_state.saved_cases)}):**")
                for case_id in st.session_state.saved_cases:
                    has_notes = bool(st.session_state.case_notes.get(f"notes_{case_id}", "").strip())
                    note_indicator = " 📝" if has_notes else ""
                    st.write(f"• {case_id}{note_indicator}")
        
        with col2:
            if st.session_state.saved_searches:
                st.markdown(f"**💾 Saved Searches ({len(st.session_state.saved_searches)}):**")
                for search in st.session_state.saved_searches:
                    filter_count = len(search.get('filters', []))
                    st.write(f"• {search['name']} ({filter_count} filters)")
