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
    .issue-container {
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        transition: box-shadow 0.2s;
    }
    .issue-container:hover {
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    .issue-header {
        padding: 1.5rem;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    .issue-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #111827;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
    }
    .issue-content {
        border-top: 1px solid #e5e7eb;
    }
    .position-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 0.5rem;
    }
    .evidence-tag {
        background-color: #e0e7ff;
        color: #4338ca;
        padding: 0.25rem 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .category-tag {
        background-color: #f3f4f6;
        color: #4b5563;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .main-argument {
        background-color: #f9fafb;
        padding: 1rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
    }
    .preview-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }
    .preview-section {
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
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
    }
    .chevron {
        color: #9ca3af;
        font-size: 1.5rem;
        padding: 0.5rem;
    }
    div[data-testid="stExpander"] {
        border: none !important;
        box-shadow: none !important;
    }
    .stButton button {
        width: 100%;
        background: none;
        border: none;
        padding: 0;
        text-align: left;
    }
    .stButton button:hover {
        border: none;
        background: none;
    }
    .section-divider {
        border-top: 1px solid #e5e7eb;
    }
    /* Hide default streamlit expander styling */
    .streamlit-expanderHeader {
        background-color: transparent !important;
        font-size: 0 !important;
        padding: 0 !important;
    }
    .streamlit-expanderContent {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

[... rest of the code remains the same until the display section ...]

def create_issue_card(arg):
    """Create an expandable issue card"""
    is_expanded = arg['id'] in st.session_state.expanded_sections
    
    # Create the header section
    st.markdown(f"""
        <div class="issue-container">
            <div class="issue-header" onclick="this.querySelector('button').click();">
                <div style="flex: 1">
                    <div class="issue-title">
                        {arg['issue']}
                        <span class="category-tag">{arg['category']}</span>
                    </div>
                    
                    {'' if is_expanded else f'''
                    <div class="preview-grid">
                        <div class="preview-section">
                            <div class="preview-label appellant">Appellant Position</div>
                            <div class="preview-text">{arg['appellant']['mainArgument']}</div>
                        </div>
                        <div class="preview-section">
                            <div class="preview-label respondent">Respondent Position</div>
                            <div class="preview-text">{arg['respondent']['mainArgument']}</div>
                        </div>
                    </div>
                    '''}
                </div>
                <div class="chevron">
                    {'▼' if is_expanded else '▶'}
                </div>
            </div>
    """, unsafe_allow_html=True)
    
    # Create the expandable button
    if st.button("Toggle", key=f"toggle_{arg['id']}", use_container_width=True):
        toggle_section(arg['id'])
    
    # Show expanded content if section is expanded
    if is_expanded:
        st.markdown('<div class="issue-content">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            create_position_section(arg['appellant'], "Appellant")
        with col2:
            create_position_section(arg['respondent'], "Respondent")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    st.title("Legal Arguments Dashboard")
    
    # Search bar and export button in the same row
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
