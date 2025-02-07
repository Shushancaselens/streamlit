import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for improved styling
st.markdown("""
    <style>
    /* Global styles */
    .stApp {
        background-color: #f9fafb;
    }
    
    /* Cards */
    .card {
        background-color: white;
        border-radius: 0.5rem;
        border: 1px solid #e5e7eb;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: white;
        border-right: 1px solid #e5e7eb;
    }
    
    /* Headers */
    .header {
        font-size: 1.25rem;
        font-weight: 600;
        color: #111827;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Status indicators */
    .success { color: #10B981; }
    .error { color: #EF4444; }
    .warning { color: #F59E0B; }
    
    /* Progress bars */
    .stProgress > div > div > div > div {
        height: 0.375rem !important;
        border-radius: 9999px !important;
    }
    .progress-success .stProgress > div > div > div > div {
        background-color: #10B981 !important;
    }
    .progress-warning .stProgress > div > div > div > div {
        background-color: #F59E0B !important;
    }
    .progress-error .stProgress > div > div > div > div {
        background-color: #EF4444 !important;
    }
    
    /* Tables */
    .styled-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
    }
    .styled-table th {
        text-align: left;
        padding: 0.75rem;
        border-bottom: 1px solid #e5e7eb;
        color: #6B7280;
        font-weight: 500;
    }
    .styled-table td {
        padding: 0.75rem;
        border-bottom: 1px solid #e5e7eb;
    }
    .styled-table tr:hover {
        background-color: #f9fafb;
    }
    
    /* Expandable sections */
    .expandable {
        border: 1px solid #e5e7eb;
        border-radius: 0.375rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
        cursor: pointer;
    }
    .expandable:hover {
        background-color: #f9fafb;
    }
    </style>
""", unsafe_allow_html=True)

# Initial data (keeping exactly the same as React version)
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

penalties = [
    {"rule": "Rule 5.5", "description": "Missing Prayer for Relief", "points": 4, "r": 2, "details": "2 points per part"},
    {"rule": "Rule 5.17", "description": "Non-Permitted Abbreviations (5 found)", "points": 3, "r": 0, "details": "1 point each, max 3"},
    {"rule": "Rule 5.13", "description": "Improper Citation", "points": 3, "r": 0, "details": "1 point per violation, max 5"}
]

