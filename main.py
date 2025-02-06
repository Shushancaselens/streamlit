import streamlit as st
import time

# Set page config
st.set_page_config(
    page_title="CaseLens",
    page_icon="📚",
    layout="wide"
)

# Custom CSS to maintain React-like styling
st.markdown("""
    <style>
    /* Main container styles */
    .stApp {
        background-color: rgb(249, 250, 251);
    }
    
    /* Card styles */
    div[data-testid="stVerticalBlock"] > div:has(div.element-container) {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid rgb(229, 231, 235);
        margin-bottom: 1rem;
    }
    
    /* Button styles */
    .stButton > button {
        width: 100%;
        text-align: left;
        background-color: white;
        border: 1px solid rgb(229, 231, 235);
        border-radius: 0.5rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    
    .stButton > button:hover {
        border-color: rgb(147, 197, 253);
        background-color: rgb(239, 246, 255);
    }
    
    /* Metric containers */
    [data-testid="stMetricValue"] {
        font-size: 1.25rem !important;
        color: rgb(17, 24, 39);
    }
    
    [data-testid="stMetricDelta"] {
        color: rgb(16, 185, 129);
        font-size: 0.875rem;
    }
    
    /* Card header styles */
    h2, h3 {
        color: rgb(17, 24, 39);
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* Custom node container */
    .node-container {
        border: 2px solid rgb(147, 197, 253);
        background-color: white;
        padding: 0.75rem;
        border-radius: 0.5rem;
        text-align: center;
        margin: 0.5rem;
    }
    
    /* Finding card styles */
    .finding-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid rgb(229, 231, 235);
        margin-bottom: 1rem;
    }
    
    /* Custom header with icon */
    .header-with-icon {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    
    /* Custom progress bar */
    .progress-container {
        width: 100%;
        height: 0.5rem;
        background-color: rgb(229, 231, 235);
        border-radius: 9999px;
        overflow: hidden;
    }
    
    .progress-bar {
        height: 100%;
        background-color: rgb(37, 99, 235);
        border-radius: 9999px;
    }
    
    /* Agent badge styles */
    .agent-badge {
        display: inline-flex;
        align-items: center;
        background-color: rgb(243, 244, 246);
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        margin-right: 0.5rem;
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
            <div style="width: 2rem; height: 2rem; background-color: rgb(37, 99, 235); border-radius: 0.25rem; 
                        display: flex; align-items: center; justify-content: center; margin-right: 0.5rem;">
                <span style="color: white; font-weight: bold; font-size: 1.25rem;">C</span>
            </div>
            <span style="font-size: 1.25rem; font-weight: bold;">caselens</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Agents section
    st.markdown("""
        <div class="header-with-icon">
            <span style="font-size: 1.5rem;">🧠</span>
            <h2 style="margin: 0;">Active Agents</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Agent buttons using Streamlit components
    for agent_id, agent in agents.items():
        if st.button(
            f"{agent['icon']} {agent['name']}\n{agent['status']}\n{agent['findings']} findings",
            key=f"agent_{agent_id}",
            help=f"View details for {agent['name']}"
        ):
            st.session_state.selected_agent = agent_id

# Main content
with col2:
    # Status metrics
    st.markdown('<div style="background-color: white; padding: 1rem; border-radius: 0.5rem; border: 1px solid rgb(229, 231, 235);">', unsafe_allow_html=True)
    
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    
    with metrics_col1:
        st.metric(
            "Documents Processed",
            "100,532",
            "2,145/min",
            help="Total documents processed and current processing rate"
        )
    
    with metrics_col2:
        st.metric(
            "Critical Findings",
            "23",
            "-5",
            delta_color="inverse",
            help="Number of critical issues detected"
        )
    
    with metrics_col3:
        st.metric(
            "Analysis Progress",
            "45%",
            "2%",
            help="Overall progress of document analysis"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Agent collaboration view
    st.markdown("""
        <div style="background-color: white; padding: 1rem; border-radius: 0.5rem; border: 1px solid rgb(229, 231, 235); margin-top: 1rem;">
            <h3>Agent Collaboration</h3>
    """, unsafe_allow_html=True)
    
    # Simple grid for agent nodes
    node_cols = st.columns(4)
    for i, (node_id, node) in enumerate(list(agents.items())[:4]):
        with node_cols[i]:
            st.markdown(f"""
                <div class="node-container">
                    <div style="font-size: 1.5rem;">{node['icon']}</div>
                    <div style="font-weight: 500;">{node['name']}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Findings
    st.markdown("<h3 style='margin-top: 1rem;'>Recent Findings</h3>", unsafe_allow_html=True)
    
    for finding in findings:
        agent = agents[finding['agent']]
        severity_color = "rgb(254, 226, 226)" if finding['severity'] == 'high' else "rgb(254, 243, 199)"
        
        st.markdown(f"""
            <div class="finding-card">
                <div style="display: flex; gap: 1rem;">
                    <div style="background-color: {severity_color}; padding: 0.5rem; border-radius: 0.5rem;">
                        {agent['icon']}
                    </div>
                    <div style="flex: 1;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <h4 style="font-weight: 600; margin: 0;">{finding['title']}</h4>
                            <span style="color: rgb(107, 114, 128); font-size: 0.875rem;">
                                {finding['timestamp']}
                            </span>
                        </div>
                        <p style="color: rgb(75, 85, 99); margin-bottom: 1rem;">
                            {finding['description']}
                        </p>
                        <div style="margin-bottom: 1rem;">
                            {' '.join([f'<span class="agent-badge">{doc}</span>' for doc in finding['related_docs']])}
                        </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Action buttons using Streamlit
        col1, col2, _ = st.columns([1, 1, 2])
        with col1:
            st.button("Investigate Further", key=f"investigate_{finding['id']}")
        with col2:
            st.button("Mark as Reviewed", key=f"review_{finding['id']}")

# Auto-refresh section
with st.sidebar:
    if st.button("Start Auto-refresh"):
        time.sleep(2)
        st.experimental_rerun()
