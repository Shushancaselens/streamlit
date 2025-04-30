import streamlit as st
import pandas as pd

# Set page config to match CaseLens layout
st.set_page_config(layout="wide", page_title="CaseLens")

# Custom CSS to EXACTLY match the CaseLens interface from the screenshots
st.markdown("""
<style>
    /* Reset and base styles */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #212529;
        background-color: #fff;
    }
    
    /* Headers match exactly as in screenshot */
    h1 {
        font-size: 32px;
        font-weight: 600;
        margin-bottom: 24px;
        color: #333;
    }
    h2 {
        font-size: 24px;
        font-weight: 500;
        margin-top: 16px;
        margin-bottom: 16px;
        color: #333;
    }
    
    /* Sidebar styling to match the screenshot */
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
    
    /* Table styling to exactly match the screenshot */
    table {
        width: 100%;
        border-collapse: collapse;
        border: none;
        margin-bottom: 20px;
        font-size: 14px;
    }
    thead {
        background-color: white;
    }
    th {
        border-bottom: 1px solid #ddd;
        padding: 12px 16px;
        text-align: left;
        font-weight: 500;
        color: #333;
    }
    td {
        padding: 12px 16px;
        text-align: left;
        border-bottom: 1px solid #eee;
    }
    tr:nth-child(even) {
        background-color: #fafafa;
    }
    tr:nth-child(odd) {
        background-color: white;
    }
    
    /* Tab styling to match the screenshot */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background-color: #f8f9fa;
        border-bottom: 1px solid #dee2e6;
        padding-left: 0;
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px;
        padding: 10px 16px;
        font-weight: 400;
        color: #333;
        background-color: transparent;
        border: none;
        margin-right: 2px;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 2px solid #4285F4;
        font-weight: 500;
        color: #4285F4;
    }
    
    /* Button styling to match the screenshot */
    .copy-export-container {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        margin-bottom: 12px;
    }
    .copy-btn, .export-btn {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 8px 12px;
        font-size: 14px;
        display: flex;
        align-items: center;
        cursor: pointer;
    }
    
    /* Party styling to exactly match the screenshot */
    .appellant {
        background-color: rgba(66, 133, 244, 0.1);
        color: rgb(66, 133, 244);
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 13px;
        font-weight: 500;
    }
    .respondent {
        background-color: rgba(244, 67, 54, 0.1);
        color: rgb(244, 67, 54);
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 13px;
        font-weight: 500;
    }
    
    /* Status styling to match the screenshot */
    .disputed {
        color: rgb(244, 67, 54);
        font-weight: 500;
    }
    .undisputed {
        color: #333;
        font-weight: 500;
    }
    
    /* Evidence styling to exactly match the screenshot */
    .evidence-tag {
        font-weight: 500;
        font-family: monospace;
    }
    .evidence-c {
        color: rgb(244, 67, 54);
    }
    .evidence-r {
        color: rgb(244, 67, 54);
    }
    
    /* Document folder styling to match the screenshot */
    .folder {
        display: flex;
        align-items: center;
        padding: 10px 12px;
        background-color: transparent;
        margin-bottom: 2px;
        cursor: pointer;
    }
    .folder:hover {
        background-color: rgba(0, 0, 0, 0.05);
    }
    .folder-icon {
        color: rgb(66, 133, 244);
        margin-right: 8px;
    }
    .folder-icon-respondent {
        color: rgb(244, 67, 54);
    }
    
    /* Hide default Streamlit elements */
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
    
    /* Document list to match screenshot */
    .doc-list {
        background-color: #fff;
        border-radius: 4px;
    }
    .doc-item {
        display: flex;
        align-items: center;
        padding: 10px;
        border-bottom: 1px solid #f2f2f2;
    }
    .doc-item:last-child {
        border-bottom: none;
    }
    .doc-item:hover {
        background-color: #f5f6f8;
    }
    .doc-icon {
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with CaseLens logo and navigation to match screenshot exactly
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 24px; padding: 12px 0;">
        <div style="background-color: rgb(66, 133, 244); width: 40px; height: 40px; display: flex; 
                justify-content: center; align-items: center; border-radius: 4px; margin-right: 10px;">
            <span style="color: white; font-weight: bold; font-size: 20px;">C</span>
        </div>
        <span style="color: rgb(66, 133, 244); font-weight: bold; font-size: 20px;">CaseLens</span>
    </div>
    
    <div style="margin-bottom: 24px;">
        <h3 style="font-size: 16px; font-weight: 500; margin-bottom: 8px; color: #333;">Legal Analysis</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation items styled to match the screenshot exactly
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: #555;">📄</span>
            <span style="color: #555;">Arguments</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: #f0f6ff; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: #555;">📊</span>
            <span style="color: #555;">Facts</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: #555;">📋</span>
            <span style="color: #555;">Exhibits</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Document folder structure to exactly match the screenshot
    st.markdown("""
    <div style="margin-top: 20px;">
        <div style="display: flex; align-items: center; padding: 10px; background-color: #f0f6ff; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>1. Statement of Appeal</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>2. Request for a Stay</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>3. Answer to Request for PM</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>4. Answer to PM</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>5. Appeal Brief</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>6. Brief on Admissibility</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>7. Reply to Objection to Admissibility</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>8. Challenge</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>ChatGPT</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>Jurisprudence</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>Objection to Admissibility</span>
        </div>
        <div style="display: flex; align-items: center; padding: 10px; background-color: white; margin-bottom: 2px; border-radius: 4px;">
            <span style="margin-right: 8px; color: rgb(66, 133, 244);">📁</span>
            <span>Swiss Court</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main content area with exact style match from screenshot
st.markdown("<h1>Summary of arguments</h1>", unsafe_allow_html=True)

# Case Facts section with title and Copy/Export buttons
st.markdown("<h2>Case Facts</h2>", unsafe_allow_html=True)
st.markdown("""
<div style="display: flex; justify-content: flex-end; gap: 8px; margin-bottom: 16px;">
    <button style="background-color: white; border: 1px solid #ddd; border-radius: 4px; padding: 6px 12px; font-size: 14px; display: flex; align-items: center;">
        <span style="margin-right: 5px;">📋</span> Copy
    </button>
    <button style="background-color: white; border: 1px solid #ddd; border-radius: 4px; padding: 6px 12px; font-size: 14px; display: flex; align-items: center;">
        <span style="margin-right: 5px;">⬇️</span> Export
    </button>
</div>
""", unsafe_allow_html=True)

# Create tabs exactly as in the screenshot
tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])

