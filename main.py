import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="CaseLens - Home",
    page_icon="📁",
    layout="wide"
)

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
    
    # Header
    col1, col2 = st.columns([6, 1])
    with col1:
        st.title("📁 CaseLens")
        st.markdown("### My Cases")
    with col2:
        if st.button("⚙️ Settings", use_container_width=True):
            st.session_state.current_page = 'settings'
            st.rerun()
    
    st.divider()
    
    # User info
    st.markdown(f"**User:** shushan@caselens.tech")
    st.markdown(f"**Total Cases:** {len(cases)}")
    
    st.divider()
    
    # Search and filter
    col1, col2 = st.columns([3, 1])
    with col1:
        search_query = st.text_input("🔍 Search cases", placeholder="Search by case name or description...")
    with col2:
        status_filter = st.selectbox("Filter by Status", ["All", "Active", "Pending", "In Review", "Closed"])
    
    # Filter cases based on search and status
    filtered_cases = cases
    if search_query:
        filtered_cases = [c for c in filtered_cases if 
                         search_query.lower() in c['name'].lower() or 
                         search_query.lower() in c['description'].lower()]
    if status_filter != "All":
        filtered_cases = [c for c in filtered_cases if c['status'] == status_filter]
    
    st.markdown(f"**Showing {len(filtered_cases)} case(s)**")
    st.divider()
    
    # Display cases in a grid layout
    if len(filtered_cases) == 0:
        st.info("No cases found matching your criteria.")
    else:
        # Create columns for card layout (2 cards per row)
        for i in range(0, len(filtered_cases), 2):
            cols = st.columns(2)
            
            for j, col in enumerate(cols):
                if i + j < len(filtered_cases):
                    case = filtered_cases[i + j]
                    
                    with col:
                        # Create a card-like container
                        with st.container():
                            st.markdown(f"""
                            <div style="
                                padding: 20px;
                                border-radius: 10px;
                                background-color: #f0f2f6;
                                border: 1px solid #e0e0e0;
                                margin-bottom: 20px;
                            ">
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Case header
                            status_colors = {
                                "Active": "🟢",
                                "Pending": "🟡",
                                "In Review": "🔵",
                                "Closed": "⚫"
                            }
                            
                            st.markdown(f"### 📂 {case['name']}")
                            st.markdown(f"{status_colors.get(case['status'], '⚪')} **Status:** {case['status']}")
                            
                            # Case details
                            st.markdown(f"**Description:** {case['description']}")
                            st.markdown(f"📄 **Documents:** {case['documents']}")
                            st.markdown(f"📅 **Date Range:** {case['date_range']}")
                            st.markdown(f"🕐 **Last Updated:** {case['last_updated']}")
                            
                            # Action buttons
                            col_btn1, col_btn2 = st.columns(2)
                            with col_btn1:
                                if st.button("📊 Open Events", key=f"open_{case['id']}", use_container_width=True):
                                    navigate_to_events(case)
                            with col_btn2:
                                if st.button("ℹ️ Details", key=f"details_{case['id']}", use_container_width=True):
                                    st.info(f"Case ID: {case['id']}\nOpening case details...")
                            
                            st.markdown("---")

def show_events_page():
    """Display the events page for selected case"""
    if st.session_state.selected_case is None:
        st.error("No case selected. Returning to home page...")
        st.session_state.current_page = 'home'
        st.rerun()
        return
    
    case = st.session_state.selected_case
    
    # Header with back button
    col1, col2 = st.columns([6, 1])
    with col1:
        if st.button("← Back to Cases"):
            st.session_state.current_page = 'home'
            st.rerun()
        st.title(f"📊 Events - {case['name']}")
    with col2:
        if st.button("⚙️ Settings", use_container_width=True):
            st.session_state.current_page = 'settings'
            st.rerun()
    
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
        
        🔗 1 Source
        """)
        
        st.divider()
        
        st.markdown("""
        **Event 2008-00-00**  
        From 2008 to 30 September 2015, a dispute in the ICC International Court of Arbitration (case number 27850/PDP) involves Harris FRC Acquisition...
        
        🔗 1 Source
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
        st.title("⚙️ Settings")
    
    st.divider()
    
    st.markdown("### Account Settings")
    
    st.markdown("**Username / Email**")
    email = st.text_input("", value="shushan@caselens.tech", disabled=True)
    
    st.divider()
    
    if st.button("🚪 Log out", type="primary"):
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
