import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Legal Document Timeline", layout="wide")

# Custom CSS for clearer visualization
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        padding-top: 1rem;
        max-width: 1200px;
    }
    
    /* Header styling */
    .app-header {
        padding: 15px;
        background-color: #f8fafc;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 20px;
        border-radius: 8px;
    }
    
    /* Document styling */
    .document-box {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: all 0.2s;
    }
    .document-box:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .document-box.selected {
        background-color: #e0f2fe;
        border-color: #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.2);
    }
    
    /* Document type indicators */
    .document-appellant {
        border-left: 5px solid #3b82f6;
    }
    .document-respondent {
        border-left: 5px solid #ef4444;
    }
    .document-system {
        border-left: 5px solid #9ca3af;
    }
    
    /* Event styling */
    .event-box {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 10px;
    }
    .event-box.connected {
        background-color: #e0f2fe;
        border-color: #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.2);
    }
    
    /* Connection line */
    .connection-arrow {
        color: #3b82f6;
        font-size: 24px;
        margin: 0 10px;
    }
    
    /* Tags */
    .tag {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 500;
        margin-right: 5px;
    }
    .appellant-tag {
        background-color: #dbeafe;
        color: #3b82f6;
    }
    .respondent-tag {
        background-color: #fee2e2;
        color: #ef4444;
    }
    .disputed-tag {
        background-color: #fee2e2;
        color: #ef4444;
    }
    .undisputed-tag {
        background-color: #f1f5f9;
        color: #334155;
    }
    
    /* Connection visualization */
    .connection-visual {
        display: flex;
        align-items: center;
        padding: 5px 10px;
        background-color: #f0f7ff;
        border-radius: 8px;
        margin: 10px 0;
        border: 1px dashed #93c5fd;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown("""
<div class="app-header">
    <h1 style="margin: 0; font-size: 1.5rem; color: #334155;">Legal Document Timeline</h1>
    <p style="margin: 5px 0 0 0; color: #64748b;">Visualizing connections between legal documents and case events</p>
</div>
""", unsafe_allow_html=True)

# Define document and event data
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

# Document-Event Connection Visualization
st.markdown("<h2>Document-Event Connections</h2>", unsafe_allow_html=True)
st.markdown("<p>Select a document to see its connections to case events.</p>", unsafe_allow_html=True)

# Create two columns for document selection and connection visualization
doc_col, visual_col = st.columns([1, 3])

# Document selection
with doc_col:
    st.markdown("<h3>Case Documents</h3>", unsafe_allow_html=True)
    
    # Filter buttons
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
    
    # Display document selection
    for doc in filtered_docs:
        # Determine if this document is selected
        is_selected = doc["id"] == st.session_state.selected_doc_id
        
        # Create document box
        doc_class = f"document-box document-{doc['type']} {'selected' if is_selected else ''}"
        
        # Create a container for the document
        doc_container = st.container()
        
        # Display document in the container
        doc_container.markdown(f"""
        <div class="{doc_class}">
            <strong>📁 {doc['name']}</strong>
            <div style="margin-top: 5px;">
                <span class="tag {doc['type']}-tag">{doc['type'].capitalize()}</span>
                {f'<span style="font-size: 0.8rem; color: #64748b;">Filed: {doc["date"]}</span>' if doc['date'] else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Handle clicks with a button (hidden in the same container)
        if doc_container.button(f"Select {doc['name']}", key=f"btn_{doc['id']}", help="Click to view connections"):
            st.session_state.selected_doc_id = doc["id"]
            st.experimental_rerun()

# Get selected document
selected_doc = next((d for d in documents if d["id"] == st.session_state.selected_doc_id), None)
related_events = [e for e in events if selected_doc and selected_doc["id"] in e["related_docs"]]

# Connection visualization
with visual_col:
    if selected_doc:
        st.markdown(f"""
        <h3>Connections for: <span style="color: {('#3b82f6' if selected_doc['type'] == 'appellant' else '#ef4444' if selected_doc['type'] == 'respondent' else '#9ca3af')};">
            {selected_doc['name']}
        </span></h3>
        """, unsafe_allow_html=True)
        
        # Show number of connections
        st.markdown(f"""
        <p>This document is connected to <strong>{len(related_events)}</strong> case events:</p>
        """, unsafe_allow_html=True)
        
        # Display connections
        if related_events:
            for event in related_events:
                # Party tag
                party_tag = f"<span class='tag {'appellant-tag' if event['party'] == 'Appellant' else 'respondent-tag'}'>{event['party']}</span>"
                
                # Status tag
                status_tag = f"<span class='tag {'disputed-tag' if event['status'] == 'Disputed' else 'undisputed-tag'}'>{event['status']}</span>"
                
                # Connection visualization
                st.markdown(f"""
                <div class="connection-visual">
                    <div style="flex: 1;">
                        <strong>📁 {selected_doc['name']}</strong>
                        <div>
                            <span class="tag {selected_doc['type']}-tag">{selected_doc['type'].capitalize()}</span>
                            {f'<span style="font-size: 0.8rem; color: #64748b;">Filed: {selected_doc["date"]}</span>' if selected_doc['date'] else ''}
                        </div>
                    </div>
                    <div class="connection-arrow">→</div>
                    <div style="flex: 2;">
                        <strong>📅 {event['date']}: {event['event']}</strong>
                        <div>
                            {party_tag}
                            {status_tag}
                            <span style="font-size: 0.8rem; background-color: #f3f4f6; padding: 3px 6px; border-radius: 4px;">{event['evidence']}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No events are connected to this document.")

# Create the full case timeline with clear connections
st.markdown("<h2>Case Timeline</h2>", unsafe_allow_html=True)

# Create tabs for filtering events
event_tabs = st.tabs(["All Events", "Disputed Facts", "Undisputed Facts"])

# Helper function to display events
def display_events(event_list, selected_doc_id):
    if not event_list:
        st.info("No events to display.")
        return
    
    # Sort events chronologically
    sorted_events = sorted(event_list, key=lambda x: x['date'].split('-')[0])
    
    # Display each event
    for event in sorted_events:
        # Check if connected to selected document
        is_connected = selected_doc_id in event["related_docs"]
        
        # Get connected documents
        connected_docs = [d for d in documents if d["id"] in event["related_docs"]]
        
        # Party and status tags
        party_tag = f"<span class='tag {'appellant-tag' if event['party'] == 'Appellant' else 'respondent-tag'}'>{event['party']}</span>"
        status_tag = f"<span class='tag {'disputed-tag' if event['status'] == 'Disputed' else 'undisputed-tag'}'>{event['status']}</span>"
        
        # Create event box
        st.markdown(f"""
        <div class="event-box {'connected' if is_connected else ''}">
            <h4 style="margin-top: 0;">{event['date']}: {event['event']}</h4>
            <div style="margin: 8px 0;">
                {party_tag}
                {status_tag}
                <span style="background-color: #f3f4f6; padding: 3px 6px; border-radius: 4px; font-size: 0.8rem;">{event['evidence']}</span>
            </div>
            
            <div style="margin-top: 10px;">
                <strong>Connected Documents:</strong>
                <div style="display: flex; flex-wrap: wrap; gap: 5px; margin-top: 5px;">
                    {' '.join([f'<div style="background-color: {("#dbeafe" if d["type"] == "appellant" else "#fee2e2" if d["type"] == "respondent" else "#f3f4f6")}; padding: 5px 10px; border-radius: 4px; font-size: 0.8rem; border-left: 3px solid {("#3b82f6" if d["type"] == "appellant" else "#ef4444" if d["type"] == "respondent" else "#9ca3af")};"><strong>{"→ " if d["id"] == selected_doc_id else ""}</strong>{d["name"]}</div>' for d in connected_docs])}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Fill the tabs
with event_tabs[0]:  # All Events
    display_events(events, st.session_state.selected_doc_id)

with event_tabs[1]:  # Disputed Facts
    disputed_events = [e for e in events if e["status"] == "Disputed"]
    display_events(disputed_events, st.session_state.selected_doc_id)

with event_tabs[2]:  # Undisputed Facts
    undisputed_events = [e for e in events if e["status"] == "Undisputed"]
    display_events(undisputed_events, st.session_state.selected_doc_id)

# Visual Timeline
if st.checkbox("Show Visual Timeline", value=True):
    st.markdown("<h2>Visual Timeline</h2>", unsafe_allow_html=True)
    
    # Group events by decade
    decades = {}
    for event in events:
        year = event['date'].split('-')[0]
        if year.isdigit():
            decade = f"{int(year) // 10 * 10}s"
            if decade not in decades:
                decades[decade] = []
            decades[decade].append(event)
    
    # Create timeline
    for decade, decade_events in sorted(decades.items()):
        st.markdown(f"<h3>{decade}</h3>", unsafe_allow_html=True)
        
        # Display decades as a horizontal timeline
        events_html = ""
        for event in decade_events:
            # Check if connected
            is_connected = st.session_state.selected_doc_id in event["related_docs"]
            
            # Generate document connections
            connected_docs = [d for d in documents if d["id"] in event["related_docs"]]
            doc_pills = " ".join([f'<span style="background-color: {("#dbeafe" if d["type"] == "appellant" else "#fee2e2" if d["type"] == "respondent" else "#f3f4f6")}; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; white-space: nowrap; margin-right: 3px;"><strong>{"→ " if d["id"] == st.session_state.selected_doc_id else ""}</strong>{d["name"]}</span>' for d in connected_docs])
            
            # Event container
            events_html += f"""
            <div style="min-width: 250px; margin-right: 15px; padding: 10px; border-radius: 8px; border: 1px solid {('#3b82f6' if is_connected else '#e2e8f0')}; background-color: {('#e0f2fe' if is_connected else 'white')};">
                <h4 style="margin-top: 0; font-size: 0.9rem;">{event['date']}</h4>
                <p style="margin: 5px 0; font-size: 0.85rem;">{event['event']}</p>
                <div style="margin-top: 5px;">
                    <span class="tag {'appellant-tag' if event['party'] == 'Appellant' else 'respondent-tag'}" style="font-size: 0.7rem;">{event['party']}</span>
                    <span class="tag {'disputed-tag' if event['status'] == 'Disputed' else 'undisputed-tag'}" style="font-size: 0.7rem;">{event['status']}</span>
                </div>
                <div style="margin-top: 8px; font-size: 0.75rem; overflow-x: auto; white-space: nowrap;">
                    {doc_pills}
                </div>
            </div>
            """
        
        # Display horizontal scrollable timeline
        st.markdown(f"""
        <div style="display: flex; overflow-x: auto; padding: 10px 0; margin-bottom: 20px;">
            {events_html}
        </div>
        """, unsafe_allow_html=True)

# Show document-event matrix
if st.checkbox("Show Document-Event Matrix", value=False):
    st.markdown("<h2>Document-Event Matrix</h2>", unsafe_allow_html=True)
    st.markdown("<p>This matrix shows all connections between documents and events.</p>", unsafe_allow_html=True)
    
    # Create matrix header
    matrix_html = """
    <div style="overflow-x: auto;">
    <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem;">
        <thead>
            <tr>
                <th style="border: 1px solid #e2e8f0; padding: 8px; background-color: #f8fafc;">Documents ↓ / Events →</th>
    """
    
    # Add event headers
    for event in events:
        matrix_html += f"""
        <th style="border: 1px solid #e2e8f0; padding: 8px; background-color: #f8fafc; min-width: 100px;">
            <div style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 150px;">
                {event['date']}
            </div>
            <div style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 150px; font-weight: normal;">
                {event['event'][:20]}...
            </div>
        </th>
        """
    
    matrix_html += "</tr></thead><tbody>"
    
    # Add rows for each document
    for doc in documents:
        matrix_html += f"""
        <tr class="{'highlighted-row' if doc['id'] == st.session_state.selected_doc_id else ''}">
            <td style="border: 1px solid #e2e8f0; padding: 8px; background-color: {('#e0f2fe' if doc['id'] == st.session_state.selected_doc_id else '#f8fafc')};">
                <div style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 200px;">
                    <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background-color: {('#3b82f6' if doc['type'] == 'appellant' else '#ef4444' if doc['type'] == 'respondent' else '#9ca3af')}; margin-right: 5px;"></span>
                    {doc['name']}
                </div>
            </td>
        """
        
        # Add cells showing connections
        for event in events:
            is_connected = doc["id"] in event["related_docs"]
            cell_color = "#e0f2fe" if is_connected else "white"
            cell_text = "✓" if is_connected else ""
            cell_style = f"background-color: {cell_color}; text-align: center; font-weight: bold; color: #3b82f6;" if is_connected else ""
            
            matrix_html += f"""
            <td style="border: 1px solid #e2e8f0; padding: 8px; {cell_style}">
                {cell_text}
            </td>
            """
        
        matrix_html += "</tr>"
    
    matrix_html += "</tbody></table></div>"
    
    # Display matrix
    st.markdown(matrix_html, unsafe_allow_html=True)

# Add explanation
st.markdown("""
---
### How to use this visualization:

1. **Select a document** from the left panel to see its connections
2. **Blue highlighting** shows connected events and documents
3. **Color-coded borders** indicate document type:
   - Blue: Appellant documents
   - Red: Respondent documents
   - Gray: System documents
4. **Visual Timeline** shows events chronologically with document connections
5. **Document-Event Matrix** provides a comprehensive view of all connections
""")
