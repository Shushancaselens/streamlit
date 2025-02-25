import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Sports Arbitration Case", layout="wide")

# Create data structures for sports arbitration case
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
                    "paragraphs": "15-17",
                    "citedParagraphs": ["15", "16", "17"]
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
                    "children": {}
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
                    "children": {}
                }
            }
        },
        "2": {
            "id": "2",
            "title": "Jurisdiction",
            "paragraphs": "70-85",
            "overview": {
                "points": [
                    "CAS has authority to hear this case",
                    "Federation rules explicitly allow appeals to CAS",
                    "Athlete has exhausted internal remedies"
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
                    "paragraphs": "203-205",
                    "citedParagraphs": ["203"]
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
                    "children": {}
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
                    "children": {}
                }
            }
        },
        "2": {
            "id": "2",
            "title": "Jurisdiction Challenge",
            "paragraphs": "250-265",
            "overview": {
                "points": [
                    "CAS cannot hear this case yet",
                    "Athlete skipped required steps in federation's appeal process",
                    "Procedural requirements must be followed"
                ],
                "paragraphs": "250-252"
            }
        }
    }
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args
    }

def get_timeline_data():
    return [
        {
            "date": "1950-01-12",
            "appellantVersion": "Original club registration",
            "respondentVersion": "Original club registration",
            "status": "Undisputed"
        },
        {
            "date": "1975-04-30",
            "appellantVersion": "Administrative restructuring",
            "respondentVersion": "Club dissolution",
            "status": "Disputed"
        },
        {
            "date": "1976-09-15",
            "appellantVersion": "Routine registration renewal",
            "respondentVersion": "New club formation",
            "status": "Disputed"
        },
        {
            "date": "1982-05-20",
            "appellantVersion": "Color variation introduced temporarily",
            "respondentVersion": "New color scheme implemented",
            "status": "Disputed"
        },
        {
            "date": "2022-12-10",
            "appellantVersion": "Appeal filed with CAS",
            "respondentVersion": "Premature CAS application",
            "status": "Disputed"
        }
    ]

def get_exhibits_data():
    return [
        {
            "id": "C-1",
            "party": "Claimant",
            "title": "Historical Registration Documents",
            "type": "official records",
            "summary": "Official records showing continuous name usage from 1950 to present day"
        },
        {
            "id": "C-2",
            "party": "Claimant",
            "title": "Federation Recognition Letters",
            "type": "correspondence",
            "summary": "Official correspondence from the Federation acknowledging club identity"
        },
        {
            "id": "C-3",
            "party": "Claimant",
            "title": "Club Colors Archive",
            "type": "photographs",
            "summary": "Historical photographs showing consistent team colors with minor variations"
        },
        {
            "id": "R-1",
            "party": "Respondent",
            "title": "Federation Records",
            "type": "official records",
            "summary": "Federation competition records showing absence from competition in 1975-1976"
        },
        {
            "id": "R-2",
            "party": "Respondent",
            "title": "Termination Certificate",
            "type": "official document",
            "summary": "Official government certificate of termination dated April 30, 1975"
        },
        {
            "id": "R-3",
            "party": "Respondent",
            "title": "New Entity Registration",
            "type": "official document",
            "summary": "Registration documents for a new legal entity filed on September 15, 1976"
        }
    ]

