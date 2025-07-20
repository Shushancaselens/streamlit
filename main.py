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
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 12px;
        margin: 2px;
        display: inline-block;
        border: 1px solid #93c5fd;
    }
    
    .case-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 16px;
        margin: 8px 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .save-preview {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 12px;
        margin: 8px 0;
    }
    
    .success-message {
        background: #d1fae5;
        border: 1px solid #10b981;
        color: #065f46;
        padding: 8px 12px;
        border-radius: 4px;
        margin: 4px 0;
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
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 12px;
        margin: 8px 0;
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
    st.image("https://via.placeholder.com/120x40/4F46E5/FFFFFF?text=caselens", width=120)

st.title("CAS Case Law Research")

# Sidebar filters
with st.sidebar:
    st.header("🔍 Search")
    
    # Search Options
    with st.expander("Search Options", expanded=False):
        search_type = st.selectbox("Search Type", ["Full Text", "Title Only", "Parties Only"])
    
    # Saved Searches
    with st.expander("Saved Searches", expanded=False):
        if st.session_state.saved_searches:
            st.write(f"Found {len(st.session_state.saved_searches)} saved searches")
            for search in st.session_state.saved_searches:
                if st.button(f"📁 {search['name']}", key=f"load_{search['name']}"):
                    st.session_state.search_query = search['query']
                    st.rerun()
        else:
            st.write("No saved searches")
    
    st.subheader("Search Filters")
    
    # Language filter
    language = st.selectbox("Language", ["All Languages", "English", "French", "Spanish"])
    
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
    
    # Outcome filter
    outcome = st.multiselect(
        "Outcome",
        ["Dismissed", "Partially upheld", "Upheld"],
        default=["Partially upheld", "Dismissed"]
    )
    
    # Sport filter
    sport = st.multiselect(
        "Sport",
        ["Football", "Basketball", "Tennis", "Swimming"],
        default=["Football"]
    )
    
    # Procedural Types
    procedural_types = st.multiselect(
        "Procedural Types",
        ["Appeal", "Ordinary", "Expedited"]
    )
    
    # Arbitrators
    arbitrators = st.multiselect(
        "Arbitrators",
        ["Prof. Luigi Fumagalli", "Mr Manfred Nan", "Mr Mark Hovell"]
    )

# Main content area
search_query = st.text_input("🔍 Search Query", value="just cause", placeholder="Enter your search terms...")

# Active Filters Display (IMPROVEMENT #1)
active_filters = []
if matter: active_filters.extend([f"Matter: {m}" for m in matter])
if outcome: active_filters.extend([f"Outcome: {o}" for o in outcome])
if sport: active_filters.extend([f"Sport: {s}" for s in sport])
if procedural_types: active_filters.extend([f"Procedure: {p}" for p in procedural_types])
if arbitrators: active_filters.extend([f"Arbitrator: {a}" for a in arbitrators])
if language != "All Languages": active_filters.append(f"Language: {language}")

if active_filters:
    st.markdown('<div class="active-filters-bar">', unsafe_allow_html=True)
    st.write(f"**🔍 Applied Filters ({len(active_filters)} active):**")
    
    # Display filter chips
    filter_html = ""
    for filter_item in active_filters:
        filter_html += f'<span class="filter-chip">{filter_item} ✕</span> '
    
    st.markdown(filter_html, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 6])
    with col1:
        if st.button("🗑️ Clear All Filters"):
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Action buttons row
col1, col2, col3, col4 = st.columns([2, 2, 2, 4])

with col1:
    # IMPROVED Save Search Button (IMPROVEMENT #2)
    if st.button("💾 Save Search", type="secondary"):
        st.session_state.show_save_modal = True

with col2:
    if st.button("🔄 New Search"):
        st.session_state.search_query = ""
        st.rerun()

