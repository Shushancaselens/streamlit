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

# Sample document sets to use throughout the app
document_sets = {
    "ICA Appeal 2023/A/001": "Appeal documents from the main club licensing case",
    "UEFA Club Licensing Documents": "Official licensing documentation for the appeal",
    "CAS Procedure 2023/O/123": "Court of Arbitration for Sport proceedings",
    "Swiss Federal Tribunal Case 4A_248": "Related Swiss federal court documents",
    "Historical Club Records (1950-1980)": "Documentation of club's historical operations"
}

with tab1:
    # Add CSS for improved facts filtering
    st.markdown("""
    <style>
        .fact-filters {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
        .fact-table {
            margin-top: 15px;
        }
        .fact-table th {
            background-color: #f1f3f5;
            padding: 8px;
        }
        .fact-table td {
            padding: 8px;
            border-bottom: 1px solid #eee;
        }
        .fact-table tr:hover {
            background-color: #f8f9fa;
        }
        .filter-pill {
            display: inline-block;
            padding: 4px 12px;
            margin-right: 8px;
            margin-bottom: 8px;
            border-radius: 16px;
            background-color: #e9ecef;
            font-size: 0.9em;
            cursor: pointer;
        }
        .filter-pill:hover {
            background-color: #dee2e6;
        }
        .filter-pill.active {
            background-color: #4285f4;
            color: white;
        }
        .filter-section {
            margin-bottom: 15px;
        }
        .filter-header {
            font-weight: 500;
            margin-bottom: 5px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Create advanced filter UI
    st.markdown("<div class='fact-filters'>", unsafe_allow_html=True)
    
    # Top filter tabs with improved styling
    col1, col2, col3 = st.columns(3)
    with col1:
        status_filter = st.radio(
            "Filter by Status:",
            options=["All Facts", "Disputed Facts", "Undisputed Facts"],
            horizontal=True
        )
    
    with col2:
        party_filter = st.multiselect(
            "Filter by Party:",
            options=["Appellant", "Respondent", "N/A"],
            default=[]
        )
        
    with col3:
        argument_filter = st.selectbox(
            "Filter by Argument:",
            options=["All Arguments"] + sorted(df_events["argument"].unique().tolist())
        )
    
    # Date range filter
    col1, col2 = st.columns(2)
    with col1:
        date_range = st.date_input(
            "Date Range:",
            value=(pd.to_datetime(df_events["date"].min()).date(), 
                   pd.to_datetime(df_events["date"].max()).date())
        )
    
    with col2:
        search_query = st.text_input("Search:", placeholder="Search in events...")
    
    # Evidence filter
    evidence_options = sorted(df_events["evidence"].unique().tolist())
    evidence_filter = st.multiselect(
        "Filter by Evidence:",
        options=evidence_options,
        default=[]
    )
    
    # Apply filters
    filtered_df = df_events.copy()
    
    # Convert date to datetime for filtering
    filtered_df["datetime"] = pd.to_datetime(filtered_df["date"])
    
    # Status filter
    if status_filter == "Disputed Facts":
        filtered_df = filtered_df[filtered_df["status"] == "Disputed"]
    elif status_filter == "Undisputed Facts":
        filtered_df = filtered_df[filtered_df["status"] == "Undisputed"]
    
    # Party filter
    if party_filter:
        filtered_df = filtered_df[filtered_df["party"].isin(party_filter)]
    
    # Argument filter
    if argument_filter != "All Arguments":
        filtered_df = filtered_df[filtered_df["argument"] == argument_filter]
    
    # Date range filter
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df["datetime"].dt.date >= start_date) & 
            (filtered_df["datetime"].dt.date <= end_date)
        ]
    
    # Evidence filter
    if evidence_filter:
        filtered_df = filtered_df[filtered_df["evidence"].isin(evidence_filter)]
    
    # Search query
    if search_query:
        search_query = search_query.lower()
        filtered_df = filtered_df[
            filtered_df["event"].str.lower().str.contains(search_query) | 
            filtered_df["argument"].str.lower().str.contains(search_query)
        ]
    
    # Show active filters summary
    active_filters = []
    if status_filter != "All Facts":
        active_filters.append(f"Status: {status_filter}")
    if party_filter:
        active_filters.append(f"Party: {', '.join(party_filter)}")
    if argument_filter != "All Arguments":
        active_filters.append(f"Argument: {argument_filter}")
    if len(date_range) == 2:
        active_filters.append(f"Date range: {date_range[0]} to {date_range[1]}")
    if evidence_filter:
        active_filters.append(f"Evidence: {', '.join(evidence_filter)}")
    if search_query:
        active_filters.append(f"Search: '{search_query}'")
    
    if active_filters:
        st.markdown(f"**Active Filters:** {' | '.join(active_filters)}")
    
    # Show result count
    st.markdown(f"**Showing {len(filtered_df)} facts**")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Create a table with the filtered events
    if not filtered_df.empty:
        facts_df = filtered_df[["date", "event", "party", "status", "argument", "evidence"]]
        facts_df = facts_df.rename(columns={
            "date": "Date", 
            "event": "Event", 
            "party": "Party", 
            "status": "Status", 
            "argument": "Related Argument", 
            "evidence": "Evidence"
        })
        
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
        
        # Display the table with improved styling
        st.markdown('<div class="fact-table">', unsafe_allow_html=True)
        st.write(facts_df.to_html(escape=False, index=False, classes="fact-table"), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Add export options
        st.download_button(
            "Export Facts as CSV",
            data=filtered_df.to_csv(index=False).encode('utf-8'),
            file_name="case_facts.csv",
            mime="text/csv"
        )
    else:
        st.info("No facts match the current filters.")

with tab2:
    # Create columns for the document structure and timeline
    col1, col2 = st.columns([3, 7])
    
    with col1:
        st.markdown("### Document Structure")
        selected_folder = st.session_state.get("selected_folder", 1)
        
        # Display folders with selection capability
        for folder in document_folders:
            folder_class = "folder selected" if folder["id"] == selected_folder else "folder"
            party_class = ""
            if folder["party"] == "Appellant":
                party_class = "appellant"
            elif folder["party"] == "Respondent":
                party_class = "respondent"
            
            folder_html = f"""
            <div class="{folder_class}" onclick="handleFolderClick({folder['id']})">
                <span class="folder-icon">📁</span> {folder['name']}
                {f'<span class="party-tag {party_class}" style="margin-left: auto;">{folder["party"]}</span>' if folder["party"] != "N/A" else ''}
            </div>
            """
            st.markdown(folder_html, unsafe_allow_html=True)
        
        # JavaScript for handling clicks
        st.markdown("""
        <script>
        function handleFolderClick(id) {
            // Use Streamlit's setComponentValue to update session state
            window.parent.postMessage({
                type: "streamlit:setComponentValue",
                value: id
            }, "*");
        }
        </script>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Document Timeline")
        
        # Filter events for the selected folder
        folder_events = df_events[df_events["document_id"] == selected_folder]
        
        if len(folder_events) > 0:
            for _, event in folder_events.iterrows():
                # Format the date range
                if pd.notna(event["end_date"]) and event["end_date"] != "None":
                    date_display = f"{event['date']} to {event['end_date']}"
                else:
                    date_display = event["date"]
                
                # Format the party tag
                party_class = ""
                if event["party"] == "Appellant":
                    party_class = "appellant"
                elif event["party"] == "Respondent":
                    party_class = "respondent"
                
                # Format the status tag
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
                        <span class="party-tag {party_class}">{event["party"]}</span>
                        <span class="status-tag {status_class}">{event["status"]}</span>
                        <span class="evidence-tag">{event["evidence"]}</span>
                    </div>
                    <div style="margin-top: 5px;">
                        <span>{event["argument"]}</span>
                    </div>
                </div>
                """
                st.markdown(timeline_html, unsafe_allow_html=True)
        else:
            st.info("No events associated with this document.")

with tab3:
    st.markdown("### Connected Timeline View")
    
    # Add additional CSS for the improved connected view
    st.markdown("""
    <style>
        .year-header {
            background-color: #f1f3f5;
            padding: 8px 12px;
            border-radius: 4px;
            margin-top: 15px;
            margin-bottom: 10px;
            font-weight: bold;
        }
        .month-header {
            background-color: #f8f9fa;
            padding: 4px 8px;
            border-radius: 4px;
            margin-top: 8px;
            margin-bottom: 5px;
            font-weight: 500;
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
    
    # Group events by document
    if view_mode == "By Document":
        document_events = filtered_events.groupby("document_id")
        
        # Create timeline data
        for doc_id, events in document_events:
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
            
            timeline_data.append({
                "document": doc_info["name"],
                "party": doc_info["party"],
                "events": doc_timeline
            })
        
        # Display the connected timeline
        st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
        for doc in timeline_data:
            # Create expandable section for each document
            with st.expander(f"{doc['document']} ({len(doc['events'])} events)"):
                # Style based on party
                party_class = ""
                if doc["party"] == "Appellant":
                    party_class = "appellant"
                elif doc["party"] == "Respondent":
                    party_class = "respondent"
                
                st.markdown(f"<span class='party-tag {party_class}'>{doc['party']}</span>", unsafe_allow_html=True)
                
                if not doc["events"]:
                    st.info("No events match the current filters.")
                    continue
                
                # Group events by year and month if there are many
                if len(doc["events"]) > 5:
                    # Group by year
                    years = {}
                    for event in doc["events"]:
                        year = event["datetime"].year
                        if year not in years:
                            years[year] = []
                        years[year].append(event)
                    
                    # Display events grouped by year
                    for year in sorted(years.keys()):
                        st.markdown(f"<div class='year-header'>{year} ({len(years[year])} events)</div>", unsafe_allow_html=True)
                        
                        # Display events for this year
                        if display_mode == "Compact":
                            st.markdown("<div class='compact-timeline'>", unsafe_allow_html=True)
                            for event in years[year]:
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
                            for event in years[year]:
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
                else:
                    # Display events without grouping for smaller sets
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
                "document_party": doc_info["party"]
            })
        
        # Sort events by date
        all_events = sorted(all_events, key=lambda x: x["datetime"])
        
        if not all_events:
            st.info("No events match the current filters.")
        else:
            # Display events grouped by year
            events_by_year = {}
            for event in all_events:
                year = event["datetime"].year
                if year not in events_by_year:
                    events_by_year[year] = []
                events_by_year[year].append(event)
            
            st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
            for year in sorted(events_by_year.keys()):
                st.markdown(f"<div class='year-header'>{year} ({len(events_by_year[year])} events)</div>", unsafe_allow_html=True)
                
                # Group by document type within the document set
                doc_types = {}
                for event in events:
                    # Create document type based on argument or evidence category
                    if "Registration" in event["argument"]:
                        doc_type = "Registration Documents"
                    elif "Color" in event["argument"]:
                        doc_type = "Club Identity Documents"
                    elif "Sporting Succession" in event["argument"]:
                        doc_type = "Historical Continuity Records"
                    elif "Procedural" in event["argument"]:
                        doc_type = "Procedural Filings"
                    else:
                        doc_type = "Supporting Evidence"
                    
                    if doc_type not in doc_types:
                        doc_types[doc_type] = []
                    doc_types[doc_type].append(event)
                
                for doc_type in sorted(doc_types.keys()):
                    st.markdown(f"<div class='month-header'>{doc_type} ({len(doc_types[doc_type])} items)</div>", unsafe_allow_html=True)
                    
                    # Display events for this month
                    if display_mode == "Compact":
                        st.markdown("<div class='compact-timeline'>", unsafe_allow_html=True)
                        for event in events_by_month[month]:
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
                            
                            # Format document party
                            doc_party_class = ""
                            if event["document_party"] == "Appellant":
                                doc_party_class = "appellant"
                            elif event["document_party"] == "Respondent":
                                doc_party_class = "respondent"
                            
                            # Create compact timeline item
                            timeline_html = f"""
                            <div class="timeline-event-compact">
                                <div class="timeline-date-compact">{date_display}</div>
                                <div class="timeline-content-compact">
                                    <strong>{event["event"]}</strong>
                                    <div style="margin-top: 2px;">
                                        <span class="status-tag {status_class}">{event["status"]}</span>
                                        <span class="evidence-tag">{event["evidence"]}</span>
                                        <span class="party-tag {doc_party_class}">{event["document_party"]}</span>
                                    </div>
                                    <div style="margin-top: 2px; font-size: 0.9em;">
                                        Document: {event["document"]}
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
                        for event in events_by_month[month]:
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
                            
                            # Format document party
                            doc_party_class = ""
                            if event["document_party"] == "Appellant":
                                doc_party_class = "appellant"
                            elif event["document_party"] == "Respondent":
                                doc_party_class = "respondent"
                            
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
                                    <span class="party-tag {doc_party_class}">{event["document_party"]}</span>
                                </div>
                                <div style="margin-top: 5px;">
                                    Document: {event["document"]}
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
