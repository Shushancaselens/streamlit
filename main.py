import streamlit as st
import pandas as pd
from pathlib import Path

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initial data setup
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

# Custom CSS for styling
st.markdown("""
<style>
    .custom-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .status-success { color: #4CAF50; }
    .status-error { color: #EF5350; }
    .status-warning { color: #FFA726; }
    .nav-item {
        padding: 0.5rem;
        border-radius: 0.25rem;
        margin-bottom: 0.5rem;
        background-color: #f8f9fa;
    }
    .section-header {
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .small-text { font-size: 0.875rem; }
    .very-small-text { font-size: 0.75rem; }
</style>
""", unsafe_allow_html=True)

def create_card(title, content, rule=None, points=None):
    header = title
    if rule and points:
        header += f' <span class="very-small-text text-muted">({rule} - {points})</span>'
    
    st.markdown(f"""
    <div class="custom-card">
        <div class="section-header">{header}</div>
        {content}
    </div>
    """, unsafe_allow_html=True)

def create_word_count_bar(count, limit):
    percentage = (count / limit) * 100
    color = "#4CAF50"  # green
    if percentage > 90:
        color = "#FFA726"  # orange
    if percentage > 100:
        color = "#EF5350"  # red
    
    st.markdown(f"""
    <div class="small-text">
        <div style="display: flex; justify-content: space-between;">
            <span>{count} words</span>
            <span style="color: {color}">{percentage:.1f}%</span>
        </div>
        <div style="background-color: #f0f0f0; height: 6px; border-radius: 3px; margin: 4px 0;">
            <div style="width: {min(percentage, 100)}%; height: 100%; background-color: {color}; border-radius: 3px;"></div>
        </div>
        <div class="very-small-text text-muted">Limit: {limit}</div>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Sidebar Navigation
    with st.sidebar:
        st.title("Jessup Penalty Checker")
        st.markdown(f"### Memorandum for the {initial_data['memorialType']}")
        
        # Penalty Points Display
        st.markdown("""
        <div class="custom-card">
            <div class="small-text text-muted">Penalty Points</div>
            <div style="font-size: 2rem; color: #dc3545; font-weight: bold;">10</div>
            <div class="very-small-text text-muted">points</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation Items
        for section in [
            ("📄", "Cover Page", "Rule 5.6", "2 points"),
            ("✓", "Memorial Parts", "Rule 5.5", "2 points per part"),
            ("📏", "Length Check", "Rule 5.12", "varies"),
            ("🔒", "Anonymity", "Rule 5.14", "up to 10 points"),
            ("📝", "Tracked Changes", "Rule 5.4", "up to 5 points"),
            ("📚", "Citations", "Rule 5.13", "up to 5 points"),
            ("🖼️", "Media", "Rule 5.5(c)", "up to 5 points"),
            ("📑", "Abbreviations", "Rule 5.17", "1 point each, max 3"),
            ("🔍", "Plagiarism", "Rule 11.2", "1-50 points")
        ]:
            st.markdown(f"""
            <div class="nav-item">
                <div>{section[0]} {section[1]}</div>
                <div class="very-small-text text-muted">{section[2]} - {section[3]}</div>
            </div>
            """, unsafe_allow_html=True)

    # Main Content
    st.title("Jessup Memorial Penalty Checker")

    # Score Breakdown
    with st.expander("Penalty Score Summary", expanded=True):
        penalties = [
            ("Rule 5.5", "Missing Prayer for Relief", 4, 2, "2 points per part"),
            ("Rule 5.17", "Non-Permitted Abbreviations (5 found)", 3, 0, "1 point each, max 3"),
            ("Rule 5.13", "Improper Citation", 3, 0, "1 point per violation, max 5")
        ]
        
        st.markdown("""
        <div class="custom-card">
            <table style="width: 100%;">
                <thead>
                    <tr style="border-bottom: 1px solid #eee;">
                        <th>Rule</th>
                        <th>Description</th>
                        <th style="text-align: center;">A</th>
                        <th style="text-align: center;">R</th>
                    </tr>
                </thead>
                <tbody>
        """, unsafe_allow_html=True)
        
        for rule, desc, points, r, details in penalties:
            st.markdown(f"""
                <tr style="border-bottom: 1px solid #eee;">
                    <td style="color: #666;">{rule}</td>
                    <td>
                        <div>{desc}</div>
                        <div class="very-small-text text-muted">{details}</div>
                    </td>
                    <td style="text-align: center;">{points}</td>
                    <td style="text-align: center;">{r}</td>
                </tr>
            """, unsafe_allow_html=True)
        
        st.markdown("""
                <tr style="background-color: #f8f9fa; font-weight: bold;">
                    <td colspan="2" style="text-align: right; padding-right: 1rem;">TOTAL</td>
                    <td style="text-align: center;">10</td>
                    <td style="text-align: center;">2</td>
                </tr>
            </tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

    # Content Grid
    col1, col2 = st.columns(2)

    # Cover Page Check
    with col1:
        content = ""
        for key, value in initial_data["coverPage"].items():
            icon = "✅" if value["present"] else "❌"
            content += f"""
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span>{key}</span>
                <span>{icon} {value["found"]}</span>
            </div>
            """
        create_card("Cover Page Information", content, "Rule 5.6", "2 points")

    # Memorial Parts
    with col2:
        content = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">'
        for part, present in initial_data["memorialParts"].items():
            icon = "✅" if present else "❌"
            content += f'<div>{icon} {part}</div>'
        content += '</div>'
        create_card("Memorial Parts", content, "Rule 5.5", "2 points per part")

    # Word Count Analysis
    st.markdown("""
    <div class="custom-card">
        <div class="section-header">
            ⚠️ Excessive Length
            <span class="very-small-text text-muted">(Rule 5.12)</span>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
    """, unsafe_allow_html=True)
    
    for section, data in initial_data["wordCounts"].items():
        st.markdown(f"""
        <div>
            <div class="small-text" style="margin-bottom: 0.25rem;">{section}</div>
        """, unsafe_allow_html=True)
        create_word_count_bar(data["count"], data["limit"])
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

    # Additional Sections Grid
    col1, col2 = st.columns(2)

    with col1:
        # Anonymity Check
        create_card("Anonymity", """
            <div class="status-success">
                ✅ No anonymity violations found
                <div class="very-small-text" style="margin-top: 0.25rem;">
                    No disclosure of school, team members, or country
                </div>
            </div>
        """, "Rule 5.14", "up to 10 points")

        # Citations
        create_card("Citations", """
            <div class="status-warning">
                ⚠️ 5 instances of improper citation format detected
            </div>
        """, "Rule 5.13", "1 point per violation, max 5")

        # Media Check
        media_content = ""
        for item in initial_data["media"]:
            media_content += f"""
            <div class="status-warning" style="margin-bottom: 0.5rem;">
                <div class="small-text">Found in {item["section"]}</div>
                <div class="very-small-text text-muted">{item["text"]}</div>
            </div>
            """
        create_card("Media", media_content, "Rule 5.5(c)", "up to 5 points")

    with col2:
        # Tracked Changes
        create_card("Tracked Changes", """
            <div class="status-success">
                <div style="margin-bottom: 0.5rem;">✅ No tracked changes found</div>
                <div>✅ No comments found</div>
            </div>
        """, "Rule 5.4", "up to 5 points")

        # Plagiarism
        create_card("Plagiarism", """
            <div class="status-success">
                ✅ No plagiarism detected
            </div>
        """, "Rule 11.2", "1-50 points")

    # Abbreviations
    st.markdown("""
    <div class="custom-card">
        <div class="section-header">
            ⚠️ Non-Permitted Abbreviations
            <span class="very-small-text text-muted">(Rule 5.17 - 1 point each, max 3)</span>
        </div>
    """, unsafe_allow_html=True)
    
    for abbr, info in initial_data["abbreviations"].items():
        with st.expander(f"{abbr} ({info['count']} occurrence{'s' if info['count'] > 1 else ''})"):
            st.markdown(f"""
            <div class="status-error">
                ❌ Non-permitted abbreviation
                <div class="very-small-text text-muted">
                    Found in: {', '.join(info['sections'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
