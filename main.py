import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64
import os
from datetime import datetime

# Set page config
st.set_page_config(page_title="CaseLens - Legal Document Analysis", layout="wide", initial_sidebar_state="collapsed")

# Initialize session state with better defaults
if 'documents' not in st.session_state:
    st.session_state.documents = []

if 'current_view' not in st.session_state:
    st.session_state.current_view = "dashboard"

if 'uploaded_files_data' not in st.session_state:
    st.session_state.uploaded_files_data = {}

if 'show_onboarding' not in st.session_state:
    st.session_state.show_onboarding = len(st.session_state.documents) == 0

# Sample data for demonstration
def get_sample_documents():
    return [
        {
            "id": "doc_1",
            "name": "Statement of Appeal",
            "party": "Appellant",
            "category": "Appeal Documents",
            "upload_date": "2024-01-15",
            "file_type": "PDF",
            "size": "245 KB",
            "status": "Processed",
            "preview": "This statement outlines the appellant's grounds for appeal...",
            "key_facts": ["Filed on January 15, 2024", "Challenges lower court decision", "Cites procedural errors"]
        },
        {
            "id": "doc_2", 
            "name": "Expert Witness Report",
            "party": "Respondent",
            "category": "Evidence",
            "upload_date": "2024-01-18",
            "file_type": "PDF", 
            "size": "1.2 MB",
            "status": "Processed",
            "preview": "Expert analysis of the technical aspects of the case...",
            "key_facts": ["Technical analysis provided", "Supports respondent position", "Peer-reviewed methodology"]
        },
        {
            "id": "doc_3",
            "name": "Contract Amendment",
            "party": "Shared",
            "category": "Contracts",
            "upload_date": "2024-01-20",
            "file_type": "PDF",
            "size": "156 KB", 
            "status": "Processing",
            "preview": "Amendment to the original service agreement...",
            "key_facts": ["Modifies payment terms", "Effective March 2024", "Signed by both parties"]
        }
    ]

def get_case_facts():
    return [
        {
            "id": "fact_1",
            "description": "Contract signed on March 15, 2023",
            "date": "2023-03-15",
            "source": "Contract Amendment",
            "party": "Shared",
            "disputed": False,
            "evidence": ["doc_3"]
        },
        {
            "id": "fact_2", 
            "description": "First breach notification sent",
            "date": "2023-08-20",
            "source": "Email Communications",
            "party": "Appellant",
            "disputed": True,
            "evidence": ["doc_1"]
        },
        {
            "id": "fact_3",
            "description": "Technical failure occurred during testing",
            "date": "2023-09-10", 
            "source": "Expert Witness Report",
            "party": "Respondent",
            "disputed": True,
            "evidence": ["doc_2"]
        }
    ]

# Smart file processing function
def process_uploaded_file(uploaded_file):
    """Process uploaded file and extract relevant information"""
    try:
        file_content = uploaded_file.read()
        
        # Auto-detect category based on filename and type
        filename = uploaded_file.name.lower()
        category = "General"
        
        if any(word in filename for word in ["contract", "agreement", "terms"]):
            category = "Contracts"
        elif any(word in filename for word in ["evidence", "exhibit", "proof"]):
            category = "Evidence"
        elif any(word in filename for word in ["appeal", "motion", "brief"]):
            category = "Appeal Documents"
        elif any(word in filename for word in ["witness", "expert", "report"]):
            category = "Expert Reports"
        
        # Auto-detect party (simplified logic)
        party = "Shared"  # Default
        if any(word in filename for word in ["appellant", "plaintiff"]):
            party = "Appellant"
        elif any(word in filename for word in ["respondent", "defendant"]):
            party = "Respondent"
        
        doc_data = {
            "id": f"doc_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "name": uploaded_file.name,
            "party": party,
            "category": category,
            "upload_date": datetime.now().strftime("%Y-%m-%d"),
            "file_type": uploaded_file.type.split('/')[-1].upper() if uploaded_file.type else "Unknown",
            "size": f"{uploaded_file.size/1024:.1f} KB" if uploaded_file.size else "Unknown",
            "status": "Processing",
            "preview": f"Document uploaded: {uploaded_file.name}",
            "key_facts": ["Document uploaded and processing"]
        }
        
        # Store file data
        st.session_state.uploaded_files_data[doc_data["id"]] = {
            "content": file_content,
            "original_name": uploaded_file.name,
            "type": uploaded_file.type,
            "size": uploaded_file.size
        }
        
        return doc_data
        
    except Exception as e:
        st.error(f"Error processing file: {e}")
        return None

