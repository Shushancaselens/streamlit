import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .stTable {
        font-size: 14px;
    }
    .evidence-tag {
        background-color: #E5E7EB;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 12px;
        color: #4B5563;
    }
    .main-argument {
        font-weight: 500;
        color: #1F2937;
    }
    .details-cell {
        color: #4B5563;
    }
    .evidence-cell {
        color: #4338CA;
    }
    .case-cell {
        color: #1F2937;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Add sidebar with logo and info
    with st.sidebar:
        # Add the logo SVG
        st.markdown("""
        <svg width="40" height="40" viewBox="0 0 175 175" xmlns="http://www.w3.org/2000/svg">
          <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
            <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
          </mask>
          <g mask="url(#whatsapp-mask)">
            <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
          </g>
        </svg>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.info(
            """
            This dashboard displays legal arguments and related case law.
            """
        )

    # Rest of your code remains exactly the same
    st.title("Legal Arguments Dashboard - Table View")
    
    # Add view toggle
    view_type = st.radio("Select View", ["Detailed Table", "Summary Table"], horizontal=True)
    
    # Search bar and export button in the same row
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        search = st.text_input("", 
                             placeholder="🔍 Search issues, arguments, or evidence...",
                             label_visibility="collapsed")
    with col2:
        if st.button("📋 Export Data", type="primary", use_container_width=True):
            df = create_table_data()
            st.download_button(
                "Download Full Data",
                df.to_csv(index=False),
                "legal_arguments_table.csv",
                "text/csv",
                use_container_width=True
            )
    
    # Create and filter table data
    df = create_table_data()
    
    if search:
        search = search.lower()
        mask = df.apply(lambda x: x.astype(str).str.lower().str.contains(search).any(), axis=1)
        df = df[mask]
    
    # Display based on view type
    if view_type == "Summary Table":
        summary_df = df[["issue", "appellant_position", "respondent_position"]]
        st.dataframe(
            summary_df,
            use_container_width=True,
            column_config={
                "issue": st.column_config.TextColumn("Issue", width="medium"),
                "appellant_position": st.column_config.TextColumn("Appellant Position", width="large"),
                "respondent_position": st.column_config.TextColumn("Respondent Position", width="large")
            }
        )
    else:
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "issue": st.column_config.TextColumn("Issue", width="medium"),
                "appellant_position": st.column_config.TextColumn("Appellant Position", width="large"),
                "appellant_details": st.column_config.TextColumn("Appellant Details", width="large"),
                "appellant_evidence": st.column_config.TextColumn("Appellant Evidence", width="large"),
                "appellant_cases": st.column_config.TextColumn("Appellant Case Law", width="large"),
                "respondent_position": st.column_config.TextColumn("Respondent Position", width="large"),
                "respondent_details": st.column_config.TextColumn("Respondent Details", width="large"),
                "respondent_evidence": st.column_config.TextColumn("Respondent Evidence", width="large"),
                "respondent_cases": st.column_config.TextColumn("Respondent Case Law", width="large")
            }
        )

# Keep all other functions (get_case_summary, create_table_data, etc.) exactly the same
# ... (rest of the code remains unchanged)

if __name__ == "__main__":
    main()
