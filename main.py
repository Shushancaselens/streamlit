import streamlit as st
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(page_title="Legal Documents", layout="wide")

# Initialize session state
if 'document_sets' not in st.session_state:
    st.session_state.document_sets = [
        {
            "id": "appeal",
            "name": "Appeal",
            "party": "Mixed",
            "documents": [
                {"id": "1", "name": "Statement of Appeal", "party": "Appellant"},
                {"id": "2", "name": "Request for a Stay", "party": "Appellant"}
            ]
        },
        {
            "id": "admissibility",
            "name": "Admissibility",
            "party": "Mixed",
            "documents": [
                {"id": "1", "name": "Brief on Admissibility", "party": "Respondent"},
                {"id": "2", "name": "Reply to Objection", "party": "Appellant"}
            ]
        }
    ]

if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = {}

# Functions for document management
def add_document_set(name, party):
    set_id = name.lower().replace(' ', '_')
    
    # Check if ID exists
    if any(ds["id"] == set_id for ds in st.session_state.document_sets):
        set_id = f"{set_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    # Create set
    new_set = {
        "id": set_id,
        "name": name,
        "party": party,
        "documents": []
    }
    
    st.session_state.document_sets.append(new_set)
    return set_id

def add_document(set_id, name, party, uploaded_file):
    # Find set
    for doc_set in st.session_state.document_sets:
        if doc_set["id"] == set_id:
            # Get next ID
            next_id = str(len(doc_set["documents"]) + 1)
            
            # Add document
            doc_set["documents"].append({
                "id": next_id,
                "name": name,
                "party": party
            })
            
            # Save file
            if uploaded_file:
                file_key = f"{set_id}-{next_id}"
                file_content = uploaded_file.read()
                st.session_state.uploaded_files[file_key] = {
                    "filename": uploaded_file.name,
                    "content": file_content,
                    "type": uploaded_file.type,
                    "size": uploaded_file.size
                }
            
            return True
    
    return False

# Main app
st.title("📤 Document Management")

# Single page with two columns
col1, col2 = st.columns([1, 2])

# Left column - Create Document Set
with col1:
    st.subheader("1. Create Document Set")
    with st.form("set_form"):
        set_name = st.text_input("Set Name", placeholder="e.g., Witness Statements")
        set_party = st.selectbox("Party", ["Appellant", "Respondent", "Mixed", "Shared"])
        
        create_set = st.form_submit_button("Create Set")
        
        if create_set:
            if not set_name:
                st.error("Please enter a set name")
            else:
                add_document_set(set_name, set_party)
                st.success(f"Created: {set_name}")

# Right column - Upload Document
with col2:
    st.subheader("2. Upload Document")
    
    # Only show if there are document sets
    if not st.session_state.document_sets:
        st.warning("Create a document set first")
    else:
        with st.form("doc_form"):
            # Select set
            set_options = [(ds["id"], f"{ds['name']} ({ds['party']})") for ds in st.session_state.document_sets]
            selected_set_id = st.selectbox("Document Set", 
                                         options=[id for id, _ in set_options],
                                         format_func=lambda x: next((name for id, name in set_options if id == x), ""))
            
            # Document details
            doc_name = st.text_input("Document Name")
            
            # Get default party from set
            selected_set = next((ds for ds in st.session_state.document_sets if ds["id"] == selected_set_id), None)
            default_party = selected_set["party"] if selected_set and selected_set["party"] != "Mixed" else "Appellant"
            doc_party = st.selectbox("Party", ["Appellant", "Respondent", "Shared"], 
                                   index=["Appellant", "Respondent", "Shared"].index(default_party))
            
            # File upload
            uploaded_file = st.file_uploader("Choose File", type=["pdf", "docx", "txt", "jpg", "png"])
            
            # Submit
            upload_doc = st.form_submit_button("Upload Document")
            
            if upload_doc:
                if not doc_name:
                    st.error("Please enter a document name")
                elif not uploaded_file:
                    st.error("Please upload a file")
                else:
                    if add_document(selected_set_id, doc_name, doc_party, uploaded_file):
                        st.success(f"Uploaded: {doc_name}")
                    else:
                        st.error("Error uploading document")

# Show all documents
st.markdown("---")
st.subheader("Document List")

# Create a clean table of all documents
all_docs = []
for doc_set in st.session_state.document_sets:
    for doc in doc_set["documents"]:
        file_key = f"{doc_set['id']}-{doc['id']}"
        status = "✅ Uploaded" if file_key in st.session_state.uploaded_files else "❌ Missing"
        
        all_docs.append({
            "Set": doc_set["name"],
            "Document": doc["name"],
            "Party": doc["party"],
            "Status": status
        })

if all_docs:
    st.dataframe(pd.DataFrame(all_docs), use_container_width=True)
else:
    st.info("No documents yet. Create a document set and upload documents.")

# Add navigation buttons at the bottom if needed
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📊 View Facts"):
        st.info("This would navigate to the Facts view")
with col2:
    if st.button("📑 View Arguments"):
        st.info("This would navigate to the Arguments view")
with col3:
    if st.button("📁 View Exhibits"):
        st.info("This would navigate to the Exhibits view")
