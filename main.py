import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Case Document Timeline", layout="wide")

# Custom CSS to match the screenshot styling
st.markdown("""
<style>
    /* Main UI styling */
    .main .block-container {
        padding-top: 1rem;
    }
    
    /* Table styling */
    .stDataFrame {
        border: none;
    }
    .facts-table {
        width: 100%;
        border-collapse: collapse;
    }
    .facts-table th {
        background-color: #f8f9fa;
        padding: 10px;
        text-align: left;
        font-weight: 600;
        color: #333;
        border-bottom: 1px solid #ddd;
    }
    .facts-table td {
        padding: 12px 10px;
        border-bottom: 1px solid #eee;
        vertical-align: top;
    }
    
    /* Status badges */
    .badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
    }
    .appellant {
        background-color: #dbeafe;
        color: #1e40af;
    }
    .respondent {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    .disputed {
        background-color: #fef3c7;
        color: #92400e;
    }
    .undisputed {
        background-color: #d1fae5;
        color: #065f46;
    }
    
    /* Document folder styling */
    .folder {
        display: flex;
        align-items: center;
        padding: 8px 12px;
        border-radius: 4px;
        margin-bottom: 4px;
        background-color: #f9fafb;
        cursor: pointer;
    }
    .folder:hover {
        background-color: #f3f4f6;
    }
    .folder-blue {
        border-left: 4px solid #3b82f6;
    }
    .folder-red {
        border-left: 4px solid #ef4444;
    }
    .folder-gray {
        border-left: 4px solid #9ca3af;
    }
    .folder-icon {
        color: #3b82f6;
        margin-right: 8px;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 16px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px;
        border-radius: 4px;
    }
    
    /* Hide default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Document folders data - matching the first screenshot
document_folders = [
    {"id": "1", "name": "1. Statement of Appeal", "party": "Appellant"},
    {"id": "2", "name": "2. Request for a Stay", "party": "Respondent"},
    {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent"},
    {"id": "4", "name": "4. Answer to PM", "party": "Respondent"},
    {"id": "5", "name": "5. Appeal Brief", "party": "Appellant"},
    {"id": "6", "name": "6. Brief on Admissibility", "party": "Court"},
    {"id": "7", "name": "7. Reply to Objection to Admissibility", "party": "Appellant"},
    {"id": "8", "name": "8. Challenge", "party": "Respondent"},
    {"id": "9", "name": "ChatGPT", "party": "Other"},
    {"id": "10", "name": "Jurisprudence", "party": "Other"},
    {"id": "11", "name": "Objection to Admissibility", "party": "Respondent"},
    {"id": "12", "name": "Swiss Court", "party": "Court"}
]

# Timeline events data - matching the second screenshot
timeline_events = [
    {"date": "1950-present", "event": "Continuous operation under same name since 1950", "party": "Appellant", "status": "Undisputed", "related_argument": "1. Sporting Succession", "evidence": "C-1"},
    {"date": "1950", "event": "Initial registration in 1950", "party": "Appellant", "status": "Undisputed", "related_argument": "1.1.1. Registration History", "evidence": "C-2"},
    {"date": "1950-present", "event": "Consistent use of blue and white since founding", "party": "Appellant", "status": "Disputed", "related_argument": "1.2. Club Colors Analysis", "evidence": "C-4"},
    {"date": "1950-1975", "event": "Pre-1976 colors represented original city district", "party": "Respondent", "status": "Undisputed", "related_argument": "1.2.1. Color Changes Analysis", "evidence": "R-5"},
    {"date": "1970-1980", "event": "Minor shade variations do not affect continuity", "party": "Appellant", "status": "Undisputed", "related_argument": "1.2.1. Color Variations Analysis", "evidence": "C-5"},
    {"date": "1975-1976", "event": "Brief administrative gap in 1975-1976", "party": "Appellant", "status": "Disputed", "related_argument": "1.1.1. Registration History", "evidence": "C-2"},
    {"date": "1975-1976", "event": "Operations ceased between 1975-1976", "party": "Respondent", "status": "Disputed", "related_argument": "1. Sporting Succession Rebuttal", "evidence": "R-1"},
    {"date": "April 30, 1975", "event": "Registration formally terminated on April 30, 1975", "party": "Respondent", "status": "Undisputed", "related_argument": "1.1.1. Registration Gap", "evidence": "R-2"}
]

# Add document folder references to events (matching your screenshots)
for event in timeline_events:
    if event["evidence"] == "C-1" or event["evidence"] == "C-2" or event["evidence"] == "C-3":
        event["related_folder"] = "1"
    elif event["evidence"] == "R-3" or event["evidence"] == "R-4":
        event["related_folder"] = "2"
    elif event["evidence"] == "R-1":
        event["related_folder"] = "3"
    elif event["evidence"] == "R-2" or event["evidence"] == "R-5":
        event["related_folder"] = "4"
    elif event["evidence"] == "C-4" or event["evidence"] == "C-5" or event["evidence"] == "C-6":
        event["related_folder"] = "5"
    else:
        event["related_folder"] = ""

# Convert to DataFrame for easier manipulation
events_df = pd.DataFrame(timeline_events)

# Create sidebar with document folders
with st.sidebar:
    # Add logo/title
    st.markdown("<h2 style='color:#3b82f6;'>CaseLens</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
    
    # Add sidebar navigation
    st.markdown("---")
    
    # Create session state for tracking selected folders
    if 'selected_folder' not in st.session_state:
        st.session_state.selected_folder = "1"  # Default to first folder
    
    # Display document folders
    st.markdown("<p style='font-weight:500; margin-bottom:10px;'>Documents</p>", unsafe_allow_html=True)
    
    # Create clickable folders
    for folder in document_folders:
        folder_id = folder["id"]
        folder_name = folder["name"]
        
        # Determine folder styling based on party
        border_class = ""
        if folder["party"] == "Appellant":
            border_class = "folder-blue"
        elif folder["party"] == "Respondent":
            border_class = "folder-red"
        else:
            border_class = "folder-gray"
        
        # Create clickable folder div
        is_selected = st.session_state.selected_folder == folder_id
        bg_color = "#f0f9ff" if is_selected else "#f9fafb"
        
        folder_html = f"""
        <div class="folder {border_class}" style="background-color:{bg_color};" 
            onclick="handleFolderClick('{folder_id}')">
            <span class="folder-icon">📁</span>
            <span>{folder_name}</span>
        </div>
        """
        st.markdown(folder_html, unsafe_allow_html=True)
        
        # Add JavaScript for handling clicks
        st.markdown("""
        <script>
        function handleFolderClick(folderId) {
            // Use Streamlit's setComponentValue to update session state
            // This is a simplified example - in a real app you'd need a custom component
            window.parent.postMessage({
                type: "streamlit:setComponentValue",
                value: folderId
            }, "*");
        }
        </script>
        """, unsafe_allow_html=True)
        
        # For the demo, also add regular buttons that actually work
        # (The clickable divs above are just for show, as they need custom components to work properly)
        if st.button(f"{folder_name}", key=f"btn_{folder_id}", use_container_width=True):
            st.session_state.selected_folder = folder_id
            st.experimental_rerun()

# Main content area
st.title("Summary of arguments")
st.header("Case Facts")

# Create tabs for filtering facts
tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])

with tab1:
    # Function to highlight the selected folder's events
    def highlight_rows(row):
        if row.related_folder == st.session_state.selected_folder:
            return ['background-color: #f0f9ff'] * len(row)
        return [''] * len(row)
    
    # Create a styled DataFrame
    styled_df = events_df.style.apply(highlight_rows, axis=1)
    
    # Custom render for table to match screenshot exactly
    html_table = """
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
    """
    
    for _, row in events_df.iterrows():
        # Highlight row if it's related to selected folder
        row_style = ""
        if row["related_folder"] == st.session_state.selected_folder:
            row_style = "background-color: #f0f9ff;"
        
        # Format party badge
        party_class = "appellant" if row["party"] == "Appellant" else "respondent"
        party_badge = f'<span class="badge {party_class}">{row["party"]}</span>'
        
        # Format status badge
        status_class = "disputed" if row["status"] == "Disputed" else "undisputed"
        status_badge = f'<span class="badge {status_class}">{row["status"]}</span>'
        
        # Format evidence and related document
        evidence_badge = f'<span class="badge" style="background-color: #f3f4f6; color: #4b5563;">Evidence: {row["evidence"]}</span>'
        
        # Add related document badge (folder number)
        folder_num = row["related_folder"]
        doc_badge = f'<span class="badge" style="background-color: #e0e7ff; color: #4338ca; margin-left: 5px;">Document {folder_num}</span>'
        
        # Add row to table
        html_table += f"""
        <tr style="{row_style}">
            <td>{row["date"]}</td>
            <td>{row["event"]}</td>
            <td>{party_badge}</td>
            <td>{status_badge}</td>
            <td>{row["related_argument"]}</td>
            <td>{evidence_badge} {doc_badge}</td>
        </tr>
        """
    
    html_table += """
        </tbody>
    </table>
    """
    
    st.markdown(html_table, unsafe_allow_html=True)
    
    # Add Copy and Export buttons to match screenshot
    col1, col2 = st.columns([1, 10])
    with col1:
        st.button("Copy", key="copy_btn")
    with col2:
        st.button("Export", key="export_btn")

with tab2:
    # Filter for disputed facts
    disputed_df = events_df[events_df["status"] == "Disputed"]
    
    # Create the same table but only with disputed facts
    html_table = """
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
    """
    
    for _, row in disputed_df.iterrows():
        # Highlight row if it's related to selected folder
        row_style = ""
        if row["related_folder"] == st.session_state.selected_folder:
            row_style = "background-color: #f0f9ff;"
        
        # Format party badge
        party_class = "appellant" if row["party"] == "Appellant" else "respondent"
        party_badge = f'<span class="badge {party_class}">{row["party"]}</span>'
        
        # Format status badge
        status_badge = f'<span class="badge disputed">Disputed</span>'
        
        # Format evidence and related document
        evidence_badge = f'<span class="badge" style="background-color: #f3f4f6; color: #4b5563;">Evidence: {row["evidence"]}</span>'
        
        # Add related document badge (folder number)
        folder_num = row["related_folder"]
        doc_badge = f'<span class="badge" style="background-color: #e0e7ff; color: #4338ca; margin-left: 5px;">Document {folder_num}</span>'
        
        # Add row to table
        html_table += f"""
        <tr style="{row_style}">
            <td>{row["date"]}</td>
            <td>{row["event"]}</td>
            <td>{party_badge}</td>
            <td>{status_badge}</td>
            <td>{row["related_argument"]}</td>
            <td>{evidence_badge} {doc_badge}</td>
        </tr>
        """
    
    html_table += """
        </tbody>
    </table>
    """
    
    st.markdown(html_table, unsafe_allow_html=True)

with tab3:
    # Filter for undisputed facts
    undisputed_df = events_df[events_df["status"] == "Undisputed"]
    
    # Create the same table but only with undisputed facts
    html_table = """
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
    """
    
    for _, row in undisputed_df.iterrows():
        # Highlight row if it's related to selected folder
        row_style = ""
        if row["related_folder"] == st.session_state.selected_folder:
            row_style = "background-color: #f0f9ff;"
        
        # Format party badge
        party_class = "appellant" if row["party"] == "Appellant" else "respondent"
        party_badge = f'<span class="badge {party_class}">{row["party"]}</span>'
        
        # Format status badge
        status_badge = f'<span class="badge undisputed">Undisputed</span>'
        
        # Format evidence and related document
        evidence_badge = f'<span class="badge" style="background-color: #f3f4f6; color: #4b5563;">Evidence: {row["evidence"]}</span>'
        
        # Add related document badge (folder number)
        folder_num = row["related_folder"]
        doc_badge = f'<span class="badge" style="background-color: #e0e7ff; color: #4338ca; margin-left: 5px;">Document {folder_num}</span>'
        
        # Add row to table
        html_table += f"""
        <tr style="{row_style}">
            <td>{row["date"]}</td>
            <td>{row["event"]}</td>
            <td>{party_badge}</td>
            <td>{status_badge}</td>
            <td>{row["related_argument"]}</td>
            <td>{evidence_badge} {doc_badge}</td>
        </tr>
        """
    
    html_table += """
        </tbody>
    </table>
    """
    
    st.markdown(html_table, unsafe_allow_html=True)

# Add visualization component that shows the relationship between documents and events
st.markdown("""
<div style="margin-top: 30px;">
    <h3>Connections Between Documents and Timeline Events</h3>
    <p>The visualization below shows how documents connect to timeline events:</p>
</div>
""", unsafe_allow_html=True)

# Create a function to visualize connections between documents and events
def visualize_document_event_connections():
    # Get the selected folder
    selected_folder = st.session_state.selected_folder
    
    # Find related events
    related_events = events_df[events_df["related_folder"] == selected_folder]
    
    # If there are no related events, show a message
    if len(related_events) == 0:
        st.info("This document doesn't have any connected timeline events.")
        return
    
    # Create HTML for visualization
    vis_html = f"""
    <div style="margin-top: 20px; background-color: #f8fafc; padding: 20px; border-radius: 8px;">
        <h4>Document: {next((f['name'] for f in document_folders if f['id'] == selected_folder), 'Unknown Document')}</h4>
        <div style="display: flex; margin-top: 15px;">
            <div style="flex: 0 0 200px; background-color: #fff; padding: 15px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <div style="font-weight: 500; margin-bottom: 10px;">📁 Document Folder</div>
                <div style="font-size: 14px; color: #4b5563;">
                    <div>ID: {selected_folder}</div>
                    <div>Party: {next((f['party'] for f in document_folders if f['id'] == selected_folder), 'Unknown')}</div>
                    <div>Exhibits: {", ".join([e["evidence"] for _, e in related_events.iterrows()])}</div>
                </div>
            </div>
            
            <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
                <div style="width: 80px; height: 2px; background-color: #3b82f6;"></div>
                <div style="width: 0; height: 0; border-top: 6px solid transparent; border-bottom: 6px solid transparent; border-left: 10px solid #3b82f6;"></div>
            </div>
            
            <div style="flex: 0 0 400px; background-color: #fff; padding: 15px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <div style="font-weight: 500; margin-bottom: 10px;">📅 Connected Timeline Events ({len(related_events)})</div>
                <div style="max-height: 200px; overflow-y: auto;">
    """
    
    # Add events to visualization
    for _, event in related_events.iterrows():
        event_status_class = "disputed" if event["status"] == "Disputed" else "undisputed"
        event_party_class = "appellant" if event["party"] == "Appellant" else "respondent"
        
        vis_html += f"""
            <div style="margin-bottom: 10px; padding: 8px; border-left: 3px solid #3b82f6; background-color: #f9fafb;">
                <div style="font-weight: 500;">{event["event"]}</div>
                <div style="display: flex; margin-top: 5px; font-size: 12px;">
                    <span class="badge {event_status_class}" style="margin-right: 5px;">{event["status"]}</span>
                    <span class="badge {event_party_class}">{event["party"]}</span>
                    <span style="margin-left: auto; color: #6b7280;">{event["date"]}</span>
                </div>
            </div>
        """
    
    vis_html += """
                </div>
            </div>
        </div>
    </div>
    """
    
    st.markdown(vis_html, unsafe_allow_html=True)

# Run the visualization function
visualize_document_event_connections()

# Add a data flow diagram showing how all documents connect to facts
st.markdown("""
<div style="margin-top: 30px;">
    <h3>Document-Event Connection Overview</h3>
    <p>This diagram shows how all case documents connect to the timeline events:</p>
</div>
""", unsafe_allow_html=True)

# Count events per document
doc_event_counts = events_df['related_folder'].value_counts().to_dict()

# Create a horizontal diagram showing connections
diagram_html = """
<div style="margin-top: 20px; padding: 20px; background-color: #f8fafc; border-radius: 8px; overflow-x: auto;">
    <div style="display: flex; justify-content: space-between; min-width: 900px;">
"""

# Left side - Documents
diagram_html += """
        <div style="flex: 0 0 300px;">
            <h4 style="margin-bottom: 15px;">Case Documents</h4>
            <div style="display: flex; flex-direction: column; gap: 8px;">
"""

# Add document boxes
for folder in document_folders:
    folder_id = folder["id"]
    folder_name = folder["name"]
    
    # Skip documents with no events
    if folder_id not in doc_event_counts:
        continue
    
    # Determine border color based on party
    border_color = "#3b82f6" if folder["party"] == "Appellant" else "#ef4444" if folder["party"] == "Respondent" else "#9ca3af"
    
    # Highlight selected folder
    bg_color = "#f0f9ff" if folder_id == st.session_state.selected_folder else "#ffffff"
    
    diagram_html += f"""
                <div style="padding: 10px; background-color: {bg_color}; border-left: 4px solid {border_color}; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <div style="font-weight: 500;">{folder_name}</div>
                    <div style="font-size: 12px; color: #6b7280;">
                        Connected events: {doc_event_counts.get(folder_id, 0)}
                    </div>
                </div>
    """

diagram_html += """
            </div>
        </div>
"""

# Center - Connections
diagram_html += """
        <div style="flex: 0 0 100px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div style="width: 80px; height: 2px; background-color: #3b82f6;"></div>
            <div style="width: 0; height: 0; border-top: 6px solid transparent; border-bottom: 6px solid transparent; border-left: 10px solid #3b82f6;"></div>
        </div>
"""

# Right side - Events
diagram_html += """
        <div style="flex: 0 0 400px;">
            <h4 style="margin-bottom: 15px;">Timeline Events</h4>
            <div style="display: flex; flex-direction: column; gap: 8px;">
"""

# Group events by status
disputed_count = len(events_df[events_df["status"] == "Disputed"])
undisputed_count = len(events_df[events_df["status"] == "Undisputed"])

# Group events by party
appellant_count = len(events_df[events_df["party"] == "Appellant"])
respondent_count = len(events_df[events_df["party"] == "Respondent"])

# Add event group boxes
diagram_html += f"""
                <div style="padding: 10px; background-color: #ffffff; border-left: 4px solid #65a30d; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <div style="font-weight: 500;">Undisputed Events</div>
                    <div style="font-size: 12px; color: #6b7280;">Count: {undisputed_count}</div>
                </div>
                <div style="padding: 10px; background-color: #ffffff; border-left: 4px solid #d97706; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <div style="font-weight: 500;">Disputed Events</div>
                    <div style="font-size: 12px; color: #6b7280;">Count: {disputed_count}</div>
                </div>
                <div style="padding: 10px; background-color: #ffffff; border-left: 4px solid #3b82f6; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <div style="font-weight: 500;">Appellant Events</div>
                    <div style="font-size: 12px; color: #6b7280;">Count: {appellant_count}</div>
                </div>
                <div style="padding: 10px; background-color: #ffffff; border-left: 4px solid #ef4444; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <div style="font-weight: 500;">Respondent Events</div>
                    <div style="font-size: 12px; color: #6b7280;">Count: {respondent_count}</div>
                </div>
"""

diagram_html += """
            </div>
        </div>
    </div>
</div>
"""

st.markdown(diagram_html, unsafe_allow_html=True)

# Function to run the app
if __name__ == "__main__":
    # This is already running in the Streamlit app
    pass

