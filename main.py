import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Create data structures as JSON for embedded components
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
                    "exhibits": ["C-1"]
                }
            ],
            "evidence": [
                {
                    "id": "C-1",
                    "title": "Historical Registration Documents",
                    "summary": "Official records showing continuous name usage from 1950 to present day. Includes original registration certificate dated January 12, 1950, and all subsequent renewal documentation without interruption.",
                    "citations": ["20", "21", "24"]
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
            ],
            "children": {
                "1.1": {
                    "id": "1.1",
                    "title": "Club Name Analysis",
                    "paragraphs": "20-45",
                    "overview": {
                        "points": [
                            "Historical continuity of name usage",
                            "Legal protection of naming rights",
                            "Public recognition of club name"
                        ],
                        "paragraphs": "20-21"
                    },
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration History",
                            "paragraphs": "25-30",
                            "factualPoints": [
                                {
                                    "point": "Initial registration in 1950",
                                    "date": "1950",
                                    "isDisputed": False,
                                    "paragraphs": "25-26",
                                    "exhibits": ["C-2"]
                                },
                                {
                                    "point": "Brief administrative gap in 1975-1976",
                                    "date": "1975-1976",
                                    "isDisputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "29-30",
                                    "exhibits": ["C-2"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "C-2",
                                    "title": "Registration Records",
                                    "summary": "Comprehensive collection of official documentation showing the full registration history of the club from its founding to present day. Includes original application forms, government certificates, and renewal documentation.",
                                    "citations": ["25", "26", "28"]
                                }
                            ]
                        }
                    }
                },
                # [rest of the data structure remains unchanged]
            }
        },
        "2": {
            "id": "2",
            "title": "Doping Violation Chain of Custody",
            "paragraphs": "70-125",
            "overview": {
                "points": [
                    "Analysis of sample collection and handling procedures",
                    "Evaluation of laboratory testing protocols",
                    "Assessment of chain of custody documentation"
                ],
                "paragraphs": "70-72"
            }
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
                    "exhibits": ["R-1"]
                }
            ],
            "evidence": [
                {
                    "id": "R-1",
                    "title": "Federation Records",
                    "summary": "Official competition records from the National Football Federation for the 1975-1976 season, showing complete absence of the club from all levels of competition that season. Includes official withdrawal notification dated May 15, 1975.",
                    "citations": ["208", "209", "210"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2017/A/5465",
                    "title": "Operational continuity requirement",
                    "relevance": "Establishes that actual operational continuity (specifically participation in competitions) is the primary determinant of sporting succession, outweighing factors such as name, colors, or stadium usage when they conflict. The panel specifically ruled that a gap in competitive activity creates a presumption against continuity that must be overcome with substantial evidence.",
                    "paragraphs": "211-213",
                    "citedParagraphs": ["212"]
                }
            ],
            "children": {
                # [content remains unchanged]
            }
        },
        "2": {
            "id": "2",
            "title": "Doping Chain of Custody Defense",
            "paragraphs": "250-290",
            "overview": {
                "points": [
                    "Defense of sample collection procedures",
                    "Validation of laboratory testing protocols",
                    "Completeness of documentation"
                ],
                "paragraphs": "250-252"
            }
        }
    }
    
    topics = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "argumentIds": ["1"]
        },
        {
            "id": "topic-2",
            "title": "Doping Violation and Chain of Custody",
            "description": "Issues related to doping test procedures and evidence handling",
            "argumentIds": ["2"]
        }
    ]
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args,
        "topics": topics
    }

