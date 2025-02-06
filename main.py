import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(page_title="Document Review System", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    /* Reset and base styles */
    div[data-testid="stAppViewContainer"] {
        background: #f8fafc;
    }
    
    /* Agent Cards */
    .agent-card {
        border-left: 4px solid transparent;
        padding: 1.25rem;
        margin-bottom: 0.75rem;
        background: white;
        border-radius: 8px;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .agent-card:hover {
        border-left-color: #3b82f6;
        background: #f8fafc;
        transform: translateX(4px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .agent-card.selected {
        border-left-color: #3b82f6;
        background: #eff6ff;
        box-shadow: 0 4px 6px rgba(59,130,246,0.1);
    }
    
    /* Status Indicators */
    .findings-number {
        background: #dbeafe;
        color: #1e40af;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    /* Cards */
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s ease-in-out;
        border: 1px solid #e5e7eb;
    }
    .stat-card:hover {
        transform: translateY(-2px);
    }
    
    .network-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 0.75rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e5e7eb;
        transition: transform 0.2s ease-in-out;
    }
    .network-card:hover {
        transform: translateY(-2px);
    }
    
    /* Progress Bars */
    .connection-status {
        height: 8px;
        border-radius: 9999px;
        margin: 0.75rem 0;
        background: #f1f5f9;
        overflow: hidden;
    }
    
    /* Findings */
    .finding-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e5e7eb;
        transition: all 0.2s ease-in-out;
    }
    .finding-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.05);
    }
    
    /* Tags */
    .doc-tag {
        background: #f1f5f9;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.875rem;
        color: #1e293b;
        border: 1px solid #e2e8f0;
        transition: all 0.2s ease-in-out;
    }
    .doc-tag:hover {
        background: #e2e8f0;
        transform: translateY(-1px);
    }
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        color: #0f172a;
        font-weight: 600;
        letter-spacing: -0.025em;
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
    }
    ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_agent' not in st.session_state:
    st.session_state.selected_agent = None

# Define agents
agents = {
    'timeline': {
        'name': 'Event Timeline',
        'status': 'Analyzing event sequences',
        'type': 'analysis',
        'findings': 8,
        'connection_strength': 0.85
    },
    'document': {
        'name': 'Document Analysis',
        'status': 'Processing document content',
        'type': 'analysis',
        'findings': 15,
        'connection_strength': 0.92
    },
    'legal': {
        'name': 'Legal Compliance',
        'status': 'Reviewing regulatory adherence',
        'type': 'expert',
        'findings': 12,
        'connection_strength': 0.78
    },
    'citation': {
        'name': 'Citation Check',
        'status': 'Verifying reference accuracy',
        'type': 'analysis',
        'findings': 6,
        'connection_strength': 0.88
    },
    'statement': {
        'name': 'Statement Review',
        'status': 'Analyzing key statements',
        'type': 'expert',
        'findings': 9,
        'connection_strength': 0.75
    }
}

# Define findings
findings = [
    {
        'id': 1,
        'agent': 'legal',
        'severity': 'high',
        'title': 'Compliance Issue Detected',
        'description': 'Potential regulatory violation in section 3.2 of the agreement',
        'related_docs': ['agreement-v2.1', 'reg-guidelines'],
        'timestamp': '2 min ago'
    },
    {
        'id': 2,
        'agent': 'document',
        'severity': 'medium',
        'title': 'Document Inconsistency',
        'description': 'Discrepancy found between revision history and document metadata',
        'related_docs': ['doc-metadata-log'],
        'timestamp': '5 min ago'
    }
]

# Create layout
col1, col2 = st.columns([1, 3])

# Sidebar with agents
with col1:
    st.markdown("### Active Agents")
    st.markdown(f"#### {len(agents)} total")
    
    for agent_id, agent in agents.items():
        # Create clickable agent card
        card_html = f"""
        <div class="agent-card {'selected' if st.session_state.selected_agent == agent_id else ''}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-weight: 500;">{agent['name']}</div>
                    <div style="color: #6b7280; font-size: 0.875rem;">{agent['status']}</div>
                </div>
                <span class="findings-number">{agent['findings']}</span>
            </div>
        </div>
        """
        if st.markdown(card_html, unsafe_allow_html=True):
            st.session_state.selected_agent = agent_id

# Main content
with col2:
    # Status cards
    st.markdown("### Active Investigation")
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
        <div class="stat-card">
            <div style="font-weight: 600; color: #1e293b; margin-bottom: 0.5rem;">Documents Under Analysis</div>
            <div style="font-size: 1.5rem; font-weight: 600; color: #0f172a;">100,532</div>
            <div style="font-size: 0.875rem; color: #64748b; margin-top: 0.25rem;">Active documents</div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="stat-card">
            <div style="font-weight: 500;">Processing Speed</div>
            <div style="color: #059669;">2,145 docs/min</div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
        <div class="stat-card">
            <div style="font-weight: 500;">Critical Findings</div>
            <div style="color: #dc2626;">23 found</div>
        </div>
        """, unsafe_allow_html=True)

    # Agent collaboration status
    st.markdown("### Agent Collaboration")
    
    # Display connection strengths as progress bars
    cols = st.columns(2)
    for idx, (agent_id, agent) in enumerate(agents.items()):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="network-card">
                <div style="font-weight: 500;">{agent['name']}</div>
                <div style="color: #6b7280; font-size: 0.875rem;">Connection Strength</div>
                <div class="connection-status" style="background: linear-gradient(to right, #3b82f6 {agent['connection_strength']*100}%, #e5e7eb {agent['connection_strength']*100}%)"></div>
                <div style="text-align: right; font-size: 0.875rem; color: #6b7280;">{int(agent['connection_strength']*100)}%</div>
            </div>
            """, unsafe_allow_html=True)

    # Findings
    st.markdown("### Latest Findings")
    
    for finding in findings:
        with st.container():
            st.markdown(f"""
            <div class="finding-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.75rem;">
                    <div style="font-weight: 600; font-size: 1.1rem; color: #0f172a;">{finding['title']}</div>
                    <div style="color: #64748b; font-size: 0.875rem; font-weight: 500;">{finding['timestamp']}</div>
                </div>
                <div style="color: #334155; margin-bottom: 1.25rem; line-height: 1.6;">{finding['description']}</div>
                <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                    {' '.join([f'<span class="doc-tag">{doc}</span>' for doc in finding['related_docs']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            cols = st.columns(2)
            with cols[0]:
                st.button("Investigate Further", key=f"investigate_{finding['id']}")
            with cols[1]:
                st.button("Mark as Reviewed", key=f"review_{finding['id']}")

# Add custom footer
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; right: 0; background: white; padding: 1rem; text-align: center; border-top: 1px solid #e5e7eb;">
        <span style="color: #6b7280;">Document Review System - Processing documents at 2,145 docs/min</span>
    </div>
""", unsafe_allow_html=True)
