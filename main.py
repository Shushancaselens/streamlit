import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="CaseLens - Home",
    page_icon="C",
    layout="wide"
)

# Custom CSS for CaseLens blue buttons
st.markdown("""
    <style>
    /* All buttons - filled with CaseLens blue */
    div[data-testid="stButton"] > button {
        background-color: #4D68F9 !important;
        color: white !important;
        border: none !important;
    }
    div[data-testid="stButton"] > button:hover {
        background-color: #3D58E9 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_case' not in st.session_state:
    st.session_state.selected_case = None

# Sample case data (replace with your actual data)
cases = [
    {
        "id": 1,
        "name": "Hanessianadr Case 1",
        "description": "Harris FRC Acquisition vs RESEARCH CORPORATION TECHNOLOGIES",
        "documents": 156,
        "num_events": 3,
        "date_range": "1999-01-01 to 2025-09-30",
        "status": "Active",
        "last_updated": "2024-11-15"
    },
    {
        "id": 2,
        "name": "Patent Infringement Case 2",
        "description": "Technology patent dispute involving multiple parties",
        "documents": 243,
        "num_events": 5,
        "date_range": "2020-03-15 to 2025-06-30",
        "status": "Active",
        "last_updated": "2024-11-18"
    },
    {
        "id": 3,
        "name": "Contract Dispute Case 3",
        "description": "Commercial contract breach and damages claim",
        "documents": 89,
        "num_events": 2,
        "date_range": "2021-07-01 to 2024-12-31",
        "status": "Pending",
        "last_updated": "2024-11-10"
    },
    {
        "id": 4,
        "name": "Trademark Litigation Case 4",
        "description": "Brand trademark infringement proceedings",
        "documents": 312,
        "num_events": 8,
        "date_range": "2019-05-20 to 2025-08-15",
        "status": "Active",
        "last_updated": "2024-11-19"
    },
    {
        "id": 5,
        "name": "Arbitration Case 5",
        "description": "International arbitration dispute resolution",
        "documents": 178,
        "num_events": 4,
        "date_range": "2022-01-10 to 2025-11-30",
        "status": "In Review",
        "last_updated": "2024-11-12"
    }
]

def navigate_to_events(case):
    """Navigate to events page with selected case"""
    st.session_state.selected_case = case
    st.session_state.current_page = 'events'
    st.rerun()

def show_home_page():
    """Display the home page with case selection"""
    
    # Sidebar with user info and navigation
    with st.sidebar:
        st.markdown("**User:** shushan@caselens.tech")
        st.divider()
        
        # Navigation buttons
        if st.button("Upload Documents", use_container_width=True):
            st.session_state.current_page = 'upload_documents'
            st.rerun()
        
        if st.button("My Documents", use_container_width=True):
            st.session_state.current_page = 'my_documents'
            st.rerun()
        
        if st.button("Settings", use_container_width=True):
            st.session_state.current_page = 'settings'
            st.rerun()
    
    st.divider()
    
    # Display cases in a grid layout (3 cards per row)
    for i in range(0, len(cases), 3):
        cols = st.columns(3)
        
        for j, col in enumerate(cols):
            if i + j < len(cases):
                case = cases[i + j]
                
                with col:
                    # Create a card using Streamlit native container with border
                    with st.container(border=True):
                        # Case name with View button
                        col_name, col_btn = st.columns([3, 1])
                        with col_name:
                            st.markdown(f"**{case['name']}**")
                        with col_btn:
                            if st.button("View", key=f"case_{case['id']}", type="secondary"):
                                navigate_to_events(case)
                        
                        # Case description with fixed height to keep cards uniform
                        st.markdown(f"""
                        <div style="height: 48px; overflow: hidden; text-overflow: ellipsis;">
                        <span style="color: #6c757d; font-size: 0.875rem;">{case['description']}</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown("")  # Spacing
                        
                        # Information as colorful Streamlit native badges with labels
                        date_range_short = case['date_range'][:4] + '-' + case['date_range'][-4:]
                        
                        # Display tags with labels inline
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"**Status:** :blue-background[{case['status']}]")
                            st.markdown(f"**Documents:** :green-background[{case['documents']}]")
                        with col2:
                            st.markdown(f"**Events:** :orange-background[{case['num_events']}]")
                            st.markdown(f"**Period:** :gray-background[{date_range_short}]")

