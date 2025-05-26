import streamlit as st
import json
import streamlit.components.v1 as components

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

def main():
    # Sidebar navigation
    with st.sidebar:
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="width: 35px; height: 35px; background-color: #4D68F9; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">CL</div>
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
        
        # Convert to JSON for JavaScript
        facts_json = json.dumps(facts_data)
        evidence_json = json.dumps(evidence_data)
        
        # Create HTML component
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
                
                .disputed-badge {{
                    background-color: rgba(229, 62, 62, 0.1);
                    color: #e53e3e;
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
                <div class="facts-header">
                    <button class="tab-button active" id="all-facts-btn" onclick="switchTab('all')">All Facts</button>
                    <button class="tab-button" id="disputed-facts-btn" onclick="switchTab('disputed')">Disputed Facts</button>
                    <button class="tab-button" id="undisputed-facts-btn" onclick="switchTab('undisputed')">Undisputed Facts</button>
                </div>
                
                <div id="facts-container"></div>
            </div>
            
            <script>
                const factsData = {facts_json};
                const evidenceData = {evidence_json};
                
                function switchTab(tabType) {{
                    // Update tab buttons
                    document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
                    document.getElementById(tabType + '-facts-btn').classList.add('active');
                    
                    // Filter and render facts
                    let filteredFacts = factsData;
                    if (tabType === 'disputed') {{
                        filteredFacts = factsData.filter(fact => fact.isDisputed);
                    }} else if (tabType === 'undisputed') {{
                        filteredFacts = factsData.filter(fact => !fact.isDisputed);
                    }}
                    
                    renderFacts(filteredFacts);
                }}
                
                function renderFacts(facts) {{
                    const container = document.getElementById('facts-container');
                    container.innerHTML = '';
                    
                    facts.forEach((fact, index) => {{
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
                
                // Initialize
                renderFacts(factsData);
            </script>
        </body>
        </html>
        """
        
        components.html(html_content, height=800, scrolling=True)
    
    elif st.session_state.view == "Arguments":
        st.title("Legal Arguments")
        st.info("Arguments view - Implementation pending")
    
    elif st.session_state.view == "Exhibits":
        st.title("Exhibits")
        st.info("Exhibits view - Implementation pending")

if __name__ == "__main__":
    main()
