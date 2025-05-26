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

def get_sample_facts():
    """Return sample legal facts data"""
    return [
        {
            "event": "Continuous operation under same name since 1950",
            "date": "1950-present",
            "isDisputed": False,
            "source_text": "The club has maintained continuous operation under the same name 'Athletic Club United' since its official registration in 1950, as evidenced by uninterrupted participation in national competitions and consistent use of the same corporate identity throughout this period.",
            "page": 23,
            "doc_name": "Statement of Appeal",
            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity.",
            "claimant_submission": "The club has maintained continuous operation under the same name 'Athletic Club United' since its official registration in 1950.",
            "respondent_submission": "No specific submission recorded",
            "exhibits": ["C-1", "C-2", "C-4"],
            "parties_involved": ["Appellant"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "paragraphs": "18-19"
        },
        {
            "event": "Operations ceased between 1975-1976",
            "date": "1975-1976",
            "isDisputed": True,
            "source_text": "The club's operations completely ceased during the 1975-1976 season, with no participation in any competitive events and complete absence from all official federation records during this period.",
            "page": 89,
            "doc_name": "Answer to Request for Provisional Measures",
            "doc_summary": "Respondent's response challenging the appellant's claims and presenting evidence of operational discontinuity.",
            "claimant_submission": "While there was a temporary administrative restructuring during 1975-1976 due to financial difficulties, the club's core operations and identity remained intact throughout this period.",
            "respondent_submission": "Complete cessation of all club operations occurred during the 1975-1976 season, with no team fielded in any competition and complete absence from federation records.",
            "exhibits": ["C-2", "R-1", "R-2"],
            "parties_involved": ["Appellant", "Respondent"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "paragraphs": "206-207"
        },
        {
            "event": "Club colors established as blue and white",
            "date": "1956-03-10",
            "isDisputed": True,
            "source_text": "The club's official colors were formally established as royal blue and white on March 10, 1956, following a unanimous decision by the club's founding committee and ratified by the membership.",
            "page": 67,
            "doc_name": "Statement of Appeal",
            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity.",
            "claimant_submission": "The club's official colors were formally established as royal blue and white on March 10, 1956, following a unanimous decision by the club's founding committee.",
            "respondent_submission": "The newly registered entity adopted a significantly different color scheme incorporating red and yellow as primary colors, abandoning the traditional blue and white entirely.",
            "exhibits": ["C-4", "R-4"],
            "parties_involved": ["Appellant", "Respondent"],
            "argId": "1.2",
            "argTitle": "Club Colors Analysis",
            "paragraphs": "51-52"
        },
        {
            "event": "First National Championship won",
            "date": "1955-05-20",
            "isDisputed": False,
            "source_text": "Athletic Club United achieved its first National Championship victory on May 20, 1955, defeating rivals 3-1 in the final match held at National Stadium, establishing the club's competitive credentials.",
            "page": 42,
            "doc_name": "Appeal Brief",
            "doc_summary": "Comprehensive brief supporting the appeal with detailed arguments and evidence regarding club continuity and identity.",
            "claimant_submission": "Athletic Club United achieved its first National Championship victory on May 20, 1955, defeating rivals 3-1 in the final match held at National Stadium.",
            "respondent_submission": "No specific counter-submission recorded",
            "exhibits": ["C-3"],
            "parties_involved": ["Appellant"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "paragraphs": "42-43"
        },
        {
            "event": "Club registration formally terminated",
            "date": "1975-04-30",
            "isDisputed": True,
            "source_text": "The club's registration with the National Football Federation was formally terminated on April 30, 1975, following failure to meet financial obligations and regulatory requirements.",
            "page": 158,
            "doc_name": "Answer to Request for Provisional Measures",
            "doc_summary": "Respondent's response challenging the appellant's claims and presenting evidence of operational discontinuity.",
            "claimant_submission": "On April 30, 1975, the club's administrative operations were formally halted due to severe financial difficulties, but this was a temporary administrative measure that did not affect the club's legal identity.",
            "respondent_submission": "The club's registration with the National Football Federation was formally terminated on April 30, 1975, following failure to meet financial obligations and regulatory requirements, creating a complete legal break.",
            "exhibits": ["R-2"],
            "parties_involved": ["Appellant", "Respondent"],
            "argId": "1.1.1",
            "argTitle": "Registration Gap Evidence",
            "paragraphs": "158-160"
        }
    ]

def get_evidence_details():
    """Return evidence details"""
    return {
        "C-1": {
            "title": "Historical Registration Documents",
            "summary": "Official records showing continuous name usage from 1950 to present day. Includes original registration certificate dated January 12, 1950, and all subsequent renewal documentation without interruption."
        },
        "C-2": {
            "title": "Competition Participation Records", 
            "summary": "Complete records of the club's participation in national and regional competitions from 1950 to present, demonstrating uninterrupted competitive activity under the same name and organizational structure."
        },
        "C-3": {
            "title": "Championship Records",
            "summary": "Official records of the club's championship victories and competitive achievements from 1955 onwards, demonstrating consistent sporting performance under the same identity."
        },
        "C-4": {
            "title": "Media Coverage Archive",
            "summary": "Comprehensive collection of newspaper clippings, sports magazines, and media reports spanning 1950-2024 consistently referring to the club by the same name and recognizing its continuous identity."
        },
        "R-1": {
            "title": "Federation Records",
            "summary": "Official competition records from the National Football Federation for the 1975-1976 season, showing complete absence of the club from all levels of competition that season."
        },
        "R-2": {
            "title": "Financial Audit Reports",
            "summary": "Independent auditor reports from 1975-1976 documenting the complete cessation of club operations, closure of all bank accounts, and termination of all contractual obligations."
        },
        "R-4": {
            "title": "Color Change Documentation",
            "summary": "Documentation showing the adoption of red and yellow colors by the newly registered entity in 1976-1977 season."
        }
    }

def get_document_sets():
    """Return document sets for categorization"""
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
                {"id": "5", "name": "5. Appeal Brief", "party": "Appellant", "category": "Appeal"}
            ]
        },
        {
            "id": "provisional_measures",
            "name": "Provisional Measures",
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
            "name": "Admissibility",
            "party": "Mixed",
            "category": "admissibility",
            "isGroup": True,
            "documents": [
                {"id": "6", "name": "6. Brief on Admissibility", "party": "Respondent", "category": "admissibility"},
                {"id": "7", "name": "7. Reply to Objection to Admissibility", "party": "Appellant", "category": "admissibility"}
            ]
        }
    ]

