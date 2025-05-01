import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="CaseLens - Document Timeline", layout="wide")

# Add custom CSS
st.markdown("""
<style>
    .folder-box {
        padding: 10px;
        border-radius: 4px;
        border: 1px solid #e0e0e0;
        margin-bottom: 8px;
    }
    .folder-appellant {
        border-left: 4px solid #3b82f6;
    }
    .folder-respondent {
        border-left: 4px solid #ef4444;
    }
    .folder-system {
        border-left: 4px solid #9ca3af;
    }
    .appellant-tag {
        background-color: #dbeafe;
        color: #3b82f6;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
    }
    .respondent-tag {
        background-color: #fee2e2;
        color: #ef4444;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
    }
    .disputed-tag {
        color: #ef4444;
        font-weight: 500;
    }
    .undisputed-tag {
        color: #333333;
        font-weight: 500;
    }
    .evidence-chip {
        background-color: #f3f4f6;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.8rem;
    }
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    .folder-icon {
        color: #3b82f6;
        margin-right: 10px;
    }
    .connection-line {
        border-left: 2px dashed #cbd5e1;
        padding-left: 15px;
        margin: 5px 0 5px 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <h1>CaseLens - Document Timeline</h1>
</div>
""", unsafe_allow_html=True)

# Define data
folders = [
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
    {"id": 12, "name": "Swiss Court", "type": "system", "date": ""}
]

events = [
    {"date": "1950-present", "event": "Continuous operation under same name since 1950", "party": "Appellant", "status": "Undisputed", "argument": "1. Sporting Succession", "evidence": "C-1", "related_docs": [1]},
    {"date": "1950", "event": "Initial registration in 1950", "party": "Appellant", "status": "Undisputed", "argument": "1.1.1. Registration History", "evidence": "C-2", "related_docs": [1]},
    {"date": "1950-present", "event": "Consistent use of blue and white since founding", "party": "Appellant", "status": "Disputed", "argument": "1.2. Club Colors Analysis", "evidence": "C-4", "related_docs": [1, 5]},
    {"date": "1950-1975", "event": "Pre-1976 colors represented original city district", "party": "Respondent", "status": "Undisputed", "argument": "1.2.1. Color Changes Analysis", "evidence": "R-5", "related_docs": [2, 4]},
    {"date": "1970-1980", "event": "Minor shade variations do not affect continuity", "party": "Appellant", "status": "Undisputed", "argument": "1.2.1. Color Variations Analysis", "evidence": "C-5", "related_docs": [5]},
    {"date": "1975-1976", "event": "Brief administrative gap in 1975-1976", "party": "Appellant", "status": "Disputed", "argument": "1.1.1. Registration History", "evidence": "C-2", "related_docs": [6, 7]},
]

# Create two columns layout
col1, col2 = st.columns([1, 3])

