import streamlit as st

# Page config
st.set_page_config(page_title="Jessup Memorial Penalty Checker", layout="wide")

# Custom CSS to match React version exactly
st.markdown("""
<style>
    /* Global styles */
    .stApp {
        background-color: rgb(249, 250, 251) !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        width: 18rem !important;
        background-color: white !important;
    }
    [data-testid="stSidebar"] > div {
        background-color: white !important;
    }
    
    /* Card styles */
    .card {
        background-color: white;
        border-radius: 0.5rem;
        padding: 1.5rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    
    .card-header {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding-bottom: 0.75rem;
        margin-bottom: 1rem;
        border-bottom: 1px solid #e5e7eb;
    }
    
    .card-title {
        font-size: 1rem;
        font-weight: 600;
        color: rgb(17, 24, 39);
    }
    
    .card-subtitle {
        font-size: 0.75rem;
        color: rgb(107, 114, 128);
    }
    
    /* Progress bar */
    .progress-bar {
        width: 100%;
        height: 0.375rem;
        background-color: #e5e7eb;
        border-radius: 9999px;
        margin: 0.25rem 0;
        overflow: hidden;
    }
    
    .progress-value {
        height: 100%;
        border-radius: 9999px;
        transition: width 0.3s ease;
    }
    
    /* Status colors */
    .text-success { color: rgb(34, 197, 94); }
    .text-error { color: rgb(239, 68, 68); }
    .text-warning { color: rgb(234, 179, 8); }
    .bg-success { background-color: rgb(34, 197, 94); }
    .bg-error { background-color: rgb(239, 68, 68); }
    .bg-warning { background-color: rgb(234, 179, 8); }
    
    /* Table styles */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .styled-table th,
    .styled-table td {
        padding: 0.75rem;
        text-align: left;
        border-bottom: 1px solid #e5e7eb;
    }
    
    .styled-table th {
        color: rgb(107, 114, 128);
        font-weight: 500;
    }
    
    .styled-table tr:hover {
        background-color: rgb(249, 250, 251);
    }
    
    /* Item styles */
    .check-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.375rem 0;
    }
    
    /* Alert styles */
    .alert {
        padding: 1rem;
        border-radius: 0.375rem;
        display: flex;
        gap: 0.5rem;
        align-items: flex-start;
    }
    
    .alert-success {
        background-color: rgb(240, 253, 244);
        color: rgb(22, 101, 52);
    }
    
    .alert-warning {
        background-color: rgb(255, 251, 235);
        color: rgb(146, 64, 14);
    }
    
    .alert-error {
        background-color: rgb(254, 242, 242);
        color: rgb(153, 27, 27);
    }
    
    /* Abbreviation styles */
    .abbr-item {
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 0.5rem;
    }
    
    .abbr-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .abbr-content {
        margin-top: 0.5rem;
        padding-left: 1.5rem;
        font-size: 0.875rem;
        color: rgb(107, 114, 128);
    }
    
    /* Remove Streamlit's margins */
    .block-container {
        padding-top: 1rem !important;
        max-width: 100rem !important;
    }
    
    /* Hide default elements */
    .stDeployButton { display: none !important; }
    footer { display: none !important; }
    
    /* Override Streamlit's default width */
    .element-container, .stMarkdown {
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# Sample data
data = {
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

def render_card(title, rule, content):
    return f"""
        <div class="card">
            <div class="card-header">
                <div class="card-title">{title}</div>
                {f'<div class="card-subtitle">({rule})</div>' if rule else ''}
            </div>
            {content}
        </div>
    """

def render_progress_bar(count, limit):
    percentage = (count / limit) * 100
    color = "error" if percentage > 100 else "warning" if percentage > 90 else "success"
    return f"""
        <div class="progress-bar">
            <div class="progress-value bg-{color}" style="width: {min(percentage, 100)}%;"></div>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.75rem;">
            <span>{count} words</span>
            <span class="text-{color}">{percentage:.1f}%</span>
        </div>
        <div class="card-subtitle">Limit: {limit}</div>
    """

# Sidebar
with st.sidebar:
    st.markdown("""
        <div class="card">
            <div style="color: #6b7280; font-size: 0.875rem; font-weight: 600;">Penalty Points</div>
            <div style="display: flex; align-items: baseline; gap: 0.25rem; margin-top: 0.5rem;">
                <span style="font-size: 1.875rem; font-weight: 700; color: #ef4444;">10</span>
                <span style="color: #6b7280; font-size: 0.875rem;">points</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown('<h1 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem;">Jessup Memorial Penalty Checker</h1>', unsafe_allow_html=True)

# Score Breakdown
st.markdown(render_card(
    "Penalty Score Summary",
    "",
    f"""
    <table class="styled-table">
        <thead>
            <tr>
                <th>Rule</th>
                <th>Description</th>
                <th style="text-align: center;">A</th>
                <th style="text-align: center;">R</th>
            </tr>
        </thead>
        <tbody>
            {''.join(f'''
                <tr>
                    <td>{p["rule"]}</td>
                    <td>
                        <div>{p["description"]}</div>
                        <div class="card-subtitle">{p["details"]}</div>
                    </td>
                    <td style="text-align: center;">{p["points"]}</td>
                    <td style="text-align: center;">{p["r"]}</td>
                </tr>
            ''' for p in penalties)}
            <tr style="font-weight: 600; background-color: rgb(249, 250, 251);">
                <td colspan="2" style="text-align: right;">TOTAL</td>
                <td style="text-align: center;">10</td>
                <td style="text-align: center;">2</td>
            </tr>
        </tbody>
    </table>
    """
), unsafe_allow_html=True)

# Two-column layout for main content
col1, col2 = st.columns(2)

# Cover Page Check
with col1:
    st.markdown(render_card(
        "Cover Page Information",
        "Rule 5.6 - 2 points",
        ''.join(f'''
            <div class="check-item">
                <span>{key}</span>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span class="text-{'success' if value['present'] else 'error'}">
                        {"✓" if value['present'] else "✗"}
                    </span>
                    <span>{value['found']}</span>
                </div>
            </div>
        ''' for key, value in data["coverPage"].items())
    ), unsafe_allow_html=True)

# Memorial Parts
with col2:
    st.markdown(render_card(
        "Memorial Parts",
        "Rule 5.5 - 2 points per part",
        f"""
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
            {''.join(f'''
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span class="text-{'success' if present else 'error'}">
                        {"✓" if present else "✗"}
                    </span>
                    <span>{part}</span>
                </div>
            ''' for part, present in data["memorialParts"].items())}
        </div>
        """
    ), unsafe_allow_html=True)

# Word Count Analysis
st.markdown(render_card(
    "Word Count Analysis",
    "Rule 5.12",
    f"""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
        {''.join(f'''
            <div>
                <div style="font-weight: 500; margin-bottom: 0.25rem;">{section}</div>
                {render_progress_bar(info["count"], info["limit"])}
            </div>
        ''' for section, info in data["wordCounts"].items())}
    </div>
    """
), unsafe_allow_html=True)

# Create two columns for remaining checks
col1, col2 = st.columns(2)

# Anonymity Check
with col1:
    st.markdown(render_card(
        "Anonymity",
        "Rule 5.14 - up to 10 points",
        """
        <div class="alert alert-success">
            <span class="text-success">✓</span>
            <div>
                <div>No anonymity violations found</div>
                <div class="card-subtitle">No disclosure of school, team members, or country</div>
            </div>
        </div>
        """
    ), unsafe_allow_html=True)

# Tracked Changes
with col2:
    st.markdown(render_card(
        "Tracked Changes",
        "Rule 5.4 - up to 5 points",
        """
        <div class="check-item">
            <span class="text-success">✓ No tracked changes found</span>
        </div>
        <div class="check-item">
            <span class="text-success">✓ No comments found</span>
        </div>
        """
    ), unsafe_allow_html=True)

# Citations
with col1:
    st.markdown(render_card(
        "Citations",
        "Rule 5.13 - 1 point per violation, max 5",
        """
        <div class="alert alert-error">
            <span class="text-error">✗</span>
            <div>
                <div>Found improper citations</div>
                <div class="card-subtitle">5 instances of improper citation format detected</div>
            </div>
        </div>
        """
    ), unsafe_allow_html=True)
1:55
# Media Check
with col2:
    st.markdown(render_card(
        "Media",
        "Rule 5.5(c) - up to 5 points",
        ''.join(f'''
            <div class="alert alert-warning">
                <div>
                    <div>Found in {item["section"]}</div>
                    <div class="card-subtitle">{item["text"]}</div>
                </div>
            </div>
        ''' for item in data["media"])
    ), unsafe_allow_html=True)

# Abbreviations
st.markdown(render_card(
    "Non-Permitted Abbreviations",
    "Rule 5.17 - 1 point each, max 3",
    f"""
    <div class="space-y-2">
        {''.join(f"""
            <div class="abbr-item">
                <div class="abbr-header">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span class="text-error">✗</span>
                        <span style="font-weight: 500;">{abbr}</span>
                        <span class="card-subtitle">
                            ({info['count']} occurrence{'s' if info['count'] != 1 else ''})
                        </span>
                    </div>
                </div>
                <div class="abbr-content">
                    Found in: {', '.join(info['sections'])}
                </div>
            </div>
        """ for abbr, info in data["abbreviations"].items())}
    </div>
    """
), unsafe_allow_html=True)

# Plagiarism
with col1:
    st.markdown(render_card(
        "Plagiarism",
        "Rule 11.2 - 1-50 points",
        """
        <div class="alert alert-success">
            <span class="text-success">✓</span>
            <div>
                <div>No plagiarism detected</div>
            </div>
        </div>
        """
    ), unsafe_allow_html=True)

# Hide Streamlit's default menu and footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
