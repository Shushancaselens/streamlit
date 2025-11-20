import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="CaseLens - Home",
    page_icon="📁",
    layout="wide"
)

# Custom CSS for better styling while keeping Streamlit native
st.markdown("""
    <style>
    .case-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #4CAF50;
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    .case-card:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    .case-header {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1f1f1f;
        margin-bottom: 0.5rem;
    }
    .case-description {
        color: #555;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }
    .case-meta {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        font-size: 0.85rem;
        color: #666;
    }
    .meta-item {
        display: flex;
        align-items: center;
        gap: 0.3rem;
    }
    .status-active { border-left-color: #4CAF50; }
    .status-pending { border-left-color: #FFC107; }
    .status-review { border-left-color: #2196F3; }
    .status-closed { border-left-color: #9E9E9E; }
    
    div[data-testid="stHorizontalBlock"] {
        gap: 1rem;
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
        "description": "Harris FRC Acquisition vs RESEARCH CORPORATION TECHNOLOGIES - Allowed Deductions dispute under License Agreements",
        "documents": 156,
        "date_range": "1999 - 2025",
        "status": "Active",
        "last_updated": "Nov 15, 2024",
        "category": "Arbitration"
    },
    {
        "id": 2,
        "name": "Patent Infringement Case 2",
        "description": "Technology patent dispute involving multiple parties across international jurisdictions",
        "documents": 243,
        "date_range": "2020 - 2025",
        "status": "Active",
        "last_updated": "Nov 18, 2024",
        "category": "Patent Law"
    },
    {
        "id": 3,
        "name": "Contract Dispute Case 3",
        "description": "Commercial contract breach and damages claim with complex financial calculations",
        "documents": 89,
        "date_range": "2021 - 2024",
        "status": "Pending",
        "last_updated": "Nov 10, 2024",
        "category": "Contract Law"
    },
    {
        "id": 4,
        "name": "Trademark Litigation Case 4",
        "description": "Brand trademark infringement proceedings with international brand protection issues",
        "documents": 312,
        "date_range": "2019 - 2025",
        "status": "Active",
        "last_updated": "Nov 19, 2024",
        "category": "IP Law"
    },
    {
        "id": 5,
        "name": "International Arbitration Case 5",
        "description": "ICC International Court of Arbitration dispute resolution for cross-border commercial issues",
        "documents": 178,
        "date_range": "2022 - 2025",
        "status": "In Review",
        "last_updated": "Nov 12, 2024",
        "category": "Arbitration"
    }
]

def get_status_class(status):
    """Get CSS class for status"""
    status_map = {
        "Active": "status-active",
        "Pending": "status-pending",
        "In Review": "status-review",
        "Closed": "status-closed"
    }
    return status_map.get(status, "status-active")

def get_status_emoji(status):
    """Get emoji for status"""
    status_emojis = {
        "Active": "🟢",
        "Pending": "🟡",
        "In Review": "🔵",
        "Closed": "⚫"
    }
    return status_emojis.get(status, "⚪")

def navigate_to_events(case):
    """Navigate to events page with selected case"""
    st.session_state.selected_case = case
    st.session_state.current_page = 'events'
    st.rerun()

def render_case_card(case):
    """Render a single case card using Streamlit native components"""
    
    # Use container with custom styling
    with st.container():
        # Case header with status
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"### 📂 {case['name']}")
        with col2:
            st.markdown(f"{get_status_emoji(case['status'])}")
        
        # Status badge
        st.caption(f"**Status:** {case['status']} • **Category:** {case['category']}")
        
        # Description
        st.markdown(case['description'])
        
        # Metadata in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Documents", case['documents'])
        with col2:
            st.metric("Date Range", case['date_range'])
        with col3:
            st.metric("Last Updated", case['last_updated'])
        
        # Action buttons
        col1, col2, col3 = st.columns([2, 2, 2])
        with col1:
            if st.button("📊 Open Events", key=f"open_{case['id']}", use_container_width=True, type="primary"):
                navigate_to_events(case)
        with col2:
            if st.button("📄 Documents", key=f"docs_{case['id']}", use_container_width=True):
                st.toast(f"Opening documents for {case['name']}", icon="📄")
        with col3:
            if st.button("ℹ️ Details", key=f"details_{case['id']}", use_container_width=True):
                st.toast(f"Case ID: {case['id']}", icon="ℹ️")

def show_home_page():
    """Display the home page with case selection"""
    
    # Header with navigation
    col1, col2, col3 = st.columns([5, 1, 1])
    with col1:
        st.title("📁 CaseLens")
    with col2:
        if st.button("👤 Profile", use_container_width=True):
            st.toast("Opening profile...", icon="👤")
    with col3:
        if st.button("⚙️ Settings", use_container_width=True):
            st.session_state.current_page = 'settings'
            st.rerun()
    
    # User info bar
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**👤 User:** shushan@caselens.tech")
    with col2:
        st.markdown(f"**📁 Total Cases:** {len(cases)}")
    with col3:
        active_cases = len([c for c in cases if c['status'] == 'Active'])
        st.markdown(f"**🟢 Active Cases:** {active_cases}")
    
    st.markdown("---")
    
    # Search and filter section
    col1, col2, col3 = st.columns([4, 2, 2])
    with col1:
        search_query = st.text_input("🔍 Search cases", placeholder="Search by name, description, or category...", label_visibility="collapsed")
    with col2:
        status_filter = st.selectbox("Status", ["All Status", "Active", "Pending", "In Review", "Closed"])
    with col3:
        category_filter = st.selectbox("Category", ["All Categories", "Arbitration", "Patent Law", "Contract Law", "IP Law"])
    
    # Filter cases
    filtered_cases = cases
    if search_query:
        filtered_cases = [c for c in filtered_cases if 
                         search_query.lower() in c['name'].lower() or 
                         search_query.lower() in c['description'].lower() or
                         search_query.lower() in c['category'].lower()]
    if status_filter != "All Status":
        filtered_cases = [c for c in filtered_cases if c['status'] == status_filter]
    if category_filter != "All Categories":
        filtered_cases = [c for c in filtered_cases if c['category'] == category_filter]
    
    # Results count
    st.markdown(f"**Showing {len(filtered_cases)} of {len(cases)} case(s)**")
    st.markdown("---")
    
    # Display cases
    if len(filtered_cases) == 0:
        st.info("🔍 No cases found matching your criteria. Try adjusting your filters.")
    else:
        # Display cases in grid (2 per row)
        for i in range(0, len(filtered_cases), 2):
            cols = st.columns(2, gap="large")
            
            for j, col in enumerate(cols):
                if i + j < len(filtered_cases):
                    case = filtered_cases[i + j]
                    with col:
                        # Add visual separator and render card
                        with st.container(border=True):
                            render_case_card(case)

def show_events_page():
    """Display the events page for selected case"""
    if st.session_state.selected_case is None:
        st.error("No case selected. Returning to home page...")
        st.session_state.current_page = 'home'
        st.rerun()
        return
    
    case = st.session_state.selected_case
    
    # Header with navigation
    col1, col2 = st.columns([5, 1])
    with col1:
        if st.button("← Back to Cases", type="secondary"):
            st.session_state.current_page = 'home'
            st.rerun()
    with col2:
        if st.button("⚙️", use_container_width=True):
            st.session_state.current_page = 'settings'
            st.rerun()
    
    st.title(f"📊 Events - {case['name']}")
    
    # Case info banner
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Status", case['status'])
    with col2:
        st.metric("Documents", case['documents'])
    with col3:
        st.metric("Date Range", case['date_range'])
    with col4:
        st.metric("Category", case['category'])
    
    st.markdown("---")
    
    # Filters and search for events
    col1, col2, col3 = st.columns([4, 2, 2])
    with col1:
        st.text_input("🔍 Search events", placeholder="Search...", key="event_search")
    with col2:
        st.toggle("AI", key="ai_toggle")
    with col3:
        st.button("⬇️ Download", use_container_width=True)
    
    # Tabs for different views
    tab1, tab2 = st.tabs(["📇 Card View", "📊 Table View"])
    
    with tab1:
        st.markdown("### Timeline Events")
        
        # Sample events
        events = [
            {
                "date": "1999-00-00",
                "title": "Definition of Allowed Deductions",
                "description": "In 1999, the definition of 'Allowed Deductions' under the License Agreements between Harris FRC Acquisition, L.P. and RESEARCH CORPORATION TECHNOLOGIES, INC. (Claimants) and UCB PHARMA GmbH., UCB SA, and UCB BIOPHARMA SPRL (Respondents) was established, as referenced by expert Peter A. Lankau in his rebuttal report for Case No. 27850/PDP. This definition, which predates changes in wholesalers' revenue models, is central to the dispute over allowable royalty deductions for products such as VIMPAT and specifies that only expressly enumerated deductions, including certain sales fees, are permitted, with no provision for deducting service fees unless explicitly stated in the agreements.",
                "sources": 1
            },
            {
                "date": "2008-00-00",
                "title": "ICC Arbitration Dispute Initiated",
                "description": "From 2008 to 30 September 2015, a dispute in the ICC International Court of Arbitration (case number 27850/PDP) involves Harris FRC Acquisition, L.P. and RESEARCH CORPORATION TECHNOLOGIES, INC. as claimants and UCB PHARMA GmbH., UCB S.A., and UCB BIOPHARMA SPRL as respondents regarding whether claims for unpaid or underpaid royalties, interest, and fees related to sales of VIMPAT (lacosamide) can be made for the period from 2008 through Q3-2015. The expert report by Sidney P. Blum states that auditable information for this period was generally not provided, contributing to the dispute over including these years in the damages analysis.",
                "sources": 1
            },
            {
                "date": "2008-01-01",
                "title": "Net Sales Reporting Period",
                "description": "From 1 January 2008 to 30 September 2023, UCB PHARMA GmbH., UCB S.A., and UCB BIOPHARMA SPRL reported net sales for VIMPAT (lacosamide) totaling between $12,265,670,572 and $12,616,441,395, as analyzed in the expert report of Sidney P. Blum and used in the ICC International Court of Arbitration proceedings between Harris FRC Acquisition, L.P. and RESEARCH CORPORATION TECHNOLOGIES, INC. (claimants) and UCB PHARMA GmbH., UCB S.A., and UCB BIOPHARMA SPRL (respondents) regarding alleged unpaid and underpaid royalties, interest, and fees.",
                "sources": 2
            }
        ]
        
        for event in events:
            with st.container(border=True):
                col1, col2 = st.columns([1, 5])
                with col1:
                    st.markdown(f"**{event['date']}**")
                with col2:
                    st.markdown(f"**{event['title']}**")
                    st.markdown(event['description'])
                    st.caption(f"🔗 {event['sources']} Source{'s' if event['sources'] > 1 else ''}")
                st.markdown("")
    
    with tab2:
        st.markdown("### Events Table")
        
        import pandas as pd
        sample_data = pd.DataFrame({
            'Date': ['1999-00-00', '2008-00-00', '2008-01-01'],
            'Title': [
                'Definition of Allowed Deductions',
                'ICC Arbitration Dispute Initiated',
                'Net Sales Reporting Period'
            ],
            'Category': ['Legal Definition', 'Dispute', 'Financial'],
            'Sources': [1, 1, 2],
            'Relevance': ['High', 'High', 'Medium']
        })
        st.dataframe(sample_data, use_container_width=True, height=400)
        
        # Export options
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("📊 Export to Excel", use_container_width=True)
        with col2:
            st.button("📄 Export to PDF", use_container_width=True)
        with col3:
            st.button("📋 Copy to Clipboard", use_container_width=True)

def show_settings_page():
    """Display the settings page"""
    
    # Header
    col1, col2 = st.columns([5, 1])
    with col1:
        if st.button("← Back to Home", type="secondary"):
            st.session_state.current_page = 'home'
            st.rerun()
    
    st.title("⚙️ Settings")
    st.markdown("---")
    
    # Account Settings
    st.markdown("### Account Settings")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.text_input("Username / Email", value="shushan@caselens.tech", disabled=True)
    
    st.markdown("---")
    
    # Preferences
    st.markdown("### Preferences")
    
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Theme", ["Light", "Dark", "Auto"])
        st.selectbox("Default View", ["Card View", "Table View"])
    with col2:
        st.selectbox("Language", ["English", "Spanish", "French", "German"])
        st.number_input("Cases per page", min_value=5, max_value=50, value=10)
    
    st.markdown("---")
    
    # Notifications
    st.markdown("### Notifications")
    st.checkbox("Email notifications for case updates", value=True)
    st.checkbox("Desktop notifications", value=False)
    
    st.markdown("---")
    
    # Danger Zone
    st.markdown("### Account Actions")
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("🚪 Log Out", type="primary", use_container_width=True):
            st.success("Logged out successfully!")
            st.balloons()

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
