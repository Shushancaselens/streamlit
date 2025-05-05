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
if 'facts_view_mode' not in st.session_state:
    st.session_state.facts_view_mode = "table"

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
                    'argTitle': arg['title'],
                    'document_set': get_document_set_for_point(point['point'], party)
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

# Helper function to assign document sets to facts
def get_document_set_for_point(point, party):
    # This is a simplified mapping - in a real app would be more sophisticated
    doc_sets = get_document_sets()
    
    if party == "Appellant":
        if "1950" in point:
            return doc_sets["claimant"][2]  # "5. Appeal Brief"
        elif "administrative gap" in point:
            return doc_sets["claimant"][0]  # "1. Statement of Appeal"
        else:
            return doc_sets["claimant"][1]  # "3. Answer to Request for PM"
    else:  # Respondent
        if "operations ceased" in point:
            return doc_sets["respondent"][2]  # "6. Brief on Admissibility"
        elif "terminated" in point:
            return doc_sets["respondent"][4]  # "Objection to Admissibility"
        else:
            return doc_sets["respondent"][1]  # "4. Answer to PM"

# Get document sets
def get_document_sets():
    return {
        "claimant": [
            "1. Statement of Appeal",
            "3. Answer to Request for PM",
            "5. Appeal Brief",
            "7. Reply to Objection to Admissibility"
        ],
        "respondent": [
            "2. Request for a Stay", 
            "4. Answer to PM",
            "6. Brief on Admissibility",
            "8. Challenge",
            "Objection to Admissibility"
        ],
        "other": [
            "ChatGPT",
            "Jurisprudence",
            "Swiss Court"
        ]
    }

# Get argument data
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
                    "children": {}
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

