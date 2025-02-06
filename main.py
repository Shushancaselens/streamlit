import streamlit as st
import plotly.graph_objects as go
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
    # Status card
    st.markdown("""
    <div class="status-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h2 style="font-size: 1.25rem; font-weight: 600; margin: 0;">Active Investigation</h2>
                <p style="color: #6B7280; margin: 0;">100,532 documents under analysis</p>
            </div>
            <div style="display: flex; gap: 1.5rem;">
                <div>
                    <div style="font-weight: 500;">Processing Speed</div>
                    <div style="color: #059669;">2,145 docs/min</div>
                </div>
                <div>
                    <div style="font-weight: 500;">Critical Findings</div>
                    <div style="color: #DC2626;">23 found</div>
                </div>
                <div>
                    <div style="font-weight: 500;">Analysis Progress</div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <div style="width: 8rem; background-color: #E5E7EB; height: 0.5rem; border-radius: 9999px;">
                            <div style="width: 45%; background-color: #2563EB; height: 100%; border-radius: 9999px;"></div>
                        </div>
                        <span>45%</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Agent collaboration network
    st.markdown("""
    <div class="status-card" style="margin-top: 1.5rem;">
        <h3 style="font-weight: 600; margin-bottom: 1rem;">Agent Collaboration</h3>
    """, unsafe_allow_html=True)

    # Network visualization using Plotly (without networkx)
    # Define node positions manually
    nodes = {
        "Timeline": {"x": 2, "y": 5},
        "Document": {"x": 4, "y": 3},
        "Legal": {"x": 6, "y": 5},
        "Citation": {"x": 8, "y": 7}
    }
    
    edges = [
        ("Timeline", "Document"),
        ("Document", "Legal"),
        ("Legal", "Citation"),
        ("Timeline", "Legal"),
        ("Document", "Citation")
    ]

    # Create edge traces
    edge_x = []
    edge_y = []
    for edge in edges:
        x0, y0 = nodes[edge[0]]["x"], nodes[edge[0]]["y"]
        x1, y1 = nodes[edge[1]]["x"], nodes[edge[1]]["y"]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#93C5FD'),
        hoverinfo='none',
        mode='lines')

    # Create node trace
    node_x = [pos["x"] for pos in nodes.values()]
    node_y = [pos["y"] for pos in nodes.values()]
    node_text = list(nodes.keys())

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        text=node_text,
        mode='markers+text',
        textposition="bottom center",
        hoverinfo='text',
        marker=dict(
            size=30,
            color='white',
            line=dict(color='#93C5FD', width=2)
        ))

    # Create the figure
    fig = go.Figure(data=[edge_trace, node_trace],
                   layout=go.Layout(
                       showlegend=False,
                       hovermode='closest',
                       margin=dict(b=20,l=5,r=5,t=40),
                       plot_bgcolor='#F9FAFB',
                       paper_bgcolor='#F9FAFB',
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                   ))
    
    st.plotly_chart(fig, use_container_width=True)

    # Findings
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
