import streamlit as st
import pandas as pd
import json
from streamlit.components.v1 import html

# Set page config for wide layout
st.set_page_config(
    page_title="Jessup Memorial Penalty Worksheet",
    page_icon="media/CaseLens Logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.logo("media/CaseLens Logo Sidebar.png", icon_image="media/CaseLens Logo.png", size="large")

# Custom CSS for styling
st.markdown("""
<style>
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
    /* Style for expander headers */
    .streamlit-expanderHeader {
        font-size: 1.3rem !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

[... Previous code for get_case_summary and argument_data remains the same ...]

def create_position_section(position_data, position_type):
    """Create a section for appellant or respondent position"""
    color = "#4F46E5" if position_type == "Appellant" else "#E11D48"
    
    st.markdown(f"""
        <h3 style="color: {color}; font-size: 19.2px;">{position_type}'s Position</h3>
    """, unsafe_allow_html=True)
    
    # Main Argument
    st.markdown(f"""
        <div class="main-argument" style="
            margin: 10px 0; 
            font-size: 1.2rem;
            max-width: 95%;
            line-height: 1.5;
            padding-right: 15px;
        ">
            <strong>{position_data['mainArgument']}</strong>
        </div>
    """, unsafe_allow_html=True)
    
    # Supporting Points
    st.markdown("""
        <div style="margin: 1.5rem 0;">
            <h5 style="margin-bottom: 0;">Supporting Points</h5>
            <ul style="
                list-style-type: none;
                padding-left: 0;
                margin-top: 4px;
                display: flex;
                flex-direction: column;
                gap: 8px;
            ">
    """, unsafe_allow_html=True)
    
    for detail in position_data['details']:
        st.markdown(f"""
            <li style="
                display: flex;
                align-items: flex-start;
                margin-bottom: 0;
                line-height: 1.5;
                padding-right: 20px;
            ">
                <span style="margin-right: 10px;">•</span>
                <span style="flex: 1;">{detail}</span>
            </li>
        """, unsafe_allow_html=True)
    
    st.markdown("</ul></div>", unsafe_allow_html=True)
    
    # Add separation between Supporting Points and Evidence
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    
    # Evidence
    st.markdown("##### Evidence")
    for evidence in position_data['evidence']:
        st.markdown(f"""
            <div class="evidence-card" style="
                display: flex;
                align-items: center;
                padding: 12px 16px;
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                margin-bottom: 8px;
                transition: all 0.2s;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
            ">
                <span style="
                    background-color: #F3F4F6;
                    color: #4B5563;
                    padding: 4px 8px;
                    border-radius: 4px;
                    font-size: 13px;
                    font-weight: 500;
                    margin-right: 12px;
                ">{evidence['id']}</span>
                <a href="/evidence/{evidence['id']}" 
                   style="
                    color: #4B5563;
                    text-decoration: none;
                    font-size: 14px;
                    flex-grow: 1;
                    transition: color 0.2s;
                   "
                   onmouseover="this.style.color='#4D68F9'"
                   onmouseout="this.style.color='#4B5563'"
                >
                    {evidence['desc']}
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    # Add separation between Evidence and Case Law
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    
    # Case Law
    st.markdown("##### Case Law")
    for case in position_data['caselaw']:
        summary = get_case_summary(case)
        st.markdown(f"""
            <div class="position-card" style="margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem;">
                    <div style="flex-grow: 1;">
                        <div style="font-weight: 500; color: #4B5563; margin-bottom: 0.5rem; display: flex; align-items: center;">
                            🗂️ {case} 
                            <a href="/cases/{case}" target="_blank" style="margin-left: 8px; text-decoration: none;">
                                <span style="font-size: 16px; color: #4B5563;">🔗</span>
                            </a>
                        </div>
                        <div style="font-size: 0.875rem; color: #6B7280;">
                            {summary}
                        </div>
                    </div>
                    <button onclick="navigator.clipboard.writeText('{case}')" 
                            style="background: none; border: none; cursor: pointer; padding: 0.25rem;">
                    </button>
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.title("Summary Overview")

    st.title("Summary of Arguments")
    
    # Create a string with all the content to be copied
    copy_content = []
    for arg in argument_data:
        copy_content.append(f"### {arg['issue']} ({arg['category']})")
        copy_content.append("\nAppellant's Position:")
        copy_content.append(f"• {arg['appellant']['mainArgument']}")
        copy_content.append("\nRespondent's Position:")
        copy_content.append(f"• {arg['respondent']['mainArgument']}\n")
    
    copy_text = "\n".join(copy_content)

    # Search bar and copy button in the same row
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        search = st.text_input("", 
                             placeholder="🔍 Search issues, arguments, or evidence...",
                             label_visibility="collapsed")
    with col2:
        # Create a hidden component that will handle the copy functionality
        copy_component = f"""
        <textarea id="copy-text" style="position: absolute; left: -9999px;">{copy_text}</textarea>
        <button
            onclick="copyToClipboard()"
            style="
                width: 100%;
                height: 38px;
                padding: 0 16px;
                background-color: #4D68F9;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 14px;
                font-weight: 500;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                transition: background-color 0.2s;
                margin-top: 4px;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            "
            onmouseover="this.style.backgroundColor='#4558D0'"
            onmouseout="this.style.backgroundColor='#4D68F9'"
        >
            <span style="font-size: 16px;">📋</span>
            <span>Copy</span>
        </button>
        <script>
        function copyToClipboard() {
            const textArea = document.getElementById('copy-text');
            textArea.select();
            document.execCommand('copy');
            const button = document.querySelector('button');
            const originalContent = button.innerHTML;
            button.innerHTML = '<span style="font-size: 16px;">✓</span><span>Copied!</span>';
            setTimeout(() => { button.innerHTML = originalContent; }, 2000);
        }
        </script>
        """
        html(copy_component, height=46)
    
    # Filter arguments based on search
    filtered_arguments = argument_data
    if search:
        search = search.lower()
        filtered_arguments = [
            arg for arg in argument_data
            if (search in arg['issue'].lower() or
                search in arg['category'].lower() or
                any(search in detail.lower() for detail in arg['appellant']['details']) or
                any(search in detail.lower() for detail in arg['respondent']['details']) or
                any(search in e['desc'].lower() for e in arg['appellant']['evidence']) or
                any(search in e['desc'].lower() for e in arg['respondent']['evidence']) or
                any(search in case.lower() for case in arg['appellant']['caselaw']) or
                any(search in case.lower() for case in arg['respondent']['caselaw']))
        ]
    
    # Display arguments
    for arg in filtered_arguments:
        with st.expander(f"{arg['issue']} ({arg['category']})", expanded=arg['id'] == '1'):
            col1, col2 = st.columns([1, 1])
            with col1:
                create_position_section(arg['appellant'], "Appellant")
            with col2:
                create_position_section(arg['respondent'], "Respondent")
            
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
