import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="CaseLens - Home",
    page_icon="C",
    layout="wide"
)

# Custom CSS for CaseLens blue buttons and tab-style navigation
st.markdown("""
<style>
    /* Primary buttons */
    .stButton > button[kind="primary"] {
        background-color: #4D68F9;
        border-color: #4D68F9;
    }
    .stButton > button[kind="primary"]:hover {
        background-color: #3D58E9;
        border-color: #3D58E9;
    }
    .stButton > button[kind="primary"]:active {
        background-color: #2D48D9;
        border-color: #2D48D9;
    }
    
    /* Navigation tabs styling */
    .nav-tabs {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
        border-bottom: 1px solid #e0e0e0;
        padding-bottom: 10px;
    }
    
    .nav-tab {
        padding: 10px 20px;
        border-radius: 8px;
        background-color: #f0f2f6;
        border: none;
        cursor: pointer;
        font-size: 16px;
        font-weight: 500;
        color: #333;
        transition: all 0.3s;
    }
    
    .nav-tab:hover {
        background-color: #e0e2e6;
    }
    
    .nav-tab.active {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_case' not in st.session_state:
    st.session_state.selected_case = None

# Sample case data (replace with your actual data)
cases = [
    {
        "id": 1,
        "name": "Hanessianadr Case 1",
        "description": "Harris FRC Acquisition vs RESEARCH CORPORATION TECHNOLOGIES",
        "documents": 156,
        "date_range": "1999-01-01 to 2025-09-30",
        "status": "Active",
        "last_updated": "2024-11-15"
    },
    {
        "id": 2,
        "name": "Patent Infringement Case 2",
        "description": "Technology patent dispute involving multiple parties",
        "documents": 243,
        "date_range": "2020-03-15 to 2025-06-30",
        "status": "Active",
        "last_updated": "2024-11-18"
    },
    {
        "id": 3,
        "name": "Contract Dispute Case 3",
        "description": "Commercial contract breach and damages claim",
        "documents": 89,
        "date_range": "2021-07-01 to 2024-12-31",
        "status": "Pending",
        "last_updated": "2024-11-10"
    },
    {
        "id": 4,
        "name": "Trademark Litigation Case 4",
        "description": "Brand trademark infringement proceedings",
        "documents": 312,
        "date_range": "2019-05-20 to 2025-08-15",
        "status": "Active",
        "last_updated": "2024-11-19"
    },
    {
        "id": 5,
        "name": "Arbitration Case 5",
        "description": "International arbitration dispute resolution",
        "documents": 178,
        "date_range": "2022-01-10 to 2025-11-30",
        "status": "In Review",
        "last_updated": "2024-11-12"
    }
]

def navigate_to_events(case):
    """Navigate to events page with selected case"""
    st.session_state.selected_case = case
    st.session_state.current_page = 'events'
    st.rerun()

def show_home_page():
    """Display the home page with case selection"""
    
    # Sidebar with user info
    with st.sidebar:
        st.markdown("**User:** shushan@caselens.tech")
        st.divider()
        if st.button("Settings", use_container_width=True):
            st.session_state.current_page = 'settings'
            st.rerun()
    
    # Header
    st.markdown("### My Cases")
    st.divider()
    
    # Display cases in a grid layout (3 cards per row for smaller cards)
    for i in range(0, len(cases), 3):
        cols = st.columns(3)
        
        for j, col in enumerate(cols):
            if i + j < len(cases):
                case = cases[i + j]
                
                with col:
                    # Create a card using Streamlit native container with border
                    with st.container(border=True):
                        # Clickable case name
                        if st.button(case['name'], key=f"case_{case['id']}", use_container_width=True, type="primary"):
                            navigate_to_events(case)
                        
                        # Case details (compact)
                        st.caption(f"**Status:** {case['status']}")
                        st.caption(f"**Documents:** {case['documents']}")
                        st.caption(f"**Last Updated:** {case['last_updated']}")

def show_events_page():
    """Display the events page for selected case"""
    if st.session_state.selected_case is None:
        st.error("No case selected. Returning to home page...")
        st.session_state.current_page = 'home'
        st.rerun()
        return
    
    case = st.session_state.selected_case
    
    # Sidebar with user info only
    with st.sidebar:
        st.markdown("**User:** shushan@caselens.tech")
    
    # Back button and header
    if st.button("← Back to Cases"):
        st.session_state.current_page = 'home'
        st.rerun()
    
    st.markdown(f"### {case['name']}")
    st.divider()
    
    # Tabs for different views
    tab1, tab2 = st.tabs(["Card View", "Table View"])
    
    with tab1:
        st.markdown("### Card View")
        st.info("This is where your events will be displayed in card format (similar to your second screenshot)")
        
        # Sample events display
        st.markdown("""
        **Event 1999-00-00**  
        In 1999, the definition of "Allowed Deductions" under the License Agreements between Harris FRC Acquisition, L.P. and RESEARCH CORPORATION TECHNOLOGIES, INC...
        
        1 Source
        """)
        
        st.divider()
        
        st.markdown("""
        **Event 2008-00-00**  
        From 2008 to 30 September 2015, a dispute in the ICC International Court of Arbitration (case number 27850/PDP) involves Harris FRC Acquisition...
        
        1 Source
        """)
    
    with tab2:
        st.markdown("### Table View")
        st.info("This is where your events will be displayed in table format")
        
        # Sample table
        import pandas as pd
        sample_data = pd.DataFrame({
            'Date': ['1999-00-00', '2008-00-00', '2008-01-01'],
            'Description': [
                'Definition of Allowed Deductions established',
                'ICC Arbitration case initiated',
                'Net sales reporting period begins'
            ],
            'Sources': [1, 1, 2]
        })
        st.dataframe(sample_data, use_container_width=True)

def show_settings_page():
    """Display the settings page"""
    
    col1, col2 = st.columns([6, 1])
    with col1:
        if st.button("← Back"):
            st.session_state.current_page = 'home'
            st.rerun()
        st.title("Settings")
    
    st.divider()
    
    st.markdown("### Account Settings")
    
    st.markdown("**Username / Email**")
    email = st.text_input("", value="shushan@caselens.tech", disabled=True)
    
    st.divider()
    
    if st.button("Log out", type="primary"):
        st.success("Logged out successfully!")

# Main app logic
def main():
    if st.session_state.current_page == 'home':
        show_home_page()
    elif st.session_state.current_page == 'events':
        show_events_page()
    elif st.session_state.current_page == 'settings':
        show_settings_page()

if __name__ == "__main__":
    main()
