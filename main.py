import streamlit as st

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initial data setup (same as before)
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

# Custom CSS
st.markdown("""
<style>
    /* Cards */
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #e5e7eb;
    }
    
    /* Status colors */
    .success { color: #10b981; }
    .warning { color: #f59e0b; }
    .error { color: #ef4444; }
    
    /* Progress bars */
    .progress-container {
        background-color: #f9fafb;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    /* Tables */
    .custom-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
    }
    .custom-table th {
        background-color: #f9fafb;
        padding: 12px;
        text-align: left;
        border-bottom: 2px solid #e5e7eb;
    }
    .custom-table td {
        padding: 12px;
        border-bottom: 1px solid #e5e7eb;
    }
</style>
""", unsafe_allow_html=True)

def display_header(title, icon, rule="", points=""):
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 15px;">
            <span style="font-size: 1.2em;">{icon}</span>
            <span style="font-size: 1.1em; font-weight: 600;">{title}</span>
            {f'<span style="font-size: 0.8em; color: #666;">({rule} - {points})</span>' if rule else ''}
        </div>
    """, unsafe_allow_html=True)

def create_progress_bar(count, limit):
    percentage = (count / limit) * 100
    color = "#10b981"  # success
    if percentage > 90:
        color = "#f59e0b"  # warning
    if percentage > 100:
        color = "#ef4444"  # error
    
    st.markdown(f"""
        <div class="progress-container">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                <span>{count} words</span>
                <span style="color: {color};">{percentage:.1f}%</span>
            </div>
            <div style="width: 100%; background-color: #e5e7eb; height: 6px; border-radius: 3px;">
                <div style="width: {min(percentage, 100)}%; height: 100%; border-radius: 3px; background-color: {color};"></div>
            </div>
            <div style="text-align: right; font-size: 0.8em; color: #666; margin-top: 5px;">Limit: {limit}</div>
        </div>
    """, unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.markdown("""
            <div style="padding: 20px;">
                <h1 style="margin-bottom: 20px;">Jessup Penalty Checker</h1>
                <div style="font-size: 1.1em; color: #4b5563;">
                    Memorandum for the Applicant
                </div>
                <div style="background: #fee2e2; padding: 15px; border-radius: 8px; margin-top: 15px;">
                    <div style="font-size: 0.9em; color: #991b1b;">Total Penalty Points</div>
                    <div style="font-size: 2em; font-weight: bold; color: #dc2626;">10</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

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
            st.markdown(f"""
                <div style="padding: 10px; border-radius: 5px; margin: 5px 0; 
                            background-color: white; cursor: pointer;">
                    <div style="display: flex; gap: 10px; align-items: center;">
                        <div>{icon}</div>
                        <div>
                            <div style="font-weight: 500;">{section}</div>
                            <div style="font-size: 0.8em; color: #666;">{rule} - {points}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Main content
    st.title("Jessup Memorial Penalty Checker")

    # Penalty Summary Table
    with st.container():
        display_header("Penalty Score Summary", "⚠️")
        st.markdown("""
            <div class="card">
                <table class="custom-table">
                    <thead>
                        <tr>
                            <th>Rule</th>
                            <th>Description</th>
                            <th style="text-align: center;">A</th>
                            <th style="text-align: center;">R</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Rule 5.5</td>
                            <td>Missing Prayer for Relief<br/>
                                <span style="font-size: 0.8em; color: #666;">2 points per part</span>
                            </td>
                            <td style="text-align: center;">4</td>
                            <td style="text-align: center;">2</td>
                        </tr>
                        <tr>
                            <td>Rule 5.17</td>
                            <td>Non-Permitted Abbreviations (5 found)<br/>
                                <span style="font-size: 0.8em; color: #666;">1 point each, max 3</span>
                            </td>
                            <td style="text-align: center;">3</td>
                            <td style="text-align: center;">0</td>
                        </tr>
                        <tr>
                            <td>Rule 5.13</td>
                            <td>Improper Citation<br/>
                                <span style="font-size: 0.8em; color: #666;">1 point per violation, max 5</span>
                            </td>
                            <td style="text-align: center;">3</td>
                            <td style="text-align: center;">0</td>
                        </tr>
                        <tr style="background-color: #f9fafb; font-weight: 600;">
                            <td colspan="2" style="text-align: right;">TOTAL</td>
                            <td style="text-align: center;">10</td>
                            <td style="text-align: center;">2</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        """, unsafe_allow_html=True)

    # Document Sections in two columns
    col1, col2 = st.columns(2)

    with col1:
        # Cover Page Check
        with st.container():
            display_header("Cover Page Information", "📄", "Rule 5.6", "2 points")
            for key, value in initial_data["coverPage"].items():
                st.markdown(f"""
                    <div class="card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span>{key}</span>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <span class="{'success' if value['present'] else 'error'}">
                                    {'✅' if value['present'] else '❌'}
                                </span>
                                <span>{value['found']}</span>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

    with col2:
        # Memorial Parts
        with st.container():
            display_header("Memorial Parts", "✓", "Rule 5.5", "2 points per part")
            st.markdown("""
                <div class="card">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
            """, unsafe_allow_html=True)
            
            for part, present in initial_data["memorialParts"].items():
                st.markdown(f"""
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span class="{'success' if present else 'error'}">
                            {'✅' if present else '❌'}
                        </span>
                        <span>{part}</span>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div></div>", unsafe_allow_html=True)

    # Word Count Analysis
    display_header("Word Count Analysis", "📏", "Rule 5.12", "varies")
    word_count_cols = st.columns(2)
    for idx, (section, data) in enumerate(initial_data["wordCounts"].items()):
        with word_count_cols[idx % 2]:
            st.markdown(f"""
                <div class="card">
                    <div style="font-weight: 500; margin-bottom: 8px;">{section}</div>
            """, unsafe_allow_html=True)
            create_progress_bar(data["count"], data["limit"])
            st.markdown("</div>", unsafe_allow_html=True)

    # Additional Checks in two columns
    col3, col4 = st.columns(2)

    with col3:
        # Tracked Changes
        display_header("Tracked Changes", "📝", "Rule 5.4", "up to 5 points")
        st.markdown("""
            <div class="card">
                <div class="success" style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    ✅ No tracked changes found
                </div>
                <div class="success" style="display: flex; align-items: center; gap: 8px;">
                    ✅ No comments found
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Citations
        display_header("Citations", "📚", "Rule 5.13", "up to 5 points")
        st.markdown("""
            <div class="card">
                <div class="error" style="display: flex; align-items: center; gap: 8px;">
                    ⚠️ 5 instances of improper citation format detected
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        # Anonymity Check
        display_header("Anonymity Check", "🔒", "Rule 5.14", "up to 10 points")
        st.markdown("""
            <div class="card">
                <div class="success" style="display: flex; align-items: center; gap: 8px;">
                    ✅ No anonymity violations found
                </div>
                <div style="margin-top: 8px; font-size: 0.9em; color: #666;">
                    No disclosure of school, team members, or country
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Media Check
        display_header("Media Check", "🖼️", "Rule 5.5(c)", "up to 5 points")
        for item in initial_data["media"]:
            st.markdown(f"""
                <div class="card">
                    <div class="warning" style="display: flex; align-items: center; gap: 8px;">
                        ⚠️ Found in {item['section']}: {item['text']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Abbreviations
    display_header("Non-Permitted Abbreviations", "📑", "Rule 5.17", "1 point each, max 3")
    for abbr, info in initial_data["abbreviations"].items():
        st.markdown(f"""
            <div class="card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
