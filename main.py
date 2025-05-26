import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide", initial_sidebar_state="expanded")

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'current_view_type' not in st.session_state:
    st.session_state.current_view_type = "card"
if 'current_filter' not in st.session_state:
    st.session_state.current_filter = "all"

# Custom CSS for the entire app
def inject_custom_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 100%;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom font family */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Custom button styling */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Custom selectbox styling */
    .stSelectbox > div > div {
        border-radius: 12px;
        border: 2px solid #e1e5e9;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Create data structures (same as original)
def get_argument_data():
    claimant_args = {
        "1": {
            "id": "1",
            "title": "Sporting Succession",
            "paragraphs": "15-18",
            "overview": {
                "points": [
                    "Analysis of multiple established criteria",
                    "Focus on continuous use of identifying elements",
                    "Public recognition assessment"
                ],
                "paragraphs": "15-16"
            },
            "factualPoints": [
                {
                    "point": "Continuous operation under same name since 1950",
                    "date": "1950-present",
                    "isDisputed": False,
                    "paragraphs": "18-19",
                    "exhibits": ["C-1", "C-2", "C-4", "R-1"],
                    "source_text": "The club has maintained continuous operation under the same name 'Athletic Club United' since its official registration in 1950, as evidenced by uninterrupted participation in national competitions and consistent use of the same corporate identity throughout this period.",
                    "page": 23,
                    "doc_name": "Statement of Appeal",
                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                }
            ],
            "evidence": [
                {
                    "id": "C-1",
                    "title": "Historical Registration Documents",
                    "summary": "Official records showing continuous name usage from 1950 to present day. Includes original registration certificate dated January 12, 1950, and all subsequent renewal documentation without interruption.",
                    "citations": ["20", "21", "24"]
                },
                {
                    "id": "C-2", 
                    "title": "Competition Participation Records",
                    "summary": "Complete records of the club's participation in national and regional competitions from 1950 to present, demonstrating uninterrupted competitive activity under the same name and organizational structure.",
                    "citations": ["25", "26", "28"]
                },
                {
                    "id": "C-4",
                    "title": "Media Coverage Archive", 
                    "summary": "Comprehensive collection of newspaper clippings, sports magazines, and media reports spanning 1950-2024 consistently referring to the club by the same name and recognizing its continuous identity.",
                    "citations": ["53", "54", "55"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2016/A/4576",
                    "title": "Criteria for sporting succession",
                    "relevance": "Establishes key factors for succession including: (1) continuous use of identifying elements, (2) public recognition of the entity's identity, (3) preservation of sporting records and achievements, and (4) consistent participation in competitions under the same identity.",
                    "paragraphs": "45-48",
                    "citedParagraphs": ["45", "46", "47"]
                }
            ]
        }
    }
    
    respondent_args = {
        "1": {
            "id": "1",
            "title": "Sporting Succession Rebuttal",
            "paragraphs": "200-218",
            "overview": {
                "points": [
                    "Challenge to claimed continuity of operations",
                    "Analysis of discontinuities in club operations",
                    "Dispute over public recognition factors"
                ],
                "paragraphs": "200-202"
            },
            "factualPoints": [
                {
                    "point": "Operations ceased between 1975-1976",
                    "date": "1975-1976",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "206-207",
                    "exhibits": ["R-1"],
                    "source_text": "The club's operations completely ceased during the 1975-1976 season, with no participation in any competitive events and complete absence from all official federation records during this period.",
                    "page": 89,
                    "doc_name": "Answer to Request for Provisional Measures",
                    "doc_summary": "Respondent's response challenging the appellant's claims and presenting evidence of operational discontinuity."
                }
            ],
            "evidence": [
                {
                    "id": "R-1",
                    "title": "Federation Records",
                    "summary": "Official competition records from the National Football Federation for the 1975-1976 season, showing complete absence of the club from all levels of competition that season.",
                    "citations": ["208", "209", "210"]
                }
            ]
        }
    }
    
    topics = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "argumentIds": ["1"]
        }
    ]
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args,
        "topics": topics
    }

