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
        "title": "CAS 2013/A/3165",
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
    
    .question-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    
    .sidebar-section {
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

def search_cases(query, max_results=20, similarity_threshold=0.5):
    """Simulate case search with relevant results"""
    relevant_cases = []
    for case in CASES_DATABASE:
        if query.lower() in case['summary'].lower() or query.lower() in case['court_reasoning'].lower():
            if case['similarity_score'] >= similarity_threshold:
                relevant_cases.append(case)
    
    return relevant_cases[:max_results]

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
    st.markdown("### 🧭 Navigation")
    page = st.radio(
        "",
        ["🔍 Search", "📄 Documents", "📊 Analytics", "🔖 Bookmarks", "👤 Admin"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Set default values
    max_results = 20
    similarity = 0.55
    show_similarity = False
    
    if page == "🔍 Search":
        # Search Options
        st.markdown("### 🎛️ Search Options")
        
        with st.container():
            st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
            st.markdown("**📊 Max Results**")
            max_results = st.number_input("", min_value=1, max_value=100, value=20, label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
            st.markdown("**🎯 Similarity Threshold**")
            similarity = st.slider("", min_value=0.0, max_value=1.0, value=0.55, step=0.01, label_visibility="collapsed")
            st.write(f"📈 Current value: {similarity}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        show_similarity = st.checkbox("📊 Show Similarity Scores ⓘ")

# Main Content Area
if page == "🔍 Search":
    # Search Interface
    st.markdown("### 🔍 Enter your search query")
    search_query = st.text_input(
        "", 
        value="just cause", 
        placeholder="🔎 Search for legal concepts, case names, or keywords...", 
        label_visibility="collapsed",
        key="search_input_updated"
    )
    
    if search_query:
        # Perform search
        results = search_cases(search_query, max_results, similarity)
        
        # Search results summary with emojis
        if len(results) > 0:
            st.success(f"🔍 Found {len(results)} matching cases!")
            st.markdown(f"📊 **Search Results:** {len(results)} relevant passages found in {len(results)} legal decisions")
        else:
            st.warning("🚫 No cases found matching your search criteria. Try adjusting your search terms or similarity threshold.")
            st.stop()
        
        # Display search results with clean formatting
        for case_index, case in enumerate(results):
            # Create colorful case descriptors using native Streamlit components
            st.markdown("---")
            
            # Case title with emoji
            st.markdown(f"### ⚖️ {case['title']}")
            
            # Create columns for descriptors with emojis
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("📅 Date", case['date'])
                st.metric("🏆 Outcome", case['outcome'])
            
            with col2:
                st.metric("📋 Matter Type", case['matter'])
                st.metric("⚽ Sport", case['sport'])
            
            with col3:
                st.metric("👨‍⚖️ Parties", f"{case['appellants']} v. {case['respondents']}")
                if show_similarity:
                    st.metric("🎯 Match Score", f"{case['similarity_score']:.0%}")
            
            # Enhanced colored text descriptors with more emojis
            outcome_emoji = "✅" if case['outcome'].lower() == "upheld" else "❌" if case['outcome'].lower() == "dismissed" else "⚖️"
            sport_emoji = "⚽" if case['sport'].lower() == "football" else "🏀" if case['sport'].lower() == "basketball" else "🏃"
            
            st.markdown(f"""
            **📊 Case Overview:**
            - 📅 **Date:** {case['date']} 
            - 👥 **Parties:** {case['appellants']} ⚔️ {case['respondents']}
            - 📋 **Matter:** {case['matter']} 
            - {outcome_emoji} **Outcome:** {case['outcome']} 
            - {sport_emoji} **Sport:** {case['sport']} 
            - 🏛️ **Procedure:** {case['procedure']}
            - 📂 **Category:** {case['category']}
            {f"- 🎯 **Similarity:** {case['similarity_score']:.0%}" if show_similarity else ""}
            """)
            
            # Panel composition with emojis
            st.markdown(f"""
            **👨‍⚖️ Arbitration Panel:**
            - 🎓 **President:** {case['president']}
            - ⚖️ **Arbitrator 1:** {case['arbitrator1']}
            - ⚖️ **Arbitrator 2:** {case['arbitrator2']}
            """)
            
            with st.expander("📖 View Full Case Details", expanded=(case_index == 0)):
                
                # Summary
                st.markdown("### 📝 Case Summary")
                st.info(case['summary'])
                
                # Court Reasoning
                st.markdown("### 🧠 Court Reasoning")
                st.warning(case['court_reasoning'])
                
                # Case Outcome
                st.markdown("### 🏆 Final Outcome")
                with st.container():
                    st.markdown(f"""
                    <div style="
                        background-color: #f0f2f6; 
                        border-radius: 0.5rem; 
                        padding: 0.75rem 1rem;
                        margin: 0.5rem 0 1rem 0;
                        line-height: 1.6;
                    ">
                        {case['case_outcome']}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Relevant Passages
                st.markdown("### 📚 Relevant Legal Passages")
                for passage_index, passage in enumerate(case['relevant_passages']):
                    passage_unique_key = f"show_context_{case['id']}_{passage_index}_{case_index}"
                    show_full_context = st.checkbox(f"📖 Show full context", key=passage_unique_key)
                    
                    if show_full_context:
                        st.success(passage['full_context'])
                    else:
                        st.success(passage['excerpt'])
                
                # AI Question Interface
                st.markdown("---")
                st.markdown("### 🤖 Ask AI About This Case")
                question_unique_key = f"ai_question_{case['id']}_{case_index}"
                user_question = st.text_area(
                    "",
                    placeholder="💭 e.g., What was the main legal issue? How did the court rule on just cause?",
                    key=question_unique_key,
                    label_visibility="collapsed"
                )
                
                button_unique_key = f"ask_ai_{case['id']}_{case_index}"
                if st.button("🚀 Ask Question", key=button_unique_key):
                    if user_question:
                        with st.spinner("🔍 Analyzing case details..."):
                            time.sleep(2)
                            ai_answer = f"🎯 Based on the case analysis, this relates to {case['matter'].lower()} issues in sports arbitration. The key legal principles involve contractual obligations and dispute resolution procedures under FIFA regulations."
                            
                            st.markdown(f"""
                            <div class="question-box">
                                <strong>🤖 AI Analysis:</strong><br>
                                {ai_answer}
                            </div>
                            """, unsafe_allow_html=True)

elif page == "📊 Analytics":
    st.title("📊 Legal Analytics Dashboard")
    st.info("📈 Advanced analytics features coming soon! Track case trends, success rates, and legal precedents.")

elif page == "🔖 Bookmarks":
    st.title("🔖 Bookmarked Cases")
    if len(st.session_state.bookmarked_cases) == 0:
        st.info("📌 No bookmarked cases yet. Start exploring cases and bookmark your favorites!")
    else:
        st.success(f"📚 You have {len(st.session_state.bookmarked_cases)} bookmarked cases")

elif page == "📄 Documents":
    st.title("📄 Document Library")
    st.info("📁 Upload and analyze legal documents here. PDF processing and AI analysis coming soon!")
    
    # Add file uploader
    uploaded_file = st.file_uploader("📎 Choose a legal document", type=['pdf', 'docx', 'txt'])
    if uploaded_file:
        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

elif page == "👤 Admin":
    st.title("👤 Admin Dashboard")
    st.info("🔧 Admin features coming soon. Manage users, system settings, and database configurations.")
    
    # Add some admin preview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("👥 Total Users", "1,234")
    with col2:
        st.metric("📚 Cases in Database", "15,678")
    with col3:
        st.metric("🔍 Searches Today", "892")
