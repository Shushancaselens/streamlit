import streamlit as st
import pandas as pd

# Configure the page
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to match the React design
st.markdown("""
    <style>
    /* Main layout */
    .main {
        background-color: #f9fafb;
        padding: 1rem;
    }
    
    /* Cards */
    .card {
        background-color: white;
        border-radius: 0.5rem;
        border: 1px solid #e5e7eb;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    /* Typography */
    .title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* Icons */
    .icon-success { color: #10B981; }
    .icon-error { color: #EF4444; }
    .icon-warning { color: #F59E0B; }
    
    /* Progress bars */
    .stProgress > div > div > div > div {
        height: 0.375rem !important;
        border-radius: 9999px !important;
    }
    
    /* Custom grid layout */
    .grid-2 {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: white;
    }
    
    /* Logo */
    .logo {
        height: 3rem;
        margin-bottom: 1rem;
    }
    
    /* Menu items */
    .menu-item {
        display: flex;
        align-items: center;
        padding: 0.5rem;
        margin: 0.25rem 0;
        border-radius: 0.25rem;
        cursor: pointer;
    }
    .menu-item:hover {
        background-color: #f3f4f6;
    }
    .menu-item.active {
        background-color: #e5e7eb;
    }
    
    /* Status indicators */
    .status-dot {
        height: 0.5rem;
        width: 0.5rem;
        border-radius: 9999px;
        margin-right: 0.5rem;
    }
    .status-dot.success { background-color: #10B981; }
    .status-dot.error { background-color: #EF4444; }
    .status-dot.warning { background-color: #F59E0B; }
    
    /* Remove default Streamlit padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for active menu item
if 'active_menu' not in st.session_state:
    st.session_state.active_menu = 'cover'

# Data
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
    }
}

# Sidebar navigation
with st.sidebar:
    # Logo placeholder
    st.markdown("""
        <div style='background-color: #4D68F9; padding: 1rem; border-radius: 0.5rem;'>
            <h1 style='color: white; font-size: 1.25rem;'>Jessup Checker</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### Memorandum for the {initial_data['memorialType']}")
    
    # Penalty points summary
    st.markdown("""
        <div style='background-color: #f3f4f6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;'>
            <p style='color: #4B5563; font-size: 0.875rem; font-weight: 600;'>Penalty Points</p>
            <div style='display: flex; align-items: baseline; gap: 0.25rem;'>
                <span style='color: #DC2626; font-size: 1.5rem; font-weight: 700;'>10</span>
                <span style='color: #6B7280; font-size: 0.875rem;'>points</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation menu
    menu_items = [
        ("📄", "Cover Page", "cover"),
        ("📋", "Memorial Parts", "parts"),
        ("📏", "Length Check", "length"),
        ("🔒", "Anonymity", "anonymity"),
        ("📝", "Tracked Changes", "tracked"),
        ("📚", "Citations", "citations"),
        ("🖼️", "Media", "media"),
        ("📑", "Abbreviations", "abbreviations"),
        ("⚠️", "Plagiarism", "plagiarism")
    ]
    
    for icon, label, key in menu_items:
        is_active = st.session_state.active_menu == key
        st.markdown(
            f"""
            <div class="menu-item{'active' if is_active else ''}"
                 onclick="handleMenuClick('{key}')">
                {icon} {label}
            </div>
            """,
            unsafe_allow_html=True
        )

# Main content
st.title("Jessup Memorial Penalty Checker")

# Penalty Score Summary Card
st.markdown("""
    <div class="card">
        <h3 class="title">Penalty Score Summary</h3>
        <table style="width: 100%;">
            <thead>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <th style="text-align: left;">Rule</th>
                    <th style="text-align: left;">Description</th>
                    <th style="text-align: center;">Points</th>
                    <th style="text-align: center;">Applied</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Rule 5.5</td>
                    <td>Missing Prayer for Relief</td>
                    <td style="text-align: center;">4</td>
                    <td style="text-align: center;">2</td>
                </tr>
                <tr>
                    <td>Rule 5.17</td>
                    <td>Non-Permitted Abbreviations</td>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">3</td>
                </tr>
                <tr>
                    <td>Rule 5.13</td>
                    <td>Improper Citations</td>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">3</td>
                </tr>
                <tr style="font-weight: bold; background-color: #f9fafb;">
                    <td colspan="2" style="text-align: right;">TOTAL</td>
                    <td style="text-align: center;">10</td>
                    <td style="text-align: center;">8</td>
                </tr>
            </tbody>
        </table>
    </div>
""", unsafe_allow_html=True)

# Create two columns for the cards
col1, col2 = st.columns(2)

# Cover Page Information
with col1:
    st.markdown("""
        <div class="card">
            <h3 class="title">Cover Page Information</h3>
    """, unsafe_allow_html=True)
    
    for key, value in initial_data["coverPage"].items():
        icon = "✅" if value["present"] else "❌"
        st.markdown(f"{icon} {key}: {value['found']}")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Memorial Parts
with col2:
    st.markdown("""
        <div class="card">
            <h3 class="title">Memorial Parts</h3>
    """, unsafe_allow_html=True)
    
    parts_cols = st.columns(2)
    items = list(initial_data["memorialParts"].items())
    mid = len(items) // 2
    
    for i, (part, present) in enumerate(items):
        col_idx = 0 if i < mid else 1
        with parts_cols[col_idx]:
            icon = "✅" if present else "❌"
            st.markdown(f"{icon} {part}")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Word Count Analysis
st.markdown("""
    <div class="card">
        <h3 class="title">Word Count Analysis</h3>
    """, unsafe_allow_html=True)

word_count_cols = st.columns(2)
for i, (section, data) in enumerate(initial_data["wordCounts"].items()):
    col_idx = i % 2
    with word_count_cols[col_idx]:
        percentage = (data["count"] / data["limit"]) * 100
        st.markdown(f"**{section}**")
        st.progress(min(percentage / 100, 1.0))
        st.markdown(f"""
            <div style="display: flex; justify-content: space-between;">
                <span>{data['count']} words</span>
                <span style="color: {'#EF4444' if percentage > 100 else '#F59E0B' if percentage > 90 else '#10B981'}">
                    {percentage:.1f}%
                </span>
            </div>
            <div style="font-size: 0.75rem; color: #6B7280;">Limit: {data['limit']}</div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Add JavaScript for handling menu clicks
st.markdown("""
    <script>
    function handleMenuClick(key) {
        window.parent.postMessage({
            type: 'streamlit:set_state',
            state: { active_menu: key }
        }, '*');
    }
    </script>
""", unsafe_allow_html=True)