# Get enhanced facts data
def get_all_facts():
    facts = [
        {
            'event': 'Club founded and officially registered',
            'date': '1950-01-12',
            'isDisputed': False,
            'claimant_submission': 'Athletic Club United was officially founded and registered with the National Football Federation on January 12, 1950, marking the beginning of its formal existence as a competitive sporting entity.',
            'respondent_submission': 'No specific counter-submission recorded',
            'exhibits': ['C-1', 'C-2'],
            'source_text': 'Athletic Club United was officially founded and registered with the National Football Federation on January 12, 1950.',
            'page': 15,
            'doc_name': 'Statement of Appeal',
            'parties_involved': ['Appellant']
        },
        {
            'event': 'Operations ceased between 1975-1976',
            'date': '1975-1976',
            'isDisputed': True,
            'claimant_submission': 'While there was a temporary administrative restructuring during 1975-1976 due to financial difficulties, the club\'s core operations and identity remained intact throughout this period.',
            'respondent_submission': 'Complete cessation of all club operations occurred during the 1975-1976 season, with no team fielded in any competition and complete absence from federation records.',
            'exhibits': ['C-2', 'R-1', 'R-2'],
            'source_text': 'Complete cessation of all club operations occurred during the 1975-1976 season.',
            'page': 127,
            'doc_name': 'Answer to Request for Provisional Measures',
            'parties_involved': ['Appellant', 'Respondent']
        },
        {
            'event': 'Club colors established as blue and white',
            'date': '1956-03-10',
            'isDisputed': True,
            'claimant_submission': 'The club\'s official colors were formally established as royal blue and white on March 10, 1956, following a unanimous decision by the club\'s founding committee.',
            'respondent_submission': 'The newly registered entity adopted a significantly different color scheme incorporating red and yellow as primary colors, abandoning the traditional blue and white entirely.',
            'exhibits': ['C-4', 'R-4'],
            'source_text': 'The club\'s official colors were formally established as royal blue and white on March 10, 1956.',
            'page': 67,
            'doc_name': 'Statement of Appeal',
            'parties_involved': ['Appellant', 'Respondent']
        },
        {
            'event': 'First National Championship won',
            'date': '1955-05-20',
            'isDisputed': False,
            'claimant_submission': 'Athletic Club United achieved its first National Championship victory on May 20, 1955, defeating rivals 3-1 in the final match held at National Stadium.',
            'respondent_submission': 'No specific counter-submission recorded',
            'exhibits': ['C-3'],
            'source_text': 'Athletic Club United achieved its first National Championship victory on May 20, 1955.',
            'page': 42,
            'doc_name': 'Appeal Brief',
            'parties_involved': ['Appellant']
        },
        {
            'event': 'New entity registered with similar name',
            'date': '1976-09-15',
            'isDisputed': True,
            'claimant_submission': 'The registration in 1976 was a continuation of the same legal entity under identical management and ownership, maintaining all historical rights and obligations.',
            'respondent_submission': 'A new sporting entity was registered on September 15, 1976, under the name \'Athletic Club United FC\' - notably different from the original \'Athletic Club United\'.',
            'exhibits': ['R-2'],
            'source_text': 'A new sporting entity was registered on September 15, 1976, under the name \'Athletic Club United FC\'.',
            'page': 162,
            'doc_name': 'Answer to Request for Provisional Measures',
            'parties_involved': ['Appellant', 'Respondent']
        }
    ]
    return facts

