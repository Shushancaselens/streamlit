import streamlit as st
import pandas as pd

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

def get_status_color(status):
    colors = {
        'success': '#10b981',
        'warning': '#f59e0b',
        'error': '#ef4444'
    }
    return colors.get(status, '#10b981')

def create_progress_bar(count, limit):
    """Create an enhanced progress bar"""
    percentage = (count / limit) * 100
    status = "success"
    if percentage > 90:
        status = "warning"
    if percentage > 100:
        status = "error"
    
    color = get_status_color(status)
    
    st.markdown(f"""
        <div style="background-color: #f9fafb; padding: 1rem; border-radius: 0.5rem; margin: 0.5rem 0;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span>{count} words</span>
                <span style="color: {color}">{percentage:.1f}%</span>
            </div>
            <div style="width: 100%; background-color: #e5e7eb; height: 0.5rem; border-radius: 0.25rem;">
                <div style="width: {min(percentage, 100)}%; height: 100%; border-radius: 0.25rem; background-color: {color};">
                </div>
            </div>
            <div style="text-align: right; font-size: 0.8rem; color: #6b7280; margin-top: 0.25rem;">
                Limit: {limit}
            </div>
        </div>
    """, unsafe_allow_html=True)

def main():
    # Add custom CSS
    st.markdown("""
        <style>
        .main-card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 0.75rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
        .section-header {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #1f2937;
        }
        .status-success { color: #10b981; }
        .status-error { color: #ef4444; }
        .status-warning { color: #f59e0b; }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("""
            <div style="padding: 1rem;">
                <h1 style="margin-bottom: 1rem;">Jessup Penalty Checker</h1>
                <div style="font-size: 1.1rem; color: #4b5563;">
                    Memorandum for the Applicant
                </div>
                <div style="background-color: #fee2e2; padding: 1rem; border-radius: 0.5rem; margin-top: 1rem;">
                    <div style="font-size: 0.9rem; color: #991b1b;">Penalty Points</div>
                    <div style="font-size: 2rem; font-weight: bold; color: #dc2626;">10</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Navigation Items
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
                <div style="padding: 0.75rem; border-radius: 0.5rem; margin-bottom: 0.5rem; 
                            background-color: #f9fafb; cursor: pointer;">
                    <div style="display: flex; gap: 0.75rem; align-items: center;">
                        <div>{icon}</div>
                        <div>
                            <div style="font-weight: 500;">{section}</div>
                            <div style="font-size: 0.8rem; color: #6b7280;">{rule} - {points}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Main content
    st.title("Jessup Memorial Penalty Checker")

    # Penalty Score Summary
    st.markdown("""
        <div class="main-card">
            <div class="section-header">⚠️ Penalty Score Summary</div>
            <table style="width: 100%; border-collapse: separate; border-spacing: 0;">
                <thead>
                    <tr style="background-color: #f9fafb;">
                        <th style="padding: 1rem; text-align: left; border-bottom: 2px solid #e5e7eb;">Rule</th>
                        <th style="padding: 1rem; text-align: left; border-bottom: 2px solid #e5e7eb;">Description</th>
                        <th style="padding: 1rem; text-align: center; border-bottom: 2px solid #e5e7eb;">A</th>
                        <th style="padding: 1rem; text-align: center; border-bottom: 2px solid #e5e7eb;">R</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 1rem; border-bottom: 1px solid #e5e7eb;">Rule 5.5</td>
                        <td style="padding: 1rem; border-bottom: 1px solid #e5e7eb;">
                            Missing Prayer for Relief
                            <div style="font-size: 0.8rem; color: #6b7280;">2 points per part</div>
                        </td>
                        <td style="padding: 1rem; text-align: center; border-bottom: 1px solid #e5e7eb;">4</td>
                        <td style="padding: 1rem; text-align: center; border-bottom: 1px solid #e5e7eb;">2</td>
                    </tr>
                    <tr>
                        <td style="padding: 1rem; border-bottom: 1px solid #e5e7eb;">Rule 5.17</td>
                        <td style="padding: 1rem; border-bottom: 1px solid #e5e7eb;">
                            Non-Permitted Abbreviations (5 found)
                            <div style="font-size: 0.8rem; color: #6b7280;">1 point each, max 3</div>
                        </td>
                        <td style="padding: 1rem; text-align: center; border-bottom: 1px solid #e5e7eb;">3</td>
                        <td style="padding: 1rem; text-align: center; border-bottom: 1px solid #e5e7eb;">0</td>
                    </tr>
                    <tr style="background-color: #f9fafb; font-weight: 600;">
                        <td colspan="2" style="padding: 1rem; text-align: right;">TOTAL</td>
                        <td style="padding: 1rem; text-align: center;">10</td>
                        <td style="padding: 1rem; text-align: center;">2</td>
                    </tr>
                </tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)

    # Create two columns for the layout
    col1, col2 = st.columns(2)

    # Cover Page Check
    with col1:
        st.markdown("""
            <div class="main-card">
                <div class="section-header">📄 Cover Page Information</div>
        """, unsafe_allow_html=True)
        
        for key, value in initial_data["coverPage"].items():
            icon = "✅" if value["present"] else "❌"
            color_class = "status-success" if value["present"] else "status-error"
            st.markdown(f"""
                <div style="display: flex; justify-content: space-between; align-items: center; 
                            padding: 0.75rem; border-bottom: 1px solid #e5e7eb;">
                    <span>{key}</span>
                    <div class="{color_class}" style="display: flex; align-items: center; gap: 0.5rem;">
                        {icon} {value["found"]}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

    # Memorial Parts
    with col2:
        st.markdown("""
            <div class="main-card">
                <div class="section-header">✓ Memorial Parts</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
        """, unsafe_allow_html=True)
        
        for part, present in initial_data["memorialParts"].items():
            icon = "✅" if present else "❌"
            color_class = "status-success" if present else "status-error"
            st.markdown(f"""
                <div class="{color_class}" style="display: flex; align-items: center; gap: 0.5rem;">
                    {icon} {part}
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

    # Word Count Analysis
    st.markdown("""
        <div class="main-card">
            <div class="section-header">📏 Word Count Analysis</div>
    """, unsafe_allow_html=True)
    
    word_count_cols = st.columns(2)
    for idx, (section, data) in enumerate(initial_data["wordCounts"].items()):
        with word_count_cols[idx % 2]:
            st.markdown(f"<div style='font-weight: 500; margin-bottom: 0.5rem;'>{section}</div>", 
                       unsafe_allow_html=True)
            create_progress_bar(data["count"], data["limit"])

    st.markdown("</div>", unsafe_allow_html=True)

    # Additional sections...
    sections_data = [
        ("Anonymity Check", "🔒", "success", "No anonymity violations found", 
         "No disclosure of school, team members, or country"),
        ("Citations", "📚", "error", "Improper citations detected", 
         "5 instances of improper citation format found"),
        ("Media Check", "🖼️", "warning", "Media found", 
         "Found media in Cover Page: ----media/image1.png----"),
        ("Plagiarism Check", "🔍", "success", "No plagiarism detected", 
         "Document passed plagiarism check")
    ]

    for title, icon, status, message, detail in sections_data:
        st.markdown(f"""
            <div class="main-card">
                <div class="section-header">{icon} {title}</div>
                <div class="status-{status}">
                    {message}
                    <div style="font-size: 0.9rem; color: #6b7280; margin-top: 0.5rem;">
                        {detail}
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
