import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Document Connections", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Document box styling */
    .doc-box {
        padding: 10px;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .doc-appellant {
        border-left: 4px solid #3b82f6;
    }
    .doc-respondent {
        border-left: 4px solid #ef4444;
    }
    .doc-system {
        border-left: 4px solid #9ca3af;
    }
    .doc-selected {
        background-color: #f0f7ff;
        border-color: #bfdbfe;
    }
    
    /* Event box styling */
    .event-box {
        padding: 10px;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .event-connected {
        background-color: #f0f7ff;
        border-color: #bfdbfe;
    }
    
    /* Tags */
    .tag {
        display: inline-block;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        margin-right: 5px;
    }
    .tag-blue {
        background-color: #dbeafe;
        color: #3b82f6;
    }
    .tag-red {
        background-color: #fee2e2;
        color: #ef4444;
    }
    .tag-gray {
        background-color: #f3f4f6;
        color: #4b5563;
    }
    
    /* Connection line */
    .connection-line {
        border-left: 2px dashed #93c5fd;
        padding-left: 10px;
        margin: 5px 0 5px 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("Legal Document and Event Connections")

# Define data
documents = [
    {"id": 1, "name": "1. Statement of Appeal", "type": "appellant", "date": "1950-03-15"},
    {"id": 2, "name": "2. Request for a Stay", "type": "respondent", "date": "1950-04-10"},
    {"id": 3, "name": "3. Answer to Request for PM", "type": "appellant", "date": "1950-05-22"},
    {"id": 4, "name": "4. Answer to PM", "type": "respondent", "date": "1950-06-30"},
    {"id": 5, "name": "5. Appeal Brief", "type": "appellant", "date": "1970-08-12"},
    {"id": 6, "name": "6. Brief on Admissibility", "type": "appellant", "date": "1975-01-20"},
    {"id": 7, "name": "7. Reply to Objection to Admissibility", "type": "appellant", "date": "1975-03-05"},
    {"id": 8, "name": "8. Challenge", "type": "respondent", "date": "1975-04-18"},
    {"id": 9, "name": "ChatGPT", "type": "system", "date": ""},
    {"id": 10, "name": "Jurisprudence", "type": "system", "date": ""},
    {"id": 11, "name": "Objection to Admissibility", "type": "respondent", "date": "1975-02-15"},
    {"id": 12, "name": "Swiss Court", "type": "system", "date": ""},
]

events = [
    {"id": 1, "date": "1950-present", "event": "Continuous operation under same name since 1950", "party": "Appellant", "status": "Undisputed", "evidence": "C-1", "related_docs": [1, 5]},
    {"id": 2, "date": "1950", "event": "Initial registration in 1950", "party": "Appellant", "status": "Undisputed", "evidence": "C-2", "related_docs": [1, 6]},
    {"id": 3, "date": "1950-present", "event": "Consistent use of blue and white since founding", "party": "Appellant", "status": "Disputed", "evidence": "C-4", "related_docs": [1, 5]},
    {"id": 4, "date": "1950-1975", "event": "Pre-1976 colors represented original city district", "party": "Respondent", "status": "Undisputed", "evidence": "R-5", "related_docs": [2, 4, 8]},
    {"id": 5, "date": "1970-1980", "event": "Minor shade variations do not affect continuity", "party": "Appellant", "status": "Undisputed", "evidence": "C-5", "related_docs": [5, 7]},
    {"id": 6, "date": "1975-1976", "event": "Brief administrative gap in 1975-1976", "party": "Appellant", "status": "Disputed", "evidence": "C-2", "related_docs": [6, 7]},
    {"id": 7, "date": "1976", "event": "New registration under same name", "party": "Appellant", "status": "Undisputed", "evidence": "C-3", "related_docs": [5, 6]},
    {"id": 8, "date": "1975", "event": "Objection to legitimacy of succession claim", "party": "Respondent", "status": "Disputed", "evidence": "R-3", "related_docs": [8, 11]},
]

# Initialize session state for selected document
if "selected_doc_id" not in st.session_state:
    st.session_state.selected_doc_id = 1

# Create columns for document selection and events
doc_col, event_col = st.columns([1, 2])

# Documents column
with doc_col:
    st.header("Legal Documents")
    
    # Document type filter
    doc_filter = st.radio(
        "Filter documents by type:",
        options=["All", "Appellant", "Respondent", "System"],
        horizontal=True
    )
    
    # Filter documents based on selection
    filtered_docs = documents
    if doc_filter == "Appellant":
        filtered_docs = [d for d in documents if d["type"] == "appellant"]
    elif doc_filter == "Respondent":
        filtered_docs = [d for d in documents if d["type"] == "respondent"]
    elif doc_filter == "System":
        filtered_docs = [d for d in documents if d["type"] == "system"]
    
    # Display documents
    for doc in filtered_docs:
        # Check if selected
        is_selected = doc["id"] == st.session_state.selected_doc_id
        
        # Document CSS classes
        doc_classes = f"doc-box doc-{doc['type']}"
        if is_selected:
            doc_classes += " doc-selected"
        
        # Display document box
        st.markdown(f"""
        <div class="{doc_classes}">
            <strong>📁 {doc['name']}</strong>
            <div style="margin-top: 5px;">
                <span class="tag tag-{'blue' if doc['type'] == 'appellant' else 'red' if doc['type'] == 'respondent' else 'gray'}">
                    {doc['type'].capitalize()}
                </span>
                {f'<span style="font-size: 12px; color: #64748b;">Filed: {doc["date"]}</span>' if doc['date'] else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Button to select document
        if st.button(f"Select", key=f"select_{doc['id']}"):
            st.session_state.selected_doc_id = doc["id"]
            st.rerun()

# Events column
with event_col:
    st.header("Case Timeline Events")
    
    # Get selected document and related events
    selected_doc = next((d for d in documents if d["id"] == st.session_state.selected_doc_id), None)
    related_events = [e for e in events if selected_doc and selected_doc["id"] in e["related_docs"]]
    
    # Display selected document info
    if selected_doc:
        st.subheader(f"Selected Document: {selected_doc['name']}")
        st.markdown(f"""
        <div class="doc-box doc-{selected_doc['type']} doc-selected">
            <strong>📁 {selected_doc['name']}</strong>
            <div style="margin-top: 5px;">
                <span class="tag tag-{'blue' if selected_doc['type'] == 'appellant' else 'red' if selected_doc['type'] == 'respondent' else 'gray'}">
                    {selected_doc['type'].capitalize()}
                </span>
                {f'<span style="font-size: 12px; color: #64748b;">Filed: {selected_doc["date"]}</span>' if selected_doc['date'] else ''}
            </div>
            <div style="margin-top: 10px;">
                <strong>Connected to {len(related_events)} events</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display related events
    st.write("### Connected Events")
    
    if related_events:
        for event in related_events:
            # Event tags
            party_tag_class = "tag-blue" if event["party"] == "Appellant" else "tag-red"
            status_tag_class = "tag-red" if event["status"] == "Disputed" else "tag-gray"
            
            # Display event box
            st.markdown(f"""
            <div class="event-box event-connected">
                <strong>{event['date']}</strong>: {event['event']}
                <div style="margin-top: 5px;">
                    <span class="tag {party_tag_class}">{event['party']}</span>
                    <span class="tag {status_tag_class}">{event['status']}</span>
                    <span class="tag tag-gray">{event['evidence']}</span>
                </div>
                <div class="connection-line" style="margin-top: 8px;">
                    Connected to: <strong>{selected_doc['name']}</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No events are connected to this document.")

    # Display all events with connections highlighted
    st.write("### All Case Events")
    
    # Event filter
    event_filter = st.radio(
        "Filter events by status:",
        options=["All", "Disputed", "Undisputed"],
        horizontal=True
    )
    
    # Filter events based on selection
    filtered_events = events
    if event_filter == "Disputed":
        filtered_events = [e for e in events if e["status"] == "Disputed"]
    elif event_filter == "Undisputed":
        filtered_events = [e for e in events if e["status"] == "Undisputed"]
    
    # Sort events chronologically
    sorted_events = sorted(filtered_events, key=lambda x: x['date'].split('-')[0])
    
    # Display events
    for event in sorted_events:
        # Check if connected to selected document
        is_connected = selected_doc and selected_doc["id"] in event["related_docs"]
        
        # Get all connected documents
        event_docs = [d for d in documents if d["id"] in event["related_docs"]]
        
        # Event CSS classes
        event_classes = "event-box"
        if is_connected:
            event_classes += " event-connected"
        
        # Event tags
        party_tag_class = "tag-blue" if event["party"] == "Appellant" else "tag-red"
        status_tag_class = "tag-red" if event["status"] == "Disputed" else "tag-gray"
        
        # Display event box
        st.markdown(f"""
        <div class="{event_classes}">
            <strong>{event['date']}</strong>: {event['event']}
            <div style="margin-top: 5px;">
                <span class="tag {party_tag_class}">{event['party']}</span>
                <span class="tag {status_tag_class}">{event['status']}</span>
                <span class="tag tag-gray">{event['evidence']}</span>
            </div>
            <div style="margin-top: 8px;">
                <strong>Connected Documents:</strong>
                <div style="margin-top: 5px;">
                    {' '.join([f'<span class="tag tag-{"blue" if d["type"] == "appellant" else "red" if d["type"] == "respondent" else "gray"}">{"→ " if d["id"] == st.session_state.selected_doc_id else ""}{d["name"]}</span>' for d in event_docs])}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Display a simple matrix view
if st.checkbox("Show Document-Event Connection Matrix"):
    st.header("Document-Event Connection Matrix")
    
    # Create a dataframe for the matrix
    matrix_data = []
    
    for doc in documents:
        row = {"Document": doc["name"]}
        for event in events:
            row[f"{event['date']}: {event['event'][:20]}..."] = "✓" if doc["id"] in event["related_docs"] else ""
        matrix_data.append(row)
    
    # Create dataframe
    df = pd.DataFrame(matrix_data)
    
    # Style the dataframe
    def highlight_connections(val):
        if val == "✓":
            return 'background-color: #dbeafe; color: #3b82f6; font-weight: bold; text-align: center'
        return ''
    
    # Display styled dataframe
    st.dataframe(df.style.applymap(highlight_connections, subset=df.columns[1:]))

# Add help information
st.sidebar.title("How to Use")
st.sidebar.write("""
1. Select a document from the left panel
2. Connected events will be highlighted in blue
3. Each event shows which documents it's connected to
4. Filter documents by type or events by status
""")
