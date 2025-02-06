import streamlit as st
import math

# Set page config
st.set_page_config(
    page_title="Document Review System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match React version precisely
st.markdown("""
    <style>
    /* Global Resets */
    div[data-testid="stAppViewContainer"],
    div[data-testid="stHeader"] {
        background: #f8fafc;
    }
    section[data-testid="stSidebar"] {
        display: none;
    }
    
    /* Layout */
    .main-container {
        display: flex;
        height: 100vh;
        max-width: 100%;
        overflow: hidden;
    }
    
    /* Left Sidebar */
    .sidebar {
        width: 320px;
        background: white;
        border-right: 1px solid #e5e7eb;
        padding: 1rem;
        overflow-y: auto;
    }
    
    /* Logo */
    .logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 0 1.5rem 0;
    }
    .logo-icon {
        width: 2rem;
        height: 2rem;
        background: #2563eb;
        border-radius: 0.375rem;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
    }
    
    /* Agent Cards */
    .agent-button {
        width: 100%;
        padding: 0.75rem;
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        transition: all 0.15s ease-in-out;
    }
    .agent-button:hover {
        background: #f8fafc;
        transform: translateX(2px);
    }
    .agent-button.selected {
        background: #eff6ff;
        border-color: #bfdbfe;
    }
    
    /* Agent Icons */
    .agent-icon {
        padding: 0.5rem;
        border-radius: 0.375rem;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 2.5rem;
        height: 2.5rem;
    }
    .agent-icon.analysis { background: #dbeafe; color: #1d4ed8; }
    .agent-icon.expert { background: #f3e8ff; color: #7e22ce; }
    .agent-icon.alert { background: #fee2e2; color: #dc2626; }
    .agent-icon.synthesis { background: #dcfce7; color: #15803d; }
    
    /* Main Content */
    .main-content {
        flex: 1;
        padding: 1.5rem;
        overflow-y: auto;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Cards */
    .card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Network Visualization */
    .network-container {
        position: relative;
        height: 300px;
        background: #f8fafc;
        border-radius: 0.5rem;
        overflow: hidden;
    }
    .network-node {
        position: absolute;
        padding: 0.75rem;
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.375rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Findings */
    .finding-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .tag {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background: #f1f5f9;
        border-radius: 9999px;
        font-size: 0.875rem;
        margin-right: 0.5rem;
        color: #475569;
    }
    .button {
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.15s;
    }
    .button.primary {
        background: #eff6ff;
        color: #1d4ed8;
    }
    .button.primary:hover {
        background: #dbeafe;
    }
    .button.secondary {
        background: #f1f5f9;
        color: #475569;
    }
    .button.secondary:hover {
        background: #e2e8f0;
    }
    
    /* Progress Indicators */
    .progress-bar {
        height: 0.5rem;
        background: #e5e7eb;
        border-radius: 9999px;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        background: #2563eb;
        transition: width 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_agent' not in st.session_state:
    st.session_state.selected_agent = None

# Define agents with more detailed metadata
agents = {
    'timeline': {
        'name': 'Event Timeline',
        'icon': '🕒',
        'status': 'Found 3 critical gaps in communication',
        'type': 'analysis',
        'findings': 12,
        'progress': 85
    },
    'document': {
        'name': 'Document Analysis',
        'icon': '📄',
        'status': 'Processing document content',
        'type': 'analysis',
        'findings': 15,
        'progress': 92
    },
    'legal': {
        'name': 'Legal Compliance',
        'icon': '⚖️',
        'status': 'Reviewing regulatory adherence',
        'type': 'expert',
        'findings': 12,
        'progress': 78
    },
    'citation': {
        'name': 'Citation Check',
        'icon': '🔍',
        'status': 'Verifying reference accuracy',
        'type': 'analysis',
        'findings': 6,
        'progress': 88
    },
    'statement': {
        'name': 'Statement Review',
        'icon': '💬',
        'status': 'Analyzing key statements',
        'type': 'expert',
        'findings': 9,
        'progress': 75
    }
}

# Network nodes (for visualization)
network_nodes = [
    {'id': 'timeline', 'x': 20, 'y': 50},
    {'id': 'document', 'x': 40, 'y': 30},
    {'id': 'legal', 'x': 60, 'y': 50},
    {'id': 'citation', 'x': 80, 'y': 70}
]

# Main container
st.markdown("""
    <div class="main-container">
        <div class="sidebar">
            <!-- Logo -->
            <div class="logo">
                <div class="logo-icon">C</div>
                <span style="font-size: 1.25rem; font-weight: 600;">caselens</span>
            </div>
            
            <!-- Agent Heading -->
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <h2 style="font-size: 1.25rem; font-weight: 600;">Active Agents</h2>
            </div>
""", unsafe_allow_html=True)

# Render agents
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
                    <div class="progress-bar" style="margin-top: 0.5rem;">
                        <div class="progress-fill" style="width: {agent['progress']}%;"></div>
                    </div>
                </div>
                <div style="background: #f3f4f6; padding: 0.25rem 0.5rem; border-radius: 9999px; font-size: 0.75rem;">
                    {agent['findings']}
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Close sidebar and start main content
st.markdown("""
        </div>
        <div class="main-content">
""", unsafe_allow_html=True)

# Status Section
st.markdown("""
    <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 0.25rem;">Active Investigation</h2>
                <p style="color: #6b7280;">100,532 documents under analysis</p>
            </div>
            <div style="display: flex; gap: 2rem;">
                <div>
                    <div style="font-weight: 500;">Processing Speed</div>
                    <div style="color: #10b981; font-size: 1.125rem;">2,145 docs/min</div>
                </div>
                <div>
                    <div style="font-weight: 500;">Critical Findings</div>
                    <div style="color: #ef4444; font-size: 1.125rem;">23 found</div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Network Visualization
st.markdown("""
    <div class="card">
        <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">Agent Collaboration</h3>
        <div class="network-container">
""", unsafe_allow_html=True)

# Render network nodes
for node in network_nodes:
    st.markdown(f"""
        <div class="network-node" style="left: {node['x']}%; top: {node['y']}%;">
            <div class="agent-icon {agents[node['id']]['type']}" style="width: 1.5rem; height: 1.5rem; padding: 0.25rem;">
                {agents[node['id']]['icon']}
            </div>
            <span style="font-size: 0.875rem; font-weight: 500;">{agents[node['id']]['name']}</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
        </div>
    </div>
""", unsafe_allow_html=True)

# Findings Section
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

st.markdown("<h3 style='font-size: 1.25rem; font-weight: 600; margin: 1.5rem 0 1rem;'>Latest Findings</h3>", unsafe_allow_html=True)

for finding in findings:
    st.markdown(f"""
        <div class="finding-card">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.75rem;">
                <div style="font-weight: 600; font-size: 1.125rem;">{finding['title']}</div>
                <span style="color: #6b7280; font-size: 0.875rem;">{finding['time']}</span>
            </div>
            <p style="color: #4b5563; margin-bottom: 1rem;">{finding['description']}</p>
            <div style="margin-bottom: 1rem;">
                {''.join([f'<span class="tag">{doc}</span>' for doc in finding['docs']])}
            </div>
            <div style="display: flex; gap: 0.75rem;">
                <button class="button primary">Investigate Further</button>
                <button class="button secondary">Mark as Reviewed</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Close main content and container
st.markdown("""
        </div>
    </div>
""", unsafe_allow_html=True)
