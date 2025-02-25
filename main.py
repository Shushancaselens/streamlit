import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Create data structures as JSON for embedded components
def get_argument_data():
    # [Keep all the existing data structure code the same]
    # ...

def get_timeline_data():
    # [Keep existing timeline data the same]
    # ...

def get_exhibits_data():
    # [Keep existing exhibits data the same]
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
    
    # Create a single HTML component containing the full UI with cleaner design
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
                background-color: #f5f7f9;
            }}
            
            /* Container */
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}
            
            /* Page title */
            .page-title {{
                font-size: 24px;
                font-weight: 600;
                margin-bottom: 20px;
            }}
            
            /* Navigation tabs */
            .nav-tabs {{
                display: flex;
                border-bottom: 1px solid #e0e0e0;
                margin-bottom: 25px;
            }}
            
            .nav-tab {{
                padding: 12px 20px;
                cursor: pointer;
                color: #5c6370;
                font-weight: 500;
                position: relative;
            }}
            
            .nav-tab.active {{
                color: #4285f4;
                font-weight: 600;
            }}
            
            .nav-tab.active::after {{
                content: "";
                position: absolute;
                bottom: -1px;
                left: 0;
                width: 100%;
                height: 2px;
                background-color: #4285f4;
            }}
            
            /* Arguments sections */
            .arguments-container {{
                display: flex;
                gap: 30px;
            }}
            
            .arguments-section {{
                flex: 1;
            }}
            
            .arguments-title {{
                font-size: 18px;
                font-weight: 600;
                margin-bottom: 16px;
            }}
            
            .claimant-title {{
                color: #4285f4;
            }}
            
            .respondent-title {{
                color: #ea4335;
            }}
            
            /* Argument cards */
            .argument-card {{
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                margin-bottom: 12px;
                overflow: hidden;
                background-color: #fff;
            }}
            
            .argument-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 14px 16px;
                cursor: pointer;
                border-bottom: 1px solid #e0e0e0;
            }}
            
            .argument-title {{
                display: flex;
                align-items: center;
                gap: 10px;
                font-weight: 500;
            }}
            
            .argument-chevron {{
                transition: transform 0.2s ease;
            }}
            
            .argument-chevron.expanded {{
                transform: rotate(90deg);
            }}
            
            .subarguments-badge {{
                background-color: rgba(0, 0, 0, 0.05);
                color: #555;
                font-size: 12px;
                padding: 3px 8px;
                border-radius: 12px;
            }}
            
            .claimant-badge {{
                background-color: rgba(66, 133, 244, 0.1);
            }}
            
            .respondent-badge {{
                background-color: rgba(234, 67, 53, 0.1);
            }}
            
            .argument-content {{
                padding: 16px;
                display: none;
            }}
            
            /* Tab content */
            .tab-content {{
                display: none;
            }}
            
            .tab-content.active {{
                display: block;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="page-title">Legal Arguments Analysis</h1>
            
            <!-- Navigation Tabs -->
            <div class="nav-tabs">
                <div class="nav-tab active" data-tab="arguments">Summary of Arguments</div>
                <div class="nav-tab" data-tab="timeline">Timeline</div>
                <div class="nav-tab" data-tab="exhibits">Exhibits</div>
            </div>
            
            <!-- Arguments Tab -->
            <div id="arguments" class="tab-content active">
                <div class="arguments-container">
                    <!-- Claimant's Arguments -->
                    <div class="arguments-section">
                        <h2 class="arguments-title claimant-title">Claimant's Arguments</h2>
                        <div id="claimant-arguments"></div>
                    </div>
                    
                    <!-- Respondent's Arguments -->
                    <div class="arguments-section">
                        <h2 class="arguments-title respondent-title">Respondent's Arguments</h2>
                        <div id="respondent-arguments"></div>
                    </div>
                </div>
            </div>
            
            <!-- Timeline Tab -->
            <div id="timeline" class="tab-content">
                <table id="timeline-table" class="data-table">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Claimant's Version</th>
                            <th>Respondent's Version</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody id="timeline-body"></tbody>
                </table>
            </div>
            
            <!-- Exhibits Tab -->
            <div id="exhibits" class="tab-content">
                <table id="exhibits-table" class="data-table">
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
            document.querySelectorAll('.nav-tab').forEach(tab => {{
                tab.addEventListener('click', function() {{
                    // Update tabs
                    document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Update content
                    const tabId = this.getAttribute('data-tab');
                    document.querySelectorAll('.tab-content').forEach(content => {{
                        content.style.display = 'none';
                        content.classList.remove('active');
                    }});
                    document.getElementById(tabId).style.display = 'block';
                    document.getElementById(tabId).classList.add('active');
                    
                    // Initialize content if needed
                    if (tabId === 'timeline') renderTimeline();
                    if (tabId === 'exhibits') renderExhibits();
                }});
            }});
            
            // Count subarguments
            function countSubarguments(arg) {{
                let count = 0;
                if (arg.children) {{
                    count = Object.keys(arg.children).length;
                }}
                return count;
            }}
            
            // Render main arguments
            function renderMainArguments() {{
                const claimantContainer = document.getElementById('claimant-arguments');
                const respondentContainer = document.getElementById('respondent-arguments');
                
                // Clear containers
                claimantContainer.innerHTML = '';
                respondentContainer.innerHTML = '';
                
                // Render claimant arguments
                Object.values(argsData.claimantArgs).forEach(arg => {{
                    const subCount = countSubarguments(arg);
                    const subBadge = subCount > 0 ? `<span class="subarguments-badge claimant-badge">${subCount} subarguments</span>` : '';
                    
                    const html = `
                    <div class="argument-card">
                        <div class="argument-header" onclick="toggleArgument('claimant-${arg.id}')">
                            <div class="argument-title">
                                <svg class="argument-chevron" id="chevron-claimant-${arg.id}" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                ${arg.id}. ${arg.title}
                            </div>
                            ${subBadge}
                        </div>
                        <div class="argument-content" id="content-claimant-${arg.id}">
                            <!-- Argument content will go here -->
                        </div>
                    </div>
                    `;
                    
                    claimantContainer.innerHTML += html;
                }});
                
                // Render respondent arguments
                Object.values(argsData.respondentArgs).forEach(arg => {{
                    const subCount = countSubarguments(arg);
                    const subBadge = subCount > 0 ? `<span class="subarguments-badge respondent-badge">${subCount} subarguments</span>` : '';
                    
                    const html = `
                    <div class="argument-card">
                        <div class="argument-header" onclick="toggleArgument('respondent-${arg.id}')">
                            <div class="argument-title">
                                <svg class="argument-chevron" id="chevron-respondent-${arg.id}" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                ${arg.id}. ${arg.title}
                            </div>
                            ${subBadge}
                        </div>
                        <div class="argument-content" id="content-respondent-${arg.id}">
                            <!-- Argument content will go here -->
                        </div>
                    </div>
                    `;
                    
                    respondentContainer.innerHTML += html;
                }});
            }}
            
            // Toggle argument content
            function toggleArgument(id) {{
                const contentEl = document.getElementById(`content-${id}`);
                const chevronEl = document.getElementById(`chevron-${id}`);
                
                if (contentEl) {{
                    contentEl.style.display = contentEl.style.display === 'block' ? 'none' : 'block';
                }}
                
                if (chevronEl) {{
                    chevronEl.classList.toggle('expanded');
                }}
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
                        <td>${item.date}</td>
                        <td>${item.appellantVersion}</td>
                        <td>${item.respondentVersion}</td>
                        <td>${item.status}</td>
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
                    
                    row.innerHTML = `
                        <td>${item.id}</td>
                        <td>${item.party}</td>
                        <td>${item.title}</td>
                        <td>${item.type}</td>
                        <td>${item.summary}</td>
                    `;
                    
                    tbody.appendChild(row);
                }});
            }}
            
            // Initialize the arguments display
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
