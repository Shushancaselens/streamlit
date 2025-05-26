import streamlit as st
import streamlit.components.v1 as components
import json

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view and current view type
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'current_view_type' not in st.session_state:
    st.session_state.current_view_type = "card"
if 'current_tab_type' not in st.session_state:
    st.session_state.current_tab_type = "all"

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
            "children": {
                "1.1": {
                    "id": "1.1",
                    "title": "Club Name Analysis",
                    "paragraphs": "20-45",
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
                            ]
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
            ]
        }
    }
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args
    }

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

# Get the data
args_data = get_argument_data()
document_sets = get_document_sets()

# Add Streamlit sidebar with navigation buttons (EXACTLY like original)
with st.sidebar:
    # Add the logo and CaseLens text (EXACTLY like original)
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
          <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
            <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
          </mask>
          <g mask="url(#whatsapp-mask)">
            <!-- Rounded square background -->
            <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
            <!-- WhatsApp phone icon -->
            <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
          </g>
        </svg>
        <h1 style="margin-left: 10px; font-weight: 600; color: #4D68F9;">CaseLens</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
    
    # Custom CSS for button styling (EXACTLY like original)
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
    
    # Define button click handlers (EXACTLY like original)
    def set_arguments_view():
        st.session_state.view = "Arguments"
        
    def set_facts_view():
        st.session_state.view = "Facts"
        
    def set_exhibits_view():
        st.session_state.view = "Exhibits"
    
    # Create buttons with names (EXACTLY like original)
    st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
    st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
    st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)

