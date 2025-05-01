import streamlit as st
import pandas as pd
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="CaseLens - Document Timeline", layout="wide")

# Add custom CSS for enhanced styling
st.markdown("""
<style>
    /* Main container styling */
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
    
    /* Document folder styling */
    .folder-container {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .folder-item {
        padding: 12px 16px;
        border-bottom: 1px solid #e2e8f0;
        cursor: pointer;
        display: flex;
        align-items: center;
        transition: background-color 0.2s;
    }
    .folder-item:last-child {
        border-bottom: none;
    }
    .folder-item:hover {
        background-color: #f8fafc;
    }
    .folder-item.selected {
        background-color: #ebf5ff;
        border-left: 3px solid #3b82f6;
    }
    .folder-icon {
        margin-right: 12px;
        color: #64748b;
        font-size: 1.1rem;
    }
    .folder-appellant .folder-icon {
        color: #3b82f6;
    }
    .folder-respondent .folder-icon {
        color: #ef4444;
    }
    .folder-system .folder-icon {
        color: #9ca3af;
    }
    
    /* Party and status tags */
    .tag {
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 500;
        display: inline-block;
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
    
    /* Timeline event styling */
    .event-card {
        padding: 16px;
        border-radius: 6px;
        margin-bottom: 12px;
        border: 1px solid #e2e8f0;
        transition: all 0.2s;
    }
    .event-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .event-card.connected {
        background-color: #f0f7ff;
        border-color: #bfdbfe;
    }
    .event-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }
    .event-title {
        font-weight: 600;
        font-size: 1.1rem;
        color: #1e293b;
        margin: 6px 0;
    }
    .event-connection {
        margin-top: 8px;
        padding-top: 8px;
        border-top: 1px dashed #cbd5e1;
    }
    
    /* Tab styling */
    .custom-tabs {
        display: flex;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 1.5rem;
    }
    .custom-tab {
        padding: 0.5rem 1rem;
        cursor: pointer;
        border-bottom: 2px solid transparent;
        font-weight: 500;
        color: #64748b;
    }
    .custom-tab.active {
        color: #3b82f6;
        border-bottom: 2px solid #3b82f6;
    }
    
    /* Summary box */
    .summary-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 16px;
        margin-bottom: 1.5rem;
    }
    .summary-title {
        font-weight: 600;
        margin-bottom: 8px;
        color: #334155;
        font-size: 1.1rem;
    }
    
    /* Connection line */
    .connection-line {
        border-left: 2px dashed #bfdbfe;
        padding-left: 12px;
        margin: 8px 0 8px 8px;
        color: #3b82f6;
    }
    
    /* Button styling */
    .custom-button {
        background-color: white;
        border: 1px solid #e2e8f0;
        padding: 6px 12px;
        border-radius: 4px;
        font-size: 0.9rem;
        color: #334155;
        cursor: pointer;
    }
    .custom-button:hover {
        background-color: #f8fafc;
    }
    
    /* Hide Streamlit branding */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Make the layout more compact */
    .row-widget.stRadio > div {
        flex-direction: column;
    }
    .row-widget.stRadio > div > label {
        margin: 0;
        padding: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Add CaseLens logo and header
st.markdown("""
<div class="logo-container">
    <div class="logo-box">C</div>
    <div class="logo-text">CaseLens</div>
</div>
""", unsafe_allow_html=True)

# Define data with more comprehensive relationships
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

# Create two columns layout with adjusted ratio
col1, col2 = st.columns([1, 3])

# Left column: Documents with improved folder display
with col1:
    st.markdown("<h2>Case Documents</h2>", unsafe_allow_html=True)
    
    # Create a container for document types
    appellant_docs = [f for f in folders if f["type"] == "appellant"]
    respondent_docs = [f for f in folders if f["type"] == "respondent"]
    system_docs = [f for f in folders if f["type"] == "system"]
    
    # Introduce tabs for document categories
    doc_tabs = st.tabs(["All Docs", "Appellant", "Respondent", "System"])
    
    # Helper function to render folder items
    def render_folders(folder_list, selected_id):
        for folder in folder_list:
            selected_class = "selected" if folder["id"] == selected_id else ""
            type_class = f"folder-{folder['type']}"
            st.markdown(f"""
            <div class="folder-item {selected_class} {type_class}" id="folder-{folder['id']}">
                <span class="folder-icon">📁</span>
                <span>{folder['name']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Use a button with the same key as the div for selection
            if st.button(f"Select {folder['name']}", key=f"select_btn_{folder['id']}", help=folder["description"]):
                st.session_state.selected_doc_id = folder["id"]
                
    # Initialize session state
    if "selected_doc_id" not in st.session_state:
        st.session_state.selected_doc_id = 1
    
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "All Facts"
    
    # Fill the tabs
    with doc_tabs[0]:  # All Docs
        render_folders(folders, st.session_state.selected_doc_id)
    
    with doc_tabs[1]:  # Appellant
        render_folders(appellant_docs, st.session_state.selected_doc_id)
    
    with doc_tabs[2]:  # Respondent
        render_folders(respondent_docs, st.session_state.selected_doc_id)
    
    with doc_tabs[3]:  # System
        render_folders(system_docs, st.session_state.selected_doc_id)
    
    # Display detailed info for selected document
    selected_doc = next((folder for folder in folders if folder["id"] == st.session_state.selected_doc_id), None)
    
    if selected_doc:
        st.markdown("<div class='summary-box'>", unsafe_allow_html=True)
        
        # Get party type tag
        party_tag = ""
        if selected_doc["type"] == "appellant":
            party_tag = "<span class='tag appellant-tag'>Appellant</span>"
        elif selected_doc["type"] == "respondent":
            party_tag = "<span class='tag respondent-tag'>Respondent</span>"
        else:
            party_tag = "<span class='tag'>System</span>"
        
        # Document header
        st.markdown(f"""
        <h3 class='summary-title'>Selected Document</h3>
        <p><strong>{selected_doc['name']}</strong></p>
        <div style='margin: 8px 0;'>
            {party_tag}
            {f"<span style='margin-left: 8px;'>Filed: {selected_doc['date']}</span>" if selected_doc['date'] else ""}
        </div>
        <p>{selected_doc['description']}</p>
        """, unsafe_allow_html=True)
        
        # Find related events
        related_events = [e for e in events if selected_doc["id"] in e["related_docs"]]
        
        if related_events:
            st.markdown(f"<p><strong>Connected to {len(related_events)} events:</strong></p>", unsafe_allow_html=True)
            
            for event in related_events:
                status_class = "disputed-tag" if event["status"] == "Disputed" else "undisputed-tag"
                
                st.markdown(f"""
                <div class='connection-line'>
                    <strong>{event['date']}</strong>: {event['event']}
                    <div style='margin-top: 4px;'>
                        <span class='tag {status_class}'>{event['status']}</span>
                        <span style='margin-left: 8px;' class='evidence-chip'>{event['evidence']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("<p>No events directly connected to this document.</p>", unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)

# Right column: Timeline with improved visualization
with col2:
    # Header with controls
    st.markdown("""
    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
        <h2>Summary of arguments</h2>
        <div>
            <button class='custom-button' style='margin-right: 8px;'>Copy</button>
            <button class='custom-button'>Export</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a header for the case facts section
    st.markdown("<h3>Case Facts</h3>", unsafe_allow_html=True)
    
    # Create custom tabs
    st.markdown("""
    <div class='custom-tabs'>
        <div class='custom-tab active' id='tab-all'>All Facts</div>
        <div class='custom-tab' id='tab-disputed'>Disputed Facts</div>
        <div class='custom-tab' id='tab-undisputed'>Undisputed Facts</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tab selector
    tab_options = ["All Facts", "Disputed Facts", "Undisputed Facts"]
    active_tab = st.radio("Select tab:", tab_options, horizontal=True, label_visibility="collapsed")
    st.session_state.active_tab = active_tab
    
    # Filter events based on active tab
    filtered_events = events
    if active_tab == "Disputed Facts":
        filtered_events = [e for e in events if e["status"] == "Disputed"]
    elif active_tab == "Undisputed Facts":
        filtered_events = [e for e in events if e["status"] == "Undisputed"]
    
    # Sort events chronologically
    filtered_events = sorted(filtered_events, key=lambda x: x["date"].split("-")[0])
    
    # Display events with enhanced styling
    if filtered_events:
        for event in filtered_events:
            # Check connection to selected document
            is_connected = selected_doc and event["id"] in [e["id"] for e in events if selected_doc["id"] in e["related_docs"]]
            
            # Party tag
            if event["party"] == "Appellant":
                party_tag = f"<span class='tag appellant-tag'>{event['party']}</span>"
            else:
                party_tag = f"<span class='tag respondent-tag'>{event['party']}</span>"
            
            # Status tag
            status_tag = f"<span class='tag {'disputed-tag' if event['status'] == 'Disputed' else 'undisputed-tag'}'>{event['status']}</span>"
            
            # Create the event card with improved styling
            st.markdown(f"""
            <div class='event-card {("connected" if is_connected else "")}'>
                <div class='event-header'>
                    <strong>{event['date']}</strong>
                    <div>
                        {party_tag}
                        {status_tag}
                    </div>
                </div>
                <h4 class='event-title'>{event['event']}</h4>
                <div style='display: flex; justify-content: space-between; margin-top: 12px;'>
                    <span>{event['argument']}</span>
                    <span class='evidence-chip'>{event['evidence']}</span>
                </div>
                {f'''
                <div class='event-connection'>
                    <strong>Connected to:</strong> {selected_doc["name"]}
                    <span style='margin-left: 8px; font-size: 0.8rem;'>({selected_doc["date"] if selected_doc["date"] else "No date"})</span>
                </div>
                ''' if is_connected else ''}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info(f"No {active_tab.lower()} available.")
    
    # Timeline visualization with interactive toggle
    show_timeline = st.checkbox("Show Timeline Visualization", value=False)
    
    if show_timeline:
        st.markdown("<h3>Case Timeline</h3>", unsafe_allow_html=True)
        
        # Create simple timeline visualization
        timeline_data = {}
        
        # Group events by decade for timeline visualization
        for event in events:
            # Extract start year
            start_year = event["date"].split("-")[0]
            if start_year.isdigit():
                decade = int(start_year) // 10 * 10
                if decade not in timeline_data:
                    timeline_data[decade] = []
                timeline_data[decade].append(event)
        
        # Sort decades
        sorted_decades = sorted(timeline_data.keys())
        
        # Create timeline visualization
        for decade in sorted_decades:
            decade_events = timeline_data[decade]
            
            # Create decade header
            st.markdown(f"""
            <div style='margin-top: 20px; margin-bottom: 10px;'>
                <h4 style='color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 5px;'>{decade}s</h4>
            </div>
            """, unsafe_allow_html=True)
            
            # Create timeline entries for this decade
            for event in decade_events:
                # Check connection to selected document
                is_connected = selected_doc and event["id"] in [e["id"] for e in events if selected_doc["id"] in e["related_docs"]]
                
                # Get document connections
                connected_docs = [f for f in folders if f["id"] in event["related_docs"]]
                connected_docs_html = ""
                
                if connected_docs:
                    docs_list = ", ".join([f"<span class='{doc['type']}-tag' style='padding: 1px 4px;'>{doc['name']}</span>" for doc in connected_docs])
                    connected_docs_html = f"<div style='margin-top: 5px;'>Connected to: {docs_list}</div>"
                
                # Create timeline entry
                st.markdown(f"""
                <div style='margin-left: 20px; margin-bottom: 15px; position: relative; padding-left: 20px; 
                     border-left: 2px solid {('#3b82f6' if event['party'] == 'Appellant' else '#ef4444')};
                     {"background-color: #f0f7ff; padding: 10px; border-radius: 4px;" if is_connected else ""}'>
                    <div style='position: absolute; left: -10px; top: 0; width: 18px; height: 18px; border-radius: 50%; 
                         background-color: {('#3b82f6' if event['party'] == 'Appellant' else '#ef4444')}; 
                         border: 3px solid white;'></div>
                    <p><strong>{event['date']}</strong>: {event['event']}</p>
                    <div style='display: flex; gap: 10px; margin-top: 5px;'>
                        <span class='tag {('appellant-tag' if event['party'] == 'Appellant' else 'respondent-tag')}'>{event['party']}</span>
                        <span class='tag {('disputed-tag' if event['status'] == 'Disputed' else 'undisputed-tag')}'>{event['status']}</span>
                        <span class='evidence-chip'>{event['evidence']}</span>
                    </div>
                    {connected_docs_html}
                </div>
                """, unsafe_allow_html=True)

# Add a search feature at the top of the page (below header)
st.sidebar.markdown("<h3>Search Case Documents</h3>", unsafe_allow_html=True)
search_term = st.sidebar.text_input("Search by keyword:")

if search_term:
    st.sidebar.markdown("<h4>Search Results:</h4>", unsafe_allow_html=True)
    
    # Search in documents
    doc_results = []
    for folder in folders:
        if search_term.lower() in folder["name"].lower() or search_term.lower() in folder.get("description", "").lower():
            doc_results.append(folder)
    
    # Search in events
    event_results = []
    for event in events:
        if search_term.lower() in event["event"].lower() or search_term.lower() in event["argument"].lower():
            event_results.append(event)
    
    # Display results
    if doc_results:
        st.sidebar.markdown("<p><strong>Documents:</strong></p>", unsafe_allow_html=True)
        for doc in doc_results:
            if st.sidebar.button(f"📁 {doc['name']}", key=f"search_doc_{doc['id']}"):
                st.session_state.selected_doc_id = doc["id"]
    
    if event_results:
        st.sidebar.markdown("<p><strong>Events:</strong></p>", unsafe_allow_html=True)
        for event in event_results:
            if st.sidebar.button(f"📅 {event['event'][:30]}...", key=f"search_event_{event['id']}"):
                # Find documents related to this event
                related_docs = [doc for doc in folders if doc["id"] in event["related_docs"]]
                if related_docs:
                    st.session_state.selected_doc_id = related_docs[0]["id"]
    
    if not doc_results and not event_results:
        st.sidebar.info("No results found.")

# Add a footer
st.markdown("---")
st.markdown("""
<div style="display: flex; justify-content: space-between; color: #64748b; font-size: 0.8rem;">
    <div>CaseLens Legal Document Analyzer</div>
    <div>© 2025 CaseLens</div>
</div>
""", unsafe_allow_html=True)

# Add JavaScript for more interactivity (in real application)
st.markdown("""
<script>
// This is a placeholder for real JavaScript functionality
// In an actual application, we would use this for more dynamic interactions
</script>
""", unsafe_allow_html=True)
