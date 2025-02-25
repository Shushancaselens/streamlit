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
                "1.2": {
                    "id": "1.2",
                    "title": "Club Colors Analysis",
                    "paragraphs": "46-65",
                    "overview": {
                        "points": [
                            "Consistent use of club colors",
                            "Minor variations analysis",
                            "Color trademark protection"
                        ],
                        "paragraphs": "46-47"
                    },
                    "factualPoints": [
                        {
                            "point": "Consistent use of blue and white since founding",
                            "date": "1950-present",
                            "isDisputed": True,
                            "source": "Respondent",
                            "paragraphs": "51-52",
                            "exhibits": ["C-4"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "C-4",
                            "title": "Historical Photographs",
                            "summary": "Collection of 73 photographs spanning from 1950 to present day showing the team's uniforms, promotional materials, and stadium decorations. Images are chronologically arranged and authenticated by sports historians.",
                            "citations": ["53", "54", "55"]
                        }
                    ],
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Variations Analysis",
                            "paragraphs": "56-60",
                            "factualPoints": [
                                {
                                    "point": "Minor shade variations do not affect continuity",
                                    "date": "1970-1980",
                                    "isDisputed": False,
                                    "paragraphs": "56-57",
                                    "exhibits": ["C-5"]
                                },
                                {
                                    "point": "Temporary third color addition in 1980s",
                                    "date": "1982-1988",
                                    "isDisputed": False,
                                    "paragraphs": "58-59",
                                    "exhibits": ["C-5"]
                                }
                            ],
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Historical Color Documentation",
                                    "paragraphs": "61-65",
                                    "evidence": [
                                        {
                                            "id": "C-5",
                                            "title": "Color Archives",
                                            "summary": "Detailed color specification documents from club archives, including official style guides, manufacturer specifications, and board meeting minutes about uniform decisions from 1950 to present day.",
                                            "citations": ["61", "62", "63"]
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
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
                "1.1": {
                    "id": "1.1",
                    "title": "Club Name Analysis Rebuttal",
                    "paragraphs": "220-240",
                    "overview": {
                        "points": [
                            "Name registration discontinuities",
                            "Trademark ownership gaps",
                            "Analysis of public confusion"
                        ],
                        "paragraphs": "220-222"
                    },
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration Gap Evidence",
                            "paragraphs": "226-230",
                            "factualPoints": [
                                {
                                    "point": "Registration formally terminated on April 30, 1975",
                                    "date": "April 30, 1975",
                                    "isDisputed": False,
                                    "paragraphs": "226-227",
                                    "exhibits": ["R-2"]
                                },
                                {
                                    "point": "New entity registered on September 15, 1976",
                                    "date": "September 15, 1976",
                                    "isDisputed": False,
                                    "paragraphs": "228-229",
                                    "exhibits": ["R-2"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "R-2",
                                    "title": "Termination Certificate",
                                    "summary": "Official government certificate of termination for the original club entity, stamped and notarized on April 30, 1975, along with completely new registration documents for a separate legal entity filed on September 15, 1976, with different founding members and bylaws.",
                                    "citations": ["226", "227"]
                                }
                            ]
                        }
                    }
                },
                "1.2": {
                    "id": "1.2",
                    "title": "Club Colors Analysis Rebuttal",
                    "paragraphs": "241-249",
                    "overview": {
                        "points": [
                            "Significant color variations",
                            "Trademark registration gaps",
                            "Multiple competing color claims"
                        ],
                        "paragraphs": "241-242"
                    },
                    "factualPoints": [
                        {
                            "point": "Significant color scheme change in 1976",
                            "date": "1976",
                            "isDisputed": True,
                            "source": "Claimant",
                            "paragraphs": "245-246",
                            "exhibits": ["R-4"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "R-4",
                            "title": "Historical Photographs Comparison",
                            "summary": "Side-by-side comparison of team uniforms from 1974 (pre-dissolution) and 1976 (post-new registration), showing significant differences in shade, pattern, and design elements. Includes expert color analysis report from textile historian confirming different dye formulations were used.",
                            "citations": ["245", "246", "247"]
                        }
                    ],
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Changes Analysis",
                            "paragraphs": "247-249",
                            "factualPoints": [
                                {
                                    "point": "Pre-1976 colors represented original city district",
                                    "date": "1950-1975",
                                    "isDisputed": False,
                                    "paragraphs": "247",
                                    "exhibits": ["R-5"]
                                },
                                {
                                    "point": "Post-1976 colors represented new ownership region",
                                    "date": "1976-present",
                                    "isDisputed": True,
                                    "source": "Claimant",
                                    "paragraphs": "248-249",
                                    "exhibits": ["R-5"]
                                }
                            ],
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Color Identity Documentation",
                                    "paragraphs": "250-255",
                                    "evidence": [
                                        {
                                            "id": "R-5",
                                            "title": "Marketing Materials",
                                            "summary": "Collection of promotional materials, merchandise, and internal design documents from both pre-1975 and post-1976 periods, showing the deliberate change in color symbolism used in marketing campaigns and communications with fans.",
                                            "citations": ["250", "251", "252"]
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
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
        {
            "date": "2023-03-22",
            "appellantVersion": "Player requested explanation",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-04-01",
            "appellantVersion": "Player sent termination letter",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-04-05",
            "appellantVersion": "—",
            "respondentVersion": "Club rejected termination as invalid",
            "status": "Undisputed"
        },
        {
            "date": "2023-04-10",
            "appellantVersion": "Player was denied access to training facilities",
            "respondentVersion": "—",
            "status": "Disputed"
        },
        {
            "date": "2023-04-15",
            "appellantVersion": "—",
            "respondentVersion": "Club issued warning letter",
            "status": "Undisputed"
        },
        {
            "date": "2023-05-01",
            "appellantVersion": "Player filed claim with FIFA",
            "respondentVersion": "—",
            "status": "Undisputed"
        }
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
        {
            "id": "C-3",
            "party": "Appellant",
            "title": "Email Correspondence",
            "type": "communication",
            "summary": "Email exchanges between Player and Club from 22-30 March 2023"
        },
        {
            "id": "C-4",
            "party": "Appellant",
            "title": "Witness Statement",
            "type": "statement",
            "summary": "Statement from team captain confirming Player's exclusion"
        },
        {
            "id": "R-1",
            "party": "Respondent",
            "title": "Club Regulations",
            "type": "regulations",
            "summary": "Internal regulations of the Club dated January 2022"
        },
        {
            "id": "R-2",
            "party": "Respondent",
            "title": "Warning Letter",
            "type": "letter",
            "summary": "Warning letter issued to Player on 15 April 2023"
        },
        {
            "id": "R-3",
            "party": "Respondent",
            "title": "Training Schedule",
            "type": "schedule",
            "summary": "Team training schedule for March-April 2023"
        }
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
    
    # Hide default Streamlit elements
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Create a single HTML component containing the full UI
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
                padding: 16px;
                background-color: #fff;
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
                color: #4361EE;
                border-bottom: 2px solid #4361EE;
            }}
            
            /* Tab content sections */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* View toggle */
            .view-toggle {{
                display: flex;
                justify-content: flex-end;
                margin-bottom: 1rem;
            }}
            
            .view-toggle-container {{
                background-color: #f7fafc;
                border-radius: 0.375rem;
                padding: 0.25rem;
            }}
            
            .view-btn {{
                padding: 0.5rem 1rem;
                border-radius: 0.375rem;
                border: none;
                background: none;
                font-size: 0.875rem;
                font-weight: 500;
                cursor: pointer;
                color: #718096;
            }}
            
            .view-btn.active {{
                background-color: white;
                color: #4a5568;
                box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            }}
            
            /* Arguments styling */
            .arguments-header {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
                margin-bottom: 1rem;
            }}
            .claimant-color {{
                color: #4361EE;
            }}
            .respondent-color {{
                color: #E63946;
            }}
            
            /* Argument container and pairs */
            .argument-pair {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
                margin-bottom: 1rem;
                position: relative;
            }}
            .argument-side {{
                position: relative;
            }}
            
            /* Argument card and details */
            .argument {{
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                overflow: hidden;
                margin-bottom: 1rem;
            }}
            .argument-header {{
                padding: 12px 16px;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
                background: white;
            }}
            .argument-header-left {{
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            .argument-content {{
                padding: 16px;
                border-top: 1px solid #e2e8f0;
                display: none;
                background-color: white;
            }}
            
            /* Child arguments container */
            .argument-children {{
                padding-left: 1.5rem;
                display: none;
                position: relative;
            }}
            
            /* Connector lines for tree structure */
            .connector-vertical {{
                position: absolute;
                left: 0.75rem;
                top: 0;
                width: 1px;
                height: 100%;
                background-color: #e2e8f0;
            }}
            .connector-horizontal {{
                position: absolute;
                left: 0.75rem;
                top: 1.25rem;
                width: 0.75rem;
                height: 1px;
                background-color: #e2e8f0;
            }}
            .claimant-connector {{
                background-color: rgba(67, 97, 238, 0.5);
            }}
            .respondent-connector {{
                background-color: rgba(230, 57, 70, 0.5);
            }}
            
            /* Badge styling */
            .badge {{
                display: inline-block;
                padding: 2px 8px;
                border-radius: 16px;
                font-size: 12px;
            }}
            .claimant-badge {{
                background-color: #EFF6FF;
                color: #4361EE;
            }}
            .respondent-badge {{
                background-color: #FEF2F2;
                color: #E63946;
            }}
            .exhibit-badge {{
                background-color: #fef3c7;
                color: #d97706;
                margin-right: 0.25rem;
            }}
            .disputed-badge {{
                background-color: #fee2e2;
                color: #b91c1c;
            }}
            .type-badge {{
                background-color: #f1f5f9;
                color: #64748b;
            }}
            
            /* Lists */
            .points-list {{
                list-style-type: none;
                padding-left: 0;
                margin-bottom: 16px;
            }}
            .point-item {{
                display: flex;
                margin-bottom: 8px;
                align-items: flex-start;
            }}
            .point-marker {{
                color: #4361EE;
                margin-right: 8px;
                flex-shrink: 0;
            }}
            .resp-point-marker {{
                color: #E63946;
            }}
            
            /* Tables */
            .data-table {{
                width: 100%;
                border-collapse: collapse;
                background-color: white;
                border-radius: 8px;
                overflow: hidden;
                border: 1px solid #e2e8f0;
                margin-top: 16px;
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
                border-bottom: 1px solid #e2e8f0;
                font-size: 14px;
            }}
            .undisputed {{
                color: #10b981;
            }}
            .disputed {{
                color: #ef4444;
            }}
            
            /* Paragraph references */
            .para-ref {{
                display: inline-block;
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 12px;
                background-color: #EFF6FF;
                color: #4361EE;
            }}
            .resp-para-ref {{
                background-color: #FEF2F2;
                color: #E63946;
            }}
            
            /* Content section styling */
            .content-section {{
                margin-bottom: 16px;
            }}
            .content-section-title {{
                font-size: 14px;
                font-weight: 500;
                color: #555;
                margin-bottom: 8px;
            }}
        </style>
    </head>
    <body>
        <!-- Tab Navigation -->
        <div class="tabs">
            <div class="tab active" data-tab="arguments">Summary of Arguments</div>
            <div class="tab" data-tab="timeline">Timeline</div>
            <div class="tab" data-tab="exhibits">Exhibits</div>
        </div>
        
        <!-- Arguments Tab -->
        <div id="arguments" class="tab-content active">
            <div class="arguments-header">
                <h3 class="claimant-color">Claimant's Arguments</h3>
                <h3 class="respondent-color">Respondent's Arguments</h3>
            </div>
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
                        <th>ACTIONS</th>
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
            
            // Keep track of expanded states - we'll use an object to track the state of each argument by its full path ID
            const expandedStates = {{}};
            
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
            
            // Render overview points
            function renderOverviewPoints(overview) {{
                if (!overview || !overview.points || overview.points.length === 0) return '';
                
                const pointsHtml = overview.points.map(point => 
                    `<li class="point-item">
                        <span class="point-marker">•</span>
                        <span>${{point}}</span>
                    </li>`
                ).join('');
                
                return `
                <div class="content-section">
                    <h4 class="content-section-title">Key Points</h4>
                    <ul class="points-list">
                        ${{pointsHtml}}
                    </ul>
                    <span class="para-ref">¶${{overview.paragraphs}}</span>
                </div>
                `;
            }}
            
            // Render factual points
            function renderFactualPoints(points, isRespondent = false) {{
                if (!points || points.length === 0) return '';
                
                const markerClass = isRespondent ? 'resp-point-marker' : 'point-marker';
                const paraRefClass = isRespondent ? 'resp-para-ref' : 'para-ref';
                
                const pointsHtml = points.map(point => {{
                    const disputed = point.isDisputed 
                        ? `<span class="disputed-badge">Disputed by ${{point.source || ''}}</span>` 
                        : '';
                    
                    // Exhibits badges
                    const exhibitBadges = point.exhibits && point.exhibits.length > 0
                        ? point.exhibits.map(exhibitId => `<span class="exhibit-badge">${{exhibitId}}</span>`).join('')
                        : '';
                    
                    return `
                    <div class="content-section">
                        <div style="display: flex; align-items: center; margin-bottom: 4px;">
                            <span class="factual-tag">Factual</span>
                            ${{disputed}}
                        </div>
                        <div style="display: flex; align-items: center; margin-bottom: 8px;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#6B7280" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                <line x1="3" y1="10" x2="21" y2="10"></line>
                            </svg>
                            <span style="margin-left: 6px; font-size: 14px; color: #6B7280;">${{point.date}}</span>
                        </div>
                        <p style="margin-top: 0;">${{point.point}}</p>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="${{paraRefClass}}">¶${{point.paragraphs}}</span>
                            <div>
                                ${{exhibitBadges}}
                            </div>
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="content-section">
                    <h4 class="content-section-title">Factual Points</h4>
                    ${{pointsHtml}}
                </div>
                `;
            }}
            
            // Render evidence
            function renderEvidence(evidence, isRespondent = false) {{
                if (!evidence || evidence.length === 0) return '';
                
                const badgeClass = isRespondent ? 'respondent-badge' : 'claimant-badge';
                
                const itemsHtml = evidence.map(item => {{
                    const citations = item.citations 
                        ? item.citations.map(cite => `<span class="badge type-badge">¶${{cite}}</span>`).join(' ') 
                        : '';
                    
                    return `
                    <div style="margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div style="display: flex; align-items: center;">
                                <span class="badge ${{badgeClass}}" style="margin-right: 8px;">${{item.id}}</span>
                                <span style="font-weight: 500;">${{item.title}}</span>
                            </div>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                            </svg>
                        </div>
                        <p style="margin: 8px 0; color: #4B5563; font-size: 14px;">${{item.summary}}</p>
                        <div>
                            <span style="font-size: 12px; color: #6B7280; margin-right: 4px;">Cited in:</span>
                            ${{citations}}
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="content-section">
                    <h4 class="content-section-title">Evidence</h4>
                    ${{itemsHtml}}
                </div>
                `;
            }}
            
            // Render case law
            function renderCaseLaw(cases, isRespondent = false) {{
                if (!cases || cases.length === 0) return '';
                
                const paraRefClass = isRespondent ? 'resp-para-ref' : 'para-ref';
                
                const itemsHtml = cases.map(item => {{
                    const citedParagraphs = item.citedParagraphs 
                        ? item.citedParagraphs.map(para => `<span class="badge type-badge">¶${{para}}</span>`).join(' ') 
                        : '';
                    
                    return `
                    <div style="margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span>${{item.caseNumber}}</span>
                            <span class="${{paraRefClass}}">¶${{item.paragraphs}}</span>
                        </div>
                        <p style="margin: 8px 0 4px; font-weight: 500;">${{item.title}}</p>
                        <p style="margin: 0 0 8px; font-size: 14px; color: #4B5563;">${{item.relevance}}</p>
                        <div>
                            <span style="font-size: 12px; color: #6B7280; margin-right: 4px;">Key Paragraphs:</span>
                            ${{citedParagraphs}}
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="content-section">
                    <h4 class="content-section-title">Case Law</h4>
                    ${{itemsHtml}}
                </div>
                `;
            }}
            
            // Render argument content
            function renderArgumentContent(arg, isRespondent = false) {{
                let content = '';
                
                // Overview points
                if (arg.overview) {{
                    content += renderOverviewPoints(arg.overview, isRespondent);
                }}
                
                // Case law
                if (arg.caseLaw) {{
                    content += renderCaseLaw(arg.caseLaw, isRespondent);
                }}
                
                // Factual points
                if (arg.factualPoints) {{
                    content += renderFactualPoints(arg.factualPoints, isRespondent);
                }}
                
                // Evidence
                if (arg.evidence) {{
                    content += renderEvidence(arg.evidence, isRespondent);
                }}
                
                return content;
            }}
            
            // Render a single argument including its children
            function renderArgument(arg, side, path = '', level = 0) {{
                if (!arg) return '';
                
                const argId = path ? `${{path}}-${{arg.id}}` : arg.id;
                const fullId = `${{side}}-${{argId}}`;
                
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const childCount = hasChildren ? Object.keys(arg.children).length : 0;
                
                // Style based on side
                const isRespondent = side === 'respondent';
                const baseColor = isRespondent ? '#E63946' : '#4361EE';
                const badgeClass = isRespondent ? 'respondent-badge' : 'claimant-badge';
                const connectorClass = isRespondent ? 'respondent-connector' : 'claimant-connector';
                
                // Header content
                const headerHtml = `
                <div class="argument-header-left">
                    <svg id="chevron-${{fullId}}" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s ease;">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                    <span style="color: ${{baseColor}}; font-weight: 500;">${{arg.id}}. ${{arg.title}}</span>
                </div>
                <div>
                    ${{hasChildren 
                        ? `<span class="badge ${{badgeClass}}">${{childCount}} subarguments</span>` 
                        : ''
                    }}
                </div>
                `;
                
                // Detailed content
                const contentHtml = renderArgumentContent(arg, isRespondent);
                
                // Child arguments
                let childrenHtml = '';
                if (hasChildren) {{
                    const childrenArgs = Object.entries(arg.children).map(([childId, child]) => {{
                        // Pass the full path for this argument's children
                        return renderArgument(child, side, argId, level + 1);
                    }}).join('');
                    
                    childrenHtml = `
                    <div id="children-${{fullId}}" class="argument-children">
                        <div class="connector-vertical ${{connectorClass}}"></div>
                        ${{childrenArgs}}
                    </div>
                    `;
                }}
                
                // Complete argument HTML
                return `
                <div class="argument" style="${{level > 0 ? 'position: relative;' : ''}}">
                    ${{level > 0 ? `<div class="connector-horizontal ${{connectorClass}}"></div>` : ''}}
                    <div class="argument-header" onclick="toggleArgument('${{fullId}}', '${{argId}}')">
                        ${{headerHtml}}
                    </div>
                    <div id="content-${{fullId}}" class="argument-content">
                        ${{contentHtml}}
                    </div>
                    ${{childrenHtml}}
                </div>
                `;
            }}
            
            // Render a pair of arguments (claimant and respondent)
            function renderArgumentPair(claimantArg, respondentArg, topLevel = true) {{
                return `
                <div class="argument-pair">
                    <div class="argument-side">
                        ${{renderArgument(claimantArg, 'claimant')}}
                    </div>
                    <div class="argument-side">
                        ${{renderArgument(respondentArg, 'respondent')}}
                    </div>
                </div>
                `;
            }}
            
            // Render the standard arguments view
            function renderStandardArguments() {{
                const container = document.getElementById('standard-arguments-container');
                let html = '';
                
                // For each top-level argument
                Object.keys(argsData.claimantArgs).forEach(argId => {{
                    if (argsData.respondentArgs[argId]) {{
                        const claimantArg = argsData.claimantArgs[argId];
                        const respondentArg = argsData.respondentArgs[argId];
                        
                        html += renderArgumentPair(claimantArg, respondentArg);
                    }}
                }});
                
                container.innerHTML = html;
            }}
            
            // Toggle argument expansion - updated to handle nested paths
            function toggleArgument(fullId, argPath) {{
                // Determine the side (claimant or respondent)
                const [side, ...rest] = fullId.split('-');
                
                // Toggle this argument
                const contentEl = document.getElementById(`content-${{fullId}}`);
                const childrenEl = document.getElementById(`children-${{fullId}}`);
                const chevronEl = document.getElementById(`chevron-${{fullId}}`);
                
                const isExpanded = contentEl.style.display === 'block';
                contentEl.style.display = isExpanded ? 'none' : 'block';
                if (chevronEl) {{
                    chevronEl.style.transform = isExpanded ? '' : 'rotate(90deg)';
                }}
                if (childrenEl) {{
                    childrenEl.style.display = isExpanded ? 'none' : 'block';
                }}
                
                // Save expanded state
                expandedStates[fullId] = !isExpanded;
                
                // Find and toggle the paired argument based on the path
                const otherSide = side === 'claimant' ? 'respondent' : 'claimant';
                const pairedId = `${{otherSide}}-${{argPath}}`;
                
                const pairedContentEl = document.getElementById(`content-${{pairedId}}`);
                const pairedChildrenEl = document.getElementById(`children-${{pairedId}}`);
                const pairedChevronEl = document.getElementById(`chevron-${{pairedId}}`);
                
                if (pairedContentEl) {{
                    pairedContentEl.style.display = contentEl.style.display;
                    expandedStates[pairedId] = expandedStates[fullId];
                }}
                
                if (pairedChevronEl) {{
                    pairedChevronEl.style.transform = chevronEl.style.transform;
                }}
                
                if (pairedChildrenEl) {{
                    pairedChildrenEl.style.display = isExpanded ? 'none' : 'block';
                }}
            }}
            
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
                    const badgeClass = item.party === 'Appellant' ? 'claimant-badge' : 'respondent-badge';
                    
                    row.innerHTML = `
                        <td><span class="badge ${{badgeClass}}">${{item.id}}</span></td>
                        <td>${{item.party}}</td>
                        <td>${{item.title}}</td>
                        <td><span class="badge type-badge">${{item.type}}</span></td>
                        <td>${{item.summary}}</td>
                        <td style="text-align: right;"><a href="#" style="color: #4361EE; text-decoration: none;">View</a></td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Initialize the page
            document.addEventListener('DOMContentLoaded', function() {{
                // Initialize arguments
                renderStandardArguments();
                
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
