import streamlit as st
import pandas as pd
from datetime import datetime
import json

# Set page config to wide mode and add title
st.set_page_config(layout="wide", page_title="CaseLens")

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .timeline-event {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: white;
    }
    .document-card {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 0.5rem;
        background-color: white;
    }
    .badge {
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .badge-blue {
        background-color: #dbeafe;
        color: #1e40af;
    }
    .badge-red {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    .badge-gray {
        background-color: #f3f4f6;
        color: #6b7280;
    }
    .section-title {
        font-size: 1.25rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sample timeline data
timeline_events = [
    {
        "id": 10,
        "fullText": "On 14 March 2000 the Parties concluded a contract for the construction of 19 km of Phase II of the Al-Ghaida internal roads.",
        "date": "14 March 2000",
        "sources": {
            "claimant": {
                "submissions": [{ 
                    "ref": "Claimant Memorial ¶145-148", 
                    "context": "The contract was signed after a competitive bidding process where the Claimant's bid was found to be the most technically and financially advantageous. The contract value was set at USD 12.5 million with a completion period of 24 months.", 
                    "marker": "CM-¶145" 
                }],
                "exhibits": [
                    { 
                        "ref": "DLP-Yemen Contract (Exh. C-21, p. 1-15)", 
                        "context": "Contract for Phase II Al-Ghaida roads project (19km), value: USD 12.5M with 24-month completion period. Agreement sets out scope of works, payment terms, and performance obligations between Desert Line Projects LLC and Republic of Yemen.", 
                        "marker": "C21-1", 
                        "fileType": "PDF" 
                    },
                    { 
                        "ref": "DLP Board Minutes (Exh. C-22, p. 3-4)", 
                        "context": "Minutes of DLP Board of Directors' extraordinary meeting approving Al-Ghaida roads contract (USD 12.5M), discussing mobilization strategy and authorizing Chairman to sign contract with Yemen government.", 
                        "marker": "C22-1", 
                        "fileType": "PDF" 
                    }
                ]
            },
            "respondent": {
                "submissions": [{ 
                    "ref": "Respondent Counter-Memorial ¶203-205", 
                    "context": "While the contract was indeed signed on the stated date, the Respondent maintains that the Claimant failed to properly mobilize within the contractual timeframe. Initial delays were already apparent by May 2000.", 
                    "marker": "RCM-¶203" 
                }],
                "exhibits": [
                    { 
                        "ref": "MoPW Bid Evaluation (Exh. R-15, p. 23-28)", 
                        "context": "Ministry's internal evaluation of three competing bids, examining proposed contract values (USD 12.5M-15.8M range) and technical capabilities. Includes detailed scoring matrix and recommendation for award to DLP.", 
                        "marker": "R15-1", 
                        "fileType": "PDF" 
                    },
                    { 
                        "ref": "MoPW Site Supervision Report (Exh. R-16, p. 102-115)", 
                        "context": "Ministry's on-site supervision reports covering first three months of project (March-May 2000), detailing contractor mobilization issues, equipment deployment status, and preliminary works progress", 
                        "marker": "R16-1", 
                        "fileType": "PDF" 
                    }
                ]
            }
        }
    }
]

# Initialize session state for expanded events
if 'expanded_events' not in st.session_state:
    st.session_state.expanded_events = {}

# Sidebar
with st.sidebar:
    st.title("🔍 CaseLens")
    
    # Search box
    st.subheader("Search Events")
    search_query = st.text_input("", placeholder="Search...")
    
    # Date range
    st.subheader("Date Range")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

# Main content
st.title("Desert Line Projects (DLP) and The Republic of Yemen")

# Copy button functionality
if st.button("📋 Copy Timeline"):
    timeline_text = "\n\n".join([
        f"{event['fullText']}\n\nSources:\n" + 
        "\n".join([f"- {ex['ref']}" for ex in event['sources']['claimant']['exhibits'] + event['sources']['respondent']['exhibits']])
        for event in timeline_events
    ])
    st.code(timeline_text, language="text")

# Display timeline events
for event in timeline_events:
    with st.container():
        st.markdown(f"""
            <div class="timeline-event">
                <div>
                    <strong>{event['date']}</strong> - {event['fullText'].replace(event['date'], '')}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Expand/collapse button
        if st.button(f"{'📖 Show Details' if not st.session_state.expanded_events.get(event['id']) else '📕 Hide Details'}", 
                    key=f"toggle_{event['id']}"):
            st.session_state.expanded_events[event['id']] = not st.session_state.expanded_events.get(event['id'], False)
        
        # Show expanded content
        if st.session_state.expanded_events.get(event['id']):
            # Citation count
            total_citations = (
                len(event['sources']['claimant']['exhibits']) + 
                len(event['sources']['respondent']['exhibits']) +
                len(event['sources']['claimant']['submissions']) + 
                len(event['sources']['respondent']['submissions'])
            )
            
            st.markdown(f"""
                <div style="background-color: #f3f4f6; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                    <div style="font-size: 1.25rem; font-weight: 500;">{total_citations}</div>
                    <div style="font-size: 0.875rem; color: #6b7280;">Citations</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Parties badges
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<span class="badge badge-blue">Claimant</span>', unsafe_allow_html=True)
            with col2:
                st.markdown('<span class="badge badge-red">Respondent</span>', unsafe_allow_html=True)
            
            # Supporting Documents
            st.markdown("### Supporting Documents")
            for doc in event['sources']['claimant']['exhibits'] + event['sources']['respondent']['exhibits']:
                st.markdown(f"""
                    <div class="document-card">
                        <div style="font-weight: 500;">{doc['ref']}</div>
                        <div style="color: #6b7280; font-size: 0.875rem;">{doc['context']}</div>
                        {'<a href="#" style="color: #2563eb; text-decoration: none;">📄 Open Document</a>' if doc.get('fileType') else ''}
                    </div>
                """, unsafe_allow_html=True)
            
            # Submissions
            st.markdown("### Submissions")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Claimant")
                for sub in event['sources']['claimant']['submissions']:
                    st.markdown(f"""
                        <div class="document-card">
                            <div style="font-weight: 500;">{sub['ref']}</div>
                            <div style="color: #6b7280; font-size: 0.875rem;">{sub['context']}</div>
                        </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("#### Respondent")
                for sub in event['sources']['respondent']['submissions']:
                    st.markdown(f"""
                        <div class="document-card">
                            <div style="font-weight: 500;">{sub['ref']}</div>
                            <div style="color: #6b7280; font-size: 0.875rem;">{sub['context']}</div>
                        </div>
                    """, unsafe_allow_html=True)