# Sidebar
with st.sidebar:
    # Logo
    st.markdown("""
        <div style='background-color: #4D68F9; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;'>
            <h1 style='color: white; font-size: 1.5rem;'>Jessup Checker</h1>
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
        ("📄", "Cover Page", "Rule 5.6", "2 points"),
        ("📋", "Memorial Parts", "Rule 5.5", "2 points per part"),
        ("📏", "Length Check", "Rule 5.12", "varies"),
        ("🔒", "Anonymity", "Rule 5.14", "up to 10 points"),
        ("📝", "Tracked Changes", "Rule 5.4", "up to 5 points"),
        ("📚", "Citations", "Rule 5.13", "up to 5 points"),
        ("🖼️", "Media", "Rule 5.5(c)", "up to 5 points"),
        ("📑", "Abbreviations", "Rule 5.17", "1 point each, max 3"),
        ("⚠️", "Plagiarism", "Rule 11.2", "1-50 points")
    ]
    
    for icon, label, rule, points in menu_items:
        st.button(
            f"{icon} {label}\n{rule} - {points}",
            key=f"nav_{label.lower().replace(' ', '_')}"
        )

# Main content
st.title("Jessup Memorial Penalty Checker")

# Penalty Score Summary
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("""
    <div class='header'>
        <span style='color: #EF4444;'>⚠️</span> Penalty Score Summary
    </div>
""", unsafe_allow_html=True)

# Create penalty summary table
penalty_data = []
total_points = 0
total_r = 0

for penalty in penalties:
    penalty_data.append([
        penalty["rule"],
        f"{penalty['description']}\n{penalty['details']}",
        penalty["points"],
        penalty["r"]
    ])
    total_points += penalty["points"]
    total_r += penalty["r"]

# Use columns to create table-like layout
col1, col2, col3, col4 = st.columns([2, 4, 1, 1])
col1.markdown("**Rule**")
col2.markdown("**Description**")
col3.markdown("**A**")
col4.markdown("**R**")

for row in penalty_data:
    col1.text(row[0])
    col2.markdown(row[1])
    col3.markdown(f"**{row[2]}**")
    col4.markdown(f"**{row[3]}**")

# Total row
st.markdown("---")
col1, col2, col3, col4 = st.columns([2, 4, 1, 1])
col2.markdown("**TOTAL**")
col3.markdown(f"**{total_points}**")
col4.markdown(f"**{total_r}**")

st.markdown("</div>", unsafe_allow_html=True)

# Create two columns for the layout
col1, col2 = st.columns(2)

# Cover Page Information
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""
        <div class='header'>
            Cover Page Information
            <span class='text-gray-500 text-sm'>(Rule 5.6 - 2 points)</span>
        </div>
    """, unsafe_allow_html=True)
    
    for key, value in initial_data["coverPage"].items():
        icon = "✅" if value["present"] else "❌"
        st.markdown(f"{icon} {key}: {value['found']}")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Memorial Parts
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""
        <div class='header'>
            Memorial Parts
            <span class='text-gray-500 text-sm'>(Rule 5.5 - 2 points per part)</span>
        </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    items = list(initial_data["memorialParts"].items())
    mid = len(items) // 2
    
    for i, (part, present) in enumerate(items):
        col_idx = 0 if i < mid else 1
        with cols[col_idx]:
            icon = "✅" if present else "❌"
            st.markdown(f"{icon} {part}")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Word Count Analysis
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("""
    <div class='header'>
        <span style='color: #F59E0B;'>⚠️</span> Excessive Length
        <span class='text-gray-500 text-sm'>(Rule 5.12)</span>
    </div>
""", unsafe_allow_html=True)

word_count_cols = st.columns(2)
for i, (section, data) in enumerate(initial_data["wordCounts"].items()):
    col_idx = i % 2
    with word_count_cols[col_idx]:
        percentage = (data["count"] / data["limit"]) * 100
        st.markdown(f"**{section}**")
        
        # Choose progress bar color based on percentage
        progress_class = "progress-success"
        if percentage > 100:
            progress_class = "progress-error"
        elif percentage > 90:
            progress_class = "progress-warning"
        
        st.markdown(f"<div class='{progress_class}'>", unsafe_allow_html=True)
        st.progress(min(percentage / 100, 1.0))
        st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 2])
        col1.text(f"{data['count']} words")
        col2.markdown(
            f"<span style='color: {'#EF4444' if percentage > 100 else '#F59E0B' if percentage > 90 else '#10B981'}'>{percentage:.1f}%</span>",
            unsafe_allow_html=True
        )
        st.markdown(f"<span style='color: #6B7280; font-size: 0.75rem;'>Limit: {data['limit']}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Abbreviations
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("""
    <div class='header'>
        <span style='color: #EF4444;'>⚠️</span> Non-Permitted Abbreviations
        <span class='text-gray-500 text-sm'>(Rule 5.17 - 1 point each, max 3)</span>
    </div>
""", unsafe_allow_html=True)

for abbr, info in initial_data["abbreviations"].items():
    with st.expander(f"❌ {abbr} ({info['count']} occurrence{'s' if info['count'] > 1 else ''})"):
        st.markdown(f"Found in: {', '.join(info['sections'])}")

st.markdown("</div>", unsafe_allow_html=True)

# Additional sections (Anonymity, Citations, etc.)
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("""
    <div class='header'>
        <span style='color: #10B981;'>✅</span> Anonymity
        <span class='text-gray-500 text-sm'>(Rule 5.14 - up to 10 points)</span>
    </div>
""", unsafe_allow_html=True)
st.success("No anonymity violations found")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("""
    <div class='header'>
        <span style='color: #EF4444;'>⚠️</span> Citations
        <span class='text-gray-500 text-sm'>(Rule 5.13 - 1
