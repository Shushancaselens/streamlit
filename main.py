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
                            "children": {
                                "1.1.1.1": {
                                    "id": "1.1.1.1",
                                    "title": "Administrative Records Verification",
                                    "paragraphs": "31-35",
                                    "factualPoints": [
                                        {
                                            "point": "Independent verification of registration documents",
                                            "date": "2022",
                                            "isDisputed": False,
                                            "paragraphs": "31-32"
                                        }
                                    ]
                                }
                            }
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
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Color Identity Preservation",
                                    "paragraphs": "61-65",
                                    "factualPoints": [
                                        {
                                            "point": "Core identity maintained despite minor variations",
                                            "date": "1950-2022",
                                            "isDisputed": False,
                                            "paragraphs": "61-62"
                                        }
                                    ]
                                }
                            }
                        },
                        "1.2.2": {
                            "id": "1.2.2",
                            "title": "Fan Recognition Analysis",
                            "paragraphs": "66-69",
                            "factualPoints": [
                                {
                                    "point": "Survey showing 95% fan recognition of club colors",
                                    "date": "2021",
                                    "isDisputed": False,
                                    "paragraphs": "66-67"
                                }
                            ]
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
            "children": {
                "2.1": {
                    "id": "2.1",
                    "title": "Sample Collection Procedures",
                    "paragraphs": "76-85",
                    "factualPoints": [
                        {
                            "point": "Collection protocol followed WADA guidelines",
                            "date": "2022-11-15",
                            "isDisputed": False,
                            "paragraphs": "76-78"
                        }
                    ]
                },
                "2.2": {
                    "id": "2.2",
                    "title": "Laboratory Analysis Process",
                    "paragraphs": "86-95",
                    "factualPoints": [
                        {
                            "point": "WADA accredited laboratory performed testing",
                            "date": "2022-11-20",
                            "isDisputed": False,
                            "paragraphs": "86-88"
                        }
                    ]
                }
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
                                    "title": "Registration Document Verification",
                                    "paragraphs": "231-235",
                                    "factualPoints": [
                                        {
                                            "point": "Independent verification of termination certificate",
                                            "date": "2022",
                                            "isDisputed": False,
                                            "paragraphs": "231-232"
                                        }
                                    ]
                                }
                            }
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
                            "title": "Color Changes Analysis",
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
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Brand Identity Disruption",
                                    "paragraphs": "250-255",
                                    "factualPoints": [
                                        {
                                            "point": "Significant changes in visual identity post-1976",
                                            "date": "1976-1980",
                                            "isDisputed": False,
                                            "paragraphs": "250-251"
                                        }
                                    ]
                                }
                            }
                        },
                        "1.2.2": {
                            "id": "1.2.2",
                            "title": "Fan Perception Analysis",
                            "paragraphs": "256-260",
                            "factualPoints": [
                                {
                                    "point": "Survey showing 45% of fans perceive post-1976 club as different entity",
                                    "date": "2021",
                                    "isDisputed": False,
                                    "paragraphs": "256-257"
                                }
                            ]
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
            "children": {
                "2.1": {
                    "id": "2.1",
                    "title": "Sample Collection Defense",
                    "paragraphs": "256-265",
                    "factualPoints": [
                        {
                            "point": "Minor deviations did not compromise sample integrity",
                            "date": "2022-11-15",
                            "isDisputed": False,
                            "paragraphs": "256-258"
                        }
                    ]
                },
                "2.2": {
                    "id": "2.2",
                    "title": "Laboratory Analysis Validation",
                    "paragraphs": "266-275",
                    "factualPoints": [
                        {
                            "point": "Testing methods were scientifically validated and reliable",
                            "date": "2022-11-20",
                            "isDisputed": False,
                            "paragraphs": "266-268"
                        }
                    ]
                }
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
    
    # Title
    st.title("Legal Arguments Analysis")
    
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
                padding: 0;
            }}
            
            /* Tab navigation */
            .tabs {{
                display: flex;
                border-bottom: 1px solid #e2e8f0;
                margin-bottom: 1.5rem;
            }}
            .tab {{
                padding: 1rem 1.5rem;
                font-weight: 500;
                color: #718096;
                cursor: pointer;
                position: relative;
            }}
            .tab:hover {{
                color: #4a5568;
            }}
            .tab.active {{
                color: #3182ce;
                border-bottom: 2px solid #3182ce;
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
                color: #3182ce;
            }}
            .respondent-color {{
                color: #e53e3e;
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
            
            /* Argument card and details - Updated styling to match screenshot */
            .argument {{
                border-radius: 0.375rem;
                overflow: hidden;
                margin-bottom: 0.5rem;
                background-color: #f8fafc; /* Lighter background */
            }}
            .argument-header {{
                padding: 0.75rem 1rem;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #e2e8f0;
                background-color: #f8fafc; /* Lighter background */
                transition: background-color 0.2s;
            }}
            .argument-header:hover {{
                background-color: #f1f5f9; /* Subtle hover effect */
            }}
            .argument-header-left {{
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            .argument-content {{
                padding: 1rem;
                display: none;
                background-color: white;
            }}
            
            /* Styling for sub-arguments */
            .sub-argument {{
                margin-left: 1.5rem;
                position: relative;
                border-left: 1px solid #e2e8f0;
                padding-left: 1rem;
                margin-top: 0.5rem;
            }}
            .sub-argument .argument-header {{
                background-color: white;
                border: none;
                border-bottom: 1px solid #e2e8f0;
                padding: 0.5rem 1rem;
            }}
            
            /* Updated legal points styling to match screenshot */
            .legal-point-section {{
                margin-bottom: 1.5rem;
            }}
            .legal-point-section h6 {{
                font-size: 0.9rem;
                font-weight: 600;
                margin-bottom: 1rem;
                color: #4a5568;
            }}
            .legal-point {{
                background-color: #f8fafc;
                border-radius: 0.25rem;
                padding: 1rem;
                margin-bottom: 0.75rem;
            }}
            .legal-point-header {{
                display: flex;
                gap: 0.5rem;
                margin-bottom: 0.5rem;
            }}
            .legal-badge {{
                display: inline-block;
                padding: 0.2rem 0.5rem;
                font-size: 0.7rem;
                border-radius: 0.25rem;
                background-color: #ebf8ff;
                color: #2c5282;
            }}
            .disputed-badge {{
                display: inline-block;
                padding: 0.2rem 0.5rem;
                font-size: 0.7rem;
                border-radius: 0.25rem;
                background-color: #fed7d7;
                color: #c53030;
            }}
            .legal-point-content {{
                font-size: 0.9rem;
                margin-bottom: 0.75rem;
            }}
            .regulation-badge {{
                display: inline-block;
                padding: 0.2rem 0.5rem;
                font-size: 0.75rem;
                border-radius: 0.25rem;
                background-color: #ebf8ff;
                color: #2c5282;
                margin-right: 0.5rem;
            }}
            .paragraph-badge {{
                font-size: 0.75rem;
                color: #718096;
            }}
            
            /* Nested arguments styling to show the hierarchy clearly */
            .nested-argument {{
                border-left: 1px solid #e2e8f0;
                margin-left: 1.5rem;
                padding-left: 0.75rem;
                margin-top: 0.25rem;
                position: relative;
            }}
            .nested-argument:before {{
                content: "";
                position: absolute;
                left: 0;
                top: 0;
                width: 0.75rem;
                height: 1px;
                background-color: #e2e8f0;
            }}
            .argument-title {{
                color: #3182ce;
                font-weight: 500;
            }}
            .argument-title-respondent {{
                color: #e53e3e;
                font-weight: 500;
            }}
            
            /* Child arguments container */
            .argument-children {{
                padding-left: 1.5rem;
                display: none;
                position: relative;
                border-left: 1px solid #e2e8f0;
                margin-top: 0.25rem;
            }}
            
            /* Badge styling */
            .badge {{
                display: inline-block;
                padding: 0.2rem 0.5rem;
                border-radius: 0.25rem;
                font-size: 0.75rem;
            }}
            .claimant-badge {{
                background-color: #ebf8ff;
                color: #3182ce;
            }}
            .respondent-badge {{
                background-color: #fff5f5;
                color: #e53e3e;
            }}
            .factual-badge {{
                background-color: #f0fff4;
                color: #276749;
                margin-right: 0.25rem;
            }}
            .type-badge {{
                background-color: #edf2f7;
                color: #4a5568;
            }}
            
            /* Content components */
            .content-section {{
                margin-bottom: 1.5rem;
            }}
            .content-section-title {{
                font-size: 0.9rem;
                font-weight: 600;
                margin-bottom: 0.75rem;
                color: #4a5568;
            }}
            
            /* Timeline & Exhibits */
            .actions-bar {{
                display: flex;
                justify-content: flex-end;
                margin-bottom: 1rem;
            }}
            .action-btn {{
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                padding: 0.5rem 1rem;
                background-color: white;
                border: 1px solid #e2e8f0;
                border-radius: 0.375rem;
                font-size: 0.875rem;
                margin-left: 0.5rem;
                cursor: pointer;
            }}
            .search-bar {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 1rem;
            }}
            .search-input-container {{
                position: relative;
            }}
            .search-input {{
                padding: 0.625rem 1rem 0.625rem 2.5rem;
                border: 1px solid #e2e8f0;
                border-radius: 0.375rem;
                width: 16rem;
            }}
            .search-icon {{
                position: absolute;
                left: 12px;
                top: 11px;
            }}
            
            /* Tables */
            .data-table {{
                width: 100%;
                border-collapse: collapse;
                background-color: white;
                border-radius: 0.375rem;
                overflow: hidden;
                border: 1px solid #e2e8f0;
            }}
            .data-table th {{
                background-color: #f7fafc;
                padding: 0.75rem 1rem;
                text-align: left;
                font-size: 0.875rem;
                font-weight: 500;
                color: #4a5568;
                border-bottom: 1px solid #e2e8f0;
            }}
            .data-table td {{
                padding: 0.75rem 1rem;
                font-size: 0.875rem;
                border-bottom: 1px solid #e2e8f0;
            }}
            .data-table tr.disputed {{
                background-color: #fff5f5;
            }}
            
            /* Status indicators */
            .undisputed {{
                color: #2f855a;
            }}
            .disputed {{
                color: #c53030;
            }}
            
            /* Toggle chevron with rotation */
            .chevron {{
                transition: transform 0.2s;
            }}
            .chevron.rotated {{
                transform: rotate(90deg);
            }}
            
            /* Visual indicator of sub-arguments */
            .subargument-count {{
                font-size: 0.75rem;
                font-weight: normal;
                padding: 0.1rem 0.5rem;
                border-radius: 9999px;
                background-color: #edf2f7;
                color: #4a5568;
            }}
            
            /* Display all nested arguments initially */
            .show-all-arguments .argument-children {{
                display: block;
            }}
            .show-all-arguments .argument-content {{
                display: block;
            }}
            .show-all-arguments .chevron {{
                transform: rotate(90deg);
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
            <div class="view-toggle">
                <div class="view-toggle-container">
                    <button class="view-btn active" data-view="standard">Standard View</button>
                    <button class="view-btn" data-view="topic">Topic View</button>
                    <button class="view-btn" data-view="expanded">Show All Sub-arguments</button>
                </div>
            </div>
            
            <!-- Standard View -->
            <div id="standard-view" class="view-content show-all-arguments">
                <div class="arguments-header">
                    <h3 class="claimant-color">Claimant's Arguments</h3>
                    <h3 class="respondent-color">Respondent's Arguments</h3>
                </div>
                <div id="standard-arguments-container"></div>
            </div>
            
            <!-- Topic View -->
            <div id="topic-view" class="view-content" style="display: none;">
                <div id="topics-container"></div>
            </div>
        </div>
        
        <!-- Timeline Tab -->
        <div id="timeline" class="tab-content">
            <div class="actions-bar">
                <button class="action-btn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                    Copy
                </button>
                <button class="action-btn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                        <polyline points="7 10 12 15 17 10"></polyline>
                        <line x1="12" y1="15" x2="12" y2="3"></line>
                    </svg>
                    Export Data
                </button>
            </div>
            
            <div class="search-bar">
                <div style="display: flex; gap: 0.5rem;">
                    <div class="search-input-container">
                        <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                        <input type="text" id="timeline-search" class="search-input" placeholder="Search events...">
                    </div>
                    <button class="action-btn">
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
            <div class="actions-bar">
                <button class="action-btn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                    Copy
                </button>
                <button class="action-btn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                        <polyline points="7 10 12 15 17 10"></polyline>
                        <line x1="12" y1="15" x2="12" y2="3"></line>
                    </svg>
                    Export Data
                </button>
            </div>
            
            <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                <div class="search-input-container">
                    <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    <input type="text" id="exhibits-search" class="search-input" placeholder="Search exhibits...">
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
            
            <table id="exhibits-table" class="data-table">
                <thead>
                    <tr>
                        <th>EXHIBIT ID</th>
                        <th>PARTY</th>
                        <th>TITLE</th>
                        <th>TYPE</th>
                        <th>SUMMARY</th>
                        <th style="text-align: right;">ACTIONS</th>
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
            
            // View switching
            document.querySelectorAll('.view-btn').forEach(btn => {{
                btn.addEventListener('click', function() {{
                    // Update buttons
                    document.querySelectorAll('.view-btn').forEach(b => {{
                        b.classList.remove('active');
                        b.style.backgroundColor = '';
                        b.style.boxShadow = '';
                    }});
                    this.classList.add('active');
                    this.style.backgroundColor = 'white';
                    this.style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';
                    
                    // Update content
                    const viewId = this.getAttribute('data-view');
                    if (viewId === 'standard') {{
                        document.getElementById('standard-view').style.display = 'block';
                        document.getElementById('topic-view').style.display = 'none';
                        document.getElementById('standard-view').classList.remove('show-all-arguments');
                    }} else if (viewId === 'topic') {{
                        document.getElementById('standard-view').style.display = 'none';
                        document.getElementById('topic-view').style.display = 'block';
                        document.getElementById('topic-view').classList.remove('show-all-arguments');
                    }} else if (viewId === 'expanded') {{
                        document.getElementById('standard-view').style.display = 'block';
                        document.getElementById('topic-view').style.display = 'none';
                        document.getElementById('standard-view').classList.add('show-all-arguments');
                    }}
                }});
            }});

            // Render legal points in the flat, cleaner style from screenshot
            function renderLegalPoints(points) {{
                if (!points || points.length === 0) return '';
                
                const pointsHtml = points.map(point => {{
                    const disputed = point.isDisputed 
                        ? `<span class="disputed-badge">Disputed</span>` 
                        : '';
                    
                    const regulations = point.regulations 
                        ? point.regulations.map(reg => `<span class="regulation-badge">${{reg}}</span>`).join('') 
                        : '';
                    
                    return `
                    <div class="legal-point">
                        <div class="legal-point-header">
                            <span class="legal-badge">Legal</span>
                            ${{disputed}}
                        </div>
                        <p class="legal-point-content">${{point.point}}</p>
                        <div>
                            ${{regulations}}
                            <span class="paragraph-badge">¶${{point.paragraphs}}</span>
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="legal-point-section">
                    <h6>Legal Points</h6>
                    ${{pointsHtml}}
                </div>
                `;
            }}
            
            // Render sub-arguments recursively
            function renderSubArguments(arg, side, level = 0) {{
                if (!arg || !arg.children || Object.keys(arg.children).length === 0) {{
                    return '';
                }}
                
                // Style based on side
                const textColorClass = side === 'claimant' ? 'argument-title' : 'argument-title-respondent';
                
                let html = '';
                
                // Render each child argument
                Object.values(arg.children).forEach(child => {{
                    const childId = `${{side}}-${{child.id}}`;
                    const hasSubArgs = child.children && Object.keys(child.children).length > 0;
                    const subArgCount = hasSubArgs ? Object.keys(child.children).length : 0;
                    
                    html += `
                    <div class="nested-argument">
                        <div class="argument-header" id="header-${{childId}}">
                            <div class="argument-header-left">
                                <svg class="chevron" id="chevron-${{childId}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <span class="${{textColorClass}}">${{child.id}}. ${{child.title}}</span>
                                ${{hasSubArgs ? `<span class="subargument-count">${{subArgCount}} subarguments</span>` : `<span class="paragraph-badge">¶${{child.paragraphs}}</span>`}}
                            </div>
                        </div>
                        
                        <div class="argument-content" id="content-${{childId}}">
                            ${{renderLegalPoints(child.legalPoints || [])}}
                        </div>
                        
                        ${{renderSubArguments(child, side, level + 1)}}
                    </div>
                    `;
                }});
                
                return html;
            }}
            
            // Render a single argument with sub-arguments
            function renderArgument(arg, side) {{
                if (!arg) return '';
                
                const argId = `${{side}}-${{arg.id}}`;
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const childCount = hasChildren ? Object.keys(arg.children).length : 0;
                
                // Style based on side
                const headerBgClass = side === 'claimant' ? 'bg-blue-50' : 'bg-red-50';
                const textColorClass = side === 'claimant' ? 'argument-title' : 'argument-title-respondent';
                
                // Main argument
                let html = `
                <div class="argument" id="arg-${{argId}}">
                    <div class="argument-header" id="header-${{argId}}">
                        <div class="argument-header-left">
                            <svg class="chevron" id="chevron-${{argId}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6"></polyline>
                            </svg>
                            <span class="${{textColorClass}}">${{arg.id}}. ${{arg.title}}</span>
                            ${{hasChildren ? `<span class="subargument-count">${{childCount}} subarguments</span>` : `<span class="paragraph-badge">¶${{arg.paragraphs}}</span>`}}
                        </div>
                    </div>
                    
                    <div class="argument-content" id="content-${{argId}}">
                        ${{renderLegalPoints(arg.legalPoints || [])}}
                    </div>
                    
                    ${{renderSubArguments(arg, side)}}
                </div>
                `;
                
                return html;
            }}
            
            // Render a pair of arguments (claimant and respondent)
            function renderArgumentPair(claimantArg, respondentArg) {{
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
                
                // Add click handlers
                document.querySelectorAll('.argument-header').forEach(header => {{
                    header.addEventListener('click', function() {{
                        // Get the content and chevron elements
                        const contentId = this.id.replace('header-', 'content-');
                        const chevronId = this.id.replace('header-', 'chevron-');
                        
                        const content = document.getElementById(contentId);
                        const chevron = document.getElementById(chevronId);
                        
                        // Toggle display
                        if (content) {{
                            content.style.display = content.style.display === 'block' ? 'none' : 'block';
                        }}
                        
                        // Toggle chevron rotation
                        if (chevron) {{
                            chevron.classList.toggle('rotated');
                        }}
                    }});
                }});
            }}
            
            // Render the topic view
            function renderTopicView() {{
                const container = document.getElementById('topics-container');
                let html = '';
                
                // For each topic
                argsData.topics.forEach(topic => {{
                    html += `
                    <div class="topic-section show-all-arguments">
                        <h2 class="topic-title">${{topic.title}}</h2>
                        <p class="topic-description">${{topic.description}}</p>
                        
                        <div class="arguments-header">
                            <h3 class="claimant-color">Claimant's Arguments</h3>
                            <h3 class="respondent-color">Respondent's Arguments</h3>
                        </div>
                    `;
                    
                    // Add arguments for this topic
                    topic.argumentIds.forEach(argId => {{
                        if (argsData.claimantArgs[argId] && argsData.respondentArgs[argId]) {{
                            const claimantArg = argsData.claimantArgs[argId];
                            const respondentArg = argsData.respondentArgs[argId];
                            
                            html += renderArgumentPair(claimantArg, respondentArg);
                        }}
                    }});
                    
                    html += `</div>`;
                }});
                
                container.innerHTML = html;
            }}
            
            // Render timeline
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
                
                // Clear existing content
                tbody.innerHTML = '';
                
                // Filter data if needed
                const searchTerm = document.getElementById('timeline-search').value.toLowerCase();
                const disputedOnly = document.getElementById('disputed-only').checked;
                
                const filteredData = timelineData.filter(item => {{
                    // Search filter
                    const matchesSearch = 
                        !searchTerm || 
                        item.appellantVersion.toLowerCase().includes(searchTerm) || 
                        item.respondentVersion.toLowerCase().includes(searchTerm);
                    
                    // Disputed filter
                    const matchesDisputed = !disputedOnly || item.status === 'Disputed';
                    
                    return matchesSearch && matchesDisputed;
                }});
                
                // Render rows
                filteredData.forEach(item => {{
                    const row = document.createElement('tr');
                    
                    if (item.status === 'Disputed') {{
                        row.classList.add('disputed');
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
                const typeFilter = document.getElementById('type-filter');
                
                // Clear existing content
                tbody.innerHTML = '';
                
                // Populate type filter if needed
                if (typeFilter.options.length === 1) {{
                    const types = [...new Set(exhibitsData.map(item => item.type))];
                    types.forEach(type => {{
                        const option = document.createElement('option');
                        option.value = type;
                        option.textContent = type.charAt(0).toUpperCase() + type.slice(1);
                        typeFilter.appendChild(option);
                    }});
                }}
                
                // Filter data if needed
                const searchTerm = document.getElementById('exhibits-search').value.toLowerCase();
                const partyFilter = document.getElementById('party-filter').value;
                const selectedType = typeFilter.value;
                
                const filteredData = exhibitsData.filter(item => {{
                    // Search filter
                    const matchesSearch = 
                        !searchTerm || 
                        item.id.toLowerCase().includes(searchTerm) || 
                        item.title.toLowerCase().includes(searchTerm) ||
                        item.summary.toLowerCase().includes(searchTerm);
                    
                    // Party filter
                    const matchesParty = 
                        partyFilter === 'All Parties' || 
                        item.party === partyFilter;
                    
                    // Type filter
                    const matchesType = 
                        selectedType === 'All Types' || 
                        item.type === selectedType;
                    
                    return matchesSearch && matchesParty && matchesType;
                }});
                
                // Render rows
                filteredData.forEach(item => {{
                    const row = document.createElement('tr');
                    const badgeClass = item.party === 'Appellant' ? 'claimant-badge' : 'respondent-badge';
                    
                    row.innerHTML = `
                        <td>${{item.id}}</td>
                        <td><span class="badge ${{badgeClass}}">${{item.party}}</span></td>
                        <td>${{item.title}}</td>
                        <td><span class="badge type-badge">${{item.type}}</span></td>
                        <td>${{item.summary}}</td>
                        <td style="text-align: right;"><a href="#" style="color: #3182ce; text-decoration: none;">View</a></td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Initialize the page
            renderStandardArguments();
            renderTopicView();
            
            // Set up event listeners
            document.getElementById('timeline-search')?.addEventListener('input', renderTimeline);
            document.getElementById('disputed-only')?.addEventListener('change', renderTimeline);
            document.getElementById('exhibits-search')?.addEventListener('input', renderExhibits);
            document.getElementById('party-filter')?.addEventListener('change', renderExhibits);
            document.getElementById('type-filter')?.addEventListener('change', renderExhibits);
            
            // Set initial active button style
            document.querySelector('.view-btn.active').style.backgroundColor = 'white';
            document.querySelector('.view-btn.active').style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
