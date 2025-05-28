import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Facts"

# Function to get facts data
def get_all_facts():
    facts = [
        {
            'point': 'Continuous operation under same name since 1950',
            'date': '1950-present',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '18-19',
            'exhibits': ['C-1'],
            'argId': '1',
            'argTitle': 'Sporting Succession'
        },
        {
            'point': 'Initial registration in 1950',
            'date': '1950',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '25-26',
            'exhibits': ['C-2'],
            'argId': '1.1.1',
            'argTitle': 'Registration History'
        },
        {
            'point': 'Brief administrative gap in 1975-1976',
            'date': '1975-1976',
            'isDisputed': True,
            'party': 'Appellant',
            'paragraphs': '29-30',
            'exhibits': ['C-2'],
            'argId': '1.1.1',
            'argTitle': 'Registration History'
        },
        {
            'point': 'Consistent use of blue and white since founding',
            'date': '1950-present',
            'isDisputed': True,
            'party': 'Appellant',
            'paragraphs': '51-52',
            'exhibits': ['C-4'],
            'argId': '1.2',
            'argTitle': 'Club Colors Analysis'
        },
        {
            'point': 'Minor shade variations do not affect continuity',
            'date': '1970-1980',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '56-57',
            'exhibits': ['C-5'],
            'argId': '1.2.1',
            'argTitle': 'Color Variations Analysis'
        },
        {
            'point': 'Temporary third color addition in 1980s',
            'date': '1982-1988',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '58-59',
            'exhibits': ['C-5'],
            'argId': '1.2.1',
            'argTitle': 'Color Variations Analysis'
        },
        {
            'point': 'Operations ceased between 1975-1976',
            'date': '1975-1976',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '206-207',
            'exhibits': ['R-1'],
            'argId': '1',
            'argTitle': 'Sporting Succession Rebuttal'
        },
        {
            'point': 'Registration formally terminated on April 30, 1975',
            'date': 'April 30, 1975',
            'isDisputed': False,
            'party': 'Respondent',
            'paragraphs': '226-227',
            'exhibits': ['R-2'],
            'argId': '1.1.1',
            'argTitle': 'Registration Gap Evidence'
        },
        {
            'point': 'New entity registered on September 15, 1976',
            'date': 'September 15, 1976',
            'isDisputed': False,
            'party': 'Respondent',
            'paragraphs': '228-229',
            'exhibits': ['R-2'],
            'argId': '1.1.1',
            'argTitle': 'Registration Gap Evidence'
        },
        {
            'point': 'Significant color scheme change in 1976',
            'date': '1976',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '245-246',
            'exhibits': ['R-4'],
            'argId': '1.2',
            'argTitle': 'Club Colors Analysis Rebuttal'
        },
        {
            'point': 'Pre-1976 colors represented original city district',
            'date': '1950-1975',
            'isDisputed': False,
            'party': 'Respondent',
            'paragraphs': '247',
            'exhibits': ['R-5'],
            'argId': '1.2.1',
            'argTitle': 'Color Changes Analysis'
        },
        {
            'point': 'Post-1976 colors represented new ownership region',
            'date': '1976-present',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '248-249',
            'exhibits': ['R-5'],
            'argId': '1.2.1',
            'argTitle': 'Color Changes Analysis'
        }
    ]
    
    return facts

