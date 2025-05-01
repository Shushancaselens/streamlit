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
        .facts-filter-bar {
            display: flex;
            gap: 15px;
            margin-bottom: 15px;
            flex-wrap: wrap;
        }
        .filter-pill {
            display: inline-block;
            padding: 6px 12px;
            background-color: #f1f3f5;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.9em;
        }
        .filter-pill.active {
            background-color: #4285f4;
            color: white;
        }
        .filter-count {
            display: inline-block;
            padding: 2px 6px;
            background-color: rgba(0,0,0,0.1);
            border-radius: 10px;
            margin-left: 5px;
            font-size: 0.8em;
        }
        .sort-icon {
            margin-left: 5px;
            opacity: 0.5;
        }
        .sort-icon.active {
            opacity: 1;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Subtabs for filtering facts
    fact_tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
    
    # Create a function to display facts based on status filter
    def display_facts(status_filter=None):
        # Create control panel for filters
        st.markdown("<div class='facts-controls'>", unsafe_allow_html=True)
        
        # Filter fact data based on status if needed
        if status_filter:
            filtered_facts = df_events[df_events["status"] == status_filter].copy()
        else:
            filtered_facts = df_events.copy()
        
        # Get counts for different categories for filter pills
        party_counts = filtered_facts["party"].value_counts().to_dict()
        argument_counts = filtered_facts["argument"].value_counts().to_dict()
        
        # Top filter section with search
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            search_term = st.text_input("Search Facts:", key=f"search_{status_filter}", placeholder="Search by keyword...")
        
        with col2:
            sort_by = st.selectbox("Sort by:", 
                                  ["Date", "Event", "Party", "Status", "Related Argument", "Evidence"],
                                  key=f"sort_{status_filter}")
        
        with col3:
            sort_order = st.radio("Order:", ["Ascending", "Descending"], horizontal=True, key=f"order_{status_filter}")
        
        # Filter pills for Party
        st.markdown("<div class='facts-filter-bar'>", unsafe_allow_html=True)
        st.markdown("<strong style='margin-right:10px;'>Party:</strong>", unsafe_allow_html=True)
        
        # Create filter pills for parties
        selected_party = st.session_state.get(f"party_filter_{status_filter}", "All")
        
        # All pill
        all_active = "active" if selected_party == "All" else ""
        all_count = len(filtered_facts)
        st.markdown(f"<span class='filter-pill {all_active}' onclick=\"setPartyFilter('{status_filter}', 'All')\">All <span class='filter-count'>{all_count}</span></span>", unsafe_allow_html=True)
        
        # Appellant pill
        appellant_active = "active" if selected_party == "Appellant" else ""
        appellant_count = party_counts.get("Appellant", 0)
        st.markdown(f"<span class='filter-pill {appellant_active}' onclick=\"setPartyFilter('{status_filter}', 'Appellant')\">Appellant <span class='filter-count'>{appellant_count}</span></span>", unsafe_allow_html=True)
        
        # Respondent pill
        respondent_active = "active" if selected_party == "Respondent" else ""
        respondent_count = party_counts.get("Respondent", 0)
        st.markdown(f"<span class='filter-pill {respondent_active}' onclick=\"setPartyFilter('{status_filter}', 'Respondent')\">Respondent <span class='filter-count'>{respondent_count}</span></span>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Filter pills for Arguments
        st.markdown("<div class='facts-filter-bar'>", unsafe_allow_html=True)
        st.markdown("<strong style='margin-right:10px;'>Argument:</strong>", unsafe_allow_html=True)
        
        # Create filter pills for arguments
        selected_argument = st.session_state.get(f"argument_filter_{status_filter}", "All")
        
        # All pill for arguments
        all_arg_active = "active" if selected_argument == "All" else ""
        st.markdown(f"<span class='filter-pill {all_arg_active}' onclick=\"setArgumentFilter('{status_filter}', 'All')\">All <span class='filter-count'>{all_count}</span></span>", unsafe_allow_html=True)
        
        # Top 5 arguments as pills (to prevent too many)
        top_arguments = sorted(argument_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        for arg, count in top_arguments:
            arg_active = "active" if selected_argument == arg else ""
            st.markdown(f"<span class='filter-pill {arg_active}' onclick=\"setArgumentFilter('{status_filter}', '{arg}')\">{'...' if len(arg) > 15 else ''}{arg[-15:] if len(arg) > 15 else arg} <span class='filter-count'>{count}</span></span>", unsafe_allow_html=True)
        
        # More filter dropdown if there are more than 5 arguments
        if len(argument_counts) > 5:
            other_arguments = sorted(argument_counts.items(), key=lambda x: x[1], reverse=True)[5:]
            if other_arguments:
                with st.expander("More arguments..."):
                    for arg, count in other_arguments:
                        arg_active = "active" if selected_argument == arg else ""
                        st.markdown(f"<span class='filter-pill {arg_active}' onclick=\"setArgumentFilter('{status_filter}', '{arg}')\">{arg} <span class='filter-count'>{count}</span></span>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)  # End of facts-controls
        
        # Apply search filter if needed
        if search_term:
            filtered_facts = filtered_facts[
                filtered_facts["event"].str.lower().str.contains(search_term.lower()) | 
                filtered_facts["argument"].str.lower().str.contains(search_term.lower())
            ]
        
        # Apply party filter if needed
        if selected_party != "All":
            filtered_facts = filtered_facts[filtered_facts["party"] == selected_party]
        
        # Apply argument filter if needed
        if selected_argument != "All":
            filtered_facts = filtered_facts[filtered_facts["argument"] == selected_argument]
        
        # Convert to a formatted DataFrame for display
        facts_df = filtered_facts[["date", "event", "party", "status", "argument", "evidence"]].copy()
        facts_df = facts_df.rename(columns={
            "date": "Date", 
            "event": "Event", 
            "party": "Party", 
            "status": "Status", 
            "argument": "Related Argument", 
            "evidence": "Evidence"
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
        
        if len(facts_df) > 0:
            # Display the table with classes for styling
            html_table = facts_df.to_html(escape=False, index=False)
            html_table = html_table.replace('<table', '<table class="facts-table"')
            html_table = html_table.replace('<th>Date</th>', '<th class="date-column">Date</th>')
            html_table = html_table.replace('<th>Event</th>', '<th class="event-column">Event</th>')
            html_table = html_table.replace('<th>Party</th>', '<th class="party-column">Party</th>')
            html_table = html_table.replace('<th>Status</th>', '<th class="status-column">Status</th>')
            html_table = html_table.replace('<th>Related Argument</th>', '<th class="argument-column">Related Argument</th>')
            html_table = html_table.replace('<th>Evidence</th>', '<th class="evidence-column">Evidence</th>')
            
            st.markdown(f"<div class='table-container'>{html_table}</div>", unsafe_allow_html=True)
            
            # Add download button for the filtered data
            csv = facts_df.to_csv(index=False).encode('utf-8')
            status_label = f"{status_filter}_" if status_filter else ""
            st.download_button(
                label=f"Download {status_label}Facts",
                data=csv,
                file_name=f"{status_label.lower()}facts.csv",
                mime="text/csv",
            )
        else:
            st.info("No facts match the current filters.")
    
    # Display the appropriate facts based on the selected tab
    with fact_tabs[0]:  # All Facts
        display_facts()
    
    with fact_tabs[1]:  # Disputed Facts
        display_facts("Disputed")
    
    with fact_tabs[2]:  # Undisputed Facts
        display_facts("Undisputed")
    
    # Add JavaScript for interactivity
    st.markdown("""
    <script>
    function setPartyFilter(statusFilter, party) {
        // Create a key for session state
        const key = `party_filter_${statusFilter}`;
        
        // Use Streamlit's setComponentValue to update session state
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: {
                [key]: party
            }
        }, '*');
    }
    
    function setArgumentFilter(statusFilter, argument) {
        // Create a key for session state
        const key = `argument_filter_${statusFilter}`;
        
        // Use Streamlit's setComponentValue to update session state
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: {
                [key]: argument
            }
        }, '*');
    }
    </script>
    """, unsafe_allow_html=True)

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
    
    # Create control panel for filters
    st.markdown("<div class='timeline-controls'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Filter by party
        party_filter = st.multiselect(
            "Filter by Party:",
            options=["All", "Appellant", "Respondent", "N/A"],
            default=["All"]
        )
    
    with col2:
        # Filter by status
        status_filter = st.multiselect(
            "Filter by Status:",
            options=["All", "Disputed", "Undisputed"],
            default=["All"]
        )
    
    with col3:
        # Filter by date range
        min_date = pd.to_datetime(df_events["date"].min())
        max_date = pd.to_datetime(df_events["date"].max())
        
        date_range = st.date_input(
            "Date Range:",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )
    
    # Search functionality
    search_term = st.text_input("Search Events:", placeholder="Enter keywords...")
    
    # Display options
    col1, col2 = st.columns(2)
    with col1:
        view_mode = st.radio(
            "View Mode:",
            options=["By Document", "By Timeline"],
            horizontal=True
        )
    with col2:
        display_mode = st.radio(
            "Display Mode:",
            options=["Compact", "Detailed"],
            horizontal=True
        )
    
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
    
    # Group events by document
    if view_mode == "By Document":
        # Create document set groups
        document_set_data = {}
        
        # Organize documents into sets
        for set_name, doc_ids in document_sets.items():
            document_set_data[set_name] = []
            
            # Filter events for this document set
            set_events = filtered_events[filtered_events["document_id"].isin(doc_ids)]
            
            # Group by document_id within the set
            for doc_id, events in set_events.groupby("document_id"):
                doc_info = df_folders[df_folders["id"] == doc_id].iloc[0]
                
                # Get timeline events for this document
                doc_timeline = []
                for _, event in events.iterrows():
                    doc_timeline.append({
                        "date": event["date"],
                        "datetime": event["datetime"],
                        "end_date": event["end_date"] if pd.notna(event["end_date"]) and event["end_date"] != "None" else None,
                        "event": event["event"],
                        "party": event["party"],
                        "status": event["status"],
                        "argument": event["argument"],
                        "evidence": event["evidence"]
                    })
                
                # Sort events by date
                doc_timeline = sorted(doc_timeline, key=lambda x: x["datetime"])
                
                document_set_data[set_name].append({
                    "document": doc_info["name"],
                    "party": doc_info["party"],
                    "events": doc_timeline
                })
        
        # Display the connected timeline organized by document sets
        st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
        
        # Count total events in all filtered documents
        total_events = sum(len(doc["events"]) for docs in document_set_data.values() for doc in docs)
        
        for set_name, docs in document_set_data.items():
            # Count events in this document set
            set_event_count = sum(len(doc["events"]) for doc in docs)
            
            if set_event_count == 0:
                continue  # Skip empty document sets
                
            # Create expandable section for each document set
            with st.expander(f"{set_name} ({set_event_count} events)"):
                for doc in docs:
                    if not doc["events"]:
                        continue  # Skip documents with no matching events
                        
                    # Display document header
                    party_class = ""
                    if doc["party"] == "Appellant":
                        party_class = "appellant"
                    elif doc["party"] == "Respondent":
                        party_class = "respondent"
                    
                    st.markdown(f"<div class='document-subset-header'>{doc['document']} ({len(doc['events'])} events) <span class='party-tag {party_class}'>{doc['party']}</span></div>", unsafe_allow_html=True)
                    
                    # Display events for this document
                    if display_mode == "Compact":
                        st.markdown("<div class='compact-timeline'>", unsafe_allow_html=True)
                        for event in doc["events"]:
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
                                        <span>{event["argument"]}</span>
                                    </div>
                                </div>
                            </div>
                            """
                            st.markdown(timeline_html, unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        # Detailed view
                        for event in doc["events"]:
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
                            
                            # Create timeline item
                            timeline_html = f"""
                            <div class="timeline-item">
                                <div class="timeline-date">{date_display}</div>
                                <div class="timeline-event">
                                    <strong>{event["event"]}</strong>
                                </div>
                                <div style="margin-top: 5px;">
                                    <span class="status-tag {status_class}">{event["status"]}</span>
                                    <span class="evidence-tag">{event["evidence"]}</span>
                                </div>
                                <div style="margin-top: 5px;">
                                    <span>{event["argument"]}</span>
                                </div>
                            </div>
                            """
                            st.markdown(timeline_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:  # View mode: By Timeline
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
                    
                    # Display events for this document
                    if display_mode == "Compact":
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
                    else:
                        # Detailed view
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
                            
                            # Create timeline item
                            timeline_html = f"""
                            <div class="timeline-item">
                                <div class="timeline-date">{date_display}</div>
                                <div class="timeline-event">
                                    <strong>{event["event"]}</strong>
                                </div>
                                <div style="margin-top: 5px;">
                                    <span class="status-tag {status_class}">{event["status"]}</span>
                                    <span class="evidence-tag">{event["evidence"]}</span>
                                </div>
                                <div style="margin-top: 5px;">
                                    {event["argument"]}
                                </div>
                            </div>
                            """
                            st.markdown(timeline_html, unsafe_allow_html=True)
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
