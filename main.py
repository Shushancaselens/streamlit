# Main function to display the arguments section
def display_arguments_section():
    args_data = get_argument_data()
    facts_data = get_all_facts()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    
    # Get CSS styles
    css = get_arguments_css()
    
    # Create the HTML with JavaScript for the arguments section
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
                        if (arg