# Save Search Modal (IMPROVEMENT #3)
if st.session_state.show_save_modal:
    with st.container():
        st.markdown("---")
        st.subheader("💾 Save Your Search")
        
        # Preview what will be saved
        with st.container():
            st.markdown('<div class="save-preview">', unsafe_allow_html=True)
            st.write("**Preview of what will be saved:**")
            st.write(f"• **Search Query:** '{search_query}'")
            if active_filters:
                st.write(f"• **Active Filters:** {len(active_filters)} filters")
                for filter_item in active_filters[:3]:  # Show first 3
                    st.write(f"  - {filter_item}")
                if len(active_filters) > 3:
                    st.write(f"  - ... and {len(active_filters)-3} more")
            else:
                st.write("• **Active Filters:** None")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Save form
        search_name = st.text_input("Search Name:", value="Just Cause Research")
        
        email_alerts = st.checkbox("📧 Send me email alerts for new matching cases")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Save Search", type="primary"):
                # Save the search
                new_search = {
                    "name": search_name,
                    "query": search_query,
                    "filters": active_filters.copy(),
                    "created": datetime.now(),
                    "email_alerts": email_alerts
                }
                st.session_state.saved_searches.append(new_search)
                st.session_state.show_save_modal = False
                st.success(f"✅ Search '{search_name}' saved successfully!")
                st.rerun()
        
        with col2:
            if st.button("❌ Cancel"):
                st.session_state.show_save_modal = False
                st.rerun()
        
        st.markdown("---")

# Search results summary
if not st.session_state.show_save_modal:
    st.write("**Found 15 relevant passages in 13 decisions**")

    # General Answer section
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
        """)

    # Case results
    st.subheader("📁 Case Results")

    for i, case in enumerate(sample_cases):
        # IMPROVED Case Display (IMPROVEMENT #4)
        with st.container():
            st.markdown('<div class="case-card">', unsafe_allow_html=True)
            
            # Case header
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{case['case_id']}** | 👥 Parties: {case['parties']} | 📅 Date: {case['date']}")
                st.write(f"📋 Matter: {case['matter']} | 🏆 Outcome: {case['outcome']} | ⚽ Sport: {case['sport']}")
            
            with col2:
                # IMPROVED Save Case Button (IMPROVEMENT #5)
                case_key = case['case_id']
                is_saved = case_key in st.session_state.saved_cases
                
                if is_saved:
                    st.write("✅ **Saved to My Cases**")
                else:
                    if st.button(f"📌 Save to My Cases", key=f"save_{case_key}"):
                        st.session_state.saved_cases.append(case_key)
                        st.success("✅ Case saved to your collection!")
                        st.rerun()
            
            # Case notes section (IMPROVEMENT #6)
            with st.expander(f"📝 Notes for {case['case_id']}", expanded=False):
                note_key = f"notes_{case_key}"
                current_note = st.session_state.case_notes.get(note_key, "")
                
                new_note = st.text_area(
                    "Add your notes about this case:",
                    value=current_note,
                    key=note_key,
                    placeholder="Add analysis, key points, or personal observations..."
                )
                
                col1, col2 = st.columns([1, 3])
                with col1:
                    if st.button(f"💾 Save Notes", key=f"save_notes_{case_key}"):
                        st.session_state.case_notes[note_key] = new_note
                        st.markdown('<div class="success-message">✅ Notes saved successfully!</div>', unsafe_allow_html=True)
                
                with col2:
                    if new_note != current_note:
                        st.markdown('<div class="warning-message">⚠️ You have unsaved changes</div>', unsafe_allow_html=True)
                    else:
                        st.write("💡 **Tip:** Notes are automatically saved when you click 'Save Notes'")
            
            # Case summary
            if case['case_id'] == "CAS 2020/A/7242":
                with st.expander("📖 Case Summary", expanded=False):
                    st.write("""
                    **Summary:** This case involves Al Wahda FSC Company (UAE club), Mr. Mourad Batna (Moroccan footballer), and Al Jazira FSC (UAE club) 
                    regarding the termination of Batna's employment contract. Batna terminated his contract citing overdue wages and abusive conduct by 
                    Al Wahda, thereafter signing with Al Jazira. Al Wahda claimed Batna left without just cause, seeking compensation and sanctions, while 
                    Batna and Al Jazira contended the termination was justified due to unpaid salaries and improper conduct by Al Wahda.
                    """)
            
            st.markdown('</div>', unsafe_allow_html=True)

    # Footer with saved items summary
    if st.session_state.saved_cases or st.session_state.saved_searches:
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.saved_cases:
                st.write(f"📌 **My Saved Cases:** {len(st.session_state.saved_cases)} cases")
                for case_id in st.session_state.saved_cases[-3:]:  # Show last 3
                    st.write(f"  • {case_id}")
        
        with col2:
            if st.session_state.saved_searches:
                st.write(f"💾 **My Saved Searches:** {len(st.session_state.saved_searches)} searches")
                for search in st.session_state.saved_searches[-3:]:  # Show last 3
                    st.write(f"  • {search['name']}")
