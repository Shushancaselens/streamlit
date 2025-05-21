import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64
import os
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="CaseLens - Legal Document Management",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to get document sets
def get_document_sets():
    return [
        {
            "id": "appeal",
            "name": "Appeal",
            "party": "Mixed",
            "category": "appeal",
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
            "category": "provisional_messier",
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

# Function to get all facts (needed for facts view)
def get_all_facts():
    # This is a placeholder - in a real app this would get actual facts
    return []

# Function to get timeline data (needed for facts view)
def get_timeline_data():
    # This is a placeholder - in a real app this would get actual timeline data
    return []

# Function to get argument data (needed for facts view)
def get_argument_data():
    # This is a placeholder - in a real app this would get actual argument data
    return {"claimantArgs": {}, "respondentArgs": {}, "topics": []}

# Main application
def main():
    # Get data for JavaScript in facts view
    args_data = get_argument_data()
    facts_data = get_all_facts()
    document_sets = st.session_state.document_sets
    timeline_data = get_timeline_data()
    
    # Sidebar navigation
    with st.sidebar:
        # Logo and title with improved design
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 30px; background-color: #f0f5ff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <div style="background-color: #2563eb; width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 8px rgba(37, 99, 235, 0.3);">
                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 15l9-9 9 9m-4.5-4.5l-9 9-9-9"/>
                    <path d="M9 21V9M15 21V9"/>
                </svg>
            </div>
            <div style="margin-left: 15px;">
                <h1 style="margin: 0; font-weight: 700; color: #1E3A8A; font-size: 24px;">CaseLens</h1>
                <p style="margin: 0; color: #4b5563; font-size: 14px;">Legal Document Management</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin-bottom: 20px; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px; color: #1E3A8A;'>Navigation</h3>", unsafe_allow_html=True)
        
        # Button styling
        st.markdown("""
        <style>
        /* Custom styling for the entire app */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        h1, h2, h3 {
            color: #1E3A8A;
            font-weight: 600;
        }
        
        /* Button styling */
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            height: 50px;
            margin-bottom: 12px;
            transition: all 0.3s;
            border: none;
            background-color: #f0f5ff;
            color: #1E3A8A;
            font-weight: 500;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            background-color: #dbeafe;
        }
        
        .stButton > button:active {
            transform: translateY(0px);
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
        
        /* Badge styling */
        .badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 16px;
            font-size: 12px;
            font-weight: 500;
            margin-right: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .appellant-badge {
            background-color: rgba(59, 130, 246, 0.15);
            color: #2563eb;
            border: 1px solid rgba(59, 130, 246, 0.3);
        }
        
        .respondent-badge {
            background-color: rgba(239, 68, 68, 0.15);
            color: #dc2626;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }
        
        .shared-badge {
            background-color: rgba(75, 85, 99, 0.15);
            color: #4b5563;
            border: 1px solid rgba(75, 85, 99, 0.3);
        }
        
        /* Card styling */
        .document-card {
            background-color: white;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            border: 1px solid #e5e7eb;
            transition: all 0.2s;
        }
        
        .document-card:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            border-radius: 8px 8px 0 0;
            padding: 0 20px;
            background-color: #f3f4f6;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #dbeafe !important;
            color: #1E3A8A !important;
            font-weight: 600;
        }
        
        /* Form styling */
        [data-testid="stForm"] {
            background-color: #f9fafb;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #f8fafc;
            border-right: 1px solid #e2e8f0;
        }
        
        /* Dataframe styling */
        .stDataFrame {
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #e5e7eb;
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            font-weight: 600;
            color: #1E3A8A;
            background-color: #f0f5ff;
            border-radius: 6px;
        }
        
        /* Status indicators */
        .status-badge {
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .status-uploaded {
            background-color: rgba(16, 185, 129, 0.1);
            color: #10b981;
            border: 1px solid rgba(16, 185, 129, 0.2);
        }
        
        .status-missing {
            background-color: rgba(239, 68, 68, 0.1);
            color: #ef4444;
            border: 1px solid rgba(239, 68, 68, 0.2);
        }
        
        /* Upload/create button styling */
        .primary-button {
            background-color: #3b82f6 !important;
            color: white !important;
            font-weight: 600 !important;
        }
        
        /* Selected tab indicator */
        .stTabs [aria-selected="true"]::before {
            content: "";
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 3px;
            background-color: #2563eb;
            border-radius: 3px 3px 0 0;
        }
        
        /* File uploader styling */
        [data-testid="stFileUploader"] {
            border: 2px dashed #d1d5db;
            border-radius: 8px;
            padding: 10px;
            background-color: #f9fafb;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #93c5fd;
            background-color: #f0f5ff;
        }
        
        /* Success/error message styling */
        [data-testid="stAlert"] {
            border-radius: 8px;
            border-left-width: 4px;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Navigation buttons
        def set_view(view_name):
            st.session_state.view = view_name
        
        # Upload Documents button first in navigation
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
    # Page header with animation
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 20px; animation: fadeIn 0.8s ease-in-out;">
        <div style="background-color: #2563eb; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"></path>
                <polyline points="17 8 12 3 7 8"></polyline>
                <line x1="12" y1="3" x2="12" y2="15"></line>
            </svg>
        </div>
        <h1 style="margin: 0 0 0 15px; color: #1E3A8A;">Document Management</h1>
    </div>
    
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    .card-hover {
        transition: all 0.3s ease;
    }
    .card-hover:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Statistics cards row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); class="card-hover">
            <h4 style="margin:0; color: #1e40af; font-size: 14px;">Document Sets</h4>
            <h2 style="margin:10px 0 0 0; color: #1e3a8a; font-size: 28px;">{len(st.session_state.document_sets)}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Calculate total documents
        total_docs = sum(len(ds["documents"]) for ds in st.session_state.document_sets)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); class="card-hover">
            <h4 style="margin:0; color: #3730a3; font-size: 14px;">Total Documents</h4>
            <h2 style="margin:10px 0 0 0; color: #312e81; font-size: 28px;">{total_docs}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Calculate total uploads
        total_uploads = len(st.session_state.uploaded_files)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); class="card-hover">
            <h4 style="margin:0; color: #166534; font-size: 14px;">Files Uploaded</h4>
            <h2 style="margin:10px 0 0 0; color: #14532d; font-size: 28px;">{total_uploads}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        # Calculate percentage uploaded
        if total_docs > 0:
            pct_uploaded = min(int((total_uploads / total_docs) * 100), 100)
        else:
            pct_uploaded = 0
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); class="card-hover">
            <h4 style="margin:0; color: #92400e; font-size: 14px;">Completion</h4>
            <h2 style="margin:10px 0 0 0; color: #78350f; font-size: 28px;">{pct_uploaded}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 25px'></div>", unsafe_allow_html=True)
    
    # Create tabs with enhanced styling
    tabs = st.tabs(["📄 Upload Documents", "📁 Manage Document Sets", "🕒 Recent Activity"])
    
    with tabs[0]:
        # Quick action cards
        st.markdown("<h3 style='margin-bottom: 15px; font-size: 18px;'>Quick Actions</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #e5e7eb; transition: all 0.3s; cursor: pointer;" class="card-hover" onclick="Streamlit.setComponentValue({'create_set': true})">
                <div style="display: flex; align-items: center;">
                    <div style="background-color: #dbeafe; width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 5v14M5 12h14"/>
                        </svg>
                    </div>
                    <div style="margin-left: 15px;">
                        <h4 style="margin: 0; font-size: 16px; color: #1e3a8a;">New Document Set</h4>
                        <p style="margin: 5px 0 0 0; font-size: 13px; color: #6b7280;">Create a new collection for documents</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("➕ New Document Set", use_container_width=True, key="create_set_btn"):
                st.session_state.creating_set = True
        
        with col2:
            st.markdown("""
            <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #e5e7eb; transition: all 0.3s; cursor: pointer;" class="card-hover" onclick="Streamlit.setComponentValue({'upload_doc': true})">
                <div style="display: flex; align-items: center;">
                    <div style="background-color: #e0e7ff; width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/>
                            <polyline points="14 2 14 8 20 8"/>
                            <line x1="12" y1="18" x2="12" y2="12"/>
                            <line x1="9" y1="15" x2="15" y2="15"/>
                        </svg>
                    </div>
                    <div style="margin-left: 15px;">
                        <h4 style="margin: 0; font-size: 16px; color: #1e3a8a;">Upload Document</h4>
                        <p style="margin: 5px 0 0 0; font-size: 13px; color: #6b7280;">Add files to an existing set</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("📄 Upload Document", use_container_width=True, key="upload_doc_btn"):
                st.session_state.creating_set = False
        
        st.markdown("<div style='height: 25px'></div>", unsafe_allow_html=True)
        
        # Display appropriate form based on user selection
        if st.session_state.creating_set:
            # Document set creation form with improved styling
            st.markdown("""
            <div style="animation: slideIn 0.5s ease-out;">
                <h3 style="margin-bottom: 15px; font-size: 18px; display: flex; align-items: center;">
                    <span style="background-color: #dbeafe; width: 24px; height: 24px; border-radius: 6px; display: inline-flex; align-items: center; justify-content: center; margin-right: 10px;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 5v14M5 12h14"/>
                        </svg>
                    </span>
                    Create New Document Set
                </h3>
            </div>
            """, unsafe_allow_html=True)
            
            with st.form("new_set_form"):
                # Enhanced set name field
                st.markdown("<p style='margin-bottom: 5px; font-size: 14px; font-weight: 500;'>Document Set Name</p>", unsafe_allow_html=True)
                set_name = st.text_input("", placeholder="e.g., Witness Statements, Expert Reports", label_visibility="collapsed")
                
                # Party selection with better styling
                st.markdown("<p style='margin: 15px 0 5px 0; font-size: 14px; font-weight: 500;'>Party</p>", unsafe_allow_html=True)
                party_options = ["Appellant", "Respondent", "Mixed", "Shared"]
                set_party = st.selectbox("", party_options, label_visibility="collapsed")
                
                # Submit button with icon and better style
                col1, col2 = st.columns([3, 1])
                with col1:
                    create_btn = st.form_submit_button("Create Document Set", use_container_width=True)
                
                if create_btn:
                    if not set_name:
                        st.error("Please provide a name for this document set")
                    else:
                        # Add new set (category is auto-generated)
                        set_id = add_document_set(set_name, set_party)
                        st.session_state.selected_set = set_id
                        st.session_state.creating_set = False
                        st.success(f"✅ Created new document set: {set_name}")
                        st.rerun()
        else:
            # Document upload form with improved styling
            st.markdown("""
            <div style="animation: slideIn 0.5s ease-out;">
                <h3 style="margin-bottom: 15px; font-size: 18px; display: flex; align-items: center;">
                    <span style="background-color: #e0e7ff; width: 24px; height: 24px; border-radius: 6px; display: inline-flex; align-items: center; justify-content: center; margin-right: 10px;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/>
                            <polyline points="14 2 14 8 20 8"/>
                        </svg>
                    </span>
                    Upload Document
                </h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Document set selection with improved UI
            if not st.session_state.document_sets:
                st.warning("No document sets exist yet. Please create your first document set.")
            else:
                # Show document sets as visual cards with selection
                st.markdown("<p style='margin-bottom: 12px; font-size: 14px; font-weight: 500;'>Select Document Set</p>", unsafe_allow_html=True)
                
                # Create a grid of set cards
                cols = st.columns(2)
                for i, doc_set in enumerate(st.session_state.document_sets):
                    col_idx = i % 2
                    
                    # Determine badge styling based on party
                    if doc_set["party"] == "Appellant":
                        badge_color = "appellant-badge"
                        bg_color = "rgba(59, 130, 246, 0.1)"
                    elif doc_set["party"] == "Respondent":
                        badge_color = "respondent-badge"
                        bg_color = "rgba(239, 68, 68, 0.1)"
                    else:
                        badge_color = "shared-badge"
                        bg_color = "rgba(75, 85, 99, 0.1)"
                    
                    # Check if this set is selected
                    is_selected = st.session_state.selected_set == doc_set["id"]
                    border_style = "2px solid #2563eb" if is_selected else "1px solid #e5e7eb"
                    
                    # Render the card
                    with cols[col_idx]:
                        card_html = f"""
                        <div style="background-color: white; border-radius: 8px; padding: 15px; margin-bottom: 12px; 
                                    box-shadow: 0 2px 6px rgba(0,0,0,0.05); border: {border_style}; 
                                    cursor: pointer; transition: all 0.2s; position: relative;"
                             class="card-hover" id="set-card-{doc_set['id']}">
                            <div style="display: flex; justify-content: space-between; align-items: start;">
                                <div>
                                    <h4 style="margin: 0; font-size: 16px; color: #1e3a8a;">{doc_set['name']}</h4>
                                    <div style="margin-top: 8px;">
                                        <span class="badge {badge_color}">{doc_set['party']}</span>
                                        <span class="badge shared-badge">{len(doc_set['documents'])} documents</span>
                                    </div>
                                </div>
                                <div style="background-color: {bg_color}; width: 32px; height: 32px; border-radius: 6px; 
                                            display: flex; align-items: center; justify-content: center;">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" 
                                         fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z"/>
                                    </svg>
                                </div>
                            </div>
                        </div>
                        """
                        
                        st.markdown(card_html, unsafe_allow_html=True)
                        
                        # Add a button to select this set
                        if st.button(f"Select", key=f"select_{doc_set['id']}", use_container_width=True):
                            st.session_state.selected_set = doc_set["id"]
                            st.rerun()
                
                # Show upload form if a set is selected
                if st.session_state.selected_set:
                    selected_set = next((ds for ds in st.session_state.document_sets if ds["id"] == st.session_state.selected_set), None)
                    
                    if selected_set:
                        st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)
                        
                        # Show selected set info
                        st.markdown(f"""
                        <div style="background-color: #f3f4f6; padding: 15px; border-radius: 8px; margin-bottom: 20px; border-left: 3px solid #2563eb;">
                            <p style="margin: 0; font-size: 13px; color: #4b5563;">Selected Document Set</p>
                            <p style="margin: 0; font-weight: 600; color: #1e3a8a; font-size: 16px;">{selected_set['name']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Enhanced upload form
                        with st.form("upload_form", clear_on_submit=True):
                            # Document name field
                            st.markdown("<p style='margin-bottom: 5px; font-size: 14px; font-weight: 500;'>Document Name</p>", unsafe_allow_html=True)
                            doc_name = st.text_input("", placeholder="Enter document name or title", label_visibility="collapsed")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                # Party field
                                st.markdown("<p style='margin: 15px 0 5px 0; font-size: 14px; font-weight: 500;'>Party</p>", unsafe_allow_html=True)
                                party_options = ["Appellant", "Respondent", "Shared"]
                                default_party = selected_set["party"] if selected_set["party"] != "Mixed" else None
                                default_index = party_options.index(default_party) if default_party in party_options else 0
                                doc_party = st.selectbox("", party_options, index=default_index, label_visibility="collapsed")
                            
                            with col2:
                                # Document type selection
                                st.markdown("<p style='margin: 15px 0 5px 0; font-size: 14px; font-weight: 500;'>Document Type</p>", unsafe_allow_html=True)
                                doc_type_options = ["Pleading", "Exhibit", "Witness Statement", "Expert Report", "Legal Authority", "Correspondence", "Other"]
                                doc_type = st.selectbox("", doc_type_options, label_visibility="collapsed")
                            
                            # Enhanced file uploader
                            st.markdown("<p style='margin: 15px 0 5px 0; font-size: 14px; font-weight: 500;'>Upload File</p>", unsafe_allow_html=True)
                            
                            # Custom file uploader styling
                            st.markdown("""
                            <style>
                            [data-testid="stFileUploader"] {
                                border: 2px dashed #d1d5db;
                                border-radius: 10px;
                                padding: 20px 20px 25px 20px;
                                background-color: #f9fafb;
                                text-align: center;
                            }
                            [data-testid="stFileUploader"]:hover {
                                border-color: #93c5fd;
                                background-color: #f0f5ff;
                            }
                            [data-testid="stFileUploader"] p {
                                color: #6b7280;
                            }
                            </style>
                            """, unsafe_allow_html=True)
                            
                            uploaded_file = st.file_uploader(
                                "Drag & drop files here or click to browse",
                                type=["pdf", "docx", "txt", "jpg", "png", "xlsx", "csv"],
                                help="Supported formats: PDF, Word, Text, Images, Excel, and CSV"
                            )
                            
                            # Submit button with better styling
                            st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)
                            submit_btn = st.form_submit_button("Upload Document", use_container_width=True)
                            
                            if submit_btn:
                                if not doc_name:
                                    st.error("Please provide a document name")
                                elif not uploaded_file:
                                    st.error("Please select a file to upload")
                                else:
                                    # Add document to set
                                    doc_id = add_document_to_set(doc_name, doc_party, st.session_state.selected_set)
                                    if doc_id:
                                        # Save the uploaded file
                                        if save_uploaded_file(uploaded_file, st.session_state.selected_set, doc_id):
                                            # Success message with details
                                            st.success(f"✅ Successfully uploaded: {doc_name}")
                                            
                                            # Show document details in a card
                                            st.markdown(f"""
                                            <div style="background-color: white; border-radius: 8px; padding: 20px; 
                                                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #e5e7eb;
                                                        margin-top: 20px; animation: fadeIn 0.5s ease-in-out;">
                                                <h4 style="margin: 0 0 15px 0; color: #1e3a8a; display: flex; align-items: center;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" 
                                                         fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                                         style="margin-right: 8px;">
                                                        <path d="M22 11.08V12a10 10 0 11-5.93-9.14"/>
                                                        <polyline points="22 4 12 14.01 9 11.01"/>
                                                    </svg>
                                                    Document Successfully Added
                                                </h4>
                                                <div style="display: flex; flex-wrap: wrap;">
                                                    <div style="min-width: 200px; margin-right: 30px; margin-bottom: 15px;">
                                                        <p style="margin: 0; font-size: 13px; color: #6b7280;">Document Name</p>
                                                        <p style="margin: 0; font-weight: 600; color: #1f2937;">{doc_name}</p>
                                                    </div>
                                                    <div style="min-width: 150px; margin-right: 30px; margin-bottom: 15px;">
                                                        <p style="margin: 0; font-size: 13px; color: #6b7280;">Document Type</p>
                                                        <p style="margin: 0; font-weight: 600; color: #1f2937;">{doc_type}</p>
                                                    </div>
                                                    <div style="min-width: 100px; margin-right: 30px; margin-bottom: 15px;">
                                                        <p style="margin: 0; font-size: 13px; color: #6b7280;">Party</p>
                                                        <p style="margin: 0; font-weight: 600; color: #1f2937;">{doc_party}</p>
                                                    </div>
                                                    <div style="min-width: 150px; margin-right: 30px; margin-bottom: 15px;">
                                                        <p style="margin: 0; font-size: 13px; color: #6b7280;">File Type</p>
                                                        <p style="margin: 0; font-weight: 600; color: #1f2937;">{uploaded_file.type}</p>
                                                    </div>
                                                    <div style="min-width: 120px; margin-bottom: 15px;">
                                                        <p style="margin: 0; font-size: 13px; color: #6b7280;">File Size</p>
                                                        <p style="margin: 0; font-weight: 600; color: #1f2937;">{uploaded_file.size/1024:.1f} KB</p>
                                                    </div>
                                                </div>
                                            </div>
                                            """, unsafe_allow_html=True)
                                        else:
                                            st.error("Error saving file")
                                    else:
                                        st.error("Error adding document")
    
    with tabs[1]:
        # Document Set Management Tab with enhanced styling
        if not st.session_state.document_sets:
            # Empty state with illustration
            st.markdown("""
            <div style="text-align: center; padding: 40px 20px; background-color: #f9fafb; border-radius: 10px; margin: 20px 0;">
                <div style="font-size: 48px; margin-bottom: 10px;">📁</div>
                <h3 style="margin: 0 0 10px 0; color: #1e3a8a;">No Document Sets Yet</h3>
                <p style="color: #6b7280; max-width: 400px; margin: 0 auto;">Create your first document set in the Upload Documents tab to get started.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Search and filter options
            col1, col2 = st.columns([3, 1])
            with col1:
                search = st.text_input("🔍 Search document sets", placeholder="Type to filter...", label_visibility="collapsed")
            with col2:
                sort_by = st.selectbox("Sort by", ["Name (A-Z)", "Most Documents", "Party"], label_visibility="collapsed")
            
            # Filter document sets based on search
            filtered_sets = st.session_state.document_sets
            if search:
                filtered_sets = [ds for ds in st.session_state.document_sets 
                                if search.lower() in ds['name'].lower() or 
                                   search.lower() in ds['category'].lower()]
            
            # Sort based on selection
            if sort_by == "Name (A-Z)":
                filtered_sets.sort(key=lambda ds: ds['name'])
            elif sort_by == "Most Documents":
                filtered_sets.sort(key=lambda ds: len(ds['documents']), reverse=True)
            elif sort_by == "Party":
                filtered_sets.sort(key=lambda ds: ds['party'])
            
            if not filtered_sets and search:
                st.warning(f"No document sets found matching '{search}'")
            
            # Display document sets in a grid
            col1, col2 = st.columns(2)
            
            for i, doc_set in enumerate(filtered_sets):
                col_idx = i % 2
                
                # Determine styling based on party
                if doc_set["party"] == "Appellant":
                    badge_color = "appellant-badge" 
                    icon_bg = "rgba(59, 130, 246, 0.15)"
                    icon_color = "#2563eb"
                elif doc_set["party"] == "Respondent":
                    badge_color = "respondent-badge"
                    icon_bg = "rgba(239, 68, 68, 0.15)"
                    icon_color = "#dc2626"
                else:
                    badge_color = "shared-badge"
                    icon_bg = "rgba(75, 85, 99, 0.15)"
                    icon_color = "#4b5563"
                
                with cols[i % 2]:
                    # Expandable card for each document set
                    with st.expander(f"{doc_set['name']} ({len(doc_set['documents'])} documents)"):
                        # Set details
                        st.markdown(f"""
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                            <div>
                                <span class="badge {badge_color}">{doc_set["party"]}</span>
                                <span class="badge shared-badge">{doc_set["category"]}</span>
                            </div>
                            <div style="display: flex; gap: 8px;">
                                <button style="background: none; border: none; cursor: pointer; padding: 5px; color: #4b5563; border-radius: 4px;">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"/>
                                        <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"/>
                                    </svg>
                                </button>
                                <button style="background: none; border: none; cursor: pointer; padding: 5px; color: #4b5563; border-radius: 4px;">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M3 6h18"/>
                                        <path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/>
                                    </svg>
                                </button>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Documents in this set
                        if doc_set["documents"]:
                            # Format data for display
                            doc_data = []
                            for doc in doc_set["documents"]:
                                file_key = f"{doc_set['id']}-{doc['id']}"
                                file_status = "✅ Uploaded" if file_key in st.session_state.uploaded_files else "❌ Missing"
                                status_class = "status-uploaded" if file_key in st.session_state.uploaded_files else "status-missing"
                                
                                doc_data.append({
                                    "ID": doc["id"],
                                    "Name": doc["name"],
                                    "Party": doc["party"],
                                    "Status": f'<span class="status-badge {status_class}">{file_status}</span>'
                                })
                            
                            if doc_data:
                                # Convert to dataframe for display
                                df = pd.DataFrame(doc_data)
                                # Convert Status column to HTML
                                df = df.style.format({"Status": lambda x: x})
                                st.write(df.to_html(escape=False), unsafe_allow_html=True)
                                
                                # Action buttons
                                col1, col2 = st.columns(2)
                                with col1:
                                    if st.button(f"Add Document", key=f"add_to_{doc_set['id']}"):
                                        st.session_state.selected_set = doc_set["id"]
                                        st.session_state.creating_set = False
                                        st.session_state.view = "Upload"
                                        st.rerun()
                                with col2:
                                    if st.button(f"Export List", key=f"export_{doc_set['id']}"):
                                        csv = pd.DataFrame(doc_data).to_csv(index=False).encode('utf-8')
                                        st.download_button(
                                            label="Download CSV",
                                            data=csv,
                                            file_name=f"{doc_set['name']}_documents.csv",
                                            mime='text/csv',
                                        )
                        else:
                            st.info("No documents in this set yet.")
    
    with tabs[2]:
        # Recent Uploads Tab with visual timeline
        if not st.session_state.uploaded_files:
            # Empty state with illustration
            st.markdown("""
            <div style="text-align: center; padding: 40px 20px; background-color: #f9fafb; border-radius: 10px; margin: 20px 0;">
                <div style="font-size: 48px; margin-bottom: 10px;">🕒</div>
                <h3 style="margin: 0 0 10px 0; color: #1e3a8a;">No Recent Activity</h3>
                <p style="color: #6b7280; max-width: 400px; margin: 0 auto;">Upload documents to see your recent activity here.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Get recent uploads with timestamp information
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
                            "Size": file_info.get("size", 0),
                            "Time": upload_time
                        })
            
            # Sort by most recent first
            uploads.sort(key=lambda x: x["Time"], reverse=True)
            
            # Display uploads as visual timeline
            st.markdown("<h3 style='margin-bottom: 15px; font-size: 18px;'>Recent Activity</h3>", unsafe_allow_html=True)
            
            for i, upload in enumerate(uploads):
                # Determine file type icon
                file_type = upload["Type"]
                if "pdf" in file_type.lower():
                    icon = """<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><path d="M9 15h6M9 18h6M9 12h2"/></svg>"""
                    bg_color = "rgba(239, 68, 68, 0.1)"
                elif "word" in file_type.lower() or "docx" in file_type.lower():
                    icon = """<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>"""
                    bg_color = "rgba(59, 130, 246, 0.1)"
                elif "image" in file_type.lower() or "jpg" in file_type.lower() or "png" in file_type.lower():
                    icon = """<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>"""
                    bg_color = "rgba(5, 150, 105, 0.1)"
                elif "excel" in file_type.lower() or "xlsx" in file_type.lower() or "csv" in file_type.lower():
                    icon = """<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="16" y2="17"/><line x1="8" y1="9" x2="9" y2="9"/></svg>"""
                    bg_color = "rgba(22, 163, 74, 0.1)"
                else:
                    icon = """<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#6b7280" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>"""
                    bg_color = "rgba(75, 85, 99, 0.1)"
                
                # Format file size
                size_str = f"{upload['Size']/1024:.1f} KB"
                
                # Party badge
                if upload["Party"] == "Appellant":
                    party_badge = "appellant-badge"
                elif upload["Party"] == "Respondent":
                    party_badge = "respondent-badge"
                else:
                    party_badge = "shared-badge"
                
                # Timeline entry
                st.markdown(f"""
                <div style="display: flex; margin-bottom: 20px; animation: slideIn 0.5s ease-out; animation-delay: {i * 0.1}s; opacity: 0; animation-fill-mode: forwards;">
                    <div style="background-color: {bg_color}; width: 40px; height: 40px; border-radius: 8px; 
                                display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                        {icon}
                    </div>
                    <div style="flex-grow: 1; background-color: white; border-radius: 8px; padding: 15px; 
                                box-shadow: 0 2px 4px rgba(0,0,0,0.05); border: 1px solid #e5e7eb;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <h4 style="margin: 0; font-size: 16px; color: #1e3a8a;">{upload['Name']}</h4>
                            <span style="font-size: 12px; color: #6b7280;">{upload['Time']}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-top: 10px;">
                            <div>
                                <span class="badge {party_badge}">{upload['Party']}</span>
                                <span class="badge shared-badge">{upload['Set']}</span>
                            </div>
                            <span style="font-size: 12px; color: #6b7280;">{size_str}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# Function to render the facts page (simplified placeholder)
def render_facts_page(facts_data, document_sets, timeline_data, args_data):
    # Convert data to JSON for JavaScript
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    document_sets_json = json.dumps(document_sets)
    timeline_json = json.dumps(timeline_data)
    
    # Create HTML content similar to your original
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Your CSS here */
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.5;
                color: #333;
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