# Create case facts DataFrame exactly matching the screenshot
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

# Create DataFrames
df = pd.DataFrame(facts_data)

# Display data in the tabs with exact styling from screenshot
with tabs[0]:  # All Facts
    # Custom HTML table to exactly match the screenshot
    table_html = """
    <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
        <thead>
            <tr>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Date</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Event</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Party</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Status</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Related Argument</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Evidence</th>
            </tr>
        </thead>
        <tbody>
    """
    
    # Add rows with exact styling
    for i, row in df.iterrows():
        bg_color = "#f9f9fa" if i % 2 == 1 else "white"
        
        # Format the party tag to match screenshot exactly
        if row["Party"] == "Appellant":
            party_html = '<span style="background-color: rgba(66, 133, 244, 0.1); color: rgb(66, 133, 244); padding: 4px 8px; border-radius: 4px; font-size: 13px; font-weight: 500;">Appellant</span>'
        else:
            party_html = '<span style="background-color: rgba(244, 67, 54, 0.1); color: rgb(244, 67, 54); padding: 4px 8px; border-radius: 4px; font-size: 13px; font-weight: 500;">Respondent</span>'
        
        # Format the status to match screenshot exactly
        if row["Status"] == "Disputed":
            status_html = '<span style="color: rgb(244, 67, 54); font-weight: 500;">Disputed</span>'
        else:
            status_html = '<span style="font-weight: 500;">Undisputed</span>'
        
        # Format the evidence tag to match screenshot exactly
        evidence = row["Evidence"]
        if evidence.startswith("C-"):
            evidence_html = f'<span style="color: rgb(244, 67, 54); font-weight: 500;">{evidence}</span>'
        else:
            evidence_html = f'<span style="color: rgb(244, 67, 54); font-weight: 500;">{evidence}</span>'
        
        table_html += f"""
        <tr style="background-color: {bg_color};">
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{row["Date"]}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{row["Event"]}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{party_html}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{status_html}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{row["Related Argument"]}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{evidence_html}</td>
        </tr>
        """
    
    table_html += """
        </tbody>
    </table>
    """
    
    st.markdown(table_html, unsafe_allow_html=True)

