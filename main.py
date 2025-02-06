import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(page_title="Document Review System", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    /* Design System Variables */
    :root {
        --primary: #3b82f6;
        --primary-light: #dbeafe;
        --primary-dark: #1e40af;
        --surface: #ffffff;
        --background: #f8fafc;
        --border: #e2e8f0;
        --text-primary: #0f172a;
        --text-secondary: #475569;
        --text-tertiary: #64748b;
        --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
        --shadow-md: 0 4px 6px rgba(0,0,0,0.05);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-full: 9999px;
        --space-1: 0.25rem;
        --space-2: 0.5rem;
        --space-3: 0.75rem;
        --space-4: 1rem;
        --space-5: 1.25rem;
        --space-6: 1.5rem;
    }

    /* Base Styles */
    div[data-testid="stAppViewContainer"] {
        background: var(--background);
    }
    
    /* Component: Card Base */
    .card {
        background: var(--surface);
        border-radius: var(--radius-md);
        border: 1px solid var(--border);
        padding: var(--space-6);
        box-shadow: var(--shadow-sm);
        transition: all 0.2s ease-in-out;
    }
    
    /* Component: Agent Card */
    .agent-card {
        border-left: 4px solid transparent;
        padding: var(--space-5);
        margin-bottom: var(--space-3);
        background: var(--surface);
        border-radius: var(--radius-sm);
        box-shadow: var(--shadow-sm);
        transition: all 0.2s ease-in-out;
    }
    .agent-card:hover {
        border-left-color: var(--primary);
        transform: translateX(4px);
        box-shadow: var(--shadow-md);
    }
    .agent-card.selected {
        border-left-color: var(--primary);
        background: var(--primary-light);
    }
    
    /* Component: Badge */
    .badge {
        background: var(--primary-light);
        color: var(--primary-dark);
        padding: var(--space-2) var(--space-4);
        border-radius: var(--radius-full);
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    /* Component: Status Card */
    .stat-card {
        display: flex;
        flex-direction: column;
        gap: var(--space-2);
    }
    .stat-card:hover {
        transform: translateY(-2px);
    }
    
    /* Component: Network Card */
    .network-card {
        margin: var(--space-3) 0;
    }
    
    /* Component: Progress Bar */
    .connection-status {
        height: 8px;
        border-radius: var(--radius-full);
        margin: var(--space-3) 0;
        background: var(--primary-light);
        overflow: hidden;
    }
    
    /* Component: Finding Card */
    .finding-card {
        margin-bottom: var(--space-4);
    }
    .finding-card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }
    
    /* Component: Document Tag */
    .doc-tag {
        display: inline-block;
        padding: var(--space-2) var(--space-4);
        background: var(--background);
        color: var(--text-secondary);
        border-radius: var(--radius-full);
        font-size: 0.875rem;
        border: 1px solid var(--border);
        transition: all 0.2s ease-in-out;
    }
    .doc-tag:hover {
        background: var(--primary-light);
        color: var(--primary-dark);
        border-color: var(--primary);
    }
    
    /* Typography */
    .heading-lg {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: var(--space-4);
    }
    .heading-md {
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: var(--space-3);
    }
    .text-sm {
        font-size: 0.875rem;
        color: var(--text-tertiary);
    }
    .text-lg {
        font-size: 1.125rem;
        color: var(--text-primary);
    }
    
    /* Layout Utilities */
    .flex-between {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .flex-col {
        display: flex;
        flex-direction: column;
    }
    .gap-2 {
        gap: var(--space-2);
    }
    .gap-3 {
        gap: var(--space-3);
    }
    
    /* States and Interactions */
    .hover-lift {
        transition: transform 0.2s ease-in-out;
    }
    .hover-lift:hover {
        transform: translateY(-2px);
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