def show_upload_documents_page():
    """Display the upload documents page"""
    
    # Sidebar with user info
    with st.sidebar:
        st.markdown("**User:** shushan@caselens.tech")
    
    # Back button and header
    if st.button("← Back to Cases", type="secondary"):
        st.session_state.current_page = 'home'
        st.rerun()
    
    st.title("Upload Documents")
    st.divider()
    
    # Initialize documents in session state if not exists
    if 'uploaded_documents' not in st.session_state:
        st.session_state.uploaded_documents = []
    
    # Upload section
    st.markdown("### Upload New Documents")
    st.caption("Upload documents to process and add to your cases")
    
    uploaded_files = st.file_uploader(
        "Choose files to upload",
        accept_multiple_files=True,
        type=['pdf', 'docx', 'doc', 'txt', 'xlsx', 'xls', 'csv', 'png', 'jpg', 'jpeg'],
        key="doc_uploader"
    )
    
    # Add uploaded files to session state
    if uploaded_files:
        with st.spinner('Processing documents...'):
            import time
            time.sleep(2)  # Simulate processing time - replace with actual processing
            
            newly_added = []
            for uploaded_file in uploaded_files:
                # Check if file already exists
                if not any(doc['name'] == uploaded_file.name for doc in st.session_state.uploaded_documents):
                    from datetime import datetime
                    doc_info = {
                        'name': uploaded_file.name,
                        'size': uploaded_file.size,
                        'type': uploaded_file.type,
                        'uploaded_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'file': uploaded_file
                    }
                    st.session_state.uploaded_documents.append(doc_info)
                    newly_added.append(doc_info)
        
        st.success(f"Successfully processed {len(newly_added)} file(s)!")
        
        st.divider()
        
        # Show the processed documents
        st.markdown("### Processed Documents")
        for idx, doc in enumerate(newly_added):
            with st.container(border=True):
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.markdown(f"**{doc['name']}**")
                    file_size_kb = doc['size'] / 1024
                    if file_size_kb > 1024:
                        st.caption(f"Type: {doc['type']} | Size: {file_size_kb/1024:.2f} MB")
                    else:
                        st.caption(f"Type: {doc['type']} | Size: {file_size_kb:.2f} KB")
                with col2:
                    st.markdown("✓ Processed")
                with col3:
                    st.download_button(
                        label="Download",
                        data=doc['file'].getvalue(),
                        file_name=doc['name'],
                        mime=doc['type'],
                        key=f"download_processed_{idx}",
                        type="secondary"
                    )
    
    st.divider()
    
    # Show summary
    st.markdown("### Summary")
    st.info(f"Total documents in library: {len(st.session_state.uploaded_documents)}")

def show_my_documents_page():
    """Display all uploaded documents"""
    
    # Sidebar with user info
    with st.sidebar:
        st.markdown("**User:** shushan@caselens.tech")
    
    # Back button and header
    if st.button("← Back to Cases", type="secondary"):
        st.session_state.current_page = 'home'
        st.rerun()
    
    st.title("My Documents")
    st.divider()
    
    # Initialize documents in session state if not exists
    if 'uploaded_documents' not in st.session_state:
        st.session_state.uploaded_documents = []
    
    # Display uploaded documents
    if len(st.session_state.uploaded_documents) == 0:
        st.info("No documents uploaded yet.")
        st.markdown("")
        if st.button("Upload Documents", type="primary"):
            st.session_state.current_page = 'upload_documents'
            st.rerun()
    else:
        # Header with count and upload button
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**Total Documents:** {len(st.session_state.uploaded_documents)}")
        with col2:
            if st.button("Upload More", type="primary"):
                st.session_state.current_page = 'upload_documents'
                st.rerun()
        
        st.markdown("")
        
        # Display documents in a table format
        for idx, doc in enumerate(st.session_state.uploaded_documents):
            with st.container(border=True):
                col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
                
                with col1:
                    st.markdown(f"**{doc['name']}**")
                    st.caption(f"Type: {doc['type']}")
                
                with col2:
                    file_size_kb = doc['size'] / 1024
                    if file_size_kb > 1024:
                        st.caption(f"Size: {file_size_kb/1024:.2f} MB")
                    else:
                        st.caption(f"Size: {file_size_kb:.2f} KB")
                
                with col3:
                    st.caption(f"Uploaded: {doc['uploaded_date']}")
                
                with col4:
                    # View/Download button
                    if st.button("View", key=f"view_doc_{idx}", type="secondary"):
                        st.session_state.viewing_doc = doc
                        st.session_state.viewing_doc_idx = idx
                    
                    # Delete button
                    if st.button("Delete", key=f"delete_doc_{idx}", type="secondary"):
                        st.session_state.uploaded_documents.pop(idx)
                        st.rerun()
        
        # Show document viewer if a document is selected
        if 'viewing_doc' in st.session_state and st.session_state.viewing_doc:
            st.divider()
            st.markdown("### Document Viewer")
            doc = st.session_state.viewing_doc
            
            st.markdown(f"**Viewing:** {doc['name']}")
            
            # Download button
            st.download_button(
                label="Download",
                data=doc['file'].getvalue(),
                file_name=doc['name'],
                mime=doc['type']
            )
            
            # Display content based on file type
            if doc['type'] == 'application/pdf':
                st.info("PDF preview - Download to view the full document")
            elif doc['type'] in ['image/png', 'image/jpeg', 'image/jpg']:
                st.image(doc['file'])
            elif doc['type'] in ['text/plain', 'text/csv']:
                st.text(doc['file'].getvalue().decode('utf-8'))
            else:
                st.info("Preview not available for this file type. Use the download button to view.")
            
            if st.button("Close Viewer"):
                del st.session_state.viewing_doc
                del st.session_state.viewing_doc_idx
                st.rerun()