with tabs[1]:  # Disputed Facts
    # Filter for disputed facts
    disputed_df = df[df['Status'] == 'Disputed']
    
    # Custom HTML table for disputed facts
    table_html = """
    <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
        <thead>
            <tr>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Date</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Event</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Party</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Status</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Related Argument</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Evidence</th>
            </tr>
        </thead>
        <tbody>
    """
    
    # Add rows with exact styling
    for i, row in disputed_df.iterrows():
        bg_color = "#f9f9fa" if i % 2 == 1 else "white"
        
        # Format the party tag to match screenshot exactly
        if row["Party"] == "Appellant":
            party_html = '<span style="background-color: rgba(66, 133, 244, 0.1); color: rgb(66, 133, 244); padding: 4px 8px; border-radius: 4px; font-size: 13px; font-weight: 500;">Appellant</span>'
        else:
            party_html = '<span style="background-color: rgba(244, 67, 54, 0.1); color: rgb(244, 67, 54); padding: 4px 8px; border-radius: 4px; font-size: 13px; font-weight: 500;">Respondent</span>'
        
        # Format the evidence tag to match screenshot exactly
        evidence = row["Evidence"]
        if evidence.startswith("C-"):
            evidence_html = f'<span style="color: rgb(244, 67, 54); font-weight: 500;">{evidence}</span>'
        else:
            evidence_html = f'<span style="color: rgb(244, 67, 54); font-weight: 500;">{evidence}</span>'
        
        table_html += f"""
        <tr style="background-color: {bg_color};">
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{row["Date"]}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{row["Event"]}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{party_html}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;"><span style="color: rgb(244, 67, 54); font-weight: 500;">Disputed</span></td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{row["Related Argument"]}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{evidence_html}</td>
        </tr>
        """
    
    table_html += """
        </tbody>
    </table>
    """
    
    st.markdown(table_html, unsafe_allow_html=True)

with tabs[2]:  # Undisputed Facts
    # Filter for undisputed facts
    undisputed_df = df[df['Status'] == 'Undisputed']
    
    # Custom HTML table for undisputed facts
    table_html = """
    <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
        <thead>
            <tr>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Date</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Event</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Party</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Status</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Related Argument</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6;">Evidence</th>
            </tr>
        </thead>
        <tbody>
    """
    
    # Add rows with exact styling
    for i, row in undisputed_df.iterrows():
        bg_color = "#f9f9fa" if i % 2 == 1 else "white"
        
        # Format the party tag to match screenshot exactly
        if row["Party"] == "Appellant":
            party_html = '<span style="background-color: rgba(66, 133, 244, 0.1); color: rgb(66, 133, 244); padding: 4px 8px; border-radius: 4px; font-size: 13px; font-weight: 500;">Appellant</span>'
        else:
            party_html = '<span style="background-color: rgba(244, 67, 54, 0.1); color: rgb(244, 67, 54); padding: 4px 8px; border-radius: 4px; font-size: 13px; font-weight: 500;">Respondent</span>'
        
        # Format the evidence tag to match screenshot exactly
        evidence = row["Evidence"]
        if evidence.startswith("C-"):
            evidence_html = f'<span style="color: rgb(244, 67, 54); font-weight: 500;">{evidence}</span>'
        else:
            evidence_html = f'<span style="color: rgb(244, 67, 54); font-weight: 500;">{evidence}</span>'
        
        table_html += f"""
        <tr style="background-color: {bg_color};">
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{row["Date"]}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{row["Event"]}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{party_html}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;"><span style="font-weight: 500;">Undisputed</span></td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{row["Related Argument"]}</td>
            <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">{evidence_html}</td>
        </tr>
        """
    
    table_html += """
        </tbody>
    </table>
    """
    
    st.markdown(table_html, unsafe_allow_html=True)

