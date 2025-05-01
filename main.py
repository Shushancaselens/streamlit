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

# Header with logo and title
col1, col2 = st.columns([1, 11])
with col1:
    st.markdown('<div style="background-color: #4285f4; width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">CL</div>', unsafe_allow_html=True)
with col2:
    st.title("CaseLens")

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

# Create two tabs
tab1, tab2 = st.tabs(["Case Facts", "Connected View"])

with tab1:
    # Add CSS for improved Facts tab
    st.markdown("""
    <style>
        .facts-controls {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
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
        .document-set-header {
            background-color: #4285f4;
            color: white;
            padding: 10px 15px;
            border-radius: 4px;
            margin-top: 20px;
            margin-bottom: 10px;
            font-weight: bold;
            font-size: 1.1em;
        }
        .document-subset-header {
            background-color: #f8f9fa;
            padding: 8px 12px;
            border-radius: 4px;
            margin-top: 8px;
            margin-bottom: 5px;
            font-weight: 500;
            border-left: 3px solid #4285f4;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Create control panel for filters
    st.markdown("<div class='facts-controls'>", unsafe_allow_html=True)
    
    # Top filter section - now with more dropdowns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        search_term = st.text_input("Search Facts:", placeholder="Search by keyword...", key="facts_search")
    
    # Create a row of dropdown filters
    filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)
    
    with filter_col1:
        sort_by = st.selectbox("Sort by:", 
                              ["Date", "Event", "Party", "Status", "Related Argument", "Evidence"],
                              key="facts_sort")
    
    with filter_col2:
        sort_order = st.selectbox("Order:", 
                                 ["Ascending", "Descending"], 
                                 key="facts_order")
    
    with filter_col3:
        # Status filter dropdown
        status_filter = st.selectbox(
            "Filter by status:",
            options=["All", "Disputed", "Undisputed"],
            key="status_filter"
        )
    
    with filter_col4:
        # View mode dropdown
        view_mode = st.selectbox(
            "View Mode:",
            options=["Table View", "Document Sets View"],
            key="facts_view_mode"
        )
    
    st.markdown("</div>", unsafe_allow_html=True)  # End of facts-controls
    
    # Get the data and apply filters
    filtered_facts = df_events.copy()
    
    # Apply status filter if needed
    if status_filter != "All":
        filtered_facts = filtered_facts[filtered_facts["status"] == status_filter]
    
    # Apply search filter if needed
    if search_term:
        filtered_facts = filtered_facts[
            filtered_facts["event"].str.lower().str.contains(search_term.lower()) | 
            filtered_facts["argument"].str.lower().str.contains(search_term.lower())
        ]
    
    # Convert to a formatted DataFrame for display
    facts_df = filtered_facts[["date", "event", "party", "status", "argument", "evidence", "document_id"]].copy()
    facts_df = facts_df.rename(columns={
        "date": "Date", 
        "event": "Event", 
        "party": "Party", 
        "status": "Status", 
        "argument": "Related Argument", 
        "evidence": "Evidence",
        "document_id": "Document ID"
    })
    
    # Sort the data
    sort_col = sort_by
    is_ascending = sort_order == "Ascending"
    facts_df = facts_df.sort_values(by=sort_col, ascending=is_ascending)
    
    # Format the data for display
    def format_party(party):
        if party == "Appellant":
            return f'<span class="party-tag appellant">{party}</span>'
        elif party == "Respondent":
            return f'<span class="party-tag respondent">{party}</span>'
        else:
            return party
    
    def format_status(status):
        if status == "Disputed":
            return f'<span class="status-tag disputed">{status}</span>'
        elif status == "Undisputed":
            return f'<span class="status-tag undisputed">{status}</span>'
        else:
            return status
    
    def format_evidence(evidence):
        return f'<span class="evidence-tag">{evidence}</span>'
    
    # Apply formatting
    facts_df["Party"] = facts_df["Party"].apply(format_party)
    facts_df["Status"] = facts_df["Status"].apply(format_status)
    facts_df["Evidence"] = facts_df["Evidence"].apply(format_evidence)
    
    # Display facts count
    st.write(f"**Found {len(facts_df)} facts**")
    
    if len(facts_df) > 0:
        # TABLE VIEW
        if view_mode == "Table View":
            # Display the table with classes for styling
            display_df = facts_df.drop(columns=["Document ID"])  # Don't show document ID in table view
            html_table = display_df.to_html(escape=False, index=False)
            html_table = html_table.replace('<table', '<table class="facts-table"')
            html_table = html_table.replace('<th>Date</th>', '<th class="date-column">Date</th>')
            html_table = html_table.replace('<th>Event</th>', '<th class="event-column">Event</th>')
            html_table = html_table.replace('<th>Party</th>', '<th class="party-column">Party</th>')
            html_table = html_table.replace('<th>Status</th>', '<th class="status-column">Status</th>')
            html_table = html_table.replace('<th>Related Argument</th>', '<th class="argument-column">Related Argument</th>')
            html_table = html_table.replace('<th>Evidence</th>', '<th class="evidence-column">Evidence</th>')
            
            st.markdown(f"<div class='table-container'>{html_table}</div>", unsafe_allow_html=True)
        
        # DOCUMENT SETS VIEW
        else:
            # Define document sets (same as in Connected View)
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
            
            # Group facts by document set
            facts_by_set = {}
            for _, fact in facts_df.iterrows():
                doc_id = fact["Document ID"]
                doc_set = doc_to_set.get(doc_id, "Other Documents")
                
                if doc_set not in facts_by_set:
                    facts_by_set[doc_set] = []
                
                facts_by_set[doc_set].append(fact)
            
            # Sort document sets (optional - by first date in each set)
            sorted_sets = sorted(
                facts_by_set.items(),
                key=lambda x: pd.to_datetime(x[1][0]["Date"]) if x[1] else pd.Timestamp.max
            )
            
            # Display facts grouped by document sets
            for doc_set, facts in sorted_sets:
                if not facts:
                    continue
                
                st.markdown(f"<div class='document-set-header'>{doc_set} ({len(facts)} facts)</div>", unsafe_allow_html=True)
                
                # Group by document within the set
                doc_ids = set([fact["Document ID"] for fact in facts])
                
                # Get document names for each ID
                for doc_id in doc_ids:
                    # Get document name
                    doc_info = df_folders[df_folders["id"] == doc_id].iloc[0]
                    doc_name = doc_info["name"]
                    doc_party = doc_info["party"]
                    
                    # Filter facts for this document
                    doc_facts = [fact for fact in facts if fact["Document ID"] == doc_id]
                    
                    # Format document party for display
                    party_class = ""
                    if doc_party == "Appellant":
                        party_class = "appellant"
                    elif doc_party == "Respondent":
                        party_class = "respondent"
                    
                    st.markdown(f"<div class='document-subset-header'>{doc_name} ({len(doc_facts)} facts) <span class='party-tag {party_class}'>{doc_party}</span></div>", unsafe_allow_html=True)
                    
                    # Create DataFrame for this document
                    doc_df = pd.DataFrame(doc_facts)
                    doc_df = doc_df.drop(columns=["Document ID"])  # Don't need to show this column
                    
                    # Display the document facts table
                    html_table = doc_df.to_html(escape=False, index=False)
                    html_table = html_table.replace('<table', '<table class="facts-table"')
                    html_table = html_table.replace('<th>Date</th>', '<th class="date-column">Date</th>')
                    html_table = html_table.replace('<th>Event</th>', '<th class="event-column">Event</th>')
                    html_table = html_table.replace('<th>Party</th>', '<th class="party-column">Party</th>')
                    html_table = html_table.replace('<th>Status</th>', '<th class="status-column">Status</th>')
                    html_table = html_table.replace('<th>Related Argument</th>', '<th class="argument-column">Related Argument</th>')
                    html_table = html_table.replace('<th>Evidence</th>', '<th class="evidence-column">Evidence</th>')
                    
                    st.markdown(f"<div class='table-container'>{html_table}</div>", unsafe_allow_html=True)
        
        # Add download button for the filtered data
        csv = facts_df.drop(columns=["Document ID"]).to_csv(index=False).encode('utf-8')
        status_label = f"{status_filter}_" if status_filter != "All" else ""
        st.download_button(
            label=f"Download {status_label}Facts",
            data=csv,
            file_name=f"{status_label.lower()}facts.csv",
            mime="text/csv",
        )
    else:
        st.info("No facts match the current filters.")

# Tab 2 is now Connected View (former tab3)

with tab2:
    st.markdown("### Connected Timeline View")
    
    # Add additional CSS for the improved connected view
    st.markdown("""
    <style>
        .document-set-header {
            background-color: #4285f4;
            color: white;
            padding: 10px 15px;
            border-radius: 4px;
            margin-top: 15px;
            margin-bottom: 10px;
            font-weight: bold;
            font-size: 1.1em;
        }
        .document-subset-header {
            background-color: #f8f9fa;
            padding: 8px 12px;
            border-radius: 4px;
            margin-top: 8px;
            margin-bottom: 5px;
            font-weight: 500;
            border-left: 3px solid #4285f4;
        }
        .timeline-controls {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
        .event-counter {
            font-size: 0.8em;
            color: #666;
            margin-left: 5px;
        }
        .timeline-container {
            max-height: 600px;
            overflow-y: auto;
            padding-right: 10px;
        }
        .compact-timeline .timeline-item {
            padding-bottom: 8px;
            margin-bottom: 5px;
        }
        .timeline-connector {
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 2px;
            background-color: #ddd;
            z-index: -1;
        }
        .timeline-event-compact {
            display: flex;
            align-items: flex-start;
            margin-bottom: 5px;
        }
        .timeline-date-compact {
            width: 120px;
            flex-shrink: 0;
            font-weight: 500;
            font-size: 0.9em;
        }
        .timeline-content-compact {
            flex-grow: 1;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Create control panel for filters with improved dropdowns
    st.markdown("<div class='timeline-controls'>", unsafe_allow_html=True)
    
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
    
    st.markdown("</div>", unsafe_allow_html=True)
    
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
            # Display all facts together in timeline format
            st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
            st.markdown("<div class='compact-timeline'>", unsafe_allow_html=True)
            
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
                
                # Create compact timeline item
                timeline_html = f"""
                <div class="timeline-event-compact">
                    <div class="timeline-date-compact">{date_display}</div>
                    <div class="timeline-content-compact">
                        <strong>{event["event"]}</strong>
                        <div style="margin-top: 2px;">
                            <span class="party-tag {party_class}">{event["party"]}</span>
                            <span class="status-tag {status_class}">{event["status"]}</span>
                            <span class="evidence-tag">{event["evidence"]}</span>
                        </div>
                        <div style="margin-top: 2px; font-size: 0.9em;">
                            {event["argument"]}
                        </div>
                        <div style="margin-top: 2px; font-size: 0.8em; color: #666;">
                            Source: {event["document"]}
                        </div>
                    </div>
                </div>
                """
                st.markdown(timeline_html, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
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
            
            # Sort document sets by earliest event date
            sorted_sets = sorted(
                events_by_set.items(),
                key=lambda x: min(e["datetime"] for e in x[1])
            )
            
            for doc_set, events in sorted_sets:
                st.markdown(f"<div class='document-set-header'>{doc_set} ({len(events)} events)</div>", unsafe_allow_html=True)
                
                # Group by document within the set
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
                    
                    # Format document party for display
                    party_class = ""
                    if doc_party == "Appellant":
                        party_class = "appellant"
                    elif doc_party == "Respondent":
                        party_class = "respondent"
                    
                    st.markdown(f"<div class='document-subset-header'>{doc_name} ({len(doc_events)} events) <span class='party-tag {party_class}'>{doc_party}</span></div>", unsafe_allow_html=True)
                    
                    # Sort events by date
                    doc_events = sorted(doc_events, key=lambda x: x["datetime"])
                    
                    # Display events for this document - always use compact mode
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
