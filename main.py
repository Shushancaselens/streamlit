import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(layout="wide", page_title="CaseLens - Case Timeline")

# Custom CSS for styling
st.markdown("""
<style>
    .main .block-container {padding-top: 2rem;}
    .folder-item {
        padding: 10px 15px;
        border-radius: 4px;
        margin-bottom: 5px;
        cursor: pointer;
        display: flex;
        align-items: center;
    }
    .folder-item:hover {background-color: #f0f2f6;}
    .folder-item.active {background-color: #e6f0ff;}
    .folder-icon {
        color: #3b82f6;
        margin-right: 10px;
        font-size: 1.2rem;
    }
    .appellant {color: #3b82f6; font-weight: 500;}
    .respondent {color: #ef4444; font-weight: 500;}
    .disputed {color: #ef4444; font-size: 0.9rem;}
    .undisputed {color: #333; font-size: 0.9rem;}
    .evidence-tag {
        background-color: #f3f4f6;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.8rem;
        color: #666;
    }
    .st-ae {border: none !important;}
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .case-title {
        font-size: 1.75rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    .tab-container {
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
    .fact-tab {
        display: inline-block;
        padding: 0.5rem 1rem;
        font-weight: 500;
        cursor: pointer;
    }
    .fact-tab.active {
        color: #3b82f6;
        border-bottom: 2px solid #3b82f6;
    }
    .document-connection-line {
        border-left: 2px dashed #cbd5e1;
        padding-left: 15px;
        margin-left: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Application Title with Logo
col1, col2 = st.columns([1, 11])
with col1:
    st.markdown('<div style="background-color: #3b82f6; color: white; width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: bold;">C</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<h1 style="margin-bottom: 0; font-size: 1.5rem; font-weight: 600;">CaseLens</h1>', unsafe_allow_html=True)

st.markdown('<hr style="margin: 0.5rem 0 1.5rem 0; border: none; height: 1px; background-color: #e2e8f0;">', unsafe_allow_html=True)

# Create columns for layout
left_col, right_col = st.columns([1, 3])

# Document folders data
folders = [
    {"id": 1, "name": "1. Statement of Appeal", "type": "appellant", "date": "1950-03-15", "connected_events": ["Initial registration in 1950"]},
    {"id": 2, "name": "2. Request for a Stay", "type": "respondent", "date": "1950-04-10", "connected_events": []},
    {"id": 3, "name": "3. Answer to Request for PM", "type": "appellant", "date": "1950-05-22", "connected_events": []},
    {"id": 4, "name": "4. Answer to PM", "type": "respondent", "date": "1950-06-30", "connected_events": []},
    {"id": 5, "name": "5. Appeal Brief", "type": "appellant", "date": "1970-08-12", "connected_events": ["Minor shade variations do not affect continuity"]},
    {"id": 6, "name": "6. Brief on Admissibility", "type": "appellant", "date": "1975-01-20", "connected_events": ["Brief administrative gap in 1975-1976"]},
    {"id": 7, "name": "7. Reply to Objection to Admissibility", "type": "appellant", "date": "1975-03-05", "connected_events": []},
    {"id": 8, "name": "8. Challenge", "type": "respondent", "date": "1975-04-18", "connected_events": []},
    {"id": 9, "name": "ChatGPT", "type": "system", "date": "", "connected_events": []},
    {"id": 10, "name": "Jurisprudence", "type": "system", "date": "", "connected_events": []},
    {"id": 11, "name": "Objection to Admissibility", "type": "respondent", "date": "1975-02-15", "connected_events": []},
    {"id": 12, "name": "Swiss Court", "type": "system", "date": "", "connected_events": []},
]

# Case events data
events = [
    {"date": "1950-present", "event": "Continuous operation under same name since 1950", "party": "Appellant", "status": "Undisputed", "argument": "1. Sporting Succession", "evidence": "C-1"},
    {"date": "1950", "event": "Initial registration in 1950", "party": "Appellant", "status": "Undisputed", "argument": "1.1.1. Registration History", "evidence": "C-2"},
    {"date": "1950-present", "event": "Consistent use of blue and white since founding", "party": "Appellant", "status": "Disputed", "argument": "1.2. Club Colors Analysis", "evidence": "C-4"},
    {"date": "1950-1975", "event": "Pre-1976 colors represented original city district", "party": "Respondent", "status": "Undisputed", "argument": "1.2.1. Color Changes Analysis", "evidence": "R-5"},
    {"date": "1970-1980", "event": "Minor shade variations do not affect continuity", "party": "Appellant", "status": "Undisputed", "argument": "1.2.1. Color Variations Analysis", "evidence": "C-5"},
    {"date": "1975-1976", "event": "Brief administrative gap in 1975-1976", "party": "Appellant", "status": "Disputed", "argument": "1.1.1. Registration History", "evidence": "C-2"},
]

# Function to display folder with icon
def display_folder(folder, active=False):
    color_class = ""
    if folder["type"] == "appellant":
        color_class = "appellant"
    elif folder["type"] == "respondent":
        color_class = "respondent"
    
    active_class = "active" if active else ""
    
    return f"""
    <div class="folder-item {active_class}" id="folder-{folder['id']}">
        <span class="folder-icon">📁</span>
        <span class="{color_class}">{folder['name']}</span>
    </div>
    """

# Display folders in the left column
with left_col:
    st.markdown("### Legal Analysis")
    st.markdown('<div style="padding: 12px; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 10px;">📄 Arguments</div>', unsafe_allow_html=True)
    
    # Active section (Facts)
    st.markdown('<div style="padding: 12px; border: 1px solid #3b82f6; border-radius: 8px; margin-bottom: 10px; background-color: #f0f7ff;">📊 Facts</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="padding: 12px; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 10px;">📑 Exhibits</div>', unsafe_allow_html=True)
    
    st.markdown("### Documents")
    
    # Track the selected folder
    if 'selected_folder' not in st.session_state:
        st.session_state.selected_folder = 1
    
    # Display folders
    for folder in folders:
        st.markdown(
            display_folder(folder, active=st.session_state.selected_folder == folder['id']),
            unsafe_allow_html=True
        )
        # Handle folder click through JavaScript (in real Streamlit, this would be a button callback)
        if st.button(f"Select {folder['name']}", key=f"btn_{folder['id']}", help="Select this folder"):
            st.session_state.selected_folder = folder['id']
            st.experimental_rerun()

# Display timeline and connections in the right column
with right_col:
    # Header with controls
    st.markdown(
        """
        <div class="header-container">
            <h2 class="case-title">Summary of arguments</h2>
            <div>
                <button style="background-color: white; border: 1px solid #e2e8f0; padding: 0.5rem 1rem; border-radius: 4px; margin-right: 0.5rem;">Copy</button>
                <button style="background-color: white; border: 1px solid #e2e8f0; padding: 0.5rem 1rem; border-radius: 4px;">Export</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Tab navigation for facts
    st.markdown(
        """
        <h3>Case Facts</h3>
        <div class="tab-container">
            <span class="fact-tab active">All Facts</span>
            <span class="fact-tab">Disputed Facts</span>
            <span class="fact-tab">Undisputed Facts</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Create the facts table
    df = pd.DataFrame(events)
    
    # Highlight selected folder connections
    selected_folder = next((f for f in folders if f['id'] == st.session_state.selected_folder), None)
    
    # Create a table with custom formatting
    table_html = "<table style='width:100%; border-collapse: collapse;'>"
    
    # Headers
    table_html += """
    <thead>
        <tr style='border-bottom: 1px solid #e2e8f0;'>
            <th style='padding: 12px 8px; text-align: left; font-weight: 500;'>Date</th>
            <th style='padding: 12px 8px; text-align: left; font-weight: 500;'>Event</th>
            <th style='padding: 12px 8px; text-align: left; font-weight: 500;'>Party</th>
            <th style='padding: 12px 8px; text-align: left; font-weight: 500;'>Status</th>
            <th style='padding: 12px 8px; text-align: left; font-weight: 500;'>Related Argument</th>
            <th style='padding: 12px 8px; text-align: left; font-weight: 500;'>Evidence</th>
        </tr>
    </thead>
    <tbody>
    """
    
    # Rows
    for i, event in enumerate(events):
        # Check if this event is connected to the selected folder
        is_connected = selected_folder and event['event'] in selected_folder['connected_events']
        row_style = "background-color: #f0f7ff;" if is_connected else ""
        
        # Party styling
        party_class = "appellant" if event['party'] == "Appellant" else "respondent"
        
        # Status styling
        status_class = "disputed" if event['status'] == "Disputed" else "undisputed"
        
        table_html += f"""
        <tr style='border-bottom: 1px solid #e2e8f0; {row_style}'>
            <td style='padding: 12px 8px;'>{event['date']}</td>
            <td style='padding: 12px 8px;'>{event['event']}</td>
            <td style='padding: 12px 8px;'><span class='{party_class}'>{event['party']}</span></td>
            <td style='padding: 12px 8px;'><span class='{status_class}'>{event['status']}</span></td>
            <td style='padding: 12px 8px;'>{event['argument']}</td>
            <td style='padding: 12px 8px;'><span class='evidence-tag'>{event['evidence']}</span></td>
        </tr>
        """
        
        # If this event is connected to the selected folder, show the connection
        if is_connected:
            table_html += f"""
            <tr style='background-color: #f0f7ff;'>
                <td colspan='6' style='padding: 0 8px 12px 8px;'>
                    <div class='document-connection-line'>
                        Connected to <strong>{selected_folder['name']}</strong> 
                        (Filed: {selected_folder['date'] if selected_folder['date'] else 'N/A'})
                    </div>
                </td>
            </tr>
            """
    
    table_html += "</tbody></table>"
    
    # Display the table
    st.markdown(table_html, unsafe_allow_html=True)
    
    # Provide a note about visualization
    st.info("📌 Select a document from the left panel to see its connections to case events.", icon="ℹ️")
    
    # Add a timeline visualization (optional enhancement)
    if st.checkbox("Show Timeline Visualization", value=False):
        # Convert dates for timeline
        timeline_data = []
        for event in events:
            # Handle date ranges
            if "-" in event['date'] and "present" not in event['date']:
                start, end = event['date'].split("-")
                timeline_data.append({
                    "Task": event['event'], 
                    "Start": start.strip(), 
                    "Finish": end.strip(),
                    "Party": event['party']
                })
            elif "present" in event['date']:
                # For ranges to present, use today's date
                start = event['date'].split("-")[0].strip()
                timeline_data.append({
                    "Task": event['event'], 
                    "Start": start, 
                    "Finish": "2025",
                    "Party": event['party']
                })
            else:
                # For single dates
                timeline_data.append({
                    "Task": event['event'], 
                    "Start": event['date'], 
                    "Finish": event['date'],
                    "Party": event['party']
                })
        
        df_timeline = pd.DataFrame(timeline_data)
        
        # Create colors
        colors = {'Appellant': '#3b82f6', 'Respondent': '#ef4444'}
        
        fig = px.timeline(
            df_timeline, 
            x_start="Start", 
            x_end="Finish", 
            y="Task",
            color="Party",
            color_discrete_map=colors,
            title="Case Timeline"
        )
        
        fig.update_layout(
            xaxis_title="",
            yaxis_title="",
            height=400,
            xaxis=dict(
                type='category'
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
