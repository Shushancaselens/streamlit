import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="CaseLens", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f9f9fb;
    }
    .css-1d391kg {
        background-color: #f9f9fb;
    }
    .doc-folder {
        background-color: white;
        border-radius: 4px;
        padding: 10px;
        margin: 5px 0;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .doc-folder:hover {
        background-color: #f0f0f5;
    }
    .folder-icon {
        color: #4c72b0;
        margin-right: 5px;
    }
    .sidebar-content {
        padding: 10px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 16px;
        background-color: #f0f0f5;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4c72b0 !important;
        color: white !important;
    }
    .timeline-event {
        padding: 10px;
        border-radius: 4px;
        margin: 5px 0;
    }
    .appellant {
        border-left: 4px solid #4c72b0;
    }
    .respondent {
        border-left: 4px solid #e15759;
    }
    .evidence-tag {
        background-color: #f0f0f5;
        border-radius: 12px;
        padding: 2px 8px;
        font-size: 12px;
        color: #666;
    }
    .status-tag {
        border-radius: 12px;
        padding: 2px 8px;
        font-size: 12px;
        color: white;
    }
    .disputed {
        background-color: #e15759;
    }
    .undisputed {
        background-color: #55a868;
    }
</style>
""", unsafe_allow_html=True)

# Create sidebar with logo and navigation
with st.sidebar:
    st.image("https://placehold.co/200x50?text=CaseLens", width=150)
    st.markdown("## Legal Analysis")
    
    # Create sidebar navigation
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    
    # Mimic folder structure from second screenshot
    folders = [
        "📄 Arguments",
        "📊 Facts",
        "📂 Exhibits"
    ]
    selected_section = st.radio("", folders, index=1, label_visibility="collapsed")
    
    # Document folders
    st.markdown("### Case Documents")
    doc_folders = [
        "1. Statement of Appeal",
        "2. Request for a Stay",
        "3. Answer to Request for PM",
        "4. Answer to PM",
        "5. Appeal Brief",
        "6. Brief on Admissibility",
        "7. Reply to Objection to Admissibility",
        "8. Challenge",
        "ChatGPT",
        "Jurisprudence",
        "Objection to Admissibility",
        "Swiss Court"
    ]
    
    for folder in doc_folders:
        st.markdown(f"""
        <div class="doc-folder">
            <span class="folder-icon">📁</span> {folder}
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Main content area
st.title("Summary of arguments")

# Create case facts section with tabs
st.header("Case Facts")

tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])

# Create case facts data
case_facts = [
    {
        "date": "1950-present", 
        "event": "Continuous operation under same name since 1950", 
        "party": "Appellant", 
        "status": "Undisputed",
        "argument": "1. Sporting Succession",
        "evidence": "C-1",
        "related_documents": ["1. Statement of Appeal", "5. Appeal Brief"]
    },
    {
        "date": "1950", 
        "event": "Initial registration in 1950", 
        "party": "Appellant", 
        "status": "Undisputed",
        "argument": "1.1.1. Registration History",
        "evidence": "C-2",
        "related_documents": ["1. Statement of Appeal"]
    },
    {
        "date": "1950-present", 
        "event": "Consistent use of blue and white since founding", 
        "party": "Appellant", 
        "status": "Disputed",
        "argument": "1.2. Club Colors Analysis",
        "evidence": "C-4",
        "related_documents": ["5. Appeal Brief", "8. Challenge"]
    },
    {
        "date": "1950-1975", 
        "event": "Pre-1976 colors represented original city district", 
        "party": "Respondent", 
        "status": "Undisputed",
        "argument": "1.2.1. Color Changes Analysis",
        "evidence": "R-5",
        "related_documents": ["2. Request for a Stay", "4. Answer to PM"]
    },
    {
        "date": "1970-1980", 
        "event": "Minor shade variations do not affect continuity", 
        "party": "Appellant", 
        "status": "Undisputed",
        "argument": "1.2.1. Color Variations Analysis",
        "evidence": "C-5",
        "related_documents": ["5. Appeal Brief"]
    },
    {
        "date": "1975-1976", 
        "event": "Brief administrative gap in 1975-1976", 
        "party": "Appellant", 
        "status": "Disputed",
        "argument": "1.1.1. Registration History",
        "evidence": "C-2",
        "related_documents": ["1. Statement of Appeal", "6. Brief on Admissibility"]
    },
    {
        "date": "1975-1976", 
        "event": "Operations ceased between 1975-1976", 
        "party": "Respondent", 
        "status": "Disputed",
        "argument": "1. Sporting Succession",
        "evidence": "R-1",
        "related_documents": ["2. Request for a Stay", "Objection to Admissibility"]
    }
]

