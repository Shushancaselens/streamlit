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

# Function to get comprehensive facts data with chronology
def get_all_facts():
    facts = [
        {
            'date': '1950-01-12',
            'point': 'Club officially registered under current name',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '18-19',
            'exhibits': ['C-1'],
            'argId': '1',
            'argTitle': 'Sporting Succession',
            'sources': 3,
            'proceedings': 'registration',
            'addressedBy': 'Both Parties',
            'supportingDocs': [
                {
                    'id': 'C-1',
                    'title': 'Original Registration Certificate',
                    'summary': 'Official registration document dated January 12, 1950, establishing the football club under its current name. The certificate was issued by the Municipal Sports Authority and includes founding member signatures, initial bylaws, and the club\'s stated objectives of promoting football in the local community.',
                    'source': 'Municipal Registry Office, Document Archive Section',
                    'pageRef': 'Page 15: Certificate No. 1950-FB-012, Municipal Sports Authority Registration'
                }
            ]
        },
        {
            'date': '1950-03-15',
            'point': 'First official match played under club colors',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '51-52',
            'exhibits': ['C-4', 'C-6'],
            'argId': '1.2',
            'argTitle': 'Club Colors Analysis',
            'sources': 2,
            'proceedings': 'evidence',
            'addressedBy': 'Appellant',
            'supportingDocs': [
                {
                    'id': 'C-4',
                    'title': 'Historical Match Records',
                    'summary': 'Official match report from March 15, 1950, documenting the club\'s first competitive fixture. The report includes team lineup, final score (2-1 victory), and notably describes the team uniform as "traditional blue and white striped jerseys with blue shorts." Local newspaper coverage from the same date corroborates the uniform description.',
                    'source': 'Regional Football Association Archives',
                    'pageRef': 'Page 23: Match Report RFA-1950-003, Regional Football Association'
                },
                {
                    'id': 'C-6',
                    'title': 'Newspaper Coverage',
                    'summary': 'Contemporary newspaper article from the Local Daily Sports section, March 16, 1950, featuring a photograph of the team in their debut match. The black and white photograph clearly shows the striped pattern of the jerseys, and the accompanying article specifically mentions the club\'s choice of blue and white as representing the city\'s traditional colors.',
                    'source': 'Local Daily Sports Archive',
                    'pageRef': 'Page 12: Sports Section, Local Daily, March 16, 1950 Edition'
                }
            ]
        },
        {
            'date': '1975-04-30',
            'point': 'Registration formally terminated',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '206-207',
            'exhibits': ['R-1', 'R-2'],
            'argId': '1',
            'argTitle': 'Sporting Succession Rebuttal',
            'sources': 4,
            'proceedings': 'challenge',
            'addressedBy': 'Respondent Only',
            'supportingDocs': [
                {
                    'id': 'R-1',
                    'title': 'Official Termination Certificate',
                    'summary': 'Government-issued certificate of termination dated April 30, 1975, formally dissolving the original club entity. The document cites "financial insolvency and failure to meet regulatory requirements" as grounds for termination. Signed by the Regional Sports Commissioner and notarized by the Municipal Clerk.',
                    'source': 'Regional Sports Authority',
                    'pageRef': 'Page 45: Termination Certificate RSA-1975-089, Regional Sports Authority'
                },
                {
                    'id': 'R-2',
                    'title': 'Bankruptcy Proceedings',
                    'summary': 'Court documents from bankruptcy proceedings initiated against the club in early 1975. The filing shows debts totaling €127,000 to various creditors including players, suppliers, and the municipal stadium authority. The bankruptcy trustee\'s report details the liquidation of all club assets.',
                    'source': 'Municipal Court Records',
                    'pageRef': 'Page 67-89: Case No. MC-1975-234, Municipal Commercial Court'
                }
            ]
        },
        {
            'date': '1975-05-15',
            'point': 'Club ceased all competitive activities',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '208-209',
            'exhibits': ['R-3'],
            'argId': '1',
            'argTitle': 'Operational Continuity',
            'sources': 2,
            'proceedings': 'evidence',
            'addressedBy': 'Not Addressed',
            'supportingDocs': [
                {
                    'id': 'R-3',
                    'title': 'League Withdrawal Notice',
                    'summary': 'Official notification to the National Football League dated May 15, 1975, announcing the club\'s immediate withdrawal from all competitions for the remainder of the 1975 season and indefinitely thereafter. The letter cites "insurmountable financial difficulties" and was signed by the then-club president.',
                    'source': 'National Football League Archives',
                    'pageRef': 'Page 156: Correspondence File NFL-1975-WD-47, National Football League'
                }
            ]
        },
        {
            'date': '1976-09-15',
            'point': 'New entity registered with same name',
            'isDisputed': True,
            'party': 'Both',
            'paragraphs': '228-229',
            'exhibits': ['R-4', 'C-7'],
            'argId': '1.1.1',
            'argTitle': 'Registration Gap Evidence',
            'sources': 5,
            'proceedings': 'challenge',
            'addressedBy': 'Both Parties',
            'supportingDocs': [
                {
                    'id': 'R-4',
                    'title': 'New Registration Documents',
                    'summary': 'Registration papers for a new football club entity dated September 15, 1976, using the same name as the terminated club. The founding members listed are entirely different from the original 1950 registration, and the registered address is in a different district of the city. The stated objectives include "continuing the football tradition of the local community."',
                    'source': 'Municipal Registry Office',
                    'pageRef': 'Page 203: Certificate No. 1976-FB-156, Municipal Sports Authority Registration'
                },
                {
                    'id': 'C-7',
                    'title': 'Continuity Declaration',
                    'summary': 'Statutory declaration signed by three founding members of the 1976 entity, asserting their intention to continue the legacy and traditions of the original club. The document references the club\'s historical achievements and states the founders\' commitment to maintaining the same colors, name, and community connection.',
                    'source': 'Notary Public Records',
                    'pageRef': 'Page 78: Statutory Declaration SD-1976-445, Municipal Notary Office'
                }
            ]
        },
        {
            'date': '1976-10-22',
            'point': 'First match under new entity with modified colors',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '245-246',
            'exhibits': ['R-5'],
            'argId': '1.2',
            'argTitle': 'Club Colors Analysis Rebuttal',
            'sources': 3,
            'proceedings': 'evidence',
            'addressedBy': 'Respondent Only',
            'supportingDocs': [
                {
                    'id': 'R-5',
                    'title': 'Match Report and Photographs',
                    'summary': 'Comprehensive match report from October 22, 1976, documenting the new entity\'s first competitive fixture. Color photographs clearly show jerseys in a darker shade of blue with white trim, distinctly different from the original light blue and white stripes. The match program notes this as a "new beginning" for the club.',
                    'source': 'Regional Football Association',
                    'pageRef': 'Page 34-36: Match Report RFA-1976-087, with Official Photography'
                }
            ]
        },
        {
            'date': '1982-01-10',
            'point': 'Temporary addition of third color (red trim)',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '58-59',
            'exhibits': ['C-5'],
            'argId': '1.2.1',
            'argTitle': 'Color Variations Analysis',
            'sources': 1,
            'proceedings': 'registration',
            'addressedBy': 'Appellant',
            'supportingDocs': [
                {
                    'id': 'C-5',
                    'title': 'Board Meeting Minutes',
                    'summary': 'Minutes from the club\'s board meeting on January 10, 1982, documenting the decision to add red trim to jerseys for the 1982-1988 period. The decision was made to commemorate the club\'s partnership with a local sponsor and was explicitly described as "temporary" with plans to revert to traditional colors.',
                    'source': 'Club Archive Records',
                    'pageRef': 'Page 91: Board Minutes BM-1982-002, Club Secretary Archives'
                }
            ]
        },
        {
            'date': '1988-06-30',
            'point': 'Return to traditional blue and white colors',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '60-61',
            'exhibits': ['C-8'],
            'argId': '1.2.1',
            'argTitle': 'Color Restoration',
            'sources': 2,
            'proceedings': 'evidence',
            'addressedBy': 'Both Parties',
            'supportingDocs': [
                {
                    'id': 'C-8',
                    'title': 'Jersey Design Specifications',
                    'summary': 'Official design specifications dated June 30, 1988, showing the return to blue and white striped jerseys without red trim. The document includes color swatches and explicitly states the intention to "restore the club\'s traditional appearance as worn since 1950." Manufacturer invoices confirm the production of jerseys matching these specifications.',
                    'source': 'Kit Manufacturer Records',
                    'pageRef': 'Page 145: Design Spec DS-1988-034, Sports Kit Manufacturing Ltd.'
                }
            ]
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
    
    # Create HTML component containing comprehensive Facts UI
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
            
            /* Chronology entry styling */
            .chronology-entry {{
                border: 1px solid #e1e5e9;
                border-radius: 8px;
                margin-bottom: 20px;
                background: white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }}
            
            .chronology-header {{
                padding: 16px 20px;
                border-bottom: 1px solid #e1e5e9;
                background-color: #f8f9fa;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            
            .chronology-header:hover {{
                background-color: #e9ecef;
            }}
            
            .chronology-date {{
                font-weight: 600;
                color: #2d3748;
            }}
            
            .chronology-event {{
                margin-left: 20px;
                flex-grow: 1;
            }}
            
            .chronology-content {{
                padding: 20px;
                display: none;
            }}
            
            .chronology-content.active {{
                display: block;
            }}
            
            /* Sources and metadata */
            .metadata-row {{
                display: flex;
                gap: 40px;
                margin-bottom: 20px;
                font-size: 14px;
            }}
            
            .metadata-item {{
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            
            .sources-count {{
                background: #3182ce;
                color: white;
                padding: 4px 8px;
                border-radius: 4px;
                font-weight: 500;
            }}
            
            .proceedings-tab {{
                padding: 6px 12px;
                border-radius: 4px;
                font-size: 12px;
                text-transform: capitalize;
            }}
            
            .proceedings-registration {{
                background: #e6fffa;
                color: #00695c;
            }}
            
            .proceedings-challenge {{
                background: #fff5f5;
                color: #c53030;
            }}
            
            .proceedings-evidence {{
                background: #f0f4ff;
                color: #3182ce;
            }}
            
            .addressed-status {{
                font-size: 12px;
                color: #666;
            }}
            
            /* Supporting documents */
            .supporting-docs {{
                margin-top: 20px;
            }}
            
            .supporting-docs h4 {{
                margin-bottom: 16px;
                font-size: 16px;
                font-weight: 600;
            }}
            
            .document-card {{
                border: 1px solid #e1e5e9;
                border-radius: 6px;
                margin-bottom: 16px;
                background: #fafbfc;
            }}
            
            .document-header {{
                padding: 12px 16px;
                border-bottom: 1px solid #e1e5e9;
                background: white;
            }}
            
            .document-title {{
                font-weight: 600;
                color: #2d3748;
                margin-bottom: 4px;
            }}
            
            .document-summary {{
                padding: 16px;
                line-height: 1.6;
            }}
            
            .document-source {{
                padding: 12px 16px;
                background: #e8f5e8;
                border-radius: 0 0 6px 6px;
                font-size: 12px;
            }}
            
            .source-label {{
                font-weight: 600;
                color: #2d5016;
            }}
            
            .page-ref {{
                font-style: italic;
                color: #5a5a5a;
                margin-top: 4px;
            }}
            
            /* Document actions */
            .document-actions {{
                display: flex;
                gap: 12px;
                padding: 12px 16px;
                border-top: 1px solid #e1e5e9;
                background: #f8f9fa;
            }}
            
            .action-btn {{
                padding: 6px 12px;
                border: 1px solid #d1d5db;
                border-radius: 4px;
                background: white;
                cursor: pointer;
                font-size: 12px;
                display: flex;
                align-items: center;
                gap: 4px;
                transition: all 0.2s;
            }}
            
            .action-btn:hover {{
                background: #f3f4f6;
                transform: translateY(-1px);
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
            
            .both-badge {{
                background-color: rgba(128, 90, 213, 0.1);
                color: #805ad5;
            }}
            
            .exhibit-badge {{
                background-color: rgba(221, 107, 32, 0.1);
                color: #dd6b20;
            }}
            
            .disputed-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            .undisputed-badge {{
                background-color: rgba(72, 187, 120, 0.1);
                color: #38a169;
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
            
            /* Chevron icon */
            .chevron {{
                transition: transform 0.2s;
                margin-left: 8px;
            }}
            
            .chevron.expanded {{
                transform: rotate(90deg);
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
                <div class="section-title">Case Chronology</div>
                
                <div class="facts-header">
                    <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                    <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                    <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                </div>
                
                <div class="facts-content" id="chronology-container">
                    <!-- Chronology entries will be populated here -->
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
                    renderChronology('all');
                }} else if (tabType === 'disputed') {{
                    disputedBtn.classList.add('active');
                    renderChronology('disputed');
                }} else {{
                    undisputedBtn.classList.add('active');
                    renderChronology('undisputed');
                }}
            }}
            
            // Toggle chronology entry
            function toggleChronologyEntry(entryId) {{
                const content = document.getElementById(`content-${{entryId}}`);
                const chevron = document.getElementById(`chevron-${{entryId}}`);
                
                if (content.classList.contains('active')) {{
                    content.classList.remove('active');
                    chevron.classList.remove('expanded');
                }} else {{
                    content.classList.add('active');
                    chevron.classList.add('expanded');
                }}
            }}
            
            // Document actions
            function viewDocument(docId) {{
                alert(`Opening document: ${{docId}}`);
            }}
            
            function downloadPDF(docId) {{
                alert(`Downloading PDF for: ${{docId}}`);
            }}
            
            function copySource(docId, source) {{
                navigator.clipboard.writeText(source).then(() => {{
                    showNotification('Source copied to clipboard!');
                }});
            }}
            
            function showNotification(message) {{
                const notification = document.getElementById('copy-notification');
                notification.textContent = message;
                notification.classList.add('show');
                
                setTimeout(() => {{
                    notification.classList.remove('show');
                }}, 2000);
            }}
            
            // Render chronology entries
            function renderChronology(type = 'all') {{
                const container = document.getElementById('chronology-container');
                container.innerHTML = '';
                
                // Filter by type
                let filteredFacts = factsData;
                
                if (type === 'disputed') {{
                    filteredFacts = factsData.filter(fact => fact.isDisputed);
                }} else if (type === 'undisputed') {{
                    filteredFacts = factsData.filter(fact => !fact.isDisputed);
                }}
                
                // Sort by date
                filteredFacts.sort((a, b) => new Date(a.date) - new Date(b.date));
                
                // Render each entry
                filteredFacts.forEach((fact, index) => {{
                    const entryId = `entry-${{index}}`;
                    
                    // Format date
                    const formatDate = (dateStr) => {{
                        const date = new Date(dateStr);
                        return date.toLocaleDateString('en-US', {{
                            year: 'numeric',
                            month: '2-digit',
                            day: '2-digit'
                        }});
                    }};
                    
                    // Party badge
                    const getPartyBadge = (party) => {{
                        if (party === 'Both') {{
                            return '<span class="badge both-badge">Both Parties</span>';
                        }} else if (party === 'Appellant') {{
                            return '<span class="badge appellant-badge">Appellant</span>';
                        }} else {{
                            return '<span class="badge respondent-badge">Respondent</span>';
                        }}
                    }};
                    
                    // Status badge
                    const statusBadge = fact.isDisputed 
                        ? '<span class="badge disputed-badge">Disputed</span>'
                        : '<span class="badge undisputed-badge">Undisputed</span>';
                    
                    // Proceedings class
                    const proceedingsClass = `proceedings-${{fact.proceedings}}`;
                    
                    // Supporting documents HTML
                    const supportingDocsHtml = fact.supportingDocs.map(doc => `
                        <div class="document-card">
                            <div class="document-header">
                                <div class="document-title">${{doc.id}} - ${{doc.title}}</div>
                            </div>
                            <div class="document-summary">
                                ${{doc.summary}}
                            </div>
                            <div class="document-source">
                                <div class="source-label">Source</div>
                                <div>${{doc.source}}</div>
                                <div class="page-ref">${{doc.pageRef}}</div>
                            </div>
                            <div class="document-actions">
                                <button class="action-btn" onclick="viewDocument('${{doc.id}}')">
                                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                        <polyline points="14,2 14,8 20,8"></polyline>
                                    </svg>
                                    View Document
                                </button>
                                <button class="action-btn" onclick="downloadPDF('${{doc.id}}')">
                                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                                        <polyline points="7 10 12 15 17 10"></polyline>
                                        <line x1="12" y1="15" x2="12" y2="3"></line>
                                    </svg>
                                    Download PDF
                                </button>
                                <button class="action-btn" onclick="copySource('${{doc.id}}', '${{doc.source}}')">
                                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                                    </svg>
                                    Copy Source
                                </button>
                            </div>
                        </div>
                    `).join('');
                    
                    const entryHtml = `
                        <div class="chronology-entry">
                            <div class="chronology-header" onclick="toggleChronologyEntry('${{entryId}}')">
                                <div class="chronology-date">${{formatDate(fact.date)}}</div>
                                <div class="chronology-event">${{fact.point}}</div>
                                <svg id="chevron-${{entryId}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                            </div>
                            <div id="content-${{entryId}}" class="chronology-content">
                                <div class="metadata-row">
                                    <div class="metadata-item">
                                        <span class="sources-count">${{fact.sources}}</span>
                                        <span>Sources</span>
                                    </div>
                                    <div class="metadata-item">
                                        <span>PROCEEDINGS:</span>
                                        <span class="proceedings-tab ${{proceedingsClass}}">${{fact.proceedings}}</span>
                                    </div>
                                    <div class="metadata-item">
                                        <span>ADDRESSED BY:</span>
                                        <span class="addressed-status">${{fact.addressedBy}}</span>
                                    </div>
                                </div>
                                <div class="metadata-row">
                                    <div class="metadata-item">
                                        ${{getPartyBadge(fact.party)}}
                                        ${{statusBadge}}
                                    </div>
                                </div>
                                <div class="supporting-docs">
                                    <h4>Supporting Documents</h4>
                                    ${{supportingDocsHtml}}
                                </div>
                            </div>
                        </div>
                    `;
                    
                    container.innerHTML += entryHtml;
                }});
            }}
            
            // Copy all content function
            function copyAllContent() {{
                let contentToCopy = 'Case Chronology\\n\\n';
                
                const entries = document.querySelectorAll('.chronology-entry');
                entries.forEach(entry => {{
                    const date = entry.querySelector('.chronology-date').textContent;
                    const event = entry.querySelector('.chronology-event').textContent;
                    contentToCopy += `${{date}} | ${{event}}\\n`;
                    
                    const docs = entry.querySelectorAll('.document-card');
                    docs.forEach(doc => {{
                        const title = doc.querySelector('.document-title').textContent;
                        const summary = doc.querySelector('.document-summary').textContent;
                        contentToCopy += `  - ${{title}}: ${{summary}}\\n`;
                    }});
                    contentToCopy += '\\n';
                }});
                
                // Create a temporary textarea to copy the content
                const textarea = document.createElement('textarea');
                textarea.value = contentToCopy;
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);
                
                showNotification('Content copied to clipboard!');
            }}
            
            // Export functions
            function exportAsCsv() {{
                let csvContent = 'Date,Event,Party,Status,Sources,Proceedings,Addressed By\\n';
                
                factsData.forEach(fact => {{
                    const date = fact.date;
                    const event = fact.point.replace(/"/g, '""');
                    const party = fact.party;
                    const status = fact.isDisputed ? 'Disputed' : 'Undisputed';
                    const sources = fact.sources;
                    const proceedings = fact.proceedings;
                    const addressedBy = fact.addressedBy;
                    
                    csvContent += `"${{date}}","${{event}}","${{party}}","${{status}}","${{sources}}","${{proceedings}}","${{addressedBy}}"\\n`;
                }});
                
                const csvFile = "data:text/csv;charset=utf-8," + encodeURIComponent(csvContent);
                const encodedUri = csvFile;
                const link = document.createElement("a");
                link.setAttribute("href", encodedUri);
                link.setAttribute("download", "case_chronology.csv");
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
            
            // Initialize the app
            document.addEventListener('DOMContentLoaded', function() {{
                // Show facts section
                document.getElementById('facts').classList.add('active');
                renderChronology('all');
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
