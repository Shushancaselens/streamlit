import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Initialize session state for expanded sections if not exists
if 'expanded_sections' not in st.session_state:
    st.session_state.expanded_sections = {'1'}  # Default first section expanded

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .issue-card {
        background-color: white;
        border-radius: 1rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
        transition: all 0.2s ease-in-out;
    }
    .issue-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    .issue-header {
        padding: 1.5rem;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    .issue-title {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .issue-name {
        font-size: 1.25rem;
        font-weight: 600;
        color: #111827;
    }
    .category-tag {
        background-color: #f3f4f6;
        color: #4b5563;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .dropdown-icon {
        color: #9ca3af;
        font-size: 1.5rem;
        padding: 0.5rem;
        border-radius: 0.5rem;
        transition: all 0.2s ease-in-out;
    }
    .dropdown-icon:hover {
        background-color: #f3f4f6;
    }
    .position-preview {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        padding: 0 1.5rem 1.5rem;
    }
    .preview-section {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }
    .preview-label {
        font-size: 0.875rem;
        font-weight: 500;
    }
    .preview-label.appellant {
        color: rgb(79, 70, 229);
    }
    .preview-label.respondent {
        color: rgb(225, 29, 72);
    }
    .preview-text {
        color: #6b7280;
        font-size: 0.875rem;
        line-height: 1.5;
    }
    .content-section {
        padding: 1.5rem;
        border-top: 1px solid #e5e7eb;
    }
    .evidence-tag {
        background-color: #e0e7ff;
        color: #4338ca;
        padding: 0.25rem 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .main-argument {
        background-color: #f9fafb;
        padding: 1rem;
        border-radius: 0.75rem;
        margin: 1rem 0;
        color: #111827;
        font-weight: 500;
    }
    .section-title {
        color: #4b5563;
        font-size: 0.875rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem;
    }
    .evidence-item {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        margin-bottom: 0.5rem;
        transition: all 0.2s ease-in-out;
    }
    .evidence-item:hover {
        border-color: rgb(79, 70, 229);
        background-color: #f5f7ff;
    }
    .case-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .copy-button {
        color: #9ca3af;
        cursor: pointer;
        padding: 0.25rem;
        border-radius: 0.25rem;
        transition: all 0.2s ease-in-out;
    }
    .copy-button:hover {
        color: rgb(79, 70, 229);
        background-color: #f5f7ff;
    }
    /* Hide Streamlit's default button styling */
    .stButton>button {
        width: 100%;
        background: none;
        border: none;
        padding: 0;
        text-align: left;
    }
    .stButton>button:hover {
        border: none;
        background: none;
    }
    .stButton>button:focus {
        box-shadow: none;
    }
</style>
""", unsafe_allow_html=True)

# Sample data remains the same...
[Previous argument_data remains the same...]

def create_position_section(position_data, position_type):
    """Create a section for appellant or respondent position"""
    st.markdown(f"""
        <div class="section-title">{position_type}'s Position</div>
        <div class="main-argument">{position_data['mainArgument']}</div>
        
        <div class="section-title">Supporting Points</div>
    """, unsafe_allow_html=True)
    
    for detail in position_data['details']:
        st.markdown(f"- {detail}")
    
    st.markdown("""<div class="section-title">Evidence</div>""", unsafe_allow_html=True)
    for evidence in position_data['evidence']:
        st.markdown(f"""
            <div class="evidence-item">
                <span class="evidence-tag">{evidence['id']}</span>
                <span>{evidence['desc']}</span>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""<div class="section-title">Case Law</div>""", unsafe_allow_html=True)
    for case in position_data['caselaw']:
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            st.markdown(f"""
                <div class="case-item">
                    <span>{case}</span>
                    <span class="copy-button">📋</span>
                </div>
            """, unsafe_allow_html=True)

def create_issue_card(arg):
    """Create a collapsible issue card"""
    is_expanded = arg['id'] in st.session_state.expanded_sections
    
    # Header with title and dropdown
    st.markdown(f"""
        <div class="issue-card">
            <div class="issue-header">
                <div>
                    <div class="issue-title">
                        <span class="issue-name">{arg['issue']}</span>
                        <span class="category-tag">{arg['category']}</span>
                    </div>
    """, unsafe_allow_html=True)
    
    # Toggle button
    if st.button(f"{'▼' if is_expanded else '▶'}", key=f"toggle_{arg['id']}"):
        toggle_section(arg['id'])
    
    # Preview or expanded content
    if not is_expanded:
        st.markdown(f"""
            <div class="position-preview">
                <div class="preview-section">
                    <span class="preview-label appellant">Appellant Position</span>
                    <span class="preview-text">{arg['appellant']['mainArgument']}</span>
                </div>
                <div class="preview-section">
                    <span class="preview-label respondent">Respondent Position</span>
                    <span class="preview-text">{arg['respondent']['mainArgument']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""<div class="content-section">""", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            create_position_section(arg['appellant'], "Appellant")
        with col2:
            create_position_section(arg['respondent'], "Respondent")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def main():
    st.title("Legal Arguments Dashboard")
    
    # Search and export section remains the same...
    [Previous search and export code remains the same...]
    
    # Display arguments
    for arg in filtered_arguments:
        create_issue_card(arg)

if __name__ == "__main__":
    main()
