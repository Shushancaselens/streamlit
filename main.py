import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config and title remain the same
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Get argument data functions remain the same
def get_argument_data():
    # Same data structure as before
    # ...data structure code from previous example...
    # Using a simplified version to save space
    return {
        "claimantArgs": {
            "1": {
                "id": "1",
                "title": "Sporting Succession",
                "paragraphs": "15-18",
                "children": {
                    "1.1": {
                        "id": "1.1",
                        "title": "Club Name Analysis",
                        "paragraphs": "20-45"
                    },
                    "1.2": {
                        "id": "1.2",
                        "title": "Club Colors Analysis",
                        "paragraphs": "46-65"
                    }
                }
            },
            "2": {
                "id": "2",
                "title": "Doping Violation Chain of Custody",
                "paragraphs": "70-125"
            }
        },
        "respondentArgs": {
            "1": {
                "id": "1",
                "title": "Sporting Succession Rebuttal",
                "paragraphs": "200-218",
                "children": {
                    "1.1": {
                        "id": "1.1",
                        "title": "Club Name Analysis Rebuttal",
                        "paragraphs": "220-240"
                    },
                    "1.2": {
                        "id": "1.2",
                        "title": "Club Colors Analysis Rebuttal",
                        "paragraphs": "241-249"
                    }
                }
            },
            "2": {
                "id": "2",
                "title": "Doping Chain of Custody Defense",
                "paragraphs": "250-290"
            }
        },
        "topics": [
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
    }

def get_timeline_data():
    # Same timeline data
    return [
        {
            "date": "2023-01-15",
            "appellantVersion": "Contract signed with Club",
            "respondentVersion": "—",
            "status": "Undisputed"
        },
        # ... other timeline items ...
    ]

def get_exhibits_data():
    # Same exhibits data
    return [
        {
            "id": "C-1",
            "party": "Appellant",
            "title": "Employment Contract",
            "type": "contract",
            "summary": "Employment contract dated 15 January 2023 between Player and Club"
        },
        # ... other exhibit items ...
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
    
    # CSS and HTML structure remain mostly the same, but with modified JavaScript
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Same CSS styling as before */
            /* ... */
            
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
            }}
            .overview-bullet {{
                width: 6px;
                height: 6px;
                border-radius: 50%;
                background-color: #3182ce;
                margin-top: 0.5rem;
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
            
            /* Legal references styling */
            .legal-point {{
                background-color: #ebf8ff;
                border-radius: 0.5rem;
                padding: 0.75rem;
                margin-bottom: 0.5rem;
            }}
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
        <!-- Same HTML structure as before -->
        
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
            
            // Keep track of expanded states
            const expandedStates = {{}};
            
            // Tab switching (same as before)
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
            
            // View switching (same as before)
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
            
            // Content rendering functions remain the same
            function renderOverviewPoints(overview) {{ /* ... */ }}
            function renderLegalPoints(points) {{ /* ... */ }}
            function renderFactualPoints(points) {{ /* ... */ }}
            function renderEvidence(evidence) {{ /* ... */ }}
            function renderCaseLaw(cases) {{ /* ... */ }}
            function renderArgumentContent(arg) {{ /* ... */ }}
            
            // Modified toggle function that doesn't synchronize paired arguments
            function toggleArgument(id) {{
                const contentEl = document.getElementById(`content-${{id}}`);
                const childrenEl = document.getElementById(`children-${{id}}`);
                const chevronEl = document.getElementById(`chevron-${{id}}`);
                
                // Toggle this argument
                const isExpanded = contentEl.style.display === 'block';
                contentEl.style.display = isExpanded ? 'none' : 'block';
                if (chevronEl) {{
                    chevronEl.style.transform = isExpanded ? '' : 'rotate(90deg)';
                }}
                if (childrenEl) {{
                    childrenEl.style.display = isExpanded ? 'none' : 'block';
                }}
                
                // Save expanded state
                expandedStates[id] = !isExpanded;
                
                // No longer synchronizing with paired argument
            }}
            
            // Remaining functions remain the same
            function renderArgument(arg, side, path = '', level = 0) {{ /* ... */ }}
            function renderArgumentPair(claimantArg, respondentArg, topLevel = true) {{ /* ... */ }}
            function renderStandardArguments() {{ /* ... */ }}
            function renderTopicView() {{ /* ... */ }}
            function renderTimeline() {{ /* ... */ }}
            function renderExhibits() {{ /* ... */ }}
            
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
