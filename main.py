import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'current_view_type' not in st.session_state:
    st.session_state.current_view_type = "card"
if 'current_tab_type' not in st.session_state:
    st.session_state.current_tab_type = "all"

# Create data structures
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
                                    "exhibits": ["C-2"],
                                    "source_text": "The club was initially registered with the National Football Federation on January 12, 1950, under registration number NFF-1950-0047, establishing its legal existence as a sporting entity.",
                                    "page": 31,
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                },
                                {
                                    "point": "Brief administrative gap in 1975-1976",
                                    "date": "1975-1976",
                                    "isDisputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "29-30",
                                    "exhibits": ["C-2"],
                                    "source_text": "While there was a temporary administrative restructuring during 1975-1976 due to financial difficulties, the club's core operations and identity remained intact throughout this period, with no cessation of sporting activities.",
                                    "page": 35,
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
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
                            "exhibits": ["C-4"],
                            "source_text": "The club has consistently utilized blue and white as its primary colors since its founding in 1950, with these colors being integral to the club's visual identity and fan recognition throughout its history.",
                            "page": 58,
                            "doc_name": "Statement of Appeal",
                            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
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
                                    "exhibits": ["C-5"],
                                    "source_text": "Minor variations in the specific shades of blue and white used in uniforms and club materials during the 1970s were purely aesthetic choices that did not alter the fundamental color identity of the club.",
                                    "page": 63,
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                },
                                {
                                    "point": "Temporary third color addition in 1980s",
                                    "date": "1982-1988",
                                    "isDisputed": False,
                                    "paragraphs": "58-59",
                                    "exhibits": ["C-5"],
                                    "source_text": "Between 1982 and 1988, the club temporarily incorporated a third accent color (gold) in its uniform design for special occasions, while maintaining blue and white as the primary colors.",
                                    "page": 65,
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                }
                            ],
                            "children": {}
                        }
                    }
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
                    "summary": "Official competition records from the National Football Federation for the 1975-1976 season, showing complete absence of the club from all levels of competition that season. Includes official withdrawal notification dated May 15, 1975.",
                    "citations": ["208", "209", "210"]
                },
                {
                    "id": "R-2",
                    "title": "Financial Audit Reports",
                    "summary": "Independent auditor reports from 1975-1976 documenting the complete cessation of club operations, closure of all bank accounts, and termination of all contractual obligations, establishing a clear operational break.",
                    "citations": ["211", "212", "213"]
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
            "children": {}
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

def get_all_facts():
    args_data = get_argument_data()
    facts = []
    
    def extract_facts(arg, party):
        if not arg:
            return
            
        if 'factualPoints' in arg and arg['factualPoints']:
            for point in arg['factualPoints']:
                fact = {
                    'event': point['point'],
                    'date': point['date'],
                    'isDisputed': point['isDisputed'],
                    'party': party,
                    'paragraphs': point.get('paragraphs', ''),
                    'exhibits': point.get('exhibits', []),
                    'argId': arg['id'],
                    'argTitle': arg['title'],
                    'source_text': point.get('source_text', ''),
                    'page': point.get('page', ''),
                    'doc_name': point.get('doc_name', ''),
                    'doc_summary': point.get('doc_summary', ''),
                    'claimant_submission': '',
                    'respondent_submission': ''
                }
                facts.append(fact)
                
        if 'children' in arg and arg['children']:
            for child_id, child in arg['children'].items():
                extract_facts(child, party)
    
    for arg_id, arg in args_data['claimantArgs'].items():
        extract_facts(arg, 'Appellant')
        
    for arg_id, arg in args_data['respondentArgs'].items():
        extract_facts(arg, 'Respondent')
    
    enhanced_facts = []
    fact_groups = {}
    
    for fact in facts:
        key = f"{fact['date']}_{fact['event'][:50]}"
        if key not in fact_groups:
            fact_groups[key] = {
                'event': fact['event'],
                'date': fact['date'],
                'isDisputed': fact['isDisputed'],
                'claimant_submission': '',
                'respondent_submission': '',
                'source_text': fact['source_text'],
                'page': fact['page'],
                'doc_name': fact['doc_name'],
                'doc_summary': fact['doc_summary'],
                'exhibits': fact['exhibits'],
                'paragraphs': fact['paragraphs'],
                'argId': fact['argId'],
                'argTitle': fact['argTitle'],
                'parties_involved': []
            }
        
        if fact['party'] == 'Appellant':
            fact_groups[key]['claimant_submission'] = fact['source_text']
        else:
            fact_groups[key]['respondent_submission'] = fact['source_text']
        
        fact_groups[key]['parties_involved'].append(fact['party'])
        
        if fact['isDisputed']:
            fact_groups[key]['isDisputed'] = True
    
    for key, group in fact_groups.items():
        enhanced_fact = {
            'event': group['event'],
            'date': group['date'],
            'isDisputed': group['isDisputed'],
            'source_text': group['source_text'],
            'page': group['page'],
            'doc_name': group['doc_name'],
            'doc_summary': group['doc_summary'],
            'exhibits': group['exhibits'],
            'paragraphs': group['paragraphs'],
            'argId': group['argId'],
            'argTitle': group['argTitle'],
            'claimant_submission': group['claimant_submission'] or 'No specific submission recorded',
            'respondent_submission': group['respondent_submission'] or 'No specific submission recorded',
            'parties_involved': list(set(group['parties_involved']))
        }
        enhanced_facts.append(enhanced_fact)
    
    return enhanced_facts

def get_document_sets():
    return [
        {
            "id": "appeal",
            "name": "Appeal",
            "party": "Mixed",
            "category": "Appeal",
            "isGroup": True,
            "documents": [
                {"id": "1", "name": "1. Statement of Appeal", "party": "Appellant", "category": "Appeal"},
                {"id": "2", "name": "2. Request for a Stay", "party": "Appellant", "category": "Appeal"},
                {"id": "5", "name": "5. Appeal Brief", "party": "Appellant", "category": "Appeal"},
                {"id": "10", "name": "Jurisprudence", "party": "Shared", "category": "Appeal"}
            ]
        },
        {
            "id": "provisional_measures",
            "name": "provisional measures",
            "party": "Respondent",
            "category": "provisional measures",
            "isGroup": True,
            "documents": [
                {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent", "category": "provisional measures"},
                {"id": "4", "name": "4. Answer to PM", "party": "Respondent", "category": "provisional measures"}
            ]
        },
        {
            "id": "admissibility",
            "name": "admissibility",
            "party": "Mixed",
            "category": "admissibility",
            "isGroup": True,
            "documents": [
                {"id": "6", "name": "6. Brief on Admissibility", "party": "Respondent", "category": "admissibility"},
                {"id": "7", "name": "7. Reply to Objection to Admissibility", "party": "Appellant", "category": "admissibility"},
                {"id": "11", "name": "Objection to Admissibility", "party": "Respondent", "category": "admissibility"}
            ]
        },
        {
            "id": "challenge",
            "name": "challenge",
            "party": "Mixed",
            "category": "challenge",
            "isGroup": True,
            "documents": [
                {"id": "8", "name": "8. Challenge", "party": "Appellant", "category": "challenge"},
                {"id": "9", "name": "ChatGPT", "party": "Shared", "category": "challenge"},
                {"id": "12", "name": "Swiss Court", "party": "Shared", "category": "challenge"}
            ]
        }
    ]

def get_evidence_content(fact):
    if not fact.get('exhibits') or len(fact['exhibits']) == 0:
        return []
    
    args_data = get_argument_data()
    evidence_content = []
    
    # Sample document content for preview
    document_previews = {
        "C-1": {
            "content": """CERTIFICATE OF REGISTRATION
National Football Federation
Registration No: NFF-1950-0047

TO WHOM IT MAY CONCERN:

This is to certify that ATHLETIC CLUB UNITED has been duly registered with the National Football Federation on January 12, 1950, and is authorized to participate in all sanctioned football competitions under the jurisdiction of this federation.

The club has maintained continuous registration since its initial filing date and has complied with all regulatory requirements for operational continuity.

REGISTRATION DETAILS:
- Club Name: Athletic Club United
- Registration Date: January 12, 1950
- Federation ID: NFF-1950-0047
- Status: Active - Continuous
- Last Renewal: January 15, 2024

This certificate serves as official documentation of the club's legal standing and operational authority within the national football framework.

Signed,
Director of Registration
National Football Federation""",
            "doc_type": "Registration Certificate",
            "pages": 2
        },
        "C-2": {
            "content": """COMPETITION PARTICIPATION RECORDS
Athletic Club United - Historical Analysis
Period: 1950-2024

SUMMARY OF PARTICIPATION:
The following records demonstrate uninterrupted competitive activity by Athletic Club United across multiple divisions and tournaments since 1950.

DIVISION PARTICIPATION:
1950-1960: Second Division (10 seasons)
1961-1975: First Division (15 seasons) 
1976-1985: Second Division (10 seasons)
1986-2000: First Division (15 seasons)
2001-2024: Premier Division (24 seasons)

TOURNAMENT RECORDS:
- National Cup: 74 participations (1950-2024)
- Regional Championships: 68 participations
- International Friendlies: 156 matches recorded

NOTABLE ACHIEVEMENTS:
- 1967: First Division Champions
- 1982: National Cup Runners-up
- 1995: First Division Champions
- 2010: Premier Division 3rd Place

The records show consistent participation without any gaps in competitive activity, maintaining the same club identity and registration throughout all periods.""",
            "doc_type": "Competition Records",
            "pages": 12
        },
        "C-4": {
            "content": """MEDIA COVERAGE ARCHIVE
Athletic Club United - Historical Documentation
Compiled by Sports Heritage Foundation

ARCHIVE OVERVIEW:
This comprehensive collection spans 74 years of media coverage, consistently documenting Athletic Club United under the same name and identity from 1950 to present day.

SAMPLE HEADLINES:

1952 - "Athletic Club United Secures Promotion"
Local Sports Weekly, March 15, 1952

1967 - "United Claims First Division Title in Historic Victory"
National Football Gazette, May 22, 1967

1975 - "Athletic Club United Faces Financial Restructuring"
Sports Business Daily, September 3, 1975

1976 - "United Returns Stronger After Administrative Changes"
Football Today, February 18, 1976

1995 - "Athletic Club United: 45 Years of Continuous Excellence"
Sports Century Magazine, January 12, 1995

2000 - "The Millennium Club: United's 50-Year Journey"
Football Heritage Quarterly, Volume 12

2024 - "Athletic Club United: Still Going Strong After 74 Years"
Modern Football Review, January 2024

ANALYSIS NOTES:
Throughout all coverage periods, media consistently refers to the organization as "Athletic Club United" with no name variations or identity discontinuities recorded.""",
            "doc_type": "Media Archive",
            "pages": 89
        },
        "C-5": {
            "content": """VISUAL IDENTITY DOCUMENTATION
Athletic Club United - Color Analysis Study
Sports Branding Institute, 2024

EXECUTIVE SUMMARY:
This study examines the visual continuity of Athletic Club United's color scheme from 1950 to present, analyzing uniform designs, promotional materials, and stadium branding.

PRIMARY COLOR ANALYSIS:
Base Colors: Blue (#1E3A8A) and White (#FFFFFF)
Usage Period: 1950-Present (Continuous)

DOCUMENTED VARIATIONS:
1950-1969: Deep Navy Blue with Pure White
1970-1979: Royal Blue with Off-White (Cream undertones)
1980-1989: Royal Blue with Pure White + Gold accents (1982-1988)
1990-1999: Navy Blue with Pure White
2000-2009: Royal Blue with Pure White
2010-Present: Deep Blue with Pure White

ANALYSIS CONCLUSIONS:
1. Core identity maintained throughout all periods
2. Minor shade variations within blue spectrum
3. White consistently used as secondary color
4. Temporary gold accent (1982-1988) did not replace base colors
5. No periods of complete color scheme abandonment

The evidence demonstrates unbroken visual identity continuity despite minor aesthetic updates reflecting contemporary design trends.""",
            "doc_type": "Color Analysis Report",
            "pages": 8
        },
        "R-1": {
            "content": """FEDERATION WITHDRAWAL NOTIFICATION
National Football Federation
Official Records Department

DATE: May 15, 1975
TO: Athletic Club United
FROM: Competition Registration Office

SUBJECT: Competition Withdrawal - 1975-1976 Season

This official notification confirms the withdrawal of Athletic Club United from all Federation competitions for the 1975-1976 season, effective immediately.

WITHDRAWAL DETAILS:
- Reason: Financial restructuring and administrative reorganization
- Effective Date: May 15, 1975
- Competition Status: Suspended
- Registration Status: Under review

FEDERATION RECORDS SHOW:
- No team entries for 1975-1976 season
- No player registrations processed
- No match participations recorded
- No fee payments received

The club's competitive status remains suspended pending resolution of administrative matters and financial obligations.

This withdrawal creates a gap in the club's competitive history and affects continuity claims under Federation succession policies.

Administrative Officer
Competition Management Division
National Football Federation""",
            "doc_type": "Official Withdrawal Notice",
            "pages": 1
        },
        "R-2": {
            "content": """INDEPENDENT AUDIT REPORT
Financial Assessment - Athletic Club United
Prepared by: Certified Sports Auditors Ltd.
Period: 1975-1976

AUDIT SUMMARY:
This independent audit examines the financial and operational status of Athletic Club United during the 1975-1976 period.

KEY FINDINGS:

OPERATIONAL CESSATION:
- All bank accounts closed: September 1975
- Staff contracts terminated: August 1975
- Facility leases terminated: October 1975
- Equipment liquidated: November 1975

FINANCIAL OBLIGATIONS:
- All creditor payments suspended
- Player wages discontinued
- Federation fees unpaid
- Insurance policies lapsed

LEGAL STATUS:
- Corporate entity remained registered
- Directors resigned positions
- Shareholders meetings suspended
- Legal representation terminated

CONCLUSION:
The audit confirms complete cessation of operational activities during 1975-1976, with no evidence of continued sporting, financial, or administrative functions.

This represents a clear operational discontinuity that challenges claims of uninterrupted club operations.

Certified Public Accountant
Sports Industry Division""",
            "doc_type": "Financial Audit Report",
            "pages": 15
        }
    }
    
    for exhibit_id in fact['exhibits']:
        def find_evidence(args):
            for arg_key in args:
                arg = args[arg_key]
                if arg.get('evidence'):
                    evidence = next((e for e in arg['evidence'] if e['id'] == exhibit_id), None)
                    if evidence:
                        return evidence
                if arg.get('children'):
                    child_evidence = find_evidence(arg['children'])
                    if child_evidence:
                        return child_evidence
            return None
        
        evidence = find_evidence(args_data['claimantArgs']) or find_evidence(args_data['respondentArgs'])
        
        if evidence:
            evidence_item = {
                'id': exhibit_id,
                'title': evidence['title'],
                'summary': evidence['summary']
            }
            
            # Add preview content if available
            if exhibit_id in document_previews:
                evidence_item['preview'] = document_previews[exhibit_id]
            
            evidence_content.append(evidence_item)
        else:
            evidence_content.append({
                'id': exhibit_id,
                'title': exhibit_id,
                'summary': 'Evidence details not available'
            })
    
    return evidence_content

def copy_text_to_clipboard(text):
    """Helper function to generate safe JavaScript for copying text"""
    # Clean text for safe JavaScript insertion
    safe_text = text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\r')
    
    js_code = f"""
    <script>
    function copyText() {{
        const text = "{safe_text}";
        if (navigator.clipboard && window.isSecureContext) {{
            navigator.clipboard.writeText(text).then(function() {{
                console.log('Text copied successfully');
            }}).catch(function(err) {{
                console.error('Copy failed: ', err);
            }});
        }} else {{
            const textArea = document.createElement('textarea');
            textArea.value = text;
            textArea.style.position = 'fixed';
            textArea.style.left = '-999999px';
            textArea.style.top = '-999999px';
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();
            try {{
                document.execCommand('copy');
                console.log('Text copied using fallback');
            }} catch (err) {{
                console.error('Fallback copy failed: ', err);
            }}
            document.body.removeChild(textArea);
        }}
    }}
    copyText();
    </script>
    """
    return js_code

def download_text_file(content, filename):
    """Helper function to generate safe JavaScript for downloading files"""
    # Clean content for safe JavaScript insertion
    safe_content = content.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\r')
    
    js_code = f"""
    <script>
    function downloadFile() {{
        const content = "{safe_content}";
        const filename = "{filename}";
        const blob = new Blob([content], {{ type: 'text/plain' }});
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    }}
    downloadFile();
    </script>
    """
    return js_code

def render_streamlit_card_view(filtered_facts=None):
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("No facts found matching the selected criteria.")
        return
    
    for i, fact in enumerate(facts_data):
        expander_title = f"**{fact['date']}** - {fact['event']}"
        if fact['isDisputed']:
            expander_title += " 🔴"
        
        with st.expander(expander_title, expanded=False):
            st.markdown("#### Evidence & Source References")
            evidence_content = get_evidence_content(fact)
            
            if evidence_content:
                for evidence in evidence_content:
                    with st.container():
                        st.markdown(f"**{evidence['id']}** - {evidence['title']}")
                        
                        if fact.get('doc_summary'):
                            st.info(f"**Document Summary:** {fact['doc_summary']}")
                        
                        if fact.get('source_text'):
                            st.markdown(f"**Source Text:** *{fact['source_text']}*")
                        
                        # Action buttons row - Preview first, Copy last
                        col1, col2, col3 = st.columns([3, 1, 1])
                        with col1:
                            ref_text = f"**Exhibit:** {evidence['id']}"
                            if fact.get('page'):
                                ref_text += f" | **Page:** {fact['page']}"
                            if fact.get('paragraphs'):
                                ref_text += f" | **Paragraphs:** {fact['paragraphs']}"
                            st.markdown(ref_text)
                        
                        with col2:
                            if evidence.get('preview'):
                                current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                                preview_key = f"preview_card_{evidence['id']}_{i}_{current_tab}"
                                preview_state_key = f"show_{preview_key}"
                                
                                if st.button("👁️", key=preview_key, help="Preview Document", use_container_width=True):
                                    # Toggle preview state
                                    if preview_state_key not in st.session_state:
                                        st.session_state[preview_state_key] = True
                                    else:
                                        st.session_state[preview_state_key] = not st.session_state[preview_state_key]
                        
                        with col3:
                            current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                            copy_key = f"copy_card_{evidence['id']}_{i}_{current_tab}"
                            
                            if st.button("📋", key=copy_key, help="Copy Reference", use_container_width=True):
                                # Prepare reference text
                                ref_copy = f"Exhibit: {evidence['id']}"
                                if fact.get('page'):
                                    ref_copy += f", Page: {fact['page']}"
                                if fact.get('paragraphs'):
                                    ref_copy += f", Paragraphs: {fact['paragraphs']}"
                                
                                # Use helper function for safe copying
                                components.html(copy_text_to_clipboard(ref_copy), height=0)
                                st.success("Reference copied!")
                        
                        # Show preview if toggled on - appears as separate section
                        current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                        preview_state_key = f"show_preview_card_{evidence['id']}_{i}_{current_tab}"
                        if evidence.get('preview') and st.session_state.get(preview_state_key, False):
                            preview_data = evidence['preview']
                            
                            # Create a modal-like preview
                            with st.container():
                                st.markdown("---")
                                st.markdown(f"### 📄 Document Preview: {evidence['id']}")
                                st.markdown(f"**{preview_data['doc_type']}** • {preview_data['pages']} page(s)")
                                
                                # Preview content in a styled container
                                st.markdown(f"""
                                <div style="
                                    background: white;
                                    padding: 20px; 
                                    border-radius: 8px;
                                    font-family: 'Courier New', monospace; 
                                    font-size: 12px; 
                                    line-height: 1.6; 
                                    white-space: pre-wrap;
                                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                                    max-height: 400px;
                                    overflow-y: auto;
                                    border: 1px solid #ddd;
                                ">
                                {preview_data['content']}
                                </div>
                                """, unsafe_allow_html=True)
                                
                                if st.button("❌ Close Preview", key=f"close_preview_card_{evidence['id']}_{i}_{current_tab}"):
                                    st.session_state[preview_state_key] = False
                                    st.rerun()
                                st.markdown("---")
                        
                        st.markdown("---")
            else:
                st.markdown("*No evidence references available for this fact*")
            
            st.subheader("⚖️ Party Submissions")
            
            st.markdown("**🔵 Claimant Submission**")
            claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
            if claimant_text == 'No specific submission recorded':
                st.markdown("*No submission provided*")
            else:
                st.info(claimant_text)
            
            st.markdown("**🔴 Respondent Submission**")
            respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
            if respondent_text == 'No specific submission recorded':
                st.markdown("*No submission provided*")
            else:
                st.warning(respondent_text)
            
            st.subheader("📊 Status")
            status_col1, status_col2 = st.columns(2)
            
            with status_col1:
                if fact['isDisputed']:
                    st.error("**Status:** Disputed")
                else:
                    st.success("**Status:** Undisputed")
            
            with status_col2:
                if fact.get('parties_involved'):
                    st.markdown(f"**Parties:** {', '.join(fact['parties_involved'])}")

def render_streamlit_table_view(filtered_facts=None):
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
    
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    if not facts_data:
        st.info("No facts found matching the selected criteria.")
        return
    
    table_data = []
    for fact in facts_data:
        table_data.append({
            'Date': fact['date'],
            'Event': fact['event'],
            'Status': '🔴 Disputed' if fact['isDisputed'] else '🟢 Undisputed',
            'Parties': ', '.join(fact.get('parties_involved', [])),
            'Exhibits': ', '.join(fact.get('exhibits', [])),
            'Page': fact.get('page', ''),
            'Document': fact.get('doc_name', '')
        })
    
    df = pd.DataFrame(table_data)
    
    st.dataframe(
        df,
        use_container_width=True,
        height=600,
        column_config={
            'Date': st.column_config.TextColumn('Date', width=120),
            'Event': st.column_config.TextColumn('Event', width=300),
            'Status': st.column_config.TextColumn('Status', width=120),
            'Parties': st.column_config.TextColumn('Parties', width=150),
            'Exhibits': st.column_config.TextColumn('Exhibits', width=120),
            'Page': st.column_config.TextColumn('Page', width=80),
            'Document': st.column_config.TextColumn('Document', width=200)
        }
    )

def render_streamlit_docset_view(filtered_facts=None):
    if filtered_facts is None:
        facts_data = get_all_facts()
    else:
        facts_data = filtered_facts
        
    document_sets = get_document_sets()
    facts_data.sort(key=lambda x: x['date'].split('-')[0])
    
    docs_with_facts = {}
    
    for ds in document_sets:
        if ds.get('isGroup'):
            docs_with_facts[ds['id']] = {
                'docset': ds,
                'facts': []
            }
    
    for fact in facts_data:
        fact_assigned = False
        
        for ds in document_sets:
            if ds.get('isGroup'):
                for doc in ds.get('documents', []):
                    if fact.get('source') and doc['id'] + '.' in fact['source']:
                        docs_with_facts[ds['id']]['facts'].append({
                            **fact,
                            'documentName': doc['name']
                        })
                        fact_assigned = True
                        break
                if fact_assigned:
                    break
        
        if not fact_assigned:
            for ds in document_sets:
                if ds.get('isGroup'):
                    for doc in ds.get('documents', []):
                        parties = fact.get('parties_involved', [])
                        if (doc['party'] == 'Mixed' or 
                            (doc['party'] == 'Appellant' and 'Appellant' in parties) or
                            (doc['party'] == 'Respondent' and 'Respondent' in parties)):
                            docs_with_facts[ds['id']]['facts'].append({
                                **fact,
                                'documentName': doc['name']
                            })
                            fact_assigned = True
                            break
                    if fact_assigned:
                        break
    
    for docset_id, doc_with_facts in docs_with_facts.items():
        docset = doc_with_facts['docset']
        facts = doc_with_facts['facts']
        
        party_color = ("🔵" if docset['party'] == 'Appellant' else 
                      "🔴" if docset['party'] == 'Respondent' else "⚪")
        
        with st.expander(f"📁 {party_color} **{docset['name']}** ({len(facts)} facts)", expanded=False):
            if facts:
                for i, fact in enumerate(facts):
                    with st.container():
                        col1, col2, col3 = st.columns([2, 4, 1])
                        
                        with col1:
                            st.markdown(f"**{fact['date']}**")
                        
                        with col2:
                            st.markdown(f"**{fact['event']}**")
                        
                        with col3:
                            if fact['isDisputed']:
                                st.error("🔴")
                            else:
                                st.success("🟢")
                        
                        with st.container():
                            st.markdown("#### Evidence & Source References")
                            evidence_content = get_evidence_content(fact)
                            
                            if evidence_content:
                                for evidence_idx, evidence in enumerate(evidence_content):
                                    with st.container():
                                        st.markdown(f"**{evidence['id']}** - {evidence['title']}")
                                        
                                        if fact.get('doc_summary'):
                                            st.info(f"**Document Summary:** {fact['doc_summary']}")
                                        
                                        if fact.get('source_text'):
                                            st.markdown(f"**Source Text:** *{fact['source_text']}*")
                                        
                                        # Action buttons row - Preview first, Copy last
                                        col1, col2, col3 = st.columns([3, 1, 1])
                                        with col1:
                                            ref_text = f"**Exhibit:** {evidence['id']}"
                                            if fact.get('page'):
                                                ref_text += f" | **Page:** {fact['page']}"
                                            if fact.get('paragraphs'):
                                                ref_text += f" | **Paragraphs:** {fact['paragraphs']}"
                                            st.markdown(ref_text)
                                        
                                        with col2:
                                            if evidence.get('preview'):
                                                current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                                                preview_key = f"preview_docset_{docset_id}_{i}_{evidence_idx}_{evidence['id']}_{current_tab}"
                                                preview_state_key = f"show_{preview_key}"
                                                
                                                if st.button("👁️", key=preview_key, help="Preview Document", use_container_width=True):
                                                    # Toggle preview state
                                                    if preview_state_key not in st.session_state:
                                                        st.session_state[preview_state_key] = True
                                                    else:
                                                        st.session_state[preview_state_key] = not st.session_state[preview_state_key]
                                        
                                        with col3:
                                            current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                                            unique_key = f"copy_docset_{docset_id}_{i}_{evidence_idx}_{evidence['id']}_{current_tab}"
                                            
                                            if st.button("📋", key=unique_key, help="Copy Reference", use_container_width=True):
                                                # Prepare reference text
                                                ref_copy = f"Exhibit: {evidence['id']}"
                                                if fact.get('page'):
                                                    ref_copy += f", Page: {fact['page']}"
                                                if fact.get('paragraphs'):
                                                    ref_copy += f", Paragraphs: {fact['paragraphs']}"
                                                
                                                # Use helper function for safe copying
                                                components.html(copy_text_to_clipboard(ref_copy), height=0)
                                                st.success("Reference copied!")
                                        
                                        # Show preview if toggled on - appears as separate section
                                        current_tab = getattr(st.session_state, 'current_tab_type', 'all')
                                        preview_state_key = f"show_preview_docset_{docset_id}_{i}_{evidence_idx}_{evidence['id']}_{current_tab}"
                                        if evidence.get('preview') and st.session_state.get(preview_state_key, False):
                                            preview_data = evidence['preview']
                                            
                                            # Create a modal-like preview
                                            with st.container():
                                                st.markdown("---")
                                                st.markdown(f"### 📄 Document Preview: {evidence['id']}")
                                                st.markdown(f"**{preview_data['doc_type']}** • {preview_data['pages']} page(s)")
                                                
                                                # Preview content in a styled container
                                                st.markdown(f"""
                                                <div style="
                                                    background: white;
                                                    padding: 20px; 
                                                    border-radius: 8px;
                                                    font-family: 'Courier New', monospace; 
                                                    font-size: 12px; 
                                                    line-height: 1.6; 
                                                    white-space: pre-wrap;
                                                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                                                    max-height: 400px;
                                                    overflow-y: auto;
                                                    border: 1px solid #ddd;
                                                ">
                                                {preview_data['content']}
                                                </div>
                                                """, unsafe_allow_html=True)
                                                
                                                close_key = f"close_preview_docset_{docset_id}_{i}_{evidence_idx}_{evidence['id']}_{current_tab}"
                                                if st.button("❌ Close Preview", key=close_key):
                                                    st.session_state[preview_state_key] = False
                                                    st.rerun()
                                                st.markdown("---")
                                        
                                        st.markdown("---")
                            else:
                                st.markdown("*No evidence references available*")
                            
                            st.markdown("**⚖️ Party Submissions**")
                            
                            st.markdown("**🔵 Claimant Submission**")
                            claimant_text = fact.get('claimant_submission', 'No specific submission recorded')
                            if claimant_text == 'No specific submission recorded':
                                st.markdown("*No submission provided*")
                            else:
                                st.info(claimant_text)
                            
                            st.markdown("**🔴 Respondent Submission**")
                            respondent_text = fact.get('respondent_submission', 'No specific submission recorded')
                            if respondent_text == 'No specific submission recorded':
                                st.markdown("*No submission provided*")
                            else:
                                st.warning(respondent_text)
                        
                        if i < len(facts) - 1:
                            st.divider()
            else:
                st.info("No facts found in this document category.")

def render_view_content(view_type, filtered_facts):
    if view_type == "card":
        render_streamlit_card_view(filtered_facts)
    elif view_type == "table":
        render_streamlit_table_view(filtered_facts)
    elif view_type == "docset":
        render_streamlit_docset_view(filtered_facts)
    else:
        render_streamlit_card_view(filtered_facts)

def main():
    # Add Streamlit sidebar with navigation buttons
    with st.sidebar:
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
              <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#whatsapp-mask)">
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <h1 style="margin-left: 10px; font-weight: 600; color: #4D68F9;">CaseLens</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
        
        # Custom CSS for sidebar button styling
        st.markdown("""
        <style>
        .stButton > button {
            width: 100%;
            border-radius: 6px;
            height: 50px;
            margin-bottom: 10px;
            transition: all 0.3s;
        }
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)
        
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
    
    # Create the facts view
    if st.session_state.view == "Facts":
        # Add global CSS for small buttons
        st.markdown("""
        <style>
        /* Very small compact buttons */
        div[data-testid="column"] button[title*="Copy Reference"],
        div[data-testid="column"] button[title*="Preview Document"] {
            height: 22px !important;
            padding: 2px 6px !important;
            font-size: 14px !important;
            min-width: auto !important;
            border-radius: 3px !important;
            margin: 1px !important;
        }
        
        /* Custom styling for preview button */
        .preview-btn {
            background: #f0f8ff !important;
            border: 1px solid #4a90e2 !important;
            color: #4a90e2 !important;
        }
        
        .preview-btn:hover {
            background: #e6f3ff !important;
            border: 1px solid #357abd !important;
        }
        
        /* Custom styling for copy button */
        .copy-btn {
            background: #f9f9f9 !important;
            border: 1px solid #999 !important;
            color: #333 !important;
        }
        
        .copy-btn:hover {
            background: #f0f0f0 !important;
            border: 1px solid #666 !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Header with title and action buttons
        col_title, col_copy, col_export = st.columns([3, 1, 1])
        
        with col_title:
            st.title("Case Facts")
        
        with col_copy:
            if st.button("📋 Copy", use_container_width=True, type="secondary", key="header_copy_btn"):
                # Get all facts for copying
                all_facts = get_all_facts()
                
                # Create formatted text for copying - build as list for safety
                copy_lines = []
                copy_lines.append("CASE FACTS SUMMARY")
                copy_lines.append("=" * 50)
                copy_lines.append("")
                
                for fact in all_facts:
                    copy_lines.append(f"Date: {fact['date']}")
                    copy_lines.append(f"Event: {fact['event']}")
                    copy_lines.append(f"Status: {'Disputed' if fact['isDisputed'] else 'Undisputed'}")
                    copy_lines.append(f"Exhibits: {', '.join(fact.get('exhibits', []))}")
                    copy_lines.append(f"Document: {fact.get('doc_name', 'N/A')}")
                    if fact.get('page'):
                        copy_lines.append(f"Page: {fact['page']}")
                    # Clean and add source text
                    source_text = str(fact.get('source_text', 'N/A')).replace('\n', ' ').replace('\r', ' ')
                    copy_lines.append(f"Source: {source_text}")
                    copy_lines.append("-" * 30)
                    copy_lines.append("")
                
                copy_text = '\n'.join(copy_lines)
                
                # Use helper function for safe copying
                components.html(copy_text_to_clipboard(copy_text), height=0)
                st.success("Facts copied to clipboard!")
        
        with col_export:
            if st.button("📥 Export", use_container_width=True, type="secondary", key="header_export_btn"):
                # Get all facts for export
                all_facts = get_all_facts()
                
                # Create detailed export content as list for safety
                export_lines = []
                export_lines.append("LEGAL CASE FACTS - DETAILED EXPORT")
                export_lines.append(f"Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
                export_lines.append("=" * 60)
                export_lines.append("")
                
                # Add summary statistics
                total_facts = len(all_facts)
                disputed_facts = len([f for f in all_facts if f['isDisputed']])
                undisputed_facts = total_facts - disputed_facts
                
                export_lines.append("SUMMARY STATISTICS:")
                export_lines.append(f"Total Facts: {total_facts}")
                export_lines.append(f"Disputed Facts: {disputed_facts}")
                export_lines.append(f"Undisputed Facts: {undisputed_facts}")
                export_lines.append("")
                export_lines.append("=" * 60)
                export_lines.append("")
                
                # Add detailed facts
                for i, fact in enumerate(all_facts, 1):
                    export_lines.append(f"FACT #{i}")
                    export_lines.append(f"Date: {fact['date']}")
                    export_lines.append(f"Event: {fact['event']}")
                    export_lines.append(f"Status: {'DISPUTED' if fact['isDisputed'] else 'UNDISPUTED'}")
                    export_lines.append(f"Parties Involved: {', '.join(fact.get('parties_involved', []))}")
                    export_lines.append(f"Exhibits: {', '.join(fact.get('exhibits', []))}")
                    export_lines.append(f"Document: {fact.get('doc_name', 'N/A')}")
                    export_lines.append(f"Page: {fact.get('page', 'N/A')}")
                    export_lines.append(f"Paragraphs: {fact.get('paragraphs', 'N/A')}")
                    
                    # Clean text content
                    doc_summary = str(fact.get('doc_summary', 'N/A')).replace('\n', ' ').replace('\r', ' ')
                    export_lines.append(f"Document Summary: {doc_summary}")
                    export_lines.append("")
                    
                    source_text = str(fact.get('source_text', 'N/A')).replace('\n', ' ').replace('\r', ' ')
                    export_lines.append("SOURCE TEXT:")
                    export_lines.append(source_text)
                    export_lines.append("")
                    
                    claimant_sub = str(fact.get('claimant_submission', 'No submission recorded')).replace('\n', ' ').replace('\r', ' ')
                    export_lines.append("CLAIMANT SUBMISSION:")
                    export_lines.append(claimant_sub)
                    export_lines.append("")
                    
                    respondent_sub = str(fact.get('respondent_submission', 'No submission recorded')).replace('\n', ' ').replace('\r', ' ')
                    export_lines.append("RESPONDENT SUBMISSION:")
                    export_lines.append(respondent_sub)
                    export_lines.append("")
                    
                    export_lines.append("=" * 60)
                    export_lines.append("")
                
                export_content = '\n'.join(export_lines)
                filename = f"case_facts_export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt"
                
                # Use helper function for safe download
                components.html(download_text_file(export_content, filename), height=0)
                st.success(f"Facts exported as {filename}!")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Ultra-modern compact view selector component
        current_view = st.session_state.current_view_type
        
        view_selector_html = f"""
        <div class="view-selector-wrapper">
            <div class="view-selector-container">
                <div class="selector-background"></div>
                <div class="selector-track">
                    <div class="selector-thumb {'thumb-card' if current_view == 'card' else 'thumb-table' if current_view == 'table' else 'thumb-docset'}"></div>
                </div>
                <button class="view-btn {'active' if current_view == 'card' else ''}" data-view="card">
                    <span class="btn-icon">📋</span>
                    <span class="btn-text">Cards</span>
                </button>
                <button class="view-btn {'active' if current_view == 'table' else ''}" data-view="table">
                    <span class="btn-icon">📊</span>
                    <span class="btn-text">Table</span>
                </button>
                <button class="view-btn {'active' if current_view == 'docset' else ''}" data-view="docset">
                    <span class="btn-icon">📁</span>
                    <span class="btn-text">Docs</span>
                </button>
            </div>
        </div>

        <style>
        .view-selector-wrapper {{
            display: flex;
            justify-content: center;
            margin: 20px 0 30px 0;
            user-select: none;
        }}

        .view-selector-container {{
            position: relative;
            display: inline-flex;
            background: linear-gradient(145deg, #f8fafc 0%, #f1f5f9 100%);
            border-radius: 16px;
            padding: 4px;
            box-shadow: 
                0 4px 12px rgba(0, 0, 0, 0.08),
                0 2px 4px rgba(0, 0, 0, 0.05),
                inset 0 1px 0 rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(226, 232, 240, 0.8);
            backdrop-filter: blur(10px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .view-selector-container:hover {{
            box-shadow: 
                0 6px 16px rgba(0, 0, 0, 0.12),
                0 3px 6px rgba(0, 0, 0, 0.08),
                inset 0 1px 0 rgba(255, 255, 255, 0.9);
            transform: translateY(-1px);
        }}

        .selector-track {{
            position: absolute;
            top: 4px;
            left: 4px;
            right: 4px;
            bottom: 4px;
            pointer-events: none;
        }}

        .selector-thumb {{
            position: absolute;
            height: 100%;
            background: linear-gradient(145deg, #ef4444 0%, #dc2626 100%);
            border-radius: 12px;
            box-shadow: 
                0 3px 8px rgba(239, 68, 68, 0.3),
                0 1px 3px rgba(239, 68, 68, 0.2),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            border: 1px solid rgba(239, 68, 68, 0.3);
        }}

        .thumb-card {{
            left: 0;
            width: 80px;
        }}

        .thumb-table {{
            left: 84px;
            width: 80px;
        }}

        .thumb-docset {{
            left: 168px;
            width: 80px;
        }}

        .view-btn {{
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            background: transparent;
            border: none;
            padding: 10px 16px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            color: #64748b;
            width: 80px;
            height: 36px;
            z-index: 2;
            outline: none;
        }}

        .view-btn:hover {{
            color: #475569;
            transform: translateY(-1px);
        }}

        .view-btn.active {{
            color: white;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }}

        .view-btn.active:hover {{
            color: rgba(255, 255, 255, 0.95);
        }}

        .btn-icon {{
            font-size: 14px;
            opacity: 0.9;
            transition: all 0.3s ease;
        }}

        .btn-text {{
            font-size: 12px;
            letter-spacing: 0.5px;
            font-weight: 600;
        }}

        .view-btn:hover .btn-icon {{
            opacity: 1;
            transform: scale(1.1);
        }}

        .view-btn.active .btn-icon {{
            opacity: 1;
            transform: scale(1.05);
        }}

        /* Ripple effect */
        .view-btn::before {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }}

        .view-btn:active::before {{
            width: 80px;
            height: 80px;
        }}

        /* Glassmorphism effect */
        @supports (backdrop-filter: blur(10px)) {{
            .view-selector-container {{
                background: rgba(248, 250, 252, 0.8);
                backdrop-filter: blur(10px);
            }}
        }}

        /* Dark mode support */
        @media (prefers-color-scheme: dark) {{
            .view-selector-container {{
                background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%);
                border: 1px solid rgba(71, 85, 105, 0.3);
            }}
            
            .view-btn {{
                color: #94a3b8;
            }}
            
            .view-btn:hover {{
                color: #cbd5e1;
            }}
        }}

        /* Accessibility improvements */
        .view-btn:focus {{
            outline: 2px solid #3b82f6;
            outline-offset: 2px;
        }}

        /* Mobile optimizations */
        @media (max-width: 640px) {{
            .view-selector-container {{
                transform: scale(0.9);
            }}
        }}
        </style>

        <script>
        (function() {{
            let isAnimating = false;
            const buttons = document.querySelectorAll('.view-btn');
            
            buttons.forEach(button => {{
                button.addEventListener('click', function(e) {{
                    if (isAnimating) return;
                    
                    e.preventDefault();
                    const viewType = this.dataset.view;
                    
                    // Visual feedback
                    this.style.transform = 'translateY(-1px) scale(0.98)';
                    setTimeout(() => {{
                        if (this.style) {{
                            this.style.transform = '';
                        }}
                    }}, 150);
                    
                    // Prevent rapid clicking
                    isAnimating = true;
                    setTimeout(() => {{ isAnimating = false; }}, 500);
                    
                    // Trigger state change
                    const customEvent = new CustomEvent('streamlit:view-change', {{
                        detail: {{ viewType }},
                        bubbles: true
                    }});
                    
                    window.dispatchEvent(customEvent);
                    
                    // Fallback for iframe
                    if (window.parent && window.parent !== window) {{
                        window.parent.postMessage({{
                            type: 'streamlit:view-change',
                            viewType: viewType,
                            timestamp: Date.now()
                        }}, '*');
                    }}
                }});
                
                // Accessibility: keyboard support
                button.addEventListener('keydown', function(e) {{
                    if (e.key === 'Enter' || e.key === ' ') {{
                        e.preventDefault();
                        this.click();
                    }}
                }});
            }});
            
            // Add hover sound effect (optional)
            buttons.forEach(button => {{
                button.addEventListener('mouseenter', function() {{
                    // Could add a subtle sound effect here
                }});
            }});
        }})();
        </script>
        """
        
        # Render the enhanced custom component
        components.html(view_selector_html, height=80)
        
        # Enhanced hidden buttons for state management
        st.markdown("""
        <style>
        .hidden-state-manager {
            position: absolute;
            left: -9999px;
            opacity: 0;
            pointer-events: none;
        }
        </style>
        """, unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="hidden-state-manager">', unsafe_allow_html=True)
            
            # Use columns but make them truly hidden
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("🔄 Card", key="enhanced_card_btn", help="Switch to card view"):
                    st.session_state.current_view_type = "card"
                    st.rerun()
            
            with col2:
                if st.button("🔄 Table", key="enhanced_table_btn", help="Switch to table view"):
                    st.session_state.current_view_type = "table" 
                    st.rerun()
            
            with col3:
                if st.button("🔄 Docs", key="enhanced_docset_btn", help="Switch to document view"):
                    st.session_state.current_view_type = "docset"
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Enhanced JavaScript bridge with better error handling
        st.markdown("""
        <script>
        (function() {
            const BUTTON_SELECTORS = {
                'card': 'button[data-testid*="enhanced_card_btn"]',
                'table': 'button[data-testid*="enhanced_table_btn"]', 
                'docset': 'button[data-testid*="enhanced_docset_btn"]'
            };
            
            let lastEventTime = 0;
            
            function handleViewChange(viewType) {
                const now = Date.now();
                if (now - lastEventTime < 300) return; // Debounce
                lastEventTime = now;
                
                const button = document.querySelector(BUTTON_SELECTORS[viewType]);
                if (button && typeof button.click === 'function') {
                    try {
                        button.click();
                    } catch (error) {
                        console.warn('Button click failed:', error);
                    }
                }
            }
            
            // Enhanced event listener for custom events
            window.addEventListener('streamlit:view-change', function(e) {
                if (e.detail && e.detail.viewType) {
                    handleViewChange(e.detail.viewType);
                }
            }, { passive: true });
            
            // Enhanced postMessage listener with validation
            window.addEventListener('message', function(e) {
                if (e.data && 
                    e.data.type === 'streamlit:view-change' && 
                    e.data.viewType &&
                    BUTTON_SELECTORS[e.data.viewType]) {
                    handleViewChange(e.data.viewType);
                }
            }, { passive: true });
            
            // Cleanup on page unload
            window.addEventListener('beforeunload', function() {
                // Clean up any pending operations
            });
        })();
        </script>
        """, unsafe_allow_html=True)
        
        # Facts filter using tabs
        tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
        
        with tab1:
            st.session_state.current_tab_type = "all"
            filtered_facts = get_all_facts()
            render_view_content(st.session_state.current_view_type, filtered_facts)
        
        with tab2:
            st.session_state.current_tab_type = "disputed"
            filtered_facts = [fact for fact in get_all_facts() if fact['isDisputed']]
            render_view_content(st.session_state.current_view_type, filtered_facts)
        
        with tab3:
            st.session_state.current_tab_type = "undisputed"
            filtered_facts = [fact for fact in get_all_facts() if not fact['isDisputed']]
            render_view_content(st.session_state.current_view_type, filtered_facts)

if __name__ == "__main__":
    main()