# Custom Card Component
def render_custom_card_view(facts_data):
    # Prepare facts data for JavaScript
    facts_json = json.dumps(facts_data)
    
    card_html = f"""
    <div id="facts-container">
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}
            
            body {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                background: #f8fafc;
                color: #1e293b;
            }}
            
            .facts-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
                gap: 24px;
                padding: 0;
                max-width: 100%;
            }}
            
            .fact-card {{
                background: white;
                border-radius: 16px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                overflow: hidden;
                border: 1px solid #e2e8f0;
                position: relative;
            }}
            
            .fact-card:hover {{
                transform: translateY(-4px);
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
            }}
            
            .fact-header {{
                padding: 24px;
                border-bottom: 1px solid #e2e8f0;
                position: relative;
            }}
            
            .fact-date {{
                display: inline-block;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 0.875rem;
                font-weight: 500;
                margin-bottom: 12px;
            }}
            
            .fact-title {{
                font-size: 1.25rem;
                font-weight: 600;
                color: #1e293b;
                line-height: 1.4;
                margin-bottom: 8px;
            }}
            
            .status-badge {{
                position: absolute;
                top: 24px;
                right: 24px;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 0.75rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.025em;
            }}
            
            .status-disputed {{
                background: #fee2e2;
                color: #dc2626;
            }}
            
            .status-undisputed {{
                background: #dcfce7;
                color: #16a34a;
            }}
            
            .fact-content {{
                padding: 0;
            }}
            
            .section {{
                padding: 24px;
                border-bottom: 1px solid #f1f5f9;
            }}
            
            .section:last-child {{
                border-bottom: none;
            }}
            
            .section-title {{
                font-size: 1rem;
                font-weight: 600;
                color: #374151;
                margin-bottom: 16px;
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            
            .submission-block {{
                margin-bottom: 20px;
            }}
            
            .submission-block:last-child {{
                margin-bottom: 0;
            }}
            
            .submission-label {{
                font-size: 0.875rem;
                font-weight: 600;
                margin-bottom: 8px;
                display: flex;
                align-items: center;
                gap: 6px;
            }}
            
            .submission-label.claimant {{
                color: #2563eb;
            }}
            
            .submission-label.respondent {{
                color: #dc2626;
            }}
            
            .submission-text {{
                background: #f8fafc;
                border-left: 4px solid #e2e8f0;
                padding: 16px;
                border-radius: 0 8px 8px 0;
                font-size: 0.9rem;
                line-height: 1.6;
                color: #475569;
                font-style: italic;
            }}
            
            .submission-text.claimant {{
                border-left-color: #3b82f6;
                background: #eff6ff;
            }}
            
            .submission-text.respondent {{
                border-left-color: #ef4444;
                background: #fef2f2;
            }}
            
            .evidence-list {{
                list-style: none;
                padding: 0;
            }}
            
            .evidence-item {{
                background: #f8fafc;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                padding: 16px;
                margin-bottom: 12px;
                transition: all 0.2s ease;
            }}
            
            .evidence-item:hover {{
                background: #f1f5f9;
                border-color: #cbd5e1;
            }}
            
            .evidence-item:last-child {{
                margin-bottom: 0;
            }}
            
            .evidence-id {{
                font-weight: 600;
                color: #6366f1;
                font-size: 0.875rem;
            }}
            
            .evidence-summary {{
                color: #64748b;
                font-size: 0.875rem;
                line-height: 1.5;
                margin-top: 4px;
            }}
            
            .meta-info {{
                display: flex;
                flex-wrap: wrap;
                gap: 16px;
                font-size: 0.8rem;
                color: #64748b;
                margin-top: 12px;
                padding-top: 12px;
                border-top: 1px solid #f1f5f9;
            }}
            
            .meta-item {{
                display: flex;
                align-items: center;
                gap: 6px;
            }}
            
            .icon {{
                width: 16px;
                height: 16px;
                opacity: 0.7;
            }}
            
            .no-content {{
                color: #94a3b8;
                font-style: italic;
                font-size: 0.875rem;
            }}
            
            @media (max-width: 768px) {{
                .facts-grid {{
                    grid-template-columns: 1fr;
                    gap: 16px;
                }}
                
                .fact-header {{
                    padding: 20px;
                }}
                
                .section {{
                    padding: 20px;
                }}
                
                .status-badge {{
                    position: static;
                    margin-top: 12px;
                    display: inline-block;
                }}
            }}
        </style>
        
        <div class="facts-grid" id="facts-grid">
            <!-- Facts will be populated by JavaScript -->
        </div>
    </div>
    
    <script>
        const factsData = {facts_json};
        
        function formatDate(dateStr) {{
            if (dateStr.includes('-')) {{
                const [year, month, day] = dateStr.split('-');
                if (day) {{
                    return new Date(year, month-1, day).toLocaleDateString('en-US', {{
                        year: 'numeric',
                        month: 'short',
                        day: 'numeric'
                    }});
                }}
            }}
            return dateStr;
        }}
        
        function createFactCard(fact) {{
            const disputedClass = fact.isDisputed ? 'disputed' : 'undisputed';
            const statusText = fact.isDisputed ? 'Disputed' : 'Undisputed';
            
            const evidenceHtml = fact.exhibits && fact.exhibits.length > 0 
                ? fact.exhibits.map(exhibit => `
                    <div class="evidence-item">
                        <div class="evidence-id">${{exhibit}}</div>
                        <div class="evidence-summary">Evidence reference</div>
                    </div>
                `).join('')
                : '<div class="no-content">No evidence references available</div>';
            
            return `
                <div class="fact-card">
                    <div class="fact-header">
                        <div class="fact-date">${{formatDate(fact.date)}}</div>
                        <div class="fact-title">${{fact.event}}</div>
                        <div class="status-badge status-${{disputedClass}}">${{statusText}}</div>
                    </div>
                    
                    <div class="fact-content">
                        <div class="section">
                            <div class="section-title">
                                📁 Evidence & References
                            </div>
                            <div class="evidence-list">
                                ${{evidenceHtml}}
                            </div>
                            ${{fact.doc_name ? `
                                <div class="meta-info">
                                    <div class="meta-item">
                                        <span class="icon">📄</span>
                                        Document: ${{fact.doc_name}}
                                    </div>
                                    ${{fact.page ? `
                                        <div class="meta-item">
                                            <span class="icon">📖</span>
                                            Page: ${{fact.page}}
                                        </div>
                                    ` : ''}}
                                </div>
                            ` : ''}}
                        </div>
                        
                        <div class="section">
                            <div class="section-title">
                                ⚖️ Party Submissions
                            </div>
                            
                            <div class="submission-block">
                                <div class="submission-label claimant">
                                    🔵 Claimant Submission
                                </div>
                                <div class="submission-text claimant">
                                    ${{fact.claimant_submission || 'No specific submission recorded'}}
                                </div>
                            </div>
                            
                            <div class="submission-block">
                                <div class="submission-label respondent">
                                    🔴 Respondent Submission
                                </div>
                                <div class="submission-text respondent">
                                    ${{fact.respondent_submission || 'No specific submission recorded'}}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }}
        
        function renderFacts() {{
            const container = document.getElementById('facts-grid');
            if (!container) return;
            
            const sortedFacts = factsData.sort((a, b) => {{
                const dateA = new Date(a.date.split('-')[0], 0, 1);
                const dateB = new Date(b.date.split('-')[0], 0, 1);
                return dateA - dateB;
            }});
            
            container.innerHTML = sortedFacts.map(createFactCard).join('');
        }}
        
        // Render facts when the DOM is ready
        if (document.readyState === 'loading') {{
            document.addEventListener('DOMContentLoaded', renderFacts);
        }} else {{
            renderFacts();
        }}
    </script>
    """
    
    components.html(card_html, height=800, scrolling=True)

