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
    
    # Create a single HTML component containing the full UI with minimalistic design
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Minimalistic base styling */
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                margin: 0;
                padding: 0;
                background-color: #fff;
            }}
            
            /* Container */
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            /* Main title */
            .main-title {{
                font-size: 24px;
                font-weight: 600;
                margin-bottom: 20px;
            }}
            
            /* Tabs */
            .tabs {{
                display: flex;
                margin-bottom: 30px;
                border-bottom: 1px solid #eaeaea;
            }}
            
            .tab {{
                padding: 15px 20px;
                cursor: pointer;
                font-weight: 500;
                color: #666;
                position: relative;
            }}
            
            .tab.active {{
                color: #3182ce;
            }}
            
            .tab.active::after {{
                content: '';
                position: absolute;
                bottom: -1px;
                left: 0;
                right: 0;
                height: 3px;
                background-color: #3182ce;
            }}
            
            /* Columns for arguments */
            .arguments-container {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 30px;
                margin-top: 20px;
            }}
            
            .column-title {{
                font-size: 20px;
                font-weight: 500;
                margin-bottom: 20px;
            }}
            
            .claimant-title {{
                color: #3182ce;
            }}
            
            .respondent-title {{
                color: #e53e3e;
            }}
            
            /* Argument card */
            .argument-card {{
                display: flex;
                align-items: center;
                padding: 15px;
                border: 1px solid #eaeaea;
                border-radius: 8px;
                margin-bottom: 15px;
                cursor: pointer;
                transition: all 0.2s;
            }}
            
            .argument-card:hover {{
                background-color: #f9f9f9;
            }}
            
            .argument-card .caret {{
                margin-right: 10px;
                transition: transform 0.2s;
            }}
            
            .argument-card .caret.expanded {{
                transform: rotate(90deg);
            }}
            
            .argument-card .title {{
                flex: 1;
                font-weight: 500;
            }}
            
            /* Badges */
            .badge {{
                display: inline-block;
                padding: 4px 8px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 500;
            }}
            
            .claimant-badge {{
                background-color: rgba(49, 130, 206, 0.1);
                color: #3182ce;
            }}
            
            .respondent-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            /* Tab content container */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* Content inside an expanded argument */
            .argument-content {{
                margin-top: 15px;
                display: none;
            }}
            
            /* Subarguments */
            .subargument-list {{
                border-left: 2px solid #eaeaea;
                margin-left: 10px;
                padding-left: 15px;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Main title -->
            <h1 class="main-title">Legal Arguments Analysis</h1>
            
            <!-- Tabs -->
            <div class="tabs">
                <div class="tab active" data-tab="summary">Summary of Arguments</div>
                <div class="tab" data-tab="timeline">Timeline</div>
                <div class="tab" data-tab="exhibits">Exhibits</div>
            </div>
            
            <!-- Summary Tab -->
            <div id="summary-tab" class="tab-content active">
                <div class="arguments-container">
                    <!-- Claimant's Arguments -->
                    <div class="claimant-column">
                        <h2 class="column-title claimant-title">Claimant's Arguments</h2>
                        <div id="claimant-arguments"></div>
                    </div>
                    
                    <!-- Respondent's Arguments -->
                    <div class="respondent-column">
                        <h2 class="column-title respondent-title">Respondent's Arguments</h2>
                        <div id="respondent-arguments"></div>
                    </div>
                </div>
            </div>
            
            <!-- Timeline Tab -->
            <div id="timeline-tab" class="tab-content">
                <table id="timeline-table" style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Date</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Appellant's Version</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Respondent's Version</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Status</th>
                        </tr>
                    </thead>
                    <tbody id="timeline-body"></tbody>
                </table>
            </div>
            
            <!-- Exhibits Tab -->
            <div id="exhibits-tab" class="tab-content">
                <table id="exhibits-table" style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">ID</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Party</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Title</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Type</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Summary</th>
                        </tr>
                    </thead>
                    <tbody id="exhibits-body"></tbody>
                </table>
            </div>
        </div>
        
        <script>
            // Initialize data
            const argsData = {args_json};
            const timelineData = {timeline_json};
            const exhibitsData = {exhibits_json};
            
            // Tab switching
            document.querySelectorAll('.tab').forEach(tab => {{
                tab.addEventListener('click', function() {{
                    // Update active tab
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Show selected tab content
                    const tabId = this.getAttribute('data-tab') + '-tab';
                    document.querySelectorAll('.tab-content').forEach(content => {{
                        content.classList.remove('active');
                    }});
                    document.getElementById(tabId).classList.add('active');
                    
                    // Initialize content if needed
                    if (tabId === 'timeline-tab') renderTimeline();
                    if (tabId === 'exhibits-tab') renderExhibits();
                }});
            }});
            
            // Count subarguments in an argument
            function countSubarguments(arg) {{
                if (!arg || !arg.children) return 0;
                return Object.keys(arg.children).length;
            }}
            
            // Render main arguments list
            function renderMainArguments() {{
                const claimantContainer = document.getElementById('claimant-arguments');
                const respondentContainer = document.getElementById('respondent-arguments');
                
                // Clear containers
                claimantContainer.innerHTML = '';
                respondentContainer.innerHTML = '';
                
                // Render claimant arguments
                for (const [argId, arg] of Object.entries(argsData.claimantArgs)) {{
                    const subargCount = countSubarguments(arg);
                    const cardHtml = `
                        <div class="argument-card" id="claimant-arg-${{argId}}" onclick="toggleArgument('claimant', '${{argId}}')">
                            <div class="caret" id="claimant-caret-${{argId}}">▶</div>
                            <div class="title">${{arg.id}}. ${{arg.title}}</div>
                            ${{subargCount > 0 ? `<div class="badge claimant-badge">${{subargCount}} subarguments</div>` : ''}
                        </div>
                        <div class="argument-content" id="claimant-content-${{argId}}">
                            <div class="subargument-list" id="claimant-subargs-${{argId}}"></div>
                        </div>
                    `;
                    claimantContainer.innerHTML += cardHtml;
                }}
                
                // Render respondent arguments
                for (const [argId, arg] of Object.entries(argsData.respondentArgs)) {{
                    const subargCount = countSubarguments(arg);
                    const cardHtml = `
                        <div class="argument-card" id="respondent-arg-${{argId}}" onclick="toggleArgument('respondent', '${{argId}}')">
                            <div class="caret" id="respondent-caret-${{argId}}">▶</div>
                            <div class="title">${{arg.id}}. ${{arg.title}}</div>
                            ${{subargCount > 0 ? `<div class="badge respondent-badge">${{subargCount}} subarguments</div>` : ''}
                        </div>
                        <div class="argument-content" id="respondent-content-${{argId}}">
                            <div class="subargument-list" id="respondent-subargs-${{argId}}"></div>
                        </div>
                    `;
                    respondentContainer.innerHTML += cardHtml;
                }}
            }}
            
            // Toggle an argument's visibility
            function toggleArgument(side, argId) {{
                const contentEl = document.getElementById(`${{side}}-content-${{argId}}`);
                const caretEl = document.getElementById(`${{side}}-caret-${{argId}}`);
                
                if (contentEl.style.display === 'block') {{
                    contentEl.style.display = 'none';
                    caretEl.textContent = '▶';
                }} else {{
                    contentEl.style.display = 'block';
                    caretEl.textContent = '▼';
                    
                    // Render subarguments if there are any
                    const arg = side === 'claimant' ? argsData.claimantArgs[argId] : argsData.respondentArgs[argId];
                    if (arg.children && Object.keys(arg.children).length > 0) {{
                        renderSubarguments(side, argId, arg.children);
                    }}
                }}
                
                // Synchronize if it's a main argument
                if (argId === '1' || argId === '2') {{
                    const otherSide = side === 'claimant' ? 'respondent' : 'claimant';
                    const otherContentEl = document.getElementById(`${{otherSide}}-content-${{argId}}`);
                    const otherCaretEl = document.getElementById(`${{otherSide}}-caret-${{argId}}`);
                    
                    if (otherContentEl) {{
                        otherContentEl.style.display = contentEl.style.display;
                        otherCaretEl.textContent = caretEl.textContent;
                        
                        // Render other side's subarguments if there are any
                        const otherArg = otherSide === 'claimant' ? argsData.claimantArgs[argId] : argsData.respondentArgs[argId];
                        if (otherArg && otherArg.children && Object.keys(otherArg.children).length > 0 && contentEl.style.display === 'block') {{
                            renderSubarguments(otherSide, argId, otherArg.children);
                        }}
                    }}
                }}
            }}
            
            // Render subarguments
            function renderSubarguments(side, parentId, children) {{
                const container = document.getElementById(`${{side}}-subargs-${{parentId}}`);
                
                // Clear container if already has content
                if (container.innerHTML !== '') return;
                
                // Create HTML for each child
                for (const [childId, child] of Object.entries(children)) {{
                    const subargCount = countSubarguments(child);
                    const cardHtml = `
                        <div class="argument-card" style="margin-top: 10px;" id="${{side}}-arg-${{parentId}}-${{childId}}" onclick="event.stopPropagation(); toggleSubargument('${{side}}', '${{parentId}}', '${{childId}}')">
                            <div class="caret" id="${{side}}-caret-${{parentId}}-${{childId}}">▶</div>
                            <div class="title">${{child.id}}. ${{child.title}}</div>
                            ${{subargCount > 0 ? `<div class="badge ${{side === 'claimant' ? 'claimant-badge' : 'respondent-badge'}}">${{subargCount}} subarguments</div>` : ''}
                        </div>
                        <div class="argument-content" id="${{side}}-content-${{parentId}}-${{childId}}">
                            <div class="subargument-list" id="${{side}}-subargs-${{parentId}}-${{childId}}"></div>
                        </div>
                    `;
                    container.innerHTML += cardHtml;
                }}
            }}
            
            // Toggle a subargument's visibility
            function toggleSubargument(side, parentId, childId) {{
                const contentEl = document.getElementById(`${{side}}-content-${{parentId}}-${{childId}}`);
                const caretEl = document.getElementById(`${{side}}-caret-${{parentId}}-${{childId}}`);
                
                if (contentEl.style.display === 'block') {{
                    contentEl.style.display = 'none';
                    caretEl.textContent = '▶';
                }} else {{
                    contentEl.style.display = 'block';
                    caretEl.textContent = '▼';
                    
                    // Get the child argument
                    const parent = side === 'claimant' ? argsData.claimantArgs[parentId] : argsData.respondentArgs[parentId];
                    const child = parent.children[childId];
                    
                    // Render subarguments if there are any
                    if (child.children && Object.keys(child.children).length > 0) {{
                        renderNestedSubarguments(side, parentId, childId, child.children);
                    }}
                }}
            }}
            
            // Render nested subarguments
            function renderNestedSubarguments(side, parentId, childId, children) {{
                const container = document.getElementById(`${{side}}-subargs-${{parentId}}-${{childId}}`);
                
                // Clear container if already has content
                if (container.innerHTML !== '') return;
                
                // Create HTML for each nested child
                for (const [nestedId, nestedChild] of Object.entries(children)) {{
                    const fullId = `${{parentId}}-${{childId}}-${{nestedId}}`;
                    const cardHtml = `
                        <div class="argument-card" style="margin-top: 10px;" id="${{side}}-arg-${{fullId}}" onclick="event.stopPropagation();">
                            <div class="title">${{nestedChild.id}}. ${{nestedChild.title}}</div>
                        </div>
                    `;
                    container.innerHTML += cardHtml;
                }}
            }}
            
            // Render timeline
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
                
                // Skip if already rendered
                if (tbody.innerHTML !== '') return;
                
                tbody.innerHTML = '';
                
                timelineData.forEach(item => {{
                    const row = document.createElement('tr');
                    if (item.status === 'Disputed') {{
                        row.style.backgroundColor = 'rgba(229, 62, 62, 0.05)';
                    }}
                    
                    row.innerHTML = `
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.date}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.appellantVersion}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.respondentVersion}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.status}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Render exhibits
            function renderExhibits() {{
                const tbody = document.getElementById('exhibits-body');
                
                // Skip if already rendered
                if (tbody.innerHTML !== '') return;
                
                tbody.innerHTML = '';
                
                exhibitsData.forEach(item => {{
                    const row = document.createElement('tr');
                    
                    row.innerHTML = `
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.id}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">
                            <span class="badge ${{item.party === 'Appellant' ? 'claimant-badge' : 'respondent-badge'}}">${{item.party}}</span>
                        </td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.title}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.type}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.summary}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Initialize the page
            renderMainArguments();
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Legal Arguments Analysis")
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
