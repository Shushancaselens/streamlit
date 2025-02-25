import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd

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
            "legalPoints": [
                {
                    "point": "CAS jurisprudence establishes criteria for sporting succession",
                    "isDisputed": False,
                    "regulations": ["CAS 2016/A/4576"],
                    "paragraphs": "15-17"
                }
            ],
            "factualPoints": [
                {
                    "point": "Continuous operation under same name since 1950",
                    "date": "1950-present",
                    "isDisputed": False,
                    "paragraphs": "18-19"
                }
            ],
            "evidence": [
                {
                    "id": "C-1",
                    "title": "Historical Registration Documents",
                    "summary": "Official records showing continuous name usage",
                    "citations": ["20", "21", "24"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2016/A/4576",
                    "title": "Criteria for sporting succession",
                    "relevance": "Establishes key factors for succession",
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
                    "legalPoints": [
                        {
                            "point": "Name registration complies with regulations",
                            "isDisputed": False,
                            "regulations": ["Name Registration Act"],
                            "paragraphs": "22-24"
                        },
                        {
                            "point": "Trademark protection since 1960",
                            "isDisputed": False,
                            "regulations": ["Trademark Law"],
                            "paragraphs": "25-27"
                        }
                    ],
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
                                    "paragraphs": "25-26"
                                },
                                {
                                    "point": "Brief administrative gap in 1975-1976",
                                    "date": "1975-1976",
                                    "isDisputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "29-30"
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "C-2",
                                    "title": "Registration Records",
                                    "summary": "Official documentation of registration history",
                                    "citations": ["25", "26", "28"]
                                }
                            ],
                            "children": {}
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
                    "legalPoints": [
                        {
                            "point": "Color trademark registration valid since 1960",
                            "isDisputed": False,
                            "regulations": ["Trademark Act"],
                            "paragraphs": "48-50"
                        }
                    ],
                    "factualPoints": [
                        {
                            "point": "Consistent use of blue and white since founding",
                            "date": "1950-present",
                            "isDisputed": True,
                            "source": "Respondent",
                            "paragraphs": "51-52"
                        }
                    ],
                    "evidence": [
                        {
                            "id": "C-4",
                            "title": "Historical Photographs",
                            "summary": "Visual evidence of consistent color usage",
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
                                    "paragraphs": "56-57"
                                },
                                {
                                    "point": "Temporary third color addition in 1980s",
                                    "date": "1982-1988",
                                    "isDisputed": False,
                                    "paragraphs": "58-59"
                                }
                            ],
                            "children": {}
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
            },
            "legalPoints": [
                {
                    "point": "WADA Code Article 5 establishes procedural requirements",
                    "isDisputed": False,
                    "regulations": ["WADA Code 2021", "International Standard for Testing"],
                    "paragraphs": "73-75"
                }
            ],
            "children": {}
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
            "legalPoints": [
                {
                    "point": "CAS jurisprudence requires operational continuity not merely identification",
                    "isDisputed": False,
                    "regulations": ["CAS 2017/A/5465"],
                    "paragraphs": "203-205"
                }
            ],
            "factualPoints": [
                {
                    "point": "Operations ceased between 1975-1976",
                    "date": "1975-1976",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "206-207"
                }
            ],
            "evidence": [
                {
                    "id": "R-1",
                    "title": "Federation Records",
                    "summary": "Records showing non-participation in 1975-1976 season",
                    "citations": ["208", "209", "210"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2017/A/5465",
                    "title": "Operational continuity requirement",
                    "relevance": "Establishes primacy of operational continuity",
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
                    "legalPoints": [
                        {
                            "point": "Registration lapse voided legal continuity",
                            "isDisputed": True,
                            "regulations": ["Registration Act"],
                            "paragraphs": "223-225"
                        }
                    ],
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
                                    "paragraphs": "226-227"
                                },
                                {
                                    "point": "New entity registered on September 15, 1976",
                                    "date": "September 15, 1976",
                                    "isDisputed": False,
                                    "paragraphs": "228-229"
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "R-2",
                                    "title": "Termination Certificate",
                                    "summary": "Official documentation of registration termination",
                                    "citations": ["226", "227"]
                                }
                            ],
                            "children": {
                                "1.1.1.1": {
                                    "id": "1.1.1.1",
                                    "title": "Legal Entity Discontinuity",
                                    "paragraphs": "231-235",
                                    "legalPoints": [
                                        {
                                            "point": "New registration created distinct legal entity",
                                            "isDisputed": True,
                                            "regulations": ["Company Law §15"],
                                            "paragraphs": "231-232"
                                        }
                                    ],
                                    "factualPoints": [
                                        {
                                            "point": "Different ownership structure post-1976",
                                            "date": "1976",
                                            "isDisputed": False,
                                            "paragraphs": "233-234"
                                        }
                                    ],
                                    "caseLaw": [
                                        {
                                            "caseNumber": "CAS 2018/A/5618",
                                            "title": "Legal entity identity case",
                                            "relevance": "Registration gap creating new legal entity",
                                            "paragraphs": "235",
                                            "citedParagraphs": ["235"]
                                        }
                                    ],
                                    "children": {}
                                }
                            }
                        },
                        "1.1.2": {
                            "id": "1.1.2",
                            "title": "Public Recognition Rebuttal",
                            "paragraphs": "236-240",
                            "legalPoints": [
                                {
                                    "point": "Public perception secondary to operational continuity",
                                    "isDisputed": True,
                                    "regulations": ["CAS 2017/A/5465 ¶45"],
                                    "paragraphs": "236-237"
                                }
                            ],
                            "factualPoints": [
                                {
                                    "point": "Media referred to 'new club' in 1976",
                                    "date": "1976",
                                    "isDisputed": True,
                                    "source": "Claimant",
                                    "paragraphs": "238-239"
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "R-3",
                                    "title": "Newspaper Articles 1976",
                                    "summary": "Media reports referring to new club formation",
                                    "citations": ["238", "239"]
                                }
                            ],
                            "children": {}
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
                    "legalPoints": [
                        {
                            "point": "Color trademark lapsed during 1975-1976",
                            "isDisputed": False,
                            "regulations": ["Trademark Act"],
                            "paragraphs": "243-244"
                        }
                    ],
                    "factualPoints": [
                        {
                            "point": "Significant color scheme change in 1976",
                            "date": "1976",
                            "isDisputed": True,
                            "source": "Claimant",
                            "paragraphs": "245-246"
                        }
                    ],
                    "evidence": [
                        {
                            "id": "R-4",
                            "title": "Historical Photographs Comparison",
                            "summary": "Visual evidence of color scheme changes",
                            "citations": ["245", "246", "247"]
                        }
                    ],
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Symbolism Analysis",
                            "paragraphs": "247-249",
                            "factualPoints": [
                                {
                                    "point": "Pre-1976 colors represented original city district",
                                    "date": "1950-1975",
                                    "isDisputed": False,
                                    "paragraphs": "247"
                                },
                                {
                                    "point": "Post-1976 colors represented new ownership region",
                                    "date": "1976-present",
                                    "isDisputed": True,
                                    "source": "Claimant",
                                    "paragraphs": "248-249"
                                }
                            ],
                            "children": {}
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
            },
            "legalPoints": [
                {
                    "point": "Minor procedural deviations do not invalidate results",
                    "isDisputed": False,
                    "regulations": ["CAS 2019/A/6148"],
                    "paragraphs": "253-255"
                }
            ],
            "children": {}
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
    # Initialize session state
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = 0
    if "view_mode" not in st.session_state:
        st.session_state.view_mode = "default"
        
    # Create tab titles with custom styling
    tab_titles = ["Summary of Arguments", "Timeline", "Exhibits"]
    
    # Add custom CSS for tabs and general styling
    st.markdown("""
    <style>
        /* Override Streamlit container width */
        .reportview-container .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Style for the section headers */
        .tab-header {
            display: flex;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 1rem;
        }
        .tab-item {
            padding: 0.75rem 1.5rem;
            font-weight: 500;
            cursor: pointer;
            color: #718096;
            position: relative;
        }
        .tab-item:hover {
            color: #2d3748;
        }
        .tab-item.active {
            color: #3182ce;
            border-bottom: 2px solid #3182ce;
        }
        
        /* Global card styling */
        .card {
            background-color: white;
            border-radius: 0.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
            margin-bottom: 1.5rem;
            overflow: hidden;
        }
        
        /* Hide Streamlit elements as needed */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding-top: 2rem; padding-bottom: 0;}
        .st-emotion-cache-16txtl3 h1 {margin-top: -4rem;}
    </style>
    """, unsafe_allow_html=True)
    
    # Create tab layout
    st.markdown("""
    <div class="tab-header">
        <div class="tab-item active" id="tab-0" onclick="selectTab(0)">Summary of Arguments</div>
        <div class="tab-item" id="tab-1" onclick="selectTab(1)">Timeline</div>
        <div class="tab-item" id="tab-2" onclick="selectTab(2)">Exhibits</div>
    </div>
    
    <script>
        function selectTab(index) {
            // Update UI
            document.querySelectorAll('.tab-item').forEach(tab => tab.classList.remove('active'));
            document.getElementById(`tab-${index}`).classList.add('active');
            
            // Show/hide content
            document.querySelectorAll('.tab-content').forEach(content => content.style.display = 'none');
            document.getElementById(`content-${index}`).style.display = 'block';
            
            // Update session state via form submission
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '';
            
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'active_tab';
            input.value = index;
            
            form.appendChild(input);
            document.body.appendChild(form);
            form.submit();
        }
        
        // Initialize correct tab
        window.onload = function() {
            selectTab(window.initialTabIndex || 0);
        };
    </script>
    """, unsafe_allow_html=True)
    
    # Get the data
    args_data = get_argument_data()
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    timeline_json = json.dumps(timeline_data)
    exhibits_json = json.dumps(exhibits_data)
    
    # Create the Arguments component
    arguments_component = f"""
    <div id="content-0" class="tab-content" style="display: block;">
        <div class="view-toggle" style="display: flex; justify-content: flex-end; margin-bottom: 1rem;">
            <div style="background-color: #f7fafc; border-radius: 0.375rem; padding: 0.25rem;">
                <button id="default-view" class="view-btn active" style="padding: 0.5rem 1rem; border-radius: 0.375rem; border: none; background: none; font-size: 0.875rem; font-weight: 500; cursor: pointer;">Standard View</button>
                <button id="topic-view" class="view-btn" style="padding: 0.5rem 1rem; border-radius: 0.375rem; border: none; background: none; font-size: 0.875rem; font-weight: 500; cursor: pointer;">Topic View</button>
            </div>
        </div>
        
        <div id="standard-view-content">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1rem;">
                <h3 style="color: #3182ce; font-size: 1.125rem; font-weight: 600;">Claimant's Arguments</h3>
                <h3 style="color: #e53e3e; font-size: 1.125rem; font-weight: 600;">Respondent's Arguments</h3>
            </div>
            <div id="arguments-container"></div>
        </div>
        
        <div id="topic-view-content" style="display: none;">
            <div id="topics-container"></div>
        </div>
    </div>
    
    <script>
    // Initialize data
    const argsData = {args_json};
    const claimantArgs = argsData.claimantArgs;
    const respondentArgs = argsData.respondentArgs;
    const topics = argsData.topics;
    
    // Track expanded state
    const expandedStates = {};
    
    // Toggle view mode
    document.getElementById('default-view').addEventListener('click', () => {
        document.getElementById('default-view').classList.add('active');
        document.getElementById('topic-view').classList.remove('active');
        document.getElementById('standard-view-content').style.display = 'block';
        document.getElementById('topic-view-content').style.display = 'none';
    });
    
    document.getElementById('topic-view').addEventListener('click', () => {
        document.getElementById('topic-view').classList.add('active');
        document.getElementById('default-view').classList.remove('active');
        document.getElementById('standard-view-content').style.display = 'none';
        document.getElementById('topic-view-content').style.display = 'block';
    });
    
    // Function to toggle argument expansion
    function toggleArgument(id) {{
        expandedStates[id] = !expandedStates[id];
        const isExpanded = expandedStates[id] || false;
        
        // Toggle visibility of content
        const content = document.getElementById(`content-${{id}}`);
        if (content) {{
            content.style.display = isExpanded ? 'block' : 'none';
        }}
        
        // Rotate chevron
        const chevron = document.getElementById(`chevron-${{id}}`);
        if (chevron) {{
            chevron.style.transform = isExpanded ? 'rotate(90deg)' : 'rotate(0deg)';
        }}
        
        // Update all matched pairs (e.g., claimant 1 and respondent 1)
        const baseId = id.split('_')[1];
        const pairIds = [`claimant_${{baseId}}`, `respondent_${{baseId}}`];
        
        pairIds.forEach(pairId => {{
            if (pairId !== id) {{
                expandedStates[pairId] = expandedStates[id];
                const pairContent = document.getElementById(`content-${{pairId}}`);
                const pairChevron = document.getElementById(`chevron-${{pairId}}`);
                
                if (pairContent) {{
                    pairContent.style.display = isExpanded ? 'block' : 'none';
                }}
                
                if (pairChevron) {{
                    pairChevron.style.transform = isExpanded ? 'rotate(90deg)' : 'rotate(0deg)';
                }}
            }}
        }});
        
        // Handle children visibility recursively
        const childrenContainer = document.getElementById(`children-${{id}}`);
        if (childrenContainer) {{
            childrenContainer.style.display = isExpanded ? 'block' : 'none';
        }}
    }}
    
    // Function to render overview points
    function renderOverviewPoints(overview) {{
        if (!overview || !overview.points) return '';
        
        const points = overview.points.map(point => 
            `<li class="flex items-center gap-2">
                <div style="width: 6px; height: 6px; border-radius: 50%; background-color: #3182ce;"></div>
                <span style="font-size: 0.875rem; color: #4a5568;">${{point}}</span>
            </li>`
        ).join('');
        
        return `
        <div style="background-color: #f7fafc; border-radius: 0.5rem; padding: 1rem; margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                <h6 style="font-size: 0.875rem; font-weight: 500;">Key Points</h6>
                <span style="font-size: 0.75rem; background-color: #ebf8ff; color: #2b6cb0; padding: 0.25rem 0.5rem; border-radius: 0.25rem;">¶${{overview.paragraphs}}</span>
            </div>
            <ul style="display: flex; flex-direction: column; gap: 0.5rem;">
                ${{points}}
            </ul>
        </div>
        `;
    }}
    
    // Function to render legal points
    function renderLegalPoints(points) {{
        if (!points || points.length === 0) return '';
        
        const pointsHtml = points.map(point => {{
            const disputed = point.isDisputed 
                ? `<span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; background-color: #fed7d7; color: #c53030; border-radius: 0.25rem;">Disputed</span>` 
                : '';
            
            const regulations = point.regulations?.map(reg => 
                `<span style="font-size: 0.75rem; background-color: #ebf8ff; color: #2b6cb0; padding: 0.25rem 0.5rem; border-radius: 0.25rem; margin-right: 0.5rem;">${{reg}}</span>`
            ).join('') || '';
            
            return `
            <div style="background-color: #ebf8ff; border-radius: 0.5rem; padding: 0.75rem; margin-bottom: 0.5rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;">
                    <span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; background-color: #bee3f8; color: #2c5282; border-radius: 0.25rem;">Legal</span>
                    ${{disputed}}
                </div>
                <p style="font-size: 0.875rem; color: #4a5568;">${{point.point}}</p>
                <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem;">
                    ${{regulations}}
                    <span style="font-size: 0.75rem; color: #718096;">¶${{point.paragraphs}}</span>
                </div>
            </div>
            `;
        }}).join('');
        
        return `
        <div style="margin-bottom: 1.5rem;">
            <h6 style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Legal Points</h6>
            ${{pointsHtml}}
        </div>
        `;
    }}
    
    // Function to render factual points
    function renderFactualPoints(points) {{
        if (!points || points.length === 0) return '';
        
        const pointsHtml = points.map(point => {{
            const disputed = point.isDisputed 
                ? `<span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; background-color: #fed7d7; color: #c53030; border-radius: 0.25rem;">Disputed by ${{point.source || ''}}</span>` 
                : '';
            
            return `
            <div style="background-color: #f0fff4; border-radius: 0.5rem; padding: 0.75rem; margin-bottom: 0.5rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;">
                    <span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; background-color: #c6f6d5; color: #276749; border-radius: 0.25rem;">Factual</span>
                    ${{disputed}}
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                    <span style="font-size: 0.75rem; color: #718096;">${{point.date}}</span>
                </div>
                <p style="font-size: 0.875rem; color: #4a5568;">${{point.point}}</p>
                <span style="font-size: 0.75rem; color: #718096; display: inline-block; margin-top: 0.5rem;">¶${{point.paragraphs}}</span>
            </div>
            `;
        }}).join('');
        
        return `
        <div style="margin-bottom: 1.5rem;">
            <h6 style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Factual Points</h6>
            ${{pointsHtml}}
        </div>
        `;
    }}
    
    // Function to render evidence
    function renderEvidence(items) {{
        if (!items || items.length === 0) return '';
        
        const itemsHtml = items.map(item => {{
            const citations = item.citations?.map(cite => 
                `<span style="font-size: 0.75rem; background-color: #edf2f7; color: #4a5568; padding: 0.25rem 0.5rem; border-radius: 0.25rem; margin-left: 0.25rem;">¶${{cite}}</span>`
            ).join('') || '';
            
            return `
            <div style="background-color: #f7fafc; border-radius: 0.5rem; padding: 0.75rem; margin-bottom: 0.5rem;">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <p style="font-size: 0.875rem; font-weight: 500;">${{item.id}}: ${{item.title}}</p>
                        <p style="font-size: 0.75rem; color: #718096; margin-top: 0.25rem;">${{item.summary}}</p>
                        <div style="margin-top: 0.5rem;">
                            <span style="font-size: 0.75rem; color: #718096;">Cited in: </span>
                            ${{citations}}
                        </div>
                    </div>
                    <button style="background: none; border: none; color: #3182ce; cursor: pointer; height: 24px;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                            <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                        </svg>
                    </button>
                </div>
            </div>
            `;
        }}).join('');
        
        return `
        <div style="margin-bottom: 1.5rem;">
            <h6 style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Evidence</h6>
            ${{itemsHtml}}
        </div>
        `;
    }}
    
    // Function to render case law
    function renderCaseLaw(items) {{
        if (!items || items.length === 0) return '';
        
        const itemsHtml = items.map(item => {{
            const citedParagraphs = item.citedParagraphs?.map(para => 
                `<span style="font-size: 0.75rem; background-color: #edf2f7; color: #4a5568; padding: 0.25rem 0.5rem; border-radius: 0.25rem; margin-left: 0.25rem;">¶${{para}}</span>`
            ).join('') || '';
            
            return `
            <div style="background-color: #f7fafc; border-radius: 0.5rem; padding: 0.75rem; margin-bottom: 0.5rem;">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <p style="font-size: 0.875rem; font-weight: 500;">${{item.caseNumber}}</p>
                            <span style="font-size: 0.75rem; color: #718096;">¶${{item.paragraphs}}</span>
                        </div>
                        <p style="font-size: 0.75rem; color: #718096; margin-top: 0.25rem;">${{item.title}}</p>
                        <p style="font-size: 0.875rem; color: #4a5568; margin-top: 0.5rem;">${{item.relevance}}</p>
                        <div style="margin-top: 0.5rem;">
                            <span style="font-size: 0.75rem; color: #718096;">Key Paragraphs: </span>
                            ${{citedParagraphs}}
                        </div>
                    </div>
                    <button style="background: none; border: none; color: #3182ce; cursor: pointer; height: 24px;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                            <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                        </svg>
                    </button>
                </div>
            </div>
            `;
        }}).join('');
        
        return `
        <div style="margin-bottom: 1.5rem;">
            <h6 style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Case Law</h6>
            ${{itemsHtml}}
        </div>
        `;
    }}
    
    // Function to render a single argument section
    function renderArgument(arg, side, level = 0) {{
        if (!arg) return '';
        
        const id = `${{side}}_${{arg.id}}`;
        const hasChildren = arg.children && Object.keys(arg.children).length > 0;
        const childCount = hasChildren ? Object.keys(arg.children).length : 0;
        
        // Style based on side
        const baseColor = side === 'claimant' ? '#3182ce' : '#e53e3e';
        const bgColor = side === 'claimant' ? '#ebf8ff' : '#fff5f5';
        const borderColor = side === 'claimant' ? '#bee3f8' : '#fed7d7';
        
        // Content rendered only when expanded
        const content = `
        <div id="content-${{id}}" style="display: none; padding: 0.5rem 1rem; background-color: white; border-radius: 0 0 0.5rem 0.5rem;">
            ${{renderOverviewPoints(arg.overview)}}
            ${{renderLegalPoints(arg.legalPoints)}}
            ${{renderFactualPoints(arg.factualPoints)}}
            ${{renderEvidence(arg.evidence)}}
            ${{renderCaseLaw(arg.caseLaw)}}
        </div>
        `;
        
        // Children container for nested arguments
        let childrenHtml = '';
        if (hasChildren) {{
            const childrenArgs = Object.values(arg.children).map(child => 
                renderArgument(child, side, level + 1)
            ).join('');
            
            childrenHtml = `
            <div id="children-${{id}}" style="display: none; margin-left: ${{level > 0 ? '1.5rem' : '0'}};">
                ${{childrenArgs}}
            </div>
            `;
        }}
        
        // Header with toggle
        const header = `
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.75rem 1rem; cursor: pointer; background-color: ${{bgColor}}; border: 1px solid ${{borderColor}}; border-radius: ${{level === 0 ? '0.5rem' : '0.5rem 0.5rem 0 0'}};" 
             onclick="toggleArgument('${{id}}')">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <svg id="chevron-${{id}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s ease-in-out;">
                    <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
                <h5 style="font-size: 0.875rem; font-weight: 500; color: ${{baseColor}};">
                    ${{arg.id}}. ${{arg.title}}
                </h5>
                ${{hasChildren 
                    ? `<span style="font-size: 0.75rem; background-color: ${{bgColor}}; color: ${{baseColor}}; padding: 0.25rem 0.5rem; border-radius: 9999px;">${{childCount}} subarguments</span>` 
                    : `<span style="font-size: 0.75rem; color: ${{baseColor}}; padding: 0.25rem 0.5rem; background-color: ${{bgColor}}; border-radius: 0.25rem;">¶${{arg.paragraphs}}</span>`
                }}
            </div>
        </div>
        `;
        
        return `
        <div style="margin-bottom: 1rem; ${{level > 0 ? `margin-left: ${{level * 0.5}}rem;` : ''}}">
            ${{header}}
            ${{content}}
            ${{childrenHtml}}
        </div>
        `;
    }}
    
    // Function to render argument pairs side by side
    function renderArgumentPair(claimantArg, respondentArg, level = 0, isRoot = false) {{
        if (!claimantArg || !respondentArg) return '';
        
        const claimantHtml = renderArgument(claimantArg, 'claimant', level);
        const respondentHtml = renderArgument(respondentArg, 'respondent', level);
        
        // Connector styles for the tree structure (only for nested levels)
        let connectorStyles = '';
        if (level > 0 && !isRoot) {{
            connectorStyles = `
            <style>
                .connector-claimant-${{claimantArg.id}} {{
                    position: absolute;
                    left: 10px;
                    top: 24px;
                    width: 12px;
                    height: 1px;
                    background-color: rgba(59, 130, 246, 0.6);
                    z-index: 1;
                }}
                .connector-vertical-claimant-${{claimantArg.id}} {{
                    position: absolute;
                    left: 10px;
                    top: -12px;
                    width: 1px;
                    height: 36px;
                    background-color: rgba(59, 130, 246, 0.6);
                }}
                .connector-respondent-${{respondentArg.id}} {{
                    position: absolute;
                    left: 10px;
                    top: 24px;
                    width: 12px;
                    height: 1px;
                    background-color: rgba(239, 68, 68, 0.6);
                    z-index: 1;
                }}
                .connector-vertical-respondent-${{respondentArg.id}} {{
                    position: absolute;
                    left: 10px;
                    top: -12px;
                    width: 1px;
                    height: 36px;
                    background-color: rgba(239, 68, 68, 0.6);
                }}
            </style>
            `;
        }}
        
        return `
        <div style="margin-bottom: 1rem;">
            ${{connectorStyles}}
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                <div style="${{level > 0 ? 'padding-left: 2rem; position: relative;' : ''}}">
                    ${{level > 0 && !isRoot ? `<div class="connector-claimant-${{claimantArg.id}}"></div>` : ''}}
                    ${{level > 0 ? `<div class="connector-vertical-claimant-${{claimantArg.id}}"></div>` : ''}}
                    <div style="position: relative;">
                        ${{claimantHtml}}
                    </div>
                </div>
                <div style="${{level > 0 ? 'padding-left: 2rem; position: relative;' : ''}}">
                    ${{level > 0 && !isRoot ? `<div class="connector-respondent-${{respondentArg.id}}"></div>` : ''}}
                    ${{level > 0 ? `<div class="connector-vertical-respondent-${{respondentArg.id}}"></div>` : ''}}
                    <div style="position: relative;">
                        ${{respondentHtml}}
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 0.5rem; position: relative;">
                ${{level === 0 && Object.keys(claimantArg.children || {}).length > 0 ? `
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; position: relative;">
                    <div style="position: relative;">
                        <div style="position: absolute; left: 10px; top: 0; width: 1px; height: 100%; background-color: rgba(59, 130, 246, 0.4);"></div>
                    </div>
                    <div style="position: relative;">
                        <div style="position: absolute; left: 10px; top: 0; width: 1px; height: 100%; background-color: rgba(239, 68, 68, 0.4);"></div>
                    </div>
                </div>
                ` : ''}}
                
                ${{Object.keys(claimantArg.children || {}).map((childId, index) => {{
                    const claimantChild = claimantArg.children[childId];
                    const respondentChild = respondentArg.children[childId];
                    
                    if (claimantChild && respondentChild) {{
                        return renderArgumentPair(claimantChild, respondentChild, level + 1);
                    }}
                    return '';
                }}).join('')}}
            </div>
        </div>
        `;
    }}
    
    // Function to render topic view
    function renderTopicView() {{
        return topics.map(topic => {{
            let topicPairs = '';
            
            topic.argumentIds.forEach(argId => {{
                const claimantArg = claimantArgs[argId];
                const respondentArg = respondentArgs[argId];
                
                if (claimantArg && respondentArg) {{
                    topicPairs += renderArgumentPair(claimantArg, respondentArg, 0, true);
                }}
            }});
            
            return `
            <div style="margin-bottom: 2rem;">
                <div style="margin-bottom: 1rem;">
                    <h2 style="font-size: 1.25rem; font-weight: 600; color: #2d3748; margin-bottom: 0.25rem;">${{topic.title}}</h2>
                    <p style="font-size: 0.875rem; color: #718096;">${{topic.description}}</p>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1rem; padding: 0 1rem;">
                    <div>
                        <h3 style="font-size: 1rem; font-weight: 500; color: #3182ce;">Claimant's Arguments</h3>
                    </div>
                    <div>
                        <h3 style="font-size: 1rem; font-weight: 500; color: #e53e3e;">Respondent's Arguments</h3>
                    </div>
                </div>
                
                ${{topicPairs}}
            </div>
            `;
        }}).join('');
    }}
    
    // Render standard view
    function renderStandardView() {{
        let pairs = '';
        
        // For each argument ID that exists in both claimant and respondent
        Object.keys(claimantArgs).forEach(argId => {{
            if (respondentArgs[argId]) {{
                pairs += renderArgumentPair(claimantArgs[argId], respondentArgs[argId], 0, true);
            }}
        }});
        
        return pairs;
    }}
    
    // Initialize views
    document.getElementById('arguments-container').innerHTML = renderStandardView();
    document.getElementById('topics-container').innerHTML = renderTopicView();
    
    // Style active buttons
    document.querySelectorAll('.view-btn').forEach(btn => {{
        btn.addEventListener('click', function() {{
            document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        }});
    }});
    
    document.querySelector('.view-btn.active').style.backgroundColor = 'white';
    document.querySelector('.view-btn.active').style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';
    
    document.querySelectorAll('.view-btn').forEach(btn => {{
        btn.addEventListener('click', function() {{
            document.querySelectorAll('.view-btn').forEach(b => {{
                b.style.backgroundColor = '';
                b.style.boxShadow = '';
            }});
            this.style.backgroundColor = 'white';
            this.style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';
        }});
    }});
    </script>
    """
    
    # Create the Timeline component
    timeline_component = f"""
    <div id="content-1" class="tab-content" style="display: none;">
        <div style="display: flex; justify-content: flex-end; margin-bottom: 1rem;">
            <button class="copy-btn" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background-color: white; border: 1px solid #e2e8f0; border-radius: 0.375rem; font-size: 0.875rem; margin-left: 0.5rem;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                Copy
            </button>
            <button class="export-btn" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background-color: white; border: 1px solid #e2e8f0; border-radius: 0.375rem; font-size: 0.875rem; margin-left: 0.5rem;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                    <polyline points="7 10 12 15 17 10"></polyline>
                    <line x1="12" y1="15" x2="12" y2="3"></line>
                </svg>
                Export Data
            </button>
        </div>
        
        <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
            <div style="display: flex; gap: 0.5rem;">
                <div style="position: relative;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="position: absolute; left: 12px; top: 11px;">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    <input type="text" id="timeline-search" placeholder="Search events..." style="padding: 0.625rem 1rem 0.625rem 2.5rem; border: 1px solid #e2e8f0; border-radius: 0.375rem; width: 16rem;">
                </div>
                <button id="timeline-filter-btn" style="display: inline-flex; align-items: center; gap: 0.25rem; padding: 0.625rem 1rem; background-color: white; border: 1px solid #e2e8f0; border-radius: 0.375rem;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>
                    </svg>
                    Filter
                </button>
            </div>
            <div style="display: flex; align-items: center;">
                <label style="display: flex; align-items: center; gap: 0.5rem;">
                    <input type="checkbox" id="disputed-only" style="width: 1rem; height: 1rem;">
                    <span style="font-size: 0.875rem; color: #4a5568;">Disputed events only</span>
                </label>
            </div>
        </div>
        
        <div style="background-color: white; border-radius: 0.375rem; border: 1px solid #e2e8f0; overflow: hidden;">
            <table id="timeline-table" style="width: 100%; border-collapse: collapse;">
                <thead>
                    <tr style="background-color: #f7fafc; border-bottom: 1px solid #e2e8f0;">
                        <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #4a5568;">DATE</th>
                        <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #4a5568;">APPELLANT'S VERSION</th>
                        <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #4a5568;">RESPONDENT'S VERSION</th>
                        <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #4a5568;">STATUS</th>
                    </tr>
                </thead>
                <tbody id="timeline-body"></tbody>
            </table>
        </div>
    </div>
    
    <script>
    // Initialize timeline data
    const timelineData = {timeline_json};
    
    // Render timeline
    function renderTimeline(data) {{
        const tbody = document.getElementById('timeline-body');
        tbody.innerHTML = '';
        
        data.forEach(item => {{
            const row = document.createElement('tr');
            if (item.status === 'Disputed') {{
                row.style.backgroundColor = '#fff5f5';
            }}
            
            row.innerHTML = `
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem; border-bottom: 1px solid #e2e8f0;">${{item.date}}</td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem; border-bottom: 1px solid #e2e8f0;">${{item.appellantVersion}}</td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem; border-bottom: 1px solid #e2e8f0;">${{item.respondentVersion}}</td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem; border-bottom: 1px solid #e2e8f0; ${{item.status === 'Disputed' ? 'color: #c53030;' : 'color: #2f855a;'}}">${{item.status}}</td>
            `;
            
            tbody.appendChild(row);
        }});
    }}
    
    // Filter timeline data
    function filterTimelineData() {{
        const searchTerm = document.getElementById('timeline-search').value.toLowerCase();
        const disputedOnly = document.getElementById('disputed-only').checked;
        
        const filteredData = timelineData.filter(item => {{
            const matchesSearch = searchTerm === '' || 
                item.appellantVersion.toLowerCase().includes(searchTerm) || 
                item.respondentVersion.toLowerCase().includes(searchTerm);
            
            const matchesDisputed = !disputedOnly || item.status === 'Disputed';
            
            return matchesSearch && matchesDisputed;
        }});
        
        renderTimeline(filteredData);
    }}
    
    // Initialize timeline
    document.getElementById('timeline-search').addEventListener('input', filterTimelineData);
    document.getElementById('disputed-only').addEventListener('change', filterTimelineData);
    
    // Initialize timeline when tab is shown
    document.getElementById('tab-1').addEventListener('click', function() {{
        setTimeout(() => {{
            renderTimeline(timelineData);
        }}, 100);
    }});
    </script>
    """
    
    # Create the Exhibits component
    exhibits_component = f"""
    <div id="content-2" class="tab-content" style="display: none;">
        <div style="display: flex; justify-content: flex-end; margin-bottom: 1rem;">
            <button class="copy-btn" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background-color: white; border: 1px solid #e2e8f0; border-radius: 0.375rem; font-size: 0.875rem; margin-left: 0.5rem;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                Copy
            </button>
            <button class="export-btn" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background-color: white; border: 1px solid #e2e8f0; border-radius: 0.375rem; font-size: 0.875rem; margin-left: 0.5rem;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                    <polyline points="7 10 12 15 17 10"></polyline>
                    <line x1="12" y1="15" x2="12" y2="3"></line>
                </svg>
                Export Data
            </button>
        </div>
        
        <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
            <div style="position: relative;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="position: absolute; left: 12px; top: 11px;">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <input type="text" id="exhibits-search" placeholder="Search exhibits..." style="padding: 0.625rem 1rem 0.625rem 2.5rem; border: 1px solid #e2e8f0; border-radius: 0.375rem; width: 16rem;">
            </div>
            
            <select id="party-filter" style="padding: 0.625rem 1rem; border: 1px solid #e2e8f0; border-radius: 0.375rem; background-color: white;">
                <option value="All Parties">All Parties</option>
                <option value="Appellant">Appellant</option>
                <option value="Respondent">Respondent</option>
            </select>
            
            <select id="type-filter" style="padding: 0.625rem 1rem; border: 1px solid #e2e8f0; border-radius: 0.375rem; background-color: white;">
                <option value="All Types">All Types</option>
            </select>
        </div>
        
        <div style="background-color: white; border-radius: 0.375rem; border: 1px solid #e2e8f0; overflow: hidden;">
            <table id="exhibits-table" style="width: 100%; border-collapse: collapse;">
                <thead>
                    <tr style="background-color: #f7fafc; border-bottom: 1px solid #e2e8f0;">
                        <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #4a5568;">EXHIBIT ID</th>
                        <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #4a5568;">PARTY</th>
                        <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #4a5568;">TITLE</th>
                        <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #4a5568;">TYPE</th>
                        <th style="padding: 0.75rem 1rem; text-align: left; font-size: 0.875rem; font-weight: 500; color: #4a5568;">SUMMARY</th>
                        <th style="padding: 0.75rem 1rem; text-align: right; font-size: 0.875rem; font-weight: 500; color: #4a5568;">ACTIONS</th>
                    </tr>
                </thead>
                <tbody id="exhibits-body"></tbody>
            </table>
        </div>
    </div>
    
    <script>
    // Initialize exhibits data
    const exhibitsData = {exhibits_json};
    
    // Populate type filter dropdown
    const typeFilter = document.getElementById('type-filter');
    const uniqueTypes = [...new Set(exhibitsData.map(item => item.type))];
    uniqueTypes.forEach(type => {{
        const option = document.createElement('option');
        option.value = type;
        option.textContent = type;
        typeFilter.appendChild(option);
    }});
    
    // Render exhibits
    function renderExhibits(data) {{
        const tbody = document.getElementById('exhibits-body');
        tbody.innerHTML = '';
        
        data.forEach(item => {{
            const row = document.createElement('tr');
            row.style.borderBottom = '1px solid #e2e8f0';
            
            const partyClass = item.party === 'Appellant' 
                ? 'background-color: #ebf8ff; color: #2b6cb0;' 
                : 'background-color: #fff5f5; color: #c53030;';
            
            row.innerHTML = `
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">${{item.id}}</td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">
                    <span style="${{partyClass}} padding: 0.25rem 0.5rem; border-radius: 0.25rem; font-size: 0.75rem;">${{item.party}}</span>
                </td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">${{item.title}}</td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">
                    <span style="background-color: #edf2f7; color: #4a5568; padding: 0.25rem 0.5rem; border-radius: 0.25rem; font-size: 0.75rem;">${{item.type}}</span>
                </td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem;">${{item.summary}}</td>
                <td style="padding: 0.75rem 1rem; font-size: 0.875rem; text-align: right;">
                    <a href="#" style="color: #3182ce; text-decoration: none;">View</a>
                </td>
            `;
            
            tbody.appendChild(row);
        }});
    }}
    
    // Filter exhibits data
    function filterExhibitsData() {{
        const searchTerm = document.getElementById('exhibits-search').value.toLowerCase();
        const partyFilter = document.getElementById('party-filter').value;
        const typeFilter = document.getElementById('type-filter').value;
        
        const filteredData = exhibitsData.filter(item => {{
            const matchesSearch = searchTerm === '' || 
                item.id.toLowerCase().includes(searchTerm) || 
                item.title.toLowerCase().includes(searchTerm) ||
                item.summary.toLowerCase().includes(searchTerm);
            
            const matchesParty = partyFilter === 'All Parties' || item.party === partyFilter;
            const matchesType = typeFilter === 'All Types' || item.type === typeFilter;
            
            return matchesSearch && matchesParty && matchesType;
        }});
        
        renderExhibits(filteredData);
    }}
    
    // Initialize exhibits
    document.getElementById('exhibits-search').addEventListener('input', filterExhibitsData);
    document.getElementById('party-filter').addEventListener('change', filterExhibitsData);
    document.getElementById('type-filter').addEventListener('change', filterExhibitsData);
    
    // Initialize exhibits when tab is shown
    document.getElementById('tab-2').addEventListener('click', function() {{
        setTimeout(() => {{
            renderExhibits(exhibitsData);
        }}, 100);
    }});
    </script>
    """
    
    # Combine all components
    full_html = f"""
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;">
        {arguments_component}
        {timeline_component}
        {exhibits_component}
        
        <script>
        // Set initial tab index from Streamlit session state
        window.initialTabIndex = {st.session_state.active_tab};
        
        // Update Streamlit session state when tab changes
        function updateStreamlitState(index) {{
            const data = {{
                active_tab: index
            }};
            
            // Send message to Streamlit
            window.parent.postMessage({{
                type: "streamlit:setComponentValue",
                value: data
            }}, "*");
        }}
        
        // Listen for messages from parent
        window.addEventListener("message", (event) => {{
            if (event.data.type === "streamlit:render") {{
                // Initialize with correct tab
                selectTab(window.initialTabIndex);
            }}
        }});
        </script>
    </div>
    """
    
    # Render the complete interface as a custom HTML component
    components.html(full_html, height=800, scrolling=True)
    
    # Update session state based on user interaction
    if st.button("Update Session State", key="update_state", style="display: none;"):
        pass

if __name__ == "__main__":
    main()
