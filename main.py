import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# All the data structures remain the same

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
            
            /* Search bar */
            .search-container {{
                margin-bottom: 20px;
                position: relative;
            }}
            
            .search-input {{
                width: 100%;
                padding: 12px 20px 12px 40px;
                border: 1px solid #e1e4e8;
                border-radius: 24px;
                font-size: 16px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            }}
            
            .search-icon {{
                position: absolute;
                left: 15px;
                top: 50%;
                transform: translateY(-50%);
                color: #8c8c8c;
            }}
            
            /* Simple tabs */
            .tabs {{
                display: flex;
                margin-bottom: 20px;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            .tab {{
                padding: 10px 20px;
                cursor: pointer;
                font-weight: 500;
                color: #585858;
            }}
            
            .tab.active {{
                color: #3182ce;
                border-bottom: 2px solid #3182ce;
            }}
            
            /* Tab content */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
            
            /* Card styling */
            .card {{
                background-color: #fff;
                border: 1px solid #f0f0f0;
                border-radius: 8px;
                margin-bottom: 16px;
                overflow: hidden;
            }}
            
            .card-header {{
                padding: 12px 16px;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #f0f0f0;
                background-color: #fafafa;
            }}
            
            .card-content {{
                padding: 16px;
                display: none;
            }}
            
            /* Arguments layout */
            .arguments-row {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
            }}
            
            .side-heading {{
                margin-bottom: 16px;
                font-weight: 500;
            }}
            
            .appellant-color {{
                color: #3182ce;
            }}
            
            .respondent-color {{
                color: #e53e3e;
            }}
            
            /* Badge styling */
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
            
            .exhibit-badge {{
                background-color: rgba(221, 107, 32, 0.1);
                color: #dd6b20;
            }}
            
            .disputed-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            .para-badge {{
                background-color: rgba(0, 0, 0, 0.05);
                color: #666;
                margin-left: 5px;
            }}
            
            /* Evidence and factual points */
            .item-block {{
                background-color: #fafafa;
                border-radius: 6px;
                padding: 12px;
                margin-bottom: 10px;
            }}
            
            .item-title {{
                font-weight: 600;
                margin-bottom: 6px;
                color: #333;
            }}
            
            .evidence-block {{
                background-color: #fff8f0;
                border-left: 3px solid #dd6b20;
                padding: 10px 12px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            .caselaw-block {{
                background-color: #ebf8ff;
                border-left: 3px solid #3182ce;
                padding: 10px 12px;
                margin-bottom: 12px;
                border-radius: 0 4px 4px 0;
            }}
            
            /* Tables */
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            
            th {{
                text-align: left;
                padding: 12px;
                background-color: #fafafa;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            td {{
                padding: 12px;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            tr.disputed {{
                background-color: rgba(229, 62, 62, 0.05);
            }}
            
            /* Copy button */
            .copy-button {{
                position: absolute;
                top: 20px;
                right: 20px;
                padding: 8px 16px;
                background-color: #f9f9f9;
                border: 1px solid #e1e4e8;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                cursor: pointer;
            }}
            
            /* Nested content */
            .nested-content {{
                padding-left: 20px;
                margin-top: 10px;
                border-left: 1px solid #f0f0f0;
            }}
            
            /* Simple list styling */
            ul.point-list {{
                list-style-type: none;
                padding-left: 0;
                margin: 0;
            }}
            
            ul.point-list li {{
                position: relative;
                padding-left: 16px;
                margin-bottom: 8px;
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
            }}
            
            ul.point-list li:before {{
                content: "•";
                position: absolute;
                left: 0;
                color: #8c8c8c;
            }}
            
            /* Chevron icon */
            .chevron {{
                transition: transform 0.2s;
            }}
            
            .chevron.expanded {{
                transform: rotate(90deg);
            }}
            
            /* Citation tags */
            .citation-tag {{
                padding: 2px 5px;
                background: rgba(0,0,0,0.05);
                border-radius: 3px;
                font-size: 11px;
                color: #666;
                margin-right: 2px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Search bar -->
            <div class="search-container">
                <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <input type="text" class="search-input" id="global-search" placeholder="Search issues, arguments, or evidence...">
            </div>
            
            <button class="copy-button" onclick="copyAllContent()">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                Copy All
            </button>
            
            <!-- Simple tabs -->
            <div class="tabs">
                <div class="tab active" data-tab="arguments">Arguments</div>
                <div class="tab" data-tab="timeline">Timeline</div>
                <div class="tab" data-tab="exhibits">Exhibits</div>
            </div>
            
            <!-- Arguments Tab -->
            <div id="arguments" class="tab-content active">
                <div id="topics-container"></div>
            </div>
            
            <!-- Timeline Tab -->
            <div id="timeline" class="tab-content">
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
            
            <!-- Exhibits Tab -->
            <div id="exhibits" class="tab-content">
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
            
            // Render overview points - updated to show paragraphs
            function renderOverviewPoints(overview) {{
                if (!overview || !overview.points || overview.points.length === 0) return '';
                
                const pointsList = overview.points.map(point => 
                    `<li>
                        <span>${{point}}</span>
                        <span class="para-badge">¶${{overview.paragraphs}}</span>
                    </li>`
                ).join('');
                
                return `
                <div class="item-block">
                    <div class="item-title">Supporting Points</div>
                    <ul class="point-list">
                        ${{pointsList}}
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
                    
                    // Exhibits badges
                    const exhibitBadges = point.exhibits && point.exhibits.length > 0
                        ? point.exhibits.map(exhibitId => `<span class="badge exhibit-badge">${{exhibitId}}</span>`).join(' ')
                        : '';
                    
                    return `
                    <div class="item-block">
                        <div style="display: flex; justify-content: space-between;">
                            <span>${{point.point}}</span>
                            <span>
                                ${{disputed}}
                                ${{exhibitBadges}}
                                <span class="para-badge">¶${{point.paragraphs}}</span>
                            </span>
                        </div>
                        <div style="font-size: 12px; color: #666; margin-top: 4px;">${{point.date}}</div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Factual Points</div>
                    ${{pointsHtml}}
                </div>
                `;
            }}
            
            // Render evidence - updated to match required format
            function renderEvidence(evidence) {{
                if (!evidence || evidence.length === 0) return '';
                
                const evidenceHtml = evidence.map(item => {{
                    const citations = item.citations && item.citations.length > 0
                        ? item.citations.map(cite => `<span class="citation-tag">¶${{cite}}</span>`).join('')
                        : '';
                    
                    return `
                    <div class="evidence-block">
                        <div class="item-title">${{item.id}}: ${{item.title}}</div>
                        <div style="margin: 6px 0;">${{item.summary}}</div>
                        <div style="margin-top: 8px; font-size: 12px;">
                            <span style="color: #666; margin-right: 5px;">Cited in:</span>
                            ${{citations}}
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Evidence</div>
                    ${{evidenceHtml}}
                </div>
                `;
            }}
            
            // Render case law - updated to match required format
            function renderCaseLaw(cases) {{
                if (!cases || cases.length === 0) return '';
                
                const casesHtml = cases.map(item => {{
                    const citedParagraphs = item.citedParagraphs && item.citedParagraphs.length > 0
                        ? item.citedParagraphs.map(cite => `<span class="citation-tag">¶${{cite}}</span>`).join('')
                        : '';
                    
                    return `
                    <div class="caselaw-block">
                        <div class="item-title">${{item.caseNumber}}</div>
                        <div style="font-size: 12px; margin: 2px 0 8px 0;">¶${{item.paragraphs}}</div>
                        <div style="font-weight: 500; margin-bottom: 4px;">${{item.title}}</div>
                        <div style="margin: 6px 0;">${{item.relevance}}</div>
                        <div style="margin-top: 8px; font-size: 12px;">
                            <span style="color: #666; margin-right: 5px;">Key Paragraphs:</span>
                            ${{citedParagraphs}}
                        </div>
                    </div>
                    `;
                }}).join('');
                
                return `
                <div style="margin-top: 16px;">
                    <div class="item-title">Case Law</div>
                    ${{casesHtml}}
                </div>
                `;
            }}
            
            // Render argument content
            function renderArgumentContent(arg) {{
                let content = '';
                
                // Overview points
                if (arg.overview) {{
                    content += renderOverviewPoints(arg.overview);
                }}
                
                // Factual points
                if (arg.factualPoints) {{
                    content += renderFactualPoints(arg.factualPoints);
                }}
                
                // Evidence
                if (arg.evidence) {{
                    content += renderEvidence(arg.evidence);
                }}
                
                // Case law
                if (arg.caseLaw) {{
                    content += renderCaseLaw(arg.caseLaw);
                }}
                
                return content;
            }}
            
            // Render a single argument including its children
            function renderArgument(arg, side) {{
                if (!arg) return '';
                
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const argId = `${{side}}-${{arg.id}}`;
                
                // Style based on side
                const badgeClass = side === 'appellant' ? 'appellant-badge' : 'respondent-badge';
                
                // Render children if any
                let childrenHtml = '';
                if (hasChildren) {{
                    childrenHtml = `<div class="nested-content" id="children-${{argId}}" style="display: none;">`;
                    
                    Object.values(arg.children).forEach(child => {{
                        childrenHtml += renderArgument(child, side);
                    }});
                    
                    childrenHtml += `</div>`;
                }}
                
                return `
                <div class="card">
                    <div class="card-header" onclick="toggleCard('${{argId}}')">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <svg id="chevron-${{argId}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6"></polyline>
                            </svg>
                            <span>${{arg.id}}. ${{arg.title}}</span>
                        </div>
                        <span class="badge ${{badgeClass}}">¶${{arg.paragraphs}}</span>
                    </div>
                    <div class="card-content" id="content-${{argId}}">
                        ${{renderArgumentContent(arg)}}
                    </div>
                    ${{childrenHtml}}
                </div>
                `;
            }}
            
            // Render arguments by topic
            function renderTopics() {{
                const container = document.getElementById('topics-container');
                let html = '';
                
                argsData.topics.forEach(topic => {{
                    html += `
                    <div class="card" style="margin-bottom: 24px;">
                        <div class="card-header" onclick="toggleCard('topic-${{topic.id}}')">
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <svg id="chevron-topic-${{topic.id}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <span>${{topic.title}}</span>
                            </div>
                        </div>
                        <div class="card-content" id="content-topic-${{topic.id}}">
                            <p>${{topic.description}}</p>
                            
                            ${{topic.argumentIds.map(argId => {{
                                if (argsData.claimantArgs[argId] && argsData.respondentArgs[argId]) {{
                                    return `
                                    <div style="margin-top: 16px;">
                                        <div class="arguments-row">
                                            <div>
                                                <h3 class="side-heading appellant-color">Appellant's Position</h3>
                                                ${{renderArgument(argsData.claimantArgs[argId], 'appellant')}}
                                            </div>
                                            <div>
                                                <h3 class="side-heading respondent-color">Respondent's Position</h3>
                                                ${{renderArgument(argsData.respondentArgs[argId], 'respondent')}}
                                            </div>
                                        </div>
                                    </div>
                                    `;
                                }}
                                return '';
                            }}).join('')}}
                        </div>
                    </div>
                    `;
                }});
                
                container.innerHTML = html;
            }}
            
            // Toggle card expansion
            function toggleCard(id) {{
                const contentEl = document.getElementById(`content-${{id}}`);
                const childrenEl = document.getElementById(`children-${{id}}`);
                const chevronEl = document.getElementById(`chevron-${{id}}`);
                
                if (contentEl) {{
                    contentEl.style.display = contentEl.style.display === 'block' ? 'none' : 'block';
                }}
                
                if (childrenEl) {{
                    childrenEl.style.display = childrenEl.style.display === 'block' ? 'none' : 'block';
                }}
                
                if (chevronEl) {{
                    chevronEl.classList.toggle('expanded');
                }}
            }}
            
            // Render timeline
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
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
                tbody.innerHTML = '';
                
                exhibitsData.forEach(item => {{
                    const row = document.createElement('tr');
                    const badgeClass = item.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge';
                    
                    row.innerHTML = `
                        <td>${{item.id}}</td>
                        <td><span class="badge ${{badgeClass}}">${{item.party}}</span></td>
                        <td>${{item.title}}</td>
                        <td>${{item.type}}</td>
                        <td>${{item.summary}}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Global search function
            document.getElementById('global-search').addEventListener('input', function() {{
                const searchTerm = this.value.toLowerCase();
                
                // If on arguments tab, filter visible arguments
                if (document.getElementById('arguments').style.display !== 'none') {{
                    // Implementation would go here
                }}
                
                // If on timeline tab, filter timeline
                if (document.getElementById('timeline').style.display !== 'none') {{
                    filterTimeline(searchTerm);
                }}
                
                // If on exhibits tab, filter exhibits
                if (document.getElementById('exhibits').style.display !== 'none') {{
                    filterExhibits(searchTerm);
                }}
            }});
            
            // Filter timeline based on search
            function filterTimeline(searchTerm) {{
                const rows = document.querySelectorAll('#timeline-body tr');
                
                rows.forEach(row => {{
                    const text = row.textContent.toLowerCase();
                    row.style.display = text.includes(searchTerm) ? '' : 'none';
                }});
            }}
            
            // Filter exhibits based on search
            function filterExhibits(searchTerm) {{
                const rows = document.querySelectorAll('#exhibits-body tr');
                
                rows.forEach(row => {{
                    const text = row.textContent.toLowerCase();
                    row.style.display = text.includes(searchTerm) ? '' : 'none';
                }});
            }}
            
            // Copy all content function
            function copyAllContent() {{
                // Simple implementation - would need to be extended 
                // to actually collect and copy all content
                alert('All content copied to clipboard');
            }}
            
            // Initialize the page
            renderTopics();
            
            // Auto-expand first topic
            setTimeout(() => {{
                const firstTopic = argsData.topics[0];
                if (firstTopic) {{
                    toggleCard(`topic-${{firstTopic.id}}`);
                }}
            }}, 100);
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Legal Arguments Analysis")
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
