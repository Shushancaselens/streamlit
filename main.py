import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* ... (previous styles remain the same) ... */
    .evidence-link {
        color: #4338ca;
        text-decoration: none;
        transition: all 0.2s;
    }
    .evidence-link:hover {
        color: #3730a3;
        text-decoration: underline;
    }
    .evidence-card {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        margin-bottom: 0.5rem;
        transition: all 0.2s;
    }
    .evidence-card:hover {
        border-color: #818cf8;
        background-color: #f5f7ff;
    }
</style>
""", unsafe_allow_html=True)

[previous case_summaries and argument_data remain exactly the same]

def create_position_section(position_data, position_type):
    """Create a section for appellant or respondent position"""
    [function remains exactly the same]

def create_sidebar():
    """Create and configure the sidebar"""
    with st.sidebar:
        st.header("Dashboard Controls")
        
        # Category Filter
        st.subheader("Filter by Category")
        categories = list(set(arg["category"] for arg in argument_data))
        selected_categories = st.multiselect(
            "Select Categories",
            options=categories,
            default=categories,
            label_visibility="collapsed"
        )
        
        # Case Type Filter
        st.subheader("Filter by Case Type")
        case_types = ["CAS", "Civil", "Patent", "Environmental"]
        selected_case_types = st.multiselect(
            "Select Case Types",
            options=case_types,
            default=case_types,
            label_visibility="collapsed"
        )
        
        # Date Range
        st.subheader("Date Range")
        start_year = st.slider("Start Year", 2017, 2023, 2017)
        
        # Display Settings
        st.subheader("Display Settings")
        show_evidence = st.checkbox("Show Evidence", value=True)
        show_case_law = st.checkbox("Show Case Law", value=True)
        
        # Export Options
        st.subheader("Export Options")
        export_format = st.radio(
            "Export Format",
            options=["CSV", "PDF", "Word"],
            label_visibility="collapsed"
        )
        
        if st.button("Export Document", type="primary", use_container_width=True):
            st.info("Export functionality would go here")
        
        # Help Section
        with st.expander("Help & Information"):
            st.markdown("""
            **Quick Guide:**
            - Use filters to narrow down cases
            - Search for specific terms
            - Export data in various formats
            - Click on evidence links for details
            """)
    
    return selected_categories, selected_case_types, start_year, show_evidence, show_case_law

def main():
    st.title("Legal Arguments Dashboard")
    
    # Initialize sidebar and get filter values
    selected_categories, selected_case_types, start_year, show_evidence, show_case_law = create_sidebar()
    
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
    
    # Filter arguments based on search and sidebar filters
    filtered_arguments = [
        arg for arg in argument_data
        if arg["category"] in selected_categories
    ]
    
    if search:
        search = search.lower()
        filtered_arguments = [
            arg for arg in filtered_arguments
            if (search in arg['issue'].lower() or
                any(search in detail.lower() for detail in arg['appellant']['details']) or
                any(search in detail.lower() for detail in arg['respondent']['details']) or
                any(search in e['desc'].lower() for e in arg['appellant']['evidence']) or
                any(search in e['desc'].lower() for e in arg['respondent']['evidence']))
        ]
    
    # Display arguments
    for arg in filtered_arguments:
        with st.expander(f"{arg['issue']} {arg['category']}", expanded=arg['id'] == '1'):
            # Content when expanded
            col1, col2 = st.columns(2)
            with col1:
                create_position_section(arg['appellant'], "Appellant")
            with col2:
                create_position_section(arg['respondent'], "Respondent")
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
