import streamlit as st

# Set page config
st.set_page_config(
    page_title="Document Review System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to exactly match React version
st.markdown("""
    <style>
    /* Global Resets */
    div[data-testid="stAppViewContainer"] {
        background: #f8fafc;
        padding: 0;
    }
    div[data-testid="stHeader"] {
        display: none;
    }
    section[data-testid="stSidebar"] {
        display: none;
    }
    
    /* Main Layout */
    .app-container {
        display: flex;
        height: 100vh;
        background: #f8fafc;
        overflow: hidden;
    }
    
    /* Left Sidebar */
    .left-sidebar {
        width: 320px;
        background: white;
        border-right: 1px solid #e5e7eb;
        padding: 1rem;
        overflow-y: auto;
        flex-shrink: 0;
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
    }
    
    /* Agent Cards */
    .agent-card {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        cursor: pointer;
        transition: all 0.2s;
    }
    .agent-card:hover {
        background: #f8fafc;
    }
    .agent-card.selected {
        background: #eff6ff;
        border-color: #bfdbfe;
    }
    
    /* Agent Icons */
    .agent-icon {
        padding: 0.5rem;
        border-radius: 0.375rem;
    }
    .agent-icon.analysis { background: #dbeafe; }
    .agent-icon.expert { background: #f3e8ff; }
    .agent-icon.alert { background: #fee2e2; }
    .agent-icon.synthesis { background: #dcfce7; }
    
    /* Main Content */
    .main-content {
        flex: 1;
        overflow-y: auto;
        padding: 1.5rem;
    }
    .content-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Status Cards */
    .status-section {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    /* Network Graph */
    .network-container {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .network-graph {
        height: 16rem;
        background: #f8fafc;
        border-radius: 0.5rem;
        position: relative;
        overflow: hidden;
    }
    .network-node {
        position: absolute;
        background: white;
        padding: 0.75rem;
        border-radius: 0.375rem;
        border: 1px solid #e5e7eb;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* Findings Cards */
    .finding-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .tag {
        background: #f1f5f9;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        color: #475569;
        margin-right: 0.5rem;
    }
    .action-btn {
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        font-weight: 500;
        cursor: pointer;
    }
    .action-btn.primary {
        background: #eff6ff;
        color: #1d4ed8;
    }
    .action-btn.secondary {
        background: #f1f5f9;
        color: #475569;
    }
    
    /* Right Sidebar - Exact match to React version */
    .right-sidebar {
        width: 320px;
        background: white;
        border-left: 1px solid #e5e7eb;
        padding: 1rem;
        flex-shrink: 0;
    }
    .context-btn {
        width: 100%;
        text-align: left;
        padding: 0.5rem;
        background: #f8fafc;
        border-radius: 0.375rem;
        margin-bottom: 0.5rem;
        font-size: 0.875rem;
        color: #475569;
    }
    .progress-item {
        margin-bottom: 0.75rem;
    }
    .progress-bar {
        height: 0.5rem;
        background: #e5e7eb;
        border-radius: 9999px;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        transition: width 0.3s;
    }
    .blue-fill { background: #2563eb; }
    .red-fill { background: #dc2626; }
    </style>
""", unsafe_allow_html=True)

# App Layout
st.markdown("""
<div class="app-container">
    <!-- Left Sidebar -->
    <div class="left-sidebar">
        <!-- Logo -->
        <div class="logo">
            <div class="logo-icon">C</div>
            <span style="font-size: 1.25rem; font-weight: bold;">caselens</span>
        </div>
        
        <!-- Agents Header -->
        <h2 style="display: flex; align-items: center; gap: 0.5rem; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">
            <span style="display: inline-flex;">🧠</span> Active Agents
        </h2>
""", unsafe_allow_html=True)

# Agents Data
agents = {
    'timeline': {'name': 'Event Timeline', 'icon': '⏱️', 'type': 'analysis', 'status': 'Found 3 critical gaps', 'findings': 12},
    'document': {'name': 'Document Analysis', 'icon': '📄', 'type': 'analysis', 'status': 'Processing content', 'findings': 15},
    'legal': {'name': 'Legal Compliance', 'icon': '⚖️', 'type': 'expert', 'status': 'Reviewing compliance', 'findings': 7},
    'citation': {'name': 'Citation Check', 'icon': '🔍', 'type': 'analysis', 'status': 'Verifying accuracy', 'findings': 6},
    'statement': {'name': 'Statement Review', 'icon': '💬', 'type': 'expert', 'status': 'Analyzing statements', 'findings': 9}
}

# Render Agents
for id, agent in agents.items():
    st.markdown(f"""
        <div class="agent-card">
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

# Main Content Start
st.markdown("""
    </div>
    <div class="main-content">
        <div class="content-container">
            <!-- Status Section -->
            <div class="status-section">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h2 style="font-size: 1.25rem; font-weight: 600;">Active Investigation</h2>
                        <p style="color: #6b7280;">100,532 documents under analysis</p>
                    </div>
                    <div style="display: flex; gap: 2rem;">
                        <div>
                            <div style="font-weight: 500;">Processing Speed</div>
                            <div style="color: #10b981;">2,145 docs/min</div>
                        </div>
                        <div>
                            <div style="font-weight: 500;">Critical Findings</div>
                            <div style="color: #dc2626;">23 found</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Network Graph -->
            <div class="network-container">
                <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 1rem;">Agent Collaboration</h3>
                <div class="network-graph">
                    <!-- Network nodes and connections would be rendered here -->
                </div>
            </div>

            <!-- Findings Section -->
            <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 1rem;">Latest Findings</h3>
""", unsafe_allow_html=True)

# Findings Data
findings = [
    {
        'title': 'Contract Term Inconsistency',
        'description': 'Different IP ownership terms found in email (March 15) vs Contract v2.1',
        'docs': ['email-5123', 'contract-v2.1'],
        'time': '2 min ago'
    },
    {
        'title': 'Communication Gap',
        'description': 'No communications found during critical negotiation period (April 2-15)',
        'docs': ['timeline-gap-1'],
        'time': '5 min ago'
    }
]

# Render Findings
for finding in findings:
    st.markdown(f"""
        <div class="finding-card">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.75rem;">
                <h4 style="font-weight: 600;">{finding['title']}</h4>
                <span style="color: #6b7280; font-size: 0.875rem;">{finding['time']}</span>
            </div>
            <p style="color: #4b5563; margin-bottom: 1rem;">{finding['description']}</p>
            <div style="margin-bottom: 1rem;">
                {''.join([f'<span class="tag">{doc}</span>' for doc in finding['docs']])}
            </div>
            <div style="display: flex; gap: 0.75rem;">
                <button class="action-btn primary">Investigate Further</button>
                <button class="action-btn secondary">Mark as Reviewed</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main Content End
st.markdown("""
        </div>
    </div>
    
    <!-- Right Sidebar -->
    <div class="right-sidebar">
        <h3 style="font-weight: 600; margin-bottom: 1rem;">Investigation Context</h3>
        
        <!-- Context Buttons -->
        <div style="margin-bottom: 1.5rem;">
            <button class="context-btn">Focus on IP Ownership Discussion</button>
            <button class="context-btn">Review Contract Versions</button>
            <button class="context-btn">Analyze Communication Gaps</button>
        </div>
        
        <!-- Progress Section -->
        <h4 style="font-weight: 500; margin-bottom: 0.75rem;">Analysis Progress</h4>
        <div class="progress-item">
            <div style="display: flex; justify-content: space-between; font-size: 0.875rem; margin-bottom: 0.25rem;">
                <span>Documents Processed</span>
                <span>45%</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill blue-fill" style="width: 45%;"></div>
            </div>
        </div>
        <div class="progress-item">
            <div style="display: flex; justify-content: space-between; font-size: 0.875rem; margin-bottom: 0.25rem;">
                <span>Critical Issues Found</span>
                <span>23</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill red-fill" style="width: 15%;"></div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Hide Streamlit elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