# Hide default Streamlit elements
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Main app
def main():
    # Get the data
    args_data = get_argument_data()
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    
    # Convert data to JSON for JavaScript
    args_json = json.dumps(args_data)
    timeline_json = json.dumps(timeline_data)
    exhibits_json = json.dumps(exhibits_data)
    
    # Create the UI
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Reset and base styles */
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}
            
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                max-width: 100%;
                background-color: #fff;
            }}
            
            /* Tab navigation */
            .tabs {{
                display: flex;
                border-bottom: 1px solid #e5e7eb;
                margin-bottom: 24px;
            }}
            
            .tab {{
                padding: 12px 24px;
                font-weight: 500;
                color: #6b7280;
                cursor: pointer;
                position: relative;
            }}
            
            .tab.active {{
                color: #4361ee;
                border-bottom: 2px solid #4361ee;
            }}
            
            /* Tab content */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* Column layout */
            .column-headers {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 24px;
                margin-bottom: 16px;
            }}
            
            .column-heading {{
                font-size: 18px;
                font-weight: 600;
            }}
            
            .two-columns {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 24px;
                margin-bottom: 24px;
            }}
            
            /* Color scheme */
            .claimant-color {{
                color: #4361ee;
            }}
            
            .respondent-color {{
                color: #e63946;
            }}
            
            /* Argument cards */
            .argument-card {{
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                margin-bottom: 16px;
                overflow: hidden;
            }}
            
            .argument-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 12px 16px;
                cursor: pointer;
                background-color: #fff;
            }}
            
            .argument-title {{
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            
            .chevron {{
                transition: transform 0.2s;
            }}
            
            .chevron.expanded {{
                transform: rotate(90deg);
            }}
            
            .subarg-badge {{
                padding: 2px 8px;
                border-radius: 16px;
                font-size: 12px;
                font-weight: normal;
            }}
            
            .claimant-badge {{
                background-color: #eff6ff;
                color: #4361ee;
            }}
            
            .respondent-badge {{
                background-color: #fef2f2;
                color: #e63946;
            }}
            
            .argument-content {{
                padding: 16px;
                border-top: 1px solid #e5e7eb;
                display: none;
            }}
            
            /* Points lists */
            .points-title {{
                font-size: 16px;
                font-weight: 500;
                margin-bottom: 12px;
            }}
            
            .points-list {{
                list-style-type: none;
                margin-bottom: 16px;
            }}
            
            .point-item {{
                display: flex;
                margin-bottom: 8px;
                align-items: flex-start;
            }}
            
            .point-bullet {{
                color: #4361ee;
                margin-right: 8px;
                flex-shrink: 0;
            }}
            
            .resp-point-bullet {{
                color: #e63946;
            }}
            
            /* Paragraph references */
            .para-ref {{
                display: inline-block;
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 12px;
                background-color: #eff6ff;
                color: #4361ee;
                margin-left: 8px;
            }}
            
            .resp-para-ref {{
                background-color: #fef2f2;
                color: #e63946;
            }}
            
            /* Legal points */
            .legal-tag {{
                display: inline-block;
                font-size: 12px;
                padding: 2px 8px;
                border-radius: 4px;
                background-color: #f3f4f6;
                color: #6b7280;
                margin-bottom: 8px;
            }}
            
            .legal-content {{
                background-color: #f9fafb;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 16px;
            }}
            
            /* Factual points */
            .factual-tag {{
                display: inline-block;
                font-size: 12px;
                padding: 2px 8px;
                border-radius: 4px;
                background-color: #ecfdf5;
                color: #059669;
                margin-bottom: 8px;
            }}
            
            .date-tag {{
                display: inline-flex;
                align-items: center;
                font-size: 12px;
                color: #6b7280;
                margin-bottom: 8px;
                margin-left: 8px;
            }}
            
            .factual-content {{
                background-color: #f0fdf4;
                padding: 16px;
                border-radius: 8px;
                margin-bottom: 16px;
            }}
            
            .disputed-tag {{
                display: inline-block;
                font-size: 12px;
                padding: 2px 8px;
                border-radius: 4px;
                background-color: #fee2e2;
                color: #b91c1c;
                margin-left: 8px;
            }}
            
            /* Evidence section */
            .evidence-section {{
                margin-top: 16px;
            }}
            
            .evidence-item {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 12px;
            }}
            
            .evidence-id {{
                display: inline-block;
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 12px;
                margin-right: 8px;
            }}
            
            /* Timeline & Exhibits tables */
            .data-table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 16px;
                background-color: white;
                border-radius: 8px;
                overflow: hidden;
                border: 1px solid #e5e7eb;
            }}
            
            .data-table th {{
                text-align: left;
                padding: 12px 16px;
                background-color: #f9fafb;
                font-weight: 500;
                color: #6b7280;
                border-bottom: 1px solid #e5e7eb;
            }}
            
            .data-table td {{
                padding: 12px 16px;
                border-bottom: 1px solid #e5e7eb;
                font-size: 14px;
            }}
            
            .data-table tr:last-child td {{
                border-bottom: none;
            }}
            
            .undisputed {{
                color: #059669;
            }}
            
            .disputed {{
                color: #dc2626;
            }}
            
            /* Icons for copy/link */
            .copy-icon {{
                cursor: pointer;
                color: #9ca3af;
            }}
            
            .copy-icon:hover {{
                color: #6b7280;
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
            <div class="column-headers">
                <h2 class="column-heading claimant-color">Claimant's Arguments</h2>
                <h2 class="column-heading respondent-color">Respondent's Arguments</h2>
            </div>
            
            <div class="two-columns">
                <!-- Claimant Arguments -->
                <div>
                    <!-- Sporting Succession -->
                    <div class="argument-card">
                        <div class="argument-header" onclick="toggleArgument('claimant-1')">
                            <div class="argument-title">
                                <svg class="chevron" id="chevron-claimant-1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <span style="color: #4361ee; font-weight: 500;">1. Sporting Succession</span>
                            </div>
                            <span class="subarg-badge claimant-badge">2 subarguments</span>
                        </div>
                        <div id="content-claimant-1" class="argument-content">
                            <!-- Key Points -->
                            <div>
                                <h3 class="points-title">Key Points</h3>
                                <ul class="points-list">
                                    <li class="point-item">
                                        <span class="point-bullet">•</span>
                                        <span>Analysis of multiple established criteria <span class="para-ref">¶15-16</span></span>
                                    </li>
                                    <li class="point-item">
                                        <span class="point-bullet">•</span>
                                        <span>Focus on continuous use of identifying elements</span>
                                    </li>
                                    <li class="point-item">
                                        <span class="point-bullet">•</span>
                                        <span>Public recognition assessment</span>
                                    </li>
                                </ul>
                            </div>
                            
                            <!-- Legal Points -->
                            <div>
                                <h3 class="points-title">Legal Points</h3>
                                <div>
                                    <span class="legal-tag">Legal</span>
                                    <div class="legal-content">
                                        <p>CAS jurisprudence establishes criteria for sporting succession</p>
                                        <div style="display: flex; justify-content: space-between; margin-top: 8px;">
                                            <span>CAS 2016/A/4576</span>
                                            <span class="para-ref">¶15-17</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Factual Points -->
                            <div>
                                <h3 class="points-title">Factual Points</h3>
                                <div>
                                    <div style="display: flex; align-items: center;">
                                        <span class="factual-tag">Factual</span>
                                        <span class="date-tag">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;">
                                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                                <line x1="3" y1="10" x2="21" y2="10"></line>
                                            </svg>
                                            1950-present
                                        </span>
                                    </div>
                                    <div class="factual-content">
                                        <p>Continuous operation under same name since 1950</p>
                                        <div style="display: flex; justify-content: space-between; margin-top: 8px;">
                                            <span class="para-ref">¶18-19</span>
                                            <span class="evidence-id claimant-badge">C-1</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Evidence -->
                            <div>
                                <h3 class="points-title">Evidence</h3>
                                <div class="evidence-item">
                                    <div>
                                        <div style="display: flex; align-items: center;">
                                            <span class="evidence-id claimant-badge">C-1</span>
                                            <strong>Historical Registration Documents</strong>
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="copy-icon" style="margin-left: 8px;">
                                                <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                                <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                                            </svg>
                                        </div>
                                        <p style="margin-top: 4px; color: #6b7280; font-size: 14px;">Official records showing continuous name usage from 1950 to present day.</p>
                                        <div style="margin-top: 4px; font-size: 12px; color: #6b7280;">
                                            <span>Cited in:</span>
                                            <span style="margin-left: 4px; background-color: #f3f4f6; padding: 2px 6px; border-radius: 4px;">¶20</span>
                                            <span style="margin-left: 4px; background-color: #f3f4f6; padding: 2px 6px; border-radius: 4px;">¶21</span>
                                            <span style="margin-left: 4px; background-color: #f3f4f6; padding: 2px 6px; border-radius: 4px;">¶24</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Jurisdiction -->
                    <div class="argument-card">
                        <div class="argument-header" onclick="toggleArgument('claimant-2')">
                            <div class="argument-title">
                                <svg class="chevron" id="chevron-claimant-2" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <span style="color: #4361ee; font-weight: 500;">2. Jurisdiction</span>
                            </div>
                        </div>
                        <div id="content-claimant-2" class="argument-content">
                            <!-- Key Points -->
                            <div>
                                <h3 class="points-title">Key Points</h3>
                                <ul class="points-list">
                                    <li class="point-item">
                                        <span class="point-bullet">•</span>
                                        <span>CAS has authority to hear this case <span class="para-ref">¶70-72</span></span>
                                    </li>
                                    <li class="point-item">
                                        <span class="point-bullet">•</span>
                                        <span>Federation rules explicitly allow appeals to CAS</span>
                                    </li>
                                    <li class="point-item">
                                        <span class="point-bullet">•</span>
                                        <span>Athlete has exhausted internal remedies</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Respondent Arguments -->
                <div>
                    <!-- Sporting Succession Rebuttal -->
                    <div class="argument-card">
                        <div class="argument-header" onclick="toggleArgument('respondent-1')">
                            <div class="argument-title">
                                <svg class="chevron" id="chevron-respondent-1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <span style="color: #e63946; font-weight: 500;">1. Sporting Succession Rebuttal</span>
                            </div>
                            <span class="subarg-badge respondent-badge">2 subarguments</span>
                        </div>
                        <div id="content-respondent-1" class="argument-content">
                            <!-- Key Points -->
                            <div>
                                <h3 class="points-title">Key Points</h3>
                                <ul class="points-list">
                                    <li class="point-item">
                                        <span class="point-bullet resp-point-bullet">•</span>
                                        <span>Challenge to claimed continuity of operations <span class="resp-para-ref">¶200-202</span></span>
                                    </li>
                                    <li class="point-item">
                                        <span class="point-bullet resp-point-bullet">•</span>
                                        <span>Analysis of discontinuities in club operations</span>
                                    </li>
                                    <li class="point-item">
                                        <span class="point-bullet resp-point-bullet">•</span>
                                        <span>Dispute over public recognition factors</span>
                                    </li>
                                </ul>
                            </div>
                            
                            <!-- Legal Points -->
                            <div>
                                <h3 class="points-title">Legal Points</h3>
                                <div>
                                    <span class="legal-tag">Legal</span>
                                    <div class="legal-content">
                                        <p>CAS jurisprudence requires operational continuity not merely identification</p>
                                        <div style="display: flex; justify-content: space-between; margin-top: 8px;">
                                            <span>CAS 2017/A/5465</span>
                                            <span class="resp-para-ref">¶203-205</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Factual Points -->
                            <div>
                                <h3 class="points-title">Factual Points</h3>
                                <div>
                                    <div style="display: flex; align-items: center;">
                                        <span class="factual-tag">Factual</span>
                                        <span class="date-tag">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;">
                                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                                <line x1="3" y1="10" x2="21" y2="10"></line>
                                            </svg>
                                            1975-1976
                                        </span>
                                        <span class="disputed-tag">Disputed by Claimant</span>
                                    </div>
                                    <div class="factual-content">
                                        <p>Operations ceased between 1975-1976</p>
                                        <div style="display: flex; justify-content: space-between; margin-top: 8px;">
                                            <span class="resp-para-ref">¶206-207</span>
                                            <span class="evidence-id respondent-badge">R-1</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Evidence -->
                            <div>
                                <h3 class="points-title">Evidence</h3>
                                <div class="evidence-item">
                                    <div>
                                        <div style="display: flex; align-items: center;">
                                            <span class="evidence-id respondent-badge">R-1</span>
                                            <strong>Federation Records</strong>
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="copy-icon" style="margin-left: 8px;">
                                                <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                                <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                                            </svg>
                                        </div>
                                        <p style="margin-top: 4px; color: #6b7280; font-size: 14px;">Records showing non-participation in 1975-1976 season.</p>
                                        <div style="margin-top: 4px; font-size: 12px; color: #6b7280;">
                                            <span>Cited in:</span>
                                            <span style="margin-left: 4px; background-color: #f3f4f6; padding: 2px 6px; border-radius: 4px;">¶208</span>
                                            <span style="margin-left: 4px; background-color: #f3f4f6; padding: 2px 6px; border-radius: 4px;">¶209</span>
                                            <span style="margin-left: 4px; background-color: #f3f4f6; padding: 2px 6px; border-radius: 4px;">¶210</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Jurisdiction Challenge -->
                    <div class="argument-card">
                        <div class="argument-header" onclick="toggleArgument('respondent-2')">
                            <div class="argument-title">
                                <svg class="chevron" id="chevron-respondent-2" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <span style="color: #e63946; font-weight: 500;">2. Jurisdiction Challenge</span>
                            </div>
                        </div>
                        <div id="content-respondent-2" class="argument-content">
                            <!-- Key Points -->
                            <div>
                                <h3 class="points-title">Key Points</h3>
                                <ul class="points-list">
                                    <li class="point-item">
                                        <span class="point-bullet resp-point-bullet">•</span>
                                        <span>CAS cannot hear this case yet <span class="resp-para-ref">¶250-252</span></span>
                                    </li>
                                    <li class="point-item">
                                        <span class="point-bullet resp-point-bullet">•</span>
                                        <span>Athlete skipped required steps in federation's appeal process</span>
                                    </li>
                                    <li class="point-item">
                                        <span class="point-bullet resp-point-bullet">•</span>
                                        <span>Procedural requirements must be followed</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Timeline Tab -->
        <div id="timeline" class="tab-content">
            <table class="data-table">
                <thead>
                    <tr>
                        <th>DATE</th>
                        <th>APPELLANT'S VERSION</th>
                        <th>RESPONDENT'S VERSION</th>
                        <th>STATUS</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1950-01-12</td>
                        <td>Original club registration</td>
                        <td>Original club registration</td>
                        <td class="undisputed">Undisputed</td>
                    </tr>
                    <tr>
                        <td>1975-04-30</td>
                        <td>Administrative restructuring</td>
                        <td>Club dissolution</td>
                        <td class="disputed">Disputed</td>
                    </tr>
                    <tr>
                        <td>1976-09-15</td>
                        <td>Routine registration renewal</td>
                        <td>New club formation</td>
                        <td class="disputed">Disputed</td>
                    </tr>
                    <tr>
                        <td>1982-05-20</td>
                        <td>Color variation introduced temporarily</td>
                        <td>New color scheme implemented</td>
                        <td class="disputed">Disputed</td>
                    </tr>
                    <tr>
                        <td>2022-12-10</td>
                        <td>Appeal filed with CAS</td>
                        <td>Premature CAS application</td>
                        <td class="disputed">Disputed</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <!-- Exhibits Tab -->
        <div id="exhibits" class="tab-content">
            <table class="data-table">
                <thead>
                    <tr>
                        <th>EXHIBIT ID</th>
                        <th>PARTY</th>
                        <th>TITLE</th>
                        <th>TYPE</th>
                        <th>SUMMARY</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><span class="evidence-id claimant-badge">C-1</span></td>
                        <td>Claimant</td>
                        <td>Historical Registration Documents</td>
                        <td>official records</td>
                        <td>Official records showing continuous name usage from 1950 to present day</td>
                    </tr>
                    <tr>
                        <td><span class="evidence-id claimant-badge">C-2</span></td>
                        <td>Claimant</td>
                        <td>Federation Recognition Letters</td>
                        <td>correspondence</td>
                        <td>Official correspondence from the Federation acknowledging club identity</td>
                    </tr>
                    <tr>
                        <td><span class="evidence-id claimant-badge">C-3</span></td>
                        <td>Claimant</td>
                        <td>Club Colors Archive</td>
                        <td>photographs</td>
                        <td>Historical photographs showing consistent team colors with minor variations</td>
                    </tr>
                    <tr>
                        <td><span class="evidence-id respondent-badge">R-1</span></td>
                        <td>Respondent</td>
                        <td>Federation Records</td>
                        <td>official records</td>
                        <td>Federation competition records showing absence from competition in 1975-1976</td>
                    </tr>
                    <tr>
                        <td><span class="evidence-id respondent-badge">R-2</span></td>
                        <td>Respondent</td>
                        <td>Termination Certificate</td>
                        <td>official document</td>
                        <td>Official government certificate of termination dated April 30, 1975</td>
                    </tr>
                    <tr>
                        <td><span class="evidence-id respondent-badge">R-3</span></td>
                        <td>Respondent</td>
                        <td>New Entity Registration</td>
                        <td>official document</td>
                        <td>Registration documents for a new legal entity filed on September 15, 1976</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <script>
            // Tab switching
            document.querySelectorAll('.tab').forEach(tab => {
                tab.addEventListener('click', function() {
                    // Update tabs
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Update content
                    const tabId = this.getAttribute('data-tab');
                    document.querySelectorAll('.tab-content').forEach(content => {
                        content.style.display = 'none';
                    });
                    document.getElementById(tabId).style.display = 'block';
                });
            });
            
            // Toggle argument expansion
            function toggleArgument(id) {
                const contentEl = document.getElementById(`content-\${id}`);
                const chevronEl = document.getElementById(`chevron-\${id}`);
                
                if (contentEl.style.display === 'block') {
                    contentEl.style.display = 'none';
                    chevronEl.classList.remove('expanded');
                } else {
                    contentEl.style.display = 'block';
                    chevronEl.classList.add('expanded');
                }
                
                // If this is a claimant/respondent pair, toggle the other side too
                const isClaimant = id.startsWith('claimant');
                const argNum = id.split('-')[1];
                const pairedId = isClaimant ? `respondent-\${argNum}` : `claimant-\${argNum}`;
                
                const pairedContentEl = document.getElementById(`content-\${pairedId}`);
                const pairedChevronEl = document.getElementById(`chevron-\${pairedId}`);
                
                if (pairedContentEl) {
                    pairedContentEl.style.display = contentEl.style.display;
                    
                    if (contentEl.style.display === 'block') {
                        pairedChevronEl.classList.add('expanded');
                    } else {
                        pairedChevronEl.classList.remove('expanded');
                    }
                }
            }
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
