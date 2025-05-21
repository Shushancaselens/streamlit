import streamlit as st
import os
import json
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view and uploaded files
if 'view' not in st.session_state:
    st.session_state.view = "Facts"

# Initialize document sets in session state if not already there
if 'document_sets' not in st.session_state:
    st.session_state.document_sets = get_document_sets()  # Using the existing function

# Initialize uploaded files in session state
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = {}

# Add a tracking for selected document set
if 'selected_set' not in st.session_state:
    st.session_state.selected_set = None

# Function to get the existing document sets
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

# Function to add a new document set
def add_document_set(set_name, set_party, set_category):
    # Create a unique ID based on the set name
    set_id = set_name.lower().replace(' ', '_')
    
    # Check if this ID already exists
    existing_ids = [ds["id"] for ds in st.session_state.document_sets]
    if set_id in existing_ids:
        # Add a timestamp to make it unique
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
    
    # Return the ID for convenience
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
            return True
    
    return False

# Function to save uploaded file
def save_uploaded_file(uploaded_file, set_id, doc_id):
    # In a real application, you would save the file to a storage system
    # For this demo, we'll just store it in session state
    
    # Read the file content
    file_content = uploaded_file.read()
    
    # Store in session state (in a real app, you'd save to disk or database)
    file_key = f"{set_id}-{doc_id}"
    st.session_state.uploaded_files[file_key] = {
        "filename": uploaded_file.name,
        "content": file_content,
        "type": uploaded_file.type,
        "size": uploaded_file.size
    }
    
    return True

