import streamlit as st
import pandas as pd
import re
from datetime import datetime
import base64
from io import BytesIO

st.set_page_config(layout="wide", page_title="CaseLens - Document Connection Analyzer")

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
    .doc-item {
        padding: 12px;
        border-radius: 4px;
        margin-bottom: 8px;
        background-color: white;
        border-left: 3px solid #dadce0;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        cursor: pointer;
        transition: all 0.2s;
    }
    .doc-item:hover {
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .doc-item-appellant {
        border-left: 3px solid #1A73E8;
    }
    .doc-item-respondent {
        border-left: 3px solid #D93025;
    }
    .doc-item-other {
        border-left: 3px solid #dadce0;
    }
    .doc-item-selected {
        background-color: #E8F0FE;
    }
    .doc-item-connected {
        border: 1px solid #1A73E8;
        background-color: #F8FBFF;
    }
    .doc-title {
        font-weight: 500;
        margin-bottom: 4px;
    }
    .doc-meta {
        display: flex;
        font-size: 12px;
        color: #5F6368;
        margin-bottom: 4px;
    }
    .doc-date {
        margin-right: 12px;
    }
    .doc-type {
        margin-right: 12px;
    }
    .doc-connection-count {
        color: #1A73E8;
        font-weight: 500;
    }
    .timeline-container {
        margin-top: 20px;
        padding: 20px;
        background-color: white;
        border-radius: 4px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .timeline-year-markers {
        display: flex;
        position: relative;
        margin-bottom: 10px;
        height: 25px;
    }
    .timeline-year-marker {
        position: absolute;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .timeline-year-marker-line {
        width: 1px;
        height: 10px;
        background-color: #5F6368;
    }
    .timeline-year-marker-text {
        font-size: 12px;
        color: #5F6368;
    }
    .timeline-line {
        height: 2px;
        background-color: #DADCE0;
        margin-bottom: 10px;
        position: relative;
    }
    .timeline-event {
        position: absolute;
        height: 60px;
        background-color: rgba(255,255,255,0.8);
        border: 1px solid #DADCE0;
        border-radius: 4px;
        padding: 6px;
        font-size: 12px;
        overflow: hidden;
        z-index: 1;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        transition: all 0.2s;
    }
    .timeline-event:hover {
        height: auto;
        min-height: 60px;
        z-index: 10;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .timeline-event-appellant {
        border-left: 3px solid #1A73E8;
    }
    .timeline-event-respondent {
        border-left: 3px solid #D93025;
    }
    .timeline-event-title {
        font-weight: 500;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .timeline-event-date {
        font-size: 10px;
        color: #5F6368;
    }
    .timeline-event-content {
        margin-top: 4px;
        font-size: 11px;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .timeline-connection {
        position: absolute;
        background-color: rgba(26, 115, 232, 0.2);
        height: 2px;
        z-index: 0;
    }
    .timeline-connection::before, .timeline-connection::after {
        content: '';
        position: absolute;
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background-color: #1A73E8;
        top: -2px;
    }
    .timeline-connection::before {
        left: -3px;
    }
    .timeline-connection::after {
        right: -3px;
    }
    .connection-diagram {
        padding: 20px;
        background-color: white;
        border-radius: 4px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .panel-title {
        font-size: 18px;
        font-weight: 500;
        margin-bottom: 16px;
        color: #202124;
    }
    .event-list {
        max-height: 300px;
        overflow-y: auto;
        padding-right: 10px;
    }
    .event-item {
        padding: 10px;
        border-bottom: 1px solid #DADCE0;
        margin-bottom: 8px;
    }
    .event-item-title {
        font-weight: 500;
        margin-bottom: 4px;
    }
    .event-item-date {
        font-size: 12px;
        color: #5F6368;
        margin-bottom: 4px;
    }
    .event-item-content {
        font-size: 14px;
    }
    .badge {
        display: inline-block;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 12px;
        margin-right: 6px;
    }
    .badge-blue {
        background-color: #E8F0FE;
        color: #1A73E8;
    }
    .badge-red {
        background-color: #FEE8E6;
        color: #D93025;
    }
    .badge-gray {
        background-color: #F1F3F4;
        color: #5F6368;
    }
    .badge-yellow {
        background-color: #FEF7E0;
        color: #F29900;
    }
    .badge-green {
        background-color: #E6F4EA;
        color: #137333;
    }
    .search-panel {
        padding: 12px;
        background-color: white;
        border-radius: 4px;
        margin-bottom: 16px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .file-uploader {
        padding: 20px;
        border: 2px dashed #DADCE0;
        border-radius: 4px;
        text-align: center;
        margin-bottom: 20px;
        background-color: #F8F9FA;
    }
    .filters-container {
        display: flex;
        gap: 10px;
        margin-bottom: 16px;
        flex-wrap: wrap;
    }
    .filter-item {
        background-color: #F1F3F4;
        padding: 6px 12px;
        border-radius: 16px;
        font-size: 14px;
        display: flex;
        align-items: center;
        cursor: pointer;
    }
    .filter-item-active {
        background-color: #E8F0FE;
        color: #1A73E8;
    }
    .filter-item:hover {
        background-color: #E8F0FE;
    }
    .connection-map {
        width: 100%;
        padding: 40px 20px;
        position: relative;
        height: 400px;
    }
    .connection-node {
        position: absolute;
        padding: 8px 12px;
        background-color: white;
        border-radius: 4px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        z-index: 2;
        max-width: 180px;
        text-align: center;
        font-size: 12px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .connection-node-appellant {
        border: 1px solid #1A73E8;
    }
    .connection-node-respondent {
        border: 1px solid #D93025;
    }
    .connection-line {
        position: absolute;
        height: 2px;
        background-color: rgba(26, 115, 232, 0.2);
        z-index: 1;
        transform-origin: left center;
    }
    .loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(255, 255, 255, 0.7);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'documents' not in st.session_state:
    # Sample documents data
    st.session_state.documents = [
        {
            "id": 1, 
            "title": "Statement of Appeal", 
            "party": "Appellant", 
            "date": "1950-03-15", 
            "type": "Statement", 
            "content": "The appellant argues continuous operation under the same name since 1950 and consistent use of club colors.",
            "exhibits": ["Exhibit A-1", "Exhibit A-2", "Exhibit A-3"],
            "events": [
                {"date": "1950-03-15", "description": "Filed Statement of Appeal", "status": "Processed"},
                {"date": "1950-present", "description": "Continuous operation under same name", "status": "Undisputed"},
                {"date": "1950", "description": "Initial registration in 1950", "status": "Undisputed"}
            ]
        },
        {
            "id": 2, 
            "title": "Request for a Stay", 
            "party": "Respondent", 
            "date": "1950-04-20", 
            "type": "Request", 
            "content": "The respondent argues that operations ceased between 1975-1976 and requests a stay of proceedings.",
            "exhibits": ["Exhibit R-1", "Exhibit R-2", "Exhibit R-3"],
            "events": [
                {"date": "1950-04-20", "description": "Filed Request for Stay", "status": "Processed"},
                {"date": "1975-1976", "description": "Operations ceased between 1975-1976", "status": "Disputed"}
            ]
        },
        {
            "id": 3, 
            "title": "Answer to Request for PM", 
            "party": "Appellant", 
            "date": "1950-05-10", 
            "type": "Answer", 
            "content": "The appellant responds to the Request for Provisional Measures.",
            "exhibits": ["Exhibit A-4", "Exhibit A-5"],
            "events": [
                {"date": "1950-05-10", "description": "Filed Answer to Request for PM", "status": "Processed"}
            ]
        },
        {
            "id": 4, 
            "title": "Answer to PM", 
            "party": "Respondent", 
            "date": "1950-06-05", 
            "type": "Answer", 
            "content": "The respondent answers regarding Provisional Measures.",
            "exhibits": ["Exhibit R-4"],
            "events": [
                {"date": "1950-06-05", "description": "Filed Answer to PM", "status": "Processed"}
            ]
        },
        {
            "id": 5, 
            "title": "Appeal Brief", 
            "party": "Appellant", 
            "date": "1970-08-15", 
            "type": "Brief", 
            "content": "The appellant submits a detailed brief arguing consistent use of blue and white since founding.",
            "exhibits": ["Exhibit A-6", "Exhibit A-7", "Exhibit A-8"],
            "events": [
                {"date": "1970-08-15", "description": "Filed Appeal Brief", "status": "Processed"},
                {"date": "1950-present", "description": "Consistent use of blue and white since founding", "status": "Disputed"}
            ]
        },
        {
            "id": 6, 
            "title": "Brief on Admissibility", 
            "party": "Respondent", 
            "date": "1970-09-25", 
            "type": "Brief", 
            "content": "The respondent argues that pre-1976 colors represented original city district.",
            "exhibits": ["Exhibit R-5", "Exhibit R-6"],
            "events": [
                {"date": "1970-09-25", "description": "Filed Brief on Admissibility", "status": "Processed"},
                {"date": "1950-1975", "description": "Pre-1976 colors represented original city district", "status": "Undisputed"}
            ]
        },
        {
            "id": 7, 
            "title": "Reply to Objection to Admissibility", 
            "party": "Appellant", 
            "date": "1970-10-30", 
            "type": "Reply", 
            "content": "The appellant argues that minor shade variations do not affect continuity.",
            "exhibits": ["Exhibit A-9", "Exhibit A-10", "Exhibit A-11"],
            "events": [
                {"date": "1970-10-30", "description": "Filed Reply to Objection", "status": "Processed"},
                {"date": "1970-1980", "description": "Minor shade variations do not affect continuity", "status": "Undisputed"}
            ]
        },
        {
            "id": 8, 
            "title": "Challenge", 
            "party": "Appellant", 
            "date": "1975-01-15", 
            "type": "Challenge", 
            "content": "The appellant acknowledges a brief administrative gap in 1975-1976 but argues it does not affect continuity.",
            "exhibits": ["Exhibit A-12"],
            "events": [
                {"date": "1975-01-15", "description": "Filed Challenge", "status": "Processed"},
                {"date": "1975-1976", "description": "Brief administrative gap in 1975-1976", "status": "Disputed"}
            ]
        },
        {
            "id": 9, 
            "title": "ChatGPT Transcript", 
            "party": "Other", 
            "date": "2023-05-20", 
            "type": "Reference", 
            "content": "Transcript of conversation about legal precedents.",
            "exhibits": [],
            "events": [
                {"date": "2023-05-20", "description": "Created ChatGPT transcript", "status": "Processed"}
            ]
        },
        {
            "id": 10, 
            "title": "Jurisprudence Collection", 
            "party": "Other", 
            "date": "2023-06-10", 
            "type": "Reference", 
            "content": "Collection of relevant jurisprudence.",
            "exhibits": [],
            "events": [
                {"date": "2023-06-10", "description": "Compiled jurisprudence", "status": "Processed"}
            ]
        },
        {
            "id": 11, 
            "title": "Objection to Admissibility", 
            "party": "Respondent", 
            "date": "1970-09-15", 
            "type": "Objection", 
            "content": "The respondent objects to the admissibility of certain exhibits.",
            "exhibits": ["Exhibit R-7"],
            "events": [
                {"date": "1970-09-15", "description": "Filed Objection to Admissibility", "status": "Processed"}
            ]
        },
        {
            "id": 12, 
            "title": "Swiss Court Decision", 
            "party": "Other", 
            "date": "1980-11-25", 
            "type": "Decision", 
            "content": "Decision of the Swiss Court regarding similar case.",
            "exhibits": [],
            "events": [
                {"date": "1980-11-25", "description": "Swiss Court issued decision", "status": "Processed"}
            ]
        },
    ]

if 'connections' not in st.session_state:
    # Sample connections data - format: [source_id, target_id, connection_type, description]
    st.session_state.connections = [
        [1, 2, "Responded To", "Request for Stay in response to Statement of Appeal"],
        [3, 4, "Responded To", "Answer to PM in response to Answer to Request for PM"],
        [5, 6, "Challenged By", "Brief on Admissibility challenges Appeal Brief claims"],
        [6, 7, "Responded To", "Reply responds to Brief on Admissibility"],
        [11, 7, "Responded To", "Reply responds to Objection to Admissibility"],
        [1, 5, "Expanded On", "Appeal Brief expands on Statement of Appeal"],
        [2, 8, "Addressed By", "Challenge addresses claims in Request for Stay"]
    ]

if 'selected_document' not in st.session_state:
    st.session_state.selected_document = 1

if 'tags' not in st.session_state:
    st.session_state.tags = {
        "parties": ["Appellant", "Respondent", "Other"],
        "document_types": ["Statement", "Request", "Answer", "Brief", "Reply", "Objection", "Challenge", "Decision", "Reference"],
        "event_status": ["Processed", "Disputed", "Undisputed"]
    }

if 'filters' not in st.session_state:
    st.session_state.filters = {
        "party": [],
        "type": [],
        "date_from": "1950-01-01",
        "date_to": "2025-01-01",
        "search": ""
    }

if 'show_timeline' not in st.session_state:
    st.session_state.show_timeline = True

if 'show_connections' not in st.session_state:
    st.session_state.show_connections = True

if 'upload_step' not in st.session_state:
    st.session_state.upload_step = "upload"  # "upload", "analyze", "complete"

# Helper functions
def display_party_badge(party):
    if party == "Appellant":
        return f'<span class="appellant">{party}</span>'
    elif party == "Respondent":
        return f'<span class="respondent">{party}</span>'
    else:
        return f'<span class="badge badge-gray">{party}</span>'

def display_status_badge(status):
    if status == "Disputed":
        return f'<span class="badge badge-red">{status}</span>'
    elif status == "Undisputed":
        return f'<span class="badge badge-green">{status}</span>'
    else:
        return f'<span class="badge badge-gray">{status}</span>'

def display_type_badge(doc_type):
    return f'<span class="badge badge-blue">{doc_type}</span>'

def get_connected_documents(doc_id):
    """Get all documents connected to the given document."""
    connected = []
    for conn in st.session_state.connections:
        if conn[0] == doc_id:
            connected.append({
                "doc_id": conn[1],
                "connection_type": conn[2],
                "description": conn[3],
                "direction": "outgoing"
            })
        elif conn[1] == doc_id:
            connected.append({
                "doc_id": conn[0],
                "connection_type": conn[2],
                "description": conn[3],
                "direction": "incoming"
            })
    return connected

def get_document_by_id(doc_id):
    """Get document by ID."""
    for doc in st.session_state.documents:
        if doc["id"] == doc_id:
            return doc
    return None

def filter_documents():
    """Filter documents based on current filters."""
    filtered_docs = st.session_state.documents.copy()
    
    # Filter by party
    if st.session_state.filters["party"]:
        filtered_docs = [doc for doc in filtered_docs if doc["party"] in st.session_state.filters["party"]]
    
    # Filter by type
    if st.session_state.filters["type"]:
        filtered_docs = [doc for doc in filtered_docs if doc["type"] in st.session_state.filters["type"]]
    
    # Filter by date range
    date_from = datetime.strptime(st.session_state.filters["date_from"], "%Y-%m-%d")
    date_to = datetime.strptime(st.session_state.filters["date_to"], "%Y-%m-%d")
    
    filtered_docs = [
        doc for doc in filtered_docs 
        if datetime.strptime(doc["date"], "%Y-%m-%d") >= date_from and 
           datetime.strptime(doc["date"], "%Y-%m-%d") <= date_to
    ]
    
    # Filter by search text
    if st.session_state.filters["search"]:
        search_term = st.session_state.filters["search"].lower()
        filtered_docs = [
            doc for doc in filtered_docs 
            if search_term in doc["title"].lower() or 
               search_term in doc["content"].lower() or
               search_term in doc["party"].lower() or
               search_term in doc["type"].lower()
        ]
    
    return filtered_docs

def detect_connections(documents):
    """Simulate detecting connections between documents based on content and chronology."""
    # This would be a sophisticated NLP function in a real application
    # Here we'll use a simple rule-based approach for the demo
    
    connections = []
    
    # Sort documents by date
    sorted_docs = sorted(documents, key=lambda x: x["date"])
    
    # Dictionary to track documents by party
    party_docs = {"Appellant": [], "Respondent": []}
    
    for doc in sorted_docs:
        if doc["party"] in ["Appellant", "Respondent"]:
            party_docs[doc["party"]].append(doc)
    
    # Find response-type connections
    response_types = {
        "Statement": ["Request", "Answer", "Objection"],
        "Request": ["Answer", "Challenge"],
        "Brief": ["Brief", "Objection"],
        "Objection": ["Reply", "Challenge"]
    }
    
    for i, doc1 in enumerate(sorted_docs):
        # Skip non-party documents
        if doc1["party"] not in ["Appellant", "Respondent"]:
            continue
            
        opposing_party = "Respondent" if doc1["party"] == "Appellant" else "Appellant"
        
        # Look for responses to this document
        for doc2 in sorted_docs[i+1:]:
            # Only consider documents from opposing party within a reasonable time frame
            date1 = datetime.strptime(doc1["date"], "%Y-%m-%d")
            date2 = datetime.strptime(doc2["date"], "%Y-%m-%d")
            days_between = (date2 - date1).days
            
            if doc2["party"] == opposing_party and days_between <= 90:  # Within 90 days
                if doc1["type"] in response_types and doc2["type"] in response_types[doc1["type"]]:
                    connections.append([
                        doc1["id"], 
                        doc2["id"], 
                        "Responded To", 
                        f"{doc2['title']} responds to {doc1['title']}"
                    ])
                    break  # Assume only one direct response
    
    # Find expansion-type connections
    for party in ["Appellant", "Respondent"]:
        party_sorted = sorted([d for d in documents if d["party"] == party], key=lambda x: x["date"])
        
        for i, doc1 in enumerate(party_sorted):
            for doc2 in party_sorted[i+1:]:
                # If later document by same party is a Brief or Reply, likely expands on earlier document
                if doc2["type"] in ["Brief", "Reply"]:
                    connections.append([
                        doc1["id"], 
                        doc2["id"], 
                        "Expanded On", 
                        f"{doc2['title']} expands on {doc1['title']}"
                    ])
                    break  # Connect to only the most recent document
    
    # Find contradiction-type connections by examining events
    for i, doc1 in enumerate(documents):
        for doc2 in documents[i+1:]:
            # Only consider documents from opposing parties
            if doc1["party"] != doc2["party"] and doc1["party"] in ["Appellant", "Respondent"] and doc2["party"] in ["Appellant", "Respondent"]:
                # Compare events for contradictions
                doc1_events = [e["description"] for e in doc1.get("events", [])]
                doc2_events = [e["description"] for e in doc2.get("events", [])]
                
                # Very simplified contradiction detection - would be more sophisticated in a real app
                for event1 in doc1_events:
                    for event2 in doc2_events:
                        if any(word in event1 and word in event2 for word in ["ceased", "gap", "continuous", "variation"]):
                            connections.append([
                                doc1["id"], 
                                doc2["id"], 
                                "Contradicts", 
                                f"{doc2['title']} contradicts event in {doc1['title']}"
                            ])
                            break
                    else:
                        continue
                    break
    
    return connections

def analyze_document_upload(uploaded_files):
    """Analyze uploaded documents to extract metadata and content."""
    # In a real application, this would use OCR, NLP, and ML to analyze documents
    # For the demo, we'll use simulated data
    
    if not uploaded_files:
        return []
    
    # Simulate document processing
    st.progress(0, "Initializing document analysis...")
    documents = []
    
    for i, file in enumerate(uploaded_files):
        # Simulate processing time
        progress = (i + 1) / len(uploaded_files)
        st.progress(progress, f"Processing document {i+1}/{len(uploaded_files)}: {file.name}")
        
        # Extract file extension and determine document type
        file_ext = file.name.split('.')[-1].lower()
        
        # Simulated document metadata extraction
        doc_id = len(st.session_state.documents) + len(documents) + 1
        doc_title = file.name.split('.')[0]
        
        # Simple rule-based classification - would be ML-based in real app
        doc_party = "Appellant" if "appellant" in file.name.lower() or "appeal" in file.name.lower() else \
                    "Respondent" if "respondent" in file.name.lower() or "response" in file.name.lower() else \
                    "Other"
        
        doc_type = "Statement" if "statement" in file.name.lower() else \
                  "Brief" if "brief" in file.name.lower() else \
                  "Request" if "request" in file.name.lower() else \
                  "Answer" if "answer" in file.name.lower() else \
                  "Objection" if "objection" in file.name.lower() else \
                  "Reply" if "reply" in file.name.lower() else \
                  "Challenge" if "challenge" in file.name.lower() else \
                  "Decision" if "decision" in file.name.lower() or "judgment" in file.name.lower() else \
                  "Reference"
        
        # Simulated content extraction
        content = f"Extracted content from {file.name}. This would be the actual document text in a real application."
        
        # Simulated date extraction - randomly between 1950 and 2023
        import random
        year = random.randint(1950, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        doc_date = f"{year}-{month:02d}-{day:02d}"
        
        # Simulated exhibits extraction
        exhibits = [f"Exhibit {doc_party[0]}-{i+1}" for i in range(random.randint(0, 3))]
        
        # Simulated events extraction
        events = [
            {
                "date": doc_date, 
                "description": f"Filed {doc_title}", 
                "status": "Processed"
            }
        ]
        
        # Add additional simulated events based on document type
        if doc_type in ["Statement", "Brief"]:
            events.append({
                "date": f"{year-random.randint(0,5)}-present",
                "description": f"{'Continuous operation' if doc_type == 'Statement' else 'Consistent practice'} since {year-random.randint(0,5)}",
                "status": random.choice(["Disputed", "Undisputed"])
            })
        
        # Create document record
        document = {
            "id": doc_id,
            "title": doc_title,
            "party": doc_party,
            "date": doc_date,
            "type": doc_type,
            "content": content,
            "exhibits": exhibits,
            "events": events
        }
        
        documents.append(document)
    
    st.progress(1.0, "Document processing complete!")
    return documents

# Main app sections
def render_header():
    """Render the application header."""
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown('<div class="header-container"><div class="header-title">Document Connection Analyzer</div></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('''
        <div class="header-buttons">
            <button class="header-button">📋 Copy</button>
            <button class="header-button">📥 Export</button>
        </div>
        ''', unsafe_allow_html=True)

def render_document_uploader():
    """Render the document upload section."""
    st.markdown('<div class="panel-title">Upload Documents</div>', unsafe_allow_html=True)
    
    uploaded_files = st.file_uploader(
        "Drag and drop documents to analyze connections", 
        accept_multiple_files=True,
        type=["pdf", "docx", "doc", "txt", "rtf"]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Process Documents", disabled=not uploaded_files):
            if uploaded_files:
                st.session_state.upload_step = "analyze"
                with st.spinner("Analyzing documents..."):
                    # Process the uploaded documents
                    new_documents = analyze_document_upload(uploaded_files)
                    
                    # Add the new documents to the session state
                    st.session_state.documents.extend(new_documents)
                    
                    # Detect connections between all documents
                    st.session_state.connections = detect_connections(st.session_state.documents)
                    
                    st.session_state.upload_step = "complete"
    
    with col2:
        if st.button("Use Demo Data"):
            # Already using demo data, so just acknowledge
            st.success("Using demo data")

def render_search_filters():
    """Render search and filter options."""
    st.markdown('<div class="panel-title">Search & Filters</div>', unsafe_allow_html=True)
    
    # Search box
    st.text_input("Search documents", key="search_input", 
                  on_change=lambda: st.session_state.filters.update({"search": st.session_state.search_input}))
    
    # Date filters
    col1, col2 = st.columns(2)
    with col1:
        date_from = st.date_input("From Date", 
                      value=datetime.strptime("1950-01-01", "%Y-%m-%d"),
                      key="date_from_input")
        st.session_state.filters["date_from"] = date_from.strftime("%Y-%m-%d")
    with col2:
        date_to = st.date_input("To Date", 
                      value=datetime.strptime("2025-01-01", "%Y-%m-%d"),
                      key="date_to_input")
        st.session_state.filters["date_to"] = date_to.strftime("%Y-%m-%d")
    
    # Party and Type filters
    st.markdown("### Filter by Party")
    parties = st.session_state.tags["parties"]
    party_cols = st.columns(len(parties))
    
    for i, party in enumerate(parties):
        with party_cols[i]:
            if st.checkbox(party, value=False, key=f"party_{party}"):
                if party not in st.session_state.filters["party"]:
                    st.session_state.filters["party"].append(party)
            else:
                if party in st.session_state.filters["party"]:
                    st.session_state.filters["party"].remove(party)
    
    st.markdown("### Filter by Document Type")
    doc_types = st.session_state.tags["document_types"]
    # Display document types in two rows for better layout
    half = len(doc_types) // 2
    
    for i in range(0, len(doc_types), half):
        type_cols = st.columns(min(half, len(doc_types) - i))
        for j, col in enumerate(type_cols):
            with col:
                idx = i + j
                if idx < len(doc_types):
                    doc_type = doc_types[idx]
                    if st.checkbox(doc_type, value=False, key=f"type_{doc_type}"):
                        if doc_type not in st.session_state.filters["type"]:
                            st.session_state.filters["type"].append(doc_type)
                    else:
                        if doc_type in st.session_state.filters["type"]:
                            st.session_state.filters["type"].remove(doc_type)
    
    # Reset filters button
    if st.button("Reset Filters"):
        st.session_state.filters = {
            "party": [],
            "type": [],
            "date_from": "1950-01-01",
            "date_to": "2025-01-01",
            "search": ""
        }
        st.session_state.search_input = ""

def render_document_list(documents):
    """Render the list of documents with connection indicators."""
    st.markdown('<div class="panel-title">Documents</div>', unsafe_allow_html=True)
    
    for doc in documents:
        # Check if this document is connected to the selected document
        connected_docs = get_connected_documents(st.session_state.selected_document)
        is_connected = any(conn["doc_id"] == doc["id"] for conn in connected_docs)
        
        # Determine document class based on selection and connection status
        doc_class = f"doc-item doc-item-{doc['party'].lower()}"
        if doc["id"] == st.session_state.selected_document:
            doc_class += " doc-item-selected"
        elif is_connected:
            doc_class += " doc-item-connected"
        
        # Count connections for this document
        connection_count = len(get_connected_documents(doc["id"]))
        
        # Render document item
        st.markdown(f'''
        <div class="{doc_class}" onclick="document.getElementById('select-doc-{doc["id"]}').click()">
            <div class="doc-title">{doc["title"]}</div>
            <div class="doc-meta">
                <div class="doc-date">{doc["date"]}</div>
                <div class="doc-type">{display_party_badge(doc["party"])}</div>
                <div>{display_type_badge(doc["type"])}</div>
            </div>
            <div>
                <span class="doc-connection-count">{connection_count} connections</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Create a clickable element and update the session state when clicked
        if st.button(f"View {doc['title']}", key=f"select-doc-{doc['id']}"):
            st.session_state.selected_document = doc["id"]

def render_document_details(doc_id):
    """Render detailed view of selected document."""
    document = get_document_by_id(doc_id)
    if not document:
        st.warning("Document not found")
        return
    
    st.markdown(f'<div class="panel-title">{document["title"]}</div>', unsafe_allow_html=True)
    
    # Document metadata
    st.markdown(f'''
    <div style="margin-bottom: 20px;">
        <div style="margin-bottom: 10px;">
            {display_party_badge(document["party"])} {display_type_badge(document["type"])}
            <span style="margin-left: 10px; color: #5F6368;">Date: {document["date"]}</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Document content
    st.markdown("### Content")
    st.write(document["content"])
    
    # Document exhibits
    if document["exhibits"]:
        st.markdown("### Exhibits")
        for exhibit in document["exhibits"]:
            st.markdown(f'<span class="badge badge-yellow">{exhibit}</span>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Document events
    if document["events"]:
        st.markdown("### Events")
        for event in document["events"]:
            st.markdown(f'''
            <div class="event-item">
                <div class="event-item-title">{event["description"]}</div>
                <div class="event-item-date">{event["date"]} • {display_status_badge(event["status"])}</div>
            </div>
            ''', unsafe_allow_html=True)

def render_connections(doc_id):
    """Render connections to the selected document."""
    st.markdown('<div class="panel-title">Connections</div>', unsafe_allow_html=True)
    
    connections = get_connected_documents(doc_id)
    
    if not connections:
        st.info("No connections found for this document")
        return
    
    for conn in connections:
        conn_doc = get_document_by_id(conn["doc_id"])
        if not conn_doc:
            continue
        
        direction_emoji = "⬅️" if conn["direction"] == "incoming" else "➡️"
        
        st.markdown(f'''
        <div class="doc-item doc-item-{conn_doc['party'].lower()}">
            <div class="doc-title">
                {direction_emoji} {conn_doc["title"]}
            </div>
            <div style="margin: 4px 0;">
                <span class="badge badge-blue">{conn["connection_type"]}</span>
                {display_party_badge(conn_doc["party"])} {display_type_badge(conn_doc["type"])}
            </div>
            <div style="margin-top: 8px; font-size: 14px;">
                {conn["description"]}
            </div>
        </div>
        ''', unsafe_allow_html=True)

def render_timeline():
    """Render a timeline visualization of documents and their connections."""
    st.markdown('<div class="panel-title">Timeline Visualization</div>', unsafe_allow_html=True)
    
    # Get all documents sorted by date
    documents = sorted(st.session_state.documents, key=lambda x: x["date"])
    
    # Calculate the date range
    start_date = datetime.strptime(documents[0]["date"], "%Y-%m-%d")
    end_date = datetime.strptime(documents[-1]["date"], "%Y-%m-%d")
    
    # Create a list of year markers (every 5 years)
    start_year = start_date.year
    end_year = end_date.year
    year_markers = list(range(start_year, end_year + 1, 5))
    
    # Render the timeline
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    
    # Render year markers
    st.markdown('<div class="timeline-year-markers">', unsafe_allow_html=True)
    for year in year_markers:
        position = (year - start_year) / (end_year - start_year + 1) * 100
        st.markdown(f'''
        <div class="timeline-year-marker" style="left: {position}%;">
            <div class="timeline-year-marker-line"></div>
            <div class="timeline-year-marker-text">{year}</div>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Render timeline line
    st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)
    
    # Render document events on timeline
    st.markdown('<div style="position: relative; height: 500px;">', unsafe_allow_html=True)
    
    # Calculate vertical positions for documents
    vertical_positions = {}
    max_overlaps = 4  # Maximum number of documents to stack vertically
    
    # First pass: calculate date positions
    for doc in documents:
        doc_date = datetime.strptime(doc["date"], "%Y-%m-%d")
        position = (doc_date.year - start_year + (doc_date.month - 1) / 12) / (end_year - start_year + 1) * 100
        vertical_positions[doc["id"]] = {"horizontal": position, "vertical": 0}
    
    # Second pass: adjust vertical positions to avoid overlaps
    for i, doc1 in enumerate(documents):
        for doc2 in documents[:i]:
            # Check if documents are close horizontally (less than 15% apart)
            if abs(vertical_positions[doc1["id"]]["horizontal"] - vertical_positions[doc2["id"]]["horizontal"]) < 15:
                # If close, increment vertical position
                vertical_positions[doc1["id"]]["vertical"] = min(
                    vertical_positions[doc2["id"]]["vertical"] + 1, 
                    max_overlaps - 1
                )
    
    # Render document markers
    for doc in documents:
        doc_date = datetime.strptime(doc["date"], "%Y-%m-%d")
        h_position = vertical_positions[doc["id"]]["horizontal"]
        v_position = vertical_positions[doc["id"]]["vertical"] * 70  # 70px vertical spacing
        
        # Highlight the selected document and its connections
        is_selected = doc["id"] == st.session_state.selected_document
        is_connected = any(conn[0] == st.session_state.selected_document and conn[1] == doc["id"] or 
                         conn[1] == st.session_state.selected_document and conn[0] == doc["id"] 
                         for conn in st.session_state.connections)
        
        highlight_class = ""
        if is_selected:
            highlight_class = "timeline-event-selected"
        elif is_connected:
            highlight_class = "timeline-event-connected"
        
        st.markdown(f'''
        <div class="timeline-event timeline-event-{doc['party'].lower()} {highlight_class}" 
             style="left: {h_position}%; top: {v_position}px; width: 200px;">
            <div class="timeline-event-title">{doc["title"]}</div>
            <div class="timeline-event-date">{doc["date"]} • {display_party_badge(doc["party"])}</div>
            <div class="timeline-event-content">{doc["content"][:100]}...</div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Render connection lines
    for conn in st.session_state.connections:
        source_id, target_id = conn[0], conn[1]
        
        # Skip connections not involving the selected document if one is selected
        if st.session_state.selected_document not in [0, source_id, target_id]:
            continue
            
        # Get positions
        if source_id not in vertical_positions or target_id not in vertical_positions:
            continue
            
        source_h = vertical_positions[source_id]["horizontal"]
        source_v = vertical_positions[source_id]["vertical"] * 70 + 30  # Center of box
        target_h = vertical_positions[target_id]["horizontal"]
        target_v = vertical_positions[target_id]["vertical"] * 70 + 30  # Center of box
        
        # Calculate line properties
        line_length = abs(target_h - source_h)
        line_angle = 0  # Horizontal line by default
        
        # Position the line
        left_pos = min(source_h, target_h)
        
        # Add curved lines in a real app, but for simplicity, use straight lines
        st.markdown(f'''
        <div class="timeline-connection" 
             style="left: {left_pos}%; top: {max(source_v, target_v)}px; width: {line_length}%;"></div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_connection_diagram():
    """Render a diagram showing connections between documents."""
    st.markdown('<div class="panel-title">Connection Diagram</div>', unsafe_allow_html=True)
    
    # Get the selected document and its connections
    selected_doc = get_document_by_id(st.session_state.selected_document)
    if not selected_doc:
        st.warning("No document selected")
        return
        
    connections = get_connected_documents(st.session_state.selected_document)
    if not connections:
        st.info("No connections found for this document")
        return
    
    # Render the connection diagram
    st.markdown('<div class="connection-map">', unsafe_allow_html=True)
    
    # Render the selected document node in the center
    st.markdown(f'''
    <div class="connection-node connection-node-{selected_doc['party'].lower()}" 
         style="top: 180px; left: 45%; transform: translate(-50%, -50%);">
        <div style="font-weight: 500;">{selected_doc["title"]}</div>
        <div style="font-size: 10px;">{selected_doc["date"]}</div>
        <div>{display_party_badge(selected_doc["party"])}</div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Render connection nodes in a circle around the center
    num_connections = len(connections)
    radius = 150  # Distance from center
    center_x = 45  # Center position (percent)
    center_y = 180  # Center position (pixels)
    
    for i, conn in enumerate(connections):
        conn_doc = get_document_by_id(conn["doc_id"])
        if not conn_doc:
            continue
            
        # Calculate position in a circle
        angle = (2 * 3.14159 * i) / num_connections
        x = center_x + radius * 0.7 * (0.6 if conn["direction"] == "incoming" else 1.3) * (i % 2 + 1) * 0.15 * (-1 if i % 2 == 0 else 1)
        y = center_y + (i * 60) - (num_connections * 30)
        
        # Render the connection node
        st.markdown(f'''
        <div class="connection-node connection-node-{conn_doc['party'].lower()}" 
             style="top: {y}px; left: {x}%; transform: translate(-50%, -50%);">
            <div style="font-weight: 500;">{conn_doc["title"]}</div>
            <div style="font-size: 10px;">{conn_doc["date"]}</div>
            <div>{display_party_badge(conn_doc["party"])}</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Render the connection line
        line_length = radius * 0.5
        line_angle = angle * (180 / 3.14159)
        
        # Render arrowhead based on direction
        arrow_emoji = "⟵" if conn["direction"] == "incoming" else "⟶"
        
        st.markdown(f'''
        <div class="connection-line" 
             style="top: {(y + center_y) / 2}px; left: {min(x, center_x)}%; 
                    width: {abs(x - center_x)}%; height: 2px;">
        </div>
        <div style="position: absolute; top: {(y + center_y) / 2 - 10}px; 
                    left: {(x + center_x) / 2}%; transform: translate(-50%, 0);
                    font-size: 16px; color: #1A73E8; font-weight: bold;">
            {arrow_emoji}
        </div>
        <div style="position: absolute; top: {(y + center_y) / 2 + 5}px; 
                    left: {(x + center_x) / 2}%; transform: translate(-50%, 0);
                    font-size: 10px; color: #5F6368; background-color: white;
                    padding: 0 4px;">
            {conn["connection_type"]}
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main application layout
def main():
    render_header()
    
    # Display upload interface if needed
    if st.session_state.upload_step == "upload":
        render_document_uploader()
    
    # Main layout with three columns
    if st.session_state.upload_step == "complete" or True:  # Always show for demo
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            render_search_filters()
            
            # Filter documents based on current filters
            filtered_docs = filter_documents()
            render_document_list(filtered_docs)
            
        with col2:
            render_document_details(st.session_state.selected_document)
            
        with col3:
            # Tabs for different views
            tab1, tab2, tab3 = st.tabs(["Connections", "Timeline", "Connection Map"])
            
            with tab1:
                render_connections(st.session_state.selected_document)
                
            with tab2:
                render_timeline()
                
            with tab3:
                render_connection_diagram()

if __name__ == "__main__":
    main()