# Custom Timeline Component
def render_custom_timeline_view(facts_data):
    facts_json = json.dumps(facts_data)
    
    timeline_html = f"""
    <div id="timeline-container">
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}
            
            body {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                background: #f8fafc;
                color: #1e293b;
            }}
            
            .timeline-wrapper {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                position: relative;
            }}
            
            .timeline {{
                position: relative;
                padding: 0;
            }}
            
            .timeline::before {{
                content: '';
                position: absolute;
                left: 50%;
                top: 0;
                bottom: 0;
                width: 4px;
                background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
                transform: translateX(-50%);
                border-radius: 2px;
            }}
            
            .timeline-item {{
                position: relative;
                margin-bottom: 60px;
                width: 100%;
            }}
            
            .timeline-item:last-child {{
                margin-bottom: 0;
            }}
            
            .timeline-content {{
                position: relative;
                width: calc(50% - 40px);
                background: white;
                border-radius: 16px;
                padding: 28px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                border: 1px solid #e2e8f0;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }}
            
            .timeline-content:hover {{
                transform: translateY(-4px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
            }}
            
            .timeline-item:nth-child(odd) .timeline-content {{
                margin-left: 0;
            }}
            
            .timeline-item:nth-child(even) .timeline-content {{
                margin-left: calc(50% + 40px);
            }}
            
            .timeline-date {{
                position: absolute;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 12px 20px;
                border-radius: 25px;
                font-weight: 600;
                font-size: 0.9rem;
                white-space: nowrap;
                box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
                z-index: 10;
            }}
            
            .timeline-arrow {{
                position: absolute;
                top: 50%;
                width: 0;
                height: 0;
                transform: translateY(-50%);
            }}
            
            .timeline-item:nth-child(odd) .timeline-arrow {{
                right: -16px;
                border-left: 16px solid white;
                border-top: 16px solid transparent;
                border-bottom: 16px solid transparent;
            }}
            
            .timeline-item:nth-child(even) .timeline-arrow {{
                left: -16px;
                border-right: 16px solid white;
                border-top: 16px solid transparent;
                border-bottom: 16px solid transparent;
            }}
            
            .event-title {{
                font-size: 1.3rem;
                font-weight: 700;
                color: #1e293b;
                margin-bottom: 16px;
                line-height: 1.4;
            }}
            
            .status-badge {{
                display: inline-block;
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 0.75rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                margin-bottom: 20px;
            }}
            
            .status-disputed {{
                background: linear-gradient(135deg, #fee2e2, #fecaca);
                color: #dc2626;
            }}
            
            .status-undisputed {{
                background: linear-gradient(135deg, #dcfce7, #bbf7d0);
                color: #16a34a;
            }}
            
            .submissions-section {{
                margin-top: 24px;
            }}
            
            .submission {{
                margin-bottom: 20px;
                padding: 20px;
                border-radius: 12px;
                border-left: 4px solid;
            }}
            
            .submission:last-child {{
                margin-bottom: 0;
            }}
            
            .submission.claimant {{
                background: linear-gradient(135deg, #eff6ff, #dbeafe);
                border-left-color: #3b82f6;
            }}
            
            .submission.respondent {{
                background: linear-gradient(135deg, #fef2f2, #fee2e2);
                border-left-color: #ef4444;
            }}
            
            .submission-label {{
                font-weight: 600;
                font-size: 0.9rem;
                margin-bottom: 8px;
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            
            .submission-label.claimant {{
                color: #1d4ed8;
            }}
            
            .submission-label.respondent {{
                color: #dc2626;
            }}
            
            .submission-text {{
                color: #475569;
                line-height: 1.6;
                font-size: 0.95rem;
                font-style: italic;
            }}
            
            .evidence-section {{
                margin-top: 20px;
                padding-top: 20px;
                border-top: 1px solid #e2e8f0;
            }}
            
            .evidence-title {{
                font-weight: 600;
                color: #374151;
                margin-bottom: 12px;
                font-size: 0.9rem;
                display: flex;
                align-items: center;
                gap: 6px;
            }}
            
            .evidence-tags {{
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
            }}
            
            .evidence-tag {{
                background: #f1f5f9;
                color: #475569;
                padding: 6px 12px;
                border-radius: 16px;
                font-size: 0.8rem;
                font-weight: 500;
                border: 1px solid #e2e8f0;
                transition: all 0.2s ease;
            }}
            
            .evidence-tag:hover {{
                background: #e2e8f0;
                border-color: #cbd5e1;
            }}
            
            @media (max-width: 768px) {{
                .timeline::before {{
                    left: 30px;
                }}
                
                .timeline-content {{
                    width: calc(100% - 80px);
                    margin-left: 80px !important;
                }}
                
                .timeline-date {{
                    left: 30px;
                    transform: translateY(-50%);
                    font-size: 0.8rem;
                    padding: 10px 16px;
                }}
                
                .timeline-arrow {{
                    display: none;
                }}
            }}
        </style>
        
        <div class="timeline-wrapper">
            <div class="timeline" id="timeline">
                <!-- Timeline items will be populated by JavaScript -->
            </div>
        </div>
    </div>
    
    <script>
        const timelineFacts = {facts_json};
        
        function formatTimelineDate(dateStr) {{
            if (dateStr.includes('-')) {{
                const [year, month, day] = dateStr.split('-');
                if (day) {{
                    return new Date(year, month-1, day).toLocaleDateString('en-US', {{
                        year: 'numeric',
                        month: 'short',
                        day: 'numeric'
                    }});
                }}
            }}
            return dateStr;
        }}
        
        function createTimelineItem(fact, index) {{
            const disputedClass = fact.isDisputed ? 'disputed' : 'undisputed';
            const statusText = fact.isDisputed ? 'Disputed' : 'Undisputed';
            
            const evidenceTags = fact.exhibits && fact.exhibits.length > 0 
                ? fact.exhibits.map(exhibit => `
                    <span class="evidence-tag">${{exhibit}}</span>
                `).join('')
                : '<span class="evidence-tag">No evidence</span>';
            
            return `
                <div class="timeline-item">
                    <div class="timeline-content">
                        <div class="timeline-arrow"></div>
                        
                        <div class="status-badge status-${{disputedClass}}">
                            ${{statusText}}
                        </div>
                        
                        <h3 class="event-title">${{fact.event}}</h3>
                        
                        <div class="submissions-section">
                            <div class="submission claimant">
                                <div class="submission-label claimant">
                                    🔵 Claimant Position
                                </div>
                                <div class="submission-text">
                                    ${{fact.claimant_submission || 'No specific submission recorded'}}
                                </div>
                            </div>
                            
                            <div class="submission respondent">
                                <div class="submission-label respondent">
                                    🔴 Respondent Position
                                </div>
                                <div class="submission-text">
                                    ${{fact.respondent_submission || 'No specific submission recorded'}}
                                </div>
                            </div>
                        </div>
                        
                        <div class="evidence-section">
                            <div class="evidence-title">
                                📁 Evidence References
                            </div>
                            <div class="evidence-tags">
                                ${{evidenceTags}}
                            </div>
                        </div>
                    </div>
                    
                    <div class="timeline-date">
                        ${{formatTimelineDate(fact.date)}}
                    </div>
                </div>
            `;
        }}
        
        function renderTimeline() {{
            const container = document.getElementById('timeline');
            if (!container) return;
            
            const sortedFacts = timelineFacts.sort((a, b) => {{
                const dateA = new Date(a.date.split('-')[0], 0, 1);
                const dateB = new Date(b.date.split('-')[0], 0, 1);
                return dateA - dateB;
            }});
            
            container.innerHTML = sortedFacts.map(createTimelineItem).join('');
        }}
        
        // Render timeline when DOM is ready
        if (document.readyState === 'loading') {{
            document.addEventListener('DOMContentLoaded', renderTimeline);
        }} else {{
            renderTimeline();
        }}
    </script>
    """
    
    components.html(timeline_html, height=1000, scrolling=True)

