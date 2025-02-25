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
                        }
                    ]
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
            ]
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
                    ]
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
            ]
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

# Main app
def main():
    # Get the data for JavaScript
    args_data = get_argument_data()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    
    # Title
    st.title("Legal Arguments Analysis")
    
    # Create HTML component focusing on arguments section only
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
            .content-section {
                margin-bottom: 1.5rem;
            }
            .content-section-title {
                font-size: 0.875rem;
                font-weight: 500;
                margin-bottom: 0.5rem;
            }
            .point-text {
                font-size: 0.875rem;
                color: #4a5568;
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
            // Initialize data
            const argsData = """ + args_json + """;
            
            // Keep track of expanded states
            const expandedStates = {};
            
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
                    return `
                    <div class="reference-block">
                        <div class="reference-header">
                            <span class="reference-title">${item.id}: ${item.title}</span>
                        </div>
                        <p class="point-text">${item.summary}</p>
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
                
                return content;
            }
            
            // Render a single argument including its children
            function renderArgument(arg, side, path = '') {
                if (!arg) return '';
                
                const argId = path ? `${path}-${arg.id}` : arg.id;
                const fullId = `${side}-${argId}`;
                
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const childCount = hasChildren ? Object.keys(arg.children).length : 0;
                
                // Style based on side
                const baseColor = side === 'claimant' ? '#3182ce' : '#e53e3e';
                const headerClass = side === 'claimant' ? 'claimant-header' : 'respondent-header';
                const badgeClass = side === 'claimant' ? 'claimant-badge' : 'respondent-badge';
                
                // Header content
                const headerHtml = `
                <div class="argument-header-left">
                    <svg id="chevron-${fullId}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s ease;">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                    <h5 style="font-size: 0.875rem; font-weight: 500; color: ${baseColor};">
                        ${arg.id}. ${arg.title}
                    </h5>
                </div>
                <div>
                    ${hasChildren 
                        ? `<span class="badge ${badgeClass}" style="border-radius: 9999px;">${childCount} subarguments</span>` 
                        : `<span class="badge ${badgeClass}">¶${arg.paragraphs}</span>`
                    }
                </div>
                `;
                
                // Detailed content
                const contentHtml = renderArgumentContent(arg);
                
                // Child arguments
                let childrenHtml = '';
                if (hasChildren) {
                    const childrenArgs = Object.values(arg.children).map(child => {
                        return renderArgument(child, side, argId);
                    }).join('');
                    
                    childrenHtml = `
                    <div id="children-${fullId}" class="argument-children">
                        ${childrenArgs}
                    </div>
                    `;
                }
                
                // Complete argument HTML
                return `
                <div class="argument ${headerClass}">
                    <div class="argument-header" onclick="toggleArgument('${fullId}', '${argId}')">
                        ${headerHtml}
                    </div>
                    <div id="content-${fullId}" class="argument-content">
                        ${contentHtml}
                    </div>
                    ${childrenHtml}
                </div>
                `;
            }
            
            // Render a pair of arguments (claimant and respondent)
            function renderArgumentPair(claimantArg, respondentArg) {
                return `
                <div class="argument-pair">
                    <div class="argument-side">
                        ${renderArgument(claimantArg, 'claimant')}
                    </div>
                    <div class="argument-side">
                        ${renderArgument(respondentArg, 'respondent')}
                    </div>
                </div>
                `;
            }
            
            // Render the standard arguments view
            function renderStandardArguments() {
                const container = document.getElementById('standard-arguments-container');
                let html = '';
                
                // For each top-level argument
                Object.keys(argsData.claimantArgs).forEach(argId => {
                    if (argsData.respondentArgs[argId]) {
                        const claimantArg = argsData.claimantArgs[argId];
                        const respondentArg = argsData.respondentArgs[argId];
                        
                        html += renderArgumentPair(claimantArg, respondentArg);
                    }
                });
                
                container.innerHTML = html;
            }
            
            // Render the topic view
            function renderTopicView() {
                const container = document.getElementById('topics-container');
                let html = '';
                
                // For each topic
                argsData.topics.forEach(topic => {
                    html += `
                    <div class="topic-section">
                        <h2 class="topic-title">${topic.title}</h2>
                        <p class="topic-description">${topic.description}</p>
                        
                        <div class="arguments-header">
                            <h3 class="claimant-color">Claimant's Arguments</h3>
                            <h3 class="respondent-color">Respondent's Arguments</h3>
                        </div>
                    `;
                    
                    // Add arguments for this topic
                    topic.argumentIds.forEach(argId => {
                        if (argsData.claimantArgs[argId] && argsData.respondentArgs[argId]) {
                            const claimantArg = argsData.claimantArgs[argId];
                            const respondentArg = argsData.respondentArgs[argId];
                            
                            html += renderArgumentPair(claimantArg, respondentArg);
                        }
                    });
                    
                    html += `</div>`;
                });
                
                container.innerHTML = html;
            }
            
            // Toggle argument expansion
            function toggleArgument(fullId, argPath) {
                // Determine the side (claimant or respondent)
                const [side, ...rest] = fullId.split('-');
                
                // Toggle this argument
                const contentEl = document.getElementById(`content-${fullId}`);
                const childrenEl = document.getElementById(`children-${fullId}`);
                const chevronEl = document.getElementById(`chevron-${fullId}`);
                
                const isExpanded = contentEl.style.display === 'block';
                contentEl.style.display = isExpanded ? 'none' : 'block';
                if (chevronEl) {
                    chevronEl.style.transform = isExpanded ? '' : 'rotate(90deg)';
                }
                if (childrenEl) {
                    childrenEl.style.display = isExpanded ? 'none' : 'block';
                }
                
                // Save expanded state
                expandedStates[fullId] = !isExpanded;
                
                // Find and toggle the paired argument based on the path
                const otherSide = side === 'claimant' ? 'respondent' : 'claimant';
                const pairedId = `${otherSide}-${argPath}`;
                
                const pairedContentEl = document.getElementById(`content-${pairedId}`);
                const pairedChildrenEl = document.getElementById(`children-${pairedId}`);
                const pairedChevronEl = document.getElementById(`chevron-${pairedId}`);
                
                if (pairedContentEl) {
                    pairedContentEl.style.display = contentEl.style.display;
                    expandedStates[pairedId] = expandedStates[fullId];
                }
                
                if (pairedChevronEl) {
                    pairedChevronEl.style.transform = chevronEl.style.transform;
                }
                
                if (pairedChildrenEl) {
                    pairedChildrenEl.style.display = isExpanded ? 'none' : 'block';
                }
            }
            
            // Initialize the page
            renderStandardArguments();
            renderTopicView();
            
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
