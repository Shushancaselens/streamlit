import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Create data structures as JSON for embedded components
def get_argument_data():
    # This is a simplified version with just essential data
    claimant_args = {
        "1": {
            "id": "1",
            "title": "Sporting Succession",
            "paragraphs": "15-18"
        },
        "2": {
            "id": "2",
            "title": "Doping Violation Chain of Custody",
            "paragraphs": "70-125"
        }
    }
    
    respondent_args = {
        "1": {
            "id": "1",
            "title": "Sporting Succession Rebuttal",
            "paragraphs": "200-218"
        },
        "2": {
            "id": "2",
            "title": "Doping Chain of Custody Defense",
            "paragraphs": "250-290"
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
            "date": "2023-04-10",
            "appellantVersion": "Player was denied access to training facilities",
            "respondentVersion": "—",
            "status": "Disputed"
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
            .arguments-container {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
            }}
            .argument {{
                margin-bottom: 1rem;
                border: 1px solid #e2e8f0;
                border-radius: 0.375rem;
                overflow: hidden;
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
            }}
            .claimant-header {{
                background-color: #ebf8ff;
                border-color: #bee3f8;
            }}
            .respondent-header {{
                background-color: #fff5f5;
                border-color: #fed7d7;
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
            
            /* Badges */
            .badge {{
                padding: 0.25rem 0.5rem;
                border-radius: 0.25rem;
                font-size: 0.75rem;
            }}
            .appellant-badge {{
                background-color: #ebf8ff;
                color: #2b6cb0;
            }}
            .respondent-badge {{
                background-color: #fff5f5;
                color: #c53030;
            }}
            .type-badge {{
                background-color: #edf2f7;
                color: #4a5568;
            }}
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
            <div id="standard-view" class="view-content active">
                <div class="arguments-header">
                    <h3 class="claimant-color">Claimant's Arguments</h3>
                    <h3 class="respondent-color">Respondent's Arguments</h3>
                </div>
                <div id="standard-arguments-container" class="arguments-container"></div>
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
                    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
                    document.getElementById(tabId).classList.add('active');
                    
                    // Initialize content if needed
                    if (tabId === 'timeline') renderTimeline();
                    if (tabId === 'exhibits') renderExhibits();
                }});
            }});
            
            // View switching
            document.querySelectorAll('.view-btn').forEach(btn => {{
                btn.addEventListener('click', function() {{
                    // Update buttons
                    document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    
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
            
            // Render the standard arguments view
            function renderStandardArguments() {{
                const container = document.getElementById('standard-arguments-container');
                let html = '';
                
                // For each argument ID
                Object.keys(argsData.claimantArgs).forEach(argId => {{
                    if (argsData.respondentArgs[argId]) {{
                        const claimantArg = argsData.claimantArgs[argId];
                        const respondentArg = argsData.respondentArgs[argId];
                        
                        html += `
                        <div class="argument claimant-header">
                            <div class="argument-header" onclick="toggleArgument('claimant-${{argId}}')">
                                <div class="argument-header-left">
                                    <svg id="chevron-claimant-${{argId}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    <h5 style="font-size: 0.875rem; font-weight: 500; color: #3182ce;">
                                        ${{claimantArg.id}}. ${{claimantArg.title}}
                                    </h5>
                                </div>
                                <span style="font-size: 0.75rem; color: #3182ce; padding: 0.25rem 0.5rem; background-color: #ebf8ff; border-radius: 0.25rem;">¶${{claimantArg.paragraphs}}</span>
                            </div>
                            <div id="content-claimant-${{argId}}" class="argument-content">
                                <p>Detailed information about this argument would appear here when expanded.</p>
                            </div>
                        </div>
                        `;
                        
                        html += `
                        <div class="argument respondent-header">
                            <div class="argument-header" onclick="toggleArgument('respondent-${{argId}}')">
                                <div class="argument-header-left">
                                    <svg id="chevron-respondent-${{argId}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    <h5 style="font-size: 0.875rem; font-weight: 500; color: #e53e3e;">
                                        ${{respondentArg.id}}. ${{respondentArg.title}}
                                    </h5>
                                </div>
                                <span style="font-size: 0.75rem; color: #e53e3e; padding: 0.25rem 0.5rem; background-color: #fff5f5; border-radius: 0.25rem;">¶${{respondentArg.paragraphs}}</span>
                            </div>
                            <div id="content-respondent-${{argId}}" class="argument-content">
                                <p>Detailed information about this argument would appear here when expanded.</p>
                            </div>
                        </div>
                        `;
                    }}
                }});
                
                container.innerHTML = html;
            }}
            
            // Render the topic view
            function renderTopicView() {{
                const container = document.getElementById('topics-container');
                let html = '';
                
                argsData.topics.forEach(topic => {{
                    html += `
                    <div class="topic-section">
                        <h2 class="topic-title">${{topic.title}}</h2>
                        <p class="topic-description">${{topic.description}}</p>
                        
                        <div class="arguments-header">
                            <h3 class="claimant-color">Claimant's Arguments</h3>
                            <h3 class="respondent-color">Respondent's Arguments</h3>
                        </div>
                        
                        <div class="arguments-container">
                    `;
                    
                    // Add arguments for this topic
                    topic.argumentIds.forEach(argId => {{
                        if (argsData.claimantArgs[argId] && argsData.respondentArgs[argId]) {{
                            const claimantArg = argsData.claimantArgs[argId];
                            const respondentArg = argsData.respondentArgs[argId];
                            
                            html += `
                            <div class="argument claimant-header">
                                <div class="argument-header" onclick="toggleTopicArgument('claimant-${{argId}}', 'respondent-${{argId}}')">
                                    <div class="argument-header-left">
                                        <svg id="topic-chevron-claimant-${{argId}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <polyline points="9 18 15 12 9 6"></polyline>
                                        </svg>
                                        <h5 style="font-size: 0.875rem; font-weight: 500; color: #3182ce;">
                                            ${{claimantArg.id}}. ${{claimantArg.title}}
                                        </h5>
                                    </div>
                                    <span style="font-size: 0.75rem; color: #3182ce; padding: 0.25rem 0.5rem; background-color: #ebf8ff; border-radius: 0.25rem;">¶${{claimantArg.paragraphs}}</span>
                                </div>
                                <div id="topic-content-claimant-${{argId}}" class="argument-content">
                                    <p>Detailed information about this argument would appear here when expanded.</p>
                                </div>
                            </div>
                            
                            <div class="argument respondent-header">
                                <div class="argument-header" onclick="toggleTopicArgument('respondent-${{argId}}', 'claimant-${{argId}}')">
                                    <div class="argument-header-left">
                                        <svg id="topic-chevron-respondent-${{argId}}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <polyline points="9 18 15 12 9 6"></polyline>
                                        </svg>
                                        <h5 style="font-size: 0.875rem; font-weight: 500; color: #e53e3e;">
                                            ${{respondentArg.id}}. ${{respondentArg.title}}
                                        </h5>
                                    </div>
                                    <span style="font-size: 0.75rem; color: #e53e3e; padding: 0.25rem 0.5rem; background-color: #fff5f5; border-radius: 0.25rem;">¶${{respondentArg.paragraphs}}</span>
                                </div>
                                <div id="topic-content-respondent-${{argId}}" class="argument-content">
                                    <p>Detailed information about this argument would appear here when expanded.</p>
                                </div>
                            </div>
                            `;
                        }}
                    }});
                    
                    html += `
                        </div>
                    </div>
                    `;
                }});
                
                container.innerHTML = html;
            }}
            
            // Toggle argument expansion
            function toggleArgument(id) {{
                const content = document.getElementById(`content-${{id}}`);
                const chevron = document.getElementById(`chevron-${{id}}`);
                
                if (content.style.display === 'block') {{
                    content.style.display = 'none';
                    chevron.style.transform = 'rotate(0deg)';
                }} else {{
                    content.style.display = 'block';
                    chevron.style.transform = 'rotate(90deg)';
                    
                    // Synchronize paired argument
                    const pairType = id.split('-')[0];
                    const argId = id.split('-')[1];
                    const pairedType = pairType === 'claimant' ? 'respondent' : 'claimant';
                    const pairedId = `${{pairedType}}-${{argId}}`;
                    
                    const pairedContent = document.getElementById(`content-${{pairedId}}`);
                    const pairedChevron = document.getElementById(`chevron-${{pairedId}}`);
                    
                    if (pairedContent) {{
                        pairedContent.style.display = 'block';
                        pairedChevron.style.transform = 'rotate(90deg)';
                    }}
                }}
            }}
            
            // Toggle topic argument expansion
            function toggleTopicArgument(id, pairedId) {{
                const content = document.getElementById(`topic-content-${{id}}`);
                const chevron = document.getElementById(`topic-chevron-${{id}}`);
                const pairedContent = document.getElementById(`topic-content-${{pairedId}}`);
                const pairedChevron = document.getElementById(`topic-chevron-${{pairedId}}`);
                
                if (content.style.display === 'block') {{
                    content.style.display = 'none';
                    chevron.style.transform = 'rotate(0deg)';
                    pairedContent.style.display = 'none';
                    pairedChevron.style.transform = 'rotate(0deg)';
                }} else {{
                    content.style.display = 'block';
                    chevron.style.transform = 'rotate(90deg)';
                    pairedContent.style.display = 'block';
                    pairedChevron.style.transform = 'rotate(90deg)';
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
                    
                    row.innerHTML = `
                        <td>${{item.id}}</td>
                        <td><span class="badge ${{item.party.toLowerCase()}}-badge">${{item.party}}</span></td>
                        <td>${{item.title}}</td>
                        <td><span class="badge type-badge">${{item.type}}</span></td>
                        <td>${{item.summary}}</td>
                        <td style="text-align: right;"><a href="#" style="color: #3182ce; text-decoration: none;">View</a></td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Initialize page
            renderStandardArguments();
            renderTopicView();
            
            // Set up event listeners
            document.getElementById('timeline-search').addEventListener('input', renderTimeline);
            document.getElementById('disputed-only').addEventListener('change', renderTimeline);
            document.getElementById('exhibits-search').addEventListener('input', renderExhibits);
            document.getElementById('party-filter').addEventListener('change', renderExhibits);
            document.getElementById('type-filter').addEventListener('change', renderExhibits);
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
