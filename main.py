import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="CaseLens - Document Timeline", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }
    
    /* Logo styling */
    .logo-container {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    .logo-box {
        background-color: #3b82f6;
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-right: 10px;
    }
    .logo-text {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1e293b;
    }
    
    /* Card styling */
    .card {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .card-appellant {
        border-left: 4px solid #3b82f6;
    }
    .card-respondent {
        border-left: 4px solid #ef4444;
    }
    .card-system {
        border-left: 4px solid #9ca3af;
    }
    .card-connected {
        background-color: #f0f7ff;
    }
    
    /* Tag styling */
    .tag {
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 500;
        display: inline-block;
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
    
    /* Evidence chip */
    .evidence-chip {
        background-color: #f3f4f6;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.75rem;
        color: #4b5563;
    }
    
    /* Connection line */
    .connection-line {
        border-left: 2px dashed #bfdbfe;
        padding-left: 12px;
        margin: 8px 0 8px 8px;
        color: #3b82f6;
    }
    
    /* Tables */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 1rem;
    }
    .styled-table th {
        background-color: #f8fafc;
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #e2e8f0;
        color: #475569;
        font-weight: 600;
    }
    .styled-table td {
        padding: 10px;
        border-bottom: 1px solid #e2e8f0;
    }
    .styled-table tr:last-child td {
        border-bottom: none;
    }
    .styled-table tr.highlighted {
        background-color: #f0f7ff;
    }
    
    /* Hide Streamlit branding */
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Add logo
st.markdown("""
<div class="logo-container">
    <div class="logo-box">C</div>
    <div class="logo-text">CaseLens</div>
</div>
""", unsafe_allow_html=True)

# Define data
folders = [
    {"id": 1, "name": "1. Statement of Appeal", "type": "appellant", "date": "1950-03-15", "description": "Initial appeal filing that establishes the case."},
    {"id": 2, "name": "2. Request for a Stay", "type": "respondent", "date": "1950-04-10", "description": "Request to pause proceedings pending resolution of jurisdictional matters."},
    {"id": 3, "name": "3. Answer to Request for PM", "type": "appellant", "date": "1950-05-22", "description": "Response to the procedural motion filed by respondent."},
    {"id": 4, "name": "4. Answer to PM", "type": "respondent", "date": "1950-06-30", "description": "Further response regarding procedural matters."},
    {"id": 5, "name": "5. Appeal Brief", "type": "appellant", "date": "1970-08-12", "description": "Comprehensive arguments on sporting succession and color continuity."},
    {"id": 6, "name": "6. Brief on Admissibility", "type": "appellant", "date": "1975-01-20", "description": "Arguments addressing the admissibility of evidence and claims."},
    {"id": 7, "name": "7. Reply to Objection to Admissibility", "type": "appellant", "date": "1975-03-05", "description": "Counter-arguments to respondent's objections."},
    {"id": 8, "name": "8. Challenge", "type": "respondent", "date": "1975-04-18", "description": "Challenge to appellant's standing and continuity claims."},
    {"id": 9, "name": "ChatGPT", "type": "system", "date": "", "description": "AI-generated analysis and supporting documentation."},
    {"id": 10, "name": "Jurisprudence", "type": "system", "date": "", "description": "Relevant legal precedents and case law."},
    {"id": 11, "name": "Objection to Admissibility", "type": "respondent", "date": "1975-02-15", "description": "Formal objection to the admissibility of appellant's evidence."},
    {"id": 12, "name": "Swiss Court", "type": "system", "date": "", "description": "Documents related to Swiss Court proceedings."},
]

events = [
    {"id": 1, "date": "1950-present", "event": "Continuous operation under same name since 1950", "party": "Appellant", "status": "Undisputed", "argument": "1. Sporting Succession", "evidence": "C-1", "related_docs": [1, 5]},
    {"id": 2, "date": "1950", "event": "Initial registration in 1950", "party": "Appellant", "status": "Undisputed", "argument": "1.1.1. Registration History", "evidence": "C-2", "related_docs": [1, 6]},
    {"id": 3, "date": "1950-present", "event": "Consistent use of blue and white since founding", "party": "Appellant", "status": "Disputed", "argument": "1.2. Club Colors Analysis", "evidence": "C-4", "related_docs": [1, 5]},
    {"id": 4, "date": "1950-1975", "event": "Pre-1976 colors represented original city district", "party": "Respondent", "status": "Undisputed", "argument": "1.2.1. Color Changes Analysis", "evidence": "R-5", "related_docs": [2, 4, 8]},
    {"id": 5, "date": "1970-1980", "event": "Minor shade variations do not affect continuity", "party": "Appellant", "status": "Undisputed", "argument": "1.2.1. Color Variations Analysis", "evidence": "C-5", "related_docs": [5, 7]},
    {"id": 6, "date": "1975-1976", "event": "Brief administrative gap in 1975-1976", "party": "Appellant", "status": "Disputed", "argument": "1.1.1. Registration History", "evidence": "C-2", "related_docs": [6, 7]},
    {"id": 7, "date": "1976", "event": "New registration under same name", "party": "Appellant", "status": "Undisputed", "argument": "1.1.2. Legal Continuity", "evidence": "C-3", "related_docs": [5, 6]},
    {"id": 8, "date": "1975", "event": "Objection to legitimacy of succession claim", "party": "Respondent", "status": "Disputed", "argument": "2.1. Challenge to Succession", "evidence": "R-3", "related_docs": [8, 11]},
]

# Create two columns layout
col1, col2 = st.columns([1, 3])

# Left column: Document selection with simple radio buttons
with col1:
    st.markdown("<h2>Case Documents</h2>", unsafe_allow_html=True)
    
    # Initialize session state for selected document
    if "selected_doc_id" not in st.session_state:
        st.session_state.selected_doc_id = 1
    
    # Simple radio button selection to avoid duplicate keys
    selected_doc_id = st.radio(
        "Select a document:",
        options=[f["id"] for f in folders],
        format_func=lambda x: next((f["name"] for f in folders if f["id"] == x), "Unknown"),
        index=folders.index(next((f for f in folders if f["id"] == st.session_state.selected_doc_id), folders[0]))
    )
    
    # Update session state
    st.session_state.selected_doc_id = selected_doc_id
    
    # Get selected document
    selected_doc = next((f for f in folders if f["id"] == selected_doc_id), None)
    
    # Display document details
    if selected_doc:
        # Create tag based on document type
        doc_type_tag = ""
        if selected_doc["type"] == "appellant":
            doc_type_tag = "<span class='tag appellant-tag'>Appellant</span>"
        elif selected_doc["type"] == "respondent":
            doc_type_tag = "<span class='tag respondent-tag'>Respondent</span>"
        else:
            doc_type_tag = "<span class='tag'>System</span>"
        
        # Display document card
        st.markdown(f"""
        <div class="card card-{selected_doc['type']}">
            <h3>📁 {selected_doc['name']}</h3>
            <p>{doc_type_tag} {f"Filed: {selected_doc['date']}" if selected_doc['date'] else ""}</p>
            <p>{selected_doc['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show connected events
        related_events = [e for e in events if selected_doc_id in e["related_docs"]]
        
        if related_events:
            st.markdown("<h4>Connected Events:</h4>", unsafe_allow_html=True)
            
            for event in related_events:
                # Create tag based on event status
                status_tag = f"<span class='tag {'disputed-tag' if event['status'] == 'Disputed' else 'undisputed-tag'}'>{event['status']}</span>"
                
                st.markdown(f"""
                <div class="connection-line">
                    <p><strong>{event['date']}</strong>: {event['event']}</p>
                    <p>{status_tag} <span class='evidence-chip'>{event['evidence']}</span></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No events connected to this document.")

# Right column: Timeline with tabbed interface
with col2:
    # Header with controls
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <h2>Summary of arguments</h2>
        <div>
            <button class="custom-button" style="margin-right: 8px; background-color: white; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 4px;">Copy</button>
            <button class="custom-button" style="background-color: white; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 4px;">Export</button>
        </div>
    </div>
    <h3>Case Facts</h3>
    """, unsafe_allow_html=True)
    
    # Create tabs
    tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
    
    # Prepare event data for each tab
    all_events = events
    disputed_events = [e for e in events if e["status"] == "Disputed"]
    undisputed_events = [e for e in events if e["status"] == "Undisputed"]
    
    # Create a function to display events in a table format
    def display_events_table(events_list):
        # Table header
        st.markdown("""
        <table class="styled-table">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Event</th>
                    <th>Party</th>
                    <th>Status</th>
                    <th>Related Argument</th>
                    <th>Evidence</th>
                </tr>
            </thead>
            <tbody>
        """, unsafe_allow_html=True)
        
        # Table rows
        for event in events_list:
            # Check if connected to selected document
            is_connected = selected_doc_id in event["related_docs"]
            row_class = "highlighted" if is_connected else ""
            
            # Party tag
            party_tag = f"<span class='tag {'appellant-tag' if event['party'] == 'Appellant' else 'respondent-tag'}'>{event['party']}</span>"
            
            # Status tag
            status_tag = f"<span class='tag {'disputed-tag' if event['status'] == 'Disputed' else 'undisputed-tag'}'>{event['status']}</span>"
            
            # Create table row
            st.markdown(f"""
            <tr class="{row_class}">
                <td>{event['date']}</td>
                <td>{event['event']}{' <div class="connection-line" style="margin-top: 5px;">Connected to: ' + selected_doc['name'] + '</div>' if is_connected else ''}</td>
                <td>{party_tag}</td>
                <td>{status_tag}</td>
                <td>{event['argument']}</td>
                <td><span class="evidence-chip">{event['evidence']}</span></td>
            </tr>
            """, unsafe_allow_html=True)
        
        # Close table
        st.markdown("</tbody></table>", unsafe_allow_html=True)
    
    # Display events in each tab
    with tabs[0]:
        display_events_table(all_events)
    
    with tabs[1]:
        if disputed_events:
            display_events_table(disputed_events)
        else:
            st.info("No disputed facts found.")
    
    with tabs[2]:
        if undisputed_events:
            display_events_table(undisputed_events)
        else:
            st.info("No undisputed facts found.")
    
    # Add a simple timeline visualization toggle
    if st.checkbox("Show Timeline Visualization"):
        st.markdown("<h3>Case Timeline</h3>", unsafe_allow_html=True)
        
        # Sort events chronologically
        sorted_events = sorted(events, key=lambda x: x['date'].split('-')[0])
        
        # Group events by decade
        by_decade = {}
        for event in sorted_events:
            year = event['date'].split('-')[0]
            if year.isdigit():
                decade = f"{int(year) // 10 * 10}s"
                if decade not in by_decade:
                    by_decade[decade] = []
                by_decade[decade].append(event)
        
        # Display timeline by decade
        for decade, decade_events in by_decade.items():
            st.markdown(f"<h4>{decade}</h4>", unsafe_allow_html=True)
            
            for event in decade_events:
                # Check if connected to selected document
                is_connected = selected_doc_id in event["related_docs"]
                
                # Party color
                party_color = "#3b82f6" if event["party"] == "Appellant" else "#ef4444"
                
                # Create timeline event
                st.markdown(f"""
                <div style="margin-left: 20px; margin-bottom: 15px; position: relative; padding-left: 20px; 
                     border-left: 2px solid {party_color};
                     {'background-color: #f0f7ff; padding: 10px; border-radius: 4px;' if is_connected else ''}">
                    <div style="position: absolute; left: -10px; top: 0; width: 16px; height: 16px; border-radius: 50%; 
                         background-color: {party_color}; border: 3px solid white;"></div>
                    <p><strong>{event['date']}</strong>: {event['event']}</p>
                    <p>
                        <span class="tag {'appellant-tag' if event['party'] == 'Appellant' else 'respondent-tag'}">{event['party']}</span>
                        <span class="tag {'disputed-tag' if event['status'] == 'Disputed' else 'undisputed-tag'}">{event['status']}</span>
                        <span class="evidence-chip">{event['evidence']}</span>
                    </p>
                    {f'<div class="connection-line">Connected to: {selected_doc["name"]}</div>' if is_connected else ''}
                </div>
                """, unsafe_allow_html=True)

# Add footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 0.8rem;">
    CaseLens - Legal Document Timeline Visualization
</div>
""", unsafe_allow_html=True)
