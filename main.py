import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# [Keep all the data functions the same]

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
            
            /* Container */
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            /* Main title */
            .main-title {{
                font-size: 24px;
                font-weight: 600;
                margin-bottom: 20px;
            }}
            
            /* Tabs */
            .tabs {{
                display: flex;
                margin-bottom: 30px;
                border-bottom: 1px solid #eaeaea;
            }}
            
            .tab {{
                padding: 15px 20px;
                cursor: pointer;
                font-weight: 500;
                color: #666;
                position: relative;
            }}
            
            .tab.active {{
                color: #3182ce;
            }}
            
            .tab.active::after {{
                content: '';
                position: absolute;
                bottom: -1px;
                left: 0;
                right: 0;
                height: 3px;
                background-color: #3182ce;
            }}
            
            /* Columns for arguments */
            .arguments-container {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 30px;
                margin-top: 20px;
            }}
            
            .column-title {{
                font-size: 20px;
                font-weight: 500;
                margin-bottom: 20px;
            }}
            
            .claimant-title {{
                color: #3182ce;
            }}
            
            .respondent-title {{
                color: #e53e3e;
            }}
            
            /* Argument card */
            .argument-card {{
                display: flex;
                align-items: center;
                padding: 15px;
                border: 1px solid #eaeaea;
                border-radius: 8px;
                margin-bottom: 15px;
                cursor: pointer;
                transition: all 0.2s;
            }}
            
            .argument-card:hover {{
                background-color: #f9f9f9;
            }}
            
            .argument-card .caret {{
                margin-right: 10px;
                transition: transform 0.2s;
            }}
            
            .argument-card .caret.expanded {{
                transform: rotate(90deg);
            }}
            
            .argument-card .title {{
                flex: 1;
                font-weight: 500;
            }}
            
            /* Badges */
            .badge {{
                display: inline-block;
                padding: 4px 8px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 500;
            }}
            
            .claimant-badge {{
                background-color: rgba(49, 130, 206, 0.1);
                color: #3182ce;
            }}
            
            .respondent-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            /* Tab content container */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* Content inside an expanded argument */
            .argument-content {{
                margin-top: 15px;
                display: none;
            }}
            
            /* Subarguments */
            .subargument-list {{
                border-left: 2px solid #eaeaea;
                margin-left: 10px;
                padding-left: 15px;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Main title -->
            <h1 class="main-title">Legal Arguments Analysis</h1>
            
            <!-- Tabs -->
            <div class="tabs">
                <div class="tab active" data-tab="summary">Summary of Arguments</div>
                <div class="tab" data-tab="timeline">Timeline</div>
                <div class="tab" data-tab="exhibits">Exhibits</div>
            </div>
            
            <!-- Summary Tab -->
            <div id="summary-tab" class="tab-content active">
                <div class="arguments-container">
                    <!-- Claimant's Arguments -->
                    <div class="claimant-column">
                        <h2 class="column-title claimant-title">Claimant's Arguments</h2>
                        <div id="claimant-arguments"></div>
                    </div>
                    
                    <!-- Respondent's Arguments -->
                    <div class="respondent-column">
                        <h2 class="column-title respondent-title">Respondent's Arguments</h2>
                        <div id="respondent-arguments"></div>
                    </div>
                </div>
            </div>
            
            <!-- Timeline Tab -->
            <div id="timeline-tab" class="tab-content">
                <table id="timeline-table" style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Date</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Appellant's Version</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Respondent's Version</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Status</th>
                        </tr>
                    </thead>
                    <tbody id="timeline-body"></tbody>
                </table>
            </div>
            
            <!-- Exhibits Tab -->
            <div id="exhibits-tab" class="tab-content">
                <table id="exhibits-table" style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">ID</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Party</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Title</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Type</th>
                            <th style="text-align: left; padding: 10px; border-bottom: 1px solid #eaeaea;">Summary</th>
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
                    // Update active tab
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Show selected tab content
                    const tabId = this.getAttribute('data-tab') + '-tab';
                    document.querySelectorAll('.tab-content').forEach(content => {{
                        content.classList.remove('active');
                    }});
                    document.getElementById(tabId).classList.add('active');
                    
                    // Initialize content if needed
                    if (tabId === 'timeline-tab') renderTimeline();
                    if (tabId === 'exhibits-tab') renderExhibits();
                }});
            }});
            
            // Count subarguments in an argument
            function countSubarguments(arg) {{
                if (!arg || !arg.children) return 0;
                return Object.keys(arg.children).length;
            }}
            
            // Render main arguments list
            function renderMainArguments() {{
                const claimantContainer = document.getElementById('claimant-arguments');
                const respondentContainer = document.getElementById('respondent-arguments');
                
                // Clear containers
                claimantContainer.innerHTML = '';
                respondentContainer.innerHTML = '';
                
                // Render claimant arguments
                for (const [argId, arg] of Object.entries(argsData.claimantArgs)) {{
                    const subargCount = countSubarguments(arg);
                    const subargBadge = subargCount > 0 ? 
                        `<div class="badge claimant-badge">${{subargCount}} subarguments</div>` : '';
                    
                    const cardHtml = `
                        <div class="argument-card" id="claimant-arg-${{argId}}" onclick="toggleArgument('claimant', '${{argId}}')">
                            <div class="caret" id="claimant-caret-${{argId}}">▶</div>
                            <div class="title">${{arg.id}}. ${{arg.title}}</div>
                            ${{subargBadge}}
                        </div>
                        <div class="argument-content" id="claimant-content-${{argId}}">
                            <div class="subargument-list" id="claimant-subargs-${{argId}}"></div>
                        </div>
                    `;
                    claimantContainer.innerHTML += cardHtml;
                }}
                
                // Render respondent arguments
                for (const [argId, arg] of Object.entries(argsData.respondentArgs)) {{
                    const subargCount = countSubarguments(arg);
                    const subargBadge = subargCount > 0 ? 
                        `<div class="badge respondent-badge">${{subargCount}} subarguments</div>` : '';
                    
                    const cardHtml = `
                        <div class="argument-card" id="respondent-arg-${{argId}}" onclick="toggleArgument('respondent', '${{argId}}')">
                            <div class="caret" id="respondent-caret-${{argId}}">▶</div>
                            <div class="title">${{arg.id}}. ${{arg.title}}</div>
                            ${{subargBadge}}
                        </div>
                        <div class="argument-content" id="respondent-content-${{argId}}">
                            <div class="subargument-list" id="respondent-subargs-${{argId}}"></div>
                        </div>
                    `;
                    respondentContainer.innerHTML += cardHtml;
                }}
            }}
            
            // Toggle an argument's visibility
            function toggleArgument(side, argId) {{
                const contentEl = document.getElementById(`${{side}}-content-${{argId}}`);
                const caretEl = document.getElementById(`${{side}}-caret-${{argId}}`);
                
                if (contentEl.style.display === 'block') {{
                    contentEl.style.display = 'none';
                    caretEl.textContent = '▶';
                }} else {{
                    contentEl.style.display = 'block';
                    caretEl.textContent = '▼';
                    
                    // Render subarguments if there are any
                    const arg = side === 'claimant' ? argsData.claimantArgs[argId] : argsData.respondentArgs[argId];
                    if (arg.children && Object.keys(arg.children).length > 0) {{
                        renderSubarguments(side, argId, arg.children);
                    }}
                }}
                
                // Synchronize if it's a main argument
                if (argId === '1' || argId === '2') {{
                    const otherSide = side === 'claimant' ? 'respondent' : 'claimant';
                    const otherContentEl = document.getElementById(`${{otherSide}}-content-${{argId}}`);
                    const otherCaretEl = document.getElementById(`${{otherSide}}-caret-${{argId}}`);
                    
                    if (otherContentEl) {{
                        otherContentEl.style.display = contentEl.style.display;
                        otherCaretEl.textContent = caretEl.textContent;
                        
                        // Render other side's subarguments if there are any
                        const otherArg = otherSide === 'claimant' ? argsData.claimantArgs[argId] : argsData.respondentArgs[argId];
                        if (otherArg && otherArg.children && Object.keys(otherArg.children).length > 0 && contentEl.style.display === 'block') {{
                            renderSubarguments(otherSide, argId, otherArg.children);
                        }}
                    }}
                }}
            }}
            
            // Render subarguments
            function renderSubarguments(side, parentId, children) {{
                const container = document.getElementById(`${{side}}-subargs-${{parentId}}`);
                
                // Clear container if already has content
                if (container.innerHTML !== '') return;
                
                // Create HTML for each child
                for (const [childId, child] of Object.entries(children)) {{
                    const subargCount = countSubarguments(child);
                    const badgeClass = side === 'claimant' ? 'claimant-badge' : 'respondent-badge';
                    const subargBadge = subargCount > 0 ? 
                        `<div class="badge ${{badgeClass}}">${{subargCount}} subarguments</div>` : '';
                    
                    const cardHtml = `
                        <div class="argument-card" style="margin-top: 10px;" id="${{side}}-arg-${{parentId}}-${{childId}}" onclick="event.stopPropagation(); toggleSubargument('${{side}}', '${{parentId}}', '${{childId}}')">
                            <div class="caret" id="${{side}}-caret-${{parentId}}-${{childId}}">▶</div>
                            <div class="title">${{child.id}}. ${{child.title}}</div>
                            ${{subargBadge}}
                        </div>
                        <div class="argument-content" id="${{side}}-content-${{parentId}}-${{childId}}">
                            <div class="subargument-list" id="${{side}}-subargs-${{parentId}}-${{childId}}"></div>
                        </div>
                    `;
                    container.innerHTML += cardHtml;
                }}
            }}
            
            // Toggle a subargument's visibility
            function toggleSubargument(side, parentId, childId) {{
                const contentEl = document.getElementById(`${{side}}-content-${{parentId}}-${{childId}}`);
                const caretEl = document.getElementById(`${{side}}-caret-${{parentId}}-${{childId}}`);
                
                if (contentEl.style.display === 'block') {{
                    contentEl.style.display = 'none';
                    caretEl.textContent = '▶';
                }} else {{
                    contentEl.style.display = 'block';
                    caretEl.textContent = '▼';
                    
                    // Get the child argument
                    const parent = side === 'claimant' ? argsData.claimantArgs[parentId] : argsData.respondentArgs[parentId];
                    const child = parent.children[childId];
                    
                    // Render subarguments if there are any
                    if (child.children && Object.keys(child.children).length > 0) {{
                        renderNestedSubarguments(side, parentId, childId, child.children);
                    }}
                }}
            }}
            
            // Render nested subarguments
            function renderNestedSubarguments(side, parentId, childId, children) {{
                const container = document.getElementById(`${{side}}-subargs-${{parentId}}-${{childId}}`);
                
                // Clear container if already has content
                if (container.innerHTML !== '') return;
                
                // Create HTML for each nested child
                for (const [nestedId, nestedChild] of Object.entries(children)) {{
                    const fullId = `${{parentId}}-${{childId}}-${{nestedId}}`;
                    const cardHtml = `
                        <div class="argument-card" style="margin-top: 10px;" id="${{side}}-arg-${{fullId}}" onclick="event.stopPropagation();">
                            <div class="title">${{nestedChild.id}}. ${{nestedChild.title}}</div>
                        </div>
                    `;
                    container.innerHTML += cardHtml;
                }}
            }}
            
            // Render timeline
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
                
                // Skip if already rendered
                if (tbody.innerHTML !== '') return;
                
                tbody.innerHTML = '';
                
                timelineData.forEach(item => {{
                    const row = document.createElement('tr');
                    if (item.status === 'Disputed') {{
                        row.style.backgroundColor = 'rgba(229, 62, 62, 0.05)';
                    }}
                    
                    row.innerHTML = `
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.date}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.appellantVersion}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.respondentVersion}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.status}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Render exhibits
            function renderExhibits() {{
                const tbody = document.getElementById('exhibits-body');
                
                // Skip if already rendered
                if (tbody.innerHTML !== '') return;
                
                tbody.innerHTML = '';
                
                exhibitsData.forEach(item => {{
                    const row = document.createElement('tr');
                    
                    row.innerHTML = `
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.id}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">
                            <span class="badge ${{item.party === 'Appellant' ? 'claimant-badge' : 'respondent-badge'}}">${{item.party}}</span>
                        </td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.title}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.type}}</td>
                        <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">${{item.summary}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Initialize the page
            renderMainArguments();
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Legal Arguments Analysis")
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
