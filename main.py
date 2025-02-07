import streamlit as st
from datetime import datetime

# Initialize session state
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Overview"
if 'last_check_time' not in st.session_state:
    st.session_state.last_check_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Configure the page with improved metadata
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Jessup Memorial Penalty Checker - Version 2.0"
    }
)

# Enhanced CSS with modern design elements
st.markdown("""
    <style>
    /* Base theme improvements */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Modern card design */
    .card {
        background-color: white;
        border-radius: 0.75rem;
        border: 1px solid #e2e8f0;
        padding: 1.5rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Enhanced header styling */
    .header {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1.25rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 0.75rem;
    }
    
    /* Improved progress bars */
    .stProgress > div > div > div > div {
        height: 0.5rem !important;
        border-radius: 9999px !important;
        transition: width 0.3s ease-in-out;
    }
    
    .progress-success .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #059669 0%, #10B981 100%) !important;
    }
    .progress-warning .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #D97706 0%, #F59E0B 100%) !important;
    }
    .progress-error .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #DC2626 0%, #EF4444 100%) !important;
    }
    
    /* Layout improvements */
    .block-container {
        padding: 2rem !important;
    }
    
    /* Enhanced sidebar */
    [data-testid="stSidebar"] {
        background-color: white;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Interactive menu items */
    .menu-item {
        padding: 0.75rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.2s;
        border: 1px solid transparent;
    }
    .menu-item:hover {
        background-color: #f1f5f9;
        border-color: #e2e8f0;
    }
    .menu-item.active {
        background-color: #e2e8f0;
        border-color: #cbd5e1;
    }
    
    /* Improved tables */
    table {
        border-collapse: separate;
        border-spacing: 0;
        width: 100%;
        border-radius: 0.5rem;
        overflow: hidden;
    }
    
    th, td {
        padding: 0.75rem;
        background: white;
        border-bottom: 1px solid #e2e8f0;
    }
    
    th {
        background: #f8fafc;
        font-weight: 600;
    }
    
    /* Badge styling */
    .badge {
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .badge-success {
        background-color: #dcfce7;
        color: #059669;
    }
    .badge-warning {
        background-color: #fef3c7;
        color: #d97706;
    }
    .badge-error {
        background-color: #fee2e2;
        color: #dc2626;
    }
    
    /* Custom expander styling */
    .streamlit-expanderHeader {
        border-radius: 0.5rem;
        border: 1px solid #e2e8f0;
        background-color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Initial data (preserved from original)
initial_data = {
    "memorialType": "Applicant",
    "coverPage": {
        "Team Number": {"present": True, "found": "349A"},
        "Court Name": {"present": True, "found": "International Court of Justice"},
        "Year": {"present": True, "found": "2025"},
        "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
        "Memorial Type": {"present": True, "found": "Memorial for the Applicant"}
    },
    "memorialParts": {
        "Cover Page": True,
        "Table of Contents": True,
        "Index of Authorities": True,
        "Statement of Jurisdiction": True,
        "Statement of Facts": True,
        "Summary of Pleadings": True,
        "Pleadings": True,
        "Prayer for Relief": False
    },
    "wordCounts": {
        "Statement of Facts": {"count": 1196, "limit": 1200},
        "Summary of Pleadings": {"count": 642, "limit": 700},
        "Pleadings": {"count": 9424, "limit": 9500},
        "Prayer for Relief": {"count": 0, "limit": 200}
    },
    "abbreviations": {
        "ISECR": {"count": 2, "sections": ["Pleadings"]},
        "ICCPED": {"count": 1, "sections": ["Summary of Pleadings"]},
        "ICC": {"count": 1, "sections": ["Pleadings"]},
        "LOSC": {"count": 1, "sections": ["Pleadings"]},
        "AFRC": {"count": 1, "sections": ["Pleadings"]}
    },
    "media": [{"section": "Cover Page", "index": 6, "text": "----media/image1.png----"}]
}

# Enhanced sidebar with better organization
with st.sidebar:
    # Modernized logo and title
    st.markdown("""
        <div style='background: linear-gradient(135deg, #4338ca 0%, #6366f1 100%); 
                    padding: 1.5rem; 
                    border-radius: 0.75rem; 
                    margin-bottom: 1.5rem;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
            <div style='color: white; font-size: 1.75rem; font-weight: 700; margin-bottom: 0.5rem;'>
                ⚖️ Jessup Checker
            </div>
            <div style='color: #e0e7ff; font-size: 0.875rem;'>
                Last checked: {st.session_state.last_check_time}
            </div>
        </div>
    """.format(st.session_state.last_check_time), unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='background-color: white; 
                    padding: 1rem; 
                    border-radius: 0.75rem; 
                    border: 1px solid #e2e8f0;
                    margin-bottom: 1.5rem;'>
            <div style='font-size: 1.25rem; font-weight: 600; color: #1e293b;'>
                Memorandum for the {initial_data['memorialType']}
            </div>
            <div style='color: #64748b; font-size: 0.875rem; margin-top: 0.25rem;'>
                Team #{initial_data['coverPage']['Team Number']['found']}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Enhanced penalty points summary
    total_penalties = sum(p["points"] for p in penalties)
    penalty_color = (
        "#22c55e" if total_penalties == 0
        else "#f59e0b" if total_penalties <= 5
        else "#ef4444"
    )
    
    st.markdown(f"""
        <div style='background-color: white; 
                    padding: 1.25rem; 
                    border-radius: 0.75rem; 
                    border: 1px solid #e2e8f0;
                    margin-bottom: 1.5rem;'>
            <div style='color: #64748b; font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;'>
                Total Penalty Points
            </div>
            <div style='display: flex; align-items: baseline; gap: 0.5rem;'>
                <span style='color: {penalty_color}; font-size: 2rem; font-weight: 700;'>{total_penalties}</span>
                <span style='color: #64748b; font-size: 0.875rem;'>points</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Interactive navigation menu
    menu_items = [
        ("📊", "Overview", "Dashboard summary"),
        ("📄", "Cover Page", "Rule 5.6 - 2 points"),
        ("📋", "Memorial Parts", "Rule 5.5 - 2 points per part"),
        ("📏", "Length Check", "Rule 5.12 - varies"),
        ("🔒", "Anonymity", "Rule 5.14 - up to 10 points"),
        ("📝", "Tracked Changes", "Rule 5.4 - up to 5 points"),
        ("📚", "Citations", "Rule 5.13 - up to 5 points"),
        ("🖼️", "Media", "Rule 5.5(c) - up to 5 points"),
        ("📑", "Abbreviations", "Rule 5.17 - 1 point each, max 3"),
        ("⚠️", "Plagiarism", "Rule 11.2 - 1-50 points")
    ]
    
    for icon, label, description in menu_items:
        is_active = st.session_state.active_tab == label
        st.markdown(f"""
            <div class='menu-item{"" if not is_active else " active"}' 
                 onclick='HandleMenuClick("{label}")'>
                {icon} {label}
                <div style='font-size: 0.75rem; color: #64748b;'>{description}</div>
            </div>
        """, unsafe_allow_html=True)

# Main content area with improved organization
st.markdown("""
    <h1 style='font-size: 2rem; font-weight: 700; color: #1e293b; margin-bottom: 2rem;'>
        Jessup Memorial Penalty Checker
    </h1>
""", unsafe_allow_html=True)

# Enhanced penalty score summary card
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("""
    <div class='header'>
        <span style='color: #ef4444;'>⚠️</span> Penalty Score Summary
    </div>
""", unsafe_allow_html=True)

penalties_df = pd.DataFrame(penalties)
st.dataframe(
    penalties_df,
    column_config={
        "rule": "Rule",
        "description": "Description",
        "points": st.column_config.NumberColumn(
            "Points",
            help="Penalty points assigned",
            format="%d"
        ),
        "r": st.column_config.NumberColumn(
            "Reduced",
            help="Points after reduction",
            format="%d"
        )
    },
    hide_index=True,
    use_container_width=True
)

total_points = penalties_df["points"].sum()
total_r = penalties_df["r"].sum()

st.markdown(f"""
    <div style='display: flex; justify-content: flex-end; gap: 2rem; margin-top: 1rem;'>
        <div>
            <span style='color: #64748b; font-weight: 500;'>Total Points:</span>
            <span style='color: #ef4444; font-weight: 600; margin-left: 0.5rem;'>{total_points}</span>
        </div>
        <div>
            <span style='color: #64748b; font-weight: 500;'>After Reduction:</span>
            <span style='color: #059669; font-weight: 600; margin-left: 0.5rem;'>{total_r}</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Two-column layout with improved spacing
col1, col2 = st.columns(2)

# Enhanced cover page information
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""
        <div class='header'>
            📄 Cover Page Information
            <span style='font-size: 0.75rem; color: #64748b;'>(Rule 5.6 - 2 points)</span>
        </div>
    """, unsafe_allow_html=True)
    
    for key, value in initial_data["coverPage"].items():
        icon = "✅" if value["present"] else "❌"
        st.markdown(f"""
            <div style='display: flex; justify-content: space-between; align-items: center; 
                      padding: 0.75rem; border-bottom: 1px solid #e2e8f0;'>
                <div>
                    <span style='margin-right: 0.5rem;'>{icon}</span>
                    <span style='color: #1e293b; font-weight: 500;'>{key}</span>
                </div>
                <div style='color: #64748b;'>{value["found"]
