import streamlit as st
from datetime import datetime, timedelta
import time

# Set page config
st.set_page_config(
    page_title="CaseLens",
    page_icon="📚",
    layout="wide"
)

# Custom CSS to match the original styling
st.markdown("""
    <style>
    .stApp {
        background-color: #F9FAFB;
    }
    .status-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #E5E7EB;
        margin-bottom: 1rem;
    }
    .finding-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #E5E7EB;
        margin-bottom: 1rem;
    }
    .agent-button {
        background-color: white;
        border: 1px solid #E5E7EB;
        border-radius: 0.5rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
        width: 100%;
        text-align: left;
    }
    .agent-button:hover {
        background-color: #F3F4F6;
    }
    .selected {
        background-color: #EBF5FF;
        border-color: #93C5FD;
    }
    .network-node {
        background-color: white;
        border: 2px solid #93C5FD;
        border-radius: 0.5rem;
        padding: 0.5rem;
        text-align: center;
        margin: 0.5rem;
        width: 120px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'selected_agent' not in st.session_state:
    st.session_state.selected_agent = None

# Data structures
agents = {
    "timeline": {
        "name": "Event Timeline",
        "icon": "⏰",
        "status": "Analyzing event sequences",
        "type": "analysis",
        "findings": 8
    },
    "document": {
        "name": "Document Analysis",
        "icon": "📄",
        "status": "Processing document content",
        "type": "analysis",
        "findings": 15
    },
    "legal": {
        "name": "Legal Compliance",
        "icon": "⚖️",
        "status": "Reviewing regulatory adherence",
        "type": "expert",
        "findings": 12
    },
    "citation": {
        "name": "Citation Check",
        "icon": "🔍",
        "status": "Verifying reference accuracy",
        "type": "analysis",
        "findings": 6
    },
    "statement": {
        "name": "Statement Review",
        "icon": "💬",
        "status": "Analyzing key statements",
        "type": "expert",
        "findings": 9
    }
}

findings = [
    {
        "id": 1,
        "agent": "legal",
        "severity": "high",
        "title": "Compliance Issue Detected",
        "description": "Potential regulatory violation in section 3.2 of the agreement",
        "related_docs": ["agreement-v2.1", "reg-guidelines"],
        "timestamp": "2 min ago"
    },
    {
        "id": 2,
        "agent": "document",
        "severity": "medium",
        "title": "Document Inconsistency",
        "description": "Discrepancy found between revision history and document metadata",
        "related_docs": ["doc-metadata-log"],
        "timestamp": "5 min ago"
    }
]

# Layout
col1, col2 = st.columns([1, 3])

# Sidebar content
with col1:
    # Logo
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 2rem;">
            <div style="width: 2rem; height: 2rem; background-color: #2563EB; border-radius: 0.25rem; 
                        display: flex; align-items: center; justify-content: center; margin-right: 0.5rem;">
                <span style="color: white; font-weight: bold; font-size: 1.25rem;">C</span>
            </div>
            <span style="font-size: 1.25rem; font-weight: bold;">caselens</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🧠 Active Agents")
    
    # Agent buttons
    for agent_id, agent in agents.items():
        button_class = "agent-button selected" if st.session_state.selected_agent == agent_id else "agent-button"
        if st.markdown(f"""
            <button class="{button_class}">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <span style="font-size: 1.25rem; margin-right: 0.5rem;">{agent['icon']}</span>
                        <span style="font-weight: 500;">{agent['name']}</span>
                        <div style="font-size: 0.75rem; color: #6B7280;">{agent['status']}</div>
                    </div>
                    <span style="background-color: #F3F4F6; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.75rem;">
                        {agent['findings']}
                    </span>
                </div>
            </button>
        """, unsafe_allow_html=True):
            st.session_state.selected_agent = agent_id

# Main content
with col2:
    # Status card with metrics
    st.markdown('<div class="status-card">', unsafe_allow_html=True)
    
    # Header metrics
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.metric("Documents Under Analysis", "100,532", "2,145/min")
    
    with metric_col2:
        st.metric("Critical Findings", "23", "-5")
    
    with metric_col3:
        st.metric("Analysis Progress", "45%", "2%")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Agent collaboration view
    st.markdown('<div class="status-card">', unsafe_allow_html=True)
    st.subheader("Agent Collaboration")
    
    # Simple grid layout for nodes
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="network-node">Timeline<br>⏰</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="network-node">Document<br>📄</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="network-node">Legal<br>⚖️</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="network-node">Citation<br>🔍</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Findings
    st.subheader("Recent Findings")
    for finding in findings:
        agent = agents[finding['agent']]
        severity_color = "#FEE2E2" if finding['severity'] == 'high' else "#FEF3C7"
        
        st.markdown(f"""
        <div class="finding-card">
            <div style="display: flex; gap: 1rem;">
                <div style="background-color: {severity_color}; padding: 0.5rem; border-radius: 0.5rem;">
                    {agent['icon']}
                </div>
                <div style="flex: 1;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                        <h3 style="font-weight: 600; margin: 0;">{finding['title']}</h3>
                        <span style="color: #6B7280; font-size: 0.875rem;">{finding['timestamp']}</span>
                    </div>
                    <p style="color: #4B5563; margin-bottom: 1rem;">{finding['description']}</p>
                    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                        {' '.join([f'<button style="background-color: #F3F4F6; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem;">{doc}</button>' for doc in finding['related_docs']])}
                    </div>
                    <div style="display: flex; gap: 0.75rem;">
                        <button style="background-color: #EBF5FF; color: #1D4ED8; padding: 0.5rem 1rem; border-radius: 0.5rem; font-size: 0.875rem;">
                            Investigate Further
                        </button>
                        <button style="background-color: #F3F4F6; color: #374151; padding: 0.5rem 1rem; border-radius: 0.5rem; font-size: 0.875rem;">
                            Mark as Reviewed
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Add auto-refresh functionality
if st.button('Start Auto-refresh'):
    time.sleep(2)  # Simulate refresh delay
    st.experimental_rerun()
