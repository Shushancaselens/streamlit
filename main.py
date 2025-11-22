import streamlit as st
from datetime import datetime
import time

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
if 'processed_docs' not in st.session_state:
    st.session_state.processed_docs = None

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
    st.markdown("### Upload Document")
    st.divider()
    
    # Upload section
    st.markdown("Upload a PDF document to process with AI and generate two Word documents.")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])
    
    if uploaded_file is not None:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Process Document", type="primary", use_container_width=True):
                # Show processing status with progress
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("🤖 AI is analyzing your document...")
                progress_bar.progress(25)
                time.sleep(1)
                
                status_text.text("📝 Generating Document 1...")
                progress_bar.progress(50)
                time.sleep(1)
                
                status_text.text("📄 Generating Document 2...")
                progress_bar.progress(75)
                time.sleep(1)
                
                # Process the document
                doc1, doc2 = process_pdf_with_ai(uploaded_file)
                
                status_text.text("✅ Processing complete!")
                progress_bar.progress(100)
                time.sleep(0.5)
                
                # Store results in session state
                st.session_state.processed_docs = {
                    'doc1': doc1,
                    'doc2': doc2,
                    'filename': uploaded_file.name
                }
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                st.rerun()
    
    # Show download buttons if documents are ready
    if st.session_state.processed_docs is not None:
        st.divider()
        st.markdown("### 📥 Generated Documents Ready")
        st.success("Your documents have been successfully generated!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container(border=True):
                st.markdown("#### 📄 Document 1: Summary Report")
                st.markdown("Contains the summary and key findings from your document.")
                st.download_button(
                    label="⬇️ Download Document 1",
                    data=st.session_state.processed_docs['doc1'],
                    file_name="document_1_summary.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )
        
        with col2:
            with st.container(border=True):
                st.markdown("#### 📄 Document 2: Detailed Analysis")
                st.markdown("Contains the detailed analysis and comprehensive insights.")
                st.download_button(
                    label="⬇️ Download Document 2",
                    data=st.session_state.processed_docs['doc2'],
                    file_name="document_2_analysis.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )
        
        # Reset button
        st.divider()
        if st.button("🔄 Process Another Document", type="secondary"):
            st.session_state.processed_docs = None
            st.rerun()

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