# Function to create CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Main app
def main():
    # Get the data for JavaScript
    facts_data = get_all_facts()
    
    # Convert data to JSON for JavaScript use
    facts_json = json.dumps(facts_data)
    
    # Initialize session state if not already done
    if 'view' not in st.session_state:
        st.session_state.view = "Facts"
    
    # Add Streamlit sidebar with navigation buttons only
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
        
        # Create buttons with names
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
    
    # Facts page content
    if st.session_state.view == "Facts":
        st.title("Case Facts")
        
        # View selector buttons
        cols = st.columns([4, 1, 1])
        with cols[1]:
            # Button for Table View
            btn_style = "primary" if st.session_state.facts_view_mode == "table" else "secondary"
            if st.button("Table View", type=btn_style, use_container_width=True):
                st.session_state.facts_view_mode = "table"
                st.rerun()
        with cols[2]:
            # Button for Document Sets View
            btn_style = "primary" if st.session_state.facts_view_mode == "sets" else "secondary"
            if st.button("Document Sets View", type=btn_style, use_container_width=True):
                st.session_state.facts_view_mode = "sets"
                st.rerun()
        
        # Table view (original HTML component)
        if st.session_state.facts_view_mode == "table":
            # Create HTML component with the facts table
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
                    }}
                    
                    td {{
                        padding: 12px;
                        border-bottom: 1px solid #f0f0f0;
                    }}
                    
                    tr.disputed {{
                        background-color: rgba(229, 62, 62, 0.05);
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
                    
                    /* Table view */
                    .table-view {{
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                    }}
                    
                    .table-view th {{
                        padding: 12px;
                        text-align: left;
                        background-color: #f8f9fa;
                        border-bottom: 2px solid #dee2e6;
                        position: sticky;
                        top: 0;
                        cursor: pointer;
                    }}
                    
                    .table-view th:hover {{
                        background-color: #e9ecef;
                    }}
                    
                    .table-view td {{
                        padding: 12px;
                        border-bottom: 1px solid #dee2e6;
                    }}
                    
                    .table-view tr:hover {{
                        background-color: #f8f9fa;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div id="facts" class="content-section active">
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
                    
                    // Initialize facts on page load
                    document.addEventListener('DOMContentLoaded', function() {{
                        renderFacts('all');
                    }});
                    
                    // Initialize facts immediately
                    renderFacts('all');
                </script>
            </body>
            </html>
            """
            
            # Render the HTML component
            components.html(html_content, height=600, scrolling=True)
            
        # Document Sets View
        else:
            # Create a dataframe of the facts data 
            facts_df = pd.DataFrame(facts_data)
            
            # Create tabs for filtering facts
            tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
            
            with tab1:
                # Group by document set
                doc_sets = sorted(facts_df['document_set'].unique())
                
                for doc_set in doc_sets:
                    st.subheader(doc_set)
                    
                    # Filter facts by document set
                    set_facts = facts_df[facts_df['document_set'] == doc_set]
                    
                    # Create HTML for document set facts
                    set_facts_json = json.dumps(set_facts.to_dict('records'))
                    set_html = f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <style>
                            body {{
                                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                                line-height: 1.5;
                                color: #333;
                                margin: 0;
                                padding: 0;
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
                            }}
                            
                            td {{
                                padding: 12px;
                                border-bottom: 1px solid #f0f0f0;
                            }}
                            
                            tr.disputed {{
                                background-color: rgba(229, 62, 62, 0.05);
                            }}
                            
                            /* Table view */
                            .table-view {{
                                width: 100%;
                                border-collapse: collapse;
                            }}
                            
                            .table-view th {{
                                padding: 12px;
                                text-align: left;
                                background-color: #f8f9fa;
                                border-bottom: 2px solid #dee2e6;
                                position: sticky;
                                top: 0;
                                cursor: pointer;
                            }}
                            
                            .table-view th:hover {{
                                background-color: #e9ecef;
                            }}
                            
                            .table-view td {{
                                padding: 12px;
                                border-bottom: 1px solid #dee2e6;
                            }}
                            
                            .table-view tr:hover {{
                                background-color: #f8f9fa;
                            }}
                        </style>
                    </head>
                    <body>
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
                            <tbody id="set-facts-body"></tbody>
                        </table>
                        
                        <script>
                            // Initialize facts data
                            const setFactsData = {set_facts_json};
                            
                            // Render facts table
                            function renderSetFacts() {{
                                const tableBody = document.getElementById('set-facts-body');
                                tableBody.innerHTML = '';
                                
                                // Sort by date
                                setFactsData.sort((a, b) => {{
                                    // Handle date ranges like "1950-present"
                                    const dateA = a.date.split('-')[0];
                                    const dateB = b.date.split('-')[0];
                                    return new Date(dateA) - new Date(dateB);
                                }});
                                
                                // Render rows
                                setFactsData.forEach(fact => {{
                                    const row = document.createElement('tr');
                                    if (fact.isDisputed) {{
                                        row.classList.add('disputed');
                                    }}
                                    
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
                            
                            // Initialize immediately
                            renderSetFacts();
                        </script>
                    </body>
                    </html>
                    """
                    
                    # Display the HTML component
                    components.html(set_html, height=400, scrolling=True)
                    
                    # CSV download link
                    st.markdown(get_csv_download_link(set_facts, f"{doc_set.replace(' ', '_')}_facts.csv", f"Download {doc_set} Facts CSV"), unsafe_allow_html=True)
                    st.markdown("---")

            with tab2:
                # Filter for disputed facts
                disputed_facts = facts_df[facts_df['isDisputed'] == True]
                
                # Group disputed facts by document set
                if not disputed_facts.empty:
                    doc_sets = sorted(disputed_facts['document_set'].unique())
                    
                    for doc_set in doc_sets:
                        st.subheader(doc_set)
                        
                        # Filter facts by document set
                        set_facts = disputed_facts[disputed_facts['document_set'] == doc_set]
                        
                        # Create HTML for document set facts
                        set_facts_json = json.dumps(set_facts.to_dict('records'))
                        set_html = f"""
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <style>
                                body {{
                                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                                    line-height: 1.5;
                                    color: #333;
                                    margin: 0;
                                    padding: 0;
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
                                }}
                                
                                td {{
                                    padding: 12px;
                                    border-bottom: 1px solid #f0f0f0;
                                }}
                                
                                tr.disputed {{
                                    background-color: rgba(229, 62, 62, 0.05);
                                }}
                                
                                /* Table view */
                                .table-view {{
                                    width: 100%;
                                    border-collapse: collapse;
                                }}
                                
                                .table-view th {{
                                    padding: 12px;
                                    text-align: left;
                                    background-color: #f8f9fa;
                                    border-bottom: 2px solid #dee2e6;
                                    position: sticky;
                                    top: 0;
                                }}
                                
                                .table-view td {{
                                    padding: 12px;
                                    border-bottom: 1px solid #dee2e6;
                                }}
                                
                                .table-view tr:hover {{
                                    background-color: #f8f9fa;
                                }}
                            </style>
                        </head>
                        <body>
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
                                <tbody id="disputed-set-facts-body"></tbody>
                            </table>
                            
                            <script>
                                // Initialize facts data
                                const disputedSetFactsData = {set_facts_json};
                                
                                // Render facts table
                                function renderDisputedSetFacts() {{
                                    const tableBody = document.getElementById('disputed-set-facts-body');
                                    tableBody.innerHTML = '';
                                    
                                    // Render rows
                                    disputedSetFactsData.forEach(fact => {{
                                        const row = document.createElement('tr');
                                        row.classList.add('disputed');
                                        
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
                                        const disputedBadge = document.createElement('span');
                                        disputedBadge.className = 'badge disputed-badge';
                                        disputedBadge.textContent = 'Disputed';
                                        statusCell.appendChild(disputedBadge);
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
                                
                                // Initialize immediately
                                renderDisputedSetFacts();
                            </script>
                        </body>
                        </html>
                        """
                        
                        # Display the HTML component
                        components.html(set_html, height=400, scrolling=True)
                        
                        # CSV download link
                        st.markdown(get_csv_download_link(set_facts, f"disputed_{doc_set.replace(' ', '_')}_facts.csv", f"Download Disputed {doc_set} Facts CSV"), unsafe_allow_html=True)
                        st.markdown("---")
                else:
                    st.info("No disputed facts found.")

            with tab3:
                # Filter for undisputed facts
                undisputed_facts = facts_df[facts_df['isDisputed'] == False]
                
                # Group undisputed facts by document set
                if not undisputed_facts.empty:
                    doc_sets = sorted(undisputed_facts['document_set'].unique())
                    
                    for doc_set in doc_sets:
                        st.subheader(doc_set)
                        
                        # Filter facts by document set
                        set_facts = undisputed_facts[undisputed_facts['document_set'] == doc_set]
                        
                        # Create HTML for document set facts
                        set_facts_json = json.dumps(set_facts.to_dict('records'))
                        set_html = f"""
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <style>
                                body {{
                                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                                    line-height: 1.5;
                                    color: #333;
                                    margin: 0;
                                    padding: 0;
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
                                
                                /* Table view */
                                .table-view {{
                                    width: 100%;
                                    border-collapse: collapse;
                                }}
                                
                                .table-view th {{
                                    padding: 12px;
                                    text-align: left;
                                    background-color: #f8f9fa;
                                    border-bottom: 2px solid #dee2e6;
                                    position: sticky;
                                    top: 0;
                                }}
                                
                                .table-view td {{
                                    padding: 12px;
                                    border-bottom: 1px solid #dee2e6;
                                }}
                                
                                .table-view tr:hover {{
                                    background-color: #f8f9fa;
                                }}
                            </style>
                        </head>
                        <body>
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
                                <tbody id="undisputed-set-facts-body"></tbody>
                            </table>
                            
                            <script>
                                // Initialize facts data
                                const undisputedSetFactsData = {set_facts_json};
                                
                                // Render facts table
                                function renderUndisputedSetFacts() {{
                                    const tableBody = document.getElementById('undisputed-set-facts-body');
                                    tableBody.innerHTML = '';
                                    
                                    // Render rows
                                    undisputedSetFactsData.forEach(fact => {{
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
                                        statusCell.textContent = 'Undisputed';
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
                                
                                // Initialize immediately
                                renderUndisputedSetFacts();
                            </script>
                        </body>
                        </html>
                        """
                        
                        # Display the HTML component
                        components.html(set_html, height=400, scrolling=True)
                        
                        # CSV download link
                        st.markdown(get_csv_download_link(set_facts, f"undisputed_{doc_set.replace(' ', '_')}_facts.csv", f"Download Undisputed {doc_set} Facts CSV"), unsafe_allow_html=True)
                        st.markdown("---")
                else:
                    st.info("No undisputed facts found.")

if __name__ == "__main__":
    main()
