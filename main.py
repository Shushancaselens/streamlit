import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Create data structures as JSON for embedded components
def get_argument_data():
    # Original data structure
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
            "legalPoints": [
                {
                    "point": "CAS jurisprudence requires operational continuity not merely identification",
                    "isDisputed": False,
                    "regulations": ["CAS 2017/A/5465"],
                    "paragraphs": "203-205"
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
    # Get the data
    args_data = get_argument_data()
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    
    # Convert data to JSON strings
    args_json = json.dumps(args_data)
    timeline_json = json.dumps(timeline_data)
    exhibits_json = json.dumps(exhibits_data)
    
    # Title
    st.title("Legal Arguments Analysis")
    
    # Create tab structure
    tab1, tab2, tab3 = st.tabs(["Arguments", "Timeline", "Exhibits"])
    
    with tab1:
        # Instead of using f-strings, we'll write the HTML/CSS and JavaScript as static strings
        # Then provide the data at runtime using a separate <script> tag
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    line-height: 1.5;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }
                .view-toggle {
                    display: flex;
                    justify-content: flex-end;
                    margin-bottom: 1rem;
                }
                .view-toggle-container {
                    background-color: #f7fafc;
                    border-radius: 0.375rem;
                    padding: 0.25rem;
                }
                .view-btn {
                    padding: 0.5rem 1rem;
                    border-radius: 0.375rem;
                    border: none;
                    background: none;
                    font-size: 0.875rem;
                    font-weight: 500;
                    cursor: pointer;
                    color: #718096;
                }
                .view-btn.active {
                    background-color: white;
                    color: #4a5568;
                    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
                }
                .arguments-header {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 1.5rem;
                    margin-bottom: 1rem;
                }
                .claimant-color {
                    color: #3182ce;
                }
                .respondent-color {
                    color: #e53e3e;
                }
                .argument-pair {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 1.5rem;
                    margin-bottom: 1rem;
                    position: relative;
                }
                .argument-side {
                    position: relative;
                }
                .argument {
                    border: 1px solid #e2e8f0;
                    border-radius: 0.375rem;
                    overflow: hidden;
                    margin-bottom: 1rem;
                }
                .argument-header {
                    padding: 0.75rem 1rem;
                    cursor: pointer;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .argument-header-left {
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                }
                .argument-content {
                    padding: 1rem;
                    border-top: 1px solid #e2e8f0;
                    display: none;
                    background-color: white;
                }
                .claimant-header {
                    background-color: #ebf8ff;
                    border-color: #bee3f8;
                }
                .respondent-header {
                    background-color: #fff5f5;
                    border-color: #fed7d7;
                }
                .argument-children {
                    padding-left: 1.5rem;
                    display: none;
                    position: relative;
                }
                .connector-vertical {
                    position: absolute;
                    left: 0.75rem;
                    top: 0;
                    width: 1px;
                    height: 100%;
                    background-color: #e2e8f0;
                }
                .connector-horizontal {
                    position: absolute;
                    left: 0.75rem;
                    top: 1.25rem;
                    width: 0.75rem;
                    height: 1px;
                    background-color: #e2e8f0;
                }
                .claimant-connector {
                    background-color: rgba(59, 130, 246, 0.5);
                }
                .respondent-connector {
                    background-color: rgba(239, 68, 68, 0.5);
                }
                .badge {
                    display: inline-block;
                    padding: 0.25rem 0.5rem;
                    border-radius: 0.25rem;
                    font-size: 0.75rem;
                }
                .claimant-badge {
                    background-color: #ebf8ff;
                    color: #3182ce;
                }
                .respondent-badge {
                    background-color: #fff5f5;
                    color: #e53e3e;
                }
                .legal-badge {
                    background-color: #ebf8ff;
                    color: #2c5282;
                    margin-right: 0.25rem;
                }
                .factual-badge {
                    background-color: #f0fff4;
                    color: #276749;
                    margin-right: 0.25rem;
                }
                .disputed-badge {
                    background-color: #fed7d7;
                    color: #c53030;
                }
                .type-badge {
                    background-color: #edf2f7;
                    color: #4a5568;
                }
                .point-block {
                    background-color: #f7fafc;
                    border-radius: 0.5rem;
                    padding: 0.75rem;
                    margin-bottom: 0.5rem;
                }
                .point-header {
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                    margin-bottom: 0.25rem;
                }
                .point-date {
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                    margin-bottom: 0.25rem;
                    font-size: 0.75rem;
                    color: #718096;
                }
                .legal-point {
                    background-color: #ebf8ff;
                    border-radius: 0.5rem;
                    padding: 0.75rem;
                    margin-bottom: 0.5rem;
                }
                .factual-point {
                    background-color: #f0fff4;
                    border-radius: 0.5rem;
                    padding: 0.75rem;
                    margin-bottom: 0.5rem;
                }
                .reference-block {
                    background-color: #f7fafc;
                    border-radius: 0.5rem;
                    padding: 0.75rem;
                    margin-bottom: 0.5rem;
                }
                .overview-block {
                    background-color: #f7fafc;
                    border-radius: 0.5rem;
                    padding: 1rem;
                    margin-bottom: 1rem;
                }
                .overview-list {
                    display: flex;
                    flex-direction: column;
                    gap: 0.5rem;
                }
                .overview-item {
                    display: flex;
                    align-items: flex-start;
                    gap: 0.5rem;
                }
                .overview-bullet {
                    width: 6px;
                    height: 6px;
                    border-radius: 50%;
                    background-color: #3182ce;
                    margin-top: 0.5rem;
                }
                .topic-section {
                    margin-bottom: 2rem;
                }
                .topic-title {
                    font-size: 1.25rem;
                    font-weight: 600;
                    color: #2d3748;
                    margin-bottom: 0.25rem;
                }
                .topic-description {
                    font-size: 0.875rem;
                    color: #718096;
                    margin-bottom: 1rem;
                }
            </style>
        </head>
        <body>
            <div id="arguments">
                <div class="view-toggle">
                    <div class="view-toggle-container">
                        <button class="view-btn active" data-view="standard">Standard View</button>
                        <button class="view-btn" data-view="topic">Topic View</button>
                    </div>
                </div>
                
                <div id="standard-view" class="view-content">
                    <div class="arguments-header">
                        <h3 class="claimant-color">Claimant's Arguments</h3>
                        <h3 class="respondent-color">Respondent's Arguments</h3>
                    </div>
                    <div id="standard-arguments-container"></div>
                </div>
                
                <div id="topic-view" class="view-content" style="display: none;">
                    <div id="topics-container"></div>
                </div>
            </div>
            
            <script>
                // Data will be injected via a separate script tag
                
                // View switching
                document.querySelectorAll('.view-btn').forEach(btn => {
                    btn.addEventListener('click', function() {
                        // Update buttons
                        document.querySelectorAll('.view-btn').forEach(b => {
                            b.classList.remove('active');
                            b.style.backgroundColor = '';
                            b.style.boxShadow = '';
                        });
                        this.classList.add('active');
                        this.style.backgroundColor = 'white';
                        this.style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';
                        
                        // Update content
                        const viewId = this.getAttribute('data-view');
                        if (viewId === 'standard') {
                            document.getElementById('standard-view').style.display = 'block';
                            document.getElementById('topic-view').style.display = 'none';
                        } else {
                            document.getElementById('standard-view').style.display = 'none';
                            document.getElementById('topic-view').style.display = 'block';
                        }
                    });
                });
                
                // Render overview points
                function renderOverviewPoints(overview) {
                    if (!overview || !overview.points || overview.points.length === 0) return '';
                    
                    const pointsHtml = overview.points.map(point => 
                        `<div class="overview-item">
                            <div class="overview-bullet"></div>
                            <span class="point-text">${point}</span>
                        </div>`
                    ).join('');
                    
                    return `
                    <div class="overview-block">
                        <div class="overview-header">
                            <h6 class="content-section-title">Key Points</h6>
                            <span class="badge claimant-badge">¶${overview.paragraphs}</span>
                        </div>
                        <div class="overview-list">
                            ${pointsHtml}
                        </div>
                    </div>
                    `;
                }
                
                // Render legal points
                function renderLegalPoints(points) {
                    if (!points || points.length === 0) return '';
                    
                    const pointsHtml = points.map(point => {
                        const disputed = point.isDisputed 
                            ? `<span class="badge disputed-badge">Disputed</span>` 
                            : '';
                        
                        const regulations = point.regulations 
                            ? point.regulations.map(reg => `<span class="badge legal-badge">${reg}</span>`).join('') 
                            : '';
                        
                        return `
                        <div class="legal-point">
                            <div class="point-header">
                                <span class="badge legal-badge">Legal</span>
                                ${disputed}
                            </div>
                            <p class="point-text">${point.point}</p>
                            <div style="margin-top: 0.5rem; display: flex; flex-wrap: wrap; gap: 0.25rem; align-items: center;">
                                ${regulations}
                                <span class="point-citation">¶${point.paragraphs}</span>
                            </div>
                        </div>
                        `;
                    }).join('');
                    
                    return `
                    <div class="content-section">
                        <h6 class="content-section-title">Legal Points</h6>
                        ${pointsHtml}
                    </div>
                    `;
                }
                
                // Render factual points
                function renderFactualPoints(points) {
                    if (!points || points.length === 0) return '';
                    
                    const pointsHtml = points.map(point => {
                        const disputed = point.isDisputed 
                            ? `<span class="badge disputed-badge">Disputed by ${point.source || ''}</span>` 
                            : '';
                        
                        return `
                        <div class="factual-point">
                            <div class="point-header">
                                <span class="badge factual-badge">Factual</span>
                                ${disputed}
                            </div>
                            <div class="point-date">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                    <line x1="16" y1="2" x2="16" y2="6"></line>
                                    <line x1="8" y1="2" x2="8" y2="6"></line>
                                    <line x1="3" y1="10" x2="21" y2="10"></line>
                                </svg>
                                ${point.date}
                            </div>
                            <p class="point-text">${point.point}</p>
                            <span class="point-citation">¶${point.paragraphs}</span>
                        </div>
                        `;
                    }).join('');
                    
                    return `
                    <div class="content-section">
                        <h6 class="content-section-title">Factual Points</h6>
                        ${pointsHtml}
                    </div>
                    `;
                }
                
                // Render evidence
                function renderEvidence(evidence) {
                    if (!evidence || evidence.length === 0) return '';
                    
                    const itemsHtml = evidence.map(item => {
                        const citations = item.citations 
                            ? item.citations.map(cite => `<span class="citation-tag">¶${cite}</span>`).join('') 
                            : '';
                        
                        return `
                        <div class="reference-block">
                            <div class="reference-header">
                                <span class="reference-title">${item.id}: ${item.title}</span>
                            </div>
                            <p class="reference-summary">${item.summary}</p>
                            ${citations ? `<div class="reference-citations">
                                <span style="font-size: 0.75rem; color: #718096;">Cited in:</span>
                                ${citations}
                            </div>` : ''}
                        </div>
                        `;
                    }).join('');
                    
                    return `
                    <div class="content-section">
                        <h6 class="content-section-title">Evidence</h6>
                        ${itemsHtml}
                    </div>
                    `;
                }
                
                // Render case law
                function renderCaseLaw(cases) {
                    if (!cases || cases.length === 0) return '';
                    
                    const itemsHtml = cases.map(item => {
                        const citedParagraphs = item.citedParagraphs 
                            ? item.citedParagraphs.map(para => `<span class="citation-tag">¶${para}</span>`).join('') 
                            : '';
                        
                        return `
                        <div class="reference-block">
                            <div class="reference-header">
                                <span class="reference-title">${item.caseNumber}</span>
                            </div>
                            <p class="reference-summary">${item.title}</p>
                            <p class="point-text">${item.relevance}</p>
                            ${citedParagraphs ? `<div class="reference-citations">
                                <span style="font-size: 0.75rem; color: #718096;">Key Paragraphs:</span>
                                ${citedParagraphs}
                            </div>` : ''}
                        </div>
                        `;
                    }).join('');
                    
                    return `
                    <div class="content-section">
                        <h6 class="content-section-title">Case Law</h6>
                        ${itemsHtml}
                    </div>
                    `;
                }
                
                // Render argument content
                function renderArgumentContent(arg) {
                    let content = '';
                    
                    // Overview points
                    if (arg.overview) {
                        content += renderOverviewPoints(arg.overview);
                    }
                    
                    // Legal points
                    if (arg.legalPoints) {
                        content += renderLegalPoints(arg.legalPoints);
                    }
                    
                    // Factual points
                    if (arg.factualPoints) {
                        content += renderFactualPoints(arg.factualPoints);
                    }
                    
                    // Evidence
                    if (arg.evidence) {
                        content += renderEvidence(arg.evidence);
                    }
                    
                    // Case law
                    if (arg.caseLaw) {
                        content += renderCaseLaw(arg.caseLaw);
                    }
                    
                    return content;
                }
                
                // Render a single argument including its children
                function renderArgument(arg, side, path = '', level = 0) {
                    if (!arg) return '';
                    
                    const argId = path ? `${path}-${arg.id}` : arg.id;
                    const fullId = `${side}-${argId}`;
                    
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
                        <svg id="chevron-${fullId}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0
