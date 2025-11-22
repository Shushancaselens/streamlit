import streamlit as st
import base64
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import io
import time

# Configure page
st.set_page_config(
    page_title="PDF to Word Converter",
    page_icon="📄",
    layout="wide"
)

# Check for anthropic package
try:
    import anthropic
except ImportError:
    st.error("❌ The 'anthropic' package is not installed. Please add it to requirements.txt")
    st.stop()

# Check for API key
if 'ANTHROPIC_API_KEY' not in st.secrets:
    st.error("❌ Please add your ANTHROPIC_API_KEY to Streamlit secrets")
    st.info("""
    ### How to add your API key:
    
    1. Go to your Streamlit Cloud dashboard
    2. Click on your app settings (⚙️)
    3. Go to "Secrets" section
    4. Add:
    ```
    ANTHROPIC_API_KEY = "your-api-key-here"
    ```
    
    Get your API key from: https://console.anthropic.com/
    """)
    st.stop()

# Initialize session state
if 'processing' not in st.session_state:
    st.session_state.processing = False
if 'documents_ready' not in st.session_state:
    st.session_state.documents_ready = False
if 'doc1_bytes' not in st.session_state:
    st.session_state.doc1_bytes = None
if 'doc2_bytes' not in st.session_state:
    st.session_state.doc2_bytes = None

def create_word_document(title, content, doc_type="summary"):
    """Create a professional Word document with the given content"""
    doc = Document()
    
    # Add title
    title_paragraph = doc.add_heading(title, 0)
    title_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    # Add content
    paragraphs = content.split('\n\n')
    for para in paragraphs:
        if para.strip():
            if para.strip().startswith('#'):
                # It's a heading
                heading_text = para.strip().lstrip('#').strip()
                doc.add_heading(heading_text, level=1)
            else:
                p = doc.add_paragraph(para.strip())
                p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
    
    # Save to bytes
    doc_bytes = io.BytesIO()
    doc.save(doc_bytes)
    doc_bytes.seek(0)
    return doc_bytes.getvalue()

def process_pdf_with_claude(pdf_file):
    """Process PDF with Claude API and generate two different analyses"""
    
    # Convert PDF to base64
    pdf_data = base64.b64encode(pdf_file.read()).decode('utf-8')
    
    # Initialize Claude client with API key from secrets
    client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
    
    # First API call - Generate Summary Document
    with st.spinner("🤖 AI is analyzing your PDF and creating Document 1 (Summary)..."):
        response1 = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "document",
                            "source": {
                                "type": "base64",
                                "media_type": "application/pdf",
                                "data": pdf_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": """Please analyze this PDF document and create a comprehensive summary. 
                            
                            Include:
                            - Main topics and themes
                            - Key points and findings
                            - Important details
                            - Overall conclusions
                            
                            Format your response as a well-structured document with clear headings (use # for headings) and paragraphs."""
                        }
                    ]
                }
            ]
        )
        
        summary_content = response1.content[0].text
        time.sleep(1)  # Small delay between requests
    
    # Second API call - Generate Key Insights Document
    with st.spinner("🤖 AI is creating Document 2 (Key Insights & Action Items)..."):
        response2 = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "document",
                            "source": {
                                "type": "base64",
                                "media_type": "application/pdf",
                                "data": pdf_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": """Please analyze this PDF document and create a document focused on actionable insights.
                            
                            Include:
                            - Key insights and takeaways
                            - Action items or recommendations
                            - Critical data points or statistics
                            - Areas requiring attention
                            - Next steps or follow-up items
                            
                            Format your response as a well-structured document with clear headings (use # for headings) and paragraphs."""
                        }
                    ]
                }
            ]
        )
        
        insights_content = response2.content[0].text
    
    return summary_content, insights_content

# Main app
st.title("📄 PDF to Word Document Generator")
st.markdown("Upload a PDF and let AI generate two comprehensive Word documents for you")

# File uploader
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=['pdf'],
    help="Upload a PDF document to analyze"
)

if uploaded_file is not None:
    # Display file info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("File Name", uploaded_file.name)
    with col2:
        st.metric("File Size", f"{uploaded_file.size / 1024:.2f} KB")
    with col3:
        st.metric("File Type", "PDF")
    
    st.divider()
    
    # Process button
    if st.button("🚀 Generate Word Documents", type="primary", disabled=st.session_state.processing):
        st.session_state.processing = True
        st.session_state.documents_ready = False
        
        try:
            # Show progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("📤 Uploading PDF to AI...")
            progress_bar.progress(20)
            
            # Process with Claude
            summary_content, insights_content = process_pdf_with_claude(uploaded_file)
            
            status_text.text("📝 Creating Word documents...")
            progress_bar.progress(70)
            
            # Create Word documents
            doc1 = create_word_document(
                f"Summary: {uploaded_file.name}",
                summary_content,
                "summary"
            )
            
            doc2 = create_word_document(
                f"Key Insights: {uploaded_file.name}",
                insights_content,
                "insights"
            )
            
            progress_bar.progress(90)
            status_text.text("✅ Documents ready!")
            
            # Store in session state
            st.session_state.doc1_bytes = doc1
            st.session_state.doc2_bytes = doc2
            st.session_state.documents_ready = True
            
            progress_bar.progress(100)
            time.sleep(0.5)
            progress_bar.empty()
            status_text.empty()
            
            st.success("✨ Successfully generated 2 Word documents!")
            
        except Exception as e:
            st.error(f"❌ Error processing PDF: {str(e)}")
            st.session_state.processing = False
        finally:
            st.session_state.processing = False
    
    # Show download buttons if documents are ready
    if st.session_state.documents_ready and st.session_state.doc1_bytes and st.session_state.doc2_bytes:
        st.divider()
        st.subheader("📥 Download Your Documents")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                label="📄 Download Document 1 (Summary)",
                data=st.session_state.doc1_bytes,
                file_name=f"summary_{uploaded_file.name.replace('.pdf', '')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
        
        with col2:
            st.download_button(
                label="📄 Download Document 2 (Key Insights)",
                data=st.session_state.doc2_bytes,
                file_name=f"insights_{uploaded_file.name.replace('.pdf', '')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )

else:
    st.info("👆 Please upload a PDF file to get started")

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: gray;'>
        <small>Powered by Claude AI • Upload any PDF and get two comprehensive Word documents</small>
    </div>
""", unsafe_allow_html=True)
