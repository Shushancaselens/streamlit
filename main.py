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

def local_css():
    st.markdown("""
        <style>
        .stApp {
            background-color: #f8fafc;
        }
        
        .glass-card {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            border: 1px solid rgba(229, 231, 235, 0.5);
        }
        
        .status-badge {
            padding: 4px 12px;
            border-radius: 999px;
            font-size: 14px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        
        .success { 
            background-color: #dcfce7;
            color: #166534;
        }
        
        .error { 
            background-color: #fee2e2;
            color: #991b1b;
        }
        
        .warning {
            background-color: #fef3c7;
            color: #92400e;
        }
        
        .section-title {
            font-size: 18px;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .nav-item {
            background-color: white;
            padding: 12px 16px;
            border-radius: 8px;
            margin: 8px 0;
            transition: all 0.2s;
            border: 1px solid #e2e8f0;
            cursor: pointer;
        }
        
        .nav-item:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        
        .table-modern {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin: 16px 0;
        }
        
        .table-modern th {
            background-color: #f8fafc;
            padding: 12px;
            text-align: left;
            color: #475569;
            border-bottom: 2px solid #e2e8f0;
            font-weight: 600;
        }
        
        .table-modern td {
            padding: 12px;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .progress-wrapper {
            background-color: #f8fafc;
            border-radius: 8px;
            padding: 16px;
            margin: 8px 0;
        }
        
        .progress-bar {
            height: 6px;
            background-color: #e2e8f0;
            border-radius: 999px;
            margin: 8px 0;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            border-radius: 999px;
            transition: width 0.3s ease;
        }
        
        .penalty-counter {
            background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
            padding: 20px;
            border-radius: 12px;
            margin: 16px 0;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        
        .section-divider {
            height: 1px;
            background-color: #e2e8f0;
            margin: 24px 0;
        }
        </style>
    """, unsafe_allow_html=True)

def create_badge(text, status, icon=""):
    return f'<span class="status-badge {status}">{icon} {text}</span>'

def create_progress_bar(count, limit):
    percentage = (count / limit) * 100
    status = "success"
    if percentage > 90: status = "warning"
    if percentage > 100: status = "error"
    
    colors = {
        "success": "#10b981",
        "warning": "#f59e0b",
        "error": "#ef4444"
    }
    
    return f"""
        <div class="progress-wrapper">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 500;">{count} words</span>
                <span style="color: {colors[status]}; font-weight: 500;">{percentage:.1f}%</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {min(percentage, 100)}%; background-color: {colors[status]};"></div>
            </div>
            <div style="text-align: right; font-size: 14px; color: #64748b;">
                Limit: {limit} words
            </div>
        </div>
    """

def main():
    local_css()
    
    # Sidebar
    with st.sidebar:
        st.markdown('<h1 style="margin-bottom: 20px;">Jessup Penalty Checker</h1>', unsafe_allow_html=True)
        st.markdown(f'''
            <div style="font-size: 18px; color: #475569;">
                Memorandum for the {initial_data["memorialType"]}
            </div>
            <div class="penalty-counter">
                <div style="font-size: 14px; color: #991b1b;">Total Penalty Points</div>
                <div style="font-size: 32px; font-weight: 700; color: #7f1d1d;">10</div>
            </div>
        ''', unsafe_allow_html=True)
        
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
                <div class="nav-item">
                    <div style="display: flex; gap: 12px; align-items: center;">
                        <div style="font-size: 20px;">{icon}</div>
                        <div>
                            <div style="font-weight: 500; color: #1e293b;">{section}</div>
                            <div style="font-size: 14px; color: #64748b;">{rule} - {points}</div>
                        </div>
                    </div>
                </div>
            ''', unsafe_allow_html=True)

    # Main content
    st.markdown('<h1 style="font-size: 32px; font-weight: 700; color: #1e293b; margin-bottom: 32px;">Jessup Memorial Penalty Checker</h1>', unsafe_allow_html=True)

    # Summary Card
    st.markdown('''
        <div class="glass-card">
            <div class="section-title">⚠️ Penalty Score Summary</div>
            <table class="table-modern">
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
                        <td>Missing Prayer for Relief<br>
                            <span style="font-size: 14px; color: #64748b;">2 points per part</span>
                        </td>
                        <td style="text-align: center;">4</td>
                        <td style="text-align: center;">2</td>
                    </tr>
                    <tr>
                        <td>Rule 5.17</td>
                        <td>Non-Permitted Abbreviations (5 found)<br>
                            <span style="font-size: 14px; color: #64748b;">1 point each, max 3</span>
                        </td>
                        <td style="text-align: center;">3</td>
                        <td style="text-align: center;">0</td>
                    </tr>
                    <tr>
                        <td>Rule 5.13</td>
                        <td>Improper Citation<br>
                            <span style="font-size: 14px; color: #64748b;">1 point per violation, max 5</span>
                        </td>
                        <td style="text-align: center;">3</td>
                        <td style="text-align: center;">0</td>
                    </tr>
                    <tr style="background-color: #f8fafc;">
                        <td colspan="2" style="text-align: right; font-weight: 600;">TOTAL</td>
                        <td style="text-align: center; font-weight: 600;">10</td>
                        <td style="text-align: center; font-weight: 600;">2</td>
                    </tr>
                </tbody>
            </table>
        </div>
    ''', unsafe_allow_html=True)

    # Document Sections
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
            <div class="glass-card">
                <div class="section-title">📄 Cover Page Information</div>
        ''', unsafe_allow_html=True)
        
        for key, value in initial_data["coverPage"].items():
            status = "success" if value["present"] else "error"
            icon = "✅" if value["present"] else "❌"
            st.markdown(f'''
                <div style="display: flex; justify-content: space-between; align-items: center; 
                            padding: 12px 0; border-bottom: 1px solid #e2e8f0;">
                    <span style="color: #1e293b;">{key}</span>
                    {create_badge(value["found"], status, icon)}
                </div>
            ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('''
            <div class="glass-card">
                <div class="section-title">✓ Memorial Parts</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
        ''', unsafe_allow_html=True)
        
        for part, present in initial_data["memorialParts"].items():
            status = "success" if present else "error"
            icon = "✅" if present else "❌"
            st.markdown(create_badge(part, status, icon), unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)

    # Word Count Analysis
    st.markdown('''
        <div class="glass-card">
            <div class="section-title">📏 Word Count Analysis</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
    ''', unsafe_allow_html=True)

    for section, data in initial_data["wordCounts"].items():
        st.markdown(f'''
            <div>
                <div style="font-weight: 500; margin-bottom: 8px; color: #1e293b;">{section}</div>
                {create_progress_bar(data["count"], data["limit"])}
            </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

    # Additional Sections
    col3, col4 = st.columns(2)

    with col3:
        # Tracked Changes
        st.markdown('''
            <div class="glass-card">
                <div class="section-title">📝 Tracked Changes</div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
        ''', unsafe_allow_html=True)
        
        st.markdown(create_badge("No tracked changes found", "success", "✅"), unsafe_allow_html=True)
        st.markdown(create_badge("No comments found", "success", "✅"), unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)

        # Citations
        st.markdown('''
            <div class="glass-card">
                <div class="
