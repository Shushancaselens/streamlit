import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# [All the data functions remain the same]

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
    
    # Create a single HTML component with debugging statements
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Base styles */
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                margin: 0;
                padding: 0;
            }}
            
            /* Main container */
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            /* Tabs */
            .tabs {{
                display: flex;
                border-bottom: 1px solid #e1e4e8;
                margin-bottom: 20px;
            }}
            
            .tab {{
                padding: 10px 16px;
                cursor: pointer;
                margin-right: 4px;
            }}
            
            .tab.active {{
                color: #2060e5;
                border-bottom: 2px solid #2060e5;
                font-weight: 500;
            }}
            
            /* Content areas */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* Two-column layout */
            .two-columns {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 24px;
            }}
            
            /* Argument titles */
            .args-title {{
                font-size: 18px;
                font-weight: 500;
                margin-bottom: 16px;
            }}
            
            .claimant-title {{
                color: #2060e5;
            }}
            
            .respondent-title {{
                color: #e53e3e;
            }}
            
            /* Argument cards */
            .arg-card {{
                border: 1px solid #e1e4e8;
                border-radius: 6px;
                margin-bottom: 16px;
                overflow: hidden;
            }}
            
            .arg-header {{
                padding: 12px 16px;
                background-color: #f6f8fa;
                border-bottom: 1px solid #e1e4e8;
                display: flex;
                justify-content: space-between;
                align-items: center;
                cursor: pointer;
            }}
            
            .arg-title {{
                display: flex;
                align-items: center;
                gap: 8px;
                font-weight: 500;
            }}
            
            .arg-content {{
                padding: 16px;
                display: none;
            }}
            
            /* Chevron */
            .chevron {{
                transition: transform 0.2s;
            }}
            
            .chevron.expanded {{
                transform: rotate(90deg);
            }}
            
            /* Badges */
            .subarg-badge {{
                background-color: rgba(32, 96, 229, 0.1);
                color: #2060e5;
                padding: 3px 8px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 500;
            }}
            
            .subarg-badge.respondent {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            /* Content sections */
            .section {{
                margin-bottom: 20px;
            }}
            
            .section-header {{
                font-weight: 500;
                margin-bottom: 10px;
            }}
            
            /* List items */
            .point-list {{
                list-style-type: none;
                padding-left: 0;
            }}
            
            .point-list li {{
                padding-left: 16px;
                position: relative;
                margin-bottom: 8px;
            }}
            
            .point-list li:before {{
                content: "•";
                position: absolute;
                left: 0;
                color: #666;
            }}
            
            /* Evidence block */
            .evidence-block {{
                background-color: #fff8f0;
                border-left: 3px solid #dd6b20;
                padding: 12px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            /* Legal block */
            .legal-block {{
                background-color: #ebf8ff;
                border-left: 3px solid #2060e5;
                padding: 12px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            /* Nested arguments */
            .nested-args {{
                margin-top: 16px;
                border-left: 2px solid #f0f0f0;
                padding-left: 16px;
            }}
            
            /* Debug info */
            .debug-info {{
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 10px;
                margin: 10px 0;
                font-family: monospace;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Legal Arguments Analysis</h1>
            
            <!-- Debug info -->
            <div class="debug-info" id="debug-info">Debug information will appear here</div>
            
            <!-- Tabs -->
            <div class="tabs">
                <div class="tab active" data-tab="arguments">Summary of Arguments</div>
                <div class="tab" data-tab="timeline">Timeline</div>
                <div class="tab" data-tab="exhibits">Exhibits</div>
            </div>
            
            <!-- Arguments tab content -->
            <div id="arguments" class="tab-content active">
                <div class="two-columns">
                    <!-- Claimant's Arguments -->
                    <div>
                        <h2 class="args-title claimant-title">Claimant's Arguments</h2>
                        <div id="claimant-args"></div>
                    </div>
                    
                    <!-- Respondent's Arguments -->
                    <div>
                        <h2 class="args-title respondent-title">Respondent's Arguments</h2>
                        <div id="respondent-args"></div>
                    </div>
                </div>
            </div>
            
            <!-- Timeline tab content -->
            <div id="timeline" class="tab-content">
                <h2>Case Timeline</h2>
                <table id="timeline-table" style="width:100%; border-collapse: collapse;">
                    <thead>
                        <tr>
                            <th style="text-align:left; padding:8px;">Date</th>
                            <th style="text-align:left; padding:8px;">Appellant's Version</th>
                            <th style="text-align:left; padding:8px;">Respondent's Version</th>
                            <th style="text-align:left; padding:8px;">Status</th>
                        </tr>
                    </thead>
                    <tbody id="timeline-body"></tbody>
                </table>
            </div>
            
            <!-- Exhibits tab content -->
            <div id="exhibits" class="tab-content">
                <h2>Case Exhibits</h2>
                <table id="exhibits-table" style="width:100%; border-collapse: collapse;">
                    <thead>
                        <tr>
                            <th style="text-align:left; padding:8px;">ID</th>
                            <th style="text-align:left; padding:8px;">Party</th>
                            <th style="text-align:left; padding:8px;">Title</th>
                            <th style="text-align:left; padding:8px;">Type</th>
                            <th style="text-align:left; padding:8px;">Summary</th>
                        </tr>
                    </thead>
                    <tbody id="exhibits-body"></tbody>
                </table>
            </div>
        </div>
        
        <script>
            // Debug function
            function debug(message) {{
                const debugElement = document.getElementById('debug-info');
                if (debugElement) {{
                    debugElement.innerHTML += message + '<br>';
                }}
                console.log(message);
            }}
            
            // Try/catch wrapper for initialization
            try {{
                debug("Starting initialization...");
                
                // Parse data from JSON
                const argsData = {args_json};
                const timelineData = {timeline_json};
                const exhibitsData = {exhibits_json};
                
                debug("Data loaded successfully.");
                
                // Tab switching
                document.querySelectorAll('.tab').forEach(tab => {{
                    tab.addEventListener('click', function() {{
                        // Update tabs
                        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                        this.classList.add('active');
                        
                        // Update content
                        const tabId = this.getAttribute('data-tab');
                        document.querySelectorAll('.tab-content').forEach(content => {{
                            content.classList.remove('active');
                        }});
                        document.getElementById(tabId).classList.add('active');
                        
                        debug("Switched to tab: " + tabId);
                    }});
                }});
                
                // Toggle argument function
                window.toggleArgument = function(id) {{
                    debug("Toggling argument: " + id);
                    const content = document.getElementById('content-' + id);
                    const chevron = document.getElementById('chevron-' + id);
                    
                    if (content) {{
                        if (content.style.display === 'block') {{
                            content.style.display = 'none';
                            if (chevron) chevron.classList.remove('expanded');
                        }} else {{
                            content.style.display = 'block';
                            if (chevron) chevron.classList.add('expanded');
                        }}
                    }} else {{
                        debug("ERROR: Content element not found for ID: " + id);
                    }}
                }};
                
                // Count subarguments
                function countSubarguments(arg) {{
                    if (!arg || !arg.children) return 0;
                    
                    let count = Object.keys(arg.children).length;
                    Object.values(arg.children).forEach(child => {{
                        count += countSubarguments(child);
                    }});
                    
                    return count;
                }}
                
                // Render key points
                function renderKeyPoints(overview) {{
                    if (!overview || !overview.points || overview.points.length === 0) return '';
                    
                    const pointsList = overview.points.map(point => `<li>${{point}}</li>`).join('');
                    
                    return `
                    <div class="section">
                        <div class="section-header">Key Points</div>
                        <ul class="point-list">
                            ${{pointsList}}
                        </ul>
                    </div>
                    `;
                }}
                
                // Render factual points
                function renderFactualPoints(points) {{
                    if (!points || points.length === 0) return '';
                    
                    const pointsList = points.map(point => `<li>${{point.point}}</li>`).join('');
                    
                    return `
                    <div class="section">
                        <div class="section-header">Factual Points</div>
                        <ul class="point-list">
                            ${{pointsList}}
                        </ul>
                    </div>
                    `;
                }}
                
                // Render evidence
                function renderEvidence(evidence) {{
                    if (!evidence || evidence.length === 0) return '';
                    
                    const evidenceHtml = evidence.map(item => `
                        <div class="evidence-block">
                            <strong>${{item.id}}: ${{item.title}}</strong>
                            <div style="margin-top:6px">${{item.summary}}</div>
                        </div>
                    `).join('');
                    
                    return `
                    <div class="section">
                        <div class="section-header">Evidence</div>
                        ${{evidenceHtml}}
                    </div>
                    `;
                }}
                
                // Render legal points
                function renderLegalPoints(caseLaw) {{
                    if (!caseLaw || caseLaw.length === 0) return '';
                    
                    const legalHtml = caseLaw.map(item => `
                        <div class="legal-block">
                            <strong>${{item.caseNumber}}: ${{item.title}}</strong>
                            <div style="margin-top:6px">${{item.relevance}}</div>
                        </div>
                    `).join('');
                    
                    return `
                    <div class="section">
                        <div class="section-header">Legal Points</div>
                        ${{legalHtml}}
                    </div>
                    `;
                }}
                
                // Render subarguments
                function renderSubarguments(children, party) {{
                    if (!children || Object.keys(children).length === 0) return '';
                    
                    const subargumentsHtml = Object.values(children).map(child => {{
                        const subId = party + '-' + child.id;
                        const subCount = countSubarguments(child);
                        const subCountBadge = subCount > 0 
                            ? `<span class="subarg-badge ${{party === 'respondent' ? 'respondent' : ''}}">${{subCount}} subargument${{subCount !== 1 ? 's' : ''}}</span>` 
                            : '';
                        
                        return `
                        <div class="arg-card">
                            <div class="arg-header" onclick="toggleArgument('${{subId}}')">
                                <div class="arg-title">
                                    <svg id="chevron-${{subId}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    ${{child.id}}. ${{child.title}}
                                </div>
                                ${{subCountBadge}}
                            </div>
                            <div class="arg-content" id="content-${{subId}}">
                                ${{renderKeyPoints(child.overview)}}
                                ${{renderFactualPoints(child.factualPoints)}}
                                ${{renderEvidence(child.evidence)}}
                                ${{renderLegalPoints(child.caseLaw)}}
                                
                                ${{renderSubarguments(child.children, party)}}
                            </div>
                        </div>
                        `;
                    }}).join('');
                    
                    return `<div class="nested-args">${{subargumentsHtml}}</div>`;
                }}
                
                // Render main arguments
                function renderMainArguments(args, container, party) {{
                    if (!args || Object.keys(args).length === 0) {{
                        debug("No arguments found for " + party);
                        return;
                    }}
                    
                    let html = '';
                    
                    // Loop through each argument
                    Object.values(args).forEach(arg => {{
                        const argId = party + '-' + arg.id;
                        const subCount = countSubarguments(arg);
                        const subCountBadge = subCount > 0 
                            ? `<span class="subarg-badge ${{party === 'respondent' ? 'respondent' : ''}}">${{subCount}} subargument${{subCount !== 1 ? 's' : ''}}</span>` 
                            : '';
                        
                        html += `
                        <div class="arg-card">
                            <div class="arg-header" onclick="toggleArgument('${{argId}}')">
                                <div class="arg-title">
                                    <svg id="chevron-${{argId}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    ${{arg.id}}. ${{arg.title}}
                                </div>
                                ${{subCountBadge}}
                            </div>
                            <div class="arg-content" id="content-${{argId}}">
                                ${{renderKeyPoints(arg.overview)}}
                                ${{renderFactualPoints(arg.factualPoints)}}
                                ${{renderEvidence(arg.evidence)}}
                                ${{renderLegalPoints(arg.caseLaw)}}
                                
                                ${{renderSubarguments(arg.children, party)}}
                            </div>
                        </div>
                        `;
                    }});
                    
                    // Set the HTML to the container
                    const containerElement = document.getElementById(container);
                    if (containerElement) {{
                        containerElement.innerHTML = html;
                        debug(party + " arguments rendered successfully.");
                    }} else {{
                        debug("ERROR: Container element not found: " + container);
                    }}
                }}
                
                // Initialize everything when the DOM is loaded
                document.addEventListener('DOMContentLoaded', function() {{
                    debug("DOM loaded, rendering arguments...");
                    
                    // Render claimant arguments
                    renderMainArguments(argsData.claimantArgs, 'claimant-args', 'claimant');
                    
                    // Render respondent arguments
                    renderMainArguments(argsData.respondentArgs, 'respondent-args', 'respondent');
                    
                    // Load timeline data (will be displayed if timeline tab is clicked)
                    document.querySelector('.tab[data-tab="timeline"]').addEventListener('click', function() {{
                        const timelineBody = document.getElementById('timeline-body');
                        if (timelineBody && timelineData.length > 0) {{
                            timelineBody.innerHTML = timelineData.map(item => `
                                <tr>
                                    <td style="padding:8px; border-bottom:1px solid #ddd;">${{item.date}}</td>
                                    <td style="padding:8px; border-bottom:1px solid #ddd;">${{item.appellantVersion}}</td>
                                    <td style="padding:8px; border-bottom:1px solid #ddd;">${{item.respondentVersion}}</td>
                                    <td style="padding:8px; border-bottom:1px solid #ddd;">${{item.status}}</td>
                                </tr>
                            `).join('');
                            debug("Timeline rendered successfully.");
                        }}
                    }});
                    
                    // Load exhibits data (will be displayed if exhibits tab is clicked)
                    document.querySelector('.tab[data-tab="exhibits"]').addEventListener('click', function() {{
                        const exhibitsBody = document.getElementById('exhibits-body');
                        if (exhibitsBody && exhibitsData.length > 0) {{
                            exhibitsBody.innerHTML = exhibitsData.map(item => `
                                <tr>
                                    <td style="padding:8px; border-bottom:1px solid #ddd;">${{item.id}}</td>
                                    <td style="padding:8px; border-bottom:1px solid #ddd;">${{item.party}}</td>
                                    <td style="padding:8px; border-bottom:1px solid #ddd;">${{item.title}}</td>
                                    <td style="padding:8px; border-bottom:1px solid #ddd;">${{item.type}}</td>
                                    <td style="padding:8px; border-bottom:1px solid #ddd;">${{item.summary}}</td>
                                </tr>
                            `).join('');
                            debug("Exhibits rendered successfully.");
                        }}
                    }});
                    
                    debug("Initialization complete.");
                }});
                
                // Also try to render arguments immediately in case DOMContentLoaded already fired
                debug("Trying immediate render...");
                renderMainArguments(argsData.claimantArgs, 'claimant-args', 'claimant');
                renderMainArguments(argsData.respondentArgs, 'respondent-args', 'respondent');
                
            }} catch (error) {{
                // Display any errors in the debug area
                debug("ERROR: " + error.message);
                debug("Stack trace: " + error.stack);
            }}
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Legal Arguments Analysis")
    components.html(html_content, height=900, scrolling=True)

if __name__ == "__main__":
    main()
