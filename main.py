import streamlit as st
import json
import streamlit.components.v1 as components
import base64

# Get data structures as JSON for embedded components
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
            "factualPoints": [
                {
                    "point": "Continuous operation under same name since 1950",
                    "date": "1950-present",
                    "isDisputed": False,
                    "paragraphs": "18-19",
                    "exhibits": ["C-1"]
                }
            ],
            "evidence": [
                {
                    "id": "C-1",
                    "title": "Historical Registration Documents",
                    "summary": "Official records showing continuous name usage from 1950 to present day. Includes original registration certificate dated January 12, 1950, and all subsequent renewal documentation without interruption.",
                    "citations": ["20", "21", "24"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2016/A/4576",
                    "title": "Criteria for sporting succession",
                    "relevance": "Establishes key factors for succession including: (1) continuous use of identifying elements, (2) public recognition of the entity's identity, (3) preservation of sporting records and achievements, and (4) consistent participation in competitions under the same identity.",
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
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration History",
                            "paragraphs": "25-30",
                            "factualPoints": [
                                {
                                    "point": "Initial registration in 1950",
                                    "date": "1950",
                                    "isDisputed": False,
                                    "paragraphs": "25-26",
                                    "exhibits": ["C-2"]
                                },
                                {
                                    "point": "Brief administrative gap in 1975-1976",
                                    "date": "1975-1976",
                                    "isDisputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "29-30",
                                    "exhibits": ["C-2"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "C-2",
                                    "title": "Registration Records",
                                    "summary": "Comprehensive collection of official documentation showing the full registration history of the club from its founding to present day. Includes original application forms, government certificates, and renewal documentation.",
                                    "citations": ["25", "26", "28"]
                                }
                            ]
                        }
                    }
                },
                "1.2": {
                    "id": "1.2",
                    "title": "Club Colors Analysis",
                    "paragraphs": "46-65",
                    "overview": {
                        "points": [
                            "Consistent use of club colors",
                            "Minor variations analysis",
                            "Color trademark protection"
                        ],
                        "paragraphs": "46-47"
                    },
                    "factualPoints": [
                        {
                            "point": "Consistent use of blue and white since founding",
                            "date": "1950-present",
                            "isDisputed": True,
                            "source": "Respondent",
                            "paragraphs": "51-52",
                            "exhibits": ["C-4"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "C-4",
                            "title": "Historical Photographs",
                            "summary": "Collection of 73 photographs spanning from 1950 to present day showing the team's uniforms, promotional materials, and stadium decorations. Images are chronologically arranged and authenticated by sports historians.",
                            "citations": ["53", "54", "55"]
                        }
                    ],
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Variations Analysis",
                            "paragraphs": "56-60",
                            "factualPoints": [
                                {
                                    "point": "Minor shade variations do not affect continuity",
                                    "date": "1970-1980",
                                    "isDisputed": False,
                                    "paragraphs": "56-57",
                                    "exhibits": ["C-5"]
                                },
                                {
                                    "point": "Temporary third color addition in 1980s",
                                    "date": "1982-1988",
                                    "isDisputed": False,
                                    "paragraphs": "58-59",
                                    "exhibits": ["C-5"]
                                }
                            ],
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Historical Color Documentation",
                                    "paragraphs": "61-65",
                                    "evidence": [
                                        {
                                            "id": "C-5",
                                            "title": "Color Archives",
                                            "summary": "Detailed color specification documents from club archives, including official style guides, manufacturer specifications, and board meeting minutes about uniform decisions from 1950 to present day.",
                                            "citations": ["61", "62", "63"]
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
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
            "factualPoints": [
                {
                    "point": "Operations ceased between 1975-1976",
                    "date": "1975-1976",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "206-207",
                    "exhibits": ["R-1"]
                }
            ],
            "evidence": [
                {
                    "id": "R-1",
                    "title": "Federation Records",
                    "summary": "Official competition records from the National Football Federation for the 1975-1976 season, showing complete absence of the club from all levels of competition that season. Includes official withdrawal notification dated May 15, 1975.",
                    "citations": ["208", "209", "210"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2017/A/5465",
                    "title": "Operational continuity requirement",
                    "relevance": "Establishes that actual operational continuity (specifically participation in competitions) is the primary determinant of sporting succession, outweighing factors such as name, colors, or stadium usage when they conflict. The panel specifically ruled that a gap in competitive activity creates a presumption against continuity that must be overcome with substantial evidence.",
                    "paragraphs": "211-213",
                    "citedParagraphs": ["212"]
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
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration Gap Evidence",
                            "paragraphs": "226-230",
                            "factualPoints": [
                                {
                                    "point": "Registration formally terminated on April 30, 1975",
                                    "date": "April 30, 1975",
                                    "isDisputed": False,
                                    "paragraphs": "226-227",
                                    "exhibits": ["R-2"]
                                },
                                {
                                    "point": "New entity registered on September 15, 1976",
                                    "date": "September 15, 1976",
                                    "isDisputed": False,
                                    "paragraphs": "228-229",
                                    "exhibits": ["R-2"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "R-2",
                                    "title": "Termination Certificate",
                                    "summary": "Official government certificate of termination for the original club entity, stamped and notarized on April 30, 1975, along with completely new registration documents for a separate legal entity filed on September 15, 1976, with different founding members and bylaws.",
                                    "citations": ["226", "227"]
                                }
                            ]
                        }
                    }
                },
                "1.2": {
                    "id": "1.2",
                    "title": "Club Colors Analysis Rebuttal",
                    "paragraphs": "241-249",
                    "overview": {
                        "points": [
                            "Significant color variations",
                            "Trademark registration gaps",
                            "Multiple competing color claims"
                        ],
                        "paragraphs": "241-242"
                    },
                    "factualPoints": [
                        {
                            "point": "Significant color scheme change in 1976",
                            "date": "1976",
                            "isDisputed": True,
                            "source": "Claimant",
                            "paragraphs": "245-246",
                            "exhibits": ["R-4"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "R-4",
                            "title": "Historical Photographs Comparison",
                            "summary": "Side-by-side comparison of team uniforms from 1974 (pre-dissolution) and 1976 (post-new registration), showing significant differences in shade, pattern, and design elements. Includes expert color analysis report from textile historian confirming different dye formulations were used.",
                            "citations": ["245", "246", "247"]
                        }
                    ],
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Changes Analysis",
                            "paragraphs": "247-249",
                            "factualPoints": [
                                {
                                    "point": "Pre-1976 colors represented original city district",
                                    "date": "1950-1975",
                                    "isDisputed": False,
                                    "paragraphs": "247",
                                    "exhibits": ["R-5"]
                                },
                                {
                                    "point": "Post-1976 colors represented new ownership region",
                                    "date": "1976-present",
                                    "isDisputed": True,
                                    "source": "Claimant",
                                    "paragraphs": "248-249",
                                    "exhibits": ["R-5"]
                                }
                            ],
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Color Identity Documentation",
                                    "paragraphs": "250-255",
                                    "evidence": [
                                        {
                                            "id": "R-5",
                                            "title": "Marketing Materials",
                                            "summary": "Collection of promotional materials, merchandise, and internal design documents from both pre-1975 and post-1976 periods, showing the deliberate change in color symbolism used in marketing campaigns and communications with fans.",
                                            "citations": ["250", "251", "252"]
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    topics = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "argumentIds": ["1"]
        }
    ]
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args,
        "topics": topics
    }

# Get all facts from the data
def get_all_facts():
    args_data = get_argument_data()
    facts = []
    
    # Helper function to extract facts from arguments
    def extract_facts(arg, party):
        if not arg:
            return
            
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
                
        # Process children
        if 'children' in arg and arg['children']:
            for child_id, child in arg['children'].items():
                extract_facts(child, party)
    
    # Extract from claimant args
    for arg_id, arg in args_data['claimantArgs'].items():
        extract_facts(arg, 'Appellant')
        
    # Extract from respondent args
    for arg_id, arg in args_data['respondentArgs'].items():
        extract_facts(arg, 'Respondent')
        
    return facts

# Function to create CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Arguments section implementation
def display_arguments_section():
    args_data = get_argument_data()
    facts_data = get_all_facts()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    
    # Define CSS for the arguments section
    css = """
    <style>
        /* Minimalistic base styling */
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.5;
            color: #333;
            margin: 0;
            padding: 0;
            background-color: #fff;
        }
        
        /* Simple container */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Card styling */
        .card {
            background-color: #fff;
            border: 1px solid #f0f0f0;
            border-radius: 8px;
            margin-bottom: 16px;
            overflow: hidden;
        }
        
        .card-header {
            padding: 12px 16px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #f0f0f0;
            background-color: #fafafa;
        }
        
        .card-content {
            padding: 16px;
            display: none;
        }
        
        /* Arguments layout */
        .arguments-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        
        .side-heading {
            margin-bottom: 16px;
            font-weight: 500;
        }
        
        .appellant-color {
            color: #3182ce;
        }
        
        .respondent-color {
            color: #e53e3e;
        }
        
        /* Badge styling */
        .badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .appellant-badge {
            background-color: rgba(49, 130, 206, 0.1);
            color: #3182ce;
        }
        
        .respondent-badge {
            background-color: rgba(229, 62, 62, 0.1);
            color: #e53e3e;
        }
        
        .exhibit-badge {
            background-color: rgba(221, 107, 32, 0.1);
            color: #dd6b20;
        }
        
        .disputed-badge {
            background-color: rgba(229, 62, 62, 0.1);
            color: #e53e3e;
        }
        
        .para-badge {
            background-color: rgba(0, 0, 0, 0.05);
            color: #666;
            margin-left: 5px;
        }
        
        /* Evidence and factual points */
        .item-block {
            background-color: #fafafa;
            border-radius: 6px;
            padding: 12px;
            margin-bottom: 10px;
        }
        
        .item-title {
            font-weight: 600;
            margin-bottom: 6px;
            color: #333;
        }
        
        .evidence-block {
            background-color: #fff8f0;
            border-left: 3px solid #dd6b20;
            padding: 10px 12px;
            margin-bottom: 12px;
            border-radius: 0 4px 4px 0;
        }
        
        .caselaw-block {
            background-color: #ebf8ff;
            border-left: 3px solid #3182ce;
            padding: 10px 12px;
            margin-bottom: 12px;
            border-radius: 0 4px 4px 0;
        }
        
        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th {
            text-align: left;
            padding: 12px;
            background-color: #fafafa;
            border-bottom: 1px solid #f0f0f0;
        }
        
        td {
            padding: 12px;
            border-bottom: 1px solid #f0f0f0;
        }
        
        tr.disputed {
            background-color: rgba(229, 62, 62, 0.05);
        }
        
        /* Nested content */
        .nested-content {
            padding-left: 20px;
            margin-top: 10px;
            border-left: 1px solid #f0f0f0;
        }
        
        /* Simple list styling */
        ul.point-list {
            list-style-type: none;
            padding-left: 0;
            margin: 0;
        }
        
        ul.point-list li {
            position: relative;
            padding-left: 16px;
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }
        
        ul.point-list li:before {
            content: "•";
            position: absolute;
            left: 0;
            color: #8c8c8c;
        }
        
        /* Chevron icon */
        .chevron {
            transition: transform 0.2s;
        }
        
        .chevron.expanded {
            transform: rotate(90deg);
        }
        
        /* Citation tags */
        .citation-tag {
            padding: 2px 5px;
            background: rgba(0,0,0,0.05);
            border-radius: 3px;
            font-size: 11px;
            color: #666;
            margin-right: 2px;
        }
        
        /* Section title */
        .section-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eaeaea;
        }
        
        /* Table view */
        .table-view {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        .table-view th {
            padding: 12px;
            text-align: left;
            background-color: #f8f9fa;
            border-bottom: 2px solid #dee2e6;
            position: sticky;
            top: 0;
            cursor: pointer;
        }
        
        .table-view th:hover {
            background-color: #e9ecef;
        }
        
        .table-view td {
            padding: 12px;
            border-bottom: 1px solid #dee2e6;
        }
        
        .table-view tr:hover {
            background-color: #f8f9fa;
        }
        
        /* View toggle */
        .view-toggle {
            display: flex;
            justify-content: flex-end;
            margin-bottom: 16px;
        }
        
        .view-toggle button {
            padding: 8px 16px;
            border: 1px solid #e2e8f0;
            background-color: #f7fafc;
            cursor: pointer;
        }
        
        .view-toggle button.active {
            background-color: #4299e1;
            color: white;
            border-color: #4299e1;
        }
        
        .view-toggle button:first-child {
            border-radius: 4px 0 0 4px;
        }
        
        .view-toggle button:last-child {
            border-radius: 0 4px 4px 0;
        }
    </style>
    """
    
    # Create the HTML content for the arguments section
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        {css}
    </head>
    <body>
        <div class="container">
            <div id="arguments" class="content-section active">
                <div class="section-title">Legal Arguments</div>
                
                <!-- View toggle buttons -->
                <div class="view-toggle" style="display: flex; justify-content: space-between;">
                    <div>
                        <button id="both-parties-btn" class="active" onclick="switchPartyView('both')">Both Parties</button>
                        <button id="appellant-btn" onclick="switchPartyView('appellant')">Appellant Only</button>
                        <button id="respondent-btn" onclick="switchPartyView('respondent')">Respondent Only</button>
                    </div>
                    <div>
                        <button id="detailed-view-btn" class="active" onclick="switchView('detailed')">Detailed View</button>
                        <button id="table-view-btn" onclick="switchView('table')">Table View</button>
                    </div>
                </div>
                
                <!-- Detailed view content -->
                <div id="detailed-view" class="view-content active">
                    <div id="topics-container"></div>
                </div>
                
                <!-- Table view content -->
                <div id="table-view" class="view-content" style="display: none;">
                    <table class="table-view">
                        <thead>
                            <tr>
                                <th onclick="sortTable('table-view-body', 0)">ID</th>
                                <th onclick="sortTable('table-view-body', 1)">Argument</th>
                                <th onclick="sortTable('table-view-body', 2)">Party</th>
                                <th onclick="sortTable('table-view-body', 3)">Status</th>
                                <th onclick="sortTable('table-view-body', 4)">Evidence</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody id="table-view-body"></tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <script>
            // Initialize data
            const argsData = {args_json};
            const factsData = {facts_json};
            
            // Global variable to track current party view
            let currentPartyView = 'both';
            
            // Document ready
            document.addEventListener('DOMContentLoaded', function() {{
                renderTopics();
                renderArgumentsTable();
            }});
            
            // Switch view between detailed and table
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
            
            // Switch party view
            function switchPartyView(partyType) {{
                currentPartyView = partyType;
                const bothBtn = document.getElementById('both-parties-btn');
                const appellantBtn = document.getElementById('appellant-btn');
                const respondentBtn = document.getElementById('respondent-btn');
                
                // Remove active class from all
                bothBtn.classList.remove('active');
                appellantBtn.classList.remove('active');
                respondentBtn.classList.remove('active');
                
                // Add active to selected
                if (partyType === 'both') {{
                    bothBtn.classList.add('active');
                }} else if (partyType === 'appellant') {{
                    appellantBtn.classList.add('active');
                }} else {{
                    respondentBtn.classList.add('active');
                }}
                
                // Re-render views with selected party filter
                renderTopics();
                renderArgumentsTable();
            }}
            
            // Sort table function
            function sortTable(tableId, columnIndex) {{
                const table = document.getElementById(tableId);
                const rows = Array.from(table.rows);
                let dir = 1; // 1 for ascending, -1 for descending
                
                // Check if already sorted in this direction
                if (table.getAttribute('data-sort-column') === String(columnIndex) &&
                    table.getAttribute('data-sort-dir') === '1') {{
                    dir = -1;
                }}
                
                // Sort the rows
                rows.sort((a, b) => {{
                    const cellA = a.cells[columnIndex].textContent.trim();
                    const cellB = b.cells[columnIndex].textContent.trim();
                    
                    return dir * cellA.localeCompare(cellB);
                }});
                
                // Remove existing rows and append in new order
                rows.forEach(row => table.appendChild(row));
                
                // Store current sort direction and column
                table.setAttribute('data-sort-column', columnIndex);
                table.setAttribute('data-sort-dir', dir);
            }}
            
            // Render arguments in table format
            function renderArgumentsTable() {{
                const tableBody = document.getElementById('table-view-body');
                tableBody.innerHTML = '';
                
                // Helper function to flatten arguments
                function flattenArguments(args, party) {{
                    let result = [];
                    
                    Object.values(args).forEach(arg => {{
                        // Track if argument has disputed facts
                        const hasDisputedFacts = arg.factualPoints && 
                            arg.factualPoints.some(point => point.isDisputed);
                        
                        // Count pieces of evidence
                        const evidenceCount = arg.evidence ? arg.evidence.length : 0;
                        
                        // Add this argument
                        result.push({{
                            id: arg.id,
                            title: arg.title,
                            party: party,
                            hasDisputedFacts: hasDisputedFacts,
                            evidenceCount: evidenceCount,
                            paragraphs: arg.paragraphs
                        }});
                        
                        // Process children recursively
                        if (arg.children) {{
                            Object.values(arg.children).forEach(child => {{
                                result = result.concat(flattenArguments({{[child.id]: child}}, party));
                            }});
                        }}
                    }});
                    
                    return result;
                }}
                
                // Get flattened arguments
                const appellantArgs = flattenArguments(argsData.claimantArgs, "Appellant");
                const respondentArgs = flattenArguments(argsData.respondentArgs, "Respondent");
                
                // Filter based on current party view
                let allArgs = [];
                if (currentPartyView === 'both') {{
                    allArgs = [...appellantArgs, ...respondentArgs];
                }} else if (currentPartyView === 'appellant') {{
                    allArgs = appellantArgs;
                }} else {{
                    allArgs = respondentArgs;
                }}
                
                // Render rows
                allArgs.forEach(arg => {{
                    const row = document.createElement('tr');
                    
                    // ID column
                    const idCell = document.createElement('td');
                    idCell.textContent = arg.id;
                    row.appendChild(idCell);
                    
                    // Title column
                    const titleCell = document.createElement('td');
                    titleCell.textContent = arg.title;
                    row.appendChild(titleCell);
