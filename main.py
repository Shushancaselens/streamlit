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
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
        gap: 0rem !important;
    }
    button[data-testid="baseButton-header"] {
        width: 100%;
        border: none !important;
        padding: 0 !important;
        background-color: transparent !important;
    }
    button[data-testid="baseButton-header"]:hover {
        border: none !important;
        background-color: transparent !important;
    }
    button[data-testid="baseButton-header"]:focus {
        box-shadow: none !important;
    }
    .header-container {
        background-color: white;
        padding: 1.5rem;
        border: 1px solid #e5e7eb;
        border-radius: 1rem;
        margin-bottom: 1rem;
        transition: all 0.2s ease;
        cursor: pointer;
    }
    .header-container:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    .header-content {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    .title-section {
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
    }
    .title-row {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    .issue-title {
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
    .chevron {
        color: #9ca3af;
        font-size: 1.5rem;
        padding: 0.5rem;
        border-radius: 0.5rem;
        transition: transform 0.2s ease;
    }
    .chevron.expanded {
        transform: rotate(180deg);
    }
    .preview-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-top: 0.75rem;
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
        background-color: white;
        border: 1px solid #e5e7eb;
        border-top: none;
        border-radius: 0 0 1rem 1rem;
        margin-top: -1rem;
        padding: 1.5rem;
        animation: slideDown 0.2s ease-out;
    }
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
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
        transition: all 0.2s ease;
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
</style>
""", unsafe_allow_html=True)

def toggle_section(section_id):
    """Toggle the expanded/collapsed state of a section"""
    if section_id in st.session_state.expanded_sections:
        st.session_state.expanded_sections.remove(section_id)
    else:
        st.session_state.expanded_sections.add(section_id)

# Sample argument_data remains the same...

def create_header(arg, is_expanded):
    """Create a header section with dropdown"""
    header_html = f"""
    <div class="header-container">
        <div class="header-content">
            <div class="title-section">
                <div class="title-row">
                    <span class="issue-title">{arg['issue']}</span>
                    <span class="category-tag">{arg['category']}</span>
                </div>
                {'' if is_expanded else f'''
                <div class="preview-grid">
                    <div class="preview-section">
                        <span class="preview-label appellant">Appellant Position</span>
                        <span class="preview-text">{arg['appellant']['mainArgument']}</span>
                    </div>
                    <div class="preview-section">
                        <span class="preview-label respondent">Respondent Position</span>
                        <span class="preview-text">{arg['respondent']['mainArgument']}</span>
                    </div>
                </div>
                '''}
            </div>
            <div class="chevron{'expanded' if is_expanded else ''}">
                {'▼' if is_expanded else '▶'}
            </div>
        </div>
    </div>
    """
    if st.button(header_html, key=f"header_{arg['id']}", use_container_width=True):
        toggle_section(arg['id'])

def create_content(arg):
    """Create the expanded content section"""
    st.markdown("""<div class="content-section">""", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Appellant's Position")
        st.markdown(f"""<div class="main-argument">{arg['appellant']['mainArgument']}</div>""", 
                   unsafe_allow_html=True)
        
        st.markdown("#### Supporting Points")
        for point in arg['appellant']['details']:
            st.markdown(f"- {point}")
        
        st.markdown("#### Evidence")
        for evidence in arg['appellant']['evidence']:
            st.markdown(f"""
                <div class="evidence-item">
                    <span class="evidence-tag">{evidence['id']}</span>
                    <span>{evidence['desc']}</span>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Respondent's Position")
        st.markdown(f"""<div class="main-argument">{arg['respondent']['mainArgument']}</div>""", 
                   unsafe_allow_html=True)
        
        st.markdown("#### Supporting Points")
        for point in arg['respondent']['details']:
            st.markdown(f"- {point}")
        
        st.markdown("#### Evidence")
        for evidence in arg['respondent']['evidence']:
            st.markdown(f"""
                <div class="evidence-item">
                    <span class="evidence-tag">{evidence['id']}</span>
                    <span>{evidence['desc']}</span>
                </div>
            """, unsafe_allow_html=True)

def create_issue_card(arg):
    """Create a complete issue card with header and content"""
    is_expanded = arg['id'] in st.session_state.expanded_sections
    
    create_header(arg, is_expanded)
    if is_expanded:
        create_content(arg)

def main():
    st.title("Legal Arguments Dashboard")
    
    # Search bar and export button
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        search = st.text_input("", 
                             placeholder="🔍 Search issues, arguments, or evidence...",
                             label_visibility="collapsed")
    with col2:
        if st.button("📋 Export Summary", type="primary", use_container_width=True):
            summary_data = []
            for arg in argument_data:
                summary_data.append({
                    "Issue": arg["issue"],
                    "Appellant Position": arg["appellant"]["mainArgument"],
                    "Respondent Position": arg["respondent"]["mainArgument"]
                })
            df = pd.DataFrame(summary_data)
            st.download_button(
                "Download Summary",
                df.to_csv(index=False),
                "legal_arguments_summary.csv",
                "text/csv",
                use_container_width=True
            )
    
    # Filter arguments based on search
    filtered_arguments = argument_data
    if search:
        search = search.lower()
        filtered_arguments = [
            arg for arg in argument_data
            if (search in arg['issue'].lower() or
                any(search in detail.lower() for detail in arg['appellant']['details']) or
                any(search in detail.lower() for detail in arg['respondent']['details']) or
                any(search in e['desc'].lower() for e in arg['appellant']['evidence']) or
                any(search in e['desc'].lower() for e in arg['respondent']['evidence']))
        ]
    
    # Display arguments
    for arg in filtered_arguments:
        create_issue_card(arg)

if __name__ == "__main__":
    main()