# Convert to dataframe for easier manipulation
df = pd.DataFrame(case_facts)

# Function to create the timeline visualization
def create_timeline():
    fig = go.Figure()
    
    # Parse dates and create a date column we can sort by
    date_vals = []
    for date_str in df['date']:
        if '-present' in date_str:
            date_vals.append(datetime.strptime(date_str.split('-')[0], '%Y'))
        elif '-' in date_str:
            date_vals.append(datetime.strptime(date_str.split('-')[0], '%Y'))
        else:
            date_vals.append(datetime.strptime(date_str, '%Y'))
    
    df['date_val'] = date_vals
    sorted_df = df.sort_values('date_val')
    
    # Add lines for time periods
    for i, row in sorted_df.iterrows():
        color = "#4c72b0" if row['party'] == "Appellant" else "#e15759"
        
        # Handle date range
        if '-' in row['date']:
            parts = row['date'].split('-')
            start_year = parts[0]
            
            # Handle "present" or end year
            if parts[1] == "present":
                end_year = "2025"  # Assuming current year
            else:
                end_year = parts[1]
                
            # Add line for time range
            fig.add_trace(go.Scatter(
                x=[start_year, end_year],
                y=[i, i],
                mode='lines',
                line=dict(color=color, width=10),
                opacity=0.7,
                name=row['event'],
                hoverinfo='text',
                hovertext=f"{row['event']}<br>Status: {row['status']}<br>Evidence: {row['evidence']}",
                showlegend=False
            ))
            
        # Add marker for the event
        fig.add_trace(go.Scatter(
            x=[row['date'].split('-')[0]],
            y=[i],
            mode='markers',
            marker=dict(size=15, color=color, line=dict(color='white', width=2)),
            name=row['event'],
            text=row['event'],
            hoverinfo='text',
            hovertext=f"{row['event']}<br>Party: {row['party']}<br>Status: {row['status']}<br>Evidence: {row['evidence']}",
            showlegend=False
        ))
    
    # Update layout
    fig.update_layout(
        title="Case Timeline",
        xaxis=dict(
            title="Year",
            type='category',
            tickvals=["1950", "1960", "1970", "1980", "1990", "2000", "2010", "2020", "Present"],
        ),
        yaxis=dict(
            showticklabels=False,
        ),
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode='closest'
    )
    
    return fig

