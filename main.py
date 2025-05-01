# Add the Connection Explorer with improved styling
st.header("Document-Event Connection Explorer")

# Add a description
st.markdown("""
<div style="background-color: white; padding: 15px; border-radius: 6px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
    <p>Use this explorer to investigate connections between specific documents and events. 
    Select a document to see all events it references, then select a specific event to examine in detail.</p>
</div>
""", unsafe_allow_html=True)

# Create a styled selectbox for documents
selected_document = st.selectbox(
    "Select Document", 
    list(doc_to_facts.keys()),
    format_func=lambda x: f"📁 {x}"
)

selected_event = None

if selected_document:
    # Get facts for the selected document
    facts = doc_to_facts[selected_document]
    
    # Create columns for document info and event selection
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Display document information in a card
        document_type = "Appellant Filing" if any(x in selected_document for x in ["Appeal", "Statement", "Reply"]) else "Respondent Filing"
        document_icon = "📝" if "Brief" in selected_document else "📄"
        
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <h3 style="margin-top: 0;">{document_icon} {selected_document}</h3>
            <p><strong>Type:</strong> {document_type}</p>
            <p><strong>Referenced Events:</strong> {len(facts)}</p>
            <p><strong>Arguments Made:</strong></p>
            <ul>
                {"".join([f"<li>{fact['argument']}</li>" for fact in facts if fact['party'] == ('Appellant' if 'Appellant' in document_type else 'Respondent')])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Group events by disputed status for better organization
        disputed_events = [fact for fact in facts if fact["status"] == "Disputed"]
        undisputed_events = [fact for fact in facts if fact["status"] == "Undisputed"]
        
        st.markdown("### Referenced Events")
        
        # Display disputed events first with warning styling
        if disputed_events:
            st.markdown("""
            <div style="background-color: #fff8f8; border-left: 3px solid #e15759; padding: 10px; margin-bottom: 15px; border-radius: 4px;">
                <h4 style="margin-top: 0; color: #e15759;">⚠️ Disputed Facts</h4>
            </div>
            """, unsafe_allow_html=True)
            
            event_options = [f"{fact['event']} ({fact['date']})" for fact in disputed_events]
            selected_disputed = st.selectbox("Select disputed event", [""] + event_options)
            
            if selected_disputed:
                selected_event = next((fact['event'] for fact in disputed_events if f"{fact['event']} ({fact['date']})" == selected_disputed), None)
        
        # Display undisputed events
        if undisputed_events:
            st.markdown("""
            <div style="background-color: #f8fff8; border-left: 3px solid #55a868; padding: 10px; margin-bottom: 15px; border-radius: 4px;">
                <h4 style="margin-top: 0; color: #55a868;">✓ Undisputed Facts</h4>
            </div>
            """, unsafe_allow_html=True)
            
            event_options = [f"{fact['event']} ({fact['date']})" for fact in undisputed_events]
            selected_undisputed = st.selectbox("Select undisputed event", [""] + event_options)
            
            if selected_undisputed:
                selected_event = next((fact['event'] for fact in undisputed_events if f"{fact['event']} ({fact['date']})" == selected_undisputed), None)

# Display the connection details if an event is selected
if selected_event:
    selected_fact = next((fact for fact in case_facts if fact['event'] == selected_event), None)
    
    if selected_fact:
        st.markdown("---")
        st.subheader("Connection Details")
        
        # Display connection visualization
        st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; margin: 30px 0; text-align: center;">
            <div style="display: flex; flex-direction: column; align-items: center;">
                <div style="width: 120px; height: 120px; border-radius: 50%; background-color: #f0f0f5; 
                      display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <span style="font-size: 48px;">📁</span>
                </div>
                <div style="margin-top: 10px; font-weight: 500;">Document</div>
                <div style="font-size: 14px; color: #666;">{selected_document}</div>
            </div>
            
            <div style="margin: 0 20px; display: flex; flex-direction: column; align-items: center;">
                <div style="width: 150px; height: 2px; background-color: #333; margin-bottom: 5px;"></div>
                <div style="font-size: 14px; color: #666;">References</div>
                <div style="width: 150px; height: 2px; background-color: #333; margin-top: 5px;"></div>
            </div>
            
            <div style="display: flex; flex-direction: column; align-items: center;">
                <div style="width: 120px; height: 120px; border-radius: 50%; 
                      background-color: {'#e6f3ff' if selected_fact['party'] == 'Appellant' else '#ffefef'}; 
                      display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <span style="font-size: 48px;">📅</span>
                </div>
                <div style="margin-top: 10px; font-weight: 500;">Event</div>
                <div style="font-size: 14px; color: #666;">{selected_fact['date']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Create columns for detailed information
        col1, col2 = st.columns(2)
        
        with col1:
            party_class = "appellant" if selected_fact["party"] == "Appellant" else "respondent"
            status_class = "disputed" if selected_fact["status"] == "Disputed" else "undisputed"
            party_tag_class = f"{party_class}-tag"
            
            st.markdown(f"""
            <div class="timeline-event {party_class}">
                <h4>{selected_fact['event']}</h4>
                <p><strong>Date:</strong> {selected_fact['date']}</p>
                <p><strong>Party:</strong> <span class="{party_tag_class}">{selected_fact['party']}</span></p>
                <p><strong>Status:</strong> <span class="status-tag {status_class}">{selected_fact['status']}</span></p>
                <p><strong>Related Argument:</strong> {selected_fact['argument']}</p>
                <p><strong>Evidence:</strong> <span class="evidence-tag">{selected_fact['evidence']}</span></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Show other documents referencing this event
            other_docs = [doc for doc in selected_fact['related_documents'] if doc != selected_document]
            
            st.markdown(f"""
            <div style="background-color: white; padding: 20px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <h4 style="margin-top: 0;">Other Documents Referencing This Event</h4>
                
                {"<ul>" + "".join([f"<li>📁 {doc}</li>" for doc in other_docs]) + "</ul>" if other_docs else 
                "<p>No other documents reference this event.</p>"}
                
                <h4>Connection Impact</h4>
                <p>This event is {'disputed' if selected_fact['status'] == 'Disputed' else 'undisputed'} and is used to support:</p>
                <ul>
                    <li><strong>{selected_fact['argument']}</strong></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # If this is a disputed fact, show the conflicting claims
        if selected_fact['status'] == 'Disputed':
            st.markdown("### Conflicting Claims")
            
            opposing_facts = [f for f in case_facts if f['argument'] == selected_fact['argument'] 
                             and f['party'] != selected_fact['party'] and f['status'] == 'Disputed']
            
            if opposing_facts:
                for fact in opposing_facts:
                    opp_party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
                    opp_party_tag_class = f"{opp_party_class}-tag"
                    
                    st.markdown(f"""
                    <div class="timeline-event {opp_party_class}">
                        <h4>{fact['event']}</h4>
                        <p><strong>Date:</strong> {fact['date']}</p>
                        <p><strong>Party:</strong> <span class="{opp_party_tag_class}">{fact['party']}</span></p>
                        <p><strong>Evidence:</strong> <span class="evidence-tag">{fact['evidence']}</span></p>
                        <p><strong>Referenced in:</strong></p>
                        <ul>
                            {"".join([f"<li>📁 {doc}</li>" for doc in fact['related_documents']])}
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)

# Add footer with action buttons to match screenshot 1
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    st.button("Copy")
with col2:
    st.button("Export")
        # Create a visual timeline specific to this document
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        st.markdown("### Timeline for this Document")
        
        # Create a horizontal timeline for document events
        st.markdown("""
        <div style="position: relative; height: 120px; margin: 30px 0; background-color: white; 
             border-radius: 6px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        """, unsafe_allow_html=True)
        
        # Get all years from events
        all_years = set()
        for fact in sorted_facts:
            date_parts = fact['date'].split('-')
            all_years.add(int(date_parts[0]))
            if len(date_parts) > 1 and date_parts[1] != "present":
                all_years.add(int(date_parts[1]))
        
        # Create year markers
        timeline_years = sorted(list(all_years))
        if "present" in [f['date'].split('-')[-1] for f in sorted_facts]:
            timeline_years.append(2025)  # Use current year for "present"
        
        # Draw the timeline line
        st.markdown("""
        <div style="position: absolute; top: 50px; left: 40px; right: 40px; height: 2px; background-color: #ddd;"></div>
        """, unsafe_allow_html=True)
        
        # Calculate positions for year markers
        if len(timeline_years) > 1:
            min_year = min(timeline_years)
            max_year = max(timeline_years)
            year_range = max_year - min_year
            
            # Draw year markers
            for year in timeline_years:
                if year_range > 0:
                    position = ((year - min_year) / year_range) * 100
                else:
                    position = 50
                
                # Display as "Present" if it's the max year and we have a "present" date
                year_label = "Present" if year == max_year and "present" in [f['date'].split('-')[-1] for f in sorted_facts] else year
                
                st.markdown(f"""
                <div style="position: absolute; top: 60px; left: calc(40px + {position}% * (100% - 80px)); 
                     transform: translateX(-50%); text-align: center;">
                    <div style="width: 2px; height: 8px; background-color: #666; margin: 0 auto;"></div>
                    <div style="font-size: 12px; color: #666; margin-top: 5px;">{year_label}</div>
                </div>
                """, unsafe_allow_html=True)
        
            # Draw event markers on timeline
            for fact in sorted_facts:
                date_parts = fact['date'].split('-')
                start_year = int(date_parts[0])
                
                # Determine position based on start year
                position = ((start_year - min_year) / year_range) * 100 if year_range > 0 else 50
                
                # Color based on party
                color = "#4c72b0" if fact["party"] == "Appellant" else "#e15759"
                
                # Draw marker
                st.markdown(f"""
                <div style="position: absolute; top: 40px; left: calc(40px + {position}% * (100% - 80px)); 
                     transform: translateX(-50%);">
                    <div style="width: 16px; height: 16px; background-color: {color}; border-radius: 50%; 
                         border: 2px solid white; box-shadow: 0 1px 3px rgba(0,0,0,0.2);"
                         title="{fact['event']}"></div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Group events by argument with improved styling
        st.markdown("### Arguments Referenced")
        
        # Group by argument
        facts_by_argument = {}
        for fact in facts:
            arg = fact['argument']
            if arg not in facts_by_argument:
                facts_by_argument[arg] = []
            facts_by_argument[arg].append(fact)
        
        for arg, arg_facts in facts_by_argument.items():
            with st.expander(arg, expanded=False):
                for fact in arg_facts:
                    party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
                    status_class = "disputed" if fact["status"] == "Disputed" else "undisputed"
                    party_tag_class = f"{party_class}-tag"
                    
                    st.markdown(f"""
                    <div class="timeline-event {party_class}" style="margin-bottom: 15px;">
                        <h4>{fact['event']}</h4>
                        <p><strong>Date:</strong> {fact['date']}</p>
                        <p><strong>Party:</strong> <span class="{party_tag_class}">{fact['party']}</span></p>
                        <p><strong>Status:</strong> <span class="status-tag {status_class}">{fact['status']}</span></p>
                        <p><strong>Evidence:</strong> <span class="evidence-tag">{fact['evidence']}</span></p>
                    </div>
                    """, unsafe_allow_html=True)import streamlit as st
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
    /* Document folders styling (from screenshot 2) */
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
    
    /* Tab styling to match screenshot 1 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0px;
        border-bottom: 1px solid #ddd;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 16px;
        background-color: transparent;
        border: none;
        font-weight: 500;
        color: #666;
    }
    .stTabs [aria-selected="true"] {
        background-color: transparent !important;
        color: #4c72b0 !important;
        border-bottom: 2px solid #4c72b0 !important;
    }
    
    /* Facts table styling to match screenshot 1 */
    .facts-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        background-color: white;
        border-radius: 6px;
        overflow: hidden;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .facts-table th {
        text-align: left;
        padding: 12px 15px;
        background-color: #f8f9fa;
        border-bottom: 1px solid #eee;
        color: #666;
        font-weight: 500;
    }
    .facts-table td {
        padding: 12px 15px;
        border-bottom: 1px solid #eee;
        vertical-align: top;
    }
    .facts-table tr:last-child td {
        border-bottom: none;
    }
    .facts-table tr:hover {
        background-color: #f9fafb;
    }
    
    /* Party and evidence tags to match screenshot 1 */
    .appellant-tag {
        color: #4c72b0;
        font-weight: 500;
    }
    .respondent-tag {
        color: #e15759;
        font-weight: 500;
    }
    .evidence-tag {
        background-color: #f8f2e9;
        border-radius: 4px;
        padding: 2px 8px;
        font-size: 12px;
        color: #c67941;
        font-weight: 500;
    }
    .status-tag {
        border-radius: 4px;
        padding: 2px 8px;
        font-size: 12px;
        color: white;
        font-weight: 500;
    }
    .disputed {
        background-color: #e15759;
    }
    .undisputed {
        background-color: #55a868;
    }
    
    /* Event styling with better match to screenshot 1 */
    .timeline-event {
        padding: 15px;
        border-radius: 6px;
        margin: 10px 0;
        background-color: white;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .appellant {
        border-left: 4px solid #4c72b0;
    }
    .respondent {
        border-left: 4px solid #e15759;
    }
    
    /* Timeline styling */
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
        background-color: #ddd;
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
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .timeline-marker.respondent {
        background-color: #e15759;
        border: 2px solid white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .timeline-content {
        position: relative;
        margin-left: 15px;
        padding: 15px;
        background-color: white;
        border-radius: 6px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .timeline-date {
        position: absolute;
        left: -85px;
        width: 70px;
        text-align: right;
        font-size: 12px;
        color: #666;
        font-weight: 500;
    }
    
    /* Button styling to match screenshot 1 */
    .stButton button {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 4px;
        color: #333;
        font-weight: 500;
    }
    .stButton button:hover {
        background-color: #f8f9fa;
        border-color: #ccc;
    }
    
    /* Header styling */
    h1, h2, h3, h4 {
        color: #333;
        font-weight: 600;
    }
    
    /* Override some default Streamlit styles */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
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
    # Display facts table matching screenshot 1 style
    st.markdown("""
    <table class="facts-table">
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
    
    # Display rows with styling based on party and status
    for i, fact in enumerate(case_facts):
        # Determine party style and class
        party_class = "appellant-tag" if fact["party"] == "Appellant" else "respondent-tag"
        status_class = "disputed" if fact["status"] == "Disputed" else "undisputed"
        
        st.markdown(f"""
        <tr>
            <td>{fact["date"]}</td>
            <td>{fact["event"]}</td>
            <td><span class="{party_class}">{fact["party"]}</span></td>
            <td><span class="status-tag {status_class}">{fact["status"]}</span></td>
            <td>{fact["argument"]}</td>
            <td><span class="evidence-tag">{fact["evidence"]}</span></td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        </tbody>
    </table>
    """, unsafe_allow_html=True)
    
    # Create expandable containers for each fact (below the table)
    for i, fact in enumerate(case_facts):
        party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
        status_class = "disputed" if fact["status"] == "Disputed" else "undisputed"
        party_tag_class = f"{party_class}-tag"
        
        with st.expander(f"View details for: {fact['event']}", expanded=False):
            st.markdown(f"""
            <div class="timeline-event {party_class}">
                <h4>{fact['event']}</h4>
                <p><strong>Date:</strong> {fact['date']}</p>
                <p><strong>Party:</strong> <span class="{party_tag_class}">{fact['party']}</span></p>
                <p><strong>Status:</strong> <span class="status-tag {status_class}">{fact['status']}</span></p>
                <p><strong>Related Argument:</strong> {fact['argument']}</p>
                <p><strong>Evidence:</strong> <span class="evidence-tag">{fact['evidence']}</span></p>
                <p><strong>Related Documents:</strong></p>
                <ul>
                    {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

with tabs[1]:  # Disputed Facts
    disputed_facts = [fact for fact in case_facts if fact["status"] == "Disputed"]
    
    if disputed_facts:
        # Display disputed facts table similar to screenshot 1
        st.markdown("""
        <table class="facts-table">
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
        
        # Display rows with styling based on party
        for i, fact in enumerate(disputed_facts):
            # Determine party style and class
            party_class = "appellant-tag" if fact["party"] == "Appellant" else "respondent-tag"
            
            st.markdown(f"""
            <tr>
                <td>{fact["date"]}</td>
                <td>{fact["event"]}</td>
                <td><span class="{party_class}">{fact["party"]}</span></td>
                <td><span class="status-tag disputed">Disputed</span></td>
                <td>{fact["argument"]}</td>
                <td><span class="evidence-tag">{fact["evidence"]}</span></td>
            </tr>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            </tbody>
        </table>
        """, unsafe_allow_html=True)
        
        # Show timeline visualization
        st.subheader("Timeline of Disputed Facts")
        create_timeline(disputed_facts)
        
        # Organize disputed facts by argument to show conflicts
        disputed_by_argument = {}
        for fact in disputed_facts:
            arg = fact['argument']
            if arg not in disputed_by_argument:
                disputed_by_argument[arg] = []
            disputed_by_argument[arg].append(fact)
        
        # Show conflicting claims for each argument
        st.subheader("Conflicting Claims Analysis")
        for arg, facts in disputed_by_argument.items():
            if len(facts) > 1 and len(set([f['party'] for f in facts])) > 1:
                with st.expander(f"Conflict: {arg}", expanded=True):
                    st.markdown(f"### {arg}")
                    
                    # Create columns for appellant and respondent
                    col1, col2 = st.columns(2)
                    
                    appellant_facts = [f for f in facts if f['party'] == 'Appellant']
                    respondent_facts = [f for f in facts if f['party'] == 'Respondent']
                    
                    with col1:
                        st.markdown("#### Appellant's Position")
                        for fact in appellant_facts:
                            st.markdown(f"""
                            <div class="timeline-event appellant">
                                <h4>{fact['event']}</h4>
                                <p><strong>Date:</strong> {fact['date']}</p>
                                <p><strong>Evidence:</strong> <span class="evidence-tag">{fact['evidence']}</span></p>
                                <p><strong>Referenced in:</strong></p>
                                <ul>
                                    {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                                </ul>
                            </div>
                            """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown("#### Respondent's Position")
                        for fact in respondent_facts:
                            st.markdown(f"""
                            <div class="timeline-event respondent">
                                <h4>{fact['event']}</h4>
                                <p><strong>Date:</strong> {fact['date']}</p>
                                <p><strong>Evidence:</strong> <span class="evidence-tag">{fact['evidence']}</span></p>
                                <p><strong>Referenced in:</strong></p>
                                <ul>
                                    {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                                </ul>
                            </div>
                            """, unsafe_allow_html=True)
            else:
                # Single disputed fact without direct conflict
                for fact in facts:
                    party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
                    party_tag_class = f"{party_class}-tag"
                    
                    with st.expander(f"{fact['event']} ({fact['party']})", expanded=False):
                        st.markdown(f"""
                        <div class="timeline-event {party_class}">
                            <h4>{fact['event']}</h4>
                            <p><strong>Date:</strong> {fact['date']}</p>
                            <p><strong>Party:</strong> <span class="{party_tag_class}">{fact['party']}</span></p>
                            <p><strong>Related Argument:</strong> {fact['argument']}</p>
                            <p><strong>Evidence:</strong> <span class="evidence-tag">{fact['evidence']}</span></p>
                            <p><strong>Related Documents:</strong></p>
                            <ul>
                                {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                            </ul>
                        </div>
                        """, unsafe_allow_html=True)
    else:
        st.info("No disputed facts found.")

with tabs[2]:  # Undisputed Facts
    undisputed_facts = [fact for fact in case_facts if fact["status"] == "Undisputed"]
    
    if undisputed_facts:
        # Display undisputed facts table similar to screenshot 1
        st.markdown("""
        <table class="facts-table">
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
        
        # Display rows with styling based on party
        for fact in undisputed_facts:
            # Determine party style and class
            party_class = "appellant-tag" if fact["party"] == "Appellant" else "respondent-tag"
            
            st.markdown(f"""
            <tr>
                <td>{fact["date"]}</td>
                <td>{fact["event"]}</td>
                <td><span class="{party_class}">{fact["party"]}</span></td>
                <td><span class="status-tag undisputed">Undisputed</span></td>
                <td>{fact["argument"]}</td>
                <td><span class="evidence-tag">{fact["evidence"]}</span></td>
            </tr>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            </tbody>
        </table>
        """, unsafe_allow_html=True)
        
        # Show timeline visualization
        st.subheader("Timeline of Undisputed Facts")
        create_timeline(undisputed_facts)
        
        # Group undisputed facts by argument for better organization
        facts_by_argument = {}
        for fact in undisputed_facts:
            arg = fact['argument']
            if arg not in facts_by_argument:
                facts_by_argument[arg] = []
            facts_by_argument[arg].append(fact)
        
        # Show details organized by argument
        st.subheader("Undisputed Facts by Argument")
        for arg, facts in facts_by_argument.items():
            with st.expander(f"{arg}", expanded=False):
                st.markdown(f"### {arg}")
                
                # Create a card for each fact
                for fact in facts:
                    party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
                    party_tag_class = f"{party_class}-tag"
                    
                    st.markdown(f"""
                    <div class="timeline-event {party_class}">
                        <h4>{fact['event']}</h4>
                        <p><strong>Date:</strong> {fact['date']}</p>
                        <p><strong>Party:</strong> <span class="{party_tag_class}">{fact['party']}</span></p>
                        <p><strong>Evidence:</strong> <span class="evidence-tag">{fact['evidence']}</span></p>
                        <p><strong>Referenced in:</strong></p>
                        <ul>
                            {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Add a small spacer between facts
                    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
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
        
        # Display a styled table for facts in this document
        st.markdown("""
        <table class="facts-table">
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
        
        # Sort facts by date and display in table
        sorted_facts = sorted(facts, key=lambda x: x['date'].split('-')[0])
        for fact in sorted_facts:
            # Determine party and status styling
            party_class = "appellant-tag" if fact["party"] == "Appellant" else "respondent-tag"
            status_class = "disputed" if fact["status"] == "Disputed" else "undisputed"
            
            st.markdown(f"""
            <tr>
                <td>{fact["date"]}</td>
                <td>{fact["event"]}</td>
                <td><span class="{party_class}">{fact["party"]}</span></td>
                <td><span class="status-tag {status_class}">{fact["status"]}</span></td>
                <td>{fact["argument"]}</td>
                <td><span class="evidence-tag">{fact["evidence"]}</span></td>
            </tr>
            """, unsafe_allow_html=True)
            
        st.markdown("""
            </tbody>
        </table>
        """, unsafe_allow_html=True)