# Enhanced Sidebar with custom styling
def render_enhanced_sidebar():
    with st.sidebar:
        # Custom logo and branding
        st.markdown("""
        <div style="
            display: flex; 
            align-items: center; 
            margin-bottom: 30px;
            padding: 20px 10px;
            background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
            border-radius: 16px;
            backdrop-filter: blur(10px);
        ">
            <div style="
                width: 45px;
                height: 45px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-right: 15px;
                box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
            ">
                <span style="color: white; font-size: 20px; font-weight: bold;">⚖️</span>
            </div>
            <div>
                <h1 style="
                    margin: 0;
                    font-weight: 700;
                    color: white;
                    font-size: 1.4rem;
                    letter-spacing: -0.02em;
                ">CaseLens</h1>
                <p style="
                    margin: 0;
                    color: rgba(255,255,255,0.8);
                    font-size: 0.85rem;
                    font-weight: 400;
                ">Legal Analysis Platform</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation buttons with enhanced styling
        if st.button("📑 Arguments", key="args_button", use_container_width=True):
            st.session_state.view = "Arguments"
            st.rerun()
            
        if st.button("📊 Facts", key="facts_button", use_container_width=True):
            st.session_state.view = "Facts"
            st.rerun()
            
        if st.button("📁 Exhibits", key="exhibits_button", use_container_width=True):
            st.session_state.view = "Exhibits"
            st.rerun()
        
        st.markdown("---")
        
        # Filter section for Facts view
        if st.session_state.view == "Facts":
            st.markdown("### 🔍 Filters")
            
            filter_option = st.selectbox(
                "Filter by Status:",
                ["All Facts", "Disputed Facts", "Undisputed Facts"],
                index=0,
                key="fact_filter"
            )
            
            st.session_state.current_filter = filter_option.lower().replace(" ", "_")
            
            st.markdown("---")
            
            # View type selector
            st.markdown("### 👁️ View Options")
            
            view_type = st.radio(
                "Select View:",
                ["Card View", "Timeline View"],
                index=0 if st.session_state.current_view_type == "card" else 1,
                key="view_type_radio"
            )
            
            st.session_state.current_view_type = "card" if view_type == "Card View" else "timeline"

# Main application
def main():
    # Inject custom CSS
    inject_custom_css()
    
    # Render enhanced sidebar
    render_enhanced_sidebar()
    
    # Main content area
    if st.session_state.view == "Facts":
        # Page header with enhanced styling
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px 30px;
            border-radius: 20px;
            margin-bottom: 30px;
            color: white;
            text-align: center;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        ">
            <h1 style="
                margin: 0 0 10px 0;
                font-size: 2.5rem;
                font-weight: 700;
                letter-spacing: -0.02em;
            ">Case Facts Analysis</h1>
            <p style="
                margin: 0;
                font-size: 1.1rem;
                opacity: 0.9;
                font-weight: 400;
            ">Comprehensive view of all factual assertions and evidence</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Get and filter facts data
        all_facts = get_all_facts()
        
        if st.session_state.current_filter == "disputed_facts":
            filtered_facts = [fact for fact in all_facts if fact['isDisputed']]
        elif st.session_state.current_filter == "undisputed_facts":
            filtered_facts = [fact for fact in all_facts if not fact['isDisputed']]
        else:
            filtered_facts = all_facts
        
        # Display stats
        disputed_count = len([f for f in filtered_facts if f['isDisputed']])
        undisputed_count = len(filtered_facts) - disputed_count
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Facts", len(filtered_facts))
        with col2:
            st.metric("Disputed", disputed_count)
        with col3:
            st.metric("Undisputed", undisputed_count)
        
        st.markdown("---")
        
        # Render the appropriate view
        if st.session_state.current_view_type == "card":
            render_custom_card_view(filtered_facts)
        else:
            render_custom_timeline_view(filtered_facts)
    
    elif st.session_state.view == "Arguments":
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px 30px;
            border-radius: 20px;
            margin-bottom: 30px;
            color: white;
            text-align: center;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        ">
            <h1 style="
                margin: 0 0 10px 0;
                font-size: 2.5rem;
                font-weight: 700;
                letter-spacing: -0.02em;
            ">Legal Arguments</h1>
            <p style="
                margin: 0;
                font-size: 1.1rem;
                opacity: 0.9;
                font-weight: 400;
            ">Detailed analysis of party arguments and legal positions</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("🚧 Arguments view is under development. Coming soon with enhanced visualizations!")
    
    else:  # Exhibits view
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px 30px;
            border-radius: 20px;
            margin-bottom: 30px;
            color: white;
            text-align: center;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        ">
            <h1 style="
                margin: 0 0 10px 0;
                font-size: 2.5rem;
                font-weight: 700;
                letter-spacing: -0.02em;
            ">Evidence & Exhibits</h1>
            <p style="
                margin: 0;
                font-size: 1.1rem;
                opacity: 0.9;
                font-weight: 400;
            ">Comprehensive evidence library and document references</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("🚧 Exhibits view is under development. Coming soon with interactive document viewer!")

if __name__ == "__main__":
    main()
