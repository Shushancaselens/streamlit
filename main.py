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
tab1, tab2, tab3 = st.tabs(["Case Facts", "Document Timeline", "Connected View"])

with tab1:
    # Subtabs for filtering facts
    fact_tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
    
    with fact_tabs[0]:  # All Facts
        # Create a table with all the events
        facts_df = df_events[["date", "event", "party", "status", "argument", "evidence"]]
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
        
        # Display the table
        st.write(facts_df.to_html(escape=False, index=False), unsafe_allow_html=True)

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
    
    # Create a visualization showing documents and their connected events
    timeline_data = []
    
    # Group events by document
    document_events = df_events.groupby("document_id")
    
    # Create timeline data
    for doc_id, events in document_events:
        doc_info = df_folders[df_folders["id"] == doc_id].iloc[0]
        
        # Get timeline events for this document
        doc_timeline = []
        for _, event in events.iterrows():
            doc_timeline.append({
                "date": event["date"],
                "end_date": event["end_date"] if pd.notna(event["end_date"]) and event["end_date"] != "None" else None,
                "event": event["event"],
                "party": event["party"],
                "status": event["status"],
                "argument": event["argument"],
                "evidence": event["evidence"]
            })
        
        timeline_data.append({
            "document": doc_info["name"],
            "party": doc_info["party"],
            "events": doc_timeline
        })
    
    # Display the connected timeline
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
            
            # Display events in a timeline
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