def render_dashboard():
    """Main dashboard view"""
    
    # Header with key metrics
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 10px; margin-bottom: 30px; color: white;">
        <h1 style="margin: 0; font-size: 2.5rem; font-weight: 700;">Case Overview</h1>
        <p style="margin: 10px 0 0 0; font-size: 1.1rem; opacity: 0.9;">Your legal documents and case analysis at a glance</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats
    all_docs = st.session_state.documents + get_sample_documents()
    facts = get_case_facts()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📄 Total Documents", len(all_docs))
    with col2:
        processing = sum(1 for doc in all_docs if doc.get("status") == "Processing")
        st.metric("⚡ Processing", processing)
    with col3:
        disputed_facts = sum(1 for fact in facts if fact.get("disputed"))
        st.metric("⚠️ Disputed Facts", disputed_facts)
    with col4:
        categories = len(set(doc.get("category", "General") for doc in all_docs))
        st.metric("📂 Categories", categories)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick actions
    st.subheader("Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📤 Upload Documents", use_container_width=True, type="primary"):
            st.session_state.current_view = "upload"
            st.rerun()
    
    with col2:
        if st.button("📊 Analyze Facts", use_container_width=True):
            st.session_state.current_view = "facts"
            st.rerun()
    
    with col3:
        if st.button("📁 Browse Documents", use_container_width=True):
            st.session_state.current_view = "documents"
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Recent documents preview
    st.subheader("Recent Documents")
    
    if all_docs:
        # Sort by upload date (most recent first)
        recent_docs = sorted(all_docs, key=lambda x: x.get("upload_date", ""), reverse=True)[:3]
        
        for doc in recent_docs:
            with st.container():
                st.markdown(f"""
                <div style="border: 1px solid #e1e5e9; border-radius: 8px; padding: 20px; margin-bottom: 15px; background: white;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <h4 style="margin: 0; color: #1f2937;">{doc['name']}</h4>
                        <span style="background: {'#10b981' if doc['status'] == 'Processed' else '#f59e0b'}; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 500;">
                            {doc['status']}
                        </span>
                    </div>
                    <div style="display: flex; gap: 20px; margin-bottom: 10px;">
                        <span style="color: #6b7280; font-size: 14px;">📂 {doc['category']}</span>
                        <span style="color: #6b7280; font-size: 14px;">⚖️ {doc['party']}</span>
                        <span style="color: #6b7280; font-size: 14px;">📅 {doc['upload_date']}</span>
                        <span style="color: #6b7280; font-size: 14px;">📏 {doc['size']}</span>
                    </div>
                    <p style="margin: 0; color: #4b5563; font-size: 14px; line-height: 1.5;">{doc['preview']}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No documents uploaded yet. Click 'Upload Documents' to get started!")

def render_upload_view():
    """Simplified upload interface"""
    
    # Back button
    if st.button("← Back to Dashboard", type="secondary"):
        st.session_state.current_view = "dashboard"
        st.rerun()
    
    st.title("📤 Upload Documents")
    st.markdown("Drag and drop your legal documents below. We'll automatically organize and analyze them for you.")
    
    # Simple drag-and-drop uploader
    uploaded_files = st.file_uploader(
        "Choose files to upload",
        type=["pdf", "docx", "txt", "jpg", "png", "xlsx", "csv"],
        accept_multiple_files=True,
        help="Supported formats: PDF, Word, Text, Images, Excel, CSV"
    )
    
    if uploaded_files:
        st.success(f"Ready to process {len(uploaded_files)} file(s)")
        
        if st.button("Process Documents", type="primary", use_container_width=True):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, uploaded_file in enumerate(uploaded_files):
                status_text.text(f"Processing {uploaded_file.name}...")
                progress_bar.progress((i + 1) / len(uploaded_files))
                
                # Process the file
                doc_data = process_uploaded_file(uploaded_file)
                if doc_data:
                    st.session_state.documents.append(doc_data)
            
            progress_bar.progress(1.0)
            status_text.text("All documents processed successfully!")
            
            st.balloons()
            st.success(f"Successfully uploaded {len(uploaded_files)} documents!")
            
            # Auto-navigate to documents view
            if st.button("View Uploaded Documents", type="primary"):
                st.session_state.current_view = "documents"
                st.rerun()

def render_documents_view():
    """Document browser with smart filtering"""
    
    # Back button
    if st.button("← Back to Dashboard", type="secondary"):
        st.session_state.current_view = "dashboard"
        st.rerun()
    
    st.title("📁 Document Library")
    
    all_docs = st.session_state.documents + get_sample_documents()
    
    if not all_docs:
        st.info("No documents available. Upload some documents to get started!")
        return
    
    # Smart filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        categories = sorted(set(doc.get("category", "General") for doc in all_docs))
        selected_category = st.selectbox("Filter by Category", ["All"] + categories)
    
    with col2:
        parties = sorted(set(doc.get("party", "Unknown") for doc in all_docs))
        selected_party = st.selectbox("Filter by Party", ["All"] + parties)
    
    with col3:
        search_term = st.text_input("🔍 Search documents", placeholder="Search by name or content...")
    
    # Filter documents
    filtered_docs = all_docs
    
    if selected_category != "All":
        filtered_docs = [doc for doc in filtered_docs if doc.get("category") == selected_category]
    
    if selected_party != "All":
        filtered_docs = [doc for doc in filtered_docs if doc.get("party") == selected_party]
    
    if search_term:
        filtered_docs = [doc for doc in filtered_docs 
                        if search_term.lower() in doc.get("name", "").lower() 
                        or search_term.lower() in doc.get("preview", "").lower()]
    
    st.markdown(f"**Showing {len(filtered_docs)} of {len(all_docs)} documents**")
    
    # Display documents in a grid
    for i in range(0, len(filtered_docs), 2):
        cols = st.columns(2)
        
        for j, col in enumerate(cols):
            if i + j < len(filtered_docs):
                doc = filtered_docs[i + j]
                
                with col:
                    # Document card
                    status_color = "#10b981" if doc["status"] == "Processed" else "#f59e0b"
                    party_color = "#3b82f6" if doc["party"] == "Appellant" else "#ef4444" if doc["party"] == "Respondent" else "#6b7280"
                    
                    st.markdown(f"""
                    <div style="border: 1px solid #e1e5e9; border-radius: 8px; padding: 20px; margin-bottom: 20px; background: white; height: 280px; display: flex; flex-direction: column;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                            <h4 style="margin: 0; color: #1f2937; font-size: 16px; line-height: 1.3;">{doc['name'][:40]}{'...' if len(doc['name']) > 40 else ''}</h4>
                            <span style="background: {status_color}; color: white; padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 500;">
                                {doc['status']}
                            </span>
                        </div>
                        
                        <div style="flex-grow: 1; margin-bottom: 15px;">
                            <p style="margin: 0 0 10px 0; color: #4b5563; font-size: 13px; line-height: 1.4;">{doc['preview'][:80]}{'...' if len(doc['preview']) > 80 else ''}</p>
                            
                            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 10px;">
                                <span style="background: {party_color}; color: white; padding: 2px 6px; border-radius: 10px; font-size: 10px; font-weight: 500;">
                                    {doc['party']}
                                </span>
                                <span style="background: #f3f4f6; color: #374151; padding: 2px 6px; border-radius: 10px; font-size: 10px;">
                                    {doc['category']}
                                </span>
                            </div>
                        </div>
                        
                        <div style="border-top: 1px solid #f3f4f6; padding-top: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: #6b7280;">
                                <span>📅 {doc['upload_date']}</span>
                                <span>📏 {doc['size']}</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

def render_facts_view():
    """Interactive facts analysis"""
    
    # Back button
    if st.button("← Back to Dashboard", type="secondary"):
        st.session_state.current_view = "dashboard"
        st.rerun()
    
    st.title("📊 Case Facts Analysis")
    
    facts = get_case_facts()
    
    # Quick stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Facts", len(facts))
    with col2:
        disputed = sum(1 for fact in facts if fact.get("disputed"))
        st.metric("Disputed", disputed, delta=f"{disputed}/{len(facts)}")
    with col3:
        undisputed = len(facts) - disputed
        st.metric("Undisputed", undisputed, delta=f"{undisputed}/{len(facts)}")
    
    # Facts filter
    fact_filter = st.radio("Show facts:", ["All", "Disputed Only", "Undisputed Only"], horizontal=True)
    
    # Filter facts
    filtered_facts = facts
    if fact_filter == "Disputed Only":
        filtered_facts = [fact for fact in facts if fact.get("disputed")]
    elif fact_filter == "Undisputed Only":
        filtered_facts = [fact for fact in facts if not fact.get("disputed")]
    
    # Display facts
    for fact in filtered_facts:
        dispute_color = "#fef2f2" if fact.get("disputed") else "#f0fdf4"
        border_color = "#fca5a5" if fact.get("disputed") else "#86efac"
        
        st.markdown(f"""
        <div style="border-left: 4px solid {border_color}; background: {dispute_color}; padding: 20px; margin-bottom: 15px; border-radius: 0 8px 8px 0;">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 10px;">
                <h4 style="margin: 0; color: #1f2937;">{fact['description']}</h4>
                <span style="background: {'#ef4444' if fact['disputed'] else '#10b981'}; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 500; margin-left: auto;">
                    {'Disputed' if fact['disputed'] else 'Undisputed'}
                </span>
            </div>
            <div style="display: flex; gap: 20px; margin-bottom: 10px; font-size: 14px; color: #6b7280;">
                <span>📅 {fact['date']}</span>
                <span>⚖️ {fact['party']}</span>
                <span>📄 {fact['source']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    # Custom CSS for better UX
    st.markdown("""
    <style>
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Custom styling */
        .stApp {
            background-color: #f8fafc;
        }
        
        .main > div {
            padding-top: 2rem;
        }
        
        /* Button improvements */
        .stButton > button {
            border-radius: 8px;
            border: none;
            font-weight: 500;
            transition: all 0.2s;
        }
        
        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        
        /* File uploader styling */
        .stFileUploader > div > div {
            border-radius: 10px;
            border: 2px dashed #cbd5e1;
            background: white;
            padding: 40px;
            text-align: center;
        }
        
        /* Metric styling */
        [data-testid="metric-container"] {
            background: white;
            border: 1px solid #e1e5e9;
            padding: 16px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        /* Remove extra spacing */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Top navigation
    st.markdown("""
    <div style="background: white; padding: 15px 0; margin: -2rem -1rem 2rem -1rem; border-bottom: 1px solid #e1e5e9;">
        <div style="max-width: 1200px; margin: 0 auto; display: flex; align-items: center; padding: 0 1rem;">
            <h2 style="margin: 0; color: #4338ca; font-weight: 700;">⚖️ CaseLens</h2>
            <span style="margin-left: auto; color: #6b7280; font-size: 14px;">Legal Document Analysis Platform</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Show onboarding for new users
    if st.session_state.show_onboarding and len(st.session_state.documents) == 0:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px; border-radius: 15px; margin-bottom: 30px; color: white; text-align: center;">
            <h1 style="margin: 0 0 20px 0; font-size: 2.5rem;">Welcome to CaseLens! 👋</h1>
            <p style="margin: 0 0 30px 0; font-size: 1.2rem; opacity: 0.9;">Your intelligent legal document analysis platform</p>
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <h3 style="margin: 0 0 15px 0;">Get started in 3 easy steps:</h3>
                <div style="display: flex; justify-content: space-around; text-align: center;">
                    <div>
                        <div style="font-size: 2rem; margin-bottom: 10px;">📤</div>
                        <div>Upload Documents</div>
                    </div>
                    <div>
                        <div style="font-size: 2rem; margin-bottom: 10px;">🤖</div>
                        <div>AI Analysis</div>
                    </div>
                    <div>
                        <div style="font-size: 2rem; margin-bottom: 10px;">📊</div>
                        <div>Review Insights</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Start by Uploading Documents", type="primary", use_container_width=True):
                st.session_state.current_view = "upload"
                st.session_state.show_onboarding = False
                st.rerun()
    
    # Route to appropriate view
    if st.session_state.current_view == "upload":
        render_upload_view()
    elif st.session_state.current_view == "documents":
        render_documents_view()
    elif st.session_state.current_view == "facts":
        render_facts_view()
    else:
        render_dashboard()

if __name__ == "__main__":
    main()

