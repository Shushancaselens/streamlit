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

# Header - keeping original structure
st.markdown("**🏛️ caselens**")
st.title("CAS Case Law Research")

# Sidebar - maintaining original structure
with st.sidebar:
    st.subheader("🔍 Search")
    
    # Search Options - original expandable structure
    with st.expander("Search Options"):
        search_type = st.selectbox("Search Type", ["Full Text", "Title Only", "Parties Only"])
    
    # Saved Searches - original expandable structure  
    with st.expander("Saved Searches"):
        if st.session_state.saved_searches:
            st.success(f"Found {len(st.session_state.saved_searches)} saved searches")
            
            # Choose a saved search to load dropdown
            search_names = ["Select a saved search..."] + [search['name'] for search in st.session_state.saved_searches]
            selected_search = st.selectbox("Choose a saved search to load:", search_names)
            
            if selected_search != "Select a saved search...":
                search_obj = next(s for s in st.session_state.saved_searches if s['name'] == selected_search)
                if st.button(f"Load '{selected_search}'"):
                    st.session_state.search_query = search_obj['query']
                    st.session_state.last_action = f"Loaded search: {selected_search}"
                    st.rerun()
        else:
            st.info("No saved searches")
    
    # Search Filters - keeping original filter structure
    st.subheader("Search Filters")
    
    # Show active filters count - IMPROVEMENT
    active_filter_count = 0
    
    # Language filter
    language = st.selectbox("Language", ["All Languages", "English", "French", "Spanish"])
    if language != "All Languages":
        active_filter_count += 1
    
    # Decision Date filter  
    date_range = st.date_input(
        "Decision Date Range",
        value=(date(2020, 1, 1), date(2025, 12, 31)),
        format="YYYY-MM-DD"
    )
    
    # Matter filter
    matter = st.multiselect(
        "Matter",
        ["Contract", "Transfer", "Disciplinary", "Doping"],
        default=["Contract"]
    )
    if matter:
        active_filter_count += len(matter)
    
    # Outcome filter
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
    
    # IMPROVEMENT: Show active filters summary
    if active_filter_count > 0:
        st.info(f"🎯 {active_filter_count} active filters")
        if st.button("Clear All Filters"):
            st.rerun()
    else:
        st.info("No active filters")

# Main content area - keeping original structure
search_query = st.text_input("Search Query", value=st.session_state.search_query, placeholder="Enter your search terms...")

if search_query != st.session_state.search_query:
    st.session_state.search_query = search_query

# IMPROVEMENT: Show applied filters clearly
if active_filter_count > 0:
    st.info(f"**Active Filters ({active_filter_count}):** " + 
            f"Matter: {', '.join(matter) if matter else 'None'} | " +
            f"Outcome: {', '.join(outcome) if outcome else 'None'} | " + 
            f"Sport: {', '.join(sport) if sport else 'None'}" +
            (f" | Language: {language}" if language != 'All Languages' else "") +
            (f" | Procedure: {', '.join(procedural_types)}" if procedural_types else "") +
            (f" | Arbitrators: {', '.join([a.split()[-1] for a in arbitrators])}" if arbitrators else ""))

# Action buttons - keeping original structure
col1, col2 = st.columns([1, 3])

with col1:
    if st.button("💾 Save Search"):
        st.session_state.show_save_modal = True

with col2:
    # IMPROVEMENT: New Search button
    if st.button("🔄 New Search"):
        st.session_state.search_query = ""
        st.session_state.last_action = "Started new search"
        st.rerun()

# Show last action feedback - IMPROVEMENT
if st.session_state.last_action:
    st.success(f"✅ {st.session_state.last_action}")
    st.session_state.last_action = None

# Save Search Modal - IMPROVEMENT but keeping simple structure
if st.session_state.show_save_modal:
    st.subheader("💾 Save Search")
    
    # Preview in info box
    preview_text = f"Query: '{search_query}'"
    if active_filter_count > 0:
        preview_text += f" | {active_filter_count} filters applied"
    st.info(f"**Will save:** {preview_text}")
    
    search_name = st.text_input("Search Name:", value=f"Just Cause Research - {datetime.now().strftime('%Y-%m-%d')}")
    
    email_alerts = st.checkbox("📧 Send me email alerts for new matching cases")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Save Search", type="primary"):
            # Create filter summary for saving
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

# Notes about the search - keeping original position
if not st.session_state.show_save_modal:
    notes_text = st.text_area("Notes about the search", placeholder="Will be saved with new ID")

