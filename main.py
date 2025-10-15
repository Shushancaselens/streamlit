import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="TechStart Inc. v. MegaCorp Ltd.", layout="wide")

# Override Streamlit's default styling to use full width and custom colors
st.markdown("""
<style>
    .main .block-container {
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: none;
    }
    /* Use #3B82F6 as primary color */
    .stButton > button[kind="primary"] {
        background-color: #3B82F6;
        border-color: #3B82F6;
    }
    .stButton > button[kind="primary"]:hover {
        background-color: #2563EB;
        border-color: #2563EB;
    }
    /* Reduce search input height */
    .stTextInput > div > div > input {
        height: 44px !important;
        padding: 8px 16px !important;
        font-size: 15px !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 8px !important;
    }
    /* Make search container taller */
    .stTextInput > div {
        height: 40px !important;
    }
    .stTextInput {
        height: 40px !important;
    }
    /* Make search button 40px */
    .stButton > button {
        height: 40px !important;
        padding: 8px 24px !important;
        font-size: 15px !important;
    }
    /* Add spacing to title */
    h1 {
        margin-bottom: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Arguments"

# Create data structures as JSON for embedded components
def get_argument_data():
    claimant_args = {
        "1": {
            "id": "1",
            "title": "Breach of Software Licensing Agreement",
            "paragraphs": "15-35",
            "overview": {
                "points": [
                    "Material breach of payment obligations under Section 4.2",
                    "Unauthorized use beyond licensed territory in violation of Section 2.1",
                    "Failure to provide required usage reports per Section 5.3"
                ],
                "paragraphs": "15-17"
            },
            "factualPoints": [
                {
                    "point": "MegaCorp failed to make quarterly license payments for Q3 and Q4 2023",
                    "date": "2023-07-01 to 2023-12-31",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "18-20",
                    "exhibits": ["C-1", "C-2"]
                }
            ],
            "evidence": [
                {
                    "id": "C-1",
                    "title": "Software Licensing Agreement",
                    "summary": "Master licensing agreement executed on January 15, 2023, between TechStart Inc. and MegaCorp Ltd., governing the licensing of TechStart's proprietary AI analytics software platform including payment terms, territorial restrictions, and usage obligations.",
                    "citations": ["18", "19", "22"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 21045/2019",
                    "title": "Material breach in software licensing",
                    "relevance": "Established that failure to make scheduled license payments for more than 60 days constitutes material breach, regardless of disputes over calculation methodology. The tribunal emphasized that payment obligations are independent of performance disputes unless explicitly linked in the contract.",
                    "paragraphs": "23-26",
                    "citedParagraphs": ["24", "25"]
                }
            ],
            "children": {
                "1.1": {
                    "id": "1.1",
                    "title": "Payment Obligations Breach",
                    "paragraphs": "30-55",
                    "overview": {
                        "points": [
                            "Clear contractual payment schedule in Section 4.2",
                            "No valid dispute resolution procedure invoked",
                            "Acceptance of software continued during non-payment"
                        ],
                        "paragraphs": "30-32"
                    },
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Quarterly Payment Analysis",
                            "paragraphs": "40-45",
                            "factualPoints": [
                                {
                                    "point": "Q3 2023 payment of $2.5M due July 1, 2023 - never received",
                                    "date": "2023-07-01",
                                    "isDisputed": False,
                                    "paragraphs": "40-41",
                                    "exhibits": ["C-3"]
                                },
                                {
                                    "point": "Q4 2023 payment of $2.8M due October 1, 2023 - partial payment only",
                                    "date": "2023-10-01",
                                    "isDisputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "42-43",
                                    "exhibits": ["C-3", "C-4"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "C-3",
                                    "title": "Payment Schedule and Banking Records",
                                    "summary": "Detailed payment schedule from the licensing agreement and TechStart's banking records showing all payments received from MegaCorp, including wire transfer confirmations and account statements for the entire contract period.",
                                    "citations": ["40", "41", "42"]
                                }
                            ]
                        }
                    }
                },
                "1.2": {
                    "id": "1.2",
                    "title": "Territorial Usage Violations",
                    "paragraphs": "56-75",
                    "overview": {
                        "points": [
                            "License limited to North American territory",
                            "Evidence of European deployment without authorization",
                            "Usage logs confirm unauthorized geographic expansion"
                        ],
                        "paragraphs": "56-58"
                    },
                    "factualPoints": [
                        {
                            "point": "Software deployed in UK and German data centers without additional licensing",
                            "date": "2023-09-15 to present",
                            "isDisputed": True,
                            "source": "Respondent",
                            "paragraphs": "62-65",
                            "exhibits": ["C-7"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "C-7",
                            "title": "Server Access Logs and Geographic Data",
                            "summary": "Comprehensive server access logs from TechStart's monitoring systems showing API calls and data processing requests originating from IP addresses in European Union countries, including detailed timestamp and geographic location data.",
                            "citations": ["62", "63", "64"]
                        }
                    ]
                }
            }
        },
        "2": {
            "id": "2",
            "title": "Intellectual Property Ownership Disputes",
            "paragraphs": "76-95",
            "overview": {
                "points": [
                    "Unauthorized creation of derivative works",
                    "Breach of IP ownership provisions in Section 7",
                    "Misappropriation of proprietary algorithms"
                ],
                "paragraphs": "76-78"
            },
            "factualPoints": [
                {
                    "point": "MegaCorp developed competing software using TechStart's proprietary algorithms",
                    "date": "2023-11-01 to present",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "82-85",
                    "exhibits": ["C-9"]
                }
            ],
            "evidence": [
                {
                    "id": "C-9",
                    "title": "Code Analysis Report",
                    "summary": "Expert technical analysis comparing TechStart's proprietary algorithms with MegaCorp's newly developed software, identifying substantial similarities in core computational methods and data processing approaches.",
                    "citations": ["82", "83", "84"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "LCIA Ref. 156789",
                    "title": "Derivative works in software licensing",
                    "relevance": "Established that licensees cannot create derivative works or competing products using licensed technology without explicit authorization. The tribunal ruled that even improvements made by the licensee remain subject to the original IP ownership terms.",
                    "paragraphs": "86-88",
                    "citedParagraphs": ["87"]
                }
            ]
        },
        "5": {
            "id": "5",
            "title": "No Confidentiality Breach",
            "paragraphs": "336-360",
            "overview": {
                "points": [
                    "Information shared was not confidential under agreement definition",
                    "Public domain and independently developed information",
                    "TechStart's claims are speculative and unsubstantiated"
                ],
                "paragraphs": "336-338"
            },
            "factualPoints": [
                {
                    "point": "Alleged confidential information was publicly available through TechStart's own documentation",
                    "date": "2023-05-01",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "342-345",
                    "exhibits": ["R-13", "R-14"]
                },
                {
                    "point": "MegaCorp developed similar technology independently before TechStart disclosure",
                    "date": "2022-11-01 to 2023-01-14",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "346-349",
                    "exhibits": ["R-15"]
                }
            ],
            "evidence": [
                {
                    "id": "R-13",
                    "title": "Public TechStart Documentation",
                    "summary": "Screenshots and archives of TechStart's publicly available technical documentation containing alleged confidential information.",
                    "citations": ["342", "343"]
                },
                {
                    "id": "R-14",
                    "title": "Industry Standard Practices Analysis",
                    "summary": "Expert report showing that alleged confidential methods are standard industry practices known to all practitioners.",
                    "citations": ["344", "345"]
                },
                {
                    "id": "R-15",
                    "title": "Prior Development Records",
                    "summary": "MegaCorp's internal development documentation predating licensing agreement showing independent development of similar technology.",
                    "citations": ["346", "347", "348"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "SIAC ARB 089/2020",
                    "title": "Definition of confidential information",
                    "relevance": "Established that information publicly available or independently developed cannot be deemed confidential, and that burden rests on claiming party to prove information meets contractual definition of confidentiality.",
                    "paragraphs": "353-357",
                    "citedParagraphs": ["354", "355"]
                }
            ]
        },
        "6": {
            "id": "6",
            "title": "No Indemnification Obligation",
            "paragraphs": "361-385",
            "overview": {
                "points": [
                    "Third-party claims resulted from TechStart's IP defects, not MegaCorp's use",
                    "TechStart failed to provide proper indemnification to MegaCorp",
                    "Indemnification clause does not cover TechStart's own IP problems"
                ],
                "paragraphs": "361-363"
            },
            "factualPoints": [
                {
                    "point": "Patent claims arose from TechStart's underlying code, not territorial deployment",
                    "date": "2024-02-15",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "367-370",
                    "exhibits": ["R-16"]
                },
                {
                    "point": "TechStart refused MegaCorp's indemnification demand for patent defense",
                    "date": "2024-03-10",
                    "isDisputed": False,
                    "paragraphs": "371-373",
                    "exhibits": ["R-17", "R-18"]
                }
            ],
            "evidence": [
                {
                    "id": "R-16",
                    "title": "Patent Claim Technical Analysis",
                    "summary": "Expert analysis of third-party patent claims showing they target TechStart's core algorithms, not MegaCorp's deployment decisions.",
                    "citations": ["367", "368", "369"]
                },
                {
                    "id": "R-17",
                    "title": "MegaCorp Indemnification Demand",
                    "summary": "MegaCorp's formal demand to TechStart for indemnification under Section 8.1 for patent infringement claims.",
                    "citations": ["371", "372"]
                },
                {
                    "id": "R-18",
                    "title": "TechStart's Refusal to Defend",
                    "summary": "TechStart's response refusing to defend or indemnify MegaCorp against third-party patent claims.",
                    "citations": ["373"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 19234/2018",
                    "title": "Indemnification for IP infringement",
                    "relevance": "Confirmed that licensors must indemnify licensees for IP claims arising from the licensed technology itself, regardless of how licensee uses the technology.",
                    "paragraphs": "377-381",
                    "citedParagraphs": ["378", "379"]
                }
            ]
        },
        "7": {
            "id": "7",
            "title": "Proper Exercise of Privacy Rights",
            "paragraphs": "386-410",
            "overview": {
                "points": [
                    "Audit timing conflicted with critical business operations",
                    "MegaCorp offered reasonable alternative dates",
                    "TechStart refused to accommodate legitimate business needs"
                ],
                "paragraphs": "386-388"
            },
            "factualPoints": [
                {
                    "point": "Proposed audit coincided with quarter-end financial close requiring all systems",
                    "date": "2023-09-05",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "392-395",
                    "exhibits": ["R-19"]
                },
                {
                    "point": "MegaCorp offered alternative audit dates in October 2023, declined by TechStart",
                    "date": "2023-09-08",
                    "isDisputed": False,
                    "paragraphs": "396-398",
                    "exhibits": ["R-20"]
                }
            ],
            "evidence": [
                {
                    "id": "R-19",
                    "title": "Quarter-End Schedule and System Requirements",
                    "summary": "Documentation showing critical financial close processes scheduled for proposed audit dates requiring full system availability.",
                    "citations": ["392", "393"]
                },
                {
                    "id": "R-20",
                    "title": "Alternative Date Proposal",
                    "summary": "MegaCorp's correspondence offering multiple alternative audit dates in October and November 2023.",
                    "citations": ["396", "397"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "LCIA Ref. 145678",
                    "title": "Reasonable accommodation of audit rights",
                    "relevance": "Established that audit rights must be exercised reasonably with accommodation for licensee's legitimate business needs, and that offering reasonable alternatives satisfies cooperation obligations.",
                    "paragraphs": "402-406",
                    "citedParagraphs": ["403", "404"]
                }
            ]
        },
        "8": {
            "id": "8",
            "title": "Limitation of Liability Applies",
            "paragraphs": "411-435",
            "overview": {
                "points": [
                    "Limitation clause explicitly applies to all claims under agreement",
                    "No evidence of willful or fraudulent conduct",
                    "TechStart's attempt to avoid limitation is improper"
                ],
                "paragraphs": "411-413"
            },
            "factualPoints": [
                {
                    "point": "Contract Section 9.5 limits all damages to fees paid in prior 12 months",
                    "date": "2023-01-15",
                    "isDisputed": False,
                    "paragraphs": "417-419",
                    "exhibits": ["C-1"]
                },
                {
                    "point": "MegaCorp's conduct was based on good faith interpretation of territorial rights",
                    "date": "2023-09-15",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "420-423",
                    "exhibits": ["R-21"]
                }
            ],
            "evidence": [
                {
                    "id": "R-21",
                    "title": "Legal Analysis of Territorial Provisions",
                    "summary": "MegaCorp's internal legal memorandum showing good faith basis for interpreting territorial restrictions as advisory rather than mandatory.",
                    "citations": ["420", "421", "422"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 20456/2020",
                    "title": "Enforcement of limitation of liability clauses",
                    "relevance": "Confirmed that limitation clauses are strictly enforced absent clear proof of fraud or willful misconduct, and that disputed contract interpretation does not constitute willfulness.",
                    "paragraphs": "427-431",
                    "citedParagraphs": ["428", "429"]
                }
            ]
        },
        "9": {
            "id": "9",
            "title": "TechStart's SLA Breaches",
            "paragraphs": "436-460",
            "overview": {
                "points": [
                    "TechStart consistently failed to meet 99% uptime requirement",
                    "System failures were frequent and severe throughout contract",
                    "TechStart's monitoring data is unreliable and self-serving"
                ],
                "paragraphs": "436-438"
            },
            "factualPoints": [
                {
                    "point": "Independent monitoring shows actual uptime of 87% in Q3 2023",
                    "date": "2023-07-01 to 2023-09-30",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "442-445",
                    "exhibits": ["R-22", "R-23"]
                },
                {
                    "point": "TechStart's monitoring excluded planned maintenance in violation of SLA definition",
                    "date": "2023-01-15 to 2024-01-20",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "446-449",
                    "exhibits": ["R-24"]
                }
            ],
            "evidence": [
                {
                    "id": "R-22",
                    "title": "MegaCorp's Independent Monitoring Data",
                    "summary": "Comprehensive monitoring data from MegaCorp's independent systems showing actual uptime significantly below SLA requirements.",
                    "citations": ["442", "443"]
                },
                {
                    "id": "R-23",
                    "title": "Third-Party Monitoring Report",
                    "summary": "Report from independent monitoring service engaged by MegaCorp confirming poor system performance.",
                    "citations": ["444", "445"]
                },
                {
                    "id": "R-24",
                    "title": "SLA Calculation Methodology Analysis",
                    "summary": "Expert analysis showing TechStart's monitoring excluded downtime that should be counted under proper SLA calculation.",
                    "citations": ["446", "447", "448"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "SIAC ARB 091/2021",
                    "title": "SLA measurement and compliance verification",
                    "relevance": "Established that licensee's independent monitoring data is admissible to rebut licensor's self-reported compliance, and that unilateral exclusions from uptime calculations are improper.",
                    "paragraphs": "453-457",
                    "citedParagraphs": ["454", "455"]
                }
            ]
        },
        "10": {
            "id": "10",
            "title": "Necessary Transition Period Use",
            "paragraphs": "461-485",
            "overview": {
                "points": [
                    "Post-termination use was necessary to prevent business catastrophe",
                    "TechStart's improper termination created emergency situation",
                    "Industry standard allows reasonable transition period"
                ],
                "paragraphs": "461-463"
            },
            "factualPoints": [
                {
                    "point": "Immediate cessation would have shut down critical business operations affecting 50,000 customers",
                    "date": "2024-01-20",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "467-470",
                    "exhibits": ["R-25"]
                },
                {
                    "point": "MegaCorp completed migration within 70 days, standard industry timeframe",
                    "date": "2024-01-21 to 2024-03-31",
                    "isDisputed": False,
                    "paragraphs": "471-473",
                    "exhibits": ["R-26"]
                }
            ],
            "evidence": [
                {
                    "id": "R-25",
                    "title": "Business Impact Assessment",
                    "summary": "Analysis showing catastrophic business impact of immediate software cessation including customer service disruption.",
                    "citations": ["467", "468", "469"]
                },
                {
                    "id": "R-26",
                    "title": "Migration Timeline and Industry Standards",
                    "summary": "Documentation of migration project timeline and expert testimony on industry-standard transition periods for enterprise software.",
                    "citations": ["471", "472"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 21789/2021",
                    "title": "Reasonable transition period after termination",
                    "relevance": "Recognized implied right to reasonable transition period after contract termination to prevent disproportionate harm, particularly where termination itself is disputed.",
                    "paragraphs": "477-481",
                    "citedParagraphs": ["478", "479"]
                }
            ]
        },
        "5": {
            "id": "5",
            "title": "Confidentiality Breaches",
            "paragraphs": "146-170",
            "overview": {
                "points": [
                    "MegaCorp disclosed TechStart's confidential information to competitors",
                    "Breach of confidentiality obligations in Section 6",
                    "Unauthorized sharing of technical specifications and trade secrets"
                ],
                "paragraphs": "146-148"
            },
            "factualPoints": [
                {
                    "point": "MegaCorp shared proprietary API documentation with third-party developers",
                    "date": "2023-10-01 to 2023-11-15",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "152-155",
                    "exhibits": ["C-18", "C-19"]
                },
                {
                    "point": "Confidential information appeared in competitor's product launch materials",
                    "date": "2023-11-20",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "156-158",
                    "exhibits": ["C-20"]
                }
            ],
            "evidence": [
                {
                    "id": "C-18",
                    "title": "Email Communications with Third Parties",
                    "summary": "Email chain showing MegaCorp employees sharing TechStart's confidential API documentation with external developers in violation of confidentiality agreement.",
                    "citations": ["152", "153"]
                },
                {
                    "id": "C-19",
                    "title": "Access Log Analysis",
                    "summary": "System logs showing unauthorized downloads of confidential technical documentation by MegaCorp personnel.",
                    "citations": ["154", "155"]
                },
                {
                    "id": "C-20",
                    "title": "Competitor Product Materials",
                    "summary": "Marketing materials and technical specifications from competitor showing proprietary TechStart information.",
                    "citations": ["156", "157"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 22156/2020",
                    "title": "Breach of confidentiality in technology agreements",
                    "relevance": "Established that disclosure of confidential information to third parties constitutes material breach even if not directly to competitors, and that licensee bears strict liability for all disclosures by its employees.",
                    "paragraphs": "162-166",
                    "citedParagraphs": ["163", "164"]
                }
            ]
        },
        "6": {
            "id": "6",
            "title": "Indemnification Claims",
            "paragraphs": "171-195",
            "overview": {
                "points": [
                    "MegaCorp's breach triggered third-party IP claims against TechStart",
                    "Indemnification obligations under Section 8",
                    "MegaCorp must reimburse defense costs and settlements"
                ],
                "paragraphs": "171-173"
            },
            "factualPoints": [
                {
                    "point": "Third-party patent holder filed suit against TechStart for MegaCorp's unauthorized use",
                    "date": "2024-02-15",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "177-180",
                    "exhibits": ["C-21", "C-22"]
                },
                {
                    "point": "TechStart incurred $450,000 in legal fees defending third-party claims",
                    "date": "2024-02-15 to 2024-06-30",
                    "isDisputed": False,
                    "paragraphs": "181-183",
                    "exhibits": ["C-23"]
                }
            ],
            "evidence": [
                {
                    "id": "C-21",
                    "title": "Third-Party Patent Infringement Complaint",
                    "summary": "Complaint filed by patent holder alleging infringement based on MegaCorp's unauthorized territorial deployment of TechStart software.",
                    "citations": ["177", "178"]
                },
                {
                    "id": "C-22",
                    "title": "Indemnification Demand Letter",
                    "summary": "TechStart's formal demand to MegaCorp for indemnification under Section 8 of licensing agreement.",
                    "citations": ["179", "180"]
                },
                {
                    "id": "C-23",
                    "title": "Defense Cost Documentation",
                    "summary": "Invoices and billing statements from legal counsel defending third-party patent claims totaling $450,000.",
                    "citations": ["181", "182"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "LCIA Ref. 167890",
                    "title": "Indemnification obligations in licensing disputes",
                    "relevance": "Confirmed that licensees must indemnify licensors for third-party claims arising from licensee's breach of territorial or use restrictions, including all defense costs and settlements.",
                    "paragraphs": "186-190",
                    "citedParagraphs": ["187", "188"]
                }
            ]
        },
        "7": {
            "id": "7",
            "title": "Audit Rights and Compliance Verification",
            "paragraphs": "196-220",
            "overview": {
                "points": [
                    "MegaCorp refused TechStart's contractual audit rights",
                    "Obstruction of compliance verification under Section 5.4",
                    "Failure to provide required usage reports and documentation"
                ],
                "paragraphs": "196-198"
            },
            "factualPoints": [
                {
                    "point": "MegaCorp denied access for scheduled audit in September 2023",
                    "date": "2023-09-05",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "202-205",
                    "exhibits": ["C-24", "C-25"]
                },
                {
                    "point": "No usage reports submitted for Q3 or Q4 2023 as required",
                    "date": "2023-07-01 to 2023-12-31",
                    "isDisputed": False,
                    "paragraphs": "206-208",
                    "exhibits": ["C-26"]
                }
            ],
            "evidence": [
                {
                    "id": "C-24",
                    "title": "Audit Request and Scheduling Correspondence",
                    "summary": "Email correspondence showing TechStart's proper notice for contractual audit and MegaCorp's refusal to provide access.",
                    "citations": ["202", "203"]
                },
                {
                    "id": "C-25",
                    "title": "Audit Rights Provision Analysis",
                    "summary": "Contract excerpt and legal analysis of Section 5.4 audit rights and MegaCorp's obligations to provide access.",
                    "citations": ["204", "205"]
                },
                {
                    "id": "C-26",
                    "title": "Usage Report Requirements and Compliance Record",
                    "summary": "Documentation showing required reporting schedule and MegaCorp's failure to submit usage reports for two consecutive quarters.",
                    "citations": ["206", "207"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 20987/2019",
                    "title": "Audit rights in software licensing agreements",
                    "relevance": "Established that refusal to permit contractual audits constitutes material breach and creates presumption of non-compliance with licensing terms.",
                    "paragraphs": "212-216",
                    "citedParagraphs": ["213", "214"]
                }
            ]
        },
        "8": {
            "id": "8",
            "title": "Limitation of Liability Disputes",
            "paragraphs": "221-245",
            "overview": {
                "points": [
                    "Liability cap does not apply to MegaCorp's willful breaches",
                    "Exception for breach of confidentiality and IP provisions",
                    "MegaCorp's conduct falls outside limitation protections"
                ],
                "paragraphs": "221-223"
            },
            "factualPoints": [
                {
                    "point": "MegaCorp's territorial violations were knowing and willful, not negligent",
                    "date": "2023-09-15 to present",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "227-230",
                    "exhibits": ["C-27"]
                },
                {
                    "point": "Internal emails show MegaCorp executives approved European deployment despite restrictions",
                    "date": "2023-09-10",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "231-234",
                    "exhibits": ["C-28"]
                }
            ],
            "evidence": [
                {
                    "id": "C-27",
                    "title": "Willful Breach Analysis",
                    "summary": "Legal memorandum establishing that MegaCorp's conduct constituted willful and knowing breach beyond scope of limitation clause.",
                    "citations": ["227", "228"]
                },
                {
                    "id": "C-28",
                    "title": "Executive Email Communications",
                    "summary": "Internal MegaCorp emails showing senior management's knowledge of territorial restrictions and decision to violate them.",
                    "citations": ["231", "232", "233"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "SIAC ARB 078/2020",
                    "title": "Limitation of liability for willful breaches",
                    "relevance": "Confirmed that limitation of liability clauses do not protect against willful or knowing breaches, and that knowledge of breach by senior management establishes willfulness.",
                    "paragraphs": "238-242",
                    "citedParagraphs": ["239", "240"]
                }
            ]
        },
        "9": {
            "id": "9",
            "title": "Service Level Agreement Enforcement",
            "paragraphs": "246-270",
            "overview": {
                "points": [
                    "TechStart met all SLA requirements throughout contract period",
                    "Performance issues resulted from MegaCorp's infrastructure problems",
                    "MegaCorp's SLA claims are pretextual"
                ],
                "paragraphs": "246-248"
            },
            "factualPoints": [
                {
                    "point": "TechStart's monitoring data shows 99.7% uptime throughout contract period",
                    "date": "2023-01-15 to 2024-01-20",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "252-255",
                    "exhibits": ["C-29", "C-30"]
                },
                {
                    "point": "Performance issues traced to MegaCorp's inadequate server infrastructure",
                    "date": "2023-06-15 to 2023-09-30",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "256-259",
                    "exhibits": ["C-31"]
                }
            ],
            "evidence": [
                {
                    "id": "C-29",
                    "title": "TechStart System Monitoring Reports",
                    "summary": "Comprehensive monitoring data from TechStart's systems showing consistent 99.7% uptime and compliance with all SLA metrics.",
                    "citations": ["252", "253"]
                },
                {
                    "id": "C-30",
                    "title": "Independent Third-Party Audit",
                    "summary": "Independent audit report confirming TechStart's SLA compliance throughout contract period.",
                    "citations": ["254", "255"]
                },
                {
                    "id": "C-31",
                    "title": "Root Cause Analysis Report",
                    "summary": "Technical analysis identifying MegaCorp's inadequate infrastructure as cause of performance issues, not TechStart's software.",
                    "citations": ["256", "257", "258"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 21567/2021",
                    "title": "SLA compliance and burden of proof",
                    "relevance": "Established that licensor's contemporaneous monitoring data creates presumption of SLA compliance, and licensee bears burden to prove non-compliance with clear evidence.",
                    "paragraphs": "263-267",
                    "citedParagraphs": ["264", "265"]
                }
            ]
        },
        "10": {
            "id": "10",
            "title": "Post-Termination Obligations",
            "paragraphs": "271-295",
            "overview": {
                "points": [
                    "MegaCorp continues to use TechStart software after termination",
                    "Failure to return or destroy confidential information",
                    "Breach of post-termination obligations in Section 10"
                ],
                "paragraphs": "271-273"
            },
            "factualPoints": [
                {
                    "point": "MegaCorp's systems show continued API calls to TechStart software after termination",
                    "date": "2024-01-21 to 2024-03-31",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "277-280",
                    "exhibits": ["C-32"]
                },
                {
                    "point": "MegaCorp failed to certify destruction of confidential materials as required",
                    "date": "2024-02-20",
                    "isDisputed": False,
                    "paragraphs": "281-283",
                    "exhibits": ["C-33"]
                }
            ],
            "evidence": [
                {
                    "id": "C-32",
                    "title": "Post-Termination Usage Logs",
                    "summary": "Server logs showing continued API calls from MegaCorp systems for 70 days after termination date.",
                    "citations": ["277", "278", "279"]
                },
                {
                    "id": "C-33",
                    "title": "Post-Termination Compliance Demand",
                    "summary": "TechStart's demand for certification of data destruction per Section 10.3 and MegaCorp's failure to respond.",
                    "citations": ["281", "282"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "LCIA Ref. 178901",
                    "title": "Post-termination use of licensed software",
                    "relevance": "Established that continued use of software after termination constitutes conversion and unauthorized use, subject to damages calculated at 3x normal licensing fees.",
                    "paragraphs": "287-291",
                    "citedParagraphs": ["288", "289"]
                }
            ]
        },
        "3": {
            "id": "3",
            "title": "Damages and Financial Losses",
            "paragraphs": "96-120",
            "overview": {
                "points": [
                    "Unpaid license fees totaling $5.3M",
                    "Lost profits from territorial violations estimated at $8.2M",
                    "Costs of investigating and pursuing IP misappropriation"
                ],
                "paragraphs": "96-98"
            },
            "factualPoints": [
                {
                    "point": "TechStart incurred $750,000 in forensic investigation costs",
                    "date": "2023-12-01 to 2024-02-28",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "102-104",
                    "exhibits": ["C-11", "C-12"]
                },
                {
                    "point": "Projected revenue loss from European market entry amounts to $8.2M",
                    "date": "2023-09-15 to 2025-12-31",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "105-108",
                    "exhibits": ["C-13"]
                }
            ],
            "evidence": [
                {
                    "id": "C-11",
                    "title": "Forensic Investigation Invoices",
                    "summary": "Invoices and payment records from cybersecurity firms engaged to investigate unauthorized software deployments and code analysis, totaling $750,000.",
                    "citations": ["102", "103"]
                },
                {
                    "id": "C-12",
                    "title": "Legal Fees and Costs Schedule",
                    "summary": "Detailed breakdown of legal costs incurred in investigating breaches, preparing arbitration claims, and expert witness fees.",
                    "citations": ["104"]
                },
                {
                    "id": "C-13",
                    "title": "Market Analysis and Revenue Projections",
                    "summary": "Expert economic analysis of European market opportunity and projected revenue losses due to MegaCorp's unauthorized territorial expansion.",
                    "citations": ["105", "106", "107"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 18234/2018",
                    "title": "Calculation of damages in software licensing disputes",
                    "relevance": "Established methodology for calculating lost profits in territorial breach cases, including market analysis, projected growth rates, and reasonable profit margins.",
                    "paragraphs": "110-114",
                    "citedParagraphs": ["111", "112"]
                }
            ],
            "children": {
                "3.1": {
                    "id": "3.1",
                    "title": "Unpaid License Fees",
                    "paragraphs": "115-125",
                    "overview": {
                        "points": [
                            "Q3 2023 payment: $2.5M outstanding",
                            "Q4 2023 payment: $1.7M outstanding (after partial payment)",
                            "Q1 2024 payment: $1.1M outstanding"
                        ],
                        "paragraphs": "115-117"
                    },
                    "factualPoints": [
                        {
                            "point": "Total unpaid license fees amount to $5.3M as of March 2024",
                            "date": "2023-07-01 to 2024-03-31",
                            "isDisputed": False,
                            "paragraphs": "118-120",
                            "exhibits": ["C-3", "C-14"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "C-14",
                            "title": "Comprehensive Payment Ledger",
                            "summary": "Complete accounting ledger showing all invoiced amounts, payments received, and outstanding balances for the entire contract period.",
                            "citations": ["118", "119"]
                        }
                    ]
                }
            }
        },
        "4": {
            "id": "4",
            "title": "Wrongful Termination of Agreement",
            "paragraphs": "126-145",
            "overview": {
                "points": [
                    "TechStart properly terminated agreement after material breach",
                    "Required notice periods were observed",
                    "MegaCorp's cure period expired without remedy"
                ],
                "paragraphs": "126-128"
            },
            "factualPoints": [
                {
                    "point": "30-day cure notice sent December 15, 2023, expired January 14, 2024",
                    "date": "2023-12-15 to 2024-01-14",
                    "isDisputed": False,
                    "paragraphs": "130-132",
                    "exhibits": ["C-15", "C-16"]
                },
                {
                    "point": "Formal termination effective January 20, 2024",
                    "date": "2024-01-20",
                    "isDisputed": True,
                    "source": "Respondent",
                    "paragraphs": "133-135",
                    "exhibits": ["C-17"]
                }
            ],
            "evidence": [
                {
                    "id": "C-15",
                    "title": "Notice of Default and Opportunity to Cure",
                    "summary": "Official notice sent to MegaCorp on December 15, 2023, outlining all breaches and providing 30-day cure period as required by contract Section 9.2.",
                    "citations": ["130", "131"]
                },
                {
                    "id": "C-16",
                    "title": "Delivery Confirmation and Read Receipts",
                    "summary": "Email delivery confirmations and read receipts proving MegaCorp received and opened the cure notice.",
                    "citations": ["132"]
                },
                {
                    "id": "C-17",
                    "title": "Termination Letter",
                    "summary": "Formal termination notice dated January 20, 2024, terminating the licensing agreement for material uncured breaches.",
                    "citations": ["133", "134"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "LCIA Ref. 145622",
                    "title": "Termination procedures in commercial contracts",
                    "relevance": "Confirmed that strict compliance with contractual termination procedures is required, including proper notice and reasonable cure periods, but that non-material procedural defects do not invalidate otherwise proper termination.",
                    "paragraphs": "138-142",
                    "citedParagraphs": ["139", "140"]
                }
            ]
        }
    }
    
    respondent_args = {
        "1": {
            "id": "1",
            "title": "No Material Breach - Payment Disputes",
            "paragraphs": "200-225",
            "overview": {
                "points": [
                    "Payments withheld due to software performance issues",
                    "Valid invocation of dispute resolution under Section 8.4",
                    "TechStart's failure to remedy defects justified payment suspension"
                ],
                "paragraphs": "200-202"
            },
            "factualPoints": [
                {
                    "point": "Software experienced critical performance failures affecting MegaCorp's operations",
                    "date": "2023-06-15 to 2023-09-30",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "206-209",
                    "exhibits": ["R-1", "R-2"]
                }
            ],
            "evidence": [
                {
                    "id": "R-1",
                    "title": "System Performance Reports",
                    "summary": "Detailed technical reports documenting software failures, including system downtime logs, error messages, and impact assessments showing significant business disruption caused by TechStart's software performance issues.",
                    "citations": ["206", "207", "208"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 19876/2020",
                    "title": "Suspension of payment for non-conforming performance",
                    "relevance": "Confirmed that parties may suspend payment obligations when the counterparty fails to deliver conforming performance, provided proper notice is given and cure period allowed. Material non-performance excuses payment obligations until remedy.",
                    "paragraphs": "210-213",
                    "citedParagraphs": ["211", "212"]
                }
            ],
            "children": {
                "1.1": {
                    "id": "1.1",
                    "title": "Software Performance Defects",
                    "paragraphs": "220-240",
                    "overview": {
                        "points": [
                            "Critical system failures impacting business operations",
                            "TechStart's inadequate technical support response",
                            "Failure to meet SLA requirements in Section 3.2"
                        ],
                        "paragraphs": "220-222"
                    },
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Documented System Failures",
                            "paragraphs": "230-235",
                            "factualPoints": [
                                {
                                    "point": "System downtime exceeded 15% in Q3 2023, violating 99% uptime SLA",
                                    "date": "2023-07-01 to 2023-09-30",
                                    "isDisputed": False,
                                    "paragraphs": "230-231",
                                    "exhibits": ["R-3"]
                                },
                                {
                                    "point": "Critical data processing errors resulted in $1.2M in business losses",
                                    "date": "2023-08-15 to 2023-08-30",
                                    "isDisputed": True,
                                    "source": "Claimant",
                                    "paragraphs": "232-234",
                                    "exhibits": ["R-4"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "R-3",
                                    "title": "SLA Compliance Reports",
                                    "summary": "Comprehensive service level agreement monitoring reports showing actual vs. contracted performance metrics, including uptime statistics, response times, and resolution timeframes for technical issues.",
                                    "citations": ["230", "231"]
                                }
                            ]
                        }
                    }
                }
            }
        },
        "2": {
            "id": "2",
            "title": "Legitimate IP Development",
            "paragraphs": "250-275",
            "overview": {
                "points": [
                    "Independent development of proprietary technology",
                    "No use of TechStart's confidential information",
                    "Legitimate competitive product development"
                ],
                "paragraphs": "250-252"
            },
            "factualPoints": [
                {
                    "point": "MegaCorp's development team created algorithms independently using clean-room methodology",
                    "date": "2023-01-01 to 2023-10-31",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "258-262",
                    "exhibits": ["R-7"]
                }
            ],
            "evidence": [
                {
                    "id": "R-7",
                    "title": "Development Documentation and Clean-Room Procedures",
                    "summary": "Complete development documentation including design specifications, coding standards, and clean-room procedures implemented to ensure independent development without reference to TechStart's proprietary technology.",
                    "citations": ["258", "259", "260"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "SIAC ARB 045/2021",
                    "title": "Independent development vs. misappropriation",
                    "relevance": "Distinguished between legitimate independent development and misappropriation, establishing that licensees retain the right to develop competing products using their own resources and expertise, provided they do not use confidential information from the licensed technology.",
                    "paragraphs": "265-268",
                    "citedParagraphs": ["266", "267"]
                }
            ]
        },
        "3": {
            "id": "3",
            "title": "MegaCorp's Counterclaim for Damages",
            "paragraphs": "276-310",
            "overview": {
                "points": [
                    "TechStart's software defects caused $3.5M in business losses",
                    "Breach of warranty and service level commitments",
                    "Improper termination caused additional $2M in damages"
                ],
                "paragraphs": "276-278"
            },
            "factualPoints": [
                {
                    "point": "Business disruption from software failures resulted in lost revenue of $3.5M",
                    "date": "2023-06-15 to 2023-12-31",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "282-286",
                    "exhibits": ["R-8", "R-9"]
                },
                {
                    "point": "Emergency migration to alternative platform cost $2M",
                    "date": "2024-01-20 to 2024-04-30",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "287-290",
                    "exhibits": ["R-10"]
                }
            ],
            "evidence": [
                {
                    "id": "R-8",
                    "title": "Financial Impact Analysis",
                    "summary": "Detailed financial analysis prepared by MegaCorp's CFO documenting lost revenue, operational costs, and business interruption damages directly attributable to software performance issues.",
                    "citations": ["282", "283", "284"]
                },
                {
                    "id": "R-9",
                    "title": "Customer Complaint Records",
                    "summary": "Documentation of customer complaints, service disruptions, and contract cancellations resulting from system failures during the relevant period.",
                    "citations": ["285", "286"]
                },
                {
                    "id": "R-10",
                    "title": "Migration Project Costs",
                    "summary": "Complete accounting of costs incurred to migrate to alternative software platform following TechStart's termination, including software licenses, implementation costs, and consulting fees.",
                    "citations": ["287", "288", "289"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "ICC Case No. 20145/2019",
                    "title": "Consequential damages in software contracts",
                    "relevance": "Established framework for calculating consequential damages in software disputes, including lost profits, business interruption, and migration costs, provided such damages were foreseeable at contract formation.",
                    "paragraphs": "295-299",
                    "citedParagraphs": ["296", "297"]
                }
            ],
            "children": {
                "3.1": {
                    "id": "3.1",
                    "title": "Warranty Breach Claims",
                    "paragraphs": "300-310",
                    "overview": {
                        "points": [
                            "Software failed to perform as warranted in Section 3.1",
                            "TechStart breached fitness for purpose warranty",
                            "Inadequate support violated maintenance obligations"
                        ],
                        "paragraphs": "300-302"
                    },
                    "factualPoints": [
                        {
                            "point": "Software never achieved warranted 99% uptime throughout contract period",
                            "date": "2023-01-15 to 2024-01-20",
                            "isDisputed": True,
                            "source": "Claimant",
                            "paragraphs": "304-307",
                            "exhibits": ["R-3", "R-11"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "R-11",
                            "title": "Complete Performance Monitoring Data",
                            "summary": "Year-long performance monitoring data showing consistent failure to meet warranted uptime, response time, and processing capacity specifications.",
                            "citations": ["304", "305", "306"]
                        }
                    ]
                }
            }
        },
        "4": {
            "id": "4",
            "title": "Invalid Termination",
            "paragraphs": "311-335",
            "overview": {
                "points": [
                    "TechStart's own material breaches invalidated termination right",
                    "Cure notice was defective and improper",
                    "Termination was premature and in bad faith"
                ],
                "paragraphs": "311-313"
            },
            "factualPoints": [
                {
                    "point": "TechStart was in material breach of SLA obligations when it attempted termination",
                    "date": "2023-06-15 to 2024-01-20",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "317-320",
                    "exhibits": ["R-3", "R-12"]
                },
                {
                    "point": "Cure notice failed to specify breaches with required particularity",
                    "date": "2023-12-15",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "321-324",
                    "exhibits": ["R-12"]
                }
            ],
            "evidence": [
                {
                    "id": "R-12",
                    "title": "Legal Analysis of Cure Notice",
                    "summary": "Legal memorandum analyzing deficiencies in TechStart's cure notice, including lack of specificity and failure to acknowledge TechStart's own breaches.",
                    "citations": ["321", "322", "323"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "LCIA Ref. 134567",
                    "title": "Clean hands doctrine in contract termination",
                    "relevance": "Established that a party in material breach of its own obligations cannot terminate the contract for the other party's breaches, applying the clean hands doctrine to commercial arbitration.",
                    "paragraphs": "327-331",
                    "citedParagraphs": ["328", "329"]
                }
            ]
        }
    }
    
    topics = [
        {
            "id": "topic-1",
            "title": "Contract Performance and Payment Disputes",
            "description": "Questions of material breach, payment obligations, and excuse for non-performance",
            "argumentIds": ["1"]
        },
        {
            "id": "topic-2", 
            "title": "Intellectual Property Rights and Development",
            "description": "Disputes over IP ownership, derivative works, and competitive product development",
            "argumentIds": ["2"]
        },
        {
            "id": "topic-3",
            "title": "Damages and Financial Claims",
            "description": "Calculation of damages, lost profits, and financial consequences of alleged breaches",
            "argumentIds": ["3"]
        },
        {
            "id": "topic-4",
            "title": "Contract Termination",
            "description": "Validity of contract termination, cure procedures, and termination consequences",
            "argumentIds": ["4"]
        },
        {
            "id": "topic-5",
            "title": "Confidentiality and Data Protection",
            "description": "Breach of confidentiality obligations and unauthorized disclosure of proprietary information",
            "argumentIds": ["5"]
        },
        {
            "id": "topic-6",
            "title": "Indemnification and Third-Party Claims",
            "description": "Obligations to indemnify for third-party claims and allocation of defense costs",
            "argumentIds": ["6"]
        },
        {
            "id": "topic-7",
            "title": "Audit Rights and Compliance Verification",
            "description": "Exercise of contractual audit rights and compliance with reporting obligations",
            "argumentIds": ["7"]
        },
        {
            "id": "topic-8",
            "title": "Limitation of Liability",
            "description": "Application and scope of contractual limitation of liability provisions",
            "argumentIds": ["8"]
        },
        {
            "id": "topic-9",
            "title": "Service Level Agreement Compliance",
            "description": "Disputes over SLA performance metrics and compliance measurement",
            "argumentIds": ["9"]
        },
        {
            "id": "topic-10",
            "title": "Post-Termination Obligations",
            "description": "Continuing obligations after contract termination and transition requirements",
            "argumentIds": ["10"]
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
            "claimantVersion": "Software licensing agreement executed between TechStart and MegaCorp",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-06-15",
            "claimantVersion": "MegaCorp began experiencing minor software performance issues",
            "respondentVersion": "Critical system failures began affecting business operations",
            "status": "Disputed"
        },
        {
            "date": "2023-07-01",
            "claimantVersion": "Q3 license payment of $2.5M due but not received",
            "respondentVersion": "Payment withheld due to ongoing software performance issues",
            "status": "Disputed"
        },
        {
            "date": "2023-08-15",
            "claimantVersion": "TechStart provided software updates to address performance concerns",
            "respondentVersion": "System failures resulted in $1.2M business losses despite 'updates'",
            "status": "Disputed"
        },
        {
            "date": "2023-09-15",
            "claimantVersion": "Discovered unauthorized deployment in European territories",
            "respondentVersion": "Deployed software globally as business necessity due to system reliability issues",
            "status": "Disputed"
        },
        {
            "date": "2023-10-01",
            "claimantVersion": "Q4 license payment of $2.8M due - only partial payment received",
            "respondentVersion": "Made partial payment pending resolution of performance issues",
            "status": "Undisputed"
        },
        {
            "date": "2023-11-01",
            "claimantVersion": "MegaCorp began developing competing software using TechStart's algorithms",
            "respondentVersion": "Commenced independent development of alternative solution using clean-room methodology",
            "status": "Disputed"
        },
        {
            "date": "2023-12-15",
            "claimantVersion": "Formal notice of breach sent to MegaCorp",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2024-01-20",
            "claimantVersion": "TechStart terminated licensing agreement for material breach",
            "respondentVersion": "Disputed termination as invalid due to TechStart's prior material breaches",
            "status": "Disputed"
        },
        {
            "date": "2024-03-01",
            "claimantVersion": "Arbitration proceedings initiated under ICC Rules",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2024-03-15",
            "claimantVersion": "TechStart filed Statement of Claim seeking $13.5M in damages",
            "respondentVersion": "Received excessive and unsubstantiated damage claims",
            "status": "Disputed"
        },
        {
            "date": "2024-04-30",
            "claimantVersion": "—",
            "respondentVersion": "MegaCorp completed emergency migration to alternative platform at cost of $2M",
            "status": "Disputed"
        },
        {
            "date": "2024-05-15",
            "claimantVersion": "—",
            "respondentVersion": "MegaCorp filed Statement of Defense and Counterclaim seeking $5.5M",
            "status": "Disputed"
        },
        {
            "date": "2024-06-01",
            "claimantVersion": "Tribunal constituted with three arbitrators",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2024-07-20",
            "claimantVersion": "Document production phase completed",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2024-09-10",
            "claimantVersion": "Expert reports on damages and technical issues exchanged",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2023-10-01",
            "claimantVersion": "Discovered MegaCorp sharing confidential API documentation with third parties",
            "respondentVersion": "Shared only publicly available information with authorized partners",
            "status": "Disputed"
        },
        {
            "date": "2023-11-20",
            "claimantVersion": "TechStart's confidential information appeared in competitor's product materials",
            "respondentVersion": "Information was independently developed and publicly known",
            "status": "Disputed"
        },
        {
            "date": "2024-02-15",
            "claimantVersion": "—",
            "respondentVersion": "Third-party patent holder filed suit against TechStart for MegaCorp's use",
            "status": "Disputed"
        },
        {
            "date": "2024-03-10",
            "claimantVersion": "—",
            "respondentVersion": "TechStart refused MegaCorp's indemnification demand for patent defense",
            "status": "Undisputed"
        },
        {
            "date": "2023-09-05",
            "claimantVersion": "MegaCorp denied access for scheduled contractual audit",
            "respondentVersion": "Requested reasonable postponement due to quarter-end financial close",
            "status": "Disputed"
        },
        {
            "date": "2023-09-08",
            "claimantVersion": "—",
            "respondentVersion": "MegaCorp offered alternative audit dates in October, declined by TechStart",
            "status": "Undisputed"
        },
        {
            "date": "2023-09-10",
            "claimantVersion": "Internal MegaCorp emails show executives approved European deployment despite restrictions",
            "respondentVersion": "Management made good faith interpretation of ambiguous territorial provisions",
            "status": "Disputed"
        },
        {
            "date": "2024-01-21",
            "claimantVersion": "MegaCorp continued using TechStart software after termination without authorization",
            "respondentVersion": "Necessary transition period to prevent catastrophic business disruption",
            "status": "Disputed"
        },
        {
            "date": "2024-02-20",
            "claimantVersion": "MegaCorp failed to certify destruction of confidential materials as required",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        {
            "date": "2024-03-31",
            "claimantVersion": "MegaCorp finally ceased using TechStart software after 70 days of unauthorized use",
            "respondentVersion": "Completed migration within industry-standard 70-day transition period",
            "status": "Disputed"
        }
    ]

def get_exhibits_data():
    return [
        {
            "id": "C-1",
            "party": "Claimant",
            "title": "Software Licensing Agreement",
            "type": "contract",
            "summary": "Master licensing agreement executed January 15, 2023, between TechStart Inc. and MegaCorp Ltd."
        },
        {
            "id": "C-2",
            "party": "Claimant", 
            "title": "Payment Demand Letters",
            "type": "correspondence",
            "summary": "Series of payment demand letters sent to MegaCorp for overdue Q3 and Q4 2023 license fees"
        },
        {
            "id": "C-3",
            "party": "Claimant",
            "title": "Banking Records and Payment Schedule",
            "type": "financial",
            "summary": "TechStart's banking records and contractual payment schedule showing payment defaults"
        },
        {
            "id": "C-4",
            "party": "Claimant",
            "title": "Partial Payment Confirmation",
            "type": "financial",
            "summary": "Wire transfer confirmation for partial Q4 2023 payment of $1.1M received from MegaCorp"
        },
        {
            "id": "C-7",
            "party": "Claimant",
            "title": "Server Access Logs",
            "type": "technical",
            "summary": "Comprehensive server logs showing API calls from European IP addresses proving territorial violations"
        },
        {
            "id": "C-9",
            "party": "Claimant",
            "title": "Code Analysis Expert Report",
            "type": "expert",
            "summary": "Technical expert analysis comparing TechStart's algorithms with MegaCorp's competing software"
        },
        {
            "id": "R-1",
            "party": "Respondent",
            "title": "System Performance Reports",
            "type": "technical",
            "summary": "Detailed technical reports documenting software failures and business impact from June-September 2023"
        },
        {
            "id": "R-2",
            "party": "Respondent",
            "title": "SLA Breach Documentation",
            "type": "technical",
            "summary": "Evidence of TechStart's failure to meet 99% uptime service level agreement requirements"
        },
        {
            "id": "R-3",
            "party": "Respondent",
            "title": "SLA Compliance Reports",
            "type": "technical",
            "summary": "Quarterly SLA monitoring reports showing actual vs. contracted performance metrics"
        },
        {
            "id": "R-4",
            "party": "Respondent",
            "title": "Business Loss Documentation",
            "type": "financial",
            "summary": "Financial impact assessment of $1.2M in losses caused by software failures in August 2023"
        },
        {
            "id": "R-7",
            "party": "Respondent",
            "title": "Clean-Room Development Documentation",
            "type": "technical",
            "summary": "Complete development records proving independent creation of competing software using clean-room methodology"
        },
        {
            "id": "C-11",
            "party": "Claimant",
            "title": "Forensic Investigation Invoices",
            "type": "financial",
            "summary": "Invoices from cybersecurity firms for investigating unauthorized deployments totaling $750,000"
        },
        {
            "id": "C-12",
            "party": "Claimant",
            "title": "Legal Fees and Costs Schedule",
            "type": "financial",
            "summary": "Breakdown of legal costs for investigating breaches and preparing arbitration claims"
        },
        {
            "id": "C-13",
            "party": "Claimant",
            "title": "Market Analysis and Revenue Projections",
            "type": "expert",
            "summary": "Expert economic analysis of European market and $8.2M projected revenue losses"
        },
        {
            "id": "C-14",
            "party": "Claimant",
            "title": "Comprehensive Payment Ledger",
            "type": "financial",
            "summary": "Complete accounting showing all invoices, payments, and $5.3M outstanding balance"
        },
        {
            "id": "C-15",
            "party": "Claimant",
            "title": "Notice of Default and Opportunity to Cure",
            "type": "correspondence",
            "summary": "Official notice sent December 15, 2023 providing 30-day cure period per contract Section 9.2"
        },
        {
            "id": "C-16",
            "party": "Claimant",
            "title": "Delivery Confirmation and Read Receipts",
            "type": "correspondence",
            "summary": "Email confirmations proving MegaCorp received and opened the cure notice"
        },
        {
            "id": "C-17",
            "party": "Claimant",
            "title": "Termination Letter",
            "type": "correspondence",
            "summary": "Formal termination notice dated January 20, 2024 for material uncured breaches"
        },
        {
            "id": "R-8",
            "party": "Respondent",
            "title": "Financial Impact Analysis",
            "type": "financial",
            "summary": "CFO analysis documenting $3.5M in lost revenue from software performance issues"
        },
        {
            "id": "R-9",
            "party": "Respondent",
            "title": "Customer Complaint Records",
            "type": "correspondence",
            "summary": "Documentation of customer complaints and contract cancellations from system failures"
        },
        {
            "id": "R-10",
            "party": "Respondent",
            "title": "Migration Project Costs",
            "type": "financial",
            "summary": "Complete accounting of $2M costs to migrate to alternative software platform"
        },
        {
            "id": "R-11",
            "party": "Respondent",
            "title": "Complete Performance Monitoring Data",
            "type": "technical",
            "summary": "Year-long data showing consistent failure to meet warranted uptime specifications"
        },
        {
            "id": "R-12",
            "party": "Respondent",
            "title": "Legal Analysis of Cure Notice",
            "type": "expert",
            "summary": "Legal memorandum analyzing deficiencies in TechStart's cure notice"
        },
        {
            "id": "C-18",
            "party": "Claimant",
            "title": "Email Communications with Third Parties",
            "type": "correspondence",
            "summary": "Email chain showing MegaCorp sharing confidential API documentation with external developers"
        },
        {
            "id": "C-19",
            "party": "Claimant",
            "title": "Access Log Analysis",
            "type": "technical",
            "summary": "System logs showing unauthorized downloads of confidential documentation by MegaCorp"
        },
        {
            "id": "C-20",
            "party": "Claimant",
            "title": "Competitor Product Materials",
            "type": "technical",
            "summary": "Marketing materials from competitor showing proprietary TechStart information"
        },
        {
            "id": "C-21",
            "party": "Claimant",
            "title": "Third-Party Patent Infringement Complaint",
            "type": "correspondence",
            "summary": "Complaint alleging infringement based on MegaCorp's unauthorized territorial deployment"
        },
        {
            "id": "C-22",
            "party": "Claimant",
            "title": "Indemnification Demand Letter",
            "type": "correspondence",
            "summary": "TechStart's formal indemnification demand to MegaCorp under Section 8"
        },
        {
            "id": "C-23",
            "party": "Claimant",
            "title": "Defense Cost Documentation",
            "type": "financial",
            "summary": "Legal invoices for defending third-party patent claims totaling $450,000"
        },
        {
            "id": "C-24",
            "party": "Claimant",
            "title": "Audit Request and Scheduling Correspondence",
            "type": "correspondence",
            "summary": "Email correspondence showing proper audit notice and MegaCorp's refusal"
        },
        {
            "id": "C-25",
            "party": "Claimant",
            "title": "Audit Rights Provision Analysis",
            "type": "contract",
            "summary": "Contract excerpt and legal analysis of Section 5.4 audit rights"
        },
        {
            "id": "C-26",
            "party": "Claimant",
            "title": "Usage Report Requirements and Compliance Record",
            "type": "technical",
            "summary": "Documentation showing MegaCorp failed to submit usage reports for two quarters"
        },
        {
            "id": "C-27",
            "party": "Claimant",
            "title": "Willful Breach Analysis",
            "type": "expert",
            "summary": "Legal memorandum establishing MegaCorp's willful and knowing breach"
        },
        {
            "id": "C-28",
            "party": "Claimant",
            "title": "Executive Email Communications",
            "type": "correspondence",
            "summary": "Internal MegaCorp emails showing management knew of and violated territorial restrictions"
        },
        {
            "id": "C-29",
            "party": "Claimant",
            "title": "TechStart System Monitoring Reports",
            "type": "technical",
            "summary": "Monitoring data showing consistent 99.7% uptime and SLA compliance"
        },
        {
            "id": "C-30",
            "party": "Claimant",
            "title": "Independent Third-Party Audit",
            "type": "expert",
            "summary": "Independent audit confirming TechStart's SLA compliance throughout contract"
        },
        {
            "id": "C-31",
            "party": "Claimant",
            "title": "Root Cause Analysis Report",
            "type": "technical",
            "summary": "Technical analysis identifying MegaCorp's infrastructure as cause of performance issues"
        },
        {
            "id": "C-32",
            "party": "Claimant",
            "title": "Post-Termination Usage Logs",
            "type": "technical",
            "summary": "Server logs showing continued API calls from MegaCorp for 70 days after termination"
        },
        {
            "id": "C-33",
            "party": "Claimant",
            "title": "Post-Termination Compliance Demand",
            "type": "correspondence",
            "summary": "TechStart's demand for data destruction certification and MegaCorp's failure to respond"
        },
        {
            "id": "R-13",
            "party": "Respondent",
            "title": "Public TechStart Documentation",
            "type": "technical",
            "summary": "Screenshots of TechStart's publicly available documentation containing alleged confidential information"
        },
        {
            "id": "R-14",
            "party": "Respondent",
            "title": "Industry Standard Practices Analysis",
            "type": "expert",
            "summary": "Expert report showing alleged confidential methods are standard industry practices"
        },
        {
            "id": "R-15",
            "party": "Respondent",
            "title": "Prior Development Records",
            "type": "technical",
            "summary": "MegaCorp's internal development documentation predating licensing agreement"
        },
        {
            "id": "R-16",
            "party": "Respondent",
            "title": "Patent Claim Technical Analysis",
            "type": "expert",
            "summary": "Expert analysis showing patent claims target TechStart's core algorithms"
        },
        {
            "id": "R-17",
            "party": "Respondent",
            "title": "MegaCorp Indemnification Demand",
            "type": "correspondence",
            "summary": "MegaCorp's formal indemnification demand to TechStart under Section 8.1"
        },
        {
            "id": "R-18",
            "party": "Respondent",
            "title": "TechStart's Refusal to Defend",
            "type": "correspondence",
            "summary": "TechStart's response refusing to defend or indemnify MegaCorp"
        },
        {
            "id": "R-19",
            "party": "Respondent",
            "title": "Quarter-End Schedule and System Requirements",
            "type": "financial",
            "summary": "Documentation showing critical financial close processes during proposed audit dates"
        },
        {
            "id": "R-20",
            "party": "Respondent",
            "title": "Alternative Date Proposal",
            "type": "correspondence",
            "summary": "MegaCorp's correspondence offering multiple alternative audit dates"
        },
        {
            "id": "R-21",
            "party": "Respondent",
            "title": "Legal Analysis of Territorial Provisions",
            "type": "expert",
            "summary": "Internal legal memorandum showing good faith basis for territorial interpretation"
        },
        {
            "id": "R-22",
            "party": "Respondent",
            "title": "MegaCorp's Independent Monitoring Data",
            "type": "technical",
            "summary": "Independent monitoring data showing actual uptime below SLA requirements"
        },
        {
            "id": "R-23",
            "party": "Respondent",
            "title": "Third-Party Monitoring Report",
            "type": "expert",
            "summary": "Independent monitoring service report confirming poor system performance"
        },
        {
            "id": "R-24",
            "party": "Respondent",
            "title": "SLA Calculation Methodology Analysis",
            "type": "expert",
            "summary": "Expert analysis showing TechStart's monitoring excluded downtime improperly"
        },
        {
            "id": "R-25",
            "party": "Respondent",
            "title": "Business Impact Assessment",
            "type": "financial",
            "summary": "Analysis showing catastrophic impact of immediate software cessation on 50,000 customers"
        },
        {
            "id": "R-26",
            "party": "Respondent",
            "title": "Migration Timeline and Industry Standards",
            "type": "technical",
            "summary": "Migration timeline documentation and expert testimony on industry-standard transition periods"
        }
    ]

# Get all facts from the data
def get_all_facts():
    args_data = get_argument_data()
    facts = []
    
    # Helper function to extract facts from arguments
    def extract_facts(arg, party):
        if not arg:
            return
            
        if 'factualPoints' in arg and arg['factualPoints']:
            for point in arg['factualPoints']:
                fact = {
                    'point': point['point'],
                    'date': point['date'],
                    'isDisputed': point['isDisputed'],
                    'party': party,
                    'paragraphs': point.get('paragraphs', ''),
                    'exhibits': point.get('exhibits', []),
                    'argId': arg['id'],
                    'argTitle': arg['title']
                }
                facts.append(fact)
                
        # Process children
        if 'children' in arg and arg['children']:
            for child_id, child in arg['children'].items():
                extract_facts(child, party)
    
    # Extract from claimant args
    for arg_id, arg in args_data['claimantArgs'].items():
        extract_facts(arg, 'Claimant')
        
    # Extract from respondent args
    for arg_id, arg in args_data['respondentArgs'].items():
        extract_facts(arg, 'Respondent')
        
    return facts

# Function to create CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Main app
def main():
    # Get the data for JavaScript
    args_data = get_argument_data()
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    facts_data = get_all_facts()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    timeline_json = json.dumps(timeline_data)
    exhibits_json = json.dumps(exhibits_data)
    facts_json = json.dumps(facts_data)
    
    # Initialize session state if not already done
    if 'view' not in st.session_state:
        st.session_state.view = "Arguments"
    
    # Add Streamlit sidebar with native design
    with st.sidebar:
        # Add the logo and CaseLens text
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 30px; padding: 10px 0;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="40" height="40">
              <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#whatsapp-mask)">
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#3B82F6"/>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <span style="margin-left: 12px; font-size: 24px; font-weight: 600; color: #262730;">caselens</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation section - moved up after search
        
        # Define button click handlers
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Create buttons with conditional styling
        if st.button("Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True, 
                    type="primary" if st.session_state.view == "Arguments" else "secondary"):
            pass
            
        if st.button("Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True,
                    type="primary" if st.session_state.view == "Exhibits" else "secondary"):
            pass
        
        st.markdown("---")
    
    # Determine which view to show based on sidebar selection
    if st.session_state.view == "Arguments":
        active_tab = 0
    else:  # Exhibits
        active_tab = 1
    
    # Initialize the view options as a JavaScript variable
    view_options_json = json.dumps({
        "activeTab": active_tab
    })
    
    # Create a single HTML component containing the full UI with minimalistic design
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Minimalistic base styling */
            html, body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                margin: 0;
                padding: 0;
                background-color: #fff;
                width: 100vw;
                min-width: 100vw;
                box-sizing: border-box;
                overflow-x: auto;
            }}
            
            * {{
                box-sizing: border-box;
                max-width: none !important;
            }}
            
            body > * {{
                width: 100vw !important;
                max-width: none !important;
            }}
            
            /* Content sections */
            .content-section {{
                display: none;
                width: calc(100vw - 40px) !important;
                max-width: none !important;
                padding: 20px;
                margin: 0;
                position: relative;
            }}
            
            .content-section.active {{
                display: block;
                width: calc(100vw - 40px) !important;
                max-width: none !important;
            }}
            
            /* Card styling */
            .card {{
                background-color: #fff;
                border: 1px solid #f0f0f0;
                border-radius: 8px;
                margin-bottom: 8px;
                overflow: hidden;
            }}
            
            .card-header {{
                padding: 12px 16px;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #f0f0f0;
                background-color: #fafafa;
            }}
            
            .card-content {{
                padding: 16px;
                display: none;
            }}
            
            /* Arguments layout */
            .arguments-row {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                width: 100%;
                max-width: none;
            }}
            
            /* Party view styles */
            .claimant-only .arguments-row > div:nth-child(2) {{
                display: none;
            }}
            .claimant-only .arguments-row > div:nth-child(1) {{
                grid-column: 1 / span 2;
            }}
            .claimant-only .respondent-color {{
                display: none;
            }}
            
            .respondent-only .arguments-row > div:nth-child(1) {{
                display: none;
            }}
            .respondent-only .arguments-row > div:nth-child(2) {{
                grid-column: 1 / span 2;
            }}
            .respondent-only .claimant-color {{
                display: none;
            }}
            
            .side-heading {{
                margin-bottom: 16px;
                font-weight: 500;
            }}
            
            .claimant-color {{
                color: #3B82F6;
            }}
            
            .respondent-color {{
                color: #e53e3e;
            }}
            
            /* Badge styling */
            .badge {{
                display: inline-block;
                padding: 3px 8px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 500;
            }}
            
            .claimant-badge {{
                background-color: rgba(59, 130, 246, 0.1);
                color: #3B82F6;
            }}
            
            .respondent-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            .exhibit-badge {{
                background-color: rgba(221, 107, 32, 0.1);
                color: #dd6b20;
            }}
            
            .disputed-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            .para-badge {{
                background-color: rgba(0, 0, 0, 0.05);
                color: #666;
                margin-left: 5px;
            }}
            
            /* Evidence and factual points */
            .item-block {{
                background-color: #fafafa;
                border-radius: 6px;
                padding: 12px;
                margin-bottom: 10px;
            }}
            
            .item-title {{
                font-weight: 600;
                margin-bottom: 6px;
                color: #333;
            }}
            
            .evidence-block {{
                background-color: #fff8f0;
                border-left: 3px solid #dd6b20;
                padding: 12px 14px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            .caselaw-block {{
                background-color: #EFF6FF;
                border-left: 3px solid #3B82F6;
                padding: 12px 14px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            /* Tables */
            table {{
                width: 100%;
                max-width: none;
                border-collapse: collapse;
            }}
            
            th {{
                text-align: left;
                padding: 12px 14px;
                background-color: #fafafa;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            td {{
                padding: 12px 14px;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            tr.disputed {{
                background-color: rgba(229, 62, 62, 0.05);
            }}
            
            /* Action buttons */
            .action-buttons {{
                position: absolute;
                top: 22px;
                right: 30px;
                display: flex;
                gap: 12px;
                z-index: 100;
                width: auto !important;
                max-width: none !important;
            }}
            
            .action-button {{
                padding: 10px 20px;
                background-color: #f9f9f9;
                border: 1px solid #e1e4e8;
                border-radius: 8px;
                display: flex;
                align-items: center;
                cursor: pointer;
                white-space: nowrap;
                font-size: 14px;
            }}
            
            .action-button:hover {{
                background-color: #f1f1f1;
            }}
            
            .export-dropdown {{
                position: relative;
                display: inline-block;
            }}
            
            .export-dropdown-content {{
                display: none;
                position: absolute;
                right: 0;
                background-color: #f9f9f9;
                min-width: 160px;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
                border-radius: 8px;
            }}
            
            .export-dropdown-content a {{
                color: black;
                padding: 12px 16px;
                text-decoration: none;
                display: block;
                cursor: pointer;
            }}
            
            .export-dropdown-content a:hover {{
                background-color: #f1f1f1;
            }}
            
            .export-dropdown:hover .export-dropdown-content {{
                display: block;
            }}
            
            /* Nested content */
            .nested-content {{
                padding-left: 24px;
                margin-top: 12px;
                border-left: 1px solid #f0f0f0;
                /* No display:none to show nested content */
            }}
            
            /* Simple list styling */
            ul.point-list {{
                list-style-type: none;
                padding-left: 0;
                margin: 0;
            }}
            
            ul.point-list li {{
                position: relative;
                padding-left: 16px;
                margin-bottom: 8px;
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
            }}
            
            ul.point-list li:before {{
                content: "•";
                position: absolute;
                left: 0;
                color: #8c8c8c;
            }}
            
            /* Chevron icon */
            .chevron {{
                transition: transform 0.2s;
            }}
            
            .chevron.expanded {{
                transform: rotate(90deg);
            }}
            
            /* Citation tags */
            .citation-tag {{
                padding: 2px 5px;
                background: rgba(0,0,0,0.05);
                border-radius: 3px;
                font-size: 11px;
                color: #666;
                margin-right: 2px;
            }}
            
            /* Section title */
            .section-title {{
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1.5rem;
                margin-top: 0;
                padding-bottom: 0.5rem;
                border-bottom: 1px solid #eaeaea;
                width: 100vw !important;
                max-width: none !important;
                padding-left: 20px;
            }}
            
            #topics-container, #facts-table-body, #timeline-body, #exhibits-body {{
                width: 100vw !important;
                max-width: none !important;
            }}
            
            /* Table view */
            .table-view {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            
            .table-view th {{
                padding: 12px 14px;
                text-align: left;
                background-color: #f8f9fa;
                border-bottom: 2px solid #dee2e6;
                position: sticky;
                top: 0;
                cursor: pointer;
            }}
            
            .table-view th:hover {{
                background-color: #e9ecef;
            }}
            
            .table-view td {{
                padding: 12px 14px;
                border-bottom: 1px solid #dee2e6;
            }}
            
            .table-view tr:hover {{
                background-color: #f8f9fa;
            }}
            
            /* View toggle */
            .view-toggle {{
                display: flex;
                justify-content: flex-end;
                margin-bottom: 16px;
            }}
            
            .view-toggle button {{
                padding: 8px 16px;
                border: 1px solid #e2e8f0;
                background-color: #f7fafc;
                cursor: pointer;
            }}
            
            .view-toggle button.active {{
                background-color: #3B82F6;
                color: white;
                border-color: #3B82F6;
            }}
            
            .view-toggle button:first-child {{
                border-radius: 8px 0 0 8px;
            }}
            
            .view-toggle button:last-child {{
                border-radius: 0 8px 8px 0;
            }}
            
            /* Copy notification */
            .copy-notification {{
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: #2d3748;
                color: white;
                padding: 10px 20px;
                border-radius: 4px;
                z-index: 1000;
                opacity: 0;
                transition: opacity 0.3s;
            }}
            
            .copy-notification.show {{
                opacity: 1;
            }}
        </style>
    </head>
    <body>
        <div id="copy-notification" class="copy-notification">Content copied to clipboard!</div>
        
        <div class="action-buttons">
                <button class="action-button" onclick="copyAllContent()">
                    Copy
                </button>
                <div class="export-dropdown">
                    <button class="action-button">
                        Export
                    </button>
                    <div class="export-dropdown-content">
                        <a onclick="exportAsCsv()">CSV</a>
                        <a onclick="exportAsPdf()">PDF</a>
                        <a onclick="exportAsWord()">Word</a>
                    </div>
                </div>
            </div>
            
            <!-- Arguments Section -->
            <div id="arguments" class="content-section">
                <div class="section-title">Dispute Summary: Software Licensing & IP Rights</div>
                
                <!-- Direct inline buttons for view toggling -->
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <div id="party-buttons" style="display: flex; gap: 5px;">
                        <button id="both-btn" onclick="changePartyView('both')" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #3B82F6; color: white; cursor: pointer; border-radius: 8px;">Both Parties</button>
                        
                        <button id="app-btn" onclick="changePartyView('claimant')" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #f7fafc; color: black; cursor: pointer; border-radius: 8px;">Claimant Only</button>
                        
                        <button id="resp-btn" onclick="changePartyView('respondent')" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #f7fafc; color: black; cursor: pointer; border-radius: 8px;">Respondent Only</button>
                    </div>
                    <div style="display: flex; gap: 20px; align-items: center;">
                        <button id="detailed-view-btn" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #3B82F6; color: white; cursor: pointer; border-radius: 8px;" onclick="document.getElementById('detailed-view').style.display='block'; document.getElementById('table-view').style.display='none'; this.style.backgroundColor='#3B82F6'; this.style.color='white'; document.getElementById('table-view-btn').style.backgroundColor='#f7fafc'; document.getElementById('table-view-btn').style.color='black';">Detailed View</button>
                        
                        <button id="table-view-btn" style="padding: 8px 16px; border: 1px solid #e2e8f0; background-color: #f7fafc; cursor: pointer; border-radius: 8px;" onclick="document.getElementById('detailed-view').style.display='none'; document.getElementById('table-view').style.display='block'; this.style.backgroundColor='#3B82F6'; this.style.color='white'; document.getElementById('detailed-view-btn').style.backgroundColor='#f7fafc'; document.getElementById('detailed-view-btn').style.color='black';">Table View</button>
                    </div>
                </div>
                
                <!-- Detailed view content -->
                <div id="detailed-view" class="view-content active">
                    <div id="topics-container"></div>
                </div>
                
                <!-- Table view content -->
                <div id="table-view" class="view-content" style="display: none;">
                    <table class="table-view">
                        <thead>
                            <tr>
                                <th onclick="sortTable('table-view-body', 0)">ID</th>
                                <th onclick="sortTable('table-view-body', 1)">Argument</th>
                                <th onclick="sortTable('table-view-body', 2)">Party</th>
                                <th onclick="sortTable('table-view-body', 3)">Status</th>
                                <th onclick="sortTable('table-view-body', 4)">Evidence</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody id="table-view-body"></tbody>
                    </table>
                </div>
            </div>
            
            <!-- Exhibits Section -->
            <div id="exhibits" class="content-section">
                <div class="section-title">Case Exhibits</div>
                <table id="exhibits-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Party</th>
                            <th>Title</th>
                            <th>Type</th>
                            <th>Summary</th>
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
            const factsData = {facts_json};
            const viewOptions = {view_options_json};
            
            // Function to change party view
            function changePartyView(view) {{
                console.log("Changing party view to:", view);
                
                // Get the container
                const container = document.getElementById('topics-container');
                
                // Update button styling
                const bothBtn = document.getElementById('both-btn');
                const appBtn = document.getElementById('app-btn');
                const respBtn = document.getElementById('resp-btn');
                
                // Reset button styles
                bothBtn.style.backgroundColor = '#f7fafc';
                bothBtn.style.color = 'black';
                appBtn.style.backgroundColor = '#f7fafc';
                appBtn.style.color = 'black';
                respBtn.style.backgroundColor = '#f7fafc';
                respBtn.style.color = 'black';
                
                // Apply class to container based on view
                container.className = '';
                
                if (view === 'both') {{
                    bothBtn.style.backgroundColor = '#3B82F6';
                    bothBtn.style.color = 'white';
                    // Default view - no special class needed
                }} else if (view === 'claimant') {{
                    appBtn.style.backgroundColor = '#3B82F6';
                    appBtn.style.color = 'white';
                    container.className = 'claimant-only';
                }} else if (view === 'respondent') {{
                    respBtn.style.backgroundColor = '#3B82F6';
                    respBtn.style.color = 'white';
                    container.className = 'respondent-only';
                }}
            }}
            
            // Show the selected view based on sidebar selection
            document.addEventListener('DOMContentLoaded', function() {{
                // Show the correct section based on sidebar selection
                const sections = ['arguments', 'exhibits'];
                const activeSection = sections[viewOptions.activeTab];
                
                document.querySelectorAll('.content-section').forEach(section => {{
                    section.classList.remove('active');
                }});
                
                document.getElementById(activeSection).classList.add('active');
                
                // Initialize content as needed
                if (activeSection === 'arguments') {{
                    renderTopics();
                    renderArgumentsTable();
                }}
                if (activeSection === 'exhibits') renderExhibits();
            }});
            
            // Switch view between detailed and table
            function switchView(viewType) {{
                const detailedBtn = document.getElementById('detailed-view-btn');
                const tableBtn = document.getElementById('table-view-btn');
                const detailedView = document.getElementById('detailed-view');
                const tableView = document.getElementById('table-view');
                
                if (viewType === 'detailed') {{
                    detailedBtn.classList.add('active');
                    tableBtn.classList.remove('active');
                    detailedView.style.display = 'block';
                    tableView.style.display = 'none';
                }} else {{
                    detailedBtn.classList.remove('active');
                    tableBtn.classList.add('active');
                    detailedView.style.display = 'none';
                    tableView.style.display = 'block';
                }}
            }}
            
            // Sort table function
            function sortTable(tableId, columnIndex) {{
                const table = document.getElementById(tableId);
                const rows = Array.from(table.rows);
                let dir = 1; // 1 for ascending, -1 for descending
                
                // Check if already sorted in this direction
                if (table.getAttribute('data-sort-column') === String(columnIndex) &&
                    table.getAttribute('data-sort-dir') === '1') {{
                    dir = -1;
                }}
                
                // Sort the rows
                rows.sort((a, b) => {{
                    const cellA = a.cells[columnIndex].textContent.trim();
                    const cellB = b.cells[columnIndex].textContent.trim();
                    
                    // Handle date sorting
                    if (columnIndex === 0 && tableId === 'facts-table-body') {{
                        // Attempt to parse as dates
                        const dateA = new Date(cellA);
                        const dateB = new Date(cellB);
                        
                        if (!isNaN(dateA) && !isNaN(dateB)) {{
                            return dir * (dateA - dateB);
                        }}
                    }}
                    
                    return dir * cellA.localeCompare(cellB);
                }});
                
                // Remove existing rows and append in new order
                rows.forEach(row => table.appendChild(row));
                
                // Store current sort direction and column
                table.setAttribute('data-sort-column', columnIndex);
                table.setAttribute('data-sort-dir', dir);
            }}
            
            // Copy all content function
            function copyAllContent() {{
                const activeSection = document.querySelector('.content-section.active');
                if (!activeSection) return;
                
                let contentToCopy = '';
                
                // Extract content based on section
                if (activeSection.id === 'arguments') {{
                    if (document.getElementById('detailed-view').style.display !== 'none') {{
                        contentToCopy = extractArgumentsDetailedText();
                    }} else {{
                        contentToCopy = extractArgumentsTableText();
                    }}
                }} else if (activeSection.id === 'exhibits') {{
                    contentToCopy = extractExhibitsText();
                }}
                
                // Create a temporary textarea to copy the content
                const textarea = document.createElement('textarea');
                textarea.value = contentToCopy;
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);
                
                // Show notification
                const notification = document.getElementById('copy-notification');
                notification.classList.add('show');
                
                setTimeout(() => {{
                    notification.classList.remove('show');
                }}, 2000);
            }}
            
            // Export functions
            function exportAsCsv() {{
                const activeSection = document.querySelector('.content-section.active');
                if (!activeSection) return;
                
                let contentToCsv = '';
                
                // Extract content based on section
                if (activeSection.id === 'arguments') {{
                    if (document.getElementById('detailed-view').style.display !== 'none') {{
                        contentToCsv = extractArgumentsDetailedText();
                    }} else {{
                        contentToCsv = extractArgumentsTableText();
                    }}
                }} else if (activeSection.id === 'exhibits') {{
                    contentToCsv = extractExhibitsText();
                }}
                
                // Create link for CSV download
                const csvContent = "data:text/csv;charset=utf-8," + encodeURIComponent(contentToCsv);
                const encodedUri = csvContent;
                const link = document.createElement("a");
                link.setAttribute("href", encodedUri);
                link.setAttribute("download", activeSection.id + ".csv");
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }}
            
            function exportAsPdf() {{
                alert("PDF export functionality would be implemented here");
            }}
            
            function exportAsWord() {{
                alert("Word export functionality would be implemented here");
            }}
            
            // Extract text from arguments detailed view
            function extractArgumentsDetailedText() {{
                const container = document.getElementById('topics-container');
                return container.innerText;
            }}
            
            // Extract text from arguments table
            function extractArgumentsTableText() {{
                const table = document.querySelector('#table-view table');
                let text = '';
                
                // Get headers
                const headers = Array.from(table.querySelectorAll('th'))
                    .map(th => th.textContent.trim())
                    .filter(header => header !== 'Actions')
                    .join('\\t');
                
                text += headers + '\\n';
                
                // Get rows
                const rows = table.querySelectorAll('tbody tr');
                rows.forEach(row => {{
                    const rowText = Array.from(row.querySelectorAll('td'))
                        .filter((td, index) => index !== row.cells.length - 1) // Exclude Actions column
                        .map(td => td.textContent.trim())
                        .join('\\t');
                    
                    text += rowText + '\\n';
                }});
                
                return text;
            }}
            
            // Extract text from exhibits
            function extractExhibitsText() {{
                const table = document.getElementById('exhibits-table');
                let text = '';
                
                // Get headers
                const headers = Array.from(table.querySelectorAll('th'))
                    .map(th => th.textContent.trim())
                    .join('\\t');
                
                text += headers + '\\n';
                
                // Get rows
                const rows = table.querySelectorAll('tbody tr');
                rows.forEach(row => {{
                    const rowText = Array.from(row.querySelectorAll('td'))
                        .map(td => td.textContent.trim())
                        .join('\\t');
                    
                    text += rowText + '\\n';
                }});
                
                return text;
            }}
            
            // Render arguments in table format
            function renderArgumentsTable() {{
                const tableBody = document.getElementById('table-view-body');
                tableBody.innerHTML = '';
                
                // Helper function to flatten arguments
                function flattenArguments(args, party) {{
                    let result = [];
                    
                    Object.values(args).forEach(arg => {{
                        // Track if argument has disputed facts
                        const hasDisputedFacts = arg.factualPoints && 
                            arg.factualPoints.some(point => point.isDisputed);
                        
                        // Count pieces of evidence
                        const evidenceCount = arg.evidence ? arg.evidence.length : 0;
                        
                        // Add this argument
                        result.push({{
                            id: arg.id,
                            title: arg.title,
                            party: party,
                            hasDisputedFacts: hasDisputedFacts,
                            evidenceCount: evidenceCount,
                            paragraphs: arg.paragraphs
                        }});
                        
                        // Process children recursively
                        if (arg.children) {{
                            Object.values(arg.children).forEach(child => {{
                                result = result.concat(flattenArguments({{[child.id]: child}}, party));
                            }});
                        }}
                    }});
                    
                    return result;
                }}
                
                // Get flattened arguments
                const claimantArgs = flattenArguments(argsData.claimantArgs, "Claimant");
                const respondentArgs = flattenArguments(argsData.respondentArgs, "Respondent");
                const allArgs = [...claimantArgs, ...respondentArgs];
                
                // Render rows
                allArgs.forEach(arg => {{
                    const row = document.createElement('tr');
                    
                    // ID column
                    const idCell = document.createElement('td');
                    idCell.textContent = arg.id;
                    row.appendChild(idCell);
                    
                    // Title column
                    const titleCell = document.createElement('td');
                    titleCell.textContent = arg.title;
                    row.appendChild(titleCell);
                    
                    // Party column
                    const partyCell = document.createElement('td');
                    const partyBadge = document.createElement('span');
                    partyBadge.className = `badge ${{arg.party === 'Claimant' ? 'claimant-badge' : 'respondent-badge'}}`;
                    partyBadge.textContent = arg.party;
                    partyCell.appendChild(partyBadge);
                    row.appendChild(partyCell);
                    
                    // Status column
                    const statusCell = document.createElement('td');
                    if (arg.hasDisputedFacts) {{
                        const disputedBadge = document.createElement('span');
                        disputedBadge.className = 'badge disputed-badge';
                        disputedBadge.textContent = 'Disputed';
                        statusCell.appendChild(disputedBadge);
                    }} else {{
                        statusCell.textContent = 'Undisputed';
                    }}
                    row.appendChild(statusCell);
                    
                    // Evidence column
                    const evidenceCell = document.createElement('td');
                    evidenceCell.textContent = arg.evidenceCount > 0 ? `${{arg.evidenceCount}} items` : 'None';
                    row.appendChild(evidenceCell);
                    
                    // Actions column
                    const actionsCell = document.createElement('td');
                    const viewBtn = document.createElement('button');
                    viewBtn.textContent = 'View';
                    viewBtn.style.padding = '4px 8px';
                    viewBtn.style.marginRight = '8px';
                    viewBtn.style.border = '1px solid #e2e8f0';
                    viewBtn.style.borderRadius = '8px';
                    viewBtn.style.backgroundColor = '#f7fafc';
                    viewBtn.style.cursor = 'pointer';
                    viewBtn.onclick = function() {{
                        // Switch to detailed view and expand this argument
                        switchView('detailed');
                        // Logic to find and expand the argument would go here
                    }};
                    actionsCell.appendChild(viewBtn);
                    row.appendChild(actionsCell);
                    
                    tableBody.appendChild(row);
                }});
            }}
            
            // Render overview points
            function renderOverviewPoints(overview) {{
                if (!overview || !overview.points || overview.points.length === 0) return '';
                
                const pointsList = overview.points.map(point => 
                    `<li>
                        <span>${{point}}</span>
                        <span class="para-badge">¶${{overview.paragraphs}}</span>
                    </li>`
                ).join('');
                
                return `
                <div class="item-block">
                    <div class="item-title">Supporting Points</div>
                    <ul class="point-list">
                        ${{pointsList}}
                    </ul>
                </div>
                `;
            }}
            
            // Render factual points (now called Events)
            function renderFactualPoints(points) {{
                if (!points || points.length === 0) return '';
                
                const pointsHtml = points.map(point => {{
                    const disputed = point.isDisputed 
                        ? `<span class="badge disputed-badge">Disputed</span>` 
                        : '';
                    
                    // Exhibits badges
                    const exhibitBadges = point.exhibits && point.exhibits.length > 0
                        ? point.exhibits.map(exhibitId => `<span class="badge exhibit-badge">${{exhibitId}}</span>`).join(' ')
                        : '';
                    
                    return `
                    <div class="item-block">
                        <div style="display: flex; justify-content: space-between;">
                            <span>${{point.point}}</span>
                            <span>
                                ${{disputed}}
                                ${{exhibitBadges}}
                            </span>
                        </div>
                        <div style="font-size: 12px; color: #666; margin-top: 4px;">${{point.date}}</div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Events</div>
                    ${{pointsHtml}}
                </div>
                `;
            }}
            
            // Render evidence
            function renderEvidence(evidence) {{
                if (!evidence || evidence.length === 0) return '';
                
                const evidenceHtml = evidence.map(item => {{
                    const citations = item.citations && item.citations.length > 0
                        ? item.citations.map(cite => `<span class="citation-tag">¶${{cite}}</span>`).join('')
                        : '';
                    
                    return `
                    <div class="evidence-block">
                        <div class="item-title">${{item.id}}: ${{item.title}}</div>
                        <div style="margin: 6px 0;">${{item.summary}}</div>
                        <div style="margin-top: 8px; font-size: 12px;">
                            <span style="color: #666; margin-right: 5px;">Cited in:</span>
                            ${{citations}}
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Evidence</div>
                    ${{evidenceHtml}}
                </div>
                `;
            }}
            
            // Render case law
            function renderCaseLaw(cases) {{
                if (!cases || cases.length === 0) return '';
                
                const casesHtml = cases.map(item => {{
                    const citedParagraphs = item.citedParagraphs && item.citedParagraphs.length > 0
                        ? item.citedParagraphs.map(cite => `<span class="citation-tag">¶${{cite}}</span>`).join('')
                        : '';
                    
                    return `
                    <div class="caselaw-block">
                        <div class="item-title">${{item.caseNumber}}</div>
                        <div style="font-size: 12px; margin: 2px 0 8px 0;">¶${{item.paragraphs}}</div>
                        <div style="font-weight: 500; margin-bottom: 4px;">${{item.title}}</div>
                        <div style="margin: 6px 0;">${{item.relevance}}</div>
                        <div style="margin-top: 8px; font-size: 12px;">
                            <span style="color: #666; margin-right: 5px;">Key Paragraphs:</span>
                            ${{citedParagraphs}}
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Case Law</div>
                    ${{casesHtml}}
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
            function renderArgument(arg, side) {{
                if (!arg) return '';
                
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const argId = `${{side}}-${{arg.id}}`;
                
                // Store corresponding pair ID for synchronization
                const pairId = arg.id;
                
                // Style based on side
                const badgeClass = side === 'claimant' ? 'claimant-badge' : 'respondent-badge';
                
                // Render children if any - removed style="display: none;"
                let childrenHtml = '';
                if (hasChildren) {{
                    childrenHtml = `<div class="nested-content" id="children-${{argId}}">`;
                    
                    Object.values(arg.children).forEach(child => {{
                        childrenHtml += renderArgument(child, side);
                    }});
                    
                    childrenHtml += `</div>`;
                }}
                
                return `
                <div class="card">
                    <div class="card-header" onclick="toggleArgument('${{argId}}', '${{pairId}}', '${{side}}')">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <svg id="chevron-${{argId}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6"></polyline>
                            </svg>
                            <span>${{arg.id}}. ${{arg.title}}</span>
                        </div>
                        <span class="badge ${{badgeClass}}">¶${{arg.paragraphs}}</span>
                    </div>
                    <div class="card-content" id="content-${{argId}}">
                        ${{renderArgumentContent(arg)}}
                    </div>
                    ${{childrenHtml}}
                </div>
                `;
            }}
            
            // Render arguments by topic
            function renderTopics() {{
                const container = document.getElementById('topics-container');
                let html = '';
                
                argsData.topics.forEach(topic => {{
                    html += `
                    <div class="card" style="margin-bottom: 20px;">
                        <div class="card-header" onclick="toggleCard('topic-${{topic.id}}')">
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <svg id="chevron-topic-${{topic.id}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <span>${{topic.title}}</span>
                            </div>
                        </div>
                        <div class="card-content" id="content-topic-${{topic.id}}">
                            <p>${{topic.description}}</p>
                            
                            ${{topic.argumentIds.map(argId => {{
                                if (argsData.claimantArgs[argId] && argsData.respondentArgs[argId]) {{
                                    return `
                                    <div style="margin-top: 20px;">
                                        <div class="arguments-row">
                                            <div>
                                                <h3 class="side-heading claimant-color">Claimant's Position</h3>
                                                ${{renderArgument(argsData.claimantArgs[argId], 'claimant')}}
                                            </div>
                                            <div>
                                                <h3 class="side-heading respondent-color">Respondent's Position</h3>
                                                ${{renderArgument(argsData.respondentArgs[argId], 'respondent')}}
                                            </div>
                                        </div>
                                    </div>
                                    `;
                                }}
                                return '';
                            }}).join('')}}
                        </div>
                    </div>
                    `;
                }});
                
                container.innerHTML = html;
                
                // Auto-expand first topic
                setTimeout(() => {{
                    const firstTopic = argsData.topics[0];
                    if (firstTopic) {{
                        toggleCard(`topic-${{firstTopic.id}}`);
                    }}
                }}, 100);
            }}
            
            // Render exhibits
            function renderExhibits() {{
                const tbody = document.getElementById('exhibits-body');
                tbody.innerHTML = '';
                
                exhibitsData.forEach(item => {{
                    const row = document.createElement('tr');
                    const badgeClass = item.party === 'Claimant' ? 'claimant-badge' : 'respondent-badge';
                    
                    row.innerHTML = `
                        <td>${{item.id}}</td>
                        <td><span class="badge ${{badgeClass}}">${{item.party}}</span></td>
                        <td>${{item.title}}</td>
                        <td>${{item.type}}</td>
                        <td>${{item.summary}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Toggle a card without synchronizing - modified to only toggle content, not children
            function toggleCard(id) {{
                const contentEl = document.getElementById(`content-${{id}}`);
                const chevronEl = document.getElementById(`chevron-${{id}}`);
                
                if (contentEl) {{
                    contentEl.style.display = contentEl.style.display === 'block' ? 'none' : 'block';
                }}
                
                if (chevronEl) {{
                    chevronEl.classList.toggle('expanded');
                }}
            }}
            
            // Toggle an argument and its counterpart - modified to only toggle content
            function toggleArgument(argId, pairId, side) {{
                // First, handle the clicked argument
                toggleCard(argId);
                
                // Then, determine and handle the counterpart
                const otherSide = side === 'claimant' ? 'respondent' : 'claimant';
                const counterpartId = `${{otherSide}}-${{pairId}}`;
                
                // Toggle the counterpart (if it exists)
                const counterpartContentEl = document.getElementById(`content-${{counterpartId}}`);
                if (counterpartContentEl) {{
                    const counterpartChevronEl = document.getElementById(`chevron-${{counterpartId}}`);
                    
                    // Make sure the counterpart's state matches the toggled argument
                    const originalDisplay = document.getElementById(`content-${{argId}}`).style.display;
                    counterpartContentEl.style.display = originalDisplay;
                    
                    if (counterpartChevronEl) {{
                        if (originalDisplay === 'block') {{
                            counterpartChevronEl.classList.add('expanded');
                        }} else {{
                            counterpartChevronEl.classList.remove('expanded');
                        }}
                    }}
                }}
            }}
            
            // Render timeline
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
                tbody.innerHTML = '';
                
                timelineData.forEach(item => {{
                    const row = document.createElement('tr');
                    if (item.status === 'Disputed') {{
                        row.classList.add('disputed');
                    }}
                    
                    row.innerHTML = `
                        <td>${{item.date}}</td>
                        <td>${{item.claimantVersion}}</td>
                        <td>${{item.respondentVersion}}</td>
                        <td>${{item.status}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Render exhibits
            function renderExhibits() {{
                const tbody = document.getElementById('exhibits-body');
                tbody.innerHTML = '';
                
                exhibitsData.forEach(item => {{
                    const row = document.createElement('tr');
                    const badgeClass = item.party === 'Claimant' ? 'claimant-badge' : 'respondent-badge';
                    
                    row.innerHTML = `
                        <td>${{item.id}}</td>
                        <td><span class="badge ${{badgeClass}}">${{item.party}}</span></td>
                        <td>${{item.title}}</td>
                        <td>${{item.type}}</td>
                        <td>${{item.summary}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("TechStart Inc. v. MegaCorp Ltd.")
    
    # Add search bar with button under title
    col1, col2 = st.columns([6, 1])
    with col1:
        search_query = st.text_input("", placeholder="Search arguments, facts, evidence...", label_visibility="collapsed", key="main_search")
    with col2:
        st.button("Search", type="primary", use_container_width=True)
    
    # Add spacing after search bar
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
    components.html(html_content, height=950, width=1400, scrolling=True)

if __name__ == "__main__":
    main()
