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
                    "summary": "Official records showing continuous name usage",
                    "citations": ["20", "21", "24"],
                    "context": "These documents include the original club registration certificate from 1950 along with annual renewal certificates spanning the entire period up to present day. The records show consistent use of the club name across all official documentation.",
                    "significance": "The continuous record of registration demonstrates an unbroken administrative history, which supports the claim of sporting succession. Particularly noteworthy are the stamps and signatures from the football association confirming the club's status each year."
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2016/A/4576",
                    "title": "Criteria for sporting succession",
                    "relevance": "Establishes key factors for succession",
                    "paragraphs": "45-48",
                    "citedParagraphs": ["45", "46", "47"],
                    "keyFindings": "The panel in this case established that sporting succession depends on several key factors: (1) Continuous use of identifying elements such as name, colors, and badge; (2) Uninterrupted participation in competitions; (3) Recognition by the relevant sporting authorities; and (4) Public perception of continuity.",
                    "precedentialValue": "This case is considered the leading authority on sporting succession and has been cited in numerous subsequent CAS awards. It moved away from previous jurisprudence that focused primarily on legal continuity to a more holistic approach that considers sporting reality."
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
                                    "summary": "Official documentation of registration history",
                                    "citations": ["25", "26", "28"],
                                    "context": "These documents include the original application for club registration submitted on March 12, 1950, bearing the signatures of the founding members and official approval dated April 3, 1950. Also included are documentation from 1975-1976 showing the administrative process during the reorganization period.",
                                    "significance": "The registration records establish the formal creation date of the club and provide evidence regarding the contested administrative gap. The reorganization documents show that while there was a procedural lapse in formal registration, club activities continued during this period with the same personnel and facilities."
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
                            "summary": "Visual evidence of consistent color usage",
                            "citations": ["53", "54", "55"],
                            "context": "This collection includes 47 photographs spanning from 1950 to present day showing the team in its official kit during matches, ceremonies, and official photoshoots. The photographs are arranged chronologically and include metadata verifying their dates and occasions. Each decade is represented by multiple images to establish continuity.",
                            "significance": "The photographic evidence demonstrates the consistent use of blue and white as the primary club colors throughout its history. While there are minor variations in shade and design elements, the core identity remains intact. Particularly notable are the championship photographs from 1958, 1967, 1982, and 2014 showing the consistent color scheme despite changes in kit manufacturers and sponsors."
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
                                            "summary": "Historical documents showing color usage",
                                            "citations": ["61", "62", "63"],
                                            "context": "This exhibit contains the club's official style guides from 1965, 1978, 1985, and 1992, showing the exact Pantone color specifications used in each era. Also included are merchandise catalogs, official communications, and marketing materials that showcase the evolving but consistent color scheme. Of particular interest is the 1985 'Brand Evolution Document' that explicitly addresses the addition of red as an accent color.",
                                            "significance": "These archives provide precise technical specifications for the club colors across different eras, establishing that while there were variations in exact shades of blue (from navy to royal blue) and layout of white elements, these changes were evolutionary rather than revolutionary. The documents also explain the rationale behind the temporary addition of red elements (1982-1988) as a marketing strategy that was later abandoned to return to the traditional blue and white scheme."
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
                    "summary": "Records showing non-participation in 1975-1976 season",
                    "citations": ["208", "209", "210"],
                    "context": "This exhibit contains official league tables, match reports, and administrative correspondence from the national football federation for the 1975-1976 season. Specifically, it includes the official participant list for the 1975-1976 season showing the absence of the club, minutes from federation meetings discussing the club's withdrawal, and correspondence regarding the reapplication process initiated in late 1976.",
                    "significance": "These federation records constitute primary evidence from the governing body of the sport showing that the club did not participate in official competitions during the 1975-1976 season. Particularly significant is the March 1976 federation bulletin that categorizes the club as 'inactive' and the September 1976 documentation treating the club's application as a 'new entity' rather than a continuing member."
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2017/A/5465",
                    "title": "Operational continuity requirement",
                    "relevance": "Establishes primacy of operational continuity",
                    "paragraphs": "211-213",
                    "citedParagraphs": ["212"],
                    "keyFindings": "This case examined a similar sporting succession dispute involving a 14-month interruption in competitive activities. The panel held that 'mere retention of identifying elements such as name, colors, and badge is insufficient to establish sporting succession if there is a substantial interruption in the club's primary activity—participation in official competitions.' The panel specifically noted that 'the essence of a sporting club is competition; extended absence from competition constitutes a fundamental break in identity.'",
                    "precedentialValue": "This more recent case refined the principles established in CAS 2016/A/4576 by emphasizing that actual sporting activity takes precedence over symbolic continuity elements. It established a hierarchy of factors where participation in competitions is considered the most essential element of sporting succession, followed by administrative continuity, with symbolic elements (name, colors, etc.) being necessary but not sufficient conditions."
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
                                    "summary": "Official documentation of registration termination",
                                    "citations": ["226", "227"],
                                    "context": "This exhibit contains two key official documents: (1) The Termination Certificate issued by the National Sports Registry on April 30, 1975, bearing the official seal and signature of the Registrar, explicitly stating that the club 'has ceased to exist as a registered entity.' (2) The New Entity Registration Certificate dated September 15, 1976, which classifies the application as a 'new registration' rather than a 'renewal' or 'reinstatement' and assigns a new registration number (76/1429) distinct from the previous entity's number (50/0872).",
                                    "significance": "These official registration documents establish that from a legal and administrative perspective, there was a complete termination of the original entity followed by the creation of a new entity with similar identifying elements. The registration forms filed with the application in 1976 make no reference to being a continuation of the previous club, and the officials who signed these documents treated it as an entirely new entity. The change in registration numbers is particularly significant as it indicates the administrative system considered this a new organization rather than a continuation."
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
                            "summary": "Visual evidence of color scheme changes",
                            "citations": ["245", "246", "247"],
                            "context": "This exhibit presents a side-by-side comparative analysis of team uniforms before and after 1976, including: (1) Match-day photographs from the 1974-75 season showing navy blue and white vertical stripes; (2) First match photographs from October 1976 showing royal blue with white accents; (3) Comparative color analysis performed by an independent design expert identifying specific Pantone color differences; (4) Local newspaper articles from 1976 specifically commenting on the 'new look' of the team with quotes from supporters discussing the color change.",
                            "significance": "This comparative visual evidence demonstrates that beyond mere shade variations, there was a fundamental redesign of the club colors and pattern upon the 1976 re-establishment. The change from navy blue and white vertical stripes to royal blue with white accents represents a significant rebranding rather than a minor variation. Contemporary accounts from supporters and media coverage confirm that this was perceived as a deliberate break from tradition at the time, with the new ownership explicitly stating they wanted to 'create a new visual identity' for the club."
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
                                            "summary": "Historical brand guidelines showing color changes",
                                            "citations": ["250", "251", "252"],
                                            "context": "This collection includes original promotional materials and internal documents explaining the symbolism of the club colors: (1) The 1950 founding charter explicitly stating that the navy blue and white stripes were chosen to represent the maritime heritage of the original North District; (2) The 1976 'New Era' marketing brochure announcing that 'the royal blue color represents the traditional color of [New Owner's] East District where the club will now be based'; (3) Internal design brief documents from 1976 instructing designers to 'create a clear visual break from the past' and 'establish a new beginning through color symbolism'.",
                                            "significance": "These documents provide crucial context for the color changes, demonstrating that they were not arbitrary aesthetic modifications but deliberate symbolic choices tied to the club's geographic identity. The explicit statements in the 1976 materials about representing a new district and creating 'a clear visual break from the past' directly contradict the claim of continuous identity. The color change was specifically designed and marketed as a transformation rather than an evolution, targeting a new fan base in a different part of the city."
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
            
            /* Argument card and details */
            .argument {{
                border: 1px solid #e2e8f0;
                border-radius: 0.375rem;
                overflow: hidden;
                margin-bottom: 1rem;
            }}
            .argument-header {{
                padding: 0.75rem 1rem;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            .argument-header-left {{
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            .argument-content {{
                padding: 1rem;
                border-top: 1px solid #e2e8f0;
                display: none;
                background-color: white;
            }}
            .claimant-header {{
                background-color: #ebf8ff;
                border-color: #bee3f8;
            }}
            .respondent-header {{
                background-color: #fff5f5;
                border-color: #fed7d7;
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
                background-color: rgba(59, 130, 246, 0.5);
            }}
            .respondent-connector {{
                background-color: rgba(239, 68, 68, 0.5);
            }}
            
            /* Badge styling */
            .badge {{
                display: inline-block;
                padding: 0.25rem 0.5rem;
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
            .legal-badge {{
                background-color: #ebf8ff;
                color: #2c5282;
                margin-right: 0.25rem;
            }}
            .factual-badge {{
                background-color: #f0fff4;
                color: #276749;
                margin-right: 0.25rem;
            }}
            .exhibit-badge {{
                background-color: #fef3c7;
                color: #d97706;
                margin-right: 0.25rem;
            }}
            .disputed-badge {{
                background-color: #fed7d7;
                color: #c53030;
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
                font-size: 0.875rem;
                font-weight: 500;
                margin-bottom: 0.5rem;
            }}
            .point-block {{
                background-color: #f7fafc;
                border-radius: 0.5rem;
                padding: 0.75rem;
                margin-bottom: 0.5rem;
            }}
            .point-header {{
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 0.25rem;
            }}
            .point-date {{
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 0.25rem;
                font-size: 0.75rem;
                color: #718096;
            }}
            .point-text {{
                font-size: 0.875rem;
                color: #4a5568;
            }}
            .point-citation {{
                display: inline-block;
                margin-top: 0.5rem;
                font-size: 0.75rem;
                color: #718096;
            }}
            
            /* Overview points */
            .overview-block {{
                background-color: #f7fafc;
                border-radius: 0.5rem;
                padding: 1rem;
                margin-bottom: 1rem;
            }}
            .overview-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 0.5rem;
            }}
            .overview-list {{
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
            }}
            .overview-item {{
                display: flex;
                align-items: flex-start;
                gap: 0.5rem;
                margin-bottom: 0.25rem;
            }}
            .overview-bullet {{
                width: 6px;
                height: 6px;
                border-radius: 50%;
                background-color: #3182ce;
                margin-top: 0.5rem;
            }}
            .overview-point-container {{
                display: flex;
                flex-direction: column;
                flex: 1;
            }}
            .overview-point-row {{
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
            }}
            
            /* Evidence and Case Law */
            .reference-block {{
                background-color: #f7fafc;
                border-radius: 0.5rem;
                padding: 0.75rem;
                margin-bottom: 0.5rem;
            }}
            .reference-header {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 0.25rem;
            }}
            .reference-title {{
                font-size: 0.875rem;
                font-weight: 500;
            }}
            .reference-summary {{
                font-size: 0.75rem;
                color: #718096;
                margin-top: 0.25rem;
                margin-bottom: 0.5rem;
            }}
            .reference-citations {{
                display: flex;
                flex-wrap: wrap;
                gap: 0.25rem;
                margin-top: 0.5rem;
            }}
            .citation-tag {{
                background-color: #edf2f7;
                color: #4a5568;
                padding: 0.125rem 0.375rem;
                border-radius: 0.25rem;
                font-size: 0.75rem;
            }}
            
            /* Detailed information sections */
            .detail-section {{
                margin-top: 1rem;
                border-top: 1px solid #e2e8f0;
                padding-top: 0.75rem;
            }}
            .detail-heading {{
                font-size: 0.8rem;
                font-weight: 600;
                color: #4a5568;
                margin-bottom: 0.5rem;
            }}
            .detail-content {{
                font-size: 0.8rem;
                color: #4a5568;
                margin-bottom: 0.75rem;
                line-height: 1.4;
            }}
            
            /* Legal references styling */
            .factual-point {{
                background-color: #f0fff4;
                border-radius: 0.5rem;
                padding: 0.75rem;
                margin-bottom: 0.5rem;
            }}
            
            /* Topic view */
            .topic-section {{
                margin-bottom: 2rem;
            }}
            .topic-title {{
                font-size: 1.25rem;
                font-weight: 600;
                color: #2d3748;
                margin-bottom: 0.25rem;
            }}
            .topic-description {{
                font-size: 0.875rem;
                color: #718096;
                margin-bottom: 1rem;
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
                </div>
            </div>
            
            <!-- Standard View -->
            <div id="standard-view" class="view-content">
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
                    }} else {{
                        document.getElementById('standard-view').style.display = 'none';
                        document.getElementById('topic-view').style.display = 'block';
                    }}
                }});
            }});
            
            // Render overview points - Supporting Points
            function renderOverviewPoints(overview) {{
                if (!overview || !overview.points || overview.points.length === 0) return '';
                
                const pointsHtml = overview.points.map(point => 
                    `<div class="overview-item">
                        <div class="overview-bullet"></div>
                        <div class="overview-point-container">
                            <div class="overview-point-row">
                                <span class="point-text">${{point}}</span>
                                <span class="badge claimant-badge">¶${{overview.paragraphs}}</span>
                            </div>
                        </div>
                    </div>`
                ).join('');
                
                return `
                <div class="overview-block">
                    <div class="overview-header">
                        <h6 class="content-section-title">Supporting Points</h6>
                    </div>
                    <div class="overview-list">
                        ${{pointsHtml}}
                    </div>
                </div>
                `;
            }}
            
            // Render factual points with exhibit numbers
            function renderFactualPoints(points) {{
                if (!points || points.length === 0) return '';
                
                const pointsHtml = points.map(point => {{
                    const disputed = point.isDisputed 
                        ? `<span class="badge disputed-badge">Disputed by ${{point.source || ''}}</span>` 
                        : '';
                    
                    // Exhibits badges
                    const exhibitBadges = point.exhibits && point.exhibits.length > 0
                        ? point.exhibits.map(exhibitId => `<span class="badge exhibit-badge">${{exhibitId}}</span>`).join('')
                        : '';
                    
                    return `
                    <div class="factual-point">
                        <div class="point-header">
                            <span class="badge factual-badge">Factual</span>
                            ${{disputed}}
                        </div>
                        <div class="point-date">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                <line x1="3" y1="10" x2="21" y2="10"></line>
                            </svg>
                            ${{point.date}}
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <p class="point-text">${{point.point}}</p>
                            <div style="margin-left: 8px; display: flex; gap: 4px;">
                                ${{exhibitBadges}}
                            </div>
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="content-section">
                    <h6 class="content-section-title">Factual Points</h6>
                    ${{pointsHtml}}
                </div>
                `;
            }}
            
            // Render evidence - expanded with more detailed explanation
            function renderEvidence(evidence) {{
                if (!evidence || evidence.length === 0) return '';
                
                const itemsHtml = evidence.map(item => {{
                    const citations = item.citations 
                        ? item.citations.map(cite => `<span class="citation-tag">¶${{cite}}</span>`).join('') 
                        : '';
                    
                    // Additional detailed content
                    const contextSection = item.context 
                        ? `<div class="detail-section">
                              <div class="detail-heading">Document Contents:</div>
                              <div class="detail-content">${{item.context}}</div>
                           </div>`
                        : '';
                        
                    const significanceSection = item.significance
                        ? `<div class="detail-section">
                              <div class="detail-heading">Evidentiary Significance:</div>
                              <div class="detail-content">${{item.significance}}</div>
                           </div>`
                        : '';
                    
                    return `
                    <div class="reference-block">
                        <div class="reference-header">
                            <span class="reference-title">${{item.id}}: ${{item.title}}</span>
                            <button class="action-btn" style="padding: 0; height: 20px; background: none; border: none;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3182ce" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                                </svg>
                            </button>
                        </div>
                        <p class="reference-summary">${{item.summary}}</p>
                        <div class="reference-citations">
                            <span style="font-size: 0.75rem; color: #718096;">Cited in:</span>
                            ${{citations}}
                        </div>
                        ${{contextSection}}
                        ${{significanceSection}}
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="content-section">
                    <h6 class="content-section-title">Documentary Exhibits</h6>
                    ${{itemsHtml}}
                </div>
                `;
            }}
            
            // Render case law - expanded with more detailed explanation
            function renderCaseLaw(cases) {{
                if (!cases || cases.length === 0) return '';
                
                const itemsHtml = cases.map(item => {{
                    const citedParagraphs = item.citedParagraphs 
                        ? item.citedParagraphs.map(para => `<span class="citation-tag">¶${{para}}</span>`).join('') 
                        : '';
                    
                    // Additional detailed content
                    const keyFindingsSection = item.keyFindings
                        ? `<div class="detail-section">
                              <div class="detail-heading">Key Findings:</div>
                              <div class="detail-content">${{item.keyFindings}}</div>
                           </div>`
                        : '';
                        
                    const precedentialValueSection = item.precedentialValue
                        ? `<div class="detail-section">
                              <div class="detail-heading">Precedential Value:</div>
                              <div class="detail-content">${{item.precedentialValue}}</div>
                           </div>`
                        : '';
                    
                    return `
                    <div class="reference-block">
                        <div class="reference-header">
                            <div>
                                <span class="reference-title">${{item.caseNumber}}</span>
                                <span class="point-citation" style="margin-left: 0.5rem;">¶${{item.paragraphs}}</span>
                            </div>
                            <button class="action-btn" style="padding: 0; height: 20px; background: none; border: none;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3182ce" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                                </svg>
                            </button>
                        </div>
                        <p class="reference-summary">${{item.title}}</p>
                        <p class="point-text">${{item.relevance}}</p>
                        <div class="reference-citations">
                            <span style="font-size: 0.75rem; color: #718096;">Key Paragraphs:</span>
                            ${{citedParagraphs}}
                        </div>
                        ${{keyFindingsSection}}
                        ${{precedentialValueSection}}
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="content-section">
                    <h6 class="content-section-title">Case Law</h6>
                    ${{itemsHtml}}
                </div>
                `;
            }}
            
            // Render argument content
            function renderArgumentContent(arg) {{
                let content = '';
                
                // Overview points
                if (arg.overview) {{
                    content += renderOverviewPoints(arg.overview);
                }}
                
                // Factual points
                if (arg.factualPoints) {{
                    content += renderFactualPoints(arg.factualPoints);
                }}
                
                // Evidence
                if (arg.evidence) {{
                    content += renderEvidence(arg.evidence);
                }}
                
                // Case law
                if (arg.caseLaw) {{
                    content += renderCaseLaw(arg.caseLaw);
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
                const baseColor = side === 'claimant' ? '#3182ce' : '#e53e3e';
                const headerClass = side === 'claimant' ? 'claimant-header' : 'respondent-header';
                const badgeClass = side === 'claimant' ? 'claimant-badge' : 'respondent-badge';
                const connectorClass = side === 'claimant' ? 'claimant-connector' : 'respondent-connector';
                
                // Header content
                const headerHtml = `
                <div class="argument-header-left">
                    <svg id="chevron-${{fullId}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s ease;">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                    <h5 style="font-size: 0.875rem; font-weight: 500; color: ${{baseColor}};">
                        ${{arg.id}}. ${{arg.title}}
                    </h5>
                </div>
                <div>
                    ${{hasChildren 
                        ? `<span class="badge ${{badgeClass}}" style="border-radius: 9999px;">${{childCount}} subarguments</span>` 
                        : `<span class="badge ${{badgeClass}}">¶${{arg.paragraphs}}</span>`
                    }}
                </div>
                `;
                
                // Detailed content
                const contentHtml = renderArgumentContent(arg);
                
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
                <div class="argument ${{headerClass}}" style="${{level > 0 ? 'position: relative;' : ''}}">
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
            
            // Render the topic view
            function renderTopicView() {{
                const container = document.getElementById('topics-container');
                let html = '';
                
                // For each topic
                argsData.topics.forEach(topic => {{
                    html += `
                    <div class="topic-section">
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
            document.getElementById('timeline-search').addEventListener('input', renderTimeline);
            document.getElementById('disputed-only').addEventListener('change', renderTimeline);
            document.getElementById('exhibits-search').addEventListener('input', renderExhibits);
            document.getElementById('party-filter').addEventListener('change', renderExhibits);
            document.getElementById('type-filter').addEventListener('change', renderExhibits);
            
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
