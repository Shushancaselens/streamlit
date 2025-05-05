import streamlit as st
import pandas as pd
from datetime import datetime
import json

st.set_page_config(layout="wide")

# Custom CSS for styling similar to the reference image
st.markdown("""
<style>
    .folder {
        background-color: #f8f9fa;
        border-radius: 4px;
        padding: 8px 12px;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
        cursor: pointer;
    }
    .folder:hover {
        background-color: #e9ecef;
    }
    .folder-icon {
        color: #4285f4;
        margin-right: 10px;
    }
    .selected {
        background-color: #e9ecef;
        border-left: 3px solid #4285f4;
    }
    .timeline-item {
        border-left: 2px solid #ccc;
        padding-left: 15px;
        padding-bottom: 15px;
        position: relative;
    }
    .timeline-item:before {
        content: '';
        width: 12px;
        height: 12px;
        background-color: white;
        border: 2px solid #4285f4;
        border-radius: 50%;
        position: absolute;
        left: -7px;
    }
    .timeline-date {
        font-weight: bold;
        color: #666;
    }
    .timeline-event {
        margin-top: 5px;
    }
    .party-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8em;
        margin-right: 8px;
    }
    .appellant {
        background-color: #e6f2ff;
        color: #0066cc;
    }
    .respondent {
        background-color: #ffebe6;
        color: #cc3300;
    }
    .status-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8em;
        margin-right: 8px;
    }
    .disputed {
        background-color: #ffebe6;
        color: #cc3300;
    }
    .undisputed {
        background-color: #e6f7e6;
        color: #008000;
    }
    .evidence-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8em;
        background-color: #f8f9fa;
        color: #666;
    }
    .header {
        font-weight: bold;
        margin-bottom: 10px;
    }
    .main-container {
        display: flex;
        margin-top: 20px;
    }
    .file-structure {
        width: 30%;
        padding-right: 20px;
    }
    .timeline-view {
        width: 70%;
        border-left: 1px solid #ddd;
        padding-left: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Remove logo and title

# Sidebar navigation
st.sidebar.markdown("## Legal Analysis")
st.sidebar.button("📄 Arguments")
st.sidebar.button("📊 Facts", type="primary")
st.sidebar.button("📁 Exhibits")

# Sample data - in a real app, this would come from a database
document_folders = [
    {"id": 1, "name": "1. Statement of Appeal", "type": "folder", "party": "Appellant"},
    {"id": 2, "name": "2. Request for a Stay", "type": "folder", "party": "Respondent"},
    {"id": 3, "name": "3. Answer to Request for PM", "type": "folder", "party": "Appellant"},
    {"id": 4, "name": "4. Answer to PM", "type": "folder", "party": "Appellant"},
    {"id": 5, "name": "5. Appeal Brief", "type": "folder", "party": "Appellant"},
    {"id": 6, "name": "6. Brief on Admissibility", "type": "folder", "party": "Respondent"},
    {"id": 7, "name": "7. Reply to Objection to Admissibility", "type": "folder", "party": "Appellant"},
    {"id": 8, "name": "8. Challenge", "type": "folder", "party": "Respondent"},
    {"id": 9, "name": "ChatGPT", "type": "folder", "party": "N/A"},
    {"id": 10, "name": "Jurisprudence", "type": "folder", "party": "N/A"},
    {"id": 11, "name": "Objection to Admissibility", "type": "folder", "party": "Respondent"},
    {"id": 12, "name": "Swiss Court", "type": "folder", "party": "N/A"}
]

# Sample events that could be connected to documents
events = [
    {"id": 1, "date": "1950-01-01", "end_date": "present", "event": "Continuous operation under same name since 1950", "party": "Appellant", "status": "Undisputed", "argument": "1. Sporting Succession", "evidence": "C-1", "document_id": 1},
    {"id": 2, "date": "1950-01-01", "end_date": None, "event": "Initial registration in 1950", "party": "Appellant", "status": "Undisputed", "argument": "1.1.1. Registration History", "evidence": "C-2", "document_id": 1},
    {"id": 3, "date": "1950-01-01", "end_date": "present", "event": "Consistent use of blue and white since founding", "party": "Appellant", "status": "Disputed", "argument": "1.2. Club Colors Analysis", "evidence": "C-4", "document_id": 5},
    {"id": 4, "date": "1950-01-01", "end_date": "1975-12-31", "event": "Pre-1976 colors represented original city district", "party": "Respondent", "status": "Undisputed", "argument": "1.2.1. Color Changes Analysis", "evidence": "R-5", "document_id": 2},
    {"id": 5, "date": "1970-01-01", "end_date": "1980-12-31", "event": "Minor shade variations do not affect continuity", "party": "Appellant", "status": "Undisputed", "argument": "1.2.1. Color Variations Analysis", "evidence": "C-5", "document_id": 5},
    {"id": 6, "date": "1975-01-01", "end_date": "1976-12-31", "event": "Brief administrative gap in 1975-1976", "party": "Appellant", "status": "Disputed", "argument": "1.1.1. Registration History", "evidence": "C-2", "document_id": 3},
    {"id": 7, "date": "1975-01-01", "end_date": "1976-12-31", "event": "Operations ceased between 1975-1976", "party": "Respondent", "status": "Disputed", "argument": "1. Sporting Succession", "evidence": "R-1", "document_id": 2},
    {"id": 8, "date": "1976-01-01", "end_date": None, "event": "Filed objection to new registration application", "party": "Respondent", "status": "Disputed", "argument": "1.1.2. Legal Identity", "evidence": "R-3", "document_id": 11},
    {"id": 9, "date": "1977-05-15", "end_date": None, "event": "Court ruling on trademark rights", "party": "N/A", "status": "Undisputed", "argument": "2.1. Legal Precedents", "evidence": "J-1", "document_id": 10},
    {"id": 10, "date": "2023-01-10", "end_date": None, "event": "Statement of Appeal filed", "party": "Appellant", "status": "Undisputed", "argument": "Procedural", "evidence": "A-1", "document_id": 1},
    {"id": 11, "date": "2023-01-25", "end_date": None, "event": "Request for stay submitted", "party": "Respondent", "status": "Undisputed", "argument": "Procedural", "evidence": "R-10", "document_id": 2},
    {"id": 12, "date": "2023-02-15", "end_date": None, "event": "Answer to PM filed", "party": "Appellant", "status": "Undisputed", "argument": "Procedural", "evidence": "A-5", "document_id": 4},
    {"id": 13, "date": "2023-03-01", "end_date": None, "event": "Appeal Brief submitted", "party": "Appellant", "status": "Undisputed", "argument": "Substantive", "evidence": "A-8", "document_id": 5},
    {"id": 14, "date": "2023-03-20", "end_date": None, "event": "Objection to Admissibility filed", "party": "Respondent", "status": "Disputed", "argument": "Procedural", "evidence": "R-15", "document_id": 11},
    {"id": 15, "date": "2023-04-05", "end_date": None, "event": "Reply to Objection submitted", "party": "Appellant", "status": "Undisputed", "argument": "Procedural", "evidence": "A-12", "document_id": 7},
]

# Convert to DataFrames
df_folders = pd.DataFrame(document_folders)
df_events = pd.DataFrame(events)

# Main content area
st.markdown("# Summary of arguments")

# Create two tabs with custom styling to remove white container
st.markdown("""
<style>
    /* Override Streamlit's default styling */
    .stTabs [data-baseweb="tab-panel"] {
        padding: 0 !important;
        margin: 0 !important;
        background-color: transparent !important;
    }
    
    /* Remove white background from tab panels */
    .stTabs [data-baseweb="tab-panel"] > div {
        background-color: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Remove padding from tab list */
    .stTabs [data-baseweb="tab-list"] {
        margin-bottom: 0 !important;
    }
    
    /* Remove padding from controls */
    .facts-controls, .timeline-controls {
        background-color: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Target any div wrapper that Streamlit might add */
    .stTabs [data-baseweb="tab-panel"] > div > div {
        background-color: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Remove any shadow effects that could make it look like a white container */
    .stTabs {
        box-shadow: none !important;
    }
    
    /* CSS for table and document styling */
    .facts-table {
        border-collapse: collapse;
        width: 100%;
    }
    .facts-table th {
        background-color: #f1f3f5;
        padding: 10px;
        text-align: left;
        position: sticky;
        top: 0;
        z-index: 10;
    }
    .facts-table td {
        padding: 8px 10px;
        border-bottom: 1px solid #eee;
    }
    .facts-table tbody tr:hover {
        background-color: #f8f9fa;
    }
    .date-column {
        width: 120px;
    }
    .event-column {
        width: 30%;
    }
    .party-column {
        width: 100px;
    }
    .status-column {
        width: 100px;
    }
    .argument-column {
        width: 25%;
    }
    .evidence-column {
        width: 80px;
    }
    .table-container {
        max-height: 600px;
        overflow-y: auto;
        margin-top: 10px;
    }
    .status-badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 12px;
        margin-right: 8px;
        background-color: #e9ecef;
        font-size: 0.9em;
        cursor: pointer;
    }
    .status-badge.active {
        color: white;
        font-weight: 500;
    }
    .status-badge.all.active {
        background-color: #6c757d;
    }
    .status-badge.disputed.active {
        background-color: #dc3545;
    }
    .status-badge.undisputed.active {
        background-color: #28a745;
    }
    .sort-icon {
        margin-left: 5px;
        opacity: 0.5;
    }
    .sort-icon.active {
        opacity: 1;
    }
    
    /* Vertical timeline with events connected by lines */
    .timeline-container {
        position: relative;
        max-height: 600px;
        overflow-y: auto;
        padding-left: 35px;
        padding-right: 10px;
    }
    
    .timeline-vertical-line {
        position: absolute;
        left: 24px;
        top: 0;
        bottom: 0;
        width: 2px;
        background-color: #4285f4;
        opacity: 0.5;
    }
    
    .timeline-event-compact {
        position: relative;
        margin-bottom: 30px;
        padding-left: 40px;
    }
    
    .timeline-event-dot {
        position: absolute;
        left: -34px;
        top: 8px;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background-color: white;
        border: 3px solid #4285f4;
        z-index: 2;
    }
    
    .timeline-event-connector {
        position: absolute;
        left: -27px;
        top: 24px;
        width: 8px;
        height: 2px;
        background-color: #4285f4;
        z-index: 1;
    }
    
    .timeline-date-compact {
        font-weight: bold;
        color: #4285f4;
        margin-bottom: 8px;
        font-size: 1em;
    }
    
    .timeline-content-compact {
        background-color: #f8f9fa;
        padding: 12px 15px;
        border-radius: 6px;
        border-left: 3px solid #4285f4;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .timeline-content-compact .event-title {
        font-weight: bold;
        font-size: 1.1em;
        margin-bottom: 8px;
        color: #333;
    }
    
    .timeline-content-compact .details-row {
        margin-top: 8px;
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
    }
    
    .timeline-content-compact .argument-text {
        margin-top: 8px;
        font-size: 0.95em;
        color: #555;
        padding: 6px 0;
    }
    
    .timeline-content-compact .source-info {
        margin-top: 8px;
        font-size: 0.9em;
        color: #666;
        font-style: italic;
        border-top: 1px solid #e0e0e0;
        padding-top: 6px;
    }
</style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Case Facts", "Connected View"])

with tab1:
    # Add CSS for improved Facts tab with hierarchical design
    st.markdown("""
    <style>
        .facts-controls-container {
            margin-bottom: 30px;
        }
        
        .facts-button-group {
            display: inline-flex;
            gap: 8px;
            margin-bottom: 20px;
        }
        
        .facts-button {
            padding: 8px 20px;
            border-radius: 4px;
            border: 1px solid #d1d5db;
            background-color: white;
            color: #374151;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .facts-button.active {
            background-color: #3b82f6;
            color: white;
            border-color: #3b82f6;
        }
        
        .facts-header-section {
            margin-bottom: 30px;
        }
        
        .facts-search-container {
            margin-bottom: 20px;
        }
        
        .facts-two-column {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 20px;
        }
        
        .facts-party-column {
            border-left: 3px solid transparent;
            padding-left: 20px;
        }
        
        .facts-appellant-column {
            border-left-color: #3b82f6;
        }
        
        .facts-respondent-column {
            border-left-color: #ef4444;
        }
        
        .facts-party-header {
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #e5e7eb;
        }
        
        .facts-appellant-header {
            color: #3b82f6;
        }
        
        .facts-respondent-header {
            color: #ef4444;
        }
        
        .facts-document-section {
            margin-bottom: 20px;
            border: 1px solid #e5e7eb;
            border-radius: 6px;
            overflow: hidden;
        }
        
        .facts-document-header {
            padding: 10px 15px;
            background-color: #f9fafb;
            border-bottom: 1px solid #e5e7eb;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .facts-document-header:hover {
            background-color: #f3f4f6;
        }
        
        .facts-arrow {
            width: 0;
            height: 0;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-top: 8px solid #666;
            transition: transform 0.2s;
            display: inline-block;
        }
        
        .facts-arrow.collapsed {
            transform: rotate(-90deg);
        }
        
        .facts-document-title {
            font-weight: 500;
        }
        
        .facts-fact-list {
            display: none;
            padding: 0;
            margin: 0;
            list-style: none;
        }
        
        .facts-fact-list.open {
            display: block;
        }
        
        .facts-fact-item {
            padding: 10px 15px;
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: flex-start;
            gap: 10px;
        }
        
        .facts-fact-item:last-child {
            border-bottom: none;
        }
        
        .facts-fact-date {
            min-width: 100px;
            color: #6b7280;
            font-size: 0.9em;
        }
        
        .facts-fact-content {
            flex: 1;
        }
        
        .facts-fact-evidence {
            background-color: #f3f4f6;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            color: #374151;
            margin-left: 10px;
        }
        
        .facts-view-buttons {
            margin-left: auto;
            display: inline-flex;
            gap: 8px;
        }
        
        .facts-view-button {
            padding: 8px 20px;
            border-radius: 4px;
            background-color: white;
            color: #374151;
            font-weight: 500;
            cursor: pointer;
            border: 1px solid #d1d5db;
        }
        
        .facts-view-button.active {
            background-color: #1e40af;
            color: white;
            border-color: #1e40af;
        }
        
        .facts-actions {
            margin-left: auto;
            display: inline-flex;
            gap: 8px;
        }
        
        .facts-action-button {
            padding: 8px 16px;
            border-radius: 4px;
            background-color: white;
            color: #374151;
            border: 1px solid #d1d5db;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header section with title
    st.markdown("""
    <div class='facts-header-section'>
        <h1 style='font-size: 2em; font-weight: bold; margin-bottom: 30px;'>Facts by Document</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Party filter buttons
    st.markdown("""
    <div class='facts-button-group'>
        <button class='facts-button active'>Both Parties</button>
        <button class='facts-button'>Appellant Only</button>
        <button class='facts-button'>Respondent Only</button>
    </div>
    """, unsafe_allow_html=True)
    
    # View toggle and search
    col_left, col_right = st.columns([1, 1])
    with col_left:
        pass  # No search box in the reference design
    with col_right:
        st.markdown("""
        <div class='facts-view-buttons'>
            <button class='facts-view-button'>Document View</button>
            <button class='facts-view-button active'>Table View</button>
        </div>
        """, unsafe_allow_html=True)
    
    # Main content area with two columns
    st.markdown("""
    <div class='facts-two-column'>
        <div class='facts-party-column facts-appellant-column'>
            <h2 class='facts-party-header facts-appellant-header'>Appellant's Facts</h2>
    """, unsafe_allow_html=True)
    
    # Get documents and facts for Appellant
    appellant_docs = {}
    for _, fact in facts_df.iterrows():
        if fact["Party"] in ["<span class='party-tag appellant'>Appellant</span>", "N/A"]:
            doc_id = fact["Document ID"]
            if doc_id not in appellant_docs:
                doc_info = df_folders[df_folders["id"] == doc_id].iloc[0]
                appellant_docs[doc_id] = {"info": doc_info, "facts": []}
            appellant_docs[doc_id]["facts"].append(fact)
    
    # Display appellant documents
    for doc_id, doc_data in appellant_docs.items():
        doc_name = doc_data["info"]["name"]
        facts = doc_data["facts"]
        
        st.markdown(f"""
        <div class='facts-document-section'>
            <div class='facts-document-header' onclick='toggleFacts("doc{doc_id}")'>
                <span class='facts-arrow' id='arrow{doc_id}'></span>
                <span class='facts-document-title'>{doc_name}</span>
            </div>
            <ul class='facts-fact-list' id='doc{doc_id}'>
        """, unsafe_allow_html=True)
        
        for fact in facts:
            st.markdown(f"""
                <li class='facts-fact-item'>
                    <span class='facts-fact-date'>{fact["Date"]}</span>
                    <span class='facts-fact-content'>{fact["Event"]}</span>
                    <span class='facts-fact-evidence'>{fact["Evidence"]}</span>
                </li>
            """, unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='facts-party-column facts-respondent-column'>
            <h2 class='facts-party-header facts-respondent-header'>Respondent's Facts</h2>
    """, unsafe_allow_html=True)
    
    # Get documents and facts for Respondent
    respondent_docs = {}
    for _, fact in facts_df.iterrows():
        if fact["Party"] in ["<span class='party-tag respondent'>Respondent</span>", "N/A"]:
            doc_id = fact["Document ID"]
            if doc_id not in respondent_docs:
                doc_info = df_folders[df_folders["id"] == doc_id].iloc[0]
                respondent_docs[doc_id] = {"info": doc_info, "facts": []}
            respondent_docs[doc_id]["facts"].append(fact)
    
    # Display respondent documents
    for doc_id, doc_data in respondent_docs.items():
        doc_name = doc_data["info"]["name"]
        facts = doc_data["facts"]
        
        st.markdown(f"""
        <div class='facts-document-section'>
            <div class='facts-document-header' onclick='toggleFacts("doc{doc_id}r")'>
                <span class='facts-arrow' id='arrow{doc_id}r'></span>
                <span class='facts-document-title'>{doc_name}</span>
            </div>
            <ul class='facts-fact-list' id='doc{doc_id}r'>
        """, unsafe_allow_html=True)
        
        for fact in facts:
            st.markdown(f"""
                <li class='facts-fact-item'>
                    <span class='facts-fact-date'>{fact["Date"]}</span>
                    <span class='facts-fact-content'>{fact["Event"]}</span>
                    <span class='facts-fact-evidence'>{fact["Evidence"]}</span>
                </li>
            """, unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Add JavaScript for expandable sections
    st.markdown("""
    <script>
    function toggleFacts(id) {
        const factList = document.getElementById(id);
        const arrow = document.getElementById('arrow' + id.replace('doc', '').replace('r', ''));
        
        if (factList.classList.contains('open')) {
            factList.classList.remove('open');
            arrow.classList.add('collapsed');
        } else {
            factList.classList.add('open');
            arrow.classList.remove('collapsed');
        }
    }
    </script>
    """, unsafe_allow_html=True)

with tab2:
    # Make sure filter display works without the containing div
    # Search and date filter row
    search_col, date_col = st.columns([1, 1])
    
    with search_col:
        # Search functionality
        search_term = st.text_input("Search Events:", placeholder="Enter keywords...")
    
    with date_col:
        # Filter by date range
        min_date = pd.to_datetime(df_events["date"].min())
        max_date = pd.to_datetime(df_events["date"].max())
        
        date_range = st.date_input(
            "Date Range:",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )
    
    # Advanced filter options
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    
    with filter_col1:
        # Filter by party - keep as multiselect for multiple selection
        party_filter = st.multiselect(
            "Filter by Party:",
            options=["All", "Appellant", "Respondent", "N/A"],
            default=["All"]
        )
    
    with filter_col2:
        # Filter by status - keep as multiselect for multiple selection
        status_filter = st.multiselect(
            "Filter by Status:",
            options=["All", "Disputed", "Undisputed"],
            default=["All"]
        )
    
    with filter_col3:
        # Display options - change to dropdown
        view_mode = st.selectbox(
            "View Mode:",
            options=["By Document Sets", "All Facts Together"],
            key="connected_view_mode"
        )
    
    # Default to Compact mode (removing the filter as requested)
    display_mode = "Compact"
    
    # Create a visualization showing documents and their connected events
    timeline_data = []
    
    # Convert date strings to datetime for filtering
    df_events["datetime"] = pd.to_datetime(df_events["date"])
    
    # Apply filters
    filtered_events = df_events.copy()
    
    # Party filter
    if "All" not in party_filter:
        filtered_events = filtered_events[filtered_events["party"].isin(party_filter)]
    
    # Status filter
    if "All" not in status_filter:
        filtered_events = filtered_events[filtered_events["status"].isin(status_filter)]
    
    # Date range filter
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_events = filtered_events[
            (filtered_events["datetime"] >= pd.to_datetime(start_date)) & 
            (filtered_events["datetime"] <= pd.to_datetime(end_date))
        ]
    
    # Search term filter
    if search_term:
        search_term = search_term.lower()
        filtered_events = filtered_events[
            filtered_events["event"].str.lower().str.contains(search_term) | 
            filtered_events["argument"].str.lower().str.contains(search_term)
        ]
    
    # Define document sets (imaginary names for demonstration)
    document_sets = {
        "Initial Registration Materials": [1, 2],
        "Trademark Opposition Filings": [3, 4, 11],
        "Appeal Documentation": [5, 6, 7],
        "Procedural Challenges": [8, 12],
        "Supporting Research": [9, 10]
    }
    
    # Create document set mapping for lookup
    doc_to_set = {}
    for set_name, doc_ids in document_sets.items():
        for doc_id in doc_ids:
            doc_to_set[doc_id] = set_name
    
    # Convert to pandas DataFrame for easier manipulation
    all_events = []
    for _, event in filtered_events.iterrows():
        doc_info = df_folders[df_folders["id"] == event["document_id"]].iloc[0]
        
        all_events.append({
            "date": event["date"],
            "datetime": event["datetime"],
            "end_date": event["end_date"] if pd.notna(event["end_date"]) and event["end_date"] != "None" else None,
            "event": event["event"],
            "party": event["party"],
            "status": event["status"],
            "argument": event["argument"],
            "evidence": event["evidence"],
            "document": doc_info["name"],
            "document_party": doc_info["party"],
            "document_set": doc_to_set.get(event["document_id"], "Other Documents")
        })
    
    # Sort events by date
    all_events = sorted(all_events, key=lambda x: x["datetime"])
    
    if not all_events:
        st.info("No events match the current filters.")
    else:
        # Check which view mode is selected
        if view_mode == "All Facts Together":
            # Display all facts together in vertical timeline format
            st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
            
            # Add the continuous vertical line
            st.markdown("<div class='timeline-vertical-line'></div>", unsafe_allow_html=True)
            
            # Sort all events by date
            all_events_sorted = sorted(all_events, key=lambda x: x["datetime"])
            
            # Display each event in timeline format
            for event in all_events_sorted:
                # Format the date range
                if event["end_date"]:
                    date_display = f"{event['date']} to {event['end_date']}"
                else:
                    date_display = event["date"]
                
                # Format status
                status_class = ""
                if event["status"] == "Disputed":
                    status_class = "disputed"
                elif event["status"] == "Undisputed":
                    status_class = "undisputed"
                
                # Format party
                party_class = ""
                if event["party"] == "Appellant":
                    party_class = "appellant"
                elif event["party"] == "Respondent":
                    party_class = "respondent"
                
                # Create vertical timeline item with connecting elements
                timeline_html = f"""
                <div class="timeline-event-compact">
                    <div class="timeline-event-dot"></div>
                    <div class="timeline-event-connector"></div>
                    <div class="timeline-date-compact">{date_display}</div>
                    <div class="timeline-content-compact">
                        <div class="event-title">{event["event"]}</div>
                        <div class="details-row">
                            <span class="party-tag {party_class}">{event["party"]}</span>
                            <span class="status-tag {status_class}">{event["status"]}</span>
                            <span class="evidence-tag">{event["evidence"]}</span>
                        </div>
                        <div class="argument-text">
                            {event["argument"]}
                        </div>
                        <div class="source-info">
                            Source: {event["document"]}
                        </div>
                    </div>
                </div>
                """
                st.markdown(timeline_html, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
        else:
            # Document Sets View (original view)
            # Group events by document set
            events_by_set = {}
            for event in all_events:
                doc_set = event["document_set"]
                if doc_set not in events_by_set:
                    events_by_set[doc_set] = []
                events_by_set[doc_set].append(event)
            
            st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
            
            # Create a flat list of all documents with their events
            all_documents = []
            for doc_set, events in events_by_set.items():
                # Group events by document within the set
                events_by_doc = {}
                for event in events:
                    doc_name = event["document"]
                    if doc_name not in events_by_doc:
                        events_by_doc[doc_name] = []
                    events_by_doc[doc_name].append(event)
                
                for doc_name, doc_events in events_by_doc.items():
                    # Get sample event to determine party
                    sample_event = doc_events[0]
                    doc_party = sample_event["document_party"]
                    all_documents.append({
                        "name": doc_name,
                        "party": doc_party,
                        "set": doc_set,
                        "events": doc_events
                    })
            
            # Display all documents in a flat list
            for doc in all_documents:
                # Format document party for display
                party_class = ""
                if doc["party"] == "Appellant":
                    party_class = "appellant"
                elif doc["party"] == "Respondent":
                    party_class = "respondent"
                
                st.markdown(f"""
                    <div style='background-color: #f8f9fa; padding: 10px 15px; border-radius: 4px; margin-top: 10px; margin-bottom: 5px; font-weight: 500; border-left: 3px solid #4285f4;'>
                        {doc["name"]} 
                        <span style='margin-left: 8px; padding: 2px 8px; border-radius: 12px; font-size: 0.85em; background-color: #e8f0fe; color: #3c4043;'>{doc["set"]}</span>
                        <span class='party-tag {party_class}'>{doc["party"]}</span>
                        <span style='margin-left: 8px; color: #666; font-size: 0.9em;'>({len(doc["events"])} events)</span>
                    </div>
                """, unsafe_allow_html=True)
                
                # Sort events by date
                doc_events = sorted(doc["events"], key=lambda x: x["datetime"])
                
                # Display events for this document
                st.markdown("<div class='compact-timeline'>", unsafe_allow_html=True)
                for event in doc_events:
                    # Format the date range
                    if event["end_date"]:
                        date_display = f"{event['date']} to {event['end_date']}"
                    else:
                        date_display = event["date"]
                    
                    # Format status
                    status_class = ""
                    if event["status"] == "Disputed":
                        status_class = "disputed"
                    elif event["status"] == "Undisputed":
                        status_class = "undisputed"
                    
                    # Create compact timeline item
                    timeline_html = f"""
                    <div class="timeline-event-compact">
                        <div class="timeline-date-compact">{date_display}</div>
                        <div class="timeline-content-compact">
                            <strong>{event["event"]}</strong>
                            <div style="margin-top: 2px;">
                                <span class="status-tag {status_class}">{event["status"]}</span>
                                <span class="evidence-tag">{event["evidence"]}</span>
                            </div>
                            <div style="margin-top: 2px; font-size: 0.9em;">
                                {event["argument"]}
                            </div>
                        </div>
                    </div>
                    """
                    st.markdown(timeline_html, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # Add a download button for the filtered events
    st.download_button(
        "Download Filtered Events as CSV",
        data=filtered_events.to_csv(index=False).encode('utf-8'),
        file_name="filtered_case_events.csv",
        mime="text/csv"
    )

# Add custom JavaScript to handle click events and update state
st.markdown("""
<script>
// Listen for messages from Streamlit
window.addEventListener('message', function(event) {
    // Check if the message is from Streamlit
    if (event.data.type === 'streamlit:componentReady') {
        // Make folders clickable
        const folders = document.querySelectorAll('.folder');
        folders.forEach(folder => {
            folder.addEventListener('click', function() {
                // Get the folder ID from the data attribute
                const folderId = this.getAttribute('data-id');
                
                // Update Streamlit state
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    value: folderId
                }, '*');
            });
        });
    }
});
</script>
""", unsafe_allow_html=True)
