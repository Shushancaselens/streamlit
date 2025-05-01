import streamlit as st
import pandas as pd
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="CaseLens", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f9f9fb;
    }
    .css-1d391kg {
        background-color: #f9f9fb;
    }
    .doc-folder {
        background-color: white;
        border-radius: 4px;
        padding: 10px;
        margin: 5px 0;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .doc-folder:hover {
        background-color: #f0f0f5;
    }
    .folder-icon {
        color: #4c72b0;
        margin-right: 5px;
    }
    .sidebar-content {
        padding: 10px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 16px;
        background-color: #f0f0f5;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4c72b0 !important;
        color: white !important;
    }
    .timeline-event {
        padding: 10px;
        border-radius: 4px;
        margin: 5px 0;
    }
    .appellant {
        border-left: 4px solid #4c72b0;
    }
    .respondent {
        border-left: 4px solid #e15759;
    }
    .evidence-tag {
        background-color: #f0f0f5;
        border-radius: 12px;
        padding: 2px 8px;
        font-size: 12px;
        color: #666;
    }
    .status-tag {
        border-radius: 12px;
        padding: 2px 8px;
        font-size: 12px;
        color: white;
    }
    .disputed {
        background-color: #e15759;
    }
    .undisputed {
        background-color: #55a868;
    }
    .timeline-container {
        position: relative;
        margin: 20px 0;
        padding-left: 50px;
    }
    .timeline-line {
        position: absolute;
        left: 15px;
        top: 0;
        bottom: 0;
        width: 2px;
        background-color: #ccc;
    }
    .timeline-marker {
        position: absolute;
        left: 0;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        text-align: center;
        line-height: 30px;
        color: white;
        font-weight: bold;
    }
    .timeline-marker.appellant {
        background-color: #4c72b0;
        border: 2px solid white;
    }
    .timeline-marker.respondent {
        background-color: #e15759;
        border: 2px solid white;
    }
    .timeline-content {
        position: relative;
        margin-left: 15px;
        padding: 10px;
        background-color: white;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .timeline-date {
        position: absolute;
        left: -85px;
        width: 70px;
        text-align: right;
        font-size: 12px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Create sidebar with logo and navigation
with st.sidebar:
    st.image("https://placehold.co/200x50?text=CaseLens", width=150)
    st.markdown("## Legal Analysis")
    
    # Create sidebar navigation
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    
    # Mimic folder structure from second screenshot
    folders = [
        "📄 Arguments",
        "📊 Facts",
        "📂 Exhibits"
    ]
    selected_section = st.radio("", folders, index=1, label_visibility="collapsed")
    
    # Document folders
    st.markdown("### Case Documents")
    doc_folders = [
        "1. Statement of Appeal",
        "2. Request for a Stay",
        "3. Answer to Request for PM",
        "4. Answer to PM",
        "5. Appeal Brief",
        "6. Brief on Admissibility",
        "7. Reply to Objection to Admissibility",
        "8. Challenge",
        "ChatGPT",
        "Jurisprudence",
        "Objection to Admissibility",
        "Swiss Court"
    ]
    
    for folder in doc_folders:
        st.markdown(f"""
        <div class="doc-folder">
            <span class="folder-icon">📁</span> {folder}
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Main content area
st.title("Summary of arguments")

# Create case facts section with tabs
st.header("Case Facts")

tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])

# Create case facts data
case_facts = [
    {
        "date": "1950-present", 
        "event": "Continuous operation under same name since 1950", 
        "party": "Appellant", 
        "status": "Undisputed",
        "argument": "1. Sporting Succession",
        "evidence": "C-1",
        "related_documents": ["1. Statement of Appeal", "5. Appeal Brief"]
    },
    {
        "date": "1950", 
        "event": "Initial registration in 1950", 
        "party": "Appellant", 
        "status": "Undisputed",
        "argument": "1.1.1. Registration History",
        "evidence": "C-2",
        "related_documents": ["1. Statement of Appeal"]
    },
    {
        "date": "1950-present", 
        "event": "Consistent use of blue and white since founding", 
        "party": "Appellant", 
        "status": "Disputed",
        "argument": "1.2. Club Colors Analysis",
        "evidence": "C-4",
        "related_documents": ["5. Appeal Brief", "8. Challenge"]
    },
    {
        "date": "1950-1975", 
        "event": "Pre-1976 colors represented original city district", 
        "party": "Respondent", 
        "status": "Undisputed",
        "argument": "1.2.1. Color Changes Analysis",
        "evidence": "R-5",
        "related_documents": ["2. Request for a Stay", "4. Answer to PM"]
    },
    {
        "date": "1970-1980", 
        "event": "Minor shade variations do not affect continuity", 
        "party": "Appellant", 
        "status": "Undisputed",
        "argument": "1.2.1. Color Variations Analysis",
        "evidence": "C-5",
        "related_documents": ["5. Appeal Brief"]
    },
    {
        "date": "1975-1976", 
        "event": "Brief administrative gap in 1975-1976", 
        "party": "Appellant", 
        "status": "Disputed",
        "argument": "1.1.1. Registration History",
        "evidence": "C-2",
        "related_documents": ["1. Statement of Appeal", "6. Brief on Admissibility"]
    },
    {
        "date": "1975-1976", 
        "event": "Operations ceased between 1975-1976", 
        "party": "Respondent", 
        "status": "Disputed",
        "argument": "1. Sporting Succession",
        "evidence": "R-1",
        "related_documents": ["2. Request for a Stay", "Objection to Admissibility"]
    }
]

# Convert to dataframe for easier manipulation
df = pd.DataFrame(case_facts)

# Create a custom timeline using pure Streamlit components
def create_timeline(facts):
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)
    
    # Sort facts by date
    def get_start_year(date_str):
        if '-' in date_str:
            return int(date_str.split('-')[0])
        return int(date_str)
    
    sorted_facts = sorted(facts, key=lambda x: get_start_year(x['date']))
    
    for i, fact in enumerate(sorted_facts):
        party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
        status_class = "disputed" if fact["status"] == "Disputed" else "undisputed"
        
        top_pos = i * 150  # Adjust vertical spacing
        
        # Create marker and content
        st.markdown(f"""
        <div class="timeline-marker {party_class}" style="top: {top_pos}px;">{i+1}</div>
        <div class="timeline-content" style="margin-top: {30 if i > 0 else 0}px;">
            <div class="timeline-date">{fact['date']}</div>
            <h4>{fact['event']}</h4>
            <p>
                <strong>Party:</strong> <span style="color: {'#4c72b0' if fact['party'] == 'Appellant' else '#e15759'};">{fact['party']}</span><br>
                <strong>Status:</strong> <span class="status-tag {status_class}">{fact['status']}</span><br>
                <strong>Argument:</strong> {fact['argument']}<br>
                <strong>Evidence:</strong> <span class="evidence-tag">{fact['evidence']}</span>
            </p>
            <details>
                <summary>Related Documents</summary>
                <ul>
                    {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                </ul>
            </details>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add spacing at the end
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# Display different content based on the active tab
with tabs[0]:  # All Facts
    st.subheader("Timeline View")
    create_timeline(case_facts)
    
    st.subheader("Table View")
    # Display facts table with columns
    cols = st.columns([1, 2, 1, 1, 2, 1])
    cols[0].markdown("**Date**")
    cols[1].markdown("**Event**")
    cols[2].markdown("**Party**")
    cols[3].markdown("**Status**")
    cols[4].markdown("**Related Argument**")
    cols[5].markdown("**Evidence**")
    
    # Display rows with styling based on party and status
    for i, fact in enumerate(case_facts):
        cols = st.columns([1, 2, 1, 1, 2, 1])
        
        # Determine party style
        party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
        
        # Create expandable container for each fact
        with st.expander(f"Event {i+1}: {fact['event']}", expanded=False):
            st.markdown(f"""
            <div class="timeline-event {party_class}">
                <p><strong>Event:</strong> {fact['event']}</p>
                <p><strong>Date:</strong> {fact['date']}</p>
                <p><strong>Party:</strong> {fact['party']}</p>
                <p><strong>Status:</strong> {fact['status']}</p>
                <p><strong>Related Argument:</strong> {fact['argument']}</p>
                <p><strong>Evidence:</strong> {fact['evidence']}</p>
                <p><strong>Related Documents:</strong></p>
                <ul>
                    {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Display basic info in the table
        cols[0].write(fact["date"])
        cols[1].write(fact["event"])
        
        # Style the party column
        party_style = "color: #4c72b0; font-weight: bold;" if fact["party"] == "Appellant" else "color: #e15759; font-weight: bold;"
        cols[2].markdown(f"<span style='{party_style}'>{fact['party']}</span>", unsafe_allow_html=True)
        
        # Style the status column
        status_class = "disputed" if fact["status"] == "Disputed" else "undisputed"
        cols[3].markdown(f"<span class='status-tag {status_class}'>{fact['status']}</span>", unsafe_allow_html=True)
        
        cols[4].write(fact["argument"])
        cols[5].markdown(f"<span class='evidence-tag'>{fact['evidence']}</span>", unsafe_allow_html=True)

with tabs[1]:  # Disputed Facts
    disputed_facts = [fact for fact in case_facts if fact["status"] == "Disputed"]
    
    if disputed_facts:
        st.subheader("Timeline of Disputed Facts")
        create_timeline(disputed_facts)
        
        st.subheader("Details")
        for i, fact in enumerate(disputed_facts):
            party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
            
            with st.expander(f"{fact['event']}", expanded=True):
                st.markdown(f"""
                <div class="timeline-event {party_class}">
                    <p><strong>Event:</strong> {fact['event']}</p>
                    <p><strong>Date:</strong> {fact['date']}</p>
                    <p><strong>Party:</strong> {fact['party']}</p>
                    <p><strong>Related Argument:</strong> {fact['argument']}</p>
                    <p><strong>Evidence:</strong> {fact['evidence']}</p>
                    <p><strong>Related Documents:</strong></p>
                    <ul>
                        {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                # Show related document connections
                if i < len(disputed_facts) - 1:
                    opposing_facts = [f for f in disputed_facts if f['argument'] == fact['argument'] and f['party'] != fact['party']]
                    if opposing_facts:
                        st.markdown("#### Conflicting Claims")
                        for opp in opposing_facts:
                            st.markdown(f"""
                            <div class="timeline-event {"appellant" if opp["party"] == "Appellant" else "respondent"}">
                                <p><strong>{opp['party']} claims:</strong> {opp['event']}</p>
                                <p><strong>Evidence:</strong> {opp['evidence']}</p>
                            </div>
                            """, unsafe_allow_html=True)
    else:
        st.info("No disputed facts found.")

with tabs[2]:  # Undisputed Facts
    undisputed_facts = [fact for fact in case_facts if fact["status"] == "Undisputed"]
    
    if undisputed_facts:
        st.subheader("Timeline of Undisputed Facts")
        create_timeline(undisputed_facts)
        
        st.subheader("Details")
        for fact in undisputed_facts:
            party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
            
            with st.expander(f"{fact['event']}", expanded=True):
                st.markdown(f"""
                <div class="timeline-event {party_class}">
                    <p><strong>Event:</strong> {fact['event']}</p>
                    <p><strong>Date:</strong> {fact['date']}</p>
                    <p><strong>Party:</strong> {fact['party']}</p>
                    <p><strong>Related Argument:</strong> {fact['argument']}</p>
                    <p><strong>Evidence:</strong> {fact['evidence']}</p>
                    <p><strong>Related Documents:</strong></p>
                    <ul>
                        {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No undisputed facts found.")

# Add a document-centric view
st.header("Documents and Related Events")

# Group facts by related documents
doc_to_facts = {}
for fact in case_facts:
    for doc in fact['related_documents']:
        if doc not in doc_to_facts:
            doc_to_facts[doc] = []
        doc_to_facts[doc].append(fact)

# Create tabs for each document type
doc_tabs = st.tabs(list(doc_to_facts.keys()))

# Fill each tab with related events
for i, (doc, facts) in enumerate(doc_to_facts.items()):
    with doc_tabs[i]:
        st.subheader(f"Events Referenced in {doc}")
        
        # Create a mini-timeline for this document
        events_df = pd.DataFrame(facts)
        
        # Group events by argument
        arguments = events_df['argument'].unique()
        for arg in arguments:
            arg_events = events_df[events_df['argument'] == arg]
            
            st.markdown(f"### {arg}")
            
            for _, event in arg_events.iterrows():
                party_class = "appellant" if event["party"] == "Appellant" else "respondent"
                status_class = "disputed" if event["status"] == "Disputed" else "undisputed"
                
                st.markdown(f"""
                <div class="timeline-event {party_class}">
                    <p><strong>Event:</strong> {event['event']}</p>
                    <p><strong>Date:</strong> {event['date']}</p>
                    <p><strong>Party:</strong> {event['party']}</p>
                    <p><strong>Status:</strong> <span class="status-tag {status_class}">{event['status']}</span></p>
                    <p><strong>Evidence:</strong> <span class="evidence-tag">{event['evidence']}</span></p>
                </div>
                """, unsafe_allow_html=True)
        
        # Visual representation of document connection to case events
        st.subheader("Document Timeline")
        st.markdown("<div style='position: relative; padding: 20px 0;'>", unsafe_allow_html=True)
        
        # Sort facts by date for timeline
        sorted_doc_facts = sorted(facts, key=lambda x: x['date'].split('-')[0])
        
        # Create a simple horizontal timeline
        timeline_html = """
        <div style="display: flex; margin-top: 30px; margin-bottom: 60px; position: relative;">
            <div style="position: absolute; top: 15px; left: 0; right: 0; height: 2px; background-color: #ddd;"></div>
        """
        
        # Add markers for each year mentioned
        years = set()
        for fact in sorted_doc_facts:
            date_parts = fact['date'].split('-')
            years.add(date_parts[0])
            if len(date_parts) > 1 and date_parts[1] != "present":
                years.add(date_parts[1])
        
        years = sorted(list(years))
        year_positions = {}
        width = 100 / (len(years) - 1) if len(years) > 1 else 100
        
        for i, year in enumerate(years):
            position = i * width if len(years) > 1 else 50
            year_positions[year] = position
            timeline_html += f"""
            <div style="position: absolute; top: 25px; left: {position}%; transform: translateX(-50%);">
                <div style="width: 10px; height: 10px; background-color: #666; border-radius: 50%; margin: 0 auto;"></div>
                <div style="text-align: center; margin-top: 5px; font-size: 12px;">{year}</div>
            </div>
            """
        
        # Add document connection points
        for i, fact in enumerate(sorted_doc_facts):
            start_year = fact['date'].split('-')[0]
            position = year_positions[start_year]
            color = "#4c72b0" if fact["party"] == "Appellant" else "#e15759"
            
            timeline_html += f"""
            <div style="position: absolute; top: -20px; left: {position}%; transform: translateX(-50%);">
                <div style="width: 14px; height: 14px; background-color: {color}; border-radius: 50%; 
                     border: 2px solid #fff; box-shadow: 0 1px 3px rgba(0,0,0,0.2);"></div>
                <div style="position: absolute; top: -25px; left: 50%; transform: translateX(-50%); 
                     background-color: white; border: 1px solid #ddd; border-radius: 4px; padding: 2px 6px; 
                     font-size: 11px; white-space: nowrap; display: none;">
                    {fact['event']}
                </div>
            </div>
            """
        
        timeline_html += "</div>"
        st.markdown(timeline_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Connection explorer view
st.header("Document-Event Connection Explorer")

selected_document = st.selectbox("Select Document", list(doc_to_facts.keys()))
selected_event = None

if selected_document:
    facts = doc_to_facts[selected_document]
    event_options = [fact['event'] for fact in facts]
    selected_event = st.selectbox("Select Event", event_options)

if selected_event:
    selected_fact = next((fact for fact in case_facts if fact['event'] == selected_event), None)
    if selected_fact:
        # Create visualization for the connection
        st.subheader("Connection Details")
        
        # Create columns for document and event
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div style="background-color: white; padding: 15px; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <h4>📁 {selected_document}</h4>
                <p><strong>Document Type:</strong> {selected_document.split('.')[0]}</p>
                <p><strong>Filed By:</strong> {"Appellant" if "Appeal" in selected_document or "Reply" in selected_document else "Respondent"}</p>
                <p><strong>Referenced Arguments:</strong></p>
                <ul>
                    {"".join([f"<li>{fact['argument']}</li>" for fact in doc_to_facts[selected_document]])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            party_class = "appellant" if selected_fact["party"] == "Appellant" else "respondent"
            status_class = "disputed" if selected_fact["status"] == "Disputed" else "undisputed"
            
            st.markdown(f"""
            <div class="timeline-event {party_class}">
                <h4>{selected_fact['event']}</h4>
                <p><strong>Date:</strong> {selected_fact['date']}</p>
                <p><strong>Party:</strong> {selected_fact['party']}</p>
                <p><strong>Status:</strong> <span class="status-tag {status_class}">{selected_fact['status']}</span></p>
                <p><strong>Related Argument:</strong> {selected_fact['argument']}</p>
                <p><strong>Evidence:</strong> <span class="evidence-tag">{selected_fact['evidence']}</span></p>
            </div>
            """, unsafe_allow_html=True)
        
        # Show connection visualization
        st.markdown("""
        <div style="margin: 30px 0; text-align: center;">
            <div style="display: inline-block; width: 100px; height: 100px; border-radius: 50%; background-color: #f0f0f5; 
                  text-align: center; line-height: 100px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                📁
            </div>
            <div style="display: inline-block; width: 100px; height: 2px; background-color: #333; margin: 0 15px; vertical-align: middle;"></div>
            <div style="display: inline-block; width: 100px; height: 100px; border-radius: 50%; background-color: #f0f0f5; 
                  text-align: center; line-height: 100px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                📅
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Show other documents referencing the same event
        other_docs = [doc for doc in selected_fact['related_documents'] if doc != selected_document]
        if other_docs:
            st.markdown("### Other Documents Referencing This Event")
            st.markdown("<ul>", unsafe_allow_html=True)
            for doc in other_docs:
                st.markdown(f"<li>{doc}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)

# Add footer with action buttons
col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    st.button("Copy")
with col2:
    st.button("Export")
