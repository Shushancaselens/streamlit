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
    /* Add container max-width style */
    .container {
        max-width: 800px;
        margin: 0 auto;
    }
</style>
""", unsafe_allow_html=True)

[... previous code remains the same until main() function ...]

def main():
    st.title("Legal Arguments Dashboard")
    
    # Container for search and export
    with st.container():
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
    
    # Container for arguments with max-width
    st.markdown('<div class="container">', unsafe_allow_html=True)
    
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
    
    # Close container
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
