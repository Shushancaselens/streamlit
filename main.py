import streamlit as st
from datetime import datetime
import json

# Page configuration with improved metadata
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.ilsa.org/contact-us/',
        'Report a bug': 'https://github.com/your-repo/issues',
        'About': 'Jessup Memorial Penalty Checker - Version 2.0'
    }
)

# Improved styling with modern components and dark mode support
st.markdown("""
    <style>
    /* Modern UI Theme */
    :root {
        --primary-color: #4F46E5;
        --secondary-color: #818CF8;
        --success-color: #10B981;
        --warning-color: #F59E0B;
        --error-color: #EF4444;
        --background-color: #F9FAFB;
        --card-background: #FFFFFF;
        --text-color: #111827;
        --text-secondary: #6B7280;
    }

    /* Dark mode support */
    @media (prefers-color-scheme: dark) {
        :root {
            --background-color: #1F2937;
            --card-background: #374151;
            --text-color: #F9FAFB;
            --text-secondary: #D1D5DB;
        }
    }
    
    .stApp {
        background-color: var(--background-color);
    }
    
    .card {
        background-color: var(--card-background);
        border-radius: 1rem;
        border: 1px solid rgba(229, 231, 235, 0.2);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease-in-out;
    }
    
    .card:hover {
        transform: translateY(-2px);
    }
    
    .header {
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text-color);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    /* Improved progress bars */
    .stProgress > div > div > div > div {
        height: 0.5rem !important;
        border-radius: 9999px !important;
        transition: width 0.3s ease-in-out;
    }
    
    .progress-success .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #059669 0%, #10B981 100%) !important;
    }
    
    .progress-warning .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #D97706 0%, #F59E0B 100%) !important;
    }
    
    .progress-error .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #DC2626 0%, #EF4444 100%) !important;
    }
    
    /* Improved sidebar */
    [data-testid="stSidebar"] {
        background-color: var(--card-background);
        border-right: 1px solid rgba(229, 231, 235, 0.2);
    }
    
    .menu-item {
        padding: 0.75rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        border: 1px solid transparent;
    }
    
    .menu-item:hover {
        background-color: rgba(79, 70, 229, 0.1);
        border-color: var(--primary-color);
    }
    
    /* Custom button styles */
    .stButton>button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: 600;
        border: none;
        transition: all 0.2s ease-in-out;
    }
    
    .stButton>button:hover {
        background-color: var(--secondary-color);
        transform: translateY(-1px);
    }
    
    /* Improved table styles */
    .styled-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 1rem 0;
    }
    
    .styled-table th,
    .styled-table td {
        padding: 0.75rem;
        border-bottom: 1px solid rgba(229, 231, 235, 0.2);
    }
    
    .styled-table th {
        background-color: rgba(79, 70, 229, 0.1);
        font-weight: 600;
    }
    
    /* Tooltip styles */
    .tooltip {
        position: relative;
        display: inline-block;
    }
    
    .tooltip .tooltiptext {
        visibility: hidden;
        background-color: var(--card-background);
        color: var(--text-color);
        text-align: center;
        padding: 0.5rem;
        border-radius: 0.25rem;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
""", unsafe_allow_html=True)

# Add session state for storing analysis results
if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []

# Improved sidebar with navigation and controls
with st.sidebar:
    # Modern logo and branding
    st.markdown("""
        <div style='background: linear-gradient(135deg, #4F46E5 0%, #818CF8 100%); 
                    padding: 1.5rem; 
                    border-radius: 1rem; 
                    margin-bottom: 2rem;
                    text-align: center;'>
            <h1 style='color: white; font-size: 1.75rem; margin-bottom: 0.5rem;'>⚖️ Jessup Checker</h1>
            <p style='color: rgba(255,255,255,0.9); font-size: 0.875rem;'>Pro Edition</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Add file uploader for memorial
    uploaded_file = st.file_uploader("Upload Memorial", type=['pdf', 'docx'])
    
    if uploaded_file:
        st.success("File uploaded successfully!")
        
        # Add analysis options
        st.markdown("### Analysis Options")
        auto_analysis = st.toggle("Auto-analyze on upload", value=True)
        include_plagiarism = st.toggle("Include plagiarism check", value=True)
        advanced_citations = st.toggle("Advanced citation analysis", value=False)
        
        if st.button("Start Analysis", type="primary"):
            with st.spinner("Analyzing memorial..."):
                # Simulate analysis delay
                import time
                time.sleep(2)
                st.session_state.analysis_history.append({
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'filename': uploaded_file.name,
                    'score': 10
                })
    
    # Add analysis history
    if st.session_state.analysis_history:
        st.markdown("### Recent Analyses")
        for analysis in st.session_state.analysis_history:
            st.markdown(f"""
                <div class='card' style='padding: 0.75rem; margin: 0.5rem 0;'>
                    <div style='font-size: 0.875rem; color: var(--text-color);'>{analysis['filename']}</div>
                    <div style='font-size: 0.75rem; color: var(--text-secondary);'>{analysis['timestamp']}</div>
                    <div style='color: var(--error-color); font-weight: 600;'>{analysis['score']} penalty points</div>
                </div>
            """, unsafe_allow_html=True)

# Main content area with tabs
tab1, tab2, tab3 = st.tabs(["Analysis Results", "Word Count Details", "Export Report"])

with tab1:
    st.markdown("## Memorial Analysis Results")
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Penalties", value="10 points", delta="2 points recoverable")
    with col2:
        st.metric(label="Word Count Status", value="Within Limits", delta="98% of max")
    with col3:
        st.metric(label="Critical Issues", value="2", delta="-1 from last check", delta_color="inverse")
    with col4:
        st.metric(label="Overall Status", value="Needs Review", delta="3 warnings")
    
    # Detailed analysis cards
    st.markdown("### Detailed Analysis")
    
    # Create expandable sections for each analysis category
    with st.expander("📄 Cover Page Analysis", expanded=True):
        st.markdown("""
            <div class='card'>
                <div class='header'>Cover Page Requirements</div>
                <table class='styled-table'>
                    <tr>
                        <th>Requirement</th>
                        <th>Status</th>
                        <th>Details</th>
                    </tr>
                    <tr>
                        <td>Team Number</td>
                        <td>✅ Present</td>
                        <td>349A</td>
                    </tr>
                    <tr>
                        <td>Court Name</td>
                        <td>✅ Present</td>
                        <td>International Court of Justice</td>
                    </tr>
                </table>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("## Word Count Analysis")
    
    # Add interactive word count charts
    import plotly.graph_objects as go
    
    # Create sample word count data
    sections = ['Statement of Facts', 'Summary of Pleadings', 'Pleadings', 'Prayer for Relief']
    current = [1196, 642, 9424, 0]
    limits = [1200, 700, 9500, 200]
    
    # Create progress bars with plotly
    fig = go.Figure()
    
    for i, (section, count, limit) in enumerate(zip(sections, current, limits)):
        percentage = (count / limit) * 100
        color = '#10B981' if percentage <= 90 else '#F59E0B' if percentage <= 100 else '#EF4444'
        
        fig.add_trace(go.Bar(
            name=section,
            y=[section],
            x=[percentage],
            orientation='h',
            marker=dict(color=color),
            customdata=[[count, limit]],
            hovertemplate="Words: %{customdata[0]}<br>Limit: %{customdata[1]}<br>Usage: %{x:.1f}%<extra></extra>"
        ))
    
    fig.update_layout(
        title="Word Count Usage by Section",
        barmode='stack',
        height=300,
        margin=dict(l=200),
        xaxis=dict(title="Percentage of Limit"),
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("## Export Options")
    
    # Add export options
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Report Format")
        report_format = st.selectbox(
            "Choose format",
            ["PDF Report", "Excel Spreadsheet", "Word Document"]
        )
        
        include_details = st.multiselect(
            "Include in report",
            ["Word Count Analysis", "Citation Check Results", "Penalty Summary", "Recommendations"],
            default=["Word Count Analysis", "Penalty Summary"]
        )
    
    with col2:
        st.markdown("### Delivery Options")
        email = st.text_input("Email report to (optional)")
        
        if st.button("Generate Report", type="primary"):
            with st.spinner("Generating report..."):
                # Simulate report generation
                import time
                time.sleep(2)
                st.success("Report generated successfully!")
                st.download_button(
                    label="Download Report",
                    data=b"Sample report content",
                    file_name=f"jessup_analysis_{datetime.now().strftime('%Y%m%d')}.pdf",
                    mime="application/pdf"
                )

# Add a floating action button for quick actions
st.markdown("""
    <div style='position: fixed; right: 2rem; bottom: 2rem;'>
        <button style='background: linear-gradient(135deg, #4F46E5 0%, #818CF8 100%); 
                      color: white; 
                      border: none; 
                      padding: 1rem; 
                      border-radius: 50%; 
                      cursor: pointer;
                      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);'>
            <span style='font-size: 1.5rem;'>+</span>
        </button>
    </div>
""", unsafe_allow_html=True)