def main():
    # Sidebar navigation
    with st.sidebar:
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
              <mask id="mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#mask)">
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                <path d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <h1 style="margin-left: 10px; font-weight: 600; color: #4D68F9;">CaseLens</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
        
        # Navigation buttons
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
    
    # Main content
    if st.session_state.view == "Facts":
        st.title("Case Facts")
        
        # Get data
        facts_data = get_sample_facts()
        evidence_data = get_evidence_details()
        document_sets = get_document_sets()
        
        # Convert to JSON for JavaScript
        facts_json = json.dumps(facts_data)
        evidence_json = json.dumps(evidence_data)
        document_sets_json = json.dumps(document_sets)
        
        # Create HTML component with all three views
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #fff;
                }}
                
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                
                .badge {{
                    display: inline-block;
                    padding: 3px 8px;
                    border-radius: 12px;
                    font-size: 12px;
                    font-weight: 500;
                }}
                
                .appellant-badge {{
                    background-color: rgba(49, 130, 206, 0.1);
                    color: #3182ce;
                }}
                
                .respondent-badge {{
                    background-color: rgba(229, 62, 62, 0.1);
                    color: #e53e3e;
                }}
                
                .shared-badge {{
                    background-color: rgba(128, 128, 128, 0.1);
                    color: #666;
                }}
                
                .disputed-badge {{
                    background-color: rgba(229, 62, 62, 0.1);
                    color: #e53e3e;
                }}
                
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
                    background-color: #4299e1;
                    color: white;
                    border-color: #4299e1;
                }}
                
                .view-toggle button:first-child {{
                    border-radius: 4px 0 0 4px;
                }}
                
                .view-toggle button:nth-child(2) {{
                    border-left: none;
                    border-right: none;
                }}
                
                .view-toggle button:last-child {{
                    border-radius: 0 4px 4px 0;
                }}
                
                .facts-header {{
                    display: flex;
                    margin-bottom: 20px;
                    border-bottom: 1px solid #dee2e6;
                }}
                
                .tab-button {{
                    padding: 10px 20px;
                    background: none;
                    border: none;
                    cursor: pointer;
                }}
                
                .tab-button.active {{
                    border-bottom: 2px solid #4299e1;
                    color: #4299e1;
                    font-weight: 500;
                }}
                
                .facts-content {{
                    margin-top: 20px;
                }}
                
                /* Card View Styles */
                .card-fact-container {{
                    margin-bottom: 16px;
                    border: 1px solid #e2e8f0;
                    border-radius: 8px;
                    background-color: white;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                
                .card-fact-container.disputed {{
                    border-left: 4px solid #e53e3e;
                    background-color: rgba(229, 62, 62, 0.02);
                }}
                
                .card-fact-header {{
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    padding: 16px;
                    background-color: #f8fafc;
                    cursor: pointer;
                }}
                
                .card-fact-header:hover {{
                    background-color: #e2e8f0;
                }}
                
                .card-fact-header.disputed {{
                    background-color: rgba(229, 62, 62, 0.05);
                }}
                
                .card-fact-title {{
                    display: flex;
                    align-items: center;
                    flex-grow: 1;
                    gap: 12px;
                }}
                
                .card-fact-date {{
                    font-weight: 600;
                    color: #2d3748;
                    min-width: 120px;
                }}
                
                .card-fact-event {{
                    font-weight: 500;
                    color: #1a202c;
                    flex-grow: 1;
                }}
                
                .card-fact-badges {{
                    display: flex;
                    gap: 6px;
                    align-items: center;
                }}
                
                .card-chevron {{
                    transition: transform 0.2s;
                    color: #718096;
                    margin-left: 8px;
                }}
                
                .card-chevron.expanded {{
                    transform: rotate(90deg);
                }}
                
                .card-fact-content {{
                    display: none;
                    padding: 20px;
                    border-top: 1px solid #e2e8f0;
                    background-color: white;
                }}
                
                .card-fact-content.show {{
                    display: block;
                }}
                
                .card-source-text {{
                    background-color: #f7fafc;
                    padding: 16px;
                    border-radius: 6px;
                    border-left: 4px solid #4299e1;
                    margin: 16px 0;
                    font-style: italic;
                    color: #4a5568;
                }}
                
                .card-source-text.claimant-submission {{
                    border-left-color: #3182ce;
                    background-color: rgba(49, 130, 206, 0.03);
                }}
                
                .card-source-text.respondent-submission {{
                    border-left-color: #e53e3e;
                    background-color: rgba(229, 62, 62, 0.03);
                }}
                
                .submission-header {{
                    font-weight: 600;
                    text-transform: uppercase;
                    font-size: 11px;
                    margin-bottom: 8px;
                }}
                
                .claimant-submission .submission-header {{
                    color: #3182ce;
                }}
                
                .respondent-submission .submission-header {{
                    color: #e53e3e;
                }}
                
                /* Timeline View Styles */
                .timeline-container {{
                    display: flex;
                    flex-direction: column;
                    margin-top: 20px;
                    position: relative;
                    max-width: 1000px;
                    margin: 0 auto;
                }}
                
                .timeline-wrapper {{
                    position: relative;
                    margin-left: 20px;
                }}
                
                .timeline-line {{
                    position: absolute;
                    left: 0;
                    top: 0;
                    bottom: 0;
                    width: 4px;
                    background: linear-gradient(to bottom, #4299e1, #7f9cf5);
                    border-radius: 4px;
                }}
                
                .timeline-item {{
                    display: flex;
                    margin-bottom: 32px;
                    position: relative;
                }}
                
                .timeline-point {{
                    position: absolute;
                    left: -12px;
                    top: 18px;
                    width: 24px;
                    height: 24px;
                    border-radius: 50%;
                    background-color: #4299e1;
                    border: 4px solid white;
                    box-shadow: 0 0 0 2px rgba(66, 153, 225, 0.3);
                    z-index: 10;
                }}
                
                .timeline-point.disputed {{
                    background-color: #e53e3e;
                    box-shadow: 0 0 0 2px rgba(229, 62, 62, 0.3);
                }}
                
                .timeline-content {{
                    margin-left: 32px;
                    flex-grow: 1;
                    background-color: white;
                    border-radius: 8px;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                
                .timeline-header {{
                    padding: 12px 16px;
                    border-bottom: 1px solid #e2e8f0;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    background-color: #f8fafc;
                }}
                
                .timeline-header.disputed {{
                    background-color: rgba(229, 62, 62, 0.05);
                }}
                
                .timeline-date {{
                    font-weight: 600;
                    color: #1a202c;
                }}
                
                .timeline-badges {{
                    display: flex;
                    gap: 6px;
                }}
                
                .timeline-body {{
                    padding: 16px;
                }}
                
                .timeline-fact {{
                    margin-bottom: 12px;
                    font-size: 15px;
                    color: #2d3748;
                }}
                
                .timeline-submission {{
                    font-style: italic;
                    color: #4a5568;
                    margin-top: 8px;
                    padding: 12px;
                    background-color: rgba(74, 85, 104, 0.05);
                    border-left: 4px solid #4a5568;
                    font-size: 13px;
                    border-radius: 0 6px 6px 0;
                }}
                
                .timeline-submission.claimant {{
                    color: #3182ce;
                    background-color: rgba(49, 130, 206, 0.05);
                    border-left-color: #3182ce;
                }}
                
                .timeline-submission.respondent {{
                    color: #e53e3e;
                    background-color: rgba(229, 62, 62, 0.05);
                    border-left-color: #e53e3e;
                }}
                
                .timeline-year-marker {{
                    display: flex;
                    align-items: center;
                    margin: 24px 0;
                    position: relative;
                }}
                
                .timeline-year {{
                    background-color: #4299e1;
                    color: white;
                    padding: 4px 12px;
                    border-radius: 16px;
                    font-weight: 600;
                    position: relative;
                    z-index: 10;
                    margin-left: 32px;
                }}
                
                .timeline-year-line {{
                    flex-grow: 1;
                    height: 2px;
                    background-color: #e2e8f0;
                    margin-left: 12px;
                }}
                
                /* Document Sets Styles */
                .docset-header {{
                    display: flex;
                    align-items: center;
                    padding: 10px 15px;
                    background-color: #f8f9fa;
                    border: 1px solid #e9ecef;
                    border-radius: 4px;
                    margin-bottom: 10px;
                    cursor: pointer;
                }}
                
                .docset-header:hover {{
                    background-color: #e9ecef;
                }}
                
                .docset-content {{
                    display: none;
                    padding: 0 0 20px 0;
                }}
                
                .docset-content.show {{
                    display: block;
                }}
                
                .folder-icon {{
                    color: #4299e1;
                    margin-right: 8px;
                }}
                
                .chevron {{
                    transition: transform 0.2s;
                    margin-right: 8px;
                    transform: rotate(0deg);
                }}
                
                .chevron.expanded {{
                    transform: rotate(90deg);
                }}
                
                /* Evidence Styles */
                .evidence-section {{
                    background-color: #f7fafc;
                    padding: 12px 16px;
                    border-radius: 6px;
                    border: 1px solid #e2e8f0;
                    margin-top: 16px;
                }}
                
                .evidence-label {{
                    font-weight: 600;
                    color: #4a5568;
                    font-size: 12px;
                    text-transform: uppercase;
                    margin-bottom: 8px;
                }}
                
                .evidence-summary {{
                    font-size: 13px;
                    color: #4a5568;
                    margin-bottom: 12px;
                    font-style: italic;
                    background-color: #f8fafc;
                    padding: 8px;
                    border-radius: 4px;
                    border-left: 3px solid #dd6b20;
                }}
                
                .evidence-item {{
                    margin-bottom: 12px;
                    border: 1px solid #e2e8f0;
                    border-radius: 6px;
                    overflow: hidden;
                }}
                
                .evidence-header {{
                    padding: 8px 12px;
                    background-color: rgba(221, 107, 32, 0.05);
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                }}
                
                .evidence-header:hover {{
                    background-color: rgba(221, 107, 32, 0.1);
                }}
                
                .evidence-content {{
                    display: none;
                    padding: 12px;
                    background-color: white;
                    border-top: 1px solid #e2e8f0;
                }}
                
                .evidence-icon {{
                    width: 16px;
                    height: 16px;
                    background-color: #dd6b20;
                    color: white;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 10px;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="view-toggle">
                    <button id="card-view-btn" class="active" onclick="switchView('card')">Card View</button>
                    <button id="timeline-view-btn" onclick="switchView('timeline')">Timeline View</button>
                    <button id="docset-view-btn" onclick="switchView('docset')">Document Categories</button>
                </div>
                
                <div class="facts-header">
                    <button class="tab-button active" id="all-facts-btn" onclick="switchTab('all')">All Facts</button>
                    <button class="tab-button" id="disputed-facts-btn" onclick="switchTab('disputed')">Disputed Facts</button>
                    <button class="tab-button" id="undisputed-facts-btn" onclick="switchTab('undisputed')">Undisputed Facts</button>
                </div>
                
                <!-- Card View -->
                <div id="card-view-content" class="facts-content">
                    <div id="card-facts-container"></div>
                </div>
                
                <!-- Timeline View -->
                <div id="timeline-view-content" class="facts-content" style="display: none;">
                    <div class="timeline-container">
                        <div class="timeline-wrapper">
                            <div class="timeline-line"></div>
                            <div id="timeline-events"></div>
                        </div>
                    </div>
                </div>
                
                <!-- Document Sets View -->
                <div id="docset-view-content" class="facts-content" style="display: none;">
                    <div id="document-sets-container"></div>
                </div>
            </div>
            
            <script>
                const factsData = {facts_json};
                const evidenceData = {evidence_json};
                const documentSets = {document_sets_json};
                
                function switchView(viewType) {{
                    const cardBtn = document.getElementById('card-view-btn');
                    const timelineBtn = document.getElementById('timeline-view-btn');
                    const docsetBtn = document.getElementById('docset-view-btn');
                    
                    const cardContent = document.getElementById('card-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    // Remove active class from all buttons
                    cardBtn.classList.remove('active');
                    timelineBtn.classList.remove('active');
                    docsetBtn.classList.remove('active');
                    
                    // Hide all content
                    cardContent.style.display = 'none';
                    timelineContent.style.display = 'none';
                    docsetContent.style.display = 'none';
                    
                    // Activate the selected view
                    if (viewType === 'card') {{
                        cardBtn.classList.add('active');
                        cardContent.style.display = 'block';
                        renderCardView();
                    }} else if (viewType === 'timeline') {{
                        timelineBtn.classList.add('active');
                        timelineContent.style.display = 'block';
                        renderTimeline();
                    }} else if (viewType === 'docset') {{
                        docsetBtn.classList.add('active');
                        docsetContent.style.display = 'block';
                        renderDocumentSets();
                    }}
                }}
                
                function switchTab(tabType) {{
                    // Update tab buttons
                    document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
                    document.getElementById(tabType + '-facts-btn').classList.add('active');
                    
                    // Update active view
                    const cardContent = document.getElementById('card-view-content');
                    const timelineContent = document.getElementById('timeline-view-content');
                    const docsetContent = document.getElementById('docset-view-content');
                    
                    if (cardContent.style.display !== 'none') {{
                        renderCardView(tabType);
                    }} else if (timelineContent.style.display !== 'none') {{
                        renderTimeline(tabType);
                    }} else if (docsetContent.style.display !== 'none') {{
                        renderDocumentSets(tabType);
                    }}
                }}
                
                function renderCardView(tabType = 'all') {{
                    const container = document.getElementById('card-facts-container');
                    container.innerHTML = '';
                    
                    // Filter facts based on tab type
                    let filteredFacts = factsData;
                    if (tabType === 'disputed') {{
                        filteredFacts = factsData.filter(fact => fact.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredFacts = factsData.filter(fact => !fact.isDisputed);
                    }}
                    
                    // Sort by date
                    filteredFacts.sort((a, b) => new Date(a.date.split('-')[0]) - new Date(b.date.split('-')[0]));
                    
                    filteredFacts.forEach((fact, index) => {{
                        const cardEl = document.createElement('div');
                        cardEl.className = `card-fact-container${{fact.isDisputed ? ' disputed' : ''}}`;
                        
                        cardEl.innerHTML = `
                            <div class="card-fact-header${{fact.isDisputed ? ' disputed' : ''}}" onclick="toggleFact(${{index}})">
                                <div class="card-fact-title">
                                    <div class="card-fact-date">${{fact.date}}</div>
                                    <div class="card-fact-event">${{fact.event}}</div>
                                </div>
                                <div class="card-fact-badges">
                                    ${{fact.parties_involved.map(party => 
                                        `<span class="badge ${{party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}">${{party}}</span>`
                                    ).join('')}}
                                    ${{fact.isDisputed ? '<span class="badge disputed-badge">Disputed</span>' : ''}}
                                    <div class="card-chevron" id="chevron-${{index}}">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <polyline points="9,18 15,12 9,6"></polyline>
                                        </svg>
                                    </div>
                                </div>
                            </div>
                            <div class="card-fact-content" id="content-${{index}}">
                                ${{fact.source_text ? `
                                    <div class="card-source-text">
                                        <div class="submission-header">Source Text</div>
                                        <div>${{fact.source_text}}</div>
                                    </div>
                                ` : ''}}
                                
                                <div class="evidence-section">
                                    <div class="evidence-label">Evidence & Source References (${{fact.exhibits.length}} items)</div>
                                    <div class="evidence-summary">
                                        This fact is supported by ${{fact.exhibits.length}} piece${{fact.exhibits.length > 1 ? 's' : ''}} of documentary evidence. Click on each evidence item below to view detailed descriptions.
                                    </div>
                                    ${{fact.exhibits.map((exhibitId, evidenceIndex) => {{
                                        const evidence = evidenceData[exhibitId];
                                        return evidence ? `
                                            <div class="evidence-item">
                                                <div class="evidence-header" onclick="toggleEvidence('${{exhibitId}}', '${{index}}-${{evidenceIndex}}')">
                                                    <div>
                                                        <span style="font-weight: 600; color: #dd6b20; font-size: 12px;">${{exhibitId}}</span>
                                                        <span style="margin-left: 8px; color: #4a5568; font-size: 12px;">${{evidence.title}}</span>
                                                    </div>
                                                    <span class="evidence-icon" id="evidence-icon-${{exhibitId}}-${{index}}-${{evidenceIndex}}">+</span>
                                                </div>
                                                <div class="evidence-content" id="evidence-content-${{exhibitId}}-${{index}}-${{evidenceIndex}}">
                                                    <div style="margin-bottom: 8px;">
                                                        <div style="font-weight: 600; color: #dd6b20; font-size: 13px; margin-bottom: 6px;">Source Reference: ${{exhibitId}}</div>
                                                        <div style="font-weight: 600; color: #2d3748; font-size: 13px; margin-bottom: 6px;">Document: ${{evidence.title}}</div>
                                                        <div style="background-color: #f0f9ff; padding: 8px; border-radius: 4px; border-left: 3px solid #0ea5e9;">
                                                            <div style="font-weight: 600; font-size: 11px; text-transform: uppercase; color: #0ea5e9; margin-bottom: 4px;">Source Text</div>
                                                            <div style="font-size: 12px; color: #4a5568; line-height: 1.4;">${{evidence.summary}}</div>
                                                        </div>
                                                        <div style="margin-top: 8px; font-size: 11px; color: #718096;">
                                                            Page: ${{fact.page || 'N/A'}} | Paragraphs: ${{fact.paragraphs || 'N/A'}}
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        ` : '';
                                    }}).join('')}}
                                </div>
                                
                                <div class="card-source-text claimant-submission">
                                    <div class="submission-header">Claimant Submission</div>
                                    <div>${{fact.claimant_submission}}</div>
                                </div>
                                
                                <div class="card-source-text respondent-submission">
                                    <div class="submission-header">Respondent Submission</div>
                                    <div>${{fact.respondent_submission}}</div>
                                </div>
                            </div>
                        `;
                        
                        container.appendChild(cardEl);
                    }});
                    
                    if (filteredFacts.length === 0) {{
                        container.innerHTML = '<p style="text-align: center; padding: 40px; color: #718096;">No facts found matching the selected criteria.</p>';
                    }}
                }}
                
                function renderTimeline(tabType = 'all') {{
                    const container = document.getElementById('timeline-events');
                    container.innerHTML = '';
                    
                    // Filter facts based on tab type
                    let filteredFacts = factsData;
                    if (tabType === 'disputed') {{
                        filteredFacts = factsData.filter(fact => fact.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredFacts = factsData.filter(fact => !fact.isDisputed);
                    }}
                    
                    // Sort chronologically
                    filteredFacts.sort((a, b) => new Date(a.date.split('-')[0]) - new Date(b.date.split('-')[0]));
                    
                    let currentYear = '';
                    let prevYear = '';
                    
                    filteredFacts.forEach(fact => {{
                        // Get the year for year markers
                        currentYear = fact.date.split('-')[0];
                        if (currentYear && currentYear !== prevYear) {{
                            const yearMarker = document.createElement('div');
                            yearMarker.className = 'timeline-year-marker';
                            yearMarker.innerHTML = `
                                <div class="timeline-year">${{currentYear}}</div>
                                <div class="timeline-year-line"></div>
                            `;
                            container.appendChild(yearMarker);
                            prevYear = currentYear;
                        }}
                        
                        const timelineItem = document.createElement('div');
                        timelineItem.className = 'timeline-item';
                        
                        timelineItem.innerHTML = `
                            <div class="timeline-point${{fact.isDisputed ? ' disputed' : ''}}"></div>
                            <div class="timeline-content">
                                <div class="timeline-header${{fact.isDisputed ? ' disputed' : ''}}">
                                    <div class="timeline-date">${{fact.date}}</div>
                                    <div class="timeline-badges">
                                        ${{fact.parties_involved.map(party => 
                                            `<span class="badge ${{party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}">${{party}}</span>`
                                        ).join('')}}
                                        <span class="badge ${{fact.isDisputed ? 'disputed-badge' : 'shared-badge'}}">${{fact.isDisputed ? 'Disputed' : 'Undisputed'}}</span>
                                    </div>
                                </div>
                                <div class="timeline-body">
                                    <div class="timeline-fact">${{fact.event}}</div>
                                    <div class="timeline-submission claimant">
                                        <strong>Claimant Submission:</strong><br>${{fact.claimant_submission}}
                                    </div>
                                    <div class="timeline-submission respondent">
                                        <strong>Respondent Submission:</strong><br>${{fact.respondent_submission}}
                                    </div>
                                </div>
                            </div>
                        `;
                        
                        container.appendChild(timelineItem);
                    }});
                    
                    if (filteredFacts.length === 0) {{
                        container.innerHTML = '<p>No timeline events found matching the selected criteria.</p>';
                    }}
                }}
                
                function renderDocumentSets(tabType = 'all') {{
                    const container = document.getElementById('document-sets-container');
                    container.innerHTML = '';
                    
                    // Filter facts based on tab type
                    let filteredFacts = factsData;
                    if (tabType === 'disputed') {{
                        filteredFacts = factsData.filter(fact => fact.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredFacts = factsData.filter(fact => !fact.isDisputed);
                    }}
                    
                    // Group facts by document sets
                    const docsWithFacts = {{}};
                    documentSets.forEach(ds => {{
                        if (ds.isGroup) {{
                            docsWithFacts[ds.id] = {{
                                docset: ds,
                                facts: []
                            }};
                        }}
                    }});
                    
                    filteredFacts.forEach(fact => {{
                        // Assign facts to document sets based on party
                        let assigned = false;
                        documentSets.forEach(ds => {{
                            if (ds.isGroup && !assigned) {{
                                if (ds.party === 'Mixed' || 
                                    (fact.parties_involved.includes('Appellant') && ds.party === 'Appellant') ||
                                    (fact.parties_involved.includes('Respondent') && ds.party === 'Respondent')) {{
                                    docsWithFacts[ds.id].facts.push(fact);
                                    assigned = true;
                                }}
                            }}
                        }});
                    }});
                    
                    Object.values(docsWithFacts).forEach(docWithFacts => {{
                        const docset = docWithFacts.docset;
                        const facts = docWithFacts.facts;
                        
                        const docsetEl = document.createElement('div');
                        docsetEl.innerHTML = `
                            <div class="docset-header" onclick="toggleDocSet('${{docset.id}}')">
                                <svg class="chevron" id="chevron-${{docset.id}}" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <polyline points="9,18 15,12 9,6"></polyline>
                                </svg>
                                <svg class="folder-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                                </svg>
                                <span><strong>${{docset.name}}</strong></span>
                                <span style="margin-left: auto;">
                                    <span class="badge ${{docset.party === 'Appellant' ? 'appellant-badge' : (docset.party === 'Respondent' ? 'respondent-badge' : 'shared-badge')}}">
                                        ${{docset.party}}
                                    </span>
                                    <span class="badge">${{facts.length}} facts</span>
                                </span>
                            </div>
                            <div class="docset-content" id="docset-content-${{docset.id}}">
                                <div style="padding: 16px;">
                                    ${{facts.length > 0 ? facts.map(fact => `
                                        <div style="margin-bottom: 16px; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; background-color: white;">
                                            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                                                <div style="font-weight: 600; color: #2d3748;">${{fact.date}}</div>
                                                <div style="display: flex; gap: 6px;">
                                                    ${{fact.parties_involved.map(party => 
                                                        `<span class="badge ${{party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}">${{party}}</span>`
                                                    ).join('')}}
                                                    ${{fact.isDisputed ? '<span class="badge disputed-badge">Disputed</span>' : ''}}
                                                </div>
                                            </div>
                                            <div style="font-weight: 500; color: #1a202c; margin-bottom: 12px;">${{fact.event}}</div>
                                            <div style="font-size: 14px; color: #4a5568; font-style: italic;">${{fact.source_text}}</div>
                                        </div>
                                    `).join('') : '<p>No facts found</p>'}}
                                </div>
                            </div>
                        `;
                        
                        container.appendChild(docsetEl);
                    }});
                }}
                
                function toggleFact(index) {{
                    const content = document.getElementById(`content-${{index}}`);
                    const chevron = document.getElementById(`chevron-${{index}}`);
                    
                    if (content.classList.contains('show')) {{
                        content.classList.remove('show');
                        chevron.classList.remove('expanded');
                    }} else {{
                        content.classList.add('show');
                        chevron.classList.add('expanded');
                    }}
                }}
                
                function toggleEvidence(evidenceId, factIndex) {{
                    const content = document.getElementById(`evidence-content-${{evidenceId}}-${{factIndex}}`);
                    const icon = document.getElementById(`evidence-icon-${{evidenceId}}-${{factIndex}}`);
                    
                    if (content.style.display === 'none' || content.style.display === '') {{
                        content.style.display = 'block';
                        icon.textContent = '−';
                    }} else {{
                        content.style.display = 'none';
                        icon.textContent = '+';
                    }}
                }}
                
                function toggleDocSet(docsetId) {{
                    const content = document.getElementById(`docset-content-${{docsetId}}`);
                    const chevron = document.getElementById(`chevron-${{docsetId}}`);
                    
                    if (content.style.display === 'none' || content.style.display === '') {{
                        content.style.display = 'block';
                        chevron.style.transform = 'rotate(90deg)';
                    }} else {{
                        content.style.display = 'none';
                        chevron.style.transform = 'rotate(0deg)';
                    }}
                }}
                
                // Initialize
                renderCardView('all');
            </script>
        </body>
        </html>
        """
        
        components.html(html_content, height=800, scrolling=True)
    
    elif st.session_state.view == "Arguments":
        st.title("Legal Arguments")
        st.info("Arguments view - This section would contain detailed legal argument analysis, case law references, and argument hierarchies.")
    
    elif st.session_state.view == "Exhibits":
        st.title("Exhibits")
        st.info("Exhibits view - This section would contain evidence management, document viewers, and exhibit categorization.")

if __name__ == "__main__":
    main()