# Function to create CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Main app
def main():
    # Get the facts data
    facts_data = get_all_facts()
    
    # Convert data to JSON for JavaScript use
    facts_json = json.dumps(facts_data)
    
    # Initialize session state if not already done
    if 'view' not in st.session_state:
        st.session_state.view = "Facts"
    
    # Add Streamlit sidebar with navigation buttons
    with st.sidebar:
        # Add the logo and CaseLens text
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
              <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#whatsapp-mask)">
                <!-- Rounded square background -->
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                <!-- WhatsApp phone icon -->
                <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <h1 style="margin-left: 10px; font-weight: 600; color: #4D68F9;">CaseLens</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
        
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
        
        # Define button click handlers
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Create buttons with names (keep all buttons but only Facts will work)
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
    
    # Always show Facts regardless of button clicked
    active_tab = 1  # Facts tab
    
    # Initialize the view options as a JavaScript variable
    view_options_json = json.dumps({
        "activeTab": active_tab
    })
    
    # Create HTML component containing only the Facts UI
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
            
            /* Content sections */
            .content-section {{
                display: none;
            }}
            
            .content-section.active {{
                display: block;
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
                cursor: pointer;
            }}
            
            th:hover {{
                background-color: #f1f1f1;
            }}
            
            td {{
                padding: 12px;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            tr.disputed {{
                background-color: rgba(229, 62, 62, 0.05);
            }}
            
            tr:hover {{
                background-color: #f8f9fa;
            }}
            
            /* Action buttons */
            .action-buttons {{
                position: absolute;
                top: 20px;
                right: 20px;
                display: flex;
                gap: 10px;
            }}
            
            .action-button {{
                padding: 8px 16px;
                background-color: #f9f9f9;
                border: 1px solid #e1e4e8;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                cursor: pointer;
            }}
            
            .action-button:hover {{
                background-color: #f1f1f1;
            }}
            
            .export-dropdown {{
                position: relative;
                display: inline-block;
            }}
            
            .export-dropdown-content {{
                display: none;
                position: absolute;
                right: 0;
                background-color: #f9f9f9;
                min-width: 160px;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
                border-radius: 4px;
            }}
            
            .export-dropdown-content a {{
                color: black;
                padding: 12px 16px;
                text-decoration: none;
                display: block;
                cursor: pointer;
            }}
            
            .export-dropdown-content a:hover {{
                background-color: #f1f1f1;
            }}
            
            .export-dropdown:hover .export-dropdown-content {{
                display: block;
            }}
            
            /* Facts styling */
            .facts-container {{
                margin-top: 20px;
            }}
            
            .facts-header {{
                display: flex;
                margin-bottom: 20px;
                border-bottom: 1px solid #dee2e6;
            }}
            
            .tab-button {{
                padding: 10px 20px;
                background: none;
                border: none;
                cursor: pointer;
            }}
            
            .tab-button.active {{
                border-bottom: 2px solid #4299e1;
                color: #4299e1;
                font-weight: 500;
            }}
            
            .facts-content {{
                margin-top: 20px;
            }}
            
            /* Section title */
            .section-title {{
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1rem;
                padding-bottom: 0.5rem;
                border-bottom: 1px solid #eaeaea;
            }}
            
            /* Copy notification */
            .copy-notification {{
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: #2d3748;
                color: white;
                padding: 10px 20px;
                border-radius: 4px;
                z-index: 1000;
                opacity: 0;
                transition: opacity 0.3s;
            }}
            
            .copy-notification.show {{
                opacity: 1;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div id="copy-notification" class="copy-notification">Content copied to clipboard!</div>
            
            <div class="action-buttons">
                <button class="action-button" onclick="copyAllContent()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                    Copy
                </button>
                <div class="export-dropdown">
                    <button class="action-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                            <polyline points="7 10 12 15 17 10"></polyline>
                            <line x1="12" y1="15" x2="12" y2="3"></line>
                        </svg>
                        Export
                    </button>
                    <div class="export-dropdown-content">
                        <a onclick="exportAsCsv()">CSV</a>
                        <a onclick="exportAsPdf()">PDF</a>
                        <a onclick="exportAsWord()">Word</a>
                    </div>
                </div>
            </div>
            
            <!-- Facts Section -->
            <div id="facts" class="content-section active">
                <div class="section-title">Case Facts</div>
                
                <div class="facts-header">
                    <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                    <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                    <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                </div>
                
                <div class="facts-content">
                    <table class="table-view">
                        <thead>
                            <tr>
                                <th onclick="sortTable('facts-table-body', 0)">Date</th>
                                <th onclick="sortTable('facts-table-body', 1)">Event</th>
                                <th onclick="sortTable('facts-table-body', 2)">Party</th>
                                <th onclick="sortTable('facts-table-body', 3)">Status</th>
                                <th onclick="sortTable('facts-table-body', 4)">Related Argument</th>
                                <th onclick="sortTable('facts-table-body', 5)">Evidence</th>
                            </tr>
                        </thead>
                        <tbody id="facts-table-body"></tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <script>
            // Initialize facts data
            const factsData = {facts_json};
            
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
                    
                    // Handle date sorting
                    if (columnIndex === 0) {{
                        // Attempt to parse as dates
                        const dateA = new Date(cellA);
                        const dateB = new Date(cellB);
                        
                        if (!isNaN(dateA) && !isNaN(dateB)) {{
                            return dir * (dateA - dateB);
                        }}
                    }}
                    
                    return dir * cellA.localeCompare(cellB);
                }});
                
                // Remove existing rows and append in new order
                rows.forEach(row => table.appendChild(row));
                
                // Store current sort direction and column
                table.setAttribute('data-sort-column', columnIndex);
                table.setAttribute('data-sort-dir', dir);
            }}
            
            // Switch facts tab
            function switchFactsTab(tabType) {{
                const allBtn = document.getElementById('all-facts-btn');
                const disputedBtn = document.getElementById('disputed-facts-btn');
                const undisputedBtn = document.getElementById('undisputed-facts-btn');
                
                // Remove active class from all
                allBtn.classList.remove('active');
                disputedBtn.classList.remove('active');
                undisputedBtn.classList.remove('active');
                
                // Add active to selected
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
            
            // Render facts table
            function renderFacts(type = 'all') {{
                const tableBody = document.getElementById('facts-table-body');
                tableBody.innerHTML = '';
                
                // Filter by type
                let filteredFacts = factsData;
                
                if (type === 'disputed') {{
                    filteredFacts = factsData.filter(fact => fact.isDisputed);
                }} else if (type === 'undisputed') {{
                    filteredFacts = factsData.filter(fact => !fact.isDisputed);
                }}
                
                // Sort by date
                filteredFacts.sort((a, b) => {{
                    // Handle date ranges like "1950-present"
                    const dateA = a.date.split('-')[0];
                    const dateB = b.date.split('-')[0];
                    return new Date(dateA) - new Date(dateB);
                }});
                
                // Render rows
                filteredFacts.forEach(fact => {{
                    const row = document.createElement('tr');
                    
                    // Date column
                    const dateCell = document.createElement('td');
                    dateCell.textContent = fact.date;
                    row.appendChild(dateCell);
                    
                    // Event column
                    const eventCell = document.createElement('td');
                    eventCell.textContent = fact.point;
                    row.appendChild(eventCell);
                    
                    // Party column
                    const partyCell = document.createElement('td');
                    const partyBadge = document.createElement('span');
                    partyBadge.className = `badge ${{fact.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}`;
                    partyBadge.textContent = fact.party;
                    partyCell.appendChild(partyBadge);
                    row.appendChild(partyCell);
                    
                    // Status column
                    const statusCell = document.createElement('td');
                    if (fact.isDisputed) {{
                        const disputedBadge = document.createElement('span');
                        disputedBadge.className = 'badge disputed-badge';
                        disputedBadge.textContent = 'Disputed';
                        statusCell.appendChild(disputedBadge);
                    }} else {{
                        statusCell.textContent = 'Undisputed';
                    }}
                    row.appendChild(statusCell);
                    
                    // Related argument
                    const argCell = document.createElement('td');
                    argCell.textContent = `${{fact.argId}}. ${{fact.argTitle}}`;
                    row.appendChild(argCell);
                    
                    // Evidence column
                    const evidenceCell = document.createElement('td');
                    if (fact.exhibits && fact.exhibits.length > 0) {{
                        fact.exhibits.forEach(exhibitId => {{
                            const exhibitBadge = document.createElement('span');
                            exhibitBadge.className = 'badge exhibit-badge';
                            exhibitBadge.textContent = exhibitId;
                            exhibitBadge.style.marginRight = '4px';
                            evidenceCell.appendChild(exhibitBadge);
                        }});
                    }} else {{
                        evidenceCell.textContent = 'None';
                    }}
                    row.appendChild(evidenceCell);
                    
                    tableBody.appendChild(row);
                }});
            }}
            
            // Copy all content function
            function copyAllContent() {{
                const contentToCopy = extractFactsText();
                
                // Create a temporary textarea to copy the content
                const textarea = document.createElement('textarea');
                textarea.value = contentToCopy;
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);
                
                // Show notification
                const notification = document.getElementById('copy-notification');
                notification.classList.add('show');
                
                setTimeout(() => {{
                    notification.classList.remove('show');
                }}, 2000);
            }}
            
            // Export functions
            function exportAsCsv() {{
                const contentToCsv = extractFactsText();
                
                // Create link for CSV download
                const csvContent = "data:text/csv;charset=utf-8," + encodeURIComponent(contentToCsv);
                const encodedUri = csvContent;
                const link = document.createElement("a");
                link.setAttribute("href", encodedUri);
                link.setAttribute("download", "facts.csv");
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }}
            
            function exportAsPdf() {{
                alert("PDF export functionality would be implemented here");
            }}
            
            function exportAsWord() {{
                alert("Word export functionality would be implemented here");
            }}
            
            // Extract text from facts
            function extractFactsText() {{
                const table = document.querySelector('.facts-content table');
                let text = '';
                
                // Get headers
                const headers = Array.from(table.querySelectorAll('th'))
                    .map(th => th.textContent.trim())
                    .join('\\t');
                
                text += headers + '\\n';
                
                // Get rows
                const rows = table.querySelectorAll('tbody tr');
                rows.forEach(row => {{
                    const rowText = Array.from(row.querySelectorAll('td'))
                        .map(td => td.textContent.trim())
                        .join('\\t');
                    
                    text += rowText + '\\n';
                }});
                
                return text;
            }}
            
            // Initialize the app
            document.addEventListener('DOMContentLoaded', function() {{
                // Show facts section
                document.getElementById('facts').classList.add('active');
                renderFacts('all');
            }});
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Case Facts Analysis")
    components.html(html_content, height=950, scrolling=True)

if __name__ == "__main__":
    main()