def get_timeline_data():
    return [
        {
            "date": "2023-01-15",
            "appellantVersion": "Contract signed with Club",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-03-20",
            "appellantVersion": "Player received notification of exclusion from team",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        # [other timeline items remain unchanged]
    ]

def get_exhibits_data():
    return [
        {
            "id": "C-1",
            "party": "Appellant",
            "title": "Employment Contract",
            "type": "contract",
            "summary": "Employment contract dated 15 January 2023 between Player and Club"
        },
        {
            "id": "C-2",
            "party": "Appellant",
            "title": "Termination Letter",
            "type": "letter",
            "summary": "Player's termination letter sent on 1 April 2023"
        },
        # [other exhibits remain unchanged]
    ]

# Main app
def main():
    # Get the data for JavaScript
    args_data = get_argument_data()
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    timeline_json = json.dumps(timeline_data)
    exhibits_json = json.dumps(exhibits_data)
    
    # Remove default Streamlit header/footer styling
    hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Create a single HTML component containing the full UI with updated minimalist design
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Base styling */
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                margin: 0;
                padding: 0;
                background-color: #fff;
            }}
            
            /* Search bar */
            .search-container {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 12px 16px;
                margin-bottom: 20px;
            }}
            
            .search-bar {{
                display: flex;
                align-items: center;
                width: 100%;
                max-width: 1200px;
                border: 1px solid #e2e8f0;
                border-radius: 25px;
                padding: 0 16px;
                background-color: #fff;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
            }}
            
            .search-icon {{
                color: #a0aec0;
                margin-right: 8px;
            }}
            
            .search-input {{
                width: 100%;
                padding: 12px 0;
                border: none;
                outline: none;
                font-size: 14px;
            }}
            
            .copy-button {{
                display: flex;
                align-items: center;
                padding: 8px 16px;
                margin-left: 16px;
                background-color: #f0f4ff;
                border: none;
                border-radius: 8px;
                color: #4f46e5;
                font-weight: 500;
                cursor: pointer;
            }}
            
            .copy-icon {{
                margin-right: 8px;
            }}
            
            /* Section container */
            .section-container {{
                margin-bottom: 16px;
                border: 1px solid #f0f0f0;
                border-radius: 8px;
                overflow: hidden;
            }}
            
            .section-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 16px;
                background-color: #fff;
                border-bottom: 1px solid #f0f0f0;
                cursor: pointer;
            }}
            
            .section-title {{
                font-size: 18px;
                font-weight: 600;
                margin: 0;
            }}
            
            .section-tag {{
                font-size: 12px;
                padding: 2px 8px;
                border-radius: 12px;
                background-color: #f7f7f7;
                color: #555;
            }}
            
            .section-content {{
                padding: 16px;
                background-color: #fff;
            }}
            
            /* Position columns */
            .positions-container {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 32px;
            }}
            
            .position-title {{
                font-size: 16px;
                margin-bottom: 16px;
            }}
            
            .appellant-color {{
                color: #4f46e5;
            }}
            
            .respondent-color {{
                color: #e11d48;
            }}
            
            .position-box {{
                background-color: #f9fafc;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 20px;
            }}
            
            .position-heading {{
                font-size: 16px;
                font-weight: 600;
                margin-top: 0;
                margin-bottom: 16px;
            }}
            
            /* Support points */
            .support-section-title {{
                font-size: 14px;
                font-weight: 500;
                margin-bottom: 12px;
                color: #555;
            }}
            
            .support-points-list {{
                list-style-type: none;
                padding-left: 0;
                margin-bottom: 20px;
            }}
            
            .support-point-item {{
                display: flex;
                margin-bottom: 8px;
                align-items: flex-start;
            }}
            
            .support-point-bullet {{
                margin-right: 12px;
                color: #a0aec0;
                flex-shrink: 0;
            }}
            
            /* Evidence */
            .evidence-section {{
                margin-top: 24px;
            }}
            
            .evidence-item {{
                display: flex;
                margin-bottom: 12px;
            }}
            
            .evidence-badge {{
                flex-shrink: 0;
                display: inline-block;
                padding: 4px 8px;
                margin-right: 12px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: 500;
            }}
            
            .appellant-badge {{
                background-color: #eff6ff;
                color: #4f46e5;
            }}
            
            .respondent-badge {{
                background-color: #fff1f2;
                color: #e11d48;
            }}
            
            .evidence-text {{
                flex-grow: 1;
            }}
            
            /* Case law */
            .case-law-section {{
                margin-top: 24px;
            }}
            
            .case-law-item {{
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                margin-bottom: 12px;
            }}
            
            .case-number {{
                font-weight: normal;
            }}
            
            .copy-icon-small {{
                cursor: pointer;
                color: #a0aec0;
            }}
            
            /* Tab navigation */
            .tabs {{
                display: flex;
                border-bottom: 1px solid #e2e8f0;
                margin-bottom: 24px;
            }}
            
            .tab {{
                padding: 12px 24px;
                font-weight: 500;
                color: #64748b;
                cursor: pointer;
                position: relative;
            }}
            
            .tab:hover {{
                color: #334155;
            }}
            
            .tab.active {{
                color: #4f46e5;
                box-shadow: inset 0 -2px 0 #4f46e5;
            }}
            
            /* Tab content */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* Chevron icon */
            .chevron {{
                transition: transform 0.2s ease;
            }}
            
            .chevron.up {{
                transform: rotate(180deg);
            }}
            
            /* Timeline & Exhibits tables */
            .data-table {{
                width: 100%;
                border-collapse: collapse;
                border: 1px solid #f1f5f9;
                border-radius: 8px;
                overflow: hidden;
            }}
            
            .data-table th {{
                text-align: left;
                padding: 12px 16px;
                background-color: #f8fafc;
                font-weight: 500;
                color: #64748b;
                border-bottom: 1px solid #e2e8f0;
            }}
            
            .data-table td {{
                padding: 12px 16px;
                border-bottom: 1px solid #f1f5f9;
                font-size: 14px;
            }}
            
            .data-table tr:last-child td {{
                border-bottom: none;
            }}
            
            .undisputed {{
                color: #10b981;
            }}
            
            .disputed {{
                color: #ef4444;
            }}
        </style>
    </head>
    <body>
        <!-- Search and Copy Bar -->
        <div class="search-container">
            <div class="search-bar">
                <div class="search-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                </div>
                <input type="text" id="global-search" class="search-input" placeholder="Search issues, arguments, or evidence...">
            </div>
            <button class="copy-button">
                <div class="copy-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                </div>
                Copy All
            </button>
        </div>
        
        <!-- Tab Navigation -->
        <div class="tabs">
            <div class="tab active" data-tab="arguments">Summary of Arguments</div>
            <div class="tab" data-tab="timeline">Timeline</div>
            <div class="tab" data-tab="exhibits">Exhibits</div>
        </div>
        
        <!-- Arguments Tab -->
        <div id="arguments" class="tab-content active">
            <!-- CAS Jurisdiction Section -->
            <div class="section-container">
                <div class="section-header" onclick="toggleSection('jurisdiction')">
                    <h2 class="section-title">CAS Jurisdiction</h2>
                    <div class="section-tag">jurisdiction</div>
                </div>
                <div id="jurisdiction-content" class="section-content">
                    <div class="positions-container">
                        <!-- Appellant's Position -->
                        <div>
                            <h3 class="position-title appellant-color">Appellant's Position</h3>
                            <div class="position-box">
                                <h4 class="position-heading">CAS Has Authority to Hear This Case</h4>
                                
                                <div>
                                    <h5 class="support-section-title">Supporting Points</h5>
                                    <ul class="support-points-list">
                                        <li class="support-point-item">
                                            <span class="support-point-bullet">•</span>
                                            <span>The Federation's Anti-Doping Rules explicitly allow CAS to hear appeals</span>
                                        </li>
                                        <li class="support-point-item">
                                            <span class="support-point-bullet">•</span>
                                            <span>Athlete has completed all required internal appeal procedures first</span>
                                        </li>
                                        <li class="support-point-item">
                                            <span class="support-point-bullet">•</span>
                                            <span>Athlete signed agreement allowing CAS to handle disputes</span>
                                        </li>
                                    </ul>
                                </div>
                                
                                <div class="evidence-section">
                                    <h5 class="support-section-title">Evidence</h5>
                                    <div class="evidence-item">
                                        <span class="evidence-badge appellant-badge">C1</span>
                                        <span class="evidence-text">Federation Rules, Art. 60</span>
                                    </div>
                                    <div class="evidence-item">
                                        <span class="evidence-badge appellant-badge">C2</span>
                                        <span class="evidence-text">Athlete's license containing arbitration agreement</span>
                                    </div>
                                    <div class="evidence-item">
                                        <span class="evidence-badge appellant-badge">C3</span>
                                        <span class="evidence-text">Appeal submission documents</span>
                                    </div>
                                </div>
                                
                                <div class="case-law-section">
                                    <h5 class="support-section-title">Case Law</h5>
                                    <div class="case-law-item">
                                        <span class="case-number">CAS 2019/A/XYZ</span>
                                        <span class="copy-icon-small">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                                            </svg>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Respondent's Position -->
                        <div>
                            <h3 class="position-title respondent-color">Respondent's Position</h3>
                            <div class="position-box">
                                <h4 class="position-heading">CAS Cannot Hear This Case Yet</h4>
                                
                                <div>
                                    <h5 class="support-section-title">Supporting Points</h5>
                                    <ul class="support-points-list">
                                        <li class="support-point-item">
                                            <span class="support-point-bullet">•</span>
                                            <span>Athlete skipped required steps in federation's appeal process</span>
                                        </li>
                                        <li class="support-point-item">
                                            <span class="support-point-bullet">•</span>
                                            <span>Athlete missed important appeal deadlines within federation</span>
                                        </li>
                                        <li class="support-point-item">
                                            <span class="support-point-bullet">•</span>
                                            <span>Must follow proper appeal steps before going to CAS</span>
                                        </li>
                                    </ul>
                                </div>
                                
                                <div class="evidence-section">
                                    <h5 class="support-section-title">Evidence</h5>
                                    <div class="evidence-item">
                                        <span class="evidence-badge respondent-badge">R1</span>
                                        <span class="evidence-text">Federation internal appeals process documentation</span>
                                    </div>
                                    <div class="evidence-item">
                                        <span class="evidence-badge respondent-badge">R2</span>
                                        <span class="evidence-text">Timeline of appeals process</span>
                                    </div>
                                    <div class="evidence-item">
                                        <span class="evidence-badge respondent-badge">R3</span>
                                        <span class="evidence-text">Federation handbook on procedures</span>
                                    </div>
                                </div>
                                
                                <div class="case-law-section">
                                    <h5 class="support-section-title">Case Law</h5>
                                    <div class="case-law-item">
                                        <span class="case-number">CAS 2019/A/123</span>
                                        <span class="copy-icon-small">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                                            </svg>
                                        </span>
                                    </div>
                                    <div class="case-law-item">
                                        <span class="case-number">CAS 2018/A/456</span>
                                        <span class="copy-icon-small">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                                            </svg>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Continue with other argument sections using the same template -->
            <div id="standard-arguments-container"></div>
        </div>
        
        <!-- Timeline Tab -->
        <div id="timeline" class="tab-content">
            <table id="timeline-table" class="data-table">
                <thead>
                    <tr>
                        <th>DATE</th>
                        <th>APPELLANT'S VERSION</th>
                        <th>RESPONDENT'S VERSION</th>
                        <th>STATUS</th>
                    </tr>
                </thead>
                <tbody id="timeline-body"></tbody>
            </table>
        </div>
        
        <!-- Exhibits Tab -->
        <div id="exhibits" class="tab-content">
            <table id="exhibits-table" class="data-table">
                <thead>
                    <tr>
                        <th>EXHIBIT ID</th>
                        <th>PARTY</th>
                        <th>TITLE</th>
                        <th>TYPE</th>
                        <th>SUMMARY</th>
                    </tr>
                </thead>
                <tbody id="exhibits-body"></tbody>
            </table>
        </div>
        
        <script>
            // Initialize data
            const argsData = {args_json};
            const timelineData = {timeline_json};
            const exhibitsData = {exhibits_json};
            
            // Keep track of expanded sections
            const expandedSections = {{
                'jurisdiction': true
            }};
            
            // Toggle section visibility
            function toggleSection(sectionId) {{
                const contentEl = document.getElementById(`${{sectionId}}-content`);
                expandedSections[sectionId] = !expandedSections[sectionId];
                
                if (expandedSections[sectionId]) {{
                    contentEl.style.display = 'block';
                }} else {{
                    contentEl.style.display = 'none';
                }}
            }}
            
            // Tab switching
            document.querySelectorAll('.tab').forEach(tab => {{
                tab.addEventListener('click', function() {{
                    // Update tabs
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Update content
                    const tabId = this.getAttribute('data-tab');
                    document.querySelectorAll('.tab-content').forEach(content => {{
                        content.style.display = 'none';
                    }});
                    document.getElementById(tabId).style.display = 'block';
                    
                    // Initialize content if needed
                    if (tabId === 'timeline') renderTimeline();
                    if (tabId === 'exhibits') renderExhibits();
                }});
            }});
            
            // Render timeline
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
                
                // Clear existing content
                tbody.innerHTML = '';
                
                // Render rows
                timelineData.forEach(item => {{
                    const row = document.createElement('tr');
                    
                    if (item.status === 'Disputed') {{
                        row.classList.add('disputed-row');
                    }}
                    
                    row.innerHTML = `
                        <td>${{item.date}}</td>
                        <td>${{item.appellantVersion}}</td>
                        <td>${{item.respondentVersion}}</td>
                        <td class="${{item.status.toLowerCase()}}">${{item.status}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Render exhibits
            function renderExhibits() {{
                const tbody = document.getElementById('exhibits-body');
                
                // Clear existing content
                tbody.innerHTML = '';
                
                // Render rows
                exhibitsData.forEach(item => {{
                    const row = document.createElement('tr');
                    const badgeClass = item.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge';
                    
                    row.innerHTML = `
                        <td><span class="evidence-badge ${{badgeClass}}">${{item.id}}</span></td>
                        <td>${{item.party}}</td>
                        <td>${{item.title}}</td>
                        <td>${{item.type}}</td>
                        <td>${{item.summary}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Initialize the page
            document.addEventListener('DOMContentLoaded', function() {{
                // Set up search functionality
                document.getElementById('global-search').addEventListener('input', function(e) {{
                    const searchTerm = e.target.value.toLowerCase();
                    // Implement search highlighting or filtering here
                }});
                
                // Initialize tables
                renderTimeline();
                renderExhibits();
            }});
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