# Main app with sidebar navigation
def main():
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
        .uploaded-file-card {
            border: 1px solid #e6e6e6;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #f9f9f9;
        }
        .document-set-header {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
            cursor: pointer;
        }
        .document-set-content {
            margin-left: 20px;
            margin-bottom: 20px;
            padding: 10px;
            border-left: 2px solid #e0e0e0;
        }
        .badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
            margin-right: 5px;
        }
        .appellant-badge {
            background-color: rgba(49, 130, 206, 0.1);
            color: #3182ce;
        }
        .respondent-badge {
            background-color: rgba(229, 62, 62, 0.1);
            color: #e53e3e;
        }
        .shared-badge {
            background-color: rgba(128, 128, 128, 0.1);
            color: #666;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Define button click handlers
        def set_view(view_name):
            st.session_state.view = view_name
            
        # Create buttons with names and icons
        st.button("📑 Arguments", key="args_button", on_click=set_view, args=("Arguments",), use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_view, args=("Facts",), use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_view, args=("Exhibits",), use_container_width=True)
        st.button("📤 Upload Documents", key="upload_button", on_click=set_view, args=("Upload",), use_container_width=True)

    # Check which view should be displayed
    if st.session_state.view == "Upload":
        render_upload_page()
    else:
        # In a real application, you would render other pages here
        st.title(f"{st.session_state.view} View")
        st.info(f"This is a placeholder for the {st.session_state.view} view. Please click on 'Upload Documents' in the sidebar to see the upload page.")

# Function to render the upload page
def render_upload_page():
    st.title("📤 Upload Documents")
    
    # Create tabs for different upload functions
    tab1, tab2 = st.tabs(["Upload New Documents", "Manage Document Sets"])
    
    with tab1:
        st.subheader("Upload and Organize Documents")
        
        # Step 1: Select document set or create a new one
        st.markdown("### Step 1: Select Document Set")
        
        # Option to create a new document set
        create_new = st.checkbox("Create a new document set", False)
        
        if create_new:
            # Form to create a new document set
            with st.form("new_set_form"):
                set_name = st.text_input("Set Name", placeholder="e.g., Witness Statements")
                
                # Party selection
                party_options = ["Appellant", "Respondent", "Mixed", "Shared"]
                set_party = st.selectbox("Party", party_options)
                
                # Category input (default to set name if not provided)
                set_category = st.text_input("Category", placeholder="e.g., witness_statements (optional)")
                
                submit_button = st.form_submit_button("Create Set")
                
                if submit_button and set_name:
                    if not set_category:
                        set_category = set_name.lower().replace(' ', '_')
                    
                    # Add the new set
                    set_id = add_document_set(set_name, set_party, set_category)
                    st.session_state.selected_set = set_id
                    st.success(f"Created new document set: {set_name}")
                    st.experimental_rerun()
        else:
            # Select an existing document set
            set_options = ["Select a document set..."] + [ds["name"] for ds in st.session_state.document_sets]
            selected_set_name = st.selectbox("Select Document Set", set_options)
            
            if selected_set_name != "Select a document set...":
                # Find the selected set ID
                for ds in st.session_state.document_sets:
                    if ds["name"] == selected_set_name:
                        st.session_state.selected_set = ds["id"]
                        break
        
        # Only proceed if a set is selected
        if st.session_state.selected_set:
            # Find the selected set
            selected_set = None
            for ds in st.session_state.document_sets:
                if ds["id"] == st.session_state.selected_set:
                    selected_set = ds
                    break
            
            if selected_set:
                st.markdown("---")
                st.markdown(f"### Step 2: Upload Document to '{selected_set['name']}'")
                
                # Show badge for the party
                party_badge_class = "appellant-badge" if selected_set["party"] == "Appellant" else \
                                    "respondent-badge" if selected_set["party"] == "Respondent" else "shared-badge"
                
                st.markdown(f"""
                <div>
                    <span class="badge {party_badge_class}">{selected_set["party"]}</span>
                    <span class="badge shared-badge">{selected_set["category"]}</span>
                </div>
                """, unsafe_allow_html=True)
                
                # Form to upload a new document
                with st.form("upload_form"):
                    # Document name
                    doc_name = st.text_input("Document Name", placeholder="e.g., Expert Report on Damages")
                    
                    # Party selection (default to the set's party if not Mixed)
                    party_options = ["Appellant", "Respondent", "Shared"]
                    default_party = selected_set["party"] if selected_set["party"] != "Mixed" else None
                    default_index = party_options.index(default_party) if default_party in party_options else 0
                    doc_party = st.selectbox("Document Party", party_options, index=default_index)
                    
                    # File upload
                    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt", "jpg", "png"])
                    
                    submit_button = st.form_submit_button("Upload Document")
                    
                    if submit_button and doc_name and uploaded_file:
                        # Add document to the set
                        if add_document_to_set(doc_name, doc_party, st.session_state.selected_set):
                            # Find the document ID that was just created
                            doc_id = None
                            for ds in st.session_state.document_sets:
                                if ds["id"] == st.session_state.selected_set:
                                    doc_id = ds["documents"][-1]["id"]  # Get the last added document's ID
                                    break
                            
                            # Save the uploaded file
                            if doc_id and save_uploaded_file(uploaded_file, st.session_state.selected_set, doc_id):
                                st.success(f"Successfully uploaded: {doc_name}")
                            else:
                                st.error("Error saving the file.")
                        else:
                            st.error("Error adding document to the set.")
    
    with tab2:
        st.subheader("Manage Document Sets")
        
        # Display all document sets with their documents
        for doc_set in st.session_state.document_sets:
            # Create an expander for each document set
            with st.expander(f"{doc_set['name']} ({len(doc_set['documents'])} documents)"):
                # Show set details
                party_badge_class = "appellant-badge" if doc_set["party"] == "Appellant" else \
                                    "respondent-badge" if doc_set["party"] == "Respondent" else "shared-badge"
                
                st.markdown(f"""
                <div style="margin-bottom: 15px;">
                    <span class="badge {party_badge_class}">{doc_set["party"]}</span>
                    <span class="badge shared-badge">{doc_set["category"]}</span>
                    <span class="badge shared-badge">ID: {doc_set["id"]}</span>
                </div>
                """, unsafe_allow_html=True)
                
                # Show documents in this set
                if doc_set["documents"]:
                    # Create a table of documents
                    doc_data = []
                    for doc in doc_set["documents"]:
                        # Check if the file is in our uploaded files
                        file_key = f"{doc_set['id']}-{doc['id']}"
                        file_status = "Uploaded" if file_key in st.session_state.uploaded_files else "Missing"
                        
                        doc_data.append({
                            "ID": doc["id"],
                            "Name": doc["name"],
                            "Party": doc["party"],
                            "Status": file_status
                        })
                    
                    if doc_data:
                        df = pd.DataFrame(doc_data)
                        st.dataframe(df, use_container_width=True)
                    
                    # Allow renaming or deleting documents (in a real app)
                    st.markdown("---")
                    st.info("Document modification features would be implemented here in a production app.")
                else:
                    st.info("No documents in this set yet.")
        
        # Option to delete a document set (in a real app)
        st.markdown("---")
        st.warning("Document set deletion would be implemented here in a production app.")

# Run the main app
if __name__ == "__main__":
    main()
