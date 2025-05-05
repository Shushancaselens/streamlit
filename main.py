import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")

# Custom CSS for styling tables
st.markdown("""
<style>
    .facts-table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 30px;
    }
    .facts-table th {
        background-color: #f1f3f5;
        padding: 10px;
        text-align: left;
        border-bottom: 2px solid #ccc;
    }
    .facts-table td {
        padding: 8px 10px;
        border-bottom: 1px solid #eee;
    }
    .facts-table tbody tr:hover {
        background-color: #f8f9fa;
    }
    .party-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8em;
        margin-right: 8px;
    }
    .appellant {
        background-color: #e6f2ff;
        color: #0066cc;
    }
    .respondent {
        background-color: #ffebe6;
        color: #cc3300;
    }
    .status-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8em;
        margin-right: 8px;
    }
    .disputed {
        background-color: #ffebe6;
        color: #cc3300;
    }
    .undisputed {
        background-color: #e6f7e6;
        color: #008000;
    }
    .evidence-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8em;
        background-color: #f8f9fa;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown("# Case Facts")

# Format party tag
def format_party(party):
    if party == "Appellant":
        return f'<span class="party-tag appellant">{party}</span>'
    elif party == "Respondent":
        return f'<span class="party-tag respondent">{party}</span>'
    else:
        return party

# Format status tag
def format_status(status):
    if status == "Disputed":
        return f'<span class="status-tag disputed">{status}</span>'
    elif status == "Undisputed":
        return f'<span class="status-tag undisputed">{status}</span>'
    else:
        return status

# Format evidence tag
def format_evidence(evidence):
    return f'<span class="evidence-tag">{evidence}</span>'

# Define tables with data
tables = [
    {
        "title": "Initial Registration Materials",
        "data": [
            {"Date": "1950-01-01", "Event": "Continuous operation under same name since 1950", "Party": "Appellant", "Status": "Undisputed", "Related Argument": "1. Sporting Succession", "Evidence": "C-1"},
            {"Date": "1950-01-01", "Event": "Initial registration in 1950", "Party": "Appellant", "Status": "Undisputed", "Related Argument": "1.1.1. Registration History", "Evidence": "C-2"},
        ]
    },
    {
        "title": "Trademark Opposition Filings",
        "data": [
            {"Date": "1975-01-01", "Event": "Brief administrative gap in 1975-1976", "Party": "Appellant", "Status": "Disputed", "Related Argument": "1.1.1. Registration History", "Evidence": "C-2"},
            {"Date": "1975-01-01", "Event": "Operations ceased between 1975-1976", "Party": "Respondent", "Status": "Disputed", "Related Argument": "1. Sporting Succession", "Evidence": "R-1"},
            {"Date": "2023-02-15", "Event": "Answer to PM filed", "Party": "Appellant", "Status": "Undisputed", "Related Argument": "Procedural", "Evidence": "A-5"},
            {"Date": "2023-03-20", "Event": "Objection to Admissibility filed", "Party": "Respondent", "Status": "Disputed", "Related Argument": "Procedural", "Evidence": "R-15"},
        ]
    },
    {
        "title": "Appeal Documentation",
        "data": [
            {"Date": "1950-01-01", "Event": "Consistent use of blue and white since founding", "Party": "Appellant", "Status": "Disputed", "Related Argument": "1.2. Club Colors Analysis", "Evidence": "C-4"},
            {"Date": "1970-01-01", "Event": "Minor shade variations do not affect continuity", "Party": "Appellant", "Status": "Undisputed", "Related Argument": "1.2.1. Color Variations Analysis", "Evidence": "C-5"},
            {"Date": "2023-03-01", "Event": "Appeal Brief submitted", "Party": "Appellant", "Status": "Undisputed", "Related Argument": "Substantive", "Evidence": "A-8"},
            {"Date": "2023-04-05", "Event": "Reply to Objection submitted", "Party": "Appellant", "Status": "Undisputed", "Related Argument": "Procedural", "Evidence": "A-12"},
        ]
    },
    {
        "title": "Supporting Research",
        "data": [
            {"Date": "1950-01-01", "Event": "Pre-1976 colors represented original city district", "Party": "Respondent", "Status": "Undisputed", "Related Argument": "1.2.1. Color Changes Analysis", "Evidence": "R-5"},
            {"Date": "1977-05-15", "Event": "Court ruling on trademark rights", "Party": "N/A", "Status": "Undisputed", "Related Argument": "2.1. Legal Precedents", "Evidence": "J-1"},
        ]
    },
    {
        "title": "Procedural Documents",
        "data": [
            {"Date": "1976-01-01", "Event": "Filed objection to new registration application", "Party": "Respondent", "Status": "Disputed", "Related Argument": "1.1.2. Legal Identity", "Evidence": "R-3"},
            {"Date": "2023-01-10", "Event": "Statement of Appeal filed", "Party": "Appellant", "Status": "Undisputed", "Related Argument": "Procedural", "Evidence": "A-1"},
            {"Date": "2023-01-25", "Event": "Request for stay submitted", "Party": "Respondent", "Status": "Undisputed", "Related Argument": "Procedural", "Evidence": "R-10"},
        ]
    }
]

# Display each table
for table in tables:
    # Display title
    st.markdown(f"## {table['title']}")
    
    # Create DataFrame
    df = pd.DataFrame(table['data'])
    
    # Apply formatting
    df["Party"] = df["Party"].apply(format_party)
    df["Status"] = df["Status"].apply(format_status)
    df["Evidence"] = df["Evidence"].apply(format_evidence)
    
    # Convert to HTML table
    html_table = df.to_html(escape=False, index=False)
    html_table = html_table.replace('<table border="1" class="dataframe">', '<table class="facts-table">')
    
    # Display the table
    st.markdown(html_table, unsafe_allow_html=True)
    
    # Add spacing between tables
    st.markdown("<br>", unsafe_allow_html=True)