# Document-Event Connection Visualization styled to match CaseLens exactly
st.markdown("<h2>Document-Event Connections</h2>", unsafe_allow_html=True)

# Document-event connections in a table format matching CaseLens style
st.markdown("""
<div style="background-color: white; border-radius: 4px; padding: 16px; margin-bottom: 24px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
    <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
        <thead>
            <tr>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6; width: 30%;">Document</th>
                <th style="text-align: left; padding: 12px 16px; border-bottom: 1px solid #dee2e6; width: 70%;">Related Events</th>
            </tr>
        </thead>
        <tbody>
""", unsafe_allow_html=True)

# Generate document event connections
for doc in documents:
    if not doc["related_events"]:
        continue
    
    # Get related events for this document
    related_events_html = ""
    for event_date in doc["related_events"]:
        events = df[df["Date"] == event_date]
        for _, event in events.iterrows():
            # Style based on party and disputed status
            if event["Party"] == "Appellant":
                event_class = "background-color: rgba(66, 133, 244, 0.1); color: rgb(66, 133, 244);"
            else:
                event_class = "background-color: rgba(244, 67, 54, 0.1); color: rgb(244, 67, 54);"
            
            # Add border for disputed items
            if event["Status"] == "Disputed":
                event_border = "border: 1px dashed rgb(244, 67, 54);"
            else:
                event_border = ""
            
            related_events_html += f"""
            <span style="display: inline-block; margin: 2px 4px; padding: 4px 8px; border-radius: 12px; font-size: 12px; {event_class} {event_border}">
                {event_date}: {event["Event"][:30]}{"..." if len(event["Event"]) > 30 else ""}
            </span>
            """
    
    # Determine document icon and style
    if doc["type"] == "appellant":
        doc_color = "rgb(66, 133, 244)"
    elif doc["type"] == "respondent":
        doc_color = "rgb(244, 67, 54)"
    else:
        doc_color = "#555"
    
    st.markdown(f"""
    <tr>
        <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2; vertical-align: top;">
            <div style="display: flex; align-items: center;">
                <span style="color: {doc_color}; margin-right: 8px;">📁</span>
                <span>{doc["name"]}</span>
            </div>
        </td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #f2f2f2;">
            <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                {related_events_html}
            </div>
        </td>
    </tr>
    """, unsafe_allow_html=True)

st.markdown("""
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)

# Summary section - styled to match CaseLens
st.markdown("""
<div style="background-color: white; border-radius: 4px; padding: 16px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
    <h3 style="font-size: 16px; margin-bottom: 12px;">Event Legend</h3>
    <div style="display: flex; flex-wrap: wrap; gap: 16px;">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="background-color: rgba(66, 133, 244, 0.1); width: 16px; height: 16px; border-radius: 4px;"></span>
            <span>Appellant</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="background-color: rgba(244, 67, 54, 0.1); width: 16px; height: 16px; border-radius: 4px;"></span>
            <span>Respondent</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="width: 16px; height: 16px; border: 1px dashed rgb(244, 67, 54); border-radius: 4px;"></span>
            <span>Disputed Fact</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
