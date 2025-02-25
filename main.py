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

# Main app
def main():
    # Get the data for JavaScript
    args_data = get_argument_data()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    
    # Title
    st.title("Legal Arguments Analysis")
    
    # Define the HTML/JS content separately to avoid f-string issues
    html_head = """
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
            .claimant-color { color: #3182ce; }
            .respondent-color { color: #e53e3e; }
            .argument-pair {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
                margin-bottom: 1rem;
                position: relative;
            }
            .argument-side { position: relative; }
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
            .content-section {
                margin-bottom: 1.5rem;
            }
            .overview-block {
                background-color: #f7fafc;
                border-radius: 0.5rem;
                padding: 1rem;
                margin-bottom: 1rem;
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
            .topic-section {
                margin-bottom: 2rem;
            }
            .topic-title {
                font-size: 1.25rem;
                font-weight: 600;
                color: #2d3748;
                margin-bottom: 0.25rem;
            }
        </style>
    </head>
    """
    
    html_body = """
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
    """
    
    html_script_part1 = """
        <script>
            // Initialize data with the JSON
            const argsData = 
    """
    
    html_script_part2 = """
            
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
            
            // Render a single argument
            function renderArgument(arg, side) {
                if (!arg) return '';
                
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const headerClass = side === 'claimant' ? 'claimant-header' : 'respondent-header';
                const badgeClass = side === 'claimant' ? 'claimant-badge' : 'respondent-badge';
                
                let content = `
                <div class="argument ${headerClass}">
                    <div class="argument-header">
                        <div class="argument-header-left">
                            <h5 style="font-size: 0.875rem; font-weight: 500;">
                                ${arg.id}. ${arg.title}
                            </h5>
                        </div>
                        <span class="badge ${badgeClass}">¶${arg.paragraphs}</span>
                    </div>
                    <div class="argument-content">
                `;
                
                // Display overview if available
                if (arg.overview && arg.overview.points) {
                    content += `<div class="content-section"><h6>Key Points:</h6>`;
                    content += `<div class="overview-block"><ul>`;
                    arg.overview.points.forEach(point => {
                        content += `<li>${point}</li>`;
                    });
                    content += `</ul></div></div>`;
                }
                
                // Display legal points if available
                if (arg.legalPoints && arg.legalPoints.length > 0) {
                    content += `<div class="content-section"><h6>Legal Points:</h6>`;
                    arg.legalPoints.forEach(point => {
                        content += `<div class="legal-badge">${point.point}</div>`;
                    });
                    content += `</div>`;
                }
                
                content += `</div></div>`;
                
                // Add children if available
                if (hasChildren) {
                    content += `<div class="argument-children">`;
                    Object.values(arg.children).forEach(child => {
                        content += renderArgument(child, side);
                    });
                    content += `</div>`;
                }
                
                return content;
            }
            
            // Render arguments in pairs
            function renderArgumentPairs() {
                const container = document.getElementById('standard-arguments-container');
                let html = '';
                
                // For each top-level argument
                Object.keys(argsData.claimantArgs).forEach(argId => {
                    if (argsData.respondentArgs[argId]) {
                        const claimantArg = argsData.claimantArgs[argId];
                        const respondentArg = argsData.respondentArgs[argId];
                        
                        html += `
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
                });
                
                container.innerHTML = html;
            }
            
            // Render topic view
            function renderTopicView() {
                const container = document.getElementById('topics-container');
                let html = '';
                
                argsData.topics.forEach(topic => {
                    html += `
                    <div class="topic-section">
                        <h2 class="topic-title">${topic.title}</h2>
                        <p>${topic.description}</p>
                        
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
                            
                            html += `
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
                    });
                    
                    html += `</div>`;
                });
                
                container.innerHTML = html;
            }
            
            // Initialize the views
            renderArgumentPairs();
            renderTopicView();
            
            // Set initial active button style
            document.querySelector('.view-btn.active').style.backgroundColor = 'white';
            document.querySelector('.view-btn.active').style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';
            
            // Add expansion functionality
            document.querySelectorAll('.argument-header').forEach(header => {
                header.addEventListener('click', function() {
                    const content = this.nextElementSibling;
                    content.style.display = content.style.display === 'block' ? 'none' : 'block';
                });
            });
        </script>
    </body>
    </html>
    """
    
    # Build the complete HTML
    html_content = html_head + html_body + html_script_part1 + args_json + html_script_part2
    
    # Render the HTML in Streamlit
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
