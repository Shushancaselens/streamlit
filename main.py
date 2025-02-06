import streamlit as st
import pandas as pd
from datetime import datetime
import networkx as nx
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Document Review System", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .agent-card {
        border-left: 4px solid transparent;
        padding: 1rem;
        margin-bottom: 0.5rem;
        background: white;
        border-radius: 4px;
        transition: all 0.2s;
    }
    .agent-card:hover {
        border-left-color: #3b82f6;
        background: #f8fafc;
    }
    .agent-card.selected {
        border-left-color: #3b82f6;
        background: #f1f5f9;
    }
    .findings-number {
        background: #f1f5f9;
        padding: 2px 8px;
        border-radius: 9999px;
        font-size: 0.875rem;
    }
    .stat-card {
        background: white;
        padding: 1rem;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
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
        'findings': 8
    },
    'document': {
        'name': 'Document Analysis',
        'status': 'Processing document content',
        'type': 'analysis',
        'findings': 15
    },
    'legal': {
        'name': 'Legal Compliance',
        'status': 'Reviewing regulatory adherence',
        'type': 'expert',
        'findings': 12
    },
    'citation': {
        'name': 'Citation Check',
        'status': 'Verifying reference accuracy',
        'type': 'analysis',
        'findings': 6
    },
    'statement': {
        'name': 'Statement Review',
        'status': 'Analyzing key statements',
        'type': 'expert',
        'findings': 9
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
            <div style="font-weight: 500;">Documents Under Analysis</div>
            <div style="color: #6b7280;">100,532</div>
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

    # Agent collaboration network
    st.markdown("### Agent Collaboration")
    
    # Create network visualization using Plotly
    G = nx.Graph()
    pos = {
        'Timeline': (0, 0),
        'Document': (1, 1),
        'Legal': (2, 0),
        'Citation': (3, 1)
    }
    
    for node in pos:
        G.add_node(node)
    
    G.add_edges_from([
        ('Timeline', 'Document'),
        ('Document', 'Legal'),
        ('Legal', 'Citation'),
        ('Timeline', 'Legal')
    ])

    edge_trace = go.Scatter(
        x=[], y=[],
        line=dict(width=1, color='#94a3b8'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += tuple([x0, x1, None])
        edge_trace['y'] += tuple([y0, y1, None])

    node_trace = go.Scatter(
        x=[pos[node][0] for node in G.nodes()],
        y=[pos[node][1] for node in G.nodes()],
        mode='markers+text',
        text=list(G.nodes()),
        textposition='bottom center',
        marker=dict(
            size=30,
            color='#3b82f6',
            line=dict(color='white', width=2)
        )
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                   layout=go.Layout(
                       showlegend=False,
                       hovermode='closest',
                       margin=dict(b=0, l=0, r=0, t=0),
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                   ))

    st.plotly_chart(fig, use_container_width=True)

    # Findings
    st.markdown("### Latest Findings")
    
    for finding in findings:
        with st.container():
            st.markdown(f"""
            <div style="background: white; padding: 1rem; border-radius: 4px; margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <div style="font-weight: 500;">{finding['title']}</div>
                    <div style="color: #6b7280; font-size: 0.875rem;">{finding['timestamp']}</div>
                </div>
                <div style="color: #4b5563; margin-bottom: 1rem;">{finding['description']}</div>
                <div style="display: flex; gap: 0.5rem;">
                    {' '.join([f'<span style="background: #f1f5f9; padding: 4px 12px; border-radius: 9999px; font-size: 0.875rem;">{doc}</span>' for doc in finding['related_docs']])}
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
