import streamlit as st

# Page config
st.set_page_config(page_title="Jessup Memorial Penalty Checker", layout="wide")

# Custom CSS
st.markdown("""
<style>
    /* Global styles */
    .stApp { background-color: rgb(249, 250, 251) !important; }
    .main-title { font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem; }
    
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
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
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
    
    /* Status colors */
    .status-success { color: rgb(34, 197, 94); }
    .status-error { color: rgb(239, 68, 68); }
    .status-warning { color: rgb(234, 179, 8); }
    
    /* Table styles */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
    }
    .styled-table th, .styled-table td {
        padding: 0.75rem;
        text-align: left;
        border-bottom: 1px solid #e5e7eb;
    }
    .styled-table tr:hover { background-color: rgb(249, 250, 251); }
    
    /* Progress bar */
    .progress-container {
        width: 100%;
        height: 6px;
        background-color: #e5e7eb;
        border-radius: 9999px;
        margin: 0.25rem 0;
    }
    .progress-bar {
        height: 100%;
        border-radius: 9999px;
        transition: width 0.3s ease;
    }
    
    /* Alert styles */
    .alert {
        padding: 1rem;
        border-radius: 0.375rem;
        margin-bottom: 0.5rem;
    }
    .alert-success { background-color: rgb(240, 253, 244); }
    .alert-error { background-color: rgb(254, 242, 242); }
    .alert-warning { background-color: rgb(255, 251, 235); }
    
    /* Hide Streamlit elements */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stDeployButton { display: none; }
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
                <span class="card-title">{title}</span>
                <span class="card-subtitle">{rule}</span>
            </div>
            {content}
        </div>
    """

def render_progress_bar(count, limit):
    percentage = (count / limit) * 100
    color = "rgb(239, 68, 68)" if percentage > 100 else "rgb(234, 179, 8)" if percentage > 90 else "rgb(34, 197, 94)"
    return f"""
        <div class="progress-container">
            <div class="progress-bar" style="width: {min(percentage, 100)}%; background-color: {color};"></div>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.75rem;">
            <span>{count} words</span>
            <span style="color: {color};">{percentage:.1f}%</span>
        </div>
        <div class="card-subtitle">Limit: {limit}</div>
    """

# Sidebar
with st.sidebar:
    st.markdown("""
        <div class="card">
            <div class="card-subtitle">Penalty Points</div>
            <div style="display: flex; align-items: baseline; gap: 0.25rem; margin-top: 0.5rem;">
                <span style="font-size: 1.875rem; font-weight: 700; color: #ef4444;">10</span>
                <span class="card-subtitle">points</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-title">Jessup Memorial Penalty Checker</h1>', unsafe_allow_html=True)

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

# Two-column layout
col1, col2 = st.columns(2)

# Cover Page Check
with col1:
    st.markdown(render_card(
        "Cover Page Information",
        "Rule 5.6 - 2 points",
        ''.join(f'''
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span>{key}</span>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span class="{'status-success' if value['present'] else 'status-error'}">
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
                    <span class="{'status-success' if present else 'status-error'}">
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

# Other checks
col1, col2 = st.columns(2)

with col1:
    # Anonymity
    st.markdown(render_card(
        "Anonymity",
        "Rule 5.14 - up to 10 points",
        """
        <div class="alert alert-success">
            <span class="status-success">✓</span> No anonymity violations found
            <div class="card-subtitle">No disclosure of school, team members, or country</div>
        </div>
        """
    ), unsafe_allow_html=True)

with col2:
    # Tracked Changes
    st.markdown(render_card(
        "Tracked Changes",
        "Rule 5.4 - up to 5 points",
        """
        <div class="status-success">
            <div>✓ No tracked changes found</div>
            <div>✓ No comments found</div>
        </div>
        """
    ), unsafe_allow_html=True)

with col1:
    # Citations
    st.markdown(render_card(
        "Citations",
        "Rule 5.13 - 1 point per violation, max 5",
        """
        <div class="alert alert-error">
            <span class="status-error">✗</span> Found improper citations
            <div class="card-subtitle">5 instances of improper citation format detected</div>
        </div>
        """
    ), unsafe_allow_html=True)

with col2:
    # Media
    st.markdown(render_card(
        "Media",
        "Rule 5.5(c) - up to 5 points",
        ''.join(f'''
            <div class="alert alert-warning">
                <div>Found in {item["section"]}</div>
                <div class="card-subtitle">{item["text"]}</div>
            </div>
        ''' for item in data["media"])
    ), unsafe_allow_html=True)

# Abbreviations
st.markdown(render_card(
    "Non-Permitted Abbreviations",
    "Rule 5.17 - 1 point each, max 3",
    ''.join(f'''
        <div style="border: 1px solid #e5e7eb; border-radius: 0.5rem; padding: 0.75rem; margin-bottom: 0.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span class="status-error">✗</span>
                    <span style="font-weight: 500;">{abbr}</span>
                    <span class="card-subtitle">
                        ({info["count"]} occurrence{"s" if info["count"] != 1 else ""})
                    </span>
                </div>
            </div>
            <div class="card-subtitle" style="margin-top: 0.5rem;">
                Found in: {", ".join(info["sections"])}
            </div>
        </div>
    ''' for abbr, info in data["abbreviations"].items())
), unsafe_allow_html=True)

# Plagiarism
with col1:
    st.markdown(render_card(
        "Plagiarism",
        "Rule 11.2 - 1-50 points",
        """
        <div class="alert alert-success">
            <span class="status-success">✓</span> No plagiarism detected
        </div>
        """
    ), unsafe_allow_html=True)
