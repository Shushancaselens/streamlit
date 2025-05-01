import streamlit as st
import pandas as pd
from datetime import datetime
import json

st.set_page_config(layout="wide")

# Custom CSS to match the design in screenshot
st.markdown("""
<style>
    .main {
        background-color: #F8F9FA;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: white;
        border-radius: 4px 4px 0 0;
        padding: 0px 20px;
        font-size: 14px;
    }
    .stTabs [aria-selected="true"] {
        background-color: white;
        border-bottom: 2px solid #4285F4;
    }
    .stTabs [data-baseweb="tab-panel"] {
        background-color: white;
        border-radius: 0 0 4px 4px;
        padding: 20px;
    }
    div[data-testid="stVerticalBlock"] > div:first-child {
        background-color: white;
        padding: 20px;
        border-radius: 4px;
        margin-bottom: 20px;
    }
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    .header-title {
        font-size: 24px;
        font-weight: 600;
        color: #202124;
    }
    .header-buttons {
        display: flex;
        gap: 10px;
    }
    .header-button {
        background-color: white;
        border: 1px solid #DADCE0;
        color: #202124;
        padding: 8px 16px;
        border-radius: 4px;
        font-size: 14px;
        cursor: pointer;
    }
    .appellant {
        background-color: #E8F0FE;
        color: #1A73E8;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
    }
    .respondent {
        background-color: #FEE8E6;
        color: #D93025;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
    }
    .status-disputed {
        color: #D93025;
    }
    .status-undisputed {
        color: #202124;
    }
    .evidence-tag {
        background-color: #FEF7E0;
        color: #F29900;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 12px;
    }
    .folder-item {
        display: flex;
        align-items: center;
        padding: 10px;
        border-radius: 4px;
        margin-bottom: 5px;
        cursor: pointer;
    }
    .folder-item:hover {
        background-color: #F1F3F4;
    }
    .folder-icon {
        color: #4285F4;
        margin-right: 10px;
        font-size: 18px;
    }
    .folder-appellant {
        border-left: 3px solid #1A73E8;
    }
    .folder-respondent {
        border-left: 3px solid #D93025;
    }
    .connected-item {
        background-color: #E8F0FE;
    }
    .timeline-container {
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Sample data for document folders
documents = [
    {"id": 1, "name": "1. Statement of Appeal", "type": "appellant", "date": "1950-03-15", "connected_to": [2]},
    {"id": 2, "name": "2. Request for a Stay", "type": "respondent", "date": "1950-04-20", "connected_to": [1]},
    {"id": 3, "name": "3. Answer to Request for PM", "type": "appellant", "date": "1950-05-10", "connected_to": [4]},
    {"id": 4, "name": "4. Answer to PM", "type": "respondent", "date": "1950-06-05", "connected_to": [3]},
    {"id": 5, "name": "5. Appeal Brief", "type": "appellant", "date": "1970-08-15", "connected_to": []},
    {"id": 6, "name": "6. Brief on Admissibility", "type": "respondent", "date": "1970-09-25", "connected_to": [7]},
    {"id": 7, "name": "7. Reply to Objection to Admissibility", "type": "appellant", "date": "1970-10-30", "connected_to": [6]},
    {"id": 8, "name": "8. Challenge", "type": "appellant", "date": "1975-01-15", "connected_to": []},
    {"id": 9, "name": "ChatGPT", "type": "other", "date": "", "connected_to": []},
    {"id": 10, "name": "Jurisprudence", "type": "other", "date": "", "connected_to": []},
    {"id": 11, "name": "Objection to Admissibility", "type": "respondent", "date": "1970-09-15", "connected_to": [7]},
    {"id": 12, "name": "Swiss Court", "type": "other", "date": "", "connected_to": []},
]

# Sample case facts data
case_facts = [
    {"date": "1950-present", "event": "Continuous operation under same name since 1950", "party": "Appellant", "status": "Undisputed", "related_argument": "1. Sporting Succession", "evidence": "C-1", "document_id": 1},
    {"date": "1950", "event": "Initial registration in 1950", "party": "Appellant", "status": "Undisputed", "related_argument": "1.1.1. Registration History", "evidence": "C-2", "document_id": 1},
    {"date": "1950-present", "event": "Consistent use of blue and white since founding", "party": "Appellant", "status": "Disputed", "related_argument": "1.2. Club Colors Analysis", "evidence": "C-4", "document_id": 5},
    {"date": "1950-1975", "event": "Pre-1976 colors represented original city district", "party": "Respondent", "status": "Undisputed", "related_argument": "1.2.1. Color Changes Analysis", "evidence": "R-5", "document_id": 6},
    {"date": "1970-1980", "event": "Minor shade variations do not affect continuity", "party": "Appellant", "status": "Undisputed", "related_argument": "1.2.1. Color Variations Analysis", "evidence": "C-5", "document_id": 7},
    {"date": "1975-1976", "event": "Brief administrative gap in 1975-1976", "party": "Appellant", "status": "Disputed", "related_argument": "1.1.1. Registration History", "evidence": "C-2", "document_id": 8},
    {"date": "1975-1976", "event": "Operations ceased between 1975-1976", "party": "Respondent", "status": "Disputed", "related_argument": "1. Sporting Succession", "evidence": "R-3", "document_id": 2},
]

# Convert to DataFrame for easier manipulation
df_documents = pd.DataFrame(documents)
df_case_facts = pd.DataFrame(case_facts)

# Function to display the party badge
def display_party_badge(party):
    if party == "Appellant":
        return f'<span class="appellant">{party}</span>'
    elif party == "Respondent":
        return f'<span class="respondent">{party}</span>'
    else:
        return party

# Function to display the status
def display_status(status):
    if status == "Disputed":
        return f'<span class="status-disputed">{status}</span>'
    else:
        return f'<span class="status-undisputed">{status}</span>'

# Function to display the evidence tag
def display_evidence(evidence):
    return f'<span class="evidence-tag">{evidence}</span>'

# App title and header
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown('<div class="header-container"><div class="header-title">Summary of arguments</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="header-buttons">
        <button class="header-button">📋 Copy</button>
        <button class="header-button">📥 Export</button>
    </div>
    ''', unsafe_allow_html=True)

# Main layout with two columns
col_left, col_right = st.columns([1, 3])

# Left column - Document folders
with col_left:
    st.markdown("## Document Folders")
    
    # Store the selected document ID in session state
    if 'selected_document' not in st.session_state:
        st.session_state.selected_document = 1
    
    # Display document folders
    for doc in documents:
        doc_class = f"folder-item folder-{doc['type']}"
        if doc['id'] == st.session_state.selected_document:
            doc_class += " connected-item"
        
        st.markdown(f'''
        <div class="{doc_class}" onclick="handleFolderClick({doc['id']})">
            <span class="folder-icon">📁</span>
            <span>{doc['name']}</span>
        </div>
        ''', unsafe_allow_html=True)
    
    # JavaScript to handle folder clicks
    st.markdown('''
    <script>
    function handleFolderClick(id) {
        // This doesn't work directly in Streamlit, but in a real app, 
        // you would implement this with callbacks
        console.log("Folder clicked:", id);
    }
    </script>
    ''', unsafe_allow_html=True)
    
    # Since the JavaScript click handler won't work in Streamlit directly,
    # we'll add buttons for demonstration
    selected_doc = st.selectbox(
        "Select a document to view connections:",
        options=df_documents['id'].tolist(),
        format_func=lambda x: df_documents[df_documents['id'] == x]['name'].iloc[0],
        index=0
    )
    st.session_state.selected_document = selected_doc

# Right column - Case facts and timeline
with col_right:
    st.markdown("## Case Facts")
    
    # Tabs for different fact views
    tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
    
    with tab1:
        # Filter facts related to the selected document
        filtered_facts = df_case_facts[df_case_facts['document_id'] == st.session_state.selected_document]
        
        if not filtered_facts.empty:
            # Create a table of case facts
            st.markdown('''
            <table style="width:100%; border-collapse: collapse;">
                <tr>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Date</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Event</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Party</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Status</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Related Argument</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Evidence</th>
                </tr>
            ''', unsafe_allow_html=True)
            
            for _, fact in filtered_facts.iterrows():
                st.markdown(f'''
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['date']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['event']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_party_badge(fact['party'])}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_status(fact['status'])}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['related_argument']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_evidence(fact['evidence'])}</td>
                </tr>
                ''', unsafe_allow_html=True)
            
            st.markdown('</table>', unsafe_allow_html=True)
            
            # Show connected documents
            selected_doc_data = df_documents[df_documents['id'] == st.session_state.selected_document].iloc[0]
            if selected_doc_data['connected_to']:
                st.markdown("### Connected Documents")
                for connected_id in selected_doc_data['connected_to']:
                    connected_doc = df_documents[df_documents['id'] == connected_id].iloc[0]
                    st.markdown(f'''
                    <div class="folder-item folder-{connected_doc['type']}">
                        <span class="folder-icon">🔗</span>
                        <span>{connected_doc['name']}</span>
                    </div>
                    ''', unsafe_allow_html=True)
        else:
            st.info(f"No case facts directly linked to the selected document: {df_documents[df_documents['id'] == st.session_state.selected_document]['name'].iloc[0]}")
            
            # Show all facts for demonstration
            st.markdown("### All Case Facts")
            st.markdown('''
            <table style="width:100%; border-collapse: collapse;">
                <tr>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Date</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Event</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Party</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Status</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Related Argument</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Evidence</th>
                </tr>
            ''', unsafe_allow_html=True)
            
            for _, fact in df_case_facts.iterrows():
                st.markdown(f'''
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['date']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['event']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_party_badge(fact['party'])}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_status(fact['status'])}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['related_argument']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_evidence(fact['evidence'])}</td>
                </tr>
                ''', unsafe_allow_html=True)
            
            st.markdown('</table>', unsafe_allow_html=True)
    
    with tab2:
        # Show only disputed facts
        disputed_facts = df_case_facts[(df_case_facts['status'] == "Disputed")]
        
        if not disputed_facts.empty:
            st.markdown('''
            <table style="width:100%; border-collapse: collapse;">
                <tr>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Date</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Event</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Party</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Status</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Related Argument</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Evidence</th>
                </tr>
            ''', unsafe_allow_html=True)
            
            for _, fact in disputed_facts.iterrows():
                st.markdown(f'''
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['date']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['event']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_party_badge(fact['party'])}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_status(fact['status'])}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['related_argument']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_evidence(fact['evidence'])}</td>
                </tr>
                ''', unsafe_allow_html=True)
            
            st.markdown('</table>', unsafe_allow_html=True)
        else:
            st.info("No disputed facts found.")
    
    with tab3:
        # Show only undisputed facts
        undisputed_facts = df_case_facts[(df_case_facts['status'] == "Undisputed")]
        
        if not undisputed_facts.empty:
            st.markdown('''
            <table style="width:100%; border-collapse: collapse;">
                <tr>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Date</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Event</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Party</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Status</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Related Argument</th>
                    <th style="text-align: left; padding: 10px; border-bottom: 1px solid #DADCE0;">Evidence</th>
                </tr>
            ''', unsafe_allow_html=True)
            
            for _, fact in undisputed_facts.iterrows():
                st.markdown(f'''
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['date']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['event']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_party_badge(fact['party'])}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_status(fact['status'])}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{fact['related_argument']}</td>
                    <td style="padding: 10px; border-bottom: 1px solid #DADCE0;">{display_evidence(fact['evidence'])}</td>
                </tr>
                ''', unsafe_allow_html=True)
            
            st.markdown('</table>', unsafe_allow_html=True)
        else:
            st.info("No undisputed facts found.")

    # Timeline visualization
    st.markdown("## Timeline Visualization", unsafe_allow_html=True)
    
    # Create a timeline of events
    timeline_data = df_case_facts.copy()
    
    # Convert dates to a format we can work with
    timeline_data['start_year'] = timeline_data['date'].apply(lambda x: int(x.split('-')[0]) if '-' in x else int(x))
    timeline_data['end_year'] = timeline_data['date'].apply(
        lambda x: int(x.split('-')[1]) if '-' in x and x.split('-')[1] != 'present' else 2025 if '-present' in x else int(x.split('-')[0])
    )
    
    # Calculate the timeline duration
    min_year = timeline_data['start_year'].min()
    max_year = timeline_data['end_year'].max()
    timeline_years = list(range(min_year, max_year + 1, 5))
    
    # Create the timeline visualization
    st.markdown('''
    <div class="timeline-container">
        <div style="display: flex; margin-bottom: 10px;">
    ''', unsafe_allow_html=True)
    
    # Year labels
    for year in timeline_years:
        st.markdown(f'''
        <div style="flex: 1; text-align: center;">{year}</div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Timeline bar
    st.markdown('''
    <div style="height: 5px; background-color: #DADCE0; margin-bottom: 20px; position: relative;">
    ''', unsafe_allow_html=True)
    
    # Year ticks
    for year in timeline_years:
        position = (year - min_year) / (max_year - min_year) * 100
        st.markdown(f'''
        <div style="position: absolute; top: -5px; left: {position}%; height: 15px; width: 2px; background-color: #202124;"></div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Events on timeline
    for _, event in timeline_data.iterrows():
        start_pos = (event['start_year'] - min_year) / (max_year - min_year) * 100
        end_pos = (event['end_year'] - min_year) / (max_year - min_year) * 100
        width = end_pos - start_pos
        
        color = "#1A73E8" if event['party'] == "Appellant" else "#D93025"
        border_style = "dashed" if event['status'] == "Disputed" else "solid"
        
        st.markdown(f'''
        <div style="position: relative; margin-bottom: 10px; height: 30px;">
            <div style="position: absolute; left: {start_pos}%; width: {width}%; height: 20px; 
                background-color: {color}33; border: 2px {border_style} {color}; 
                border-radius: 4px; display: flex; align-items: center; padding: 0 5px;
                overflow: hidden; white-space: nowrap; text-overflow: ellipsis;">
                <span style="font-size: 12px; color: #202124;">{event['event']}</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Explanation of the connections
st.markdown("""
## Document Connections

The visualizations above show how different documents are connected to events in the case timeline. Here are the key relationships:

1. **Appellant's Statement of Appeal** is connected to **Respondent's Request for a Stay**. 
   - Both documents are related to the establishment and continuous operation claims.

2. **Answer to Request for PM** is connected to **Answer to PM**.
   - These documents exchange arguments about procedural matters.

3. **Appeal Brief** contains arguments about club colors which are disputed.

4. **Brief on Admissibility** is connected to the **Reply to Objection to Admissibility**.
   - These documents debate technical admissibility questions.

When you select a document from the left panel, the right panel will display all the events and facts related to that document, highlighting the connections between documents and their chronological placement in the case.
""")

# Add a feature to filter events by date range
st.sidebar.markdown("## Filter Options")
min_filter_year = st.sidebar.slider("Start Year", min_value=min_year, max_value=max_year, value=min_year)
max_filter_year = st.sidebar.slider("End Year", min_value=min_year, max_value=max_year, value=max_year)

st.sidebar.markdown("## Document Types")
show_appellant = st.sidebar.checkbox("Show Appellant Documents", value=True)
show_respondent = st.sidebar.checkbox("Show Respondent Documents", value=True)
show_other = st.sidebar.checkbox("Show Other Documents", value=True)

st.sidebar.markdown("## Status Filter")
show_disputed = st.sidebar.checkbox("Show Disputed Facts", value=True)
show_undisputed = st.sidebar.checkbox("Show Undisputed Facts", value=True)

st.sidebar.markdown("""
## How to Use
1. Select a document folder from the left panel or dropdown
2. View related case facts on the right
3. See connected documents and timeline visualization
4. Use filters in the sidebar to narrow down the view
""")
