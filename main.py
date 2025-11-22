import streamlit as st
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="CaseLens - Home",
    page_icon="C",
    layout="wide"
)

# Custom CSS for buttons
st.markdown("""
    <style>
    /* All buttons - simple with borders */
    div[data-testid="stButton"] > button {
        background-color: transparent !important;
        color: inherit !important;
        border: 1px solid rgba(49, 51, 63, 0.2) !important;
    }
    div[data-testid="stButton"] > button:hover {
        background-color: rgba(49, 51, 63, 0.05) !important;
        border: 1px solid rgba(49, 51, 63, 0.4) !important;
    }
    /* Make download buttons simple with borders */
    div[data-testid="stDownloadButton"] > button {
        background-color: transparent !important;
        color: inherit !important;
        border: 1px solid rgba(49, 51, 63, 0.2) !important;
    }
    div[data-testid="stDownloadButton"] > button:hover {
        background-color: rgba(49, 51, 63, 0.05) !important;
        border: 1px solid rgba(49, 51, 63, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'processed_docs' not in st.session_state:
    st.session_state.processed_docs = None
if 'uploaded_filename' not in st.session_state:
    st.session_state.uploaded_filename = None

def process_pdf_with_ai(uploaded_file):
    """
    Process the uploaded PDF with AI and generate two Word documents
    Replace this function with your actual AI processing logic
    """
    # Here you would:
    # 1. Extract text from PDF
    # 2. Send to AI for processing
    # 3. Generate two Word documents based on AI output
    
    # For now, we'll create placeholder Word documents
    # You'll need to replace this with actual docx generation using python-docx library
    
    doc1_content = f"Summary Report for {uploaded_file.name}"
    doc2_content = f"Detailed Analysis for {uploaded_file.name}"
    
    return doc1_content, doc2_content

def show_home_page():
    """Display the home page with PDF upload"""
    
    # Sidebar with user info
    with st.sidebar:
        st.markdown("**User:** shushan@caselens.tech")
        st.divider()
        if st.button("Settings", use_container_width=True):
            st.session_state.current_page = 'settings'
            st.rerun()
    
    # Header
    st.markdown("### AI Data Extraction and Summarization")
    st.divider()
    
    # Upload section
    st.markdown("Upload typewritten or handwritten scanned PDF files")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])
    
    if uploaded_file is not None:
        # Check if this is a new file
        if st.session_state.uploaded_filename != uploaded_file.name:
            
            st.info(f"File uploaded: {uploaded_file.name}")
            
            # Automatically start AI analysis - show progress
            progress_bar = st.progress(0, text="AI is analyzing your document...")
            time.sleep(1)
            
            progress_bar.progress(33, text="Generating Document 1...")
            time.sleep(1)
            
            progress_bar.progress(66, text="Generating Document 2...")
            time.sleep(1)
            
            # Process the document
            doc1, doc2 = process_pdf_with_ai(uploaded_file)
            
            progress_bar.progress(100, text="Processing complete!")
            time.sleep(0.5)
            
            # Store results in session state
            st.session_state.processed_docs = {
                'doc1': doc1,
                'doc2': doc2,
                'filename': uploaded_file.name
            }
            st.session_state.uploaded_filename = uploaded_file.name
            
            # Clear progress bar
            progress_bar.empty()
            
            st.rerun()
        
        # Show download section if documents are ready
        if st.session_state.processed_docs is not None:
            st.markdown("### Results")
            st.markdown("2 documents ready")
            
            # Create a zip file with both documents
            import io
            import zipfile
            
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.writestr("document_1_summary.docx", st.session_state.processed_docs['doc1'])
                zip_file.writestr("document_2_analysis.docx", st.session_state.processed_docs['doc2'])
            zip_buffer.seek(0)
            
            st.download_button(
                label="Download All Documents",
                data=zip_buffer.getvalue(),
                file_name="all_documents.zip",
                mime="application/zip",
                key="download_all"
            )

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
    elif st.session_state.current_page == 'settings':
        show_settings_page()

if __name__ == "__main__":
    main()
