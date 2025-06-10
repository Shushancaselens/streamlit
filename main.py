import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64
import os
from datetime import datetime

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Sample document sets for demonstrating the document set view
def get_document_sets():
    # Return grouped document sets with individual document subfolders
    return [
        {
            "id": "appeal",
            "name": "Appeal",
            "party": "Mixed",
            "category": "Appeal",
            "isGroup": True,
            "documents": [
                {"id": "1", "name": "1. Statement of Appeal", "party": "Appellant", "category": "Appeal"},
                {"id": "2", "name": "2. Request for a Stay", "party": "Appellant", "category": "Appeal"},
                {"id": "5", "name": "5. Appeal Brief", "party": "Appellant", "category": "Appeal"},
                {"id": "10", "name": "Jurisprudence", "party": "Shared", "category": "Appeal"}
            ]
        },
        {
            "id": "provisional_messier",
            "name": "provisional messier",
            "party": "Respondent",
            "category": "provisional messier",
            "isGroup": True,
            "documents": [
                {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent", "category": "provisional messier"},
                {"id": "4", "name": "4. Answer to PM", "party": "Respondent", "category": "provisional messier"}
            ]
        },
        {
            "id": "admissibility",
            "name": "admissibility",
            "party": "Mixed",
            "category": "admissibility",
            "isGroup": True,
            "documents": [
                {"id": "6", "name": "6. Brief on Admissibility", "party": "Respondent", "category": "admissibility"},
                {"id": "7", "name": "7. Reply to Objection to Admissibility", "party": "Appellant", "category": "admissibility"},
                {"id": "11", "name": "Objection to Admissibility", "party": "Respondent", "category": "admissibility"}
            ]
        },
        {
            "id": "challenge",
            "name": "challenge",
            "party": "Mixed",
            "category": "challenge",
            "isGroup": True,
            "documents": [
                {"id": "8", "name": "8. Challenge", "party": "Appellant", "category": "challenge"},
                {"id": "9", "name": "ChatGPT", "party": "Shared", "category": "challenge"},
                {"id": "12", "name": "Swiss Court", "party": "Shared", "category": "challenge"}
            ]
        }
    ]

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = "Upload"  # Start with Upload view

if 'document_sets' not in st.session_state:
    st.session_state.document_sets = get_document_sets()

if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = {}

if 'selected_set' not in st.session_state:
    st.session_state.selected_set = None

if 'creating_set' not in st.session_state:
    st.session_state.creating_set = False

if 'viewing_set' not in st.session_state:
    st.session_state.viewing_set = None

# Function to add a document set (auto-generates category)
def add_document_set(set_name, set_party):
    # Create a unique ID based on the set name
    set_id = set_name.lower().replace(' ', '_')
    
    # Auto-generate category from set name
    set_category = set_name.lower().replace(' ', '_')
    
    # Check if ID already exists
    existing_ids = [ds["id"] for ds in st.session_state.document_sets]
    if set_id in existing_ids:
        # Add timestamp to make it unique
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        set_id = f"{set_id}_{timestamp}"
    
    # Create the new document set
    new_set = {
        "id": set_id,
        "name": set_name,
        "party": set_party,
        "category": set_category,
        "isGroup": True,
        "documents": []
    }
    
    # Add to session state
    st.session_state.document_sets.append(new_set)
    
    return set_id

# Function to add a document to a set
def add_document_to_set(doc_name, doc_party, set_id):
    # Find the set
    for doc_set in st.session_state.document_sets:
        if doc_set["id"] == set_id:
            # Create a new document ID
            if doc_set["documents"]:
                # Use the next available number
                existing_ids = [int(doc["id"]) for doc in doc_set["documents"] if doc["id"].isdigit()]
                next_id = str(max(existing_ids) + 1) if existing_ids else "1"
            else:
                next_id = "1"
            
            # Create the document
            new_doc = {
                "id": next_id,
                "name": doc_name,
                "party": doc_party,
                "category": doc_set["category"]
            }
            
            # Add to the set
            doc_set["documents"].append(new_doc)
            return next_id
    
    return None

# Function to save uploaded file
def save_uploaded_file(uploaded_file, set_id, doc_id):
    try:
        # Read file content
        file_content = uploaded_file.read()
        
        # Store in session state
        file_key = f"{set_id}-{doc_id}"
        st.session_state.uploaded_files[file_key] = {
            "filename": uploaded_file.name,
            "content": file_content,
            "type": uploaded_file.type,
            "size": uploaded_file.size,
            "upload_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return True
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return False

# Function to get CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Create data structures as JSON for embedded components
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
                            "children": {}
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
            "children": {}
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
                    'argTitle': arg['title'],
                    'source': point.get('source', party)
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

# Get enhanced timeline data with additional events
def get_timeline_data():
    # Create a richer set of timeline events
    timeline_events = [
        {
            "point": "Club founded and officially registered in the Football Federation",
            "date": "1950-01-12",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-1"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Statement of Appeal"
        },
        {
            "point": "First National Championship won",
            "date": "1955-05-20",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-3"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Appeal Brief"
        },
        {
            "point": "Operations ceased between 1975-1976",
            "date": "1975-1976",
            "isDisputed": True,
            "party": "Respondent",
            "exhibits": ["R-1"],
            "argId": "1",
            "argTitle": "Sporting Succession Rebuttal",
            "source": "provisional messier - Answer to PM"
        },
        # More timeline events would be here
    ]
    
    # Sort events chronologically
    timeline_events.sort(key=lambda x: x['date'])
    
    return timeline_events

# Main application
def main():
    # Get data for JavaScript in facts view
    args_data = get_argument_data()
    facts_data = get_all_facts()
    document_sets = st.session_state.document_sets
    timeline_data = get_timeline_data()
    
    # Add Streamlit sidebar with navigation buttons
    with st.sidebar:
        # Add the logo and CaseLens text (original design)
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
        
        # Custom CSS for button styling and UI improvements
        st.markdown("""
        <style>
        /* Button styling - keep original structure but enhance appearance */
        .stButton > button {
            width: 100%;
            border-radius: 6px;
            height: 50px;
            margin-bottom: 10px;
            transition: all 0.3s;
            font-weight: 500;
            border: none;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Badge styling - slightly improved but keeping original look */
        .badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
            margin-right: 5px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        
        .appellant-badge {
            background-color: rgba(49, 130, 206, 0.1);
            color: #3182ce;
            border: 1px solid rgba(49, 130, 206, 0.2);
        }
        
        .respondent-badge {
            background-color: rgba(229, 62, 62, 0.1);
            color: #e53e3e;
            border: 1px solid rgba(229, 62, 62, 0.2);
        }
        
        .shared-badge {
            background-color: rgba(128, 128, 128, 0.1);
            color: #666;
            border: 1px solid rgba(128, 128, 128, 0.2);
        }
        
        /* Improve uploaded file cards */
        .uploaded-file-card {
            border: 1px solid #e6e6e6;
            border-radius: 5px;
            padding: 12px;
            margin-bottom: 12px;
            background-color: #f9f9f9;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        
        /* Improve document set headers */
        .document-set-header {
            background-color: #f0f5ff;
            padding: 12px;
            border-radius: 5px;
            margin-bottom: 12px;
            cursor: pointer;
            border-left: 3px solid #4D68F9;
        }
        
        .document-set-content {
            margin-left: 20px;
            margin-bottom: 20px;
            padding: 12px;
            border-left: 2px solid #e0e7ff;
        }
        
        /* Improve form appearance */
        [data-testid="stForm"] {
            background-color: #f9fafb;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
            margin-bottom: 20px;
        }
        
        /* Better headings */
        h1, h2, h3 {
            color: #111927;
            font-weight: 600;
        }
        
        /* Better file uploader */
        [data-testid="stFileUploader"] {
            border: 1px solid #e5e7eb;
            border-radius: 5px;
            padding: 5px;
        }
        
        /* Improve expander styling */
        .streamlit-expanderHeader {
            font-weight: 500;
            color: #111927;
            background-color: #f8fafc;
            border-radius: 4px;
        }
        
        /* Better tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 4px 4px 0 0;
            padding: 0px 16px;
            background-color: #f3f4f6;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: white !important;
            border-bottom: 2px solid #4D68F9 !important;
        }
        
        /* Status indicators */
        .status-badge {
            padding: 3px 6px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
        }
        
        .status-success {
            background-color: rgba(16, 185, 129, 0.1);
            color: #10b981;
        }
        
        .status-warning {
            background-color: rgba(245, 158, 11, 0.1);
            color: #f59e0b;
        }
        
        .status-error {
            background-color: rgba(239, 68, 68, 0.1);
            color: #ef4444;
        }
        
        /* Quick upload improvements */
        .quick-upload-area {
            border: 2px dashed #cbd5e1;
            border-radius: 8px;
            padding: 30px;
            text-align: center;
            background-color: #f8fafc;
            margin-bottom: 20px;
        }
        
        .quick-upload-area:hover {
            border-color: #4D68F9;
            background-color: #f0f5ff;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Button click handler
        def set_view(view_name):
            st.session_state.view = view_name
        
        # Original order of buttons with Upload Documents first
        st.button("📤 Upload Documents", key="upload_button", on_click=set_view, args=("Upload",), use_container_width=True)
        st.button("📑 Arguments", key="args_button", on_click=set_view, args=("Arguments",), use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_view, args=("Facts",), use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_view, args=("Exhibits",), use_container_width=True)
    
    # Render the appropriate view based on session state
    if st.session_state.view == "Upload":
        render_upload_page()
    elif st.session_state.view == "Facts":
        render_facts_page(facts_data, document_sets, timeline_data, args_data)
    else:
        # Placeholder for other views
        st.title(f"{st.session_state.view} View")
        st.info(f"This is a placeholder for the {st.session_state.view} view.")

# Function to render the upload page with UX improvements
def render_upload_page():
    st.title("Document Management")
    
    # Add quick upload at the top for better UX
    st.markdown("### 🚀 Quick Upload")
    st.markdown("Drop files here to automatically organize them, or use the options below for more control.")
    
    # Quick upload area
    quick_upload = st.file_uploader(
        "Drag and drop files here for quick upload",
        type=["pdf", "docx", "txt", "jpg", "png", "xlsx", "csv"],
        accept_multiple_files=True,
        help="Files will be automatically categorized. You can organize them later.",
        key="quick_upload"
    )
    
    if quick_upload:
        if st.button("🔄 Process Files Automatically", type="primary", use_container_width=True):
            for uploaded_file in quick_upload:
                # Auto-create a document set based on file type if none exists
                filename = uploaded_file.name.lower()
                
                # Auto-categorize
                if any(word in filename for word in ["appeal", "motion", "brief"]):
                    category = "Appeals"
                elif any(word in filename for word in ["evidence", "exhibit"]):
                    category = "Evidence"
                elif any(word in filename for word in ["contract", "agreement"]):
                    category = "Contracts"
                else:
                    category = "General Documents"
                
                # Check if category set exists, if not create it
                existing_set = next((ds for ds in st.session_state.document_sets if ds["name"] == category), None)
                if not existing_set:
                    set_id = add_document_set(category, "Mixed")
                else:
                    set_id = existing_set["id"]
                
                # Add document to set
                doc_id = add_document_to_set(uploaded_file.name, "Shared", set_id)
                if doc_id:
                    save_uploaded_file(uploaded_file, set_id, doc_id)
            
            st.success(f"Successfully processed {len(quick_upload)} files!")
            st.balloons()
    
    st.markdown("---")
    
    # Create tabs for upload functionality
    tab1, tab2, tab3 = st.tabs(["📄 Organized Upload", "📁 Manage Document Sets", "🕒 Recent Uploads"])
    
    with tab1:
        # Upload interface with much better UX
        st.subheader("Organized Upload")
        st.markdown("Choose a document category below and upload your files directly.")
        
        # Show existing document sets with inline upload
        if st.session_state.document_sets:
            for i, doc_set in enumerate(st.session_state.document_sets):
                party_badge_class = "appellant-badge" if doc_set["party"] == "Appellant" else \
                                    "respondent-badge" if doc_set["party"] == "Respondent" else "shared-badge"
                
                # Use expander for each document set - much cleaner UX
                with st.expander(f"📁 {doc_set['name']} ({len(doc_set['documents'])} documents)", expanded=False):
                    
                    # Show set info
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.markdown(f"""
                        <div style="margin-bottom: 15px;">
                            <span class="badge {party_badge_class}">{doc_set["party"]}</span>
                            <span class="badge shared-badge">{doc_set["category"]}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Inline upload form - this is the key improvement!
                    with st.form(f"upload_form_{doc_set['id']}"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            doc_name = st.text_input("Document Name", 
                                                   placeholder="Enter document name", 
                                                   key=f"name_{doc_set['id']}")
                        
                        with col2:
                            # Smart default party selection
                            party_options = ["Appellant", "Respondent", "Shared"]
                            default_party = doc_set["party"] if doc_set["party"] != "Mixed" else "Shared"
                            default_index = party_options.index(default_party) if default_party in party_options else 0
                            doc_party = st.selectbox("Party", party_options, 
                                                   index=default_index, 
                                                   key=f"party_{doc_set['id']}")
                        
                        # File uploader
                        uploaded_file = st.file_uploader(
                            "Choose file to upload",
                            type=["pdf", "docx", "txt", "jpg", "png", "xlsx", "csv"],
                            key=f"file_{doc_set['id']}"
                        )
                        
                        # Upload button
                        submit_btn = st.form_submit_button(
                            f"📤 Upload to {doc_set['name']}", 
                            use_container_width=True, 
                            type="primary"
                        )
                        
                        if submit_btn:
                            if not doc_name:
                                st.error("Please enter a document name")
                            elif not uploaded_file:
                                st.error("Please select a file to upload")
                            else:
                                # Process upload
                                doc_id = add_document_to_set(doc_name, doc_party, doc_set['id'])
                                if doc_id:
                                    if save_uploaded_file(uploaded_file, doc_set['id'], doc_id):
                                        st.success(f"✅ Successfully uploaded '{doc_name}' to {doc_set['name']}")
                                        st.balloons()
                                        st.rerun()
                                    else:
                                        st.error("❌ Failed to save file")
                                else:
                                    st.error("❌ Failed to add document to set")
        else:
            st.info("No document sets exist yet. Create your first one below!")
        
        # Create new document set section - simplified
        st.markdown("---")
        st.markdown("### ➕ Create New Document Category")
        
        with st.form("new_set_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            
            with col1:
                set_name = st.text_input("Category Name", 
                                       placeholder="e.g., Evidence, Contracts, Witness Statements")
            
            with col2:
                party_options = ["Mixed", "Appellant", "Respondent", "Shared"]
                set_party = st.selectbox("Default Party", party_options, 
                                       help="Documents in this category will default to this party")
            
            create_btn = st.form_submit_button("Create Document Category", 
                                             use_container_width=True, 
                                             type="secondary")
            
            if create_btn:
                if not set_name:
                    st.error("Please enter a category name")
                else:
                    set_id = add_document_set(set_name, set_party)
                    st.success(f"✅ Created new category: {set_name}")
                    st.rerun()
    
    with tab2:
        # Document set management with improvements
        st.subheader("Manage Document Sets")
        
        if not st.session_state.document_sets:
            # Empty state message
            st.markdown("""
            <div style="text-align: center; padding: 30px; background-color: #f8fafc; border-radius: 6px; border: 1px dashed #cbd5e1;">
                <p style="margin: 0; color: #64748b; font-size: 16px;">No document sets exist yet</p>
                <p style="margin: 5px 0 0 0; color: #94a3b8;">Create your first document set above</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Search for document sets
            search_term = st.text_input("🔍 Search document sets", placeholder="Type to filter document sets...", 
                                     help="Filter document sets by name or category")
            
            # Filter document sets if search is provided
            filtered_sets = st.session_state.document_sets
            if search_term:
                filtered_sets = [ds for ds in st.session_state.document_sets 
                                if search_term.lower() in ds['name'].lower() or 
                                   search_term.lower() in ds['category'].lower()]
                
                if not filtered_sets:
                    st.warning(f"No document sets found matching '{search_term}'")
            
            # Display all document sets
            for doc_set in filtered_sets:
                # Create an expander for each document set
                with st.expander(f"{doc_set['name']} ({len(doc_set['documents'])} documents)"):
                    # Show set details
                    party_badge_class = "appellant-badge" if doc_set["party"] == "Appellant" else \
                                       "respondent-badge" if doc_set["party"] == "Respondent" else "shared-badge"
                    
                    st.markdown(f"""
                    <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
                        <div>
                            <span class="badge {party_badge_class}">{doc_set["party"]}</span>
                            <span class="badge shared-badge">{doc_set["category"]}</span>
                        </div>
                        <div>
                            <span style="color: #64748b; font-size: 13px;">ID: {doc_set["id"]}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Show documents in this set
                    if doc_set["documents"]:
                        # Create a table of documents
                        doc_data = []
                        for doc in doc_set["documents"]:
                            # Check if the file is in our uploaded files
                            file_key = f"{doc_set['id']}-{doc['id']}"
                            file_status = "✅ Uploaded" if file_key in st.session_state.uploaded_files else "❌ Missing"
                            
                            # Get file size if available
                            file_size = ""
                            if file_key in st.session_state.uploaded_files:
                                file_size = f"{st.session_state.uploaded_files[file_key]['size']/1024:.1f} KB"
                            
                            doc_data.append({
                                "ID": doc["id"],
                                "Name": doc["name"],
                                "Party": doc["party"],
                                "Status": file_status,
                                "Size": file_size
                            })
                        
                        if doc_data:
                            # Use native Streamlit dataframe
                            df = pd.DataFrame(doc_data)
                            st.dataframe(df, use_container_width=True, height=None)
                            
                            # Action buttons
                            col1, col2, col3 = st.columns(3)
                            
                            with col1:
                                # Button to add documents to this set
                                if st.button(f"➕ Add Document", key=f"add_to_{doc_set['id']}"):
                                    st.session_state.selected_set = doc_set["id"]
                                    st.session_state.creating_set = False
                                    st.rerun()
                            
                            with col2:
                                # Export to CSV button
                                csv = df.to_csv(index=False).encode('utf-8')
                                st.download_button(
                                    label="📥 Export CSV",
                                    data=csv,
                                    file_name=f"{doc_set['name']}_documents.csv",
                                    mime='text/csv',
                                    key=f"export_{doc_set['id']}"
                                )
                            
                            with col3:
                                # View details button
                                if st.button(f"🔍 View Details", key=f"view_{doc_set['id']}"):
                                    if st.session_state.viewing_set == doc_set["id"]:
                                        st.session_state.viewing_set = None  # Toggle off
                                    else:
                                        st.session_state.viewing_set = doc_set["id"]  # Toggle on
                            
                            # If viewing this set, show additional details
                            if st.session_state.get('viewing_set') == doc_set["id"]:
                                st.markdown("""
                                <div style="background-color: #f8fafc; padding: 15px; border-radius: 6px; margin-top: 15px; border: 1px solid #e2e8f0;">
                                    <h4 style="margin-top: 0; color: #0f172a;">Document Set Details</h4>
                                """, unsafe_allow_html=True)
                                
                                # Show document stats
                                total_docs = len(doc_set["documents"])
                                uploaded_docs = sum(1 for doc in doc_set["documents"] 
                                                   if f"{doc_set['id']}-{doc['id']}" in st.session_state.uploaded_files)
                                
                                col1, col2, col3 = st.columns(3)
                                col1.metric("Total Documents", total_docs)
                                col2.metric("Uploaded", uploaded_docs)
                                col3.metric("Completion", f"{int(uploaded_docs/total_docs*100)}%" if total_docs > 0 else "0%")
                                
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        # Empty state for documents
                        st.markdown("""
                        <div style="padding: 15px; background-color: #f8fafc; border-radius: 4px; text-align: center;">
                            <p style="margin: 0; color: #64748b;">No documents in this set yet</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Add first document button
                        if st.button(f"Add First Document", key=f"add_first_{doc_set['id']}"):
                            st.session_state.selected_set = doc_set["id"]
                            st.session_state.creating_set = False
                            st.rerun()
    
    with tab3:
        # Recent uploads tab
        st.subheader("Recent Uploads")
        
        if not st.session_state.uploaded_files:
            # Empty state message
            st.markdown("""
            <div style="text-align: center; padding: 30px; background-color: #f8fafc; border-radius: 6px; border: 1px dashed #cbd5e1;">
                <p style="margin: 0; color: #64748b; font-size: 16px;">No documents have been uploaded yet</p>
                <p style="margin: 5px 0 0 0; color: #94a3b8;">Upload documents to see them listed here</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Get list of uploaded files
            uploads = []
            for file_key, file_info in st.session_state.uploaded_files.items():
                set_id, doc_id = file_key.split("-")
                
                # Find document set and document
                doc_set = next((ds for ds in st.session_state.document_sets if ds["id"] == set_id), None)
                
                if doc_set:
                    doc = next((d for d in doc_set["documents"] if d["id"] == doc_id), None)
                    
                    if doc:
                        # Format upload time nicely
                        upload_time = file_info.get("upload_time", "Just now")
                        
                        uploads.append({
                            "Name": doc["name"],
                            "Set": doc_set["name"],
                            "Party": doc["party"],
                            "Type": file_info.get("type", "Unknown"),
                            "Size": f"{file_info.get('size', 0)/1024:.1f} KB",
                            "Time": upload_time
                        })
            
            # Sort uploads by time (most recent first)
            uploads = sorted(uploads, key=lambda x: x.get("Time", ""), reverse=True)
            
            # Display uploads in a table
            if uploads:
                # Create styled upload cards
                for upload in uploads:
                    # Determine party badge class
                    party_badge_class = "appellant-badge" if upload["Party"] == "Appellant" else \
                                       "respondent-badge" if upload["Party"] == "Respondent" else "shared-badge"
                    
                    # Create card for each upload
                    st.markdown(f"""
                    <div style="background-color: white; border-radius: 6px; padding: 16px; margin-bottom: 16px; border: 1px solid #e2e8f0; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <div style="font-weight: 500; color: #111927;">{upload["Name"]}</div>
                            <div style="font-size: 12px; color: #64748b;">{upload["Time"]}</div>
                        </div>
                        <div style="display: flex; flex-wrap: wrap; gap: 15px;">
                            <div>
                                <span style="font-size: 12px; color: #64748b;">Set:</span>
                                <span style="font-size: 13px; font-weight: 500; color: #111927;"> {upload["Set"]}</span>
                            </div>
                            <div>
                                <span style="font-size: 12px; color: #64748b;">Party:</span>
                                <span class="badge {party_badge_class}">{upload["Party"]}</span>
                            </div>
                            <div>
                                <span style="font-size: 12px; color: #64748b;">Type:</span>
                                <span style="font-size: 13px; font-weight: 500; color: #111927;"> {upload["Type"]}</span>
                            </div>
                            <div>
                                <span style="font-size: 12px; color: #64748b;">Size:</span>
                                <span style="font-size: 13px; font-weight: 500; color: #111927;"> {upload["Size"]}</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No upload information available.")

# Function to render the facts page
def render_facts_page(facts_data, document_sets, timeline_data, args_data):
    # Convert data to JSON for JavaScript
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    document_sets_json = json.dumps(document_sets)
    timeline_json = json.dumps(timeline_data)
    
    # Create HTML content for the Facts view
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
            
            .shared-badge {{
                background-color: rgba(128, 128, 128, 0.1);
                color: #666;
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
            
            /* View toggle */
            .view-toggle {{
                display: flex;
                justify-content: flex-end;
                margin-bottom: 16px;
            }}
            
            .view-toggle button {{
                padding: 8px 16px;
                border: 1px solid #e2e8f0;
                background-color: #f7fafc;
                cursor: pointer;
            }}
            
            .view-toggle button.active {{
                background-color: #4299e1;
                color: white;
                border-color: #4299e1;
            }}
            
            .view-toggle button:first-child {{
                border-radius: 4px 0 0 4px;
            }}
            
            .view-toggle button:not(:first-child):not(:last-child) {{
                border-radius: 0;
                border-left: none;
                border-right: none;
            }}
            
            .view-toggle button:last-child {{
                border-radius: 0 4px 4px 0;
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
            </div>
            
            <!-- Facts Section -->
            <div id="facts" class="content-section active">
                <div class="section-title">Case Facts</div>
                
                <div class="view-toggle">
                    <button id="table-view-btn" class="active" onclick="switchView('table')">Table View</button>
                    <button id="docset-view-btn" onclick="switchView('docset')">Document Categories</button>
                    <button id="timeline-view-btn" onclick="switchView('timeline')">Timeline View</button>
                </div>
                
                <div class="facts-header">
                    <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                    <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                    <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                </div>
                
                <!-- Table View -->
                <div id="table-view-content" class="facts-content">
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
                
                <!-- Other views would go here -->
                <div id="timeline-view-content" class="facts-content" style="display: none;">
                    Timeline content would go here
                </div>
                
                <div id="docset-view-content" class="facts-content" style="display: none;">
                    Document categories content would go here
                </div>
            </div>
        </div>
        
        <script>
            // Initialize data
            const factsData = {facts_json};
            const documentSets = {document_sets_json};
            const timelineData = {timeline_json};
            
            // Switch view between table, timeline, and document sets
            function switchView(viewType) {{
                const tableBtn = document.getElementById('table-view-btn');
                const timelineBtn = document.getElementById('timeline-view-btn');
                const docsetBtn = document.getElementById('docset-view-btn');
                
                const tableContent = document.getElementById('table-view-content');
                const timelineContent = document.getElementById('timeline-view-content');
                const docsetContent = document.getElementById('docset-view-content');
                
                // Remove active class from all buttons
                tableBtn.classList.remove('active');
                timelineBtn.classList.remove('active');
                docsetBtn.classList.remove('active');
                
                // Hide all content
                tableContent.style.display = 'none';
                timelineContent.style.display = 'none';
                docsetContent.style.display = 'none';
                
                // Activate the selected view
                if (viewType === 'table') {{
                    tableBtn.classList.add('active');
                    tableContent.style.display = 'block';
                    renderFacts();
                }} else if (viewType === 'timeline') {{
                    timelineBtn.classList.add('active');
                    timelineContent.style.display = 'block';
                    // Timeline rendering would go here
                }} else if (viewType === 'docset') {{
                    docsetBtn.classList.add('active');
                    docsetContent.style.display = 'block';
                    // Document set rendering would go here
                }}
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
                }} else if (tabType === 'disputed') {{
                    disputedBtn.classList.add('active');
                }} else {{
                    undisputedBtn.classList.add('active');
                }}
                
                // Update active view with filtered facts
                renderFacts(tabType);
            }}
            
            // Copy content function
            function copyAllContent() {{
                const notification = document.getElementById('copy-notification');
                notification.classList.add('show');
                
                setTimeout(() => {{
                    notification.classList.remove('show');
                }}, 2000);
            }}
            
            // Sort table function
            function sortTable(tableId, columnIndex) {{
                // Sorting logic would go here
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
                
                // Render rows
                filteredFacts.forEach(fact => {{
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
                    partyCell.innerHTML = `<span class="badge ${{fact.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}">${{fact.party}}</span>`;
                    row.appendChild(partyCell);
                    
                    // Status column
                    const statusCell = document.createElement('td');
                    statusCell.innerHTML = fact.isDisputed ? 
                        '<span class="badge disputed-badge">Disputed</span>' : 
                        'Undisputed';
                    row.appendChild(statusCell);
                    
                    // Related argument
                    const argCell = document.createElement('td');
                    argCell.textContent = `${{fact.argId}}. ${{fact.argTitle}}`;
                    row.appendChild(argCell);
                    
                    // Evidence column
                    const evidenceCell = document.createElement('td');
                    if (fact.exhibits && fact.exhibits.length > 0) {{
                        evidenceCell.innerHTML = fact.exhibits.map(ex => 
                            `<span class="badge exhibit-badge">${{ex}}</span>`
                        ).join(' ');
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
    st.title("Case Facts")
    components.html(html_content, height=800, scrolling=True)

# Run the main app
if __name__ == "__main__":
    main()