# Only show Facts view content (since that's what we're implementing)
if st.session_state.view == "Facts":
    # Enhanced header section with better organization
    st.title("📊 Case Facts Analysis")
    st.markdown("**Comprehensive overview of factual assertions, evidence, and party submissions**")
    
    # Improved section with better visual hierarchy
    st.markdown("---")
    
    # View Selection Section with descriptions
    st.markdown("### 🔍 **View Options**")
    st.markdown("*Choose how you want to explore the case facts:*")
    
    # Enhanced view toggle buttons with descriptions
    view_col1, view_col2, view_col3 = st.columns(3)
    
    with view_col1:
        card_active = st.session_state.current_view_type == "card"
        if st.button("📋 **Card View**", use_container_width=True, 
                    type="primary" if card_active else "secondary", key="card_btn"):
            st.session_state.current_view_type = "card"
            st.rerun()
        if card_active:
            st.markdown("*<small>📄 Detailed expandable cards with full evidence and submissions</small>*", unsafe_allow_html=True)
    
    with view_col2:
        timeline_active = st.session_state.current_view_type == "timeline"
        if st.button("📅 **Timeline View**", use_container_width=True,
                    type="primary" if timeline_active else "secondary", key="timeline_btn"):
            st.session_state.current_view_type = "timeline"
            st.rerun()
        if timeline_active:
            st.markdown("*<small>⏰ Chronological sequence of events grouped by year</small>*", unsafe_allow_html=True)
    
    with view_col3:
        docset_active = st.session_state.current_view_type == "docset"
        if st.button("📁 **Document Categories**", use_container_width=True,
                    type="primary" if docset_active else "secondary", key="docset_btn"):
            st.session_state.current_view_type = "docset"
            st.rerun()
        if docset_active:
            st.markdown("*<small>📂 Facts organized by document sets and party submissions</small>*", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Filter Section with enhanced UI
    st.markdown("### 🎯 **Fact Filtering**")
    
    filter_col1, filter_col2 = st.columns([1, 2])
    
    with filter_col1:
        filter_option = st.selectbox(
            "**Show Facts:**",
            ["All Facts", "Disputed Facts", "Undisputed Facts"],
            index=0,
            help="Filter facts based on whether they are disputed between parties"
        )
    
    with filter_col2:
        # Add summary stats
        if filter_option == "All Facts":
            st.session_state.current_tab_type = "all"
            st.info("📊 **Showing all factual assertions** from both parties")
        elif filter_option == "Disputed Facts":
            st.session_state.current_tab_type = "disputed"
            st.warning("⚠️ **Showing contested facts** where parties disagree")
        else:
            st.session_state.current_tab_type = "undisputed"
            st.success("✅ **Showing agreed facts** accepted by both parties")
    
    st.markdown("---")
    
    # Enhanced content section header
    view_type_labels = {
        "card": "📋 Card View",
        "timeline": "📅 Timeline View", 
        "docset": "📁 Document Categories"
    }
    
    filter_labels = {
        "all": "All Facts",
        "disputed": "Disputed Facts",
        "undisputed": "Undisputed Facts"
    }
    
    current_view_label = view_type_labels.get(st.session_state.current_view_type, "Card View")
    current_filter_label = filter_labels.get(st.session_state.current_tab_type, "All Facts")
    
    st.markdown(f"### 📋 **{current_view_label}** - *{current_filter_label}*")
    
    # Add instructional text based on view type
    if st.session_state.current_view_type == "card":
        st.markdown("*Click on any fact card below to expand and view detailed evidence, source references, and party submissions.*")
    elif st.session_state.current_view_type == "timeline":
        st.markdown("*Facts are displayed chronologically, grouped by year. Each event shows the date, evidence, and both parties' positions.*")
    else:
        st.markdown("*Facts are organized by document categories. Click on each category to expand and view the facts from those documents.*")
    
    # Now render the React component for the main content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CaseLens Facts View</title>
        <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
        <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        <style>
            body {{
                margin: 0;
                font-family: "Source Sans Pro", sans-serif;
                background-color: #ffffff;
                color: #262730;
                line-height: 1.6;
            }}
            
            .main-content {{
                padding: 0;
            }}
            
            /* Enhanced Fact Cards */
            .fact-card {{
                border: 1px solid #e1e5e9;
                border-radius: 8px;
                margin-bottom: 1.5rem;
                overflow: hidden;
                background-color: white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.08);
                transition: all 0.3s ease;
            }}
            
            .fact-card:hover {{
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                transform: translateY(-2px);
            }}
            
            .fact-header {{
                padding: 1.25rem;
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #e1e5e9;
                transition: all 0.2s ease;
                position: relative;
            }}
            
            .fact-header:hover {{
                background: linear-gradient(135deg, #e9ecef 0%, #dee2e6 100%);
            }}
            
            .fact-header::after {{
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #4D68F9, #ff6900);
                opacity: 0;
                transition: opacity 0.3s ease;
            }}
            
            .fact-card:hover .fact-header::after {{
                opacity: 1;
            }}
            
            .fact-title {{
                font-weight: 600;
                color: #262730;
                font-size: 1.05rem;
                display: flex;
                align-items: center;
                flex: 1;
            }}
            
            .fact-date {{
                background: #4D68F9;
                color: white;
                padding: 0.25rem 0.75rem;
                border-radius: 20px;
                font-size: 0.85rem;
                font-weight: 600;
                margin-right: 1rem;
                min-width: fit-content;
            }}
            
            .dispute-indicator {{
                width: 16px;
                height: 16px;
                border-radius: 50%;
                background-color: #dc3545;
                border: 2px solid white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                position: relative;
            }}
            
            .dispute-indicator.undisputed {{
                background-color: #28a745;
            }}
            
            .dispute-indicator::after {{
                content: '';
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 6px;
                height: 6px;
                background: white;
                border-radius: 50%;
            }}
            
            .fact-content {{
                padding: 0;
                display: none;
                animation: slideDown 0.3s ease-out;
            }}
            
            .fact-content.expanded {{
                display: block;
            }}
            
            @keyframes slideDown {{
                from {{
                    opacity: 0;
                    max-height: 0;
                }}
                to {{
                    opacity: 1;
                    max-height: 1000px;
                }}
            }}
            
            .content-inner {{
                padding: 1.5rem;
            }}
            
            /* Enhanced Section Headers */
            .section-header {{
                font-size: 1.2rem;
                font-weight: 700;
                margin: 2rem 0 1rem 0;
                color: #262730;
                display: flex;
                align-items: center;
                padding-bottom: 0.5rem;
                border-bottom: 2px solid #e1e5e9;
            }}
            
            .section-header:first-child {{
                margin-top: 0;
            }}
            
            /* Enhanced Evidence Items */
            .evidence-item {{
                margin-bottom: 1.5rem;
                padding: 1.25rem;
                background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
                border-radius: 8px;
                border: 1px solid #e1e5e9;
                border-left: 4px solid #4D68F9;
                transition: all 0.2s ease;
            }}
            
            .evidence-item:hover {{
                border-left-color: #ff6900;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            
            .evidence-title {{
                font-weight: 700;
                margin-bottom: 0.75rem;
                color: #262730;
                font-size: 1.05rem;
            }}
            
            .document-summary {{
                margin: 0.75rem 0;
                padding: 1rem;
                background: linear-gradient(135deg, #cce5ff 0%, #b3d9ff 100%);
                border-radius: 6px;
                border: 1px solid #99ccff;
                border-left: 4px solid #4D68F9;
            }}
            
            .source-text {{
                margin: 0.75rem 0;
                padding: 1rem;
                background: #f8f9fa;
                border-radius: 6px;
                border-left: 4px solid #6c757d;
                font-style: italic;
                font-size: 0.95rem;
                line-height: 1.6;
            }}
            
            /* Enhanced Submissions */
            .submission-section {{
                margin: 1.5rem 0;
            }}
            
            .submission-header {{
                font-weight: 700;
                margin-bottom: 0.75rem;
                font-size: 1.05rem;
                display: flex;
                align-items: center;
            }}
            
            .submission-content {{
                padding: 1.25rem;
                border-radius: 8px;
                font-style: italic;
                border-left: 4px solid;
                line-height: 1.7;
                font-size: 0.95rem;
                position: relative;
                overflow: hidden;
            }}
            
            .submission-content::before {{
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                opacity: 0.05;
                background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23000000' fill-opacity='0.1'%3E%3Ccircle cx='7' cy='7' r='1'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            }}
            
            .claimant-submission {{
                background: linear-gradient(135deg, #cce5ff 0%, #e6f3ff 100%);
                border-left-color: #4D68F9;
                color: #1a365d;
            }}
            
            .respondent-submission {{
                background: linear-gradient(135deg, #ffe6e6 0%, #fff2f2 100%);
                border-left-color: #dc3545;
                color: #7a1e1e;
            }}
            
            /* Enhanced Status Section */
            .status-section {{
                display: flex;
                gap: 2rem;
                margin-top: 1.5rem;
                padding: 1.25rem;
                background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
                border-radius: 8px;
                border: 1px solid #e1e5e9;
            }}
            
            .status-item {{
                display: flex;
                align-items: center;
                gap: 0.75rem;
                font-weight: 600;
            }}
            
            /* Enhanced Copy Button */
            .copy-button {{
                padding: 0.5rem 1rem;
                background: linear-gradient(135deg, #6c757d 0%, #5a6268 100%);
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 0.85rem;
                font-weight: 600;
                transition: all 0.2s ease;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            
            .copy-button:hover {{
                background: linear-gradient(135deg, #5a6268 0%, #495057 100%);
                transform: translateY(-1px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }}
            
            .copy-button:active {{
                transform: translateY(0);
            }}
            
            /* Enhanced Timeline Styles */
            .timeline-year {{
                font-size: 2rem;
                font-weight: 700;
                margin: 3rem 0 1.5rem 0;
                color: #262730;
                display: flex;
                align-items: center;
                gap: 1rem;
                padding: 1rem 0;
                border-bottom: 3px solid #e1e5e9;
                position: relative;
            }}
            
            .timeline-year::after {{
                content: '';
                position: absolute;
                bottom: -3px;
                left: 0;
                width: 60px;
                height: 3px;
                background: linear-gradient(90deg, #4D68F9, #ff6900);
            }}
            
            .timeline-event {{
                margin-bottom: 2.5rem;
                padding: 1.5rem;
                border-left: 5px solid #ff6900;
                background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
                border-radius: 0 8px 8px 0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                transition: all 0.3s ease;
                position: relative;
            }}
            
            .timeline-event:hover {{
                border-left-color: #4D68F9;
                transform: translateX(5px);
                box-shadow: 0 4px 16px rgba(0,0,0,0.15);
            }}
            
            .timeline-event::before {{
                content: '';
                position: absolute;
                left: -8px;
                top: 1.5rem;
                width: 16px;
                height: 16px;
                background: #ff6900;
                border-radius: 50%;
                border: 3px solid white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            }}
            
            .timeline-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1.5rem;
                padding-bottom: 1rem;
                border-bottom: 1px solid #e1e5e9;
            }}
            
            .timeline-date {{
                font-weight: 700;
                color: #ff6900;
                font-size: 1.1rem;
                background: rgba(255, 105, 0, 0.1);
                padding: 0.5rem 1rem;
                border-radius: 20px;
            }}
            
            .timeline-title {{
                font-weight: 700;
                flex: 1;
                margin: 0 1.5rem;
                font-size: 1.1rem;
            }}
            
            /* Enhanced Document Categories */
            .docset-container {{
                margin-bottom: 2rem;
            }}
            
            .docset-header {{
                padding: 1.5rem;
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                cursor: pointer;
                border: 1px solid #e1e5e9;
                border-radius: 8px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                transition: all 0.2s ease;
                font-weight: 600;
                font-size: 1.1rem;
            }}
            
            .docset-header:hover {{
                background: linear-gradient(135deg, #e9ecef 0%, #dee2e6 100%);
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}
            
            .docset-content {{
                display: none;
                border: 1px solid #e1e5e9;
                border-top: none;
                border-radius: 0 0 8px 8px;
                padding: 1.5rem;
                background: white;
                animation: slideDown 0.3s ease-out;
            }}
            
            .docset-content.expanded {{
                display: block;
            }}
            
            /* Enhanced No Facts Message */
            .no-facts {{
                text-align: center;
                padding: 4rem 2rem;
                color: #6c757d;
                font-style: italic;
                font-size: 1.1rem;
                background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
                border-radius: 8px;
                border: 2px dashed #e1e5e9;
            }}
            
            .divider {{
                height: 1px;
                background: linear-gradient(90deg, transparent, #e1e5e9, transparent);
                margin: 1.5rem 0;
            }}
            
            /* Responsive Design */
            @media (max-width: 768px) {{
                .fact-header {{
                    flex-direction: column;
                    align-items: flex-start;
                    gap: 0.5rem;
                }}
                
                .timeline-header {{
                    flex-direction: column;
                    align-items: flex-start;
                    gap: 0.5rem;
                }}
                
                .status-section {{
                    flex-direction: column;
                    gap: 1rem;
                }}
            }}
        </style>
    </head>
    <body>
        <div id="root"></div>

        <script type="text/babel">
            const {{ useState }} = React;

            // Data
            const argumentData = {json.dumps(args_data)};
            const documentSets = {json.dumps(document_sets)};
            const currentViewType = "{st.session_state.current_view_type}";
            const currentTabType = "{st.session_state.current_tab_type}";

            // Utility functions (same as before)
            const extractFacts = (args, party) => {{
                const facts = [];
                
                const processArg = (arg) => {{
                    if (arg.factualPoints) {{
                        arg.factualPoints.forEach(point => {{
                            facts.push({{
                                event: point.point,
                                date: point.date,
                                isDisputed: point.isDisputed,
                                party: party,
                                paragraphs: point.paragraphs || '',
                                exhibits: point.exhibits || [],
                                argId: arg.id,
                                argTitle: arg.title,
                                source_text: point.source_text || '',
                                page: point.page || '',
                                doc_name: point.doc_name || '',
                                doc_summary: point.doc_summary || ''
                            }});
                        }});
                    }}
                    
                    if (arg.children) {{
                        Object.values(arg.children).forEach(processArg);
                    }}
                }};
                
                Object.values(args).forEach(processArg);
                return facts;
            }};

            const getAllFacts = () => {{
                const claimantFacts = extractFacts(argumentData.claimantArgs, 'Appellant');
                const respondentFacts = extractFacts(argumentData.respondentArgs, 'Respondent');
                
                const allFacts = [...claimantFacts, ...respondentFacts];
                const factGroups = {{}};
                
                allFacts.forEach(fact => {{
                    const key = `${{fact.date}}_${{fact.event.substring(0, 50)}}`;
                    if (!factGroups[key]) {{
                        factGroups[key] = {{
                            event: fact.event,
                            date: fact.date,
                            isDisputed: fact.isDisputed,
                            claimant_submission: '',
                            respondent_submission: '',
                            source_text: fact.source_text,
                            page: fact.page,
                            doc_name: fact.doc_name,
                            doc_summary: fact.doc_summary,
                            exhibits: fact.exhibits,
                            paragraphs: fact.paragraphs,
                            argId: fact.argId,
                            argTitle: fact.argTitle,
                            parties_involved: []
                        }};
                    }}
                    
                    if (fact.party === 'Appellant') {{
                        factGroups[key].claimant_submission = fact.source_text;
                    }} else {{
                        factGroups[key].respondent_submission = fact.source_text;
                    }}
                    
                    factGroups[key].parties_involved.push(fact.party);
                    
                    if (fact.isDisputed) {{
                        factGroups[key].isDisputed = true;
                    }}
                }});
                
                return Object.values(factGroups).map(group => ({{
                    ...group,
                    claimant_submission: group.claimant_submission || 'No specific submission recorded',
                    respondent_submission: group.respondent_submission || 'No specific submission recorded',
                    parties_involved: [...new Set(group.parties_involved)]
                }}));
            }};

            const getEvidenceContent = (fact) => {{
                if (!fact.exhibits || fact.exhibits.length === 0) {{
                    return [];
                }}
                
                const evidenceContent = [];
                
                const findEvidence = (args) => {{
                    for (const argKey in args) {{
                        const arg = args[argKey];
                        if (arg.evidence) {{
                            const evidence = arg.evidence.find(e => fact.exhibits.includes(e.id));
                            if (evidence) {{
                                evidenceContent.push({{
                                    id: evidence.id,
                                    title: evidence.title,
                                    summary: evidence.summary
                                }});
                            }}
                        }}
                        if (arg.children) {{
                            findEvidence(arg.children);
                        }}
                    }}
                }};
                
                findEvidence(argumentData.claimantArgs);
                findEvidence(argumentData.respondentArgs);
                
                fact.exhibits.forEach(exhibitId => {{
                    if (!evidenceContent.find(e => e.id === exhibitId)) {{
                        evidenceContent.push({{
                            id: exhibitId,
                            title: exhibitId,
                            summary: 'Evidence details not available'
                        }});
                    }}
                }});
                
                return evidenceContent;
            }};

            // Enhanced Components
            const FactCard = ({{ fact, index }}) => {{
                const [expanded, setExpanded] = useState(false);
                const evidenceContent = getEvidenceContent(fact);
                
                return (
                    <div className="fact-card">
                        <div className="fact-header" onClick={{() => setExpanded(!expanded)}}>
                            <div className="fact-title">
                                <span className="fact-date">{{fact.date}}</span>
                                {{fact.event}}
                            </div>
                            <div className={{`dispute-indicator ${{!fact.isDisputed ? 'undisputed' : ''}}`}} 
                                 title={{fact.isDisputed ? 'Disputed Fact' : 'Undisputed Fact'}}></div>
                        </div>
                        <div className={{`fact-content ${{expanded ? 'expanded' : ''}}`}}>
                            <div className="content-inner">
                                <div className="section-header">📁 Evidence & Source References</div>
                                {{evidenceContent.length > 0 ? (
                                    evidenceContent.map((evidence, idx) => (
                                        <div key={{idx}} className="evidence-item">
                                            <div className="evidence-title">
                                                📄 <strong>{{evidence.id}}</strong> - {{evidence.title}}
                                            </div>
                                            {{fact.doc_summary && (
                                                <div className="document-summary">
                                                    <strong>📋 Document Summary:</strong> {{fact.doc_summary}}
                                                </div>
                                            )}}
                                            {{fact.source_text && (
                                                <div className="source-text">
                                                    <strong>📝 Source Text:</strong> {{fact.source_text}}
                                                </div>
                                            )}}
                                            <div style={{{{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '1rem', flexWrap: 'wrap', gap: '1rem' }}}}>
                                                <div style={{{{ fontSize: '0.9rem', color: '#6c757d' }}}}>
                                                    <strong>📎 Exhibit:</strong> {{evidence.id}}
                                                    {{fact.page && <span> | <strong>📄 Page:</strong> {{fact.page}}</span>}}
                                                    {{fact.paragraphs && <span> | <strong>📝 Paragraphs:</strong> {{fact.paragraphs}}</span>}}
                                                </div>
                                                <button className="copy-button" onClick={{() => {{
                                                    const refText = `Exhibit: ${{evidence.id}}${{fact.page ? `, Page: ${{fact.page}}` : ''}}${{fact.paragraphs ? `, Paragraphs: ${{fact.paragraphs}}` : ''}}`;
                                                    navigator.clipboard.writeText(refText).then(() => {{
                                                        // You could add a toast notification here
                                                    }});
                                                }}}}>
                                                    📋 Copy Reference
                                                </button>
                                            </div>
                                            {{idx < evidenceContent.length - 1 && <div className="divider"></div>}}
                                        </div>
                                    ))
                                ) : (
                                    <div className="no-facts" style={{{{ padding: '2rem', fontSize: '0.95rem' }}}}>
                                        📝 No evidence references available for this fact
                                    </div>
                                )}}
                                
                                <div className="section-header">⚖️ Party Submissions</div>
                                <div className="submission-section">
                                    <div className="submission-header">🔵 Appellant Submission</div>
                                    <div className="submission-content claimant-submission">
                                        {{fact.claimant_submission === 'No specific submission recorded' ? 
                                            <em>📝 No submission provided by appellant</em> : 
                                            fact.claimant_submission
                                        }}
                                    </div>
                                </div>
                                <div className="submission-section">
                                    <div className="submission-header">🔴 Respondent Submission</div>
                                    <div className="submission-content respondent-submission">
                                        {{fact.respondent_submission === 'No specific submission recorded' ? 
                                            <em>📝 No submission provided by respondent</em> : 
                                            fact.respondent_submission
                                        }}
                                    </div>
                                </div>
                                
                                <div className="section-header">📊 Fact Status</div>
                                <div className="status-section">
                                    <div className="status-item">
                                        {{fact.isDisputed ? '⚠️' : '✅'}} <strong>Status:</strong> 
                                        <span style={{{{ color: fact.isDisputed ? '#dc3545' : '#28a745', marginLeft: '0.5rem' }}}}>
                                            {{fact.isDisputed ? 'Disputed' : 'Undisputed'}}
                                        </span>
                                    </div>
                                    {{fact.parties_involved && (
                                        <div className="status-item">
                                            👥 <strong>Parties:</strong> {{fact.parties_involved.join(', ')}}
                                        </div>
                                    )}}
                                </div>
                            </div>
                        </div>
                    </div>
                );
            }};

            // Enhanced Timeline View Component
            const TimelineView = ({{ facts }}) => {{
                const sortedFacts = [...facts].sort((a, b) => {{
                    const dateA = a.date.split('-')[0];
                    const dateB = b.date.split('-')[0];
                    return dateA.localeCompare(dateB);
                }});
                
                // Group by year
                const eventsByYear = {{}};
                sortedFacts.forEach(fact => {{
                    const year = fact.date.split('-')[0];
                    if (!eventsByYear[year]) {{
                        eventsByYear[year] = [];
                    }}
                    eventsByYear[year].push(fact);
                }});
                
                return (
                    <div>
                        {{Object.entries(eventsByYear).map(([year, events]) => (
                            <div key={{year}}>
                                <div className="timeline-year">📅 {{year}}</div>
                                {{events.map((fact, index) => {{
                                    const evidenceContent = getEvidenceContent(fact);
                                    return (
                                        <div key={{index}} className="timeline-event">
                                            <div className="timeline-header">
                                                <div className="timeline-date">📆 {{fact.date}}</div>
                                                <div className="timeline-title">{{fact.event}}</div>
                                                <div className={{`dispute-indicator ${{!fact.isDisputed ? 'undisputed' : ''}}`}} 
                                                     title={{fact.isDisputed ? 'Disputed Fact' : 'Undisputed Fact'}}></div>
                                            </div>
                                            
                                            <div>
                                                <div className="section-header">📁 Evidence & Source References</div>
                                                {{evidenceContent.length > 0 ? (
                                                    evidenceContent.map((evidence, idx) => (
                                                        <div key={{idx}} className="evidence-item">
                                                            <div>📄 <strong>{{evidence.id}}</strong> - {{evidence.title}}</div>
                                                            {{fact.doc_summary && (
                                                                <div className="document-summary">
                                                                    <strong>📋 Document Summary:</strong> {{fact.doc_summary}}
                                                                </div>
                                                            )}}
                                                            {{fact.source_text && (
                                                                <div className="source-text">
                                                                    <strong>📝 Source Text:</strong> {{fact.source_text}}
                                                                </div>
                                                            )}}
                                                        </div>
                                                    ))
                                                ) : (
                                                    <div className="no-facts" style={{{{ padding: '1.5rem', fontSize: '0.95rem' }}}}>
                                                        📝 No evidence references available
                                                    </div>
                                                )}}
                                                
                                                <div className="section-header">⚖️ Party Submissions</div>
                                                <div className="submission-section">
                                                    <div className="submission-header">🔵 Appellant Submission</div>
                                                    <div className="submission-content claimant-submission">
                                                        {{fact.claimant_submission === 'No specific submission recorded' ? 
                                                            <em>📝 No submission provided by appellant</em> : 
                                                            fact.claimant_submission
                                                        }}
                                                    </div>
                                                </div>
                                                <div className="submission-section">
                                                    <div className="submission-header">🔴 Respondent Submission</div>
                                                    <div className="submission-content respondent-submission">
                                                        {{fact.respondent_submission === 'No specific submission recorded' ? 
                                                            <em>📝 No submission provided by respondent</em> : 
                                                            fact.respondent_submission
                                                        }}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    );
                                }})}}
                            </div>
                        ))}}
                    </div>
                );
            }};

            // Enhanced Document Categories View Component
            const DocumentCategoriesView = ({{ facts }}) => {{
                const [expandedDocsets, setExpandedDocsets] = useState({{}});
                
                // Group facts by document categories
                const docsWithFacts = {{}};
                
                // Initialize all groups
                documentSets.forEach(ds => {{
                    if (ds.isGroup) {{
                        docsWithFacts[ds.id] = {{
                            docset: ds,
                            facts: []
                        }};
                    }}
                }});
                
                // Distribute facts to categories
                facts.forEach(fact => {{
                    let factAssigned = false;
                    
                    // Try to assign based on source matching
                    for (const ds of documentSets) {{
                        if (ds.isGroup) {{
                            for (const doc of ds.documents) {{
                                if (fact.source && fact.source.includes(doc.id + '.')) {{
                                    docsWithFacts[ds.id].facts.push({{
                                        ...fact,
                                        documentName: doc.name
                                    }});
                                    factAssigned = true;
                                    break;
                                }}
                            }}
                            if (factAssigned) break;
                        }}
                    }}
                    
                    // If not assigned by source, assign by party matching
                    if (!factAssigned) {{
                        for (const ds of documentSets) {{
                            if (ds.isGroup) {{
                                for (const doc of ds.documents) {{
                                    const parties = fact.parties_involved || [];
                                    if (doc.party === 'Mixed' || 
                                        (doc.party === 'Appellant' && parties.includes('Appellant')) ||
                                        (doc.party === 'Respondent' && parties.includes('Respondent'))) {{
                                        docsWithFacts[ds.id].facts.push({{
                                            ...fact,
                                            documentName: doc.name
                                        }});
                                        factAssigned = true;
                                        break;
                                    }}
                                }}
                                if (factAssigned) break;
                            }}
                        }}
                    }}
                }});
                
                const toggleDocset = (docsetId) => {{
                    setExpandedDocsets(prev => ({{
                        ...prev,
                        [docsetId]: !prev[docsetId]
                    }}));
                }};
                
                return (
                    <div>
                        {{Object.entries(docsWithFacts).map(([docsetId, docWithFacts]) => {{
                            const docset = docWithFacts.docset;
                            const docsetFacts = docWithFacts.facts;
                            
                            const partyColor = docset.party === 'Appellant' ? '🔵' : 
                                             docset.party === 'Respondent' ? '🔴' : '⚪';
                            
                            return (
                                <div key={{docsetId}} className="docset-container">
                                    <div className="docset-header" onClick={{() => toggleDocset(docsetId)}}>
                                        <div>📁 {{partyColor}} <strong>{{docset.name}}</strong> <em>({{docsetFacts.length}} facts)</em></div>
                                        <div style={{{{ fontSize: '1.2rem' }}}}>{{expandedDocsets[docsetId] ? '🔽' : '▶️'}}</div>
                                    </div>
                                    <div className={{`docset-content ${{expandedDocsets[docsetId] ? 'expanded' : ''}}`}}>
                                        {{docsetFacts.length > 0 ? (
                                            docsetFacts.map((fact, index) => {{
                                                const evidenceContent = getEvidenceContent(fact);
                                                return (
                                                    <div key={{index}} style={{{{ marginBottom: '2.5rem', paddingBottom: '1.5rem', borderBottom: index < docsetFacts.length - 1 ? '1px solid #e1e5e9' : 'none' }}}}>
                                                        <div style={{{{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', padding: '1rem', background: 'linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%)', borderRadius: '6px', border: '1px solid #e1e5e9' }}}}>
                                                            <div style={{{{ display: 'flex', alignItems: 'center', gap: '1rem' }}}}>
                                                                <span className="fact-date">{{fact.date}}</span>
                                                                <strong>{{fact.event}}</strong>
                                                            </div>
                                                            <div className={{`dispute-indicator ${{!fact.isDisputed ? 'undisputed' : ''}}`}} 
                                                                 title={{fact.isDisputed ? 'Disputed Fact' : 'Undisputed Fact'}}></div>
                                                        </div>
                                                        
                                                        <div className="section-header">📁 Evidence & Source References</div>
                                                        {{evidenceContent.length > 0 ? (
                                                            evidenceContent.map((evidence, idx) => (
                                                                <div key={{idx}} className="evidence-item">
                                                                    <div>📄 <strong>{{evidence.id}}</strong> - {{evidence.title}}</div>
                                                                    {{fact.doc_summary && (
                                                                        <div className="document-summary">
                                                                            <strong>📋 Document Summary:</strong> {{fact.doc_summary}}
                                                                        </div>
                                                                    )}}
                                                                    {{fact.source_text && (
                                                                        <div className="source-text">
                                                                            <strong>📝 Source Text:</strong> {{fact.source_text}}
                                                                        </div>
                                                                    )}}
                                                                </div>
                                                            ))
                                                        ) : (
                                                            <div className="no-facts" style={{{{ padding: '1.5rem', fontSize: '0.95rem' }}}}>
                                                                📝 No evidence references available
                                                            </div>
                                                        )}}
                                                        
                                                        <div className="section-header">⚖️ Party Submissions</div>
                                                        <div className="submission-section">
                                                            <div className="submission-header">🔵 Appellant Submission</div>
                                                            <div className="submission-content claimant-submission">
                                                                {{fact.claimant_submission === 'No specific submission recorded' ? 
                                                                    <em>📝 No submission provided by appellant</em> : 
                                                                    fact.claimant_submission
                                                                }}
                                                            </div>
                                                        </div>
                                                        <div className="submission-section">
                                                            <div className="submission-header">🔴 Respondent Submission</div>
                                                            <div className="submission-content respondent-submission">
                                                                {{fact.respondent_submission === 'No specific submission recorded' ? 
                                                                    <em>📝 No submission provided by respondent</em> : 
                                                                    fact.respondent_submission
                                                                }}
                                                            </div>
                                                        </div>
                                                    </div>
                                                );
                                            }})
                                        ) : (
                                            <div className="no-facts">📂 No facts found in this document category</div>
                                        )}}
                                    </div>
                                </div>
                            );
                        }})}}
                    </div>
                );
            }};

            // Main App Component
            const FactsMainContent = () => {{
                const allFacts = getAllFacts();
                
                const getFilteredFacts = () => {{
                    switch (currentTabType) {{
                        case 'disputed':
                            return allFacts.filter(fact => fact.isDisputed);
                        case 'undisputed':
                            return allFacts.filter(fact => !fact.isDisputed);
                        default:
                            return allFacts;
                    }}
                }};
                
                const filteredFacts = getFilteredFacts();
                
                const renderContent = () => {{
                    switch (currentViewType) {{
                        case 'timeline':
                            return <TimelineView facts={{filteredFacts}} />;
                        case 'docset':
                            return <DocumentCategoriesView facts={{filteredFacts}} />;
                        default:
                            return (
                                <div>
                                    {{filteredFacts.length > 0 ? (
                                        filteredFacts.map((fact, index) => (
                                            <FactCard key={{index}} fact={{fact}} index={{index}} />
                                        ))
                                    ) : (
                                        <div className="no-facts">
                                            🔍 No facts found matching the selected criteria.<br/>
                                            <small>Try adjusting your filter settings above.</small>
                                        </div>
                                    )}}
                                </div>
                            );
                    }}
                }};
                
                return (
                    <div className="main-content">
                        {{renderContent()}}
                    </div>
                );
            }};

            ReactDOM.render(<FactsMainContent />, document.getElementById('root'));
        </script>
    </body>
    </html>
    """
    
    # Render the React component
    components.html(html_content, height=800, scrolling=True)

else:
    # Show enhanced placeholder for other views
    st.title(f"📑 {st.session_state.view}")
    st.markdown(f"**{st.session_state.view} Analysis Dashboard**")
    st.markdown("---")
    
    # Create attractive placeholder
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info(f"🔧 **{st.session_state.view} view is currently under development.**")
        st.markdown(f"""
        The **{st.session_state.view}** section will include:
        - Comprehensive {st.session_state.view.lower()} analysis
        - Interactive visualizations
        - Detailed breakdowns and summaries
        - Cross-referencing with case facts
        """)
        
        st.markdown("### ✅ Currently Available:")
        st.success("**📊 Facts View** - Fully functional with enhanced UI")
        
    with col2:
        st.markdown("### 🎯 Quick Access")
        if st.button("🔄 Go to Facts View", type="primary", use_container_width=True):
            st.session_state.view = "Facts"
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 📋 Features in Facts View:")
        st.markdown("""
        - **📋 Card View**: Expandable fact cards
        - **📅 Timeline View**: Chronological events  
        - **📁 Document Categories**: Organized by docs
        - **🎯 Smart Filtering**: All/Disputed/Undisputed
        - **📎 Evidence Tracking**: Source references
        - **📋 Copy References**: Easy citation copying
        """)
