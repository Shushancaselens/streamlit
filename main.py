import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Component spacing and sizing */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .section-spacing {
        margin: 2rem 0;
    }
    
    .component-spacing {
        margin: 1.5rem 0;
    }
    
    /* Evidence styling */
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
        max-width: 90%;
    }
    
    .evidence-card:hover {
        border-color: #818cf8;
        background-color: #f5f7ff;
    }
    
    /* Position card styling */
    .position-card {
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        padding: 1rem;
        margin-bottom: 1rem;
        max-width: 90%;
    }
    
    /* Main argument styling */
    .main-argument {
        background-color: #f3f4f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        max-width: 90%;
    }
    
    /* Divider styling */
    .divider {
        border-top: 1px solid #e5e7eb;
        margin: 2rem 0;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #f9fafb;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

[Previous code remains the same from here until the create_position_section function]

def create_position_section(position_data, position_type):
    """Create a section for appellant or respondent position"""
    color = "indigo" if position_type == "Appellant" else "rose"
    
    st.markdown(f"""
        <div class="component-spacing">
            <h3>{position_type}'s Position</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Main Argument
    st.markdown(f"""
        <div class="main-argument">
            <strong>{position_data['mainArgument']}</strong>
        </div>
    """, unsafe_allow_html=True)
    
    # Supporting Points
    st.markdown("""
        <div class="component-spacing">
            <h5>Supporting Points</h5>
        </div>
    """, unsafe_allow_html=True)
    for detail in position_data['details']:
        st.markdown(f"- {detail}")
    
    # Evidence
    st.markdown("""
        <div class="component-spacing">
            <h5>Evidence</h5>
        </div>
    """, unsafe_allow_html=True)
    for evidence in position_data['evidence']:
        st.markdown(f"""
            <div class="evidence-card">
                <span class="evidence-tag">{evidence['id']}</span>
                <a href="/evidence/{evidence['id']}" class="evidence-link" target="_blank">
                    {evidence['desc']}
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    # Case Law
    st.markdown("""
        <div class="component-spacing">
            <h5>Case Law</h5>
        </div>
    """, unsafe_allow_html=True)
    for case in position_data['caselaw']:
        summary = get_case_summary(case)
        st.markdown(f"""
            <div class="position-card">
                <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem;">
                    <div style="flex-grow: 1;">
                        <div style="font-weight: 500; color: #4B5563; margin-bottom: 0.5rem;">
                            {case}
                        </div>
                        <div style="font-size: 0.875rem; color: #6B7280;">
                            {summary}
                        </div>
                    </div>
                    <button onclick="navigator.clipboard.writeText('{case}')" 
                            style="background: none; border: none; cursor: pointer; padding: 0.25rem;">
                        📋
                    </button>
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    st.markdown("""
        <div class="main-container">
            <h1>Legal Arguments Dashboard</h1>
        </div>
    """, unsafe_allow_html=True)
    
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
    
    st.markdown("<div class='section-spacing'></div>", unsafe_allow_html=True)
    
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
        with st.expander(f"{arg['issue']} {arg['category']}", expanded=arg['id'] == '1'):
            st.markdown("<div class='component-spacing'></div>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                create_position_section(arg['appellant'], "Appellant")
            with col2:
                create_position_section(arg['respondent'], "Respondent")
            st.markdown("<div class='component-spacing'></div>", unsafe_allow_html=True)
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
