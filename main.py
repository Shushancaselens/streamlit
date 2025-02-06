import streamlit as st

# Page config and custom styling
st.set_page_config(page_title="Jessup Memorial Penalty Checker", layout="wide")

# Custom CSS
def load_css():
    st.markdown("""
        <style>
            .stApp { background-color: rgb(249, 250, 251) !important; }
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
                border-bottom: 1px solid #e5e7eb;
                padding-bottom: 0.5rem;
            }
            .status-success { color: #22c55e; }
            .status-error { color: #ef4444; }
            .status-warning { color: #eab308; }
            .styled-table {
                width: 100%;
                border-collapse: collapse;
            }
            .styled-table th, .styled-table td {
                padding: 0.75rem;
                border-bottom: 1px solid #e5e7eb;
            }
            .styled-table tr:hover { background-color: #f9fafb; }
            .word-count-bar {
                width: 100%;
                height: 6px;
                background-color: #e5e7eb;
                border-radius: 9999px;
                margin: 0.25rem 0;
            }
        </style>
    """, unsafe_allow_html=True)

# Sample data
data = {
    "cover_page": {
        "Team Number": {"present": True, "found": "349A"},
        "Court Name": {"present": True, "found": "ICJ"},
        "Year": {"present": True, "found": "2025"},
        "Case Name": {"present": True, "found": "Naegea Sea Case"},
    },
    "memorial_parts": {
        "Cover Page": True, "Table of Contents": True,
        "Statement of Facts": True, "Pleadings": True,
        "Prayer for Relief": False
    },
    "word_counts": {
        "Statement of Facts": {"count": 1196, "limit": 1200},
        "Pleadings": {"count": 9424, "limit": 9500}
    },
    "abbreviations": {
        "ISECR": {"count": 2, "sections": ["Pleadings"]},
        "ICC": {"count": 1, "sections": ["Pleadings"]}
    }
}

penalties = [
    {"rule": "5.5", "description": "Missing Prayer for Relief", "points": 4},
    {"rule": "5.17", "description": "Non-Permitted Abbreviations", "points": 3},
    {"rule": "5.13", "description": "Improper Citations", "points": 3}
]

def render_card(title, rule, content):
    st.markdown(f"""
        <div class="card">
            <div class="card-header">
                <span>{title}</span>
                <span style="font-size: 0.75rem; color: #6b7280;">({rule})</span>
            </div>
            {content}
        </div>
    """, unsafe_allow_html=True)

def render_word_count(section, count, limit):
    percentage = (count / limit) * 100
    color = "red" if percentage > 100 else "orange" if percentage > 90 else "green"
    return f"""
        <div>
            <div style="font-weight: 500;">{section}</div>
            <div class="word-count-bar">
                <div style="width: {min(percentage, 100)}%; height: 100%; background-color: {color}; 
                     border-radius: 9999px;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.75rem;">
                <span>{count} words</span>
                <span style="color: {color};">{percentage:.1f}%</span>
            </div>
        </div>
    """

def render_check_item(label, is_present, value=""):
    icon = "✅" if is_present else "❌"
    color_class = "status-success" if is_present else "status-error"
    return f"""
        <div style="display: flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0;">
            <span class="{color_class}">{icon}</span>
            <span>{label}{f': {value}' if value else ''}</span>
        </div>
    """

def main():
    load_css()

    # Sidebar
    with st.sidebar:
        st.markdown("""
            <div class="card">
                <div style="color: #6b7280; font-size: 0.875rem; font-weight: 600;">
                    Penalty Points
                </div>
                <div style="display: flex; align-items: baseline; gap: 0.25rem; margin-top: 0.5rem;">
                    <span style="font-size: 1.875rem; font-weight: 700; color: #ef4444;">10</span>
                    <span style="color: #6b7280; font-size: 0.875rem;">points</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.title("Jessup Memorial Penalty Checker")

    # Score Summary
    summary_content = """
        <table class="styled-table">
            <tr>
                <th>Rule</th>
                <th>Description</th>
                <th style="text-align: center;">Points</th>
            </tr>
    """
    for p in penalties:
        summary_content += f"""
            <tr>
                <td>{p['rule']}</td>
                <td>{p['description']}</td>
                <td style="text-align: center;">{p['points']}</td>
            </tr>
        """
    summary_content += """
            <tr style="font-weight: 600; background-color: #f9fafb;">
                <td colspan="2" style="text-align: right;">TOTAL</td>
                <td style="text-align: center;">10</td>
            </tr>
        </table>
    """
    render_card("Penalty Score Summary", "", summary_content)

    # Main content in two columns
    col1, col2 = st.columns(2)

    with col1:
        # Cover Page
        cover_content = "".join(
            render_check_item(key, value["present"], value["found"])
            for key, value in data["cover_page"].items()
        )
        render_card("Cover Page Information", "Rule 5.6 - 2 points", cover_content)

    with col2:
        # Memorial Parts
        parts_content = "".join(
            render_check_item(part, present)
            for part, present in data["memorial_parts"].items()
        )
        render_card("Memorial Parts", "Rule 5.5 - 2 points per part", parts_content)

    # Word Count Analysis
    word_count_content = """
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
    """
    for section, info in data["word_counts"].items():
        word_count_content += render_word_count(section, info["count"], info["limit"])
    word_count_content += "</div>"
    render_card("Word Count Analysis", "Rule 5.12", word_count_content)

    # Abbreviations
    abbr_content = "".join(f"""
        <div style="border: 1px solid #e5e7eb; border-radius: 0.5rem; padding: 0.75rem; margin-bottom: 0.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span class="status-error">❌</span>
                    <span style="font-weight: 500;">{abbr}</span>
                    <span style="font-size: 0.75rem; color: #6b7280;">
                        ({info['count']} occurrence{'s' if info['count'] != 1 else ''})
                    </span>
                </div>
            </div>
            <div style="margin-top: 0.5rem; font-size: 0.75rem; color: #6b7280;">
                Found in: {', '.join(info['sections'])}
            </div>
        </div>
    """ for abbr, info in data["abbreviations"].items())
    render_card("Abbreviations", "Rule 5.17 - 1 point each, max 3", abbr_content)

if __name__ == "__main__":
    main()









