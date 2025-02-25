import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Create data structures as JSON for embedded components
def get_argument_data():
    # Same data structure as before
    # ...
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args,
        "topics": topics
    }

def get_timeline_data():
    # Same timeline data as before
    # ...

def get_exhibits_data():
    # Same exhibits data as before
    # ...

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
    
    # Create a single HTML component containing the full UI with minimalistic design
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Minimalistic base styling */
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                margin: 0;
                padding: 0;
                background-color: #fff;
            }}
            
            /* Simple container */
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            /* Header styles */
            .header {{
                margin-bottom: 20px;
            }}
            
            .tabs {{
                display: flex;
                border-bottom: 1px solid #e1e4e8;
                margin-bottom: 25px;
            }}
            
            .tab {{
                padding: 12px 16px;
                cursor: pointer;
                color: #586069;
                border-bottom: 2px solid transparent;
                margin-right: 4px;
            }}
            
            .tab.active {{
                color: #2060e5;
                border-bottom: 2px solid #2060e5;
                font-weight: 500;
            }}
            
            /* Main content styles */
            .content-area {{
                display: none;
            }}
            
            .content-area.active {{
                display: block;
            }}
            
            /* Sections */
            .section-title {{
                font-size: 18px;
                font-weight: 500;
                margin-bottom: 20px;
            }}
            
            .claimant-title {{
                color: #2060e5;
            }}
            
            .respondent-title {{
                color: #e53e3e;
            }}
            
            /* Split layout */
            .split-layout {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 24px;
            }}
            
            /* Argument card */
            .argument-card {{
                border: 1px solid #e1e4e8;
                border-radius: 8px;
                margin-bottom: 16px;
                overflow: hidden;
            }}
            
            .argument-header {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 15px;
                cursor: pointer;
                background-color: #f6f8fa;
                border-bottom: 1px solid #e1e4e8;
            }}
            
            .argument-title {{
                display: flex;
                align-items: center;
                gap: 8px;
                font-weight: 500;
            }}
            
            .argument-content {{
                padding: 15px;
                display: none;
            }}
            
            .subargument-badge {{
                background-color: rgba(32, 96, 229, 0.1);
                color: #2060e5;
                padding: 4px 10px;
                border-radius: 16px;
                font-size: 12px;
                font-weight: 500;
            }}
            
            .subargument-badge.respondent {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            /* Chevron */
            .chevron {{
                transition: transform 0.2s;
            }}
            
            .chevron.expanded {{
                transform: rotate(90deg);
            }}
            
            /* Content sections */
            .content-section {{
                margin-bottom: 20px;
            }}
            
            .section-header {{
                font-weight: 500;
                margin-bottom: 10px;
            }}
            
            .point-list {{
                list-style-type: none;
                padding-left: 0;
                margin: 0;
            }}
            
            .point-list li {{
                position: relative;
                padding-left: 20px;
                margin-bottom: 8px;
            }}
            
            .point-list li:before {{
                content: "•";
                position: absolute;
                left: 0;
                color: #8c8c8c;
            }}
            
            /* Evidence block */
            .evidence-block {{
                background-color: #fff8f0;
                border-left: 3px solid #dd6b20;
                padding: 10px 16px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            /* Legal point block */
            .legal-block {{
                background-color: #ebf8ff;
                border-left: 3px solid #3182ce;
                padding: 10px 16px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            /* Tabs for Timeline and Exhibits */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* Tables */
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 16px;
            }}
            
            thead {{
                background-color: #f6f8fa;
            }}
            
            th, td {{
                padding: 12px 16px;
                text-align: left;
                border-bottom: 1px solid #e1e4e8;
            }}
            
            /* Badges */
            .badge {{
                display: inline-block;
                padding: 3px 8px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 500;
            }}
            
            .disputed-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            .exhibit-badge {{
                background-color: rgba(221, 107, 32, 0.1);
                color: #dd6b20;
            }}
            
            /* Subarguments */
            .subarguments-container {{
                margin-top: 12px;
                border-left: 2px solid #f0f0f0;
                padding-left: 16px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Legal Arguments Analysis</h1>
                <div class="tabs">
                    <div class="tab active" data-tab="summary">Summary of Arguments</div>
                    <div class="tab" data-tab="timeline">Timeline</div>
                    <div class="tab" data-tab="exhibits">Exhibits</div>
                </div>
            </div>
            
            <!-- Summary tab content -->
            <div id="summary" class="content-area active">
                <div class="split-layout">
                    <!-- Claimant's arguments -->
                    <div>
                        <h2 class="section-title claimant-title">Claimant's Arguments</h2>
                        <div id="claimant-arguments"></div>
                    </div>
                    
                    <!-- Respondent's arguments -->
                    <div>
                        <h2 class="section-title respondent-title">Respondent's Arguments</h2>
                        <div id="respondent-arguments"></div>
                    </div>
                </div>
            </div>
            
            <!-- Timeline tab content -->
            <div id="timeline" class="content-area">
                <table id="timeline-table">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Appellant's Version</th>
                            <th>Respondent's Version</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody id="timeline-body"></tbody>
                </table>
            </div>
            
            <!-- Exhibits tab content -->
            <div id="exhibits" class="content-area">
                <table id="exhibits-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Party</th>
                            <th>Title</th>
                            <th>Type</th>
                            <th>Summary</th>
                        </tr>
                    </thead>
                    <tbody id="exhibits-body"></tbody>
                </table>
            </div>
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
                    
                    // Update content areas
                    const tabId = this.getAttribute('data-tab');
                    document.querySelectorAll('.content-area').forEach(content => {{
                        content.classList.remove('active');
                    }});
                    document.getElementById(tabId).classList.add('active');
                    
                    // Initialize content if needed
                    if (tabId === 'timeline') renderTimeline();
                    if (tabId === 'exhibits') renderExhibits();
                }});
            }});
            
            // Toggle argument details
            function toggleArgument(id) {{
                const content = document.getElementById(`content-${{id}}`);
                const chevron = document.getElementById(`chevron-${{id}}`);
                
                if (content.style.display === 'block') {{
                    content.style.display = 'none';
                    chevron.classList.remove('expanded');
                }} else {{
                    content.style.display = 'block';
                    chevron.classList.add('expanded');
                }}
            }}
            
            // Count subarguments
            function countSubarguments(arg) {{
                let count = 0;
                if (arg.children) {{
                    count += Object.keys(arg.children).length;
                    
                    // Also count descendant subarguments
                    Object.values(arg.children).forEach(child => {{
                        if (child.children) {{
                            count += countSubarguments(child);
                        }}
                    }});
                }}
                return count;
            }}
            
            // Render key points
            function renderKeyPoints(overview) {{
                if (!overview || !overview.points || overview.points.length === 0) return '';
                
                const pointsHtml = overview.points.map(point => `<li>${{point}}</li>`).join('');
                
                return `
                <div class="content-section">
                    <div class="section-header">Key Points</div>
                    <ul class="point-list">
                        ${{pointsHtml}}
                    </ul>
                </div>
                `;
            }}
            
            // Render factual points
            function renderFactualPoints(points) {{
                if (!points || points.length === 0) return '';
                
                const pointsHtml = points.map(point => {{
                    const disputed = point.isDisputed 
                        ? `<span class="badge disputed-badge">Disputed</span>` 
                        : '';
                    
                    return `<li>${{point.point}} ${{disputed}}</li>`;
                }}).join('');
                
                return `
                <div class="content-section">
                    <div class="section-header">Factual Points</div>
                    <ul class="point-list">
                        ${{pointsHtml}}
                    </ul>
                </div>
                `;
            }}
            
            // Render evidence
            function renderEvidence(evidence) {{
                if (!evidence || evidence.length === 0) return '';
                
                const evidenceHtml = evidence.map(item => {{
                    return `
                    <div class="evidence-block">
                        <div style="font-weight: 500;">${{item.id}}: ${{item.title}}</div>
                        <div style="margin-top: 6px;">${{item.summary}}</div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="content-section">
                    <div class="section-header">Evidence</div>
                    ${{evidenceHtml}}
                </div>
                `;
            }}
            
            // Render legal points
            function renderLegalPoints(caseLaw) {{
                if (!caseLaw || caseLaw.length === 0) return '';
                
                const legalHtml = caseLaw.map(item => {{
                    return `
                    <div class="legal-block">
                        <div style="font-weight: 500;">${{item.caseNumber}}: ${{item.title}}</div>
                        <div style="margin-top: 6px;">${{item.relevance}}</div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="content-section">
                    <div class="section-header">Legal Points</div>
                    ${{legalHtml}}
                </div>
                `;
            }}
            
            // Render subarguments
            function renderSubarguments(children, party) {{
                if (!children || Object.keys(children).length === 0) return '';
                
                const subargumentsHtml = Object.values(children).map(child => {{
                    const subCount = countSubarguments(child);
                    const subCountBadge = subCount > 0 
                        ? `<span class="subargument-badge ${{party === 'respondent' ? 'respondent' : ''}}">${{subCount}} subargument${{subCount !== 1 ? 's' : ''}}</span>` 
                        : '';
                    
                    return `
                    <div class="argument-card">
                        <div class="argument-header" onclick="toggleArgument('${{party}}-${{child.id}}')">
                            <div class="argument-title">
                                <svg id="chevron-${{party}}-${{child.id}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                ${{child.id}}. ${{child.title}}
                            </div>
                            ${{subCountBadge}}
                        </div>
                        <div class="argument-content" id="content-${{party}}-${{child.id}}">
                            ${{renderKeyPoints(child.overview)}}
                            ${{renderFactualPoints(child.factualPoints)}}
                            ${{renderEvidence(child.evidence)}}
                            ${{renderLegalPoints(child.caseLaw)}}
                            
                            ${{child.children ? renderSubarguments(child.children, party) : ''}}
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div class="subarguments-container">
                    ${{subargumentsHtml}}
                </div>
                `;
            }}
            
            // Render claimant arguments
            function renderClaimantArguments() {{
                const container = document.getElementById('claimant-arguments');
                let html = '';
                
                // Iterate through topics to find all claimant arguments
                argsData.topics.forEach(topic => {{
                    topic.argumentIds.forEach(argId => {{
                        const arg = argsData.claimantArgs[argId];
                        if (arg) {{
                            const subCount = countSubarguments(arg);
                            const subCountBadge = subCount > 0 
                                ? `<span class="subargument-badge">${{subCount}} subargument${{subCount !== 1 ? 's' : ''}}</span>` 
                                : '';
                            
                            html += `
                            <div class="argument-card">
                                <div class="argument-header" onclick="toggleArgument('claimant-${{arg.id}}')">
                                    <div class="argument-title">
                                        <svg id="chevron-claimant-${{arg.id}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <polyline points="9 18 15 12 9 6"></polyline>
                                        </svg>
                                        ${{arg.id}}. ${{arg.title}}
                                    </div>
                                    ${{subCountBadge}}
                                </div>
                                <div class="argument-content" id="content-claimant-${{arg.id}}">
                                    ${{renderKeyPoints(arg.overview)}}
                                    ${{renderFactualPoints(arg.factualPoints)}}
                                    ${{renderEvidence(arg.evidence)}}
                                    ${{renderLegalPoints(arg.caseLaw)}}
                                    
                                    ${{arg.children ? renderSubarguments(arg.children, 'claimant') : ''}}
                                </div>
                            </div>
                            `;
                        }}
                    }});
                }});
                
                container.innerHTML = html;
            }}
            
            // Render respondent arguments
            function renderRespondentArguments() {{
                const container = document.getElementById('respondent-arguments');
                let html = '';
                
                // Iterate through topics to find all respondent arguments
                argsData.topics.forEach(topic => {{
                    topic.argumentIds.forEach(argId => {{
                        const arg = argsData.respondentArgs[argId];
                        if (arg) {{
                            const subCount = countSubarguments(arg);
                            const subCountBadge = subCount > 0 
                                ? `<span class="subargument-badge respondent">${{subCount}} subargument${{subCount !== 1 ? 's' : ''}}</span>` 
                                : '';
                            
                            html += `
                            <div class="argument-card">
                                <div class="argument-header" onclick="toggleArgument('respondent-${{arg.id}}')">
                                    <div class="argument-title">
                                        <svg id="chevron-respondent-${{arg.id}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <polyline points="9 18 15 12 9 6"></polyline>
                                        </svg>
                                        ${{arg.id}}. ${{arg.title}}
                                    </div>
                                    ${{subCountBadge}}
                                </div>
                                <div class="argument-content" id="content-respondent-${{arg.id}}">
                                    ${{renderKeyPoints(arg.overview)}}
                                    ${{renderFactualPoints(arg.factualPoints)}}
                                    ${{renderEvidence(arg.evidence)}}
                                    ${{renderLegalPoints(arg.caseLaw)}}
                                    
                                    ${{arg.children ? renderSubarguments(arg.children, 'respondent') : ''}}
                                </div>
                            </div>
                            `;
                        }}
                    }});
                }});
                
                container.innerHTML = html;
            }}
            
            // Render timeline
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
                if (!tbody) return;
                
                tbody.innerHTML = '';
                
                timelineData.forEach(item => {{
                    const row = document.createElement('tr');
                    if (item.status === 'Disputed') {{
                        row.classList.add('disputed');
                    }}
                    
                    row.innerHTML = `
                        <td>${{item.date}}</td>
                        <td>${{item.appellantVersion}}</td>
                        <td>${{item.respondentVersion}}</td>
                        <td>${{item.status}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Render exhibits
            function renderExhibits() {{
                const tbody = document.getElementById('exhibits-body');
                if (!tbody) return;
                
                tbody.innerHTML = '';
                
                exhibitsData.forEach(item => {{
                    const row = document.createElement('tr');
                    const badgeClass = item.party === 'Appellant' ? '' : 'respondent';
                    
                    row.innerHTML = `
                        <td>${{item.id}}</td>
                        <td>${{item.party}}</td>
                        <td>${{item.title}}</td>
                        <td>${{item.type}}</td>
                        <td>${{item.summary}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Initialize the app
            renderClaimantArguments();
            renderRespondentArguments();
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Legal Arguments Analysis")
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