# Left column: Documents
with col1:
    st.subheader("Case Documents")
    
    # Radio buttons for document selection
    selected_doc_id = st.radio(
        "Select a document to see connections:",
        options=[folder["id"] for folder in folders],
        format_func=lambda x: next((f["name"] for f in folders if f["id"] == x), "Unknown")
    )
    
    # Display selected document details
    selected_doc = next((folder for folder in folders if folder["id"] == selected_doc_id), None)
    if selected_doc:
        doc_type_class = f"folder-{selected_doc['type']}"
        doc_type_label = selected_doc['type'].capitalize()
        
        st.markdown(f"""
        <div class="folder-box {doc_type_class}">
            <h3>📁 {selected_doc['name']}</h3>
            <p>Type: <span class="{selected_doc['type']}-tag">{doc_type_label}</span></p>
            <p>Filed: {selected_doc['date'] if selected_doc['date'] else 'N/A'}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show related events
        related_events = [e for e in events if selected_doc_id in e["related_docs"]]
        if related_events:
            st.markdown("### Connected Events:")
            for event in related_events:
                st.markdown(f"""
                <div class="connection-line">
                    <p><strong>{event['date']}</strong>: {event['event']}</p>
                    <p>Status: <span class="{event['status'].lower()}-tag">{event['status']}</span></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No events directly connected to this document.")

# Right column: Timeline
with col2:
    st.subheader("Case Facts Timeline")
    
    # Create tabs
    tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
    
    with tabs[0]:  # All Facts
        # Create a DataFrame for display
        df = pd.DataFrame(events)
        
        # Create a custom table
        for i, event in enumerate(events):
            # Check if this event is connected to the selected document
            is_connected = selected_doc_id in event["related_docs"]
            bg_color = "#f0f7ff" if is_connected else "white"
            
            # Party tag
            if event["party"] == "Appellant":
                party_tag = f'<span class="appellant-tag">{event["party"]}</span>'
            else:
                party_tag = f'<span class="respondent-tag">{event["party"]}</span>'
            
            # Status tag
            status_tag = f'<span class="{event["status"].lower()}-tag">{event["status"]}</span>'
            
            # Create the event card
            st.markdown(f"""
            <div style="padding: 15px; border-radius: 4px; margin-bottom: 10px; background-color: {bg_color}; border: 1px solid #e0e0e0;">
                <div style="display: flex; justify-content: space-between;">
                    <span><strong>{event['date']}</strong></span>
                    {party_tag}
                    {status_tag}
                </div>
                <h4>{event['event']}</h4>
                <div style="display: flex; justify-content: space-between; margin-top: 10px;">
                    <span>{event['argument']}</span>
                    <span class="evidence-chip">{event['evidence']}</span>
                </div>
                {f'<div class="connection-line"><strong>Connected to:</strong> {selected_doc["name"]}</div>' if is_connected else ''}
            </div>
            """, unsafe_allow_html=True)

    with tabs[1]:  # Disputed Facts
        disputed_events = [e for e in events if e["status"] == "Disputed"]
        if disputed_events:
            for event in disputed_events:
                is_connected = selected_doc_id in event["related_docs"]
                bg_color = "#f0f7ff" if is_connected else "white"
                
                if event["party"] == "Appellant":
                    party_tag = f'<span class="appellant-tag">{event["party"]}</span>'
                else:
                    party_tag = f'<span class="respondent-tag">{event["party"]}</span>'
                
                st.markdown(f"""
                <div style="padding: 15px; border-radius: 4px; margin-bottom: 10px; background-color: {bg_color}; border: 1px solid #e0e0e0;">
                    <div style="display: flex; justify-content: space-between;">
                        <span><strong>{event['date']}</strong></span>
                        {party_tag}
                        <span class="disputed-tag">{event['status']}</span>
                    </div>
                    <h4>{event['event']}</h4>
                    <div style="display: flex; justify-content: space-between; margin-top: 10px;">
                        <span>{event['argument']}</span>
                        <span class="evidence-chip">{event['evidence']}</span>
                    </div>
                    {f'<div class="connection-line"><strong>Connected to:</strong> {selected_doc["name"]}</div>' if is_connected else ''}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No disputed facts found.")

    with tabs[2]:  # Undisputed Facts
        undisputed_events = [e for e in events if e["status"] == "Undisputed"]
        if undisputed_events:
            for event in undisputed_events:
                is_connected = selected_doc_id in event["related_docs"]
                bg_color = "#f0f7ff" if is_connected else "white"
                
                if event["party"] == "Appellant":
                    party_tag = f'<span class="appellant-tag">{event["party"]}</span>'
                else:
                    party_tag = f'<span class="respondent-tag">{event["party"]}</span>'
                
                st.markdown(f"""
                <div style="padding: 15px; border-radius: 4px; margin-bottom: 10px; background-color: {bg_color}; border: 1px solid #e0e0e0;">
                    <div style="display: flex; justify-content: space-between;">
                        <span><strong>{event['date']}</strong></span>
                        {party_tag}
                        <span class="undisputed-tag">{event['status']}</span>
                    </div>
                    <h4>{event['event']}</h4>
                    <div style="display: flex; justify-content: space-between; margin-top: 10px;">
                        <span>{event['argument']}</span>
                        <span class="evidence-chip">{event['evidence']}</span>
                    </div>
                    {f'<div class="connection-line"><strong>Connected to:</strong> {selected_doc["name"]}</div>' if is_connected else ''}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No undisputed facts found.")

# Add a footer with information
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p>This application visualizes the connection between legal documents and case timeline events.</p>
</div>
""", unsafe_allow_html=True)
