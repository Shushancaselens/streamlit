import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Arguments"

# Create data structures as JSON for embedded components
def get_argument_data():
    """
    Returns data **only** for the Doping Violation / Chain of Custody arguments 
    (Sporting Succession / Club Identity removed).
    """
    claimant_args = {
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
    
    # We keep only Topic #2 (Doping), removing the identity topic
    topics = [
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
    """
    Timeline data remains intact, but it has no references to the removed club identity arguments.
    """
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
    """
    Exhibits remain the same, as they do not directly reference the club identity arguments.
    """
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

# Get all facts from the data
def get_all_facts():
    """
    Extracts only factual points from the doping argument (#2).
    Since we removed the club identity arguments, the logic is simplified.
    """
    args_data = get_argument_data()
    facts = []
    
    def extract_facts(arg, party):
        if not arg:
            return
        # Check if 'factualPoints' exist; in doping argument as given, none are listed,
        # but we’ll leave this logic in case you add any in the future.
        if 'factualPoints' in arg and arg['factualPoints']:
            for point in arg['factualPoints']:
                fact = {
                    'point': point['point'],
                    'date': point['date'],
                    'isDisputed': point['isDisputed'],
                    'party': party,
                    'paragraphs': point.get('paragraphs', ''),
                    'exhibits': point.get('exhibits', []),
                    'argId': arg['id'],
                    'argTitle': arg['title']
                }
                facts.append(fact)
                
        # Process children (if any). Currently doping argument has no children, but code is left for structure.
        if 'children' in arg and arg['children']:
            for child_id, child in arg['children'].items():
                extract_facts(child, party)
    
    # Extract from claimant's doping argument
    for arg_id, arg in args_data['claimantArgs'].items():
        extract_facts(arg, 'Appellant')
        
    # Extract from respondent's doping argument
    for arg_id, arg in args_data['respondentArgs'].items():
        extract_facts(arg, 'Respondent')
        
    return facts

# Function to create CSV download link (used by older code snippet)
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

def main():
    # Get the data
    args_data = get_argument_data()
    
    # Ensure all arguments have overviews (in case you need them for rendering)
    def add_overviews_to_args(args_dict, party_name):
        for arg_id, arg in args_dict.items():
            # Add overview if missing
            if 'overview' not in arg:
                arg['overview'] = {
                    "points": [
                        f"Main point of {party_name}'s argument",
                        f"Supporting analysis for {arg['title']}",
                        "Contextual information"
                    ],
                    "paragraphs": arg.get('paragraphs', 'N/A')
                }
            # Process children (if any)
            if 'children' in arg and arg['children']:
                add_overviews_to_args(arg['children'], party_name)
    
    # Add overviews
    add_overviews_to_args(args_data['claimantArgs'], "Appellant")
    add_overviews_to_args(args_data['respondentArgs'], "Respondent")
    
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    facts_data = get_all_facts()
    
    # Convert data to JSON for the JavaScript portion
    args_json = json.dumps(args_data)
    timeline_json = json.dumps(timeline_data)
    exhibits_json = json.dumps(exhibits_data)
    facts_json = json.dumps(facts_data)
    
    # Initialize session state if not already done
    if 'view' not in st.session_state:
        st.session_state.view = "Arguments"
    
    # Add Streamlit sidebar
    with st.sidebar:
        st.title("Legal Analysis")
        
        # Custom CSS for button styling
        st.markdown("""
        <style>
        .stButton > button {
            width: 100%;
            border-radius: 6px;
            height: 50px;
            margin-bottom: 10px;
            transition: all 0.3s;
        }
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)
        
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_timeline_view():
            st.session_state.view = "Timeline"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📅 Timeline", key="timeline_button", on_click=set_timeline_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
    
    # Determine which view to show
    if st.session_state.view == "Arguments":
        active_tab = 0
    elif st.session_state.view == "Facts":
        active_tab = 1
    elif st.session_state.view == "Timeline":
        active_tab = 2
    else:  # Exhibits
        active_tab = 3
    
    view_options_json = json.dumps({"activeTab": active_tab})
    
    # Build the HTML/JS content
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
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            .content-section {{
                display: none;
            }}
            .content-section.active {{
                display: block;
            }}
            /* (Omitted detailed CSS for brevity; same structure as before) */
        </style>
    </head>
    <body>
        <div class="container">
            <div id="copy-notification" class="copy-notification">Content copied to clipboard!</div>
            
            <div class="action-buttons">
                <!-- Copy and Export Buttons (same structure) -->
                <button class="action-button" onclick="copyAllContent()">Copy</button>
                <div class="export-dropdown">
                    <button class="action-button">Export</button>
                    <div class="export-dropdown-content">
                        <a onclick="exportAsCsv()">CSV</a>
                        <a onclick="exportAsPdf()">PDF</a>
                        <a onclick="exportAsWord()">Word</a>
                    </div>
                </div>
            </div>
            
            <!-- Arguments Section -->
            <div id="arguments" class="content-section">
                <h2>Doping Issue</h2>
                <div class="view-toggle">
                    <button id="detailed-view-btn" class="active" onclick="switchView('detailed')">Detailed View</button>
                    <button id="table-view-btn" onclick="switchView('table')">Table View</button>
                </div>
                
                <div id="detailed-view" class="view-content active">
                    <div id="topics-container"></div>
                </div>
                <div id="table-view" class="view-content" style="display: none;">
                    <table class="table-view">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Argument</th>
                                <th>Party</th>
                                <th>Status</th>
                                <th>Evidence</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody id="table-view-body"></tbody>
                    </table>
                </div>
            </div>
            
            <!-- Facts Section -->
            <div id="facts" class="content-section">
                <h2>Case Facts</h2>
                <div class="facts-header">
                    <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                    <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                    <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                </div>
                <div class="facts-content">
                    <table class="table-view">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Event</th>
                                <th>Party</th>
                                <th>Status</th>
                                <th>Related Argument</th>
                                <th>Evidence</th>
                            </tr>
                        </thead>
                        <tbody id="facts-table-body"></tbody>
                    </table>
                </div>
            </div>
            
            <!-- Timeline Section -->
            <div id="timeline" class="content-section">
                <h2>Case Timeline</h2>
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
            
            <!-- Exhibits Section -->
            <div id="exhibits" class="content-section">
                <h2>Case Exhibits</h2>
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
            const argsData = {args_json};
            const timelineData = {timeline_json};
            const exhibitsData = {exhibits_json};
            const factsData = {facts_json};
            const viewOptions = {view_options_json};

            document.addEventListener('DOMContentLoaded', function() {{
                const sections = ['arguments', 'facts', 'timeline', 'exhibits'];
                const activeSection = sections[viewOptions.activeTab];
                
                document.querySelectorAll('.content-section').forEach(section => {{
                    section.classList.remove('active');
                }});
                document.getElementById(activeSection).classList.add('active');
                
                if (activeSection === 'arguments') {{
                    renderTopics();
                    renderArgumentsTable();
                }}
                if (activeSection === 'timeline') renderTimeline();
                if (activeSection === 'exhibits') renderExhibits();
                if (activeSection === 'facts') renderFacts();
            }});
            
            // ... (JavaScript for toggling views, copying, exports, and rendering content)
            // The only difference is that the doping argument is the sole argument now.
            
            function switchView(viewType) {{
                const detailedBtn = document.getElementById('detailed-view-btn');
                const tableBtn = document.getElementById('table-view-btn');
                const detailedView = document.getElementById('detailed-view');
                const tableView = document.getElementById('table-view');
                
                if (viewType === 'detailed') {{
                    detailedBtn.classList.add('active');
                    tableBtn.classList.remove('active');
                    detailedView.style.display = 'block';
                    tableView.style.display = 'none';
                }} else {{
                    detailedBtn.classList.remove('active');
                    tableBtn.classList.add('active');
                    detailedView.style.display = 'none';
                    tableView.style.display = 'block';
                }}
            }}
            
            function switchFactsTab(tabType) {{
                const allBtn = document.getElementById('all-facts-btn');
                const disputedBtn = document.getElementById('disputed-facts-btn');
                const undisputedBtn = document.getElementById('undisputed-facts-btn');
                
                allBtn.classList.remove('active');
                disputedBtn.classList.remove('active');
                undisputedBtn.classList.remove('active');
                
                if (tabType === 'all') {{
                    allBtn.classList.add('active');
                    renderFacts('all');
                }} else if (tabType === 'disputed') {{
                    disputedBtn.classList.add('active');
                    renderFacts('disputed');
                }} else {{
                    undisputedBtn.classList.add('active');
                    renderFacts('undisputed');
                }}
            }}
            
            // Example for sorting (omitted for brevity)
            function sortTable(tableId, columnIndex) {{ /* ... */ }}
            
            // Copy / Export stubs
            function copyAllContent() {{ /* ... */ }}
            function exportAsCsv() {{ /* ... */ }}
            function exportAsPdf() {{ /* ... */ }}
            function exportAsWord() {{ /* ... */ }}
            
            // Renders
            function renderTopics() {{
                const container = document.getElementById('topics-container');
                let html = '';
                
                // We now have only one topic: doping
                argsData.topics.forEach(topic => {{
                    html += `
                    <div>
                        <h3>${{topic.title}}</h3>
                        <p>${{topic.description}}</p>
                        ${{topic.argumentIds.map(argId => {{
                            const claimantArg = argsData.claimantArgs[argId];
                            const respondentArg = argsData.respondentArgs[argId];
                            if (claimantArg && respondentArg) {{
                                return `
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
                                    <div>
                                        <h4>Appellant's Position</h4>
                                        ${renderArgument(claimantArg, 'Appellant')}
                                    </div>
                                    <div>
                                        <h4>Respondent's Position</h4>
                                        ${renderArgument(respondentArg, 'Respondent')}
                                    </div>
                                </div>
                                `;
                            }}
                            return '';
                        }}).join('')}}
                    </div>
                    `;
                }});
                
                container.innerHTML = html;
            }}
            
            function renderArgument(arg, side) {{
                // Example simple render (you can expand as needed)
                return `
                    <div style="border: 1px solid #ccc; padding: 10px; border-radius: 6px;">
                        <div><strong>Argument ID:</strong> ${arg.id}</div>
                        <div><strong>Title:</strong> ${arg.title}</div>
                        <div><strong>Paragraphs:</strong> ${arg.paragraphs}</div>
                        <div style="margin-top: 10px;">
                            <strong>Overview:</strong>
                            <ul>
                                ${(arg.overview.points || []).map(p => `<li>${p}</li>`).join('')}
                            </ul>
                        </div>
                    </div>
                `;
            }}
            
            function renderArgumentsTable() {{
                const tableBody = document.getElementById('table-view-body');
                tableBody.innerHTML = '';
                
                function flattenArguments(args, party) {{
                    let result = [];
                    Object.values(args).forEach(arg => {{
                        // For demonstration, we assume doping argument has no disputed facts
                        const hasDisputedFacts = false; 
                        const evidenceCount = arg.evidence ? arg.evidence.length : 0;
                        
                        result.push({{
                            id: arg.id,
                            title: arg.title,
                            party,
                            hasDisputedFacts,
                            evidenceCount
                        }});
                    }});
                    return result;
                }}
                
                const appellantArgs = flattenArguments(argsData.claimantArgs, 'Appellant');
                const respondentArgs = flattenArguments(argsData.respondentArgs, 'Respondent');
                const allArgs = [...appellantArgs, ...respondentArgs];
                
                allArgs.forEach(arg => {{
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${arg.id}</td>
                        <td>${arg.title}</td>
                        <td>${arg.party}</td>
                        <td>${arg.hasDisputedFacts ? 'Disputed' : 'Undisputed'}</td>
                        <td>${arg.evidenceCount > 0 ? arg.evidenceCount + ' items' : 'None'}</td>
                        <td><button>View</button></td>
                    `;
                    tableBody.appendChild(row);
                }});
            }}
            
            function renderFacts(type = 'all') {{
                const tableBody = document.getElementById('facts-table-body');
                tableBody.innerHTML = '';
                
                // Filter
                let filteredFacts = factsData;
                if (type === 'disputed') {{
                    filteredFacts = factsData.filter(f => f.isDisputed);
                }} else if (type === 'undisputed') {{
                    filteredFacts = factsData.filter(f => !f.isDisputed);
                }}
                
                filteredFacts.forEach(fact => {{
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${fact.date}</td>
                        <td>${fact.point || ''}</td>
                        <td>${fact.party}</td>
                        <td>${fact.isDisputed ? 'Disputed' : 'Undisputed'}</td>
                        <td>${fact.argId ? fact.argId + '. ' + fact.argTitle : ''}</td>
                        <td>${(fact.exhibits || []).join(', ') || 'None'}</td>
                    `;
                    tableBody.appendChild(row);
                }});
            }}
            
            function renderTimeline() {{
                const tbody = document.getElementById('timeline-body');
                tbody.innerHTML = '';
                timelineData.forEach(item => {{
                    const row = document.createElement('tr');
                    if (item.status === 'Disputed') {{
                        row.style.backgroundColor = 'rgba(229, 62, 62, 0.05)';
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
            
            function renderExhibits() {{
                const tbody = document.getElementById('exhibits-body');
                tbody.innerHTML = '';
                exhibitsData.forEach(exh => {{
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${exh.id}</td>
                        <td>${exh.party}</td>
                        <td>${exh.title}</td>
                        <td>${exh.type}</td>
                        <td>${exh.summary}</td>
                    `;
                    tbody.appendChild(row);
                }});
            }}
        </script>
    </body>
    </html>
    """

    st.title("Summary of arguments (Doping Only)")
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