def show_events_page():
    """Display the events page for selected case"""
    if st.session_state.selected_case is None:
        st.error("No case selected. Returning to home page...")
        st.session_state.current_page = 'home'
        st.rerun()
        return
    
    case = st.session_state.selected_case
    
    # Sidebar with user info only
    with st.sidebar:
        st.markdown("**User:** shushan@caselens.tech")
    
    # Back button and header
    if st.button("← Back to Cases", type="secondary"):
        st.session_state.current_page = 'home'
        st.rerun()
    
    st.markdown(f"### {case['name']}")
    st.divider()
    
    # Tabs for different views
    tab1, tab2 = st.tabs(["Card View", "Table View"])
    
    with tab1:
        st.markdown("### Card View")
        st.info("This is where your events will be displayed in card format (similar to your second screenshot)")
        
        # Sample events display
        st.markdown("""
        **Event 1999-00-00**  
        In 1999, the definition of "Allowed Deductions" under the License Agreements between Harris FRC Acquisition, L.P. and RESEARCH CORPORATION TECHNOLOGIES, INC...
        
        1 Source
        """)
        
        st.divider()
        
        st.markdown("""
        **Event 2008-00-00**  
        From 2008 to 30 September 2015, a dispute in the ICC International Court of Arbitration (case number 27850/PDP) involves Harris FRC Acquisition...
        
        1 Source
        """)
    
    with tab2:
        st.markdown("### Table View")
        st.info("This is where your events will be displayed in table format")
        
        # Sample table
        import pandas as pd
        sample_data = pd.DataFrame({
            'Date': ['1999-00-00', '2008-00-00', '2008-01-01'],
            'Description': [
                'Definition of Allowed Deductions established',
                'ICC Arbitration case initiated',
                'Net sales reporting period begins'
            ],
            'Sources': [1, 1, 2]
        })
        st.dataframe(sample_data, use_container_width=True)

def show_settings_page():
    """Display the settings page"""
    
    col1, col2 = st.columns([6, 1])
    with col1:
        if st.button("← Back"):
            st.session_state.current_page = 'home'
            st.rerun()
        st.title("Settings")
    
    st.divider()
    
    st.markdown("### Account Settings")
    
    st.markdown("**Username / Email**")
    email = st.text_input("", value="shushan@caselens.tech", disabled=True)
    
    st.divider()
    
    if st.button("Log out", type="primary"):
        st.success("Logged out successfully!")

# Main app logic
def main():
    if st.session_state.current_page == 'home':
        show_home_page()
    elif st.session_state.current_page == 'upload_documents':
        show_upload_documents_page()
    elif st.session_state.current_page == 'my_documents':
        show_my_documents_page()
    elif st.session_state.current_page == 'events':
        show_events_page()
    elif st.session_state.current_page == 'settings':
        show_settings_page()

if __name__ == "__main__":
    main()
