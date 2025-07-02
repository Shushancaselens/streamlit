import streamlit as st
import pandas as pd
from datetime import datetime, date
import time

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
            {
                "excerpt": "Page 15 - 78. The Commentary on the RSTP states the following with regard to the concept of 'just cause': 'The definition of just cause and whether just cause exists shall be established in accordance with the merits of each particular case.",
                "full_context": "Page 15 - 77. The concept of just cause has been extensively developed through CAS jurisprudence and FIFA regulations. The FIFA Regulations on the Status and Transfer of Players (RSTP) provide the foundational framework for determining when a party may terminate a contract.\n\nPage 15 - 78. The Commentary on the RSTP states the following with regard to the concept of 'just cause': 'The definition of just cause and whether just cause exists shall be established in accordance with the merits of each particular case. Behaviour that is in violation of the terms of an employment contract cannot justify unilateral termination by the other party if such behaviour is of minor importance.'\n\nPage 15 - 79. Furthermore, the Commentary emphasizes that just cause must be of such gravity that the injured party cannot reasonably be expected to continue the employment relationship. This standard has been consistently applied by CAS panels in determining whether contract termination was justified."
            },
            {
                "excerpt": "Page 22 - 89. Non-payment of salary constitutes a breach of contract which may give rise to just cause for the employee to terminate the employment contract.",
                "full_context": "Page 22 - 88. The obligation to pay salary is a fundamental contractual duty in employment relationships. When an employer fails to meet this basic obligation, it strikes at the heart of the employment contract.\n\nPage 22 - 89. Non-payment of salary constitutes a breach of contract which may give rise to just cause for the employee to terminate the employment contract. The CAS has consistently held that when salary payments are delayed for a period exceeding two to three months, this constitutes a substantial breach sufficient to justify termination.\n\nPage 22 - 90. However, the employee must demonstrate that they have given the employer reasonable opportunity to remedy the breach and that the non-payment was not justified by any countervailing circumstances or legitimate disputes over the amount owed."
            },
            {
                "excerpt": "Page 31 - 105. The consistent jurisprudence of CAS establishes that just cause must be of such severity that the injured party cannot reasonably be expected to continue the contractual relationship.",
                "full_context": "Page 31 - 104. In assessing whether just cause exists, CAS panels must weigh all relevant circumstances, including the nature and severity of the breach, the conduct of both parties, and the overall context of the contractual relationship.\n\nPage 31 - 105. The consistent jurisprudence of CAS establishes that just cause must be of such severity that the injured party cannot reasonably be expected to continue the contractual relationship. This objective test requires careful analysis of whether a reasonable person in the same position would consider the breach sufficiently serious to warrant termination.\n\nPage 31 - 106. The Panel notes that minor infractions, isolated incidents, or breaches that can be readily remedied do not typically constitute just cause. The breach must fundamentally undermine the basis of the contractual relationship and make continued performance unreasonable or impossible."
            }
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
            {
                "excerpt": "Page 8 - 45. The solidarity mechanism ensures fair compensation for clubs investing in youth development.",
                "full_context": "Page 8 - 44. FIFA's solidarity mechanism is designed to reward clubs that contribute to the training and education of players throughout their career development.\n\nPage 8 - 45. The solidarity mechanism ensures fair compensation for clubs investing in youth development. When a player is transferred during the course of a contract, 5% of any compensation paid to the former club shall be distributed to the club(s) involved in the training and education of the player.\n\nPage 8 - 46. This system recognizes the financial investment made by clubs in developing young talent and ensures they receive appropriate compensation even when players move to other clubs."
            }
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
            {
                "excerpt": "Page 5 - 23. Strict liability applies regardless of intent in anti-doping cases.",
                "full_context": "Page 5 - 22. The World Anti-Doping Code establishes a comprehensive framework for anti-doping rule violations, with strict liability being a cornerstone principle of the system.\n\nPage 5 - 23. Strict liability applies regardless of intent in anti-doping cases. Athletes are responsible for any prohibited substance found in their samples, irrespective of how the substance entered their system or whether they intended to enhance their performance.\n\nPage 5 - 24. This principle ensures the integrity of sport by placing the burden of responsibility on athletes to ensure they do not consume prohibited substances, while also providing exceptions for cases involving no fault or negligence."
            }
        ],
        "similarity_score": 0.45
    }
]