# Display different content based on the active tab
with tabs[0]:  # All Facts
    # Display timeline
    st.plotly_chart(create_timeline(), use_container_width=True)
    
    # Display facts table with columns
    cols = st.columns([1, 2, 1, 1, 2, 1])
    cols[0].markdown("**Date**")
    cols[1].markdown("**Event**")
    cols[2].markdown("**Party**")
    cols[3].markdown("**Status**")
    cols[4].markdown("**Related Argument**")
    cols[5].markdown("**Evidence**")
    
    # Display rows with styling based on party and status
    for i, fact in enumerate(case_facts):
        cols = st.columns([1, 2, 1, 1, 2, 1])
        
        # Determine party style
        party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
        
        # Create expandable container for each fact
        with st.expander(f"Event {i+1}: {fact['event']}", expanded=False):
            st.markdown(f"""
            <div class="timeline-event {party_class}">
                <p><strong>Event:</strong> {fact['event']}</p>
                <p><strong>Date:</strong> {fact['date']}</p>
                <p><strong>Party:</strong> {fact['party']}</p>
                <p><strong>Status:</strong> {fact['status']}</p>
                <p><strong>Related Argument:</strong> {fact['argument']}</p>
                <p><strong>Evidence:</strong> {fact['evidence']}</p>
                <p><strong>Related Documents:</strong></p>
                <ul>
                    {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Display basic info in the table
        cols[0].write(fact["date"])
        cols[1].write(fact["event"])
        
        # Style the party column
        party_style = "color: #4c72b0; font-weight: bold;" if fact["party"] == "Appellant" else "color: #e15759; font-weight: bold;"
        cols[2].markdown(f"<span style='{party_style}'>{fact['party']}</span>", unsafe_allow_html=True)
        
        # Style the status column
        status_class = "disputed" if fact["status"] == "Disputed" else "undisputed"
        cols[3].markdown(f"<span class='status-tag {status_class}'>{fact['status']}</span>", unsafe_allow_html=True)
        
        cols[4].write(fact["argument"])
        cols[5].markdown(f"<span class='evidence-tag'>{fact['evidence']}</span>", unsafe_allow_html=True)

with tabs[1]:  # Disputed Facts
    disputed_facts = [fact for fact in case_facts if fact["status"] == "Disputed"]
    
    if disputed_facts:
        for i, fact in enumerate(disputed_facts):
            party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
            
            with st.expander(f"{fact['event']}", expanded=True):
                st.markdown(f"""
                <div class="timeline-event {party_class}">
                    <p><strong>Event:</strong> {fact['event']}</p>
                    <p><strong>Date:</strong> {fact['date']}</p>
                    <p><strong>Party:</strong> {fact['party']}</p>
                    <p><strong>Related Argument:</strong> {fact['argument']}</p>
                    <p><strong>Evidence:</strong> {fact['evidence']}</p>
                    <p><strong>Related Documents:</strong></p>
                    <ul>
                        {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                # Show related document connections
                if i < len(disputed_facts) - 1:
                    opposing_facts = [f for f in disputed_facts if f['argument'] == fact['argument'] and f['party'] != fact['party']]
                    if opposing_facts:
                        st.markdown("#### Conflicting Claims")
                        for opp in opposing_facts:
                            st.markdown(f"""
                            <div class="timeline-event {"appellant" if opp["party"] == "Appellant" else "respondent"}">
                                <p><strong>{opp['party']} claims:</strong> {opp['event']}</p>
                                <p><strong>Evidence:</strong> {opp['evidence']}</p>
                            </div>
                            """, unsafe_allow_html=True)
    else:
        st.info("No disputed facts found.")

with tabs[2]:  # Undisputed Facts
    undisputed_facts = [fact for fact in case_facts if fact["status"] == "Undisputed"]
    
    if undisputed_facts:
        for fact in undisputed_facts:
            party_class = "appellant" if fact["party"] == "Appellant" else "respondent"
            
            with st.expander(f"{fact['event']}", expanded=True):
                st.markdown(f"""
                <div class="timeline-event {party_class}">
                    <p><strong>Event:</strong> {fact['event']}</p>
                    <p><strong>Date:</strong> {fact['date']}</p>
                    <p><strong>Party:</strong> {fact['party']}</p>
                    <p><strong>Related Argument:</strong> {fact['argument']}</p>
                    <p><strong>Evidence:</strong> {fact['evidence']}</p>
                    <p><strong>Related Documents:</strong></p>
                    <ul>
                        {"".join([f"<li>{doc}</li>" for doc in fact['related_documents']])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No undisputed facts found.")

# Add a document-centric view
st.header("Documents and Related Events")

# Group facts by related documents
doc_to_facts = {}
for fact in case_facts:
    for doc in fact['related_documents']:
        if doc not in doc_to_facts:
            doc_to_facts[doc] = []
        doc_to_facts[doc].append(fact)

# Create tabs for each document type
doc_tabs = st.tabs(list(doc_to_facts.keys()))

# Fill each tab with related events
for i, (doc, facts) in enumerate(doc_to_facts.items()):
    with doc_tabs[i]:
        st.subheader(f"Events Referenced in {doc}")
        
        # Create a mini-timeline for this document
        events_df = pd.DataFrame(facts)
        
        # Group events by argument
        arguments = events_df['argument'].unique()
        for arg in arguments:
            arg_events = events_df[events_df['argument'] == arg]
            
            st.markdown(f"### {arg}")
            
            for _, event in arg_events.iterrows():
                party_class = "appellant" if event["party"] == "Appellant" else "respondent"
                status_class = "disputed" if event["status"] == "Disputed" else "undisputed"
                
                st.markdown(f"""
                <div class="timeline-event {party_class}">
                    <p><strong>Event:</strong> {event['event']}</p>
                    <p><strong>Date:</strong> {event['date']}</p>
                    <p><strong>Party:</strong> {event['party']}</p>
                    <p><strong>Status:</strong> <span class="status-tag {status_class}">{event['status']}</span></p>
                    <p><strong>Evidence:</strong> <span class="evidence-tag">{event['evidence']}</span></p>
                </div>
                """, unsafe_allow_html=True)

# Add footer with action buttons
col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    st.button("Copy")
with col2:
    st.button("Export")
