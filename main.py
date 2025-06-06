import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64
import os
from datetime import datetime

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Function to get document sets
def get_document_sets():
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

# Get all facts from the data (needed for facts view)
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

# Function to get timeline data (needed for facts view)
def get_timeline_data():
    # Create a set of timeline events
    return [
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
        # More timeline events would be here
    ]

# Function to get argument data (needed for facts view)
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
            "children": {}
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

# Main application
def main():
    # Get data for JavaScript in facts view
    args_data = get_argument_data()
    facts_data = get_all_facts()
    document_sets = st.session_state.document_sets
    timeline_data = get_timeline_data()
    
    # Add Streamlit sidebar with navigation buttons only
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
        
        # Custom CSS for subtle UI improvements while maintaining original structure
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

# Function to render the upload page
def render_upload_page():
    # Page header with subtle improvement
    st.markdown("<h1 style='color: #111927; margin-bottom: 25px;'>Document Management</h1>", unsafe_allow_html=True)
    
    # Create tabs with enhanced styling but same structure
    tab1, tab2, tab3 = st.tabs(["📄 Upload Documents", "📁 Manage Document Sets", "🕒 Recent Uploads"])
    
    with tab1:
        # Upload interface
        st.markdown("<h3 style='color: #111927; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 10px;'>Upload Documents</h3>", unsafe_allow_html=True)
        
        # Action buttons with better appearance but same layout
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ New Document Set", use_container_width=True):
                st.session_state.creating_set = True
        with col2:
            if st.button("📄 Upload Document", use_container_width=True):
                st.session_state.creating_set = False
        
        st.markdown("<div style='margin: 20px 0; border-top: 1px solid #e5e7eb;'></div>", unsafe_allow_html=True)
        
        # Display appropriate form based on user selection
        if st.session_state.creating_set:
            # Document set creation form with subtle enhancements
            st.markdown("<h4 style='color: #111927; margin-bottom: 15px;'>Create Document Set</h4>", unsafe_allow_html=True)
            
            with st.form("new_set_form"):
                # Set name field with better style
                st.markdown("<p style='font-weight: 500; margin-bottom: 5px;'>Set Name</p>", unsafe_allow_html=True)
                set_name = st.text_input("", placeholder="e.g., Witness Statements, Expert Reports", label_visibility="collapsed")
                
                # Party selection with better label
                st.markdown("<p style='font-weight: 500; margin: 15px 0 5px 0;'>Party</p>", unsafe_allow_html=True)
                party_options = ["Appellant", "Respondent", "Mixed", "Shared"]
                set_party = st.selectbox("", party_options, label_visibility="collapsed")
                
                # Submit button with better style
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    create_btn = st.form_submit_button("Create Document Set", use_container_width=True)
                
                if create_btn:
                    if not set_name:
                        st.error("Please provide a name for this document set")
                    else:
                        # Add new set (category is auto-generated)
                        set_id = add_document_set(set_name, set_party)
                        st.session_state.selected_set = set_id
                        st.session_state.creating_set = False
                        
                        # Better success message
                        st.markdown(f"""
                        <div style="background-color: #ecfdf5; border-left: 4px solid #10b981; padding: 15px; border-radius: 4px; margin: 20px 0;">
                            <p style="margin: 0; color: #065f46; font-weight: 500;">✅ Successfully created document set</p>
                            <p style="margin: 5px 0 0 0; color: #047857;">{set_name}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.rerun()
        else:
            # Document upload form with subtle improvements
            st.markdown("<h4 style='color: #111927; margin-bottom: 15px;'>Upload Document</h4>", unsafe_allow_html=True)
            
            # Document set selection with better styling
            if not st.session_state.document_sets:
                st.warning("No document sets exist. Please create a document set first.")
            else:
                st.markdown("<p style='font-weight: 500; margin-bottom: 5px;'>Select Document Set</p>", unsafe_allow_html=True)
                set_options = ["--Select a document set--"] + [ds["name"] for ds in st.session_state.document_sets]
                selected_set_name = st.selectbox("", set_options, label_visibility="collapsed")
                
                if selected_set_name == "--Select a document set--":
                    st.warning("Please select a document set first")
                else:
                    # Find the selected set
                    selected_set = None
                    for ds in st.session_state.document_sets:
                        if ds["name"] == selected_set_name:
                            selected_set = ds
                            st.session_state.selected_set = ds["id"]
                            break
                    
                    # Show selected set info with better style
                    party_badge_class = "appellant-badge" if selected_set["party"] == "Appellant" else \
                                        "respondent-badge" if selected_set["party"] == "Respondent" else "shared-badge"
                    
                    st.markdown(f"""
                    <div style="background-color: #f8fafc; padding: 12px; border-radius: 6px; margin: 15px 0; border-left: 3px solid #4D68F9;">
                        <p style="margin: 0; font-size: 13px; color: #64748b;">Selected Document Set</p>
                        <p style="margin: 5px 0 0 0; font-weight: 600; color: #0f172a;">{selected_set['name']}</p>
                        <div style="margin-top: 8px;">
                            <span class="badge {party_badge_class}">{selected_set["party"]}</span>
                            <span class="badge shared-badge">{len(selected_set["documents"])} documents</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Form for document upload with better styling
                    with st.form("upload_form"):
                        # Document name field with better label
                        st.markdown("<p style='font-weight: 500; margin-bottom: 5px;'>Document Name</p>", unsafe_allow_html=True)
                        doc_name = st.text_input("", placeholder="Enter document name or title", label_visibility="collapsed")
                        
                        # Party selection (default to the set's party if not Mixed)
                        st.markdown("<p style='font-weight: 500; margin: 15px 0 5px 0;'>Party</p>", unsafe_allow_html=True)
                        party_options = ["Appellant", "Respondent", "Shared"]
                        default_party = selected_set["party"] if selected_set["party"] != "Mixed" else None
                        default_index = party_options.index(default_party) if default_party in party_options else 0
                        doc_party = st.selectbox("", party_options, index=default_index, label_visibility="collapsed")
                        
                        # File uploader with better style
                        st.markdown("<p style='font-weight: 500; margin: 15px 0 5px 0;'>Upload File</p>", unsafe_allow_html=True)
                        
                        # Enhanced file uploader with same functionality
                        uploaded_file = st.file_uploader(
                            "Drag files here or click to browse",
                            type=["pdf", "docx", "txt", "jpg", "png", "xlsx", "csv"],
                            help="Supported formats: PDF, Word, Text, Images, Excel and CSV"
                        )
                        
                        # Submit button with better style
                        col1, col2, col3 = st.columns([1, 2, 1])
                        with col2:
                            submit_btn = st.form_submit_button("Upload Document", use_container_width=True)
                        
                        if submit_btn:
                            if not doc_name:
                                st.error("Please provide a document name")
                            elif not uploaded_file:
                                st.error("Please select a file")
                            else:
                                # Add document to set
                                doc_id = add_document_to_set(doc_name, doc_party, st.session_state.selected_set)
                                if doc_id:
                                    # Save the uploaded file
                                    if save_uploaded_file(uploaded_file, st.session_state.selected_set, doc_id):
                                        # Enhanced success message with document details
                                        st.markdown(f"""
                                        <div style="background-color: #ecfdf5; border-left: 4px solid #10b981; padding: 15px; border-radius: 4px; margin: 20px 0;">
                                            <p style="margin: 0; color: #065f46; font-weight: 500;">✅ Document successfully uploaded</p>
                                            <p style="margin: 5px 0 0 0; color: #047857;">{doc_name}</p>
                                        </div>
                                        
                                        <div style="background-color: #f8fafc; padding: 15px; border-radius: 6px; margin-top: 20px; border: 1px solid #e2e8f0;">
                                            <div style="display: flex; flex-wrap: wrap; gap: 20px;">
                                                <div>
                                                    <p style="margin: 0; font-size: 13px; color: #64748b;">Document Name</p>
                                                    <p style="margin: 0; font-weight: 500; color: #0f172a;">{doc_name}</p>
                                                </div>
                                                <div>
                                                    <p style="margin: 0; font-size: 13px; color: #64748b;">Party</p>
                                                    <p style="margin: 0; font-weight: 500; color: #0f172a;">{doc_party}</p>
                                                </div>
                                                <div>
                                                    <p style="margin: 0; font-size: 13px; color: #64748b;">File Type</p>
                                                    <p style="margin: 0; font-weight: 500; color: #0f172a;">{uploaded_file.type}</p>
                                                </div>
                                                <div>
                                                    <p style="margin: 0; font-size: 13px; color: #64748b;">File Size</p>
                                                    <p style="margin: 0; font-weight: 500; color: #0f172a;">{uploaded_file.size/1024:.1f} KB</p>
                                                </div>
                                            </div>
                                        </div>
                                        """, unsafe_allow_html=True)
                                    else:
                                        st.error("Error saving file")
                                else:
                                    st.error("Error adding document")
    
    with tab2:
        # Document set management with subtle enhancements
        st.markdown("<h3 style='color: #111927; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 10px;'>Manage Document Sets</h3>", unsafe_allow_html=True)
        
        if not st.session_state.document_sets:
            # Improved empty state message
            st.markdown("""
            <div style="text-align: center; padding: 30px; background-color: #f8fafc; border-radius: 6px; border: 1px dashed #cbd5e1;">
                <p style="margin: 0; color: #64748b; font-size: 16px;">No document sets exist yet</p>
                <p style="margin: 5px 0 0 0; color: #94a3b8;">Create your first document set in the Upload Documents tab</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Display all document sets with enhanced styling
            for doc_set in st.session_state.document_sets:
                # Create an expander for each document set with better styling
                with st.expander(f"{doc_set['name']} ({len(doc_set['documents'])} documents)"):
                    # Show set details with enhanced appearance
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
                    
                    # Show documents in this set with better styling
                    if doc_set["documents"]:
                        # Create a table of documents with enhanced status indicators
                        doc_data = []
                        for doc in doc_set["documents"]:
                            # Check if the file is in our uploaded files
                            file_key = f"{doc_set['id']}-{doc['id']}"
                            if file_key in st.session_state.uploaded_files:
                                file_status = "✅ Uploaded"
                                status_class = "status-success"
                            else:
                                file_status = "❌ Missing"
                                status_class = "status-error"
                            
                            doc_data.append({
                                "ID": doc["id"],
                                "Name": doc["name"],
                                "Party": doc["party"],
                                "Status": f'<span class="status-badge {status_class}">{file_status}</span>'
                            })
                        
                        if doc_data:
                            # Convert to DataFrame and display with HTML for status badges
                            df = pd.DataFrame(doc_data)
                            # Convert Status column to HTML
                            st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
                            
                            # Add action buttons with better styling
                            col1, col2 = st.columns(2)
                            with col1:
                                if st.button(f"Add Document to Set", key=f"add_to_{doc_set['id']}"):
                                    st.session_state.selected_set = doc_set["id"]
                                    st.session_state.creating_set = False
                                    st.session_state.view = "Upload"
                                    st.rerun()
                            with col2:
                                # Generate CSV download
                                csv = pd.DataFrame({
                                    "ID": [doc["id"] for doc in doc_set["documents"]],
                                    "Name": [doc["name"] for doc in doc_set["documents"]],
                                    "Party": [doc["party"] for doc in doc_set["documents"]]
                                }).to_csv(index=False).encode('utf-8')
                                
                                st.download_button(
                                    label="Export Document List",
                                    data=csv,
                                    file_name=f"{doc_set['name']}_documents.csv",
                                    mime='text/csv',
                                )
                    else:
                        # Better empty state for documents
                        st.markdown("""
                        <div style="padding: 15px; background-color: #f8fafc; border-radius: 4px; text-align: center;">
                            <p style="margin: 0; color: #64748b;">No documents in this set yet</p>
                        </div>
                        """, unsafe_allow_html=True)
    
    with tab3:
        # Recent uploads with better styling
        st.markdown("<h3 style='color: #111927; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 10px;'>Recent Uploads</h3>", unsafe_allow_html=True)
        
        if not st.session_state.uploaded_files:
            # Better empty state
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
            
            # Display uploads in a styled table
            if uploads:
                # Sort by most recent first (assuming upload_time is available)
                uploads = sorted(uploads, key=lambda x: x.get("Time", ""), reverse=True)
                
                # Create styled HTML cards for recent uploads
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

# Function to render the facts page (simplified placeholder)
def render_facts_page(facts_data, document_sets, timeline_data, args_data):
    # Convert data to JSON for JavaScript
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    document_sets_json = json.dumps(document_sets)
    timeline_json = json.dumps(timeline_data)
    
    # Create HTML content similar to original design
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
            
            /* Section title */
            .section-title {{
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1rem;
                padding-bottom: 0.5rem;
                border-bottom: 1px solid #eaeaea;
            }}
            
            /* More styles would go here */
        </style>
    </head>
    <body>
        <div class="container">
            <div id="facts" class="content-section active">
                <div class="section-title">Case Facts</div>
                <div id="facts-content">Facts content would display here</div>
            </div>
        </div>
        
        <script>
            // Initialize data
            const factsData = {facts_json};
            const documentSets = {document_sets_json};
            const timelineData = {timeline_json};
            
            // JavaScript for Facts view would go here
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


