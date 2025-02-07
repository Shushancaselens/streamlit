import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="Jessup Memorial Penalty Checker", layout="wide")

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

# CSS styles
st.markdown("""
<style>
    .card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }
    .success { color: #10b981; }
    .warning { color: #f59e0b; }
    .error { color: #ef4444; }
</style>
""", unsafe_allow_html=True)

def create_progress_bar(count, limit):
    percentage = (count / limit) * 100
    color = "#10b981"
    if percentage > 90: color = "#f59e0b"
    if percentage > 100: color = "#ef4444"
    
    st.markdown(f'''
        <div style="background-color: #f8f9fa; padding: 1rem; border-radius: 0.5rem;">
            <div style="display: flex; justify-content: space-between;">
                <span>{count} words</span>
                <span style="color: {color}">{percentage:.1f}%</span>
            </div>
            <div style="background-color: #e5e7eb; height: 6px; border-radius: 3px; margin: 0.5rem 0;">
                <div style="width: {min(percentage, 100)}%; height: 100%; border-radius: 3px; background-color: {color}">
                </div>
            </div>
            <div style="text-align: right; font-size: 0.8rem; color: #666;">Limit: {limit}</div>
        </div>
    ''', unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.title("Jessup Penalty Checker")
        st.markdown(f"Memorandum for the {initial_data['memorialType']}")
        st.markdown('''
            <div style="background: #fee2e2; padding: 1rem; border-radius: 0.5rem;">
                <div style="color: #991b1b;">Total Penalty Points</div>
                <div style="font-size: 2rem; font-weight: bold; color: #dc2626;">10</div>
            </div>
        ''', unsafe_allow_html=True)
        
        # Navigation
        st.markdown("### Sections")
        sections = [
            ("📄", "Cover Page", "Rule 5.6", "2 points"),
            ("✓", "Memorial Parts", "Rule 5.5", "2 points per part"),
            ("📏", "Length Check", "Rule 5.12", "varies"),
            ("🔒", "Anonymity", "Rule 5.14", "up to 10 points"),
            ("📝", "Tracked Changes", "Rule 5.4", "up to 5 points"),
            ("📚", "Citations", "Rule 5.13", "up to 5 points"),
            ("🖼️", "Media", "Rule 5.5(c)", "up to 5 points"),
            ("📑", "Abbreviations", "Rule 5.17", "1 point each, max 3"),
            ("🔍", "Plagiarism", "Rule 11.2", "1-50 points")
        ]
        
        for icon, section, rule, points in sections:
            st.markdown(f'''
                <div class="card" style="margin-bottom: 0.5rem;">
                    <div style="display: flex; gap: 0.5rem;">
                        <div>{icon}</div>
                        <div>
                            <div style="font-weight: 500;">{section}</div>
                            <div style="font-size: 0.8rem; color: #666;">{rule} - {points}</div>
                        </div>
                    </div>
                </div>
            ''', unsafe_allow_html=True)

    # Main content
    st.title("Jessup Memorial Penalty Checker")

    # Penalty Summary
    st.markdown("### ⚠️ Penalty Score Summary")
    st.markdown('''
        <div class="card">
            <table style="width: 100%;">
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <th>Rule</th>
                    <th>Description</th>
                    <th style="text-align: center;">A</th>
                    <th style="text-align: center;">R</th>
                </tr>
                <tr>
                    <td>Rule 5.5</td>
                    <td>Missing Prayer for Relief<br><span style="font-size: 0.8rem; color: #666;">2 points per part</span></td>
                    <td style="text-align: center;">4</td>
                    <td style="text-align: center;">2</td>
                </tr>
                <tr>
                    <td>Rule 5.17</td>
                    <td>Non-Permitted Abbreviations (5 found)<br><span style="font-size: 0.8rem; color: #666;">1 point each, max 3</span></td>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">0</td>
                </tr>
                <tr>
                    <td>Rule 5.13</td>
                    <td>Improper Citation<br><span style="font-size: 0.8rem; color: #666;">1 point per violation, max 5</span></td>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">0</td>
                </tr>
                <tr style="font-weight: bold; background-color: #f8f9fa;">
                    <td colspan="2" style="text-align: right;">TOTAL</td>
                    <td style="text-align: center;">10</td>
                    <td style="text-align: center;">2</td>
                </tr>
            </table>
        </div>
    ''', unsafe_allow_html=True)

    # Document Sections
    col1, col2 = st.columns(2)

    with col1:
        # Cover Page Check
        st.markdown("### 📄 Cover Page Information")
        st.markdown("#### Rule 5.6 - 2 points")
        for key, value in initial_data["coverPage"].items():
            icon = "✅" if value["present"] else "❌"
            color = "success" if value["present"] else "error"
            st.markdown(f'''
                <div class="card">
                    <div style="display: flex; justify-content: space-between;">
                        <span>{key}</span>
                        <span class="{color}">{icon} {value["found"]}</span>
                    </div>
                </div>
            ''', unsafe_allow_html=True)

    with col2:
        # Memorial Parts
        st.markdown("### ✓ Memorial Parts")
        st.markdown("#### Rule 5.5 - 2 points per part")
        st.markdown('''
            <div class="card">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
        ''', unsafe_allow_html=True)
        
        for part, present in initial_data["memorialParts"].items():
            icon = "✅" if present else "❌"
            color = "success" if present else "error"
            st.markdown(f'''
                <div class="{color}">
                    {icon} {part}
                </div>
            ''', unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

    # Word Count Analysis
    st.markdown("### 📏 Word Count Analysis")
    st.markdown("#### Rule 5.12")
    word_count_cols = st.columns(2)
    for idx, (section, data) in enumerate(initial_data["wordCounts"].items()):
        with word_count_cols[idx % 2]:
            st.markdown(f'<div class="card">', unsafe_allow_html=True)
            st.markdown(f"**{section}**")
            create_progress_bar(data["count"], data["limit"])
            st.markdown('</div>', unsafe_allow_html=True)

    # Additional sections
    col3, col4 = st.columns(2)

    with col3:
        # Tracked Changes
        st.markdown("### 📝 Tracked Changes")
        st.markdown("#### Rule 5.4 - up to 5 points")
        st.markdown('''
            <div class="card">
                <div class="success">✅ No tracked changes found</div>
                <div class="success" style="margin-top: 0.5rem;">✅ No comments found</div>
            </div>
        ''', unsafe_allow_html=True)

        # Citations
        st.markdown("### 📚 Citations")
        st.markdown("#### Rule 5.13 - up to 5 points")
        st.markdown('''
            <div class="card">
                <div class="error">⚠️ 5 instances of improper citation format detected</div>
            </div>
        ''', unsafe_allow_html=True)

    with col4:
        # Anonymity Check
        st.markdown("### 🔒 Anonymity Check")
        st.markdown("#### Rule 5.14 - up to 10 points")
        st.markdown('''
            <div class="card">
                <div class="success">✅ No anonymity violations found</div>
                <div style="margin-top: 0.5rem; color: #666;">
                    No disclosure of school, team members, or country
                </div>
            </div>
        ''', unsafe_allow_html=True)

        # Media Check
        st.markdown("### 🖼️ Media Check")
        st.markdown("#### Rule 5.5(c) - up to 5 points")
        for item in initial_data["media"]:
            st.markdown(f'''
                <div class="card">
                    <div class="warning">⚠️ Found in {item["section"]}: {item["text"]}</div>
                </div>
            ''', unsafe_allow_html=True)

    # Abbreviations
    st.markdown("### 📑 Non-Permitted Abbreviations")
    st.markdown("#### Rule 5.17 - 1 point each, max 3")
    for abbr, info in initial_data["abbreviations"].items():
        with st.expander(f"❌ {abbr} ({info['count']} occurrence{'s' if info['count'] > 1 else ''})"):
            st.markdown(f"Found in: {', '.join(info['sections'])}")

    # Plagiarism Check
    st.markdown("### 🔍 Plagiarism Check")
    st.markdown("#### Rule 11.2 - 1-50 points")
    st.markdown('''
        <div class="card">
            <div class="success">✅ No plagiarism detected</div>
        </div>
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
