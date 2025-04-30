import streamlit as st
import pandas as pd

# Set page config to match CaseLens layout
st.set_page_config(layout="wide", page_title="CaseLens")

# Custom CSS to exactly match the CaseLens interface
st.markdown("""
<style>
    /* Main layout and colors */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #212529;
        background-color: #f8f9fa;
    }
    h1 {
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        color: #212529;
    }
    h2 {
        font-size: 1.4rem;
        font-weight: 500;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
        color: #212529;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #f5f6f8;
    }
    .sidebar-title {
        display: flex;
        align-items: center;
        margin-bottom: 2rem;
    }
    .logo-container {
        background-color: #4285F4;
        width: 40px;
        height: 40px;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 8px;
        margin-right: 10px;
    }
    .logo-text {
        color: #4285F4;
        font-weight: bold;
        font-size: 24px;
    }
    
    /* Table styling */
    table {
        width: 100%;
        border-collapse: collapse;
    }
    thead tr {
        border-bottom: 1px solid #dee2e6;
    }
    th {
        background-color: #fff;
        font-weight: 500;
        text-align: left;
        padding: 12px 8px;
    }
    td {
        padding: 12px 8px;
        text-align: left;
        border-top: 1px solid #f2f2f2;
    }
    tr:nth-child(even) {
        background-color: #fbfbfb;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        border-bottom: 1px solid #dee2e6;
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 400;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 2px solid #4285F4;
        font-weight: 500;
    }
    
    /* Button styling */
    .stButton button {
        background-color: white;
        border: 1px solid #d0d7de;
        border-radius: 6px;
        padding: 8px 16px;
        font-size: 14px;
        color: #24292f;
    }
    .copy-export-container {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        margin-bottom: 12px;
    }
    
    /* Party styling */
    .appellant {
        background-color: rgba(66, 133, 244, 0.1);
        color: #4285F4;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 500;
    }
    .respondent {
        background-color: rgba(244, 67, 54, 0.1);
        color: #F44336;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 500;
    }
    
    /* Status styling */
    .disputed {
        color: #F44336;
        font-weight: 500;
    }
    .undisputed {
        color: #24292f;
        font-weight: 500;
    }
    
    /* Evidence styling */
    .evidence-tag {
        color: #F44336;
        font-weight: 500;
        font-family: monospace;
    }
    .evidence-tag-c {
        color: #F44336;
    }
    .evidence-tag-r {
        color: #FF9800;
    }
    
    /* Document folder styling */
    .folder {
        display: flex;
        align-items: center;
        padding: 8px 16px;
        background-color: white;
        margin-bottom: 2px;
        border-radius: 4px;
        cursor: pointer;
    }
    .folder:hover {
        background-color: #f0f6ff;
    }
    .folder-appellant {
        background-color: rgba(66, 133, 244, 0.1);
    }
    .folder-respondent {
        background-color: rgba(244, 67, 54, 0.1);
    }
    .folder-icon {
        color: #4285F4;
        margin-right: 8px;
    }
    .folder-icon-respondent {
        color: #F44336;
    }
    
    /* Document-event connection styling */
    .connection-container {
        background-color: white;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 16px;
    }
    .connection-header {
        font-weight: 500;
        margin-bottom: 12px;
        display: flex;
        justify-content: space-between;
    }
    .connection-item {
        display: flex;
        padding: 12px;
        border-bottom: 1px solid #f2f2f2;
        align-items: center;
    }
    .connection-document {
        width: 30%;
        font-weight: 500;
        display: flex;
        align-items: center;
    }
    .connection-events {
        width: 70%;
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    .connection-event {
        background-color: #f2f2f2;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 12px;
    }
    .connection-event-appellant {
        background-color: rgba(66, 133, 244, 0.1);
        color: #4285F4;
    }
    .connection-event-respondent {
        background-color: rgba(244, 67, 54, 0.1);
        color: #F44336;
    }
    .connection-event-disputed {
        border: 1px dashed #F44336;
    }
    
    /* Hide default elements */
    div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
    }
    div[data-testid="stDecoration"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
    }
    footer {
        visibility: hidden;
    }
    
    /* Document connections matrix */
    .matrix-container {
        overflow-x: auto;
        background-color: white;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .matrix-table {
        width: 100%;
        border-collapse: collapse;
    }
    .matrix-table th {
        background-color: #f5f6f8;
        padding: 8px;
        text-align: center;
        font-weight: 500;
        font-size: 13px;
    }
    .matrix-table td {
        padding: 8px;
        text-align: center;
        border: 1px solid #f2f2f2;
    }
    .matrix-connected {
        background-color: rgba(66, 133, 244, 0.2);
        color: #4285F4;
        font-weight: bold;
    }
    .matrix-connected-respondent {
        background-color: rgba(244, 67, 54, 0.2);
        color: #F44336;
        font-weight: bold;
    }
    .matrix-disputed {
        border: 2px dashed #F44336;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with CaseLens logo and navigation
with st.sidebar:
    st.markdown("""
    <div class="sidebar-title">
        <div class="logo-container">
            <span style="color: white; font-weight: bold; font-size: 20px;">C</span>
        </div>
        <span class="logo-text">CaseLens</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
    
    # Navigation items styled to match the screenshot
    st.markdown("""
    <div>
        <div class="folder">
            <span style="margin-right: 8px;">📄</span> Arguments
        </div>
        <div class="folder" style="background-color: rgba(66, 133, 244, 0.1);">
            <span style="margin-right: 8px;">📊</span> Facts
        </div>
        <div class="folder">
            <span style="margin-right: 8px;">📋</span> Exhibits
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Document folder structure
    st.markdown("<h4 style='margin-top: 20px;'>Case Documents</h4>", unsafe_allow_html=True)
    
    # Appellant documents
    st.markdown("""
    <div>
        <div class="folder folder-appellant">
            <span class="folder-icon">📁</span> 1. Statement of Appeal
        </div>
        <div class="folder">
            <span class="folder-icon folder-icon-respondent">📁</span> 2. Request for a Stay
        </div>
        <div class="folder">
            <span class="folder-icon folder-icon-respondent">📁</span> 3. Answer to Request for PM
        </div>
        <div class="folder">
            <span class="folder-icon folder-icon-respondent">📁</span> 4. Answer to PM
        </div>
        <div class="folder folder-appellant">
            <span class="folder-icon">📁</span> 5. Appeal Brief
        </div>
        <div class="folder folder-appellant">
            <span class="folder-icon">📁</span> 6. Brief on Admissibility
        </div>
        <div class="folder folder-appellant">
            <span class="folder-icon">📁</span> 7. Reply to Objection to Admissibility
        </div>
        <div class="folder folder-appellant">
            <span class="folder-icon">📁</span> 8. Challenge
        </div>
        <div class="folder">
            <span class="folder-icon">📁</span> ChatGPT
        </div>
        <div class="folder">
            <span class="folder-icon">📁</span> Jurisprudence
        </div>
        <div class="folder">
            <span class="folder-icon folder-icon-respondent">📁</span> Objection to Admissibility
        </div>
        <div class="folder">
            <span class="folder-icon">📁</span> Swiss Court
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main content area
st.markdown("<h1>Summary of arguments</h1>", unsafe_allow_html=True)

# Case Facts section with title and Copy/Export buttons
st.markdown("<h2>Case Facts</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="copy-export-container">
    <button class="copy-btn">
        <span style="margin-right: 5px;">📋</span> Copy
    </button>
    <button class="export-btn">
        <span style="margin-right: 5px;">⬇️</span> Export
    </button>
</div>
""", unsafe_allow_html=True)

# Create tabs for All Facts, Disputed Facts, Undisputed Facts
tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])

# Case facts data exactly matching the screenshot
facts_data = {
    "Date": ["1950-present", "1950", "1950-present", "1950-1975", "1970-1980", "1975-1976", "1975-1976"],
    "Event": [
        "Continuous operation under same name since 1950",
        "Initial registration in 1950",
        "Consistent use of blue and white since founding",
        "Pre-1976 colors represented original city district",
        "Minor shade variations do not affect continuity",
        "Brief administrative gap in 1975-1976",
        "Operations ceased between 1975-1976"
    ],
    "Party": ["Appellant", "Appellant", "Appellant", "Respondent", "Appellant", "Appellant", "Respondent"],
    "Status": ["Undisputed", "Undisputed", "Disputed", "Undisputed", "Undisputed", "Disputed", "Disputed"],
    "Related Argument": [
        "1. Sporting Succession",
        "1.1.1. Registration History",
        "1.2. Club Colors Analysis",
        "1.2.1. Color Changes Analysis",
        "1.2.1. Color Variations Analysis",
        "1.1.1. Registration History",
        "1. Sporting Succession"
    ],
    "Evidence": ["C-1", "C-2", "C-4", "R-5", "C-5", "C-2", "R-1"]
}

# Document structure with related events
documents = [
    {"name": "1. Statement of Appeal", "type": "appellant", "related_events": ["1950-present", "1950"]},
    {"name": "2. Request for a Stay", "type": "respondent", "related_events": ["1950-1975"]},
    {"name": "3. Answer to Request for PM", "type": "respondent", "related_events": ["1950-1975"]},
    {"name": "4. Answer to PM", "type": "respondent", "related_events": ["1970-1980"]},
    {"name": "5. Appeal Brief", "type": "appellant", "related_events": ["1950-present"]},
    {"name": "6. Brief on Admissibility", "type": "appellant", "related_events": ["1950-present", "1970-1980"]},
    {"name": "7. Reply to Objection to Admissibility", "type": "appellant", "related_events": ["1975-1976"]},
    {"name": "8. Challenge", "type": "appellant", "related_events": []},
    {"name": "ChatGPT", "type": "other", "related_events": []},
    {"name": "Jurisprudence", "type": "other", "related_events": []},
    {"name": "Objection to Admissibility", "type": "respondent", "related_events": ["1975-1976"]},
    {"name": "Swiss Court", "type": "other", "related_events": []}
]

# Create a DataFrame
df = pd.DataFrame(facts_data)

# Display data in the tabs
with tabs[0]:  # All Facts
    # Format the DataFrame to match the exact styling from the screenshot
    html_table = df.to_html(index=False, escape=False)
    
    # Replace with styled content
    html_table = html_table.replace('<td>Appellant</td>', '<td><span class="appellant">Appellant</span></td>')
    html_table = html_table.replace('<td>Respondent</td>', '<td><span class="respondent">Respondent</span></td>')
    html_table = html_table.replace('<td>Disputed</td>', '<td><span class="disputed">Disputed</span></td>')
    html_table = html_table.replace('<td>Undisputed</td>', '<td><span class="undisputed">Undisputed</span></td>')
    
    # Format evidence tags with color
    for i, evidence in enumerate(["C-1", "C-2", "C-4", "R-5", "C-5", "C-2", "R-1"]):
        if evidence.startswith("C-"):
            html_table = html_table.replace(f'<td>{evidence}</td>', f'<td><span class="evidence-tag evidence-tag-c">{evidence}</span></td>')
        else:
            html_table = html_table.replace(f'<td>{evidence}</td>', f'<td><span class="evidence-tag evidence-tag-r">{evidence}</span></td>')
    
    st.markdown(f"""
    <div style="overflow-x: auto;">
        {html_table}
    </div>
    """, unsafe_allow_html=True)

with tabs[1]:  # Disputed Facts
    disputed_df = df[df['Status'] == 'Disputed']
    
    html_table = disputed_df.to_html(index=False, escape=False)
    
    # Replace with styled content
    html_table = html_table.replace('<td>Appellant</td>', '<td><span class="appellant">Appellant</span></td>')
    html_table = html_table.replace('<td>Respondent</td>', '<td><span class="respondent">Respondent</span></td>')
    html_table = html_table.replace('<td>Disputed</td>', '<td><span class="disputed">Disputed</span></td>')
    
    # Format evidence tags with color
    for evidence in ["C-4", "C-2", "R-1"]:
        if evidence.startswith("C-"):
            html_table = html_table.replace(f'<td>{evidence}</td>', f'<td><span class="evidence-tag evidence-tag-c">{evidence}</span></td>')
        else:
            html_table = html_table.replace(f'<td>{evidence}</td>', f'<td><span class="evidence-tag evidence-tag-r">{evidence}</span></td>')
    
    st.markdown(f"""
    <div style="overflow-x: auto;">
        {html_table}
    </div>
    """, unsafe_allow_html=True)

with tabs[2]:  # Undisputed Facts
    undisputed_df = df[df['Status'] == 'Undisputed']
    
    html_table = undisputed_df.to_html(index=False, escape=False)
    
    # Replace with styled content
    html_table = html_table.replace('<td>Appellant</td>', '<td><span class="appellant">Appellant</span></td>')
    html_table = html_table.replace('<td>Respondent</td>', '<td><span class="respondent">Respondent</span></td>')
    html_table = html_table.replace('<td>Undisputed</td>', '<td><span class="undisputed">Undisputed</span></td>')
    
    # Format evidence tags with color
    for evidence in ["C-1", "C-2", "R-5", "C-5"]:
        if evidence.startswith("C-"):
            html_table = html_table.replace(f'<td>{evidence}</td>', f'<td><span class="evidence-tag evidence-tag-c">{evidence}</span></td>')
        else:
            html_table = html_table.replace(f'<td>{evidence}</td>', f'<td><span class="evidence-tag evidence-tag-r">{evidence}</span></td>')
    
    st.markdown(f"""
    <div style="overflow-x: auto;">
        {html_table}
    </div>
    """, unsafe_allow_html=True)

# Document-Event Connection Visualization (custom section)
st.markdown("<h2>Document-Event Connections</h2>", unsafe_allow_html=True)

# Connection display for each document
st.markdown("""
<div class="connection-container">
    <div class="connection-header">
        <span>Document</span>
        <span>Connected Events</span>
    </div>
""", unsafe_allow_html=True)

# Iterate through documents with related events
for doc in documents:
    if not doc["related_events"]:
        continue
    
    # Get related events for this document
    related_events_html = ""
    for event_date in doc["related_events"]:
        events = df[df["Date"] == event_date]
        for _, event in events.iterrows():
            event_class = "connection-event-appellant" if event["Party"] == "Appellant" else "connection-event-respondent"
            disputed_class = "connection-event-disputed" if event["Status"] == "Disputed" else ""
            related_events_html += f'<span class="connection-event {event_class} {disputed_class}">{event_date}: {event["Event"][:30]}{"..." if len(event["Event"]) > 30 else ""}</span>'
    
    # Determine document class based on type
    doc_class = ""
    icon_class = "folder-icon"
    if doc["type"] == "appellant":
        doc_class = "connection-document-appellant"
        icon_class = "folder-icon"
    elif doc["type"] == "respondent":
        doc_class = "connection-document-respondent"
        icon_class = "folder-icon-respondent"
    
    st.markdown(f"""
    <div class="connection-item">
        <div class="connection-document {doc_class}">
            <span class="{icon_class}" style="margin-right:8px;">📁</span>
            {doc["name"]}
        </div>
        <div class="connection-events">
            {related_events_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Document-Event Matrix visualization
st.markdown("<h2>Document-Event Matrix</h2>", unsafe_allow_html=True)

# Create a matrix to show all connections
st.markdown('<div class="matrix-container">', unsafe_allow_html=True)

# Events for column headers
events = []
for date in facts_data["Date"]:
    matching_events = df[df["Date"] == date]
    for _, event in matching_events.iterrows():
        events.append({
            "date": event["Date"],
            "name": event["Event"],
            "party": event["Party"],
            "status": event["Status"]
        })

# Generate HTML for matrix
matrix_html = '<table class="matrix-table"><tr><th>Document / Event</th>'
for event in events:
    matrix_html += f'<th>{event["date"]}<br/>{event["name"][:20]}...</th>'
matrix_html += '</tr>'

# Rows for each document
for doc in documents:
    if doc["type"] == "other":
        continue
    
    matrix_html += f'<tr><td><span class="{"folder-icon" if doc["type"] == "appellant" else "folder-icon-respondent"}" style="margin-right:8px;">📁</span> {doc["name"]}</td>'
    
    # Check each event for connection
    for event in events:
        is_connected = event["date"] in doc["related_events"]
        is_disputed = event["status"] == "Disputed"
        
        if is_connected:
            cell_class = "matrix-connected" if doc["type"] == "appellant" else "matrix-connected-respondent"
            disputed_class = "matrix-disputed" if is_disputed else ""
            matrix_html += f'<td class="{cell_class} {disputed_class}">✓</td>'
        else:
            matrix_html += '<td></td>'
    
    matrix_html += '</tr>'

matrix_html += '</table>'
st.markdown(matrix_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Legend for the visualizations
st.markdown("""
<div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top: 20px; background-color: white; padding: 16px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
    <div style="display: flex; align-items: center; gap: 8px;">
        <span class="appellant" style="width:12px; height:12px; border-radius:50%; display:inline-block;"></span>
        <span>Appellant Document</span>
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
        <span class="respondent" style="width:12px; height:12px; border-radius:50%; display:inline-block;"></span>
        <span>Respondent Document</span>
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
        <span style="width:12px; height:12px; border:2px dashed #F44336; border-radius:50%; display:inline-block;"></span>
        <span>Disputed Fact</span>
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
        <span class="evidence-tag-c" style="font-weight:bold;">C-#</span>
        <span>Appellant Evidence</span>
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
        <span class="evidence-tag-r" style="font-weight:bold;">R-#</span>
        <span>Respondent Evidence</span>
    </div>
</div>
""", unsafe_allow_html=True)