def search_cases(query, max_results=20, similarity_threshold=0.5):
    """Simulate case search with relevant results"""
    relevant_cases = []
    for case in CASES_DATABASE:
        if query.lower() in case['summary'].lower() or query.lower() in case['court_reasoning'].lower():
            if case['similarity_score'] >= similarity_threshold:
                relevant_cases.append(case)
    return relevant_cases[:max_results]

def display_case_tags(case):
    """Display case metadata as badges using columns"""
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.info(f"📅 {case['date']}")
    with col2:
        st.info(f"⚖️ {case['procedure']}")
    with col3:
        st.info(f"📋 {case['matter']}")
    with col4:
        st.info(f"🏆 {case['category']}")
    with col5:
        if case['outcome'] == 'Dismissed':
            st.error(f"⚡ {case['outcome']}")
        elif case['outcome'] == 'Upheld':
            st.success(f"⚡ {case['outcome']}")
        else:
            st.warning(f"⚡ {case['outcome']}")
    with col6:
        st.success(f"⚽ {case['sport']}")

# Sidebar with Caselens branding
with st.sidebar:
    # Logo using columns for better alignment
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("## ⚖️")
    with col2:
        st.markdown("## caselens")
    
    st.divider()
    
    # Navigation using radio buttons
    st.markdown("### Navigation")
    page = st.radio(
        "Select page:",
        ["🔍 Search", "📄 Documents", "📊 Analytics", "🔖 Bookmarks", "👤 Admin"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.divider()
    
    if page == "🔍 Search":
        # Search Options
        st.markdown("### Search Options")
        
        st.markdown("**Max Results**")
        max_results = st.number_input(
            "Maximum number of results",
            min_value=1, 
            max_value=100, 
            value=20,
            label_visibility="collapsed"
        )
        
        st.markdown("**Similarity Threshold**")
        similarity = st.slider(
            "Minimum similarity score",
            min_value=0.0, 
            max_value=1.0, 
            value=0.55, 
            step=0.01,
            label_visibility="collapsed"
        )
        
        show_similarity = st.checkbox("Show Similarity Scores ⓘ")
        
        st.divider()
        
        # Advanced Filters in expander
        with st.expander("🔧 Advanced Filters"):
            date_range = st.date_input(
                "Date Range",
                value=[date(2010, 1, 1), date(2024, 12, 31)]
            )
            
            sport_filter = st.multiselect(
                "Sport",
                ["Football", "Basketball", "Tennis", "Swimming", "Athletics", "Hockey"]
            )
            
            outcome_filter = st.multiselect(
                "Outcome",
                ["Dismissed", "Upheld", "Partially Upheld", "Settled"]
            )
            
            procedure_filter = st.selectbox(
                "Procedure Type",
                ["All", "Appeal Arbitration", "Ordinary Arbitration", "Fast-Track"]
            )
        
        # Search History
        if st.session_state.search_history:
            st.markdown("### Recent Searches")
            for search in st.session_state.search_history[-5:]:
                if st.button(f"🔍 {search}", use_container_width=True):
                    st.session_state.current_search = search

# Main Content Area
if page == "🔍 Search":
    # Search Interface
    st.title("🔍 Legal Case Search")
    
    search_query = st.text_input(
        "Enter your search query:",
        value="just cause",
        placeholder="Enter your search query (e.g., contract termination, doping violation, transfer dispute)"
    )
    
    # Add to search history
    if search_query and search_query not in st.session_state.search_history:
        st.session_state.search_history.append(search_query)
    
    if search_query:
        # Perform search
        results = search_cases(search_query, max_results, similarity)
        
        # Search results summary
        st.success(f"✓ Found {len(results)} results")
        st.info(f"Found {len(results)} relevant passages in {len(results)} decisions")
        
        # Display results
        for i, case in enumerate(results):
            with st.expander(f"**{case['title']}**", expanded=(i == 0)):
                
                # Case tags using native components
                display_case_tags(case)
                
                st.markdown("---")
                
                # Case metadata
                st.markdown("**Case Details:**")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Appellants:** {case['appellants']}")
                    st.markdown(f"**Respondents:** {case['respondents']}")
                with col2:
                    st.markdown(f"**President:** {case['president']}")
                    st.markdown(f"**Arbitrators:** {case['arbitrator1']}, {case['arbitrator2']}")
                
                # Tabbed content for better organization
                tab1, tab2, tab3, tab4 = st.tabs(["📋 Summary", "⚖️ Court Reasoning", "📊 Case Outcome", "📖 Relevant Passages"])
                
                with tab1:
                    st.write(case['summary'])
                
                with tab2:
                    st.write(case['court_reasoning'])
                
                with tab3:
                    st.write(case['case_outcome'])
                
                with tab4:
                    st.markdown("**Relevant Passages:**")
                    for idx, passage in enumerate(case['relevant_passages']):
                        # Show excerpt in info box
                        st.info(passage['excerpt'])
                        
                        # Toggle for full context
                        show_context = st.checkbox(
                            "📖 Show full context", 
                            key=f"context_{case['id']}_{idx}"
                        )
                        
                        if show_context:
                            with st.container(border=True):
                                st.markdown("**Full Context:**")
                                st.text(passage['full_context'])
                
                # Similarity Score
                if show_similarity:
                    st.metric("Similarity Score", f"{case['similarity_score']:.2f}")
                
                st.markdown("---")
                
                # AI Question Interface
                st.markdown("**💬 Ask a Question About This Case**")
                question = st.text_area(
                    "Your question:",
                    placeholder="e.g., What was the main legal issue? What was the outcome? What were the key arguments?",
                    key=f"question_{case['id']}"
                )
                
                if st.button("Ask Question", key=f"ask_{case['id']}", type="primary"):
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
                            
                            st.success("**AI Answer:**")
                            st.write(answer)

elif page == "📊 Analytics":
    st.title("📊 Legal Analytics Dashboard")
    
    # Summary statistics using metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Cases", "15,847", "↗ 234")
    with col2:
        st.metric("Sports Covered", "23", "→ 0")
    with col3:
        st.metric("Cases Resolved", "89%", "↗ 2%")
    with col4:
        st.metric("Countries", "156", "↗ 3")
    
    # Charts using native streamlit charts
    st.markdown("### Case Trends")
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
        st.success(f"You have {len(st.session_state.bookmarked_cases)} bookmarked cases.")
        
        for case_id in st.session_state.bookmarked_cases:
            case = next((c for c in CASES_DATABASE if c['id'] == case_id), None)
            if case:
                with st.expander(f"**{case['title']}**"):
                    display_case_tags(case)
                    st.write(f"**Summary:** {case['summary'][:200]}...")
                    
                    if st.button("Remove Bookmark", key=f"remove_{case_id}"):
                        st.session_state.bookmarked_cases.remove(case_id)
                        st.rerun()
    else:
        st.info("No bookmarked cases yet. Bookmark cases from the search results to see them here.")

elif page == "📄 Documents":
    st.title("📄 Document Library")
    
    uploaded_files = st.file_uploader(
        "Upload legal documents for analysis",
        type=['pdf', 'docx', 'txt'],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.success(f"Uploaded {len(uploaded_files)} files successfully!")
        
        for file in uploaded_files:
            with st.expander(f"📄 {file.name}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("File Size", f"{file.size} bytes")
                with col2:
                    st.metric("File Type", file.type)
                
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
st.markdown("*Caselens Legal Research Platform - Powered by AI*")
st.markdown("© 2024 Caselens. All rights reserved.")
