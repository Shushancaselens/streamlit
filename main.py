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
        # Logo and title
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
              <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#whatsapp-mask)">
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <h1 style="margin-left: 10px; font-weight: 600; color: #4D68F9;">CaseLens</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
        
        # Button styling
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
    st.title("Document Management")
    
    # Single-screen upload interface
    left_col, right_col = st.columns([1, 1])
    
    with left_col:
        # Document set creation on the left
        st.subheader("1. Create Document Set")
        
        # Simple form for creating a document set
        with st.form("new_set_form"):
            set_name = st.text_input("Set Name", placeholder="e.g., Witness Statements")
            
            # Party selection
            party_options = ["Appellant", "Respondent", "Mixed", "Shared"]
            set_party = st.selectbox("Party", party_options)
            
            # Submit button
            if st.form_submit_button("Create Set", use_container_width=True):
                if not set_name:
                    st.error("Please provide a set name")
                else:
                    # Add new set (category is auto-generated)
                    set_id = add_document_set(set_name, set_party)
                    st.session_state.selected_set = set_id
                    st.success(f"✓ Created: {set_name}")
        
        # Document sets listing on the left (below creation form)
        st.subheader("Your Document Sets")
        
        if not st.session_state.document_sets:
            st.info("No document sets yet. Create your first set above.")
        else:
            # Display document sets as clickable buttons
            for idx, doc_set in enumerate(st.session_state.document_sets):
                # Create a button for each set
                if st.button(f"{doc_set['name']} ({len(doc_set['documents'])} docs)", key=f"set_{idx}"):
                    st.session_state.selected_set = doc_set["id"]
                    st.rerun()
    
    with right_col:
        # Document upload on the right
        st.subheader("2. Upload Document")
        
        # Simple message at the top
        if not st.session_state.document_sets:
            st.warning("Create a document set first, then upload documents")
        else:
            # Get selected set
            selected_set = None
            if st.session_state.selected_set:
                selected_set = next((ds for ds in st.session_state.document_sets if ds["id"] == st.session_state.selected_set), None)
            
            # Show selected set or dropdown
            if selected_set:
                st.info(f"Uploading to: **{selected_set['name']}** ({selected_set['party']})")
            else:
                # Simple dropdown to select a set
                set_options = [ds["name"] for ds in st.session_state.document_sets]
                if set_options:
                    selected_set_name = st.selectbox("Select Document Set", set_options)
                    selected_set = next((ds for ds in st.session_state.document_sets if ds["name"] == selected_set_name), None)
                    if selected_set:
                        st.session_state.selected_set = selected_set["id"]
            
            # If a set is selected, show the upload form
            if selected_set:
                with st.form("upload_form"):
                    # Document name field
                    doc_name = st.text_input("Document Name")
                    
                    # Party selection (default to the set's party if not Mixed)
                    party_options = ["Appellant", "Respondent", "Shared"]
                    default_party = selected_set["party"] if selected_set["party"] != "Mixed" else None
                    default_index = party_options.index(default_party) if default_party in party_options else 0
                    doc_party = st.selectbox("Party", party_options, index=default_index)
                    
                    # File uploader
                    uploaded_file = st.file_uploader("Select File", 
                                                  type=["pdf", "docx", "txt", "jpg", "png", "xlsx", "csv"])
                    
                    # Submit button
                    if st.form_submit_button("Upload Document", use_container_width=True):
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
                                    st.success(f"✓ Uploaded: {doc_name}")
                                else:
                                    st.error("Error saving file")
                            else:
                                st.error("Error adding document")
    
    # Document list at the bottom (full width)
    st.markdown("---")
    st.subheader("Documents")
    
    # Show documents from selected set
    if st.session_state.selected_set:
        selected_set = next((ds for ds in st.session_state.document_sets if ds["id"] == st.session_state.selected_set), None)
        
        if selected_set:
            if not selected_set["documents"]:
                st.info(f"No documents in set: {selected_set['name']}")
            else:
                # Build document data for display
                doc_data = []
                for doc in selected_set["documents"]:
                    # Check if the file is in our uploaded files
                    file_key = f"{selected_set['id']}-{doc['id']}"
                    file_status = "✓ Uploaded" if file_key in st.session_state.uploaded_files else "× Missing"
                    file_size = ""
                    if file_key in st.session_state.uploaded_files:
                        file_size = f"{st.session_state.uploaded_files[file_key]['size']/1024:.1f} KB"
                    
                    doc_data.append({
                        "Name": doc["name"],
                        "Party": doc["party"],
                        "Status": file_status,
                        "Size": file_size
                    })
                
                # Display as a simple table
                if doc_data:
                    st.dataframe(pd.DataFrame(doc_data), use_container_width=True)

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