# Search results - keeping original structure  
if not st.session_state.show_save_modal:
    # IMPROVEMENT: Better results summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Found Results", "15 passages")
    with col2: 
        st.metric("Total Cases", "13 decisions")
    with col3:
        st.metric("My Saved Cases", len(st.session_state.saved_cases))

    # General Answer - keeping original expandable structure
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

    st.subheader(f"Found 15 relevant passages in 13 decisions")

    # Case results - keeping original structure but with improvements
    for i, case in enumerate(sample_cases):
        case_key = case['case_id']
        is_saved = case_key in st.session_state.saved_cases
        
        # Case header with parties, date, matter, outcome, sport - original structure
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.write(f"**{case['case_id']}** | 👥 Parties: {case['parties']} | 📅 Date: {case['date']} | 📋 Matter: {case['matter']} | 🏆 Outcome: {case['outcome']} | ⚽ Sport: {case['sport']}")
        
        with col2:
            # IMPROVEMENT: Clear save status and better button
            if is_saved:
                st.success("✅ Saved to My Cases")
                if st.button("Remove", key=f"remove_{case_key}"):
                    st.session_state.saved_cases.remove(case_key)
                    st.session_state.last_action = f"Removed {case_key} from saved cases"
                    st.rerun()
            else:
                if st.button("📌 Save to My Cases", key=f"save_{case_key}", type="primary"):
                    st.session_state.saved_cases.append(case_key)
                    st.session_state.last_action = f"✅ {case_key} saved to your cases!"
                    st.rerun()
        
        # Save Case checkbox - keeping original but with improvement
        col1, col2 = st.columns([1, 4])
        with col1:
            save_case_checked = st.checkbox("⭐ Save Case", key=f"checkbox_{case_key}", value=is_saved)
        with col2:
            if is_saved:
                st.success("💡 **Tip:** This case is saved to your collection with notes preserved")
            else:
                st.info("💡 **Tip:** Save cases to keep your notes permanently")
        
        # Relevant Passages - keeping original expandable structure
        with st.expander(f"Relevant Passages | Page 21 | Section: i."):
            st.success("**i. The existence of just cause**")
            
            # Case summary - original structure
            if case['case_id'] == "CAS 2020/A/7242":
                st.write("**Summary:** This case involves Al Wahda FSC Company (UAE club), Mr. Mourad Batna (Moroccan footballer), and Al Jazira FSC (UAE club) regarding the termination of Batna's employment contract. Batna terminated his contract citing overdue wages and abusive conduct by Al Wahda, thereafter signing with Al Jazira. Al Wahda claimed Batna left without just cause, seeking compensation and sanctions, while Batna and Al Jazira contended the termination was justified due to unpaid salaries and improper conduct by Al Wahda. The Court of")
        
        # IMPROVEMENT: Notes section
        with st.expander(f"📝 My Notes for {case['case_id']}"):
            note_key = f"notes_{case_key}"
            current_note = st.session_state.case_notes.get(note_key, "")
            
            new_note = st.text_area(
                "Add your analysis and notes:",
                value=current_note,
                key=f"textarea_{note_key}",
                placeholder="Add your legal analysis, key points, or observations about this case...",
                height=100
            )
            
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💾 Save Notes", key=f"save_notes_{case_key}", type="primary"):
                    st.session_state.case_notes[note_key] = new_note
                    st.session_state.last_action = f"Notes saved for {case_key}"
                    st.rerun()
            
            with col2:
                if new_note != current_note and new_note:
                    st.warning("⚠️ You have unsaved changes")
                elif current_note:
                    st.success("✅ Notes saved")
                else:
                    st.info("💭 Your notes will be saved with this case")
        
        st.divider()

    # Footer - IMPROVEMENT: Summary of saved items
    if st.session_state.saved_cases or st.session_state.saved_searches:
        st.subheader("📊 My Research Collection")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.saved_cases:
                st.write(f"**📌 Saved Cases ({len(st.session_state.saved_cases)}):**")
                for case_id in st.session_state.saved_cases:
                    note_indicator = "📝" if st.session_state.case_notes.get(f"notes_{case_id}") else ""
                    st.write(f"• {case_id} {note_indicator}")
        
        with col2:
            if st.session_state.saved_searches:
                st.write(f"**💾 Saved Searches ({len(st.session_state.saved_searches)}):**")
                for search in st.session_state.saved_searches:
                    filter_count = len(search.get('filters', []))
                    alert_indicator = "📧" if search.get('email_alerts') else ""
                    st.write(f"• {search['name']} ({filter_count} filters) {alert_indicator}")
