import streamlit as st
import pandas as pd
from datetime import datetime, date
import time
import random
import re

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

# Sample case database (expanded for better search demonstration)
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
    },
    {
        "id": "CAS_2012_A_2794",
        "title": "CAS 2012/A/2794",
        "date": "2013-03-15",
        "procedure": "Appeal Arbitration",
        "matter": "Doping",
        "category": "Award",
        "outcome": "Upheld",
        "sport": "Cycling",
        "appellants": "Alberto Contador",
        "respondents": "UCI & WADA",
        "president": "John Coates",
        "arbitrator1": "Romano Subiotto",
        "arbitrator2": "Quentin Byrnes-Studer",
        "summary": "Alberto Contador appealed his two-year suspension for testing positive for clenbuterol during the 2010 Tour de France. He claimed the positive test resulted from contaminated meat consumed in Spain. The UCI and WADA argued that regardless of the source, he was strictly liable for the presence of the prohibited substance in his system.",
        "court_reasoning": "The panel applied the principle of strict liability under the World Anti-Doping Code. While they accepted that contaminated meat could explain the presence of clenbuterol, this did not eliminate the athlete's responsibility. The panel found no significant fault or negligence that would reduce the standard two-year sanction for a first-time offense involving a specified substance.",
        "case_outcome": "The appeal was dismissed and the two-year period of ineligibility was confirmed. Contador was stripped of his 2010 Tour de France victory and all results from July 21, 2010, onwards were disqualified. The strict liability principle was upheld as fundamental to maintaining integrity in sport.",
        "relevant_passages": [
            {
                "excerpt": "Page 45 - 156. The principle of strict liability is fundamental to the anti-doping system and serves to ensure that athletes are responsible for what is in their bodies.",
                "full_context": "Page 45 - 155. The World Anti-Doping Code establishes a comprehensive framework for anti-doping violations and sanctions. Central to this framework is the principle of strict liability.\n\nPage 45 - 156. The principle of strict liability is fundamental to the anti-doping system and serves to ensure that athletes are responsible for what is in their bodies. This principle does not require proof of intent, fault, or knowledge on the part of the athlete.\n\nPage 45 - 157. While strict liability may seem harsh, it is necessary to maintain the integrity of sport and provide a level playing field for all competitors. Athletes must take all necessary precautions to ensure prohibited substances do not enter their systems."
            }
        ],
        "similarity_score": 0.92
    },
    {
        "id": "CAS_2015_A_4298",
        "title": "CAS 2015/A/4298",
        "date": "2016-06-21",
        "procedure": "Appeal Arbitration",
        "matter": "Transfer",
        "category": "Award",
        "outcome": "Partially Upheld",
        "sport": "Football",
        "appellants": "Real Madrid CF",
        "respondents": "FIFA",
        "president": "Luigi Fumagalli",
        "arbitrator1": "Goetz Eilers",
        "arbitrator2": "Manfred Nan",
        "summary": "Real Madrid challenged FIFA's decision imposing a transfer ban for irregularities in the international transfer and registration of minors. FIFA found that Real Madrid had breached regulations regarding the protection of minors by signing players under 18 from outside Spain without meeting the limited exceptions provided in the regulations.",
        "court_reasoning": "The panel confirmed that protecting minors in football is a legitimate and important objective. However, they found that some of FIFA's findings were not sufficiently substantiated by evidence. The panel reduced the sanction while maintaining the principle that clubs must strictly comply with regulations protecting minor players.",
        "case_outcome": "The appeal was partially successful. The transfer ban was reduced from two registration periods to one registration period. Real Madrid was also required to pay a reduced fine and implement enhanced compliance procedures for future minor transfers.",
        "relevant_passages": [
            {
                "excerpt": "Page 67 - 203. The protection of minors in international football transfers is a fundamental principle that must be strictly enforced.",
                "full_context": "Page 67 - 202. FIFA's regulations on the status and transfer of players include specific provisions designed to protect minor players from exploitation and ensure their welfare and education are prioritized.\n\nPage 67 - 203. The protection of minors in international football transfers is a fundamental principle that must be strictly enforced. Clubs have a responsibility to ensure full compliance with these regulations before engaging in any transfer involving players under the age of 18.\n\nPage 67 - 204. The limited exceptions to the general prohibition on international transfers of minors are narrowly construed and clubs must demonstrate clear compliance with all applicable criteria."
            }
        ],
        "similarity_score": 0.78
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
    
    .search-highlight {
        background-color: #fef3c7;
        padding: 1px 2px;
        border-radius: 2px;
    }
</style>
""", unsafe_allow_html=True)

def calculate_relevance_score(case, query_terms):
    """Calculate relevance score based on multiple factors"""
    score = 0
    query_lower = [term.lower() for term in query_terms]
    
    # Weight different fields differently
    field_weights = {
        'title': 3.0,
        'summary': 2.0,
        'court_reasoning': 2.0,
        'case_outcome': 1.5,
        'matter': 2.5,
        'sport': 1.0,
        'appellants': 1.5,
        'respondents': 1.5,
        'relevant_passages': 2.5
    }
    
    for field, weight in field_weights.items():
        if field == 'relevant_passages':
            # Search in all passages
            passage_text = ' '.join([p['excerpt'] + ' ' + p['full_context'] for p in case[field]])
            field_content = passage_text.lower()
        else:
            field_content = str(case[field]).lower()
        
        # Count exact phrase matches (higher weight)
        full_query = ' '.join(query_lower)
        if full_query in field_content:
            score += weight * 3
        
        # Count individual term matches
        for term in query_lower:
            if term in field_content:
                # Bonus for exact word matches
                if re.search(r'\b' + re.escape(term) + r'\b', field_content):
                    score += weight * 2
                else:
                    score += weight
    
    return score

def highlight_search_terms(text, query_terms):
    """Highlight search terms in text"""
    if not query_terms:
        return text
    
    highlighted_text = text
    for term in query_terms:
        if len(term) > 2:  # Only highlight terms longer than 2 characters
            pattern = re.compile(re.escape(term), re.IGNORECASE)
            highlighted_text = pattern.sub(f'<span class="search-highlight">{term}</span>', highlighted_text)
    
    return highlighted_text

def search_cases(query, max_results=20, similarity_threshold=0.5, sport_filter=None, matter_filter=None, date_range=None):
    """Enhanced case search with improved relevance scoring and filtering"""
    if not query.strip():
        return []
    
    # Parse query into terms
    query_terms = [term.strip() for term in query.split() if term.strip()]
    
    relevant_cases = []
    
    for case in CASES_DATABASE:
        # Apply filters first
        if sport_filter and sport_filter != "All" and case['sport'] != sport_filter:
            continue
        
        if matter_filter and matter_filter != "All" and case['matter'] != matter_filter:
            continue
        
        if date_range:
            case_date = datetime.strptime(case['date'], '%Y-%m-%d').date()
            if not (date_range[0] <= case_date <= date_range[1]):
                continue
        
        # Calculate relevance score
        relevance_score = calculate_relevance_score(case, query_terms)
        
        if relevance_score > 0:
            case_copy = case.copy()
            case_copy['relevance_score'] = relevance_score
            case_copy['similarity_score'] = min(relevance_score / 10, 1.0)  # Normalize to 0-1
            relevant_cases.append(case_copy)
    
    # Sort by relevance score (highest first)
    relevant_cases.sort(key=lambda x: x['relevance_score'], reverse=True)
    
    # Filter by similarity threshold
    relevant_cases = [case for case in relevant_cases if case['similarity_score'] >= similarity_threshold]
    
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
            similarity = st.slider("", min_value=0.0, max_value=1.0, value=0.25, step=0.01, label_visibility="collapsed")
            st.write(f"Current value: {similarity}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Advanced Filters
        st.markdown("### Filters")
        
        with st.container():
            st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
            st.markdown("**Sport**")
            sport_options = ["All"] + list(set([case['sport'] for case in CASES_DATABASE]))
            sport_filter = st.selectbox("", sport_options, label_visibility="collapsed", key="sport_filter")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
            st.markdown("**Matter Type**")
            matter_options = ["All"] + list(set([case['matter'] for case in CASES_DATABASE]))
            matter_filter = st.selectbox("", matter_options, label_visibility="collapsed", key="matter_filter")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
            st.markdown("**Date Range**")
            use_date_filter = st.checkbox("Enable date filter")
            if use_date_filter:
                start_date = st.date_input("From", date(2010, 1, 1))
                end_date = st.date_input("To", date.today())
                date_range = (start_date, end_date)
            else:
                date_range = None
            st.markdown('</div>', unsafe_allow_html=True)
        
        show_similarity = st.checkbox("Show Similarity Scores ⓘ")
        highlight_terms = st.checkbox("Highlight Search Terms", value=True)

# Main Content Area
if page == "🔍 Search":
    # Search Interface
    st.markdown("### Enter your search query")
    search_query = st.text_input(
        "", 
        value="just cause", 
        placeholder="Enter your search query (e.g., 'contract breach', 'doping violation', 'transfer ban')", 
        label_visibility="collapsed",
        key="search_input_updated"
    )
    
    # Add search history
    if search_query and search_query not in st.session_state.search_history:
        st.session_state.search_history.insert(0, search_query)
        st.session_state.search_history = st.session_state.search_history[:10]  # Keep last 10 searches
    
    # Quick search suggestions
    if st.session_state.search_history:
        st.markdown("**Recent searches:**")
        cols = st.columns(min(len(st.session_state.search_history), 3))
        for i, recent_query in enumerate(st.session_state.search_history[:3]):
            if cols[i % 3].button(f"🔍 {recent_query}", key=f"recent_{i}"):
                st.session_state.search_input_updated = recent_query
                st.rerun()
    
    if search_query:
        # Perform search with filters
        sport_filter_val = sport_filter if 'sport_filter' in locals() else None
        matter_filter_val = matter_filter if 'matter_filter' in locals() else None
        date_range_val = date_range if 'date_range' in locals() else None
        
        results = search_cases(
            search_query, 
            max_results, 
            similarity,
            sport_filter_val,
            matter_filter_val,
            date_range_val
        )
        
        # Search results summary
        if results:
            st.success(f"Found {len(results)} results")
            
            # Display search statistics
            if show_similarity:
                avg_score = sum(case['similarity_score'] for case in results) / len(results)
                st.info(f"Average relevance score: {avg_score:.2f}")
        else:
            st.warning("No results found. Try adjusting your search terms or filters.")
        
        # Display search results with clean formatting
        query_terms = search_query.split() if highlight_terms else []
        
        for case_index, case in enumerate(results):
            # Clean case header with bold descriptors
            case_title = f"**{case['title']}** | 📅 **Date:** {case['date']} | 👥 **Parties:** {case['appellants']} v. {case['respondents']} | 📝 **Matter:** {case['matter']} | 📄 **Outcome:** {case['outcome']} | 🏅 **Sport:** {case['sport']}"
            
            if show_similarity:
                case_title += f" | 🎯 **Score:** {case['similarity_score']:.2f}"
            
            with st.expander(case_title, expanded=(case_index == 0)):
                
                st.markdown(f"""
                **Procedure:** {case['procedure']}  
                **Category:** {case['category']}  
                **President:** {case['president']} | **Arbitrators:** {case['arbitrator1']}, {case['arbitrator2']}
                """)
                
                # Relevant Passages - Most important, moved to top
                st.markdown("### **Relevant Passages**")
                for passage_index, passage in enumerate(case['relevant_passages']):
                    passage_unique_key = f"show_more_{case['id']}_{passage_index}_{case_index}"
                    
                    # Extract page reference and content for excerpt (first page)
                    excerpt_text = passage['excerpt']
                    if highlight_terms:
                        excerpt_text = highlight_search_terms(excerpt_text, query_terms)
                    
                    if excerpt_text.startswith('Page'):
                        if '.' in excerpt_text:
                            page_ref = excerpt_text.split(' - ')[0] if ' - ' in excerpt_text else excerpt_text
                            content_parts = excerpt_text.split('.', 1)
                            content = content_parts[1].strip() if len(content_parts) > 1 else excerpt_text
                            
                            # Put page and checkbox on same line
                            show_more = st.checkbox(f"show more | **{page_ref}**", key=passage_unique_key)
                            
                            if show_more:
                                full_context = passage['full_context']
                                if highlight_terms:
                                    full_context = highlight_search_terms(full_context, query_terms)
                                st.success(full_context, unsafe_allow_html=True)
                            else:
                                st.success(content, unsafe_allow_html=True)
                        else:
                            st.success(excerpt_text, unsafe_allow_html=True)
                    else:
                        show_more = st.checkbox("show more", key=passage_unique_key)
                        if show_more:
                            full_context = passage['full_context']
                            if highlight_terms:
                                full_context = highlight_search_terms(full_context, query_terms)
                            st.success(full_context, unsafe_allow_html=True)
                        else:
                            st.success(excerpt_text, unsafe_allow_html=True)
                
                # Summary
                summary_text = case['summary']
                if highlight_terms:
                    summary_text = highlight_search_terms(summary_text, query_terms)
                st.info(f"**Summary:** {summary_text}", unsafe_allow_html=True)
                
                # Court Reasoning
                reasoning_text = case['court_reasoning']
                if highlight_terms:
                    reasoning_text = highlight_search_terms(reasoning_text, query_terms)
                st.warning(f"**Court Reasoning:** {reasoning_text}", unsafe_allow_html=True)
                
                # Case Outcome
                outcome_text = case['case_outcome']
                if highlight_terms:
                    outcome_text = highlight_search_terms(outcome_text, query_terms)
                
                with st.container():
                    st.markdown(f"""
                    <div style="
                        background-color: #f0f2f6; 
                        border-radius: 0.5rem; 
                        padding: 0.75rem 1rem;
                        margin: 0.5rem 0 1rem 0;
                        line-height: 1.6;
                    ">
                        <strong>Case Outcome:</strong> {outcome_text}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Bookmark functionality
                bookmark_key = f"bookmark_{case['id']}"
                is_bookmarked = case['id'] in st.session_state.bookmarked_cases
                bookmark_text = "🔖 Bookmarked" if is_bookmarked else "📌 Bookmark"
                
                if st.button(bookmark_text, key=bookmark_key):
                    if is_bookmarked:
                        st.session_state.bookmarked_cases.remove(case['id'])
                        st.success("Removed from bookmarks")
                    else:
                        st.session_state.bookmarked_cases.append(case['id'])
                        st.success("Added to bookmarks")
                    st.rerun()
                
                # AI Question Interface
                st.markdown("---")
                st.markdown("**Ask a Question About This Case**")
                question_unique_key = f"ai_question_{case['id']}_{case_index}"
                user_question = st.text_area(
                    "",
                    placeholder="e.g., What was the main legal issue?",
                    key=question_unique_key,
                    label_visibility="collapsed"
                )
                
                button_unique_key = f"ask_ai_{case['id']}_{case_index}"
                if st.button("Ask Question", key=button_unique_key):
                    if user_question:
                        with st.spinner("Analyzing case..."):
                            time.sleep(2)
                            
                            # Enhanced AI responses based on case content
                            if "legal issue" in user_question.lower():
                                ai_answer = f"The main legal issue in this case was {case['matter'].lower()}-related, specifically involving {case['summary'][:100]}..."
                            elif "outcome" in user_question.lower():
                                ai_answer = f"The case outcome was: {case['outcome']}. {case['case_outcome'][:150]}..."
                            elif "reasoning" in user_question.lower():
                                ai_answer = f"The court's reasoning focused on: {case['court_reasoning'][:200]}..."
                            else:
                                ai_answer = f"Based on the case details, this {case['matter'].lower()} dispute in {case['sport']} involved {case['appellants']} and {case['respondents']}, with the panel ultimately ruling that the appeal was {case['outcome'].lower()}."
                            
                            st.markdown(f"""
                            <div class="question-box">
                                <strong>AI Answer:</strong><br>
                                {ai_answer}
                            </div>
                            """, unsafe_allow_html=True)

elif page == "📊 Analytics":
    st.title("📊 Legal Analytics Dashboard")
    
    # Sample analytics data
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Cases", len(CASES_DATABASE), "2 new")
    
    with col2:
        st.metric("Contract Disputes", len([c for c in CASES_DATABASE if c['matter'] == 'Contract']), "1 new")
    
    with col3:
        st.metric("Success Rate", "67%", "5%")
    
    # Case distribution by sport
    sports_data = {}
    for case in CASES_DATABASE:
        sport = case['sport']
        sports_data[sport] = sports_data.get(sport, 0) + 1
    
    if sports_data:
        st.subheader("Cases by Sport")
        st.bar_chart(sports_data)

elif page == "🔖 Bookmarks":
    st.title("🔖 Bookmarked Cases")
    
    if st.session_state.bookmarked_cases:
        bookmarked_data = [case for case in CASES_DATABASE if case['id'] in st.session_state.bookmarked_cases]
        
        for case in bookmarked_data:
            with st.expander(f"**{case['title']}** | {case['date']} | {case['appellants']} v. {case['respondents']}"):
                st.write(f"**Matter:** {case['matter']} | **Outcome:** {case['outcome']}")
                st.write(f"**Summary:** {case['summary'][:200]}...")
                
                if st.button(f"Remove from bookmarks", key=f"remove_bookmark_{case['id']}"):
                    st.session_state.bookmarked_cases.remove(case['id'])
                    st.rerun()
    else:
        st.info("No bookmarked cases yet. Use the bookmark button when viewing search results.")

elif page == "📄 Documents":
    st.title("📄 Document Library")
    st.info("Upload legal documents for analysis.")
    
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'txt'])
    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

elif page == "👤 Admin":
    st.title("👤 Admin Dashboard")
    
    st.subheader("Search Statistics")
    if st.session_state.search_history:
        st.write("Recent search queries:")
        for i, query in enumerate(st.session_state.search_history[:5], 1):
            st.write(f"{i}. {query}")
    
    st.subheader("System Status")
    st.success("✅ Search engine operational")
    st.success("✅ Database connected")
    st.success(f"✅ {len(CASES_DATABASE)} cases indexed")
