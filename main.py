import streamlit as st

# Set page config
st.set_page_config(page_title="Document Review System", layout="wide")

# Custom CSS to match React version
st.markdown("""
    <style>
    /* Reset and Base Styles */
    div[data-testid="stAppViewContainer"] {
        background: #f8fafc;
    }
    
    /* Logo */
    .logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .logo-icon {
        width: 2rem;
        height: 2rem;
        background: #2563eb;
        border-radius: 0.25rem;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 1.25rem;
    }
    
    /* Sidebar Agent */
    .agent-button {
        width: 100%;
        padding: 0.75rem;
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        transition: all 0.15s ease-in-out;
        cursor: pointer;
        text-align: left;
    }
    .agent-button:hover {
        background: #f8fafc;
    }
    .agent-button.selected {
        background: #eff6ff;
        border-color: #bfdbfe;
    }
    .agent-icon {
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
    .agent-icon.analysis { background: #dbeafe; }
    .agent-icon.expert { background: #f3e8ff; }
    .agent-icon.alert { background: #fee2e2; }
    .agent-icon.synthesis { background: #dcfce7; }
    
    /* Main Content */
    .status-card {
        background: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #e5e7eb;
    }
    
    /* Network Visualization */
    .network-vis {
        background: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #e5e7eb;
        margin: 1rem 0;
        height: 16rem;
    }
    
    /* Findings */
    .finding {
        background: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }
    .doc-tag {
        background: #f1f5f9;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        margin-right: 0.5rem;
    }
    .finding-button {
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        cursor: pointer;
    }
    .finding-button.primary {
        background: #eff6ff;
        color: #1d4ed8;
    }
    .finding-button.secondary {
        background: #f1f5f9;
        color: #475569;
    }
    </style>
""", unsafe_allow_html=True)

# Logo Component
st.markdown("""
    <div class="logo">
        <div class="logo-icon">C</div>
        <span style="font-size: 1.25rem; font-weight: bold;">caselens</span>
    </div>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_agent' not in st.session_state:
    st.session_state.selected_agent = None

# Data
agents = {
    'timeline': {
        'name': 'Event Timeline',
        'icon': '⏱️',
        'status': 'Found 3 critical gaps in communication',
        'type': 'analysis',
        'findings': 12
    },
    'document': {
        'name': 'Document Analysis',
        'icon': '📄',
        'status': 'Processing document content',
        'type': 'analysis',
        'findings': 15
    },
    'legal': {
        'name': 'Legal Compliance',
        'icon': '⚖️',
        'status': 'Reviewing regulatory adherence',
        'type': 'expert',
        'findings': 12
    },
    'citation': {
        'name': 'Citation Check',
        'icon': '🔍',
        'status': 'Verifying reference accuracy',
        'type': 'analysis',
        'findings': 6
    },
    'statement': {
        'name': 'Statement Review',
        'icon': '💬',
        'status': 'Analyzing key statements',
        'type': 'expert',
        'findings': 9
    }
}

# Layout
col1, col2 = st.columns([1, 3])

# Sidebar
with col1:
    st.markdown("### Active Agents", help="Select an agent to view its findings")
    
    for agent_id, agent in agents.items():
        st.markdown(f"""
            <div class="agent-button {'selected' if st.session_state.selected_agent == agent_id else ''}">
                <div style="display: flex; align-items: center; gap: 0.75rem;">
                    <div class="agent-icon {agent['type']}">
                        {agent['icon']}
                    </div>
                    <div style="flex: 1">
                        <div style="font-weight: 500;">{agent['name']}</div>
                        <div style="font-size: 0.75rem; color: #6b7280;">{agent['status']}</div>
                    </div>
                    <div style="background: #f3f4f6; padding: 0.25rem 0.5rem; border-radius: 9999px; font-size: 0.75rem;">
                        {agent['findings']}
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Main Content
with col2:
    # Status Cards
    st.markdown("### Active Investigation")
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
            <div class="status-card">
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.25rem;">Documents Under Analysis</h3>
                <p style="color: #6b7280;">100,532 documents</p>
            </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
            <div class="status-card">
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.25rem;">Processing Speed</h3>
                <p style="color: #10b981;">2,145 docs/min</p>
            </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
            <div class="status-card">
                <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.25rem;">Critical Findings</h3>
                <p style="color: #ef4444;">23 found</p>
            </div>
        """, unsafe_allow_html=True)

    # Network Visualization
    st.markdown("### Agent Collaboration")
    st.markdown("""
        <div class="network-vis">
            <!-- Simple placeholder for network visualization -->
            <div style="height: 100%; display: flex; align-items: center; justify-content: center; color: #6b7280;">
                Network visualization would appear here
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Findings
    st.markdown("### Latest Findings")
    
    findings = [
        {
            'title': 'Contract Term Inconsistency',
            'description': 'Different IP ownership terms found in email (March 15) vs Contract v2.1',
            'docs': ['email-5123', 'contract-v2.1'],
            'severity': 'high',
            'time': '2 min ago'
        },
        {
            'title': 'Communication Gap',
            'description': 'No communications found during critical negotiation period (April 2-15)',
            'docs': ['timeline-gap-1'],
            'severity': 'medium',
            'time': '5 min ago'
        }
    ]

    for finding in findings:
        st.markdown(f"""
            <div class="finding">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <h3 style="font-weight: 600;">{finding['title']}</h3>
                    <span style="color: #6b7280; font-size: 0.875rem;">{finding['time']}</span>
                </div>
                <p style="color: #4b5563; margin-bottom: 1rem;">{finding['description']}</p>
                <div style="margin-bottom: 1rem;">
                    {''.join([f'<span class="doc-tag">{doc}</span>' for doc in finding['docs']])}
                </div>
                <div style="display: flex; gap: 0.75rem;">
                    <button class="finding-button primary">Investigate Further</button>
                    <button class="finding-button secondary">Mark as Reviewed</button>
                </div>
            </div>
        """, unsafe_allow_html=True)
