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

[... previous functions and data remain exactly the same ...]

def main():
    # Sidebar with only logo
    with st.sidebar:
        # Logo
        st.markdown("""
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <svg width="40" height="40" viewBox="0 0 175 175" xmlns="http://www.w3.org/2000/svg">
                    <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
                        <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
                    </mask>
                    <g mask="url(#whatsapp-mask)">
                        <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
                    </g>
                </svg>
            </div>
        """, unsafe_allow_html=True)

    st.title("Legal Arguments Dashboard")
    
    # Top section with filters and controls
    col1, col2, col3, col4 = st.columns([0.4, 0.2, 0.2, 0.2])
    
    # Search in first column
    with col1:
        search = st.text_input("", 
                             placeholder="🔍 Search issues, arguments, or evidence...",
                             label_visibility="collapsed")
    
    # Category filter in second column
    with col2:
        categories = list(set(arg["category"] for arg in argument_data))
        selected_categories = st.multiselect(
            "Category",
            categories,
            default=categories
        )
    
    # Issue count in third column
    with col3:
        st.metric("Total Issues", len(argument_data))
    
    # Export buttons in fourth column
    with col4:
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
    
    # Filter arguments based on search and categories
    filtered_arguments = [arg for arg in argument_data if arg["category"] in selected_categories]
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
