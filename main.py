import streamlit as st
import pandas as pd
from datetime import datetime, date
import time
import random

# Page configuration
st.set_page_config(
    page_title="Caselens - Legal Research Platform",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'search_history' not in st.session_state:
    st.session_state.search_history = []
if 'bookmarked_cases' not in st.session_state:
    st.session_state.bookmarked_cases = []
if 'current_case' not in st.session_state:
    st.session_state.current_case = None

# Sample case database
CASES_DATABASE = [
    {
        "id": "CAS_2013_A_3165",
        "title": "CAS 2013/A/3165 - CAS 2013/A/3165",
        "date": "2014-01-14",
        "procedure": "Appeal Arbitration",
        "matter": "Contract",
        "category": "Award",
        "outcome": "Dismissed",
        "sport": "Football",
        "appellants": "FC Volyn",
        "respondents": "Issa Ndoye",
        "president": "Petros Mavroidis",
        "arbitrator1": "Geraint Jones",
        "arbitrator2": "Raymond Hack",
        "summary": "The case involves a contractual dispute between FC Volyn, a Ukrainian football club, and Issa Ndoye, a Senegalese footballer. Ndoye terminated his employment with FC Volyn in June 2011, claiming unpaid salary and contract breach, subsequently bringing a claim before FIFA's Dispute Resolution Chamber (DRC), which ruled in his favor, ordering the club to pay outstanding remuneration and compensation. FC Volyn appealed to the CAS, arguing that Ndoye had no just cause due to his alleged breaches (mainly late returns to training), while Ndoye countered that non-payment constituted just cause and sought increased compensation. Both parties debated applicable law and timing of appeals/counterclaims.",
        "court_reasoning": "The CAS panel found that FIFA regulations take precedence over national law due to the contract's terms and parties' submission to FIFA/CAS jurisdiction. The Club's repeated failure to pay Ndoye's salary for over three months was a substantial breach, constituting just cause for contract termination. Alleged late returns by Ndoye did not nullify this breach, and there was no evidence he agreed to delay payment. Counterclaims by respondents were inadmissible per CAS procedural rules. The compensation set by the FIFA DRC was appropriate.",
        "case_outcome": "The appeal by FC Volyn was dismissed and the FIFA DRC's decision was upheld: FC Volyn must pay Ndoye USD 299,200 in outstanding remuneration and USD 495,000 as compensation. Ndoye's counterclaim for additional damages was ruled inadmissible, and all other requests were dismissed. The panel confirmed that the time limit for appeal had been respected and that FIFA regulations (with Swiss law supplementary) applied.",
        "relevant_passages": [
            "Page 15 - 78. The Commentary on the RSTP states the following with regard to the concept of 'just cause': 'The definition of just cause and whether just cause exists shall be established in accordance with the merits of each particular case.",
            "Page 22 - 89. Non-payment of salary constitutes a breach of contract which may give rise to just cause for the employee to terminate the employment contract.",
            "Page 31 - 105. The consistent jurisprudence of CAS establishes that just cause must be of such severity that the injured party cannot reasonably be expected to continue the contractual relationship."
        ],
        "similarity_score": 0.87
    },
    {
        "id": "CAS_2014_A_3567",
        "title": "CAS 2014/A/3567 - Player Transfer Dispute",
        "date": "2015-03-22",
        "procedure": "Appeal Arbitration",
        "matter": "Transfer",
        "category": "Award",
        "outcome": "Upheld",
        "sport": "Football",
        "appellants": "Real Madrid CF",
        "respondents": "Manchester United FC",
        "president": "John Smith",
        "arbitrator1": "Maria Rodriguez",
        "arbitrator2": "Hans Mueller",
        "summary": "Dispute concerning transfer compensation and solidarity mechanism payments for a youth player transfer between Manchester United and Real Madrid.",
        "court_reasoning": "The panel found that FIFA's solidarity mechanism provisions were properly applied and the requesting club was entitled to compensation.",
        "case_outcome": "Appeal upheld. Real Madrid must pay additional compensation of EUR 2,500,000 to Manchester United for the player transfer.",
        "relevant_passages": [
            "Page 8 - 45. The solidarity mechanism ensures fair compensation for clubs investing in youth development.",
            "Page 12 - 67. Training compensation is due when a player signs their first professional contract."
        ],
        "similarity_score": 0.72
    },
    {
        "id": "CAS_2015_A_4123",
        "title": "CAS 2015/A/4123 - Doping Violation Case",
        "date": "2016-01-15",
        "procedure": "Ordinary Arbitration",
        "matter": "Anti-Doping",
        "category": "Award",
        "outcome": "Partially Upheld",
        "sport": "Athletics",
        "appellants": "International Association of Athletics Federations",
        "respondents": "John Athlete",
        "president": "Dr. Sarah Wilson",
        "arbitrator1": "Prof. Michael Brown",
        "arbitrator2": "Anna Thompson",
        "summary": "Anti-doping rule violation case involving the use of prohibited substances during competition period.",
        "court_reasoning": "The panel found evidence of rule violation but considered mitigating circumstances regarding the athlete's lack of intent.",
        "case_outcome": "Partially upheld. Athlete sanctioned with 18-month suspension instead of 4 years due to mitigating circumstances.",
        "relevant_passages": [
            "Page 5 - 23. Strict liability applies regardless of intent in anti-doping cases.",
            "Page 9 - 34. Mitigating circumstances may reduce the standard sanction period."
        ],
        "similarity_score": 0.45
    }
]

# Custom CSS
st.markdown("""
<style>
    .main-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 20px;
    }
    
    .logo-icon {
        background-color: #4f46e5;
        color: white;
        padding: 8px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 16px;
    }
    
    .case-title {
        font-size: 18px;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 8px;
    }
    
    .tag {
        display: inline-block;
        font-size: 11px;
        font-weight: 500;
        padding: 3px 8px;
        margin: 2px 4px 2px 0;
        border-radius: 12px;
        background-color: #f1f5f9;
        color: #475569;
        border: 1px solid #e2e8f0;
    }
    
    .tag-date {
        background-color: #eff6ff;
        color: #1d4ed8;
        border-color: #dbeafe;
    }
    
    .tag-outcome-dismissed {
        background-color: #fef2f2;
        color: #991b1b;
        border-color: #fecaca;
    }
    
    .tag-outcome-upheld {
        background-color: #f0fdf4;
        color: #166534;
        border-color: #bbf7d0;
    }
    
    .tag-outcome-partially-upheld {
        background-color: #fefce8;
        color: #a16207;
        border-color: #fde047;
    }
    
    .tag-sport-football {
        background-color: #f0fdf4;
        color: #166534;
        border-color: #bbf7d0;
    }
    
    .tag-sport-athletics {
        background-color: #fdf2f8;
        color: #9d174d;
        border-color: #fbcfe8;
    }
    
    .case-meta {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 12px;
    }
    
    .section-content {
        background-color: #f8fafc;
        padding: 12px;
        border-radius: 6px;
        border-left: 3px solid #4f46e5;
        margin: 8px 0;
    }
    
    .results-summary {
        background-color: #d1fae5;
        border: 1px solid #a7f3d0;
        border-radius: 6px;
        padding: 12px 16px;
        margin: 16px 0;
        color: #065f46;
    }
    
    .relevant-passage {
        background-color: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-radius: 6px;
        padding: 10px;
        margin: 8px 0;
        font-size: 14px;
    }
    
    .highlighted-text {
        background-color: #dcfce7;
        padding: 2px 4px;
        border-radius: 3px;
        font-weight: 500;
    }
    
    .question-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    
    .stats-card {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
        margin: 8px 0;
    }
    
    .stats-number {
        font-size: 24px;
        font-weight: bold;
        color: #4f46e5;
    }
    
    .stats-label {
        font-size: 14px;
        color: #6b7280;
        margin-top: 4px;
    }
    
    .sidebar-section {
        margin-bottom: 25px;
    }
    
    .bookmark-btn {
        background-color: #fef3c7;
        color: #92400e;
        border: 1px solid #fbbf24;
        border-radius: 4px;
        padding: 4px 8px;
        font-size: 12px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

def search_cases(query, max_results=20, similarity_threshold=0.5):
    """Simulate case search with relevant results"""
    # Simple search simulation - in real app, this would query a database
    relevant_cases = []
    for case in CASES_DATABASE:
        if query.lower() in case['summary'].lower() or query.lower() in case['court_reasoning'].lower():
            if case['similarity_score'] >= similarity_threshold:
                relevant_cases.append(case)
    
    return relevant_cases[:max_results]

def highlight_text(text, query):
    """Highlight search terms in text"""
    if query.lower() in text.lower():
        return text.replace(query, f'<span class="highlighted-text">{query}</span>')
    return text

def render_case_tags(case):
    """Render colored tags for case metadata"""
    tags_html = f"""
    <div>
        <span class="tag tag-date">Date: {case['date']}</span>
        <span class="tag">Type: {case['procedure']}</span>
        <span class="tag">Matter: {case['matter']}</span>
        <span class="tag">Category: {case['category']}</span>
        <span class="tag tag-outcome-{case['outcome'].lower().replace(' ', '-')}">Outcome: {case['outcome']}</span>
        <span class="tag tag-sport-{case['sport'].lower()}">Sport: {case['sport']}</span>
    </div>
    """
    return tags_html

# Sidebar Navigation
with st.sidebar:
    # Logo
    st.markdown("""
    <div class="main-header">
        <span class="logo-icon">C</span>
        <h2 style="margin: 0; color: #1f2937;">caselens</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    st.markdown("### Navigation")
    page = st.radio(
        "",
        ["🔍 Search", "📄 Documents", "📊 Analytics", "🔖 Bookmarks", "👤 Admin"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    if page == "🔍 Search":
        # Search Options
        st.markdown("### Search Options")
        
        with st.container():
            st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
            st.markdown("**Max Results**")
            max_results = st.number_input("", min_value=1, max_value=100, value=20, label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
            st.markdown("**Similarity Threshold**")
            similarity = st.slider("", min_value=0.0, max_value=1.0, value=0.55, step=0.01, label_visibility="collapsed")
            st.write(f"Current value: {similarity}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        show_similarity = st.checkbox("Show Similarity Scores ⓘ")
        
        st.markdown("---")
        
        # Advanced Filters
        with st.expander("🔧 Advanced Filters"):
            date_range = st.date_input(
                "Date Range",
                value=[date(2010, 1, 1), date(2024, 12, 31)],
                key="date_filter"
            )
            
            sport_filter = st.multiselect(
                "Sport",
                ["Football", "Basketball", "Tennis", "Swimming", "Athletics", "Hockey"],
                key="sport_filter"
            )
            
            outcome_filter = st.multiselect(
                "Outcome",
                ["Dismissed", "Upheld", "Partially Upheld", "Settled"],
                key="outcome_filter"
            )
            
            procedure_filter = st.selectbox(
                "Procedure Type",
                ["All", "Appeal Arbitration", "Ordinary Arbitration", "Fast-Track"],
                key="procedure_filter"
            )
        
        # Search History
        if st.session_state.search_history:
            st.markdown("### Recent Searches")
            for i, search in enumerate(st.session_state.search_history[-5:]):
                if st.button(f"🔍 {search}", key=f"history_{i}"):
                    st.session_state.current_search = search

# Main Content Area
if page == "🔍 Search":
    # Search Interface
    st.markdown("### Enter your search query")
    search_query = st.text_input(
        "", 
        value="just cause", 
        placeholder="Enter your search query (e.g., contract termination, doping violation, transfer dispute)", 
        label_visibility="collapsed",
        key="main_search"
    )
    
    # Add to search history
    if search_query and search_query not in st.session_state.search_history:
        st.session_state.search_history.append(search_query)
    
    if search_query:
        # Perform search
        results = search_cases(search_query, max_results, similarity)
        
        # Search results summary
        st.markdown(f"""
        <div class="results-summary">
            <strong>✓ Found {len(results)} results</strong>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"Found {len(results)} relevant passages in {len(results)} decisions")
        
        # Display results
        for i, case in enumerate(results):
            with st.expander(f"**{case['title']}**", expanded=(i == 0)):
                # Tags
                st.markdown(render_case_tags(case), unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                

                # Case metadata
                st.markdown(f"""
                <div class="case-meta">
                    <strong>Appellants:</strong> {case['appellants']} | <strong>Respondents:</strong> {case['respondents']} | 
                    <strong>President:</strong> {case['president']} | <strong>Arbitrator 1:</strong> {case['arbitrator1']} | 
                    <strong>Arbitrator 2:</strong> {case['arbitrator2']}
                </div>
                """, unsafe_allow_html=True)
                
                # Summary
                st.markdown("**Summary:**")
                st.markdown(f"""
                <div class="section-content">
                    {highlight_text(case['summary'], search_query)}
                </div>
                """, unsafe_allow_html=True)
                
                # Court Reasoning
                st.markdown("**Court Reasoning:**")
                st.markdown(f"""
                <div class="section-content">
                    {highlight_text(case['court_reasoning'], search_query)}
                </div>
                """, unsafe_allow_html=True)
                
                # Case Outcome
                st.markdown("**Case Outcome:**")
                st.markdown(f"""
                <div class="section-content">
                    {highlight_text(case['case_outcome'], search_query)}
                </div>
                """, unsafe_allow_html=True)
                
                # Relevant Passages
                st.markdown("**Relevant Passages:**")
                for passage in case['relevant_passages']:
                    st.markdown(f"""
                    <div class="relevant-passage">
                        {highlight_text(passage, search_query)}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Similarity Score
                if show_similarity:
                    st.markdown(f"**Similarity Score:** {case['similarity_score']:.2f}")
                
                # AI Question Interface
                st.markdown("---")
                st.markdown("**Ask a Question About This Case**")
                question = st.text_area(
                    "",
                    placeholder="e.g., What was the main legal issue? What was the outcome? What were the key arguments?",
                    key=f"question_{case['id']}",
                    label_visibility="collapsed"
                )
                
                if st.button("Ask Question", key=f"ask_{case['id']}"):
                    if question:
                        with st.spinner("Analyzing case and generating answer..."):
                            time.sleep(2)  # Simulate AI processing
                            # Simulate AI response
                            if "legal issue" in question.lower():
                                answer = f"The main legal issue in this case was {case['matter'].lower()} dispute, specifically focusing on contract termination and just cause provisions."
                            elif "outcome" in question.lower():
                                answer = f"The case outcome was '{case['outcome']}'. {case['case_outcome'][:100]}..."
                            elif "arguments" in question.lower():
                                answer = f"Key arguments included: {case['court_reasoning'][:150]}..."
                            else:
                                answer = "Based on the case details, this relates to the core legal principles and procedural aspects discussed in the reasoning section."
                            
                            st.markdown(f"""
                            <div class="question-box">
                                <strong>AI Answer:</strong><br>
                                {answer}
                            </div>
                            """, unsafe_allow_html=True)

elif page == "📊 Analytics":
    st.title("📊 Legal Analytics Dashboard")
    
    # Summary statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-number">15,847</div>
            <div class="stats-label">Total Cases</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-number">23</div>
            <div class="stats-label">Sports Covered</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-number">89%</div>
            <div class="stats-label">Cases Resolved</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-number">156</div>
            <div class="stats-label">Countries</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    st.markdown("### Case Trends")
    
    # Sample data for charts
    chart_data = pd.DataFrame({
        'Year': [2019, 2020, 2021, 2022, 2023, 2024],
        'Cases Filed': [1245, 1189, 1567, 1834, 2156, 2234],
        'Cases Resolved': [1198, 1167, 1456, 1723, 2001, 2089]
    })
    
    st.line_chart(chart_data.set_index('Year'))
    
    # Outcome distribution
    st.markdown("### Case Outcomes Distribution")
    outcome_data = pd.DataFrame({
        'Outcome': ['Dismissed', 'Upheld', 'Partially Upheld', 'Settled'],
        'Count': [3456, 2890, 1234, 567]
    })
    st.bar_chart(outcome_data.set_index('Outcome'))

elif page == "🔖 Bookmarks":
    st.title("🔖 Bookmarked Cases")
    
    if st.session_state.bookmarked_cases:
        st.markdown(f"You have {len(st.session_state.bookmarked_cases)} bookmarked cases.")
        
        for case_id in st.session_state.bookmarked_cases:
            case = next((c for c in CASES_DATABASE if c['id'] == case_id), None)
            if case:
                with st.expander(f"**{case['title']}**"):
                    st.markdown(render_case_tags(case), unsafe_allow_html=True)
                    st.markdown(f"**Summary:** {case['summary'][:200]}...")
                    
                    if st.button("Remove Bookmark", key=f"remove_{case_id}"):
                        st.session_state.bookmarked_cases.remove(case_id)
                        st.rerun()
    else:
        st.info("No bookmarked cases yet. Bookmark cases from the search results to see them here.")

elif page == "📄 Documents":
    st.title("📄 Document Library")
    
    uploaded_file = st.file_uploader(
        "Upload legal documents for analysis",
        type=['pdf', 'docx', 'txt'],
        accept_multiple_files=True
    )
    
    if uploaded_file:
        st.success(f"Uploaded {len(uploaded_file)} files successfully!")
        
        for file in uploaded_file:
            with st.expander(f"📄 {file.name}"):
                st.markdown(f"**File Size:** {file.size} bytes")
                st.markdown(f"**File Type:** {file.type}")
                
                if st.button(f"Analyze {file.name}", key=f"analyze_{file.name}"):
                    with st.spinner("Analyzing document..."):
                        time.sleep(3)
                        st.success("Document analyzed! Found 12 legal concepts and 3 case references.")

elif page == "👤 Admin":
    st.title("👤 Admin Dashboard")
    
    # User management
    st.markdown("### User Management")
    
    user_data = pd.DataFrame({
        'User': ['john.doe@law.com', 'jane.smith@legal.org', 'admin@caselens.com'],
        'Role': ['Researcher', 'Senior Associate', 'Administrator'],
        'Last Login': ['2024-07-01', '2024-07-02', '2024-07-02'],
        'Cases Accessed': [145, 289, 1024]
    })
    
    st.dataframe(user_data, use_container_width=True)
    
    # System settings
    st.markdown("### System Settings")
    
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Enable AI Question Answering", value=True)
        st.checkbox("Auto-backup Database", value=True)
        st.selectbox("Default Search Results", [10, 20, 50, 100], index=1)
    
    with col2:
        st.checkbox("Email Notifications", value=False)
        st.checkbox("Advanced Analytics", value=True)
        st.selectbox("Session Timeout (minutes)", [30, 60, 120, 240], index=2)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("*Caselens Legal Research Platform - Powered by AI*")
    st.markdown("© 2024 Caselens. All rights reserved.")
