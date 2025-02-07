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

# Enhanced CSS for a more polished look
st.markdown("""
<style>
    /* Global styles */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
    }
    
    .main {
        background-color: #f1f5f9;
    }
    
    /* Cards */
    .glass-card {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 0.75rem;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
    }
    
    /* Status indicators */
    .success-badge {
        background-color: #dcfce7;
        color: #166534;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        display: inline-flex;
        align-items: center;
        gap: 0.375rem;
    }
    
    .error-badge {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        display: inline-flex;
        align-items: center;
        gap: 0.375rem;
    }
    
    .warning-badge {
        background-color: #fef3c7;
        color: #92400e;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        display: inline-flex;
        align-items: center;
        gap: 0.375rem;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Navigation items */
    .nav-item {
        background-color: white;
        padding: 0.75rem 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        transition: all 0.2s;
        border: 1px solid #e2e8f0;
    }
    
    .nav-item:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Tables */
    .modern-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
    }
    
    .modern-table th {
        background-color: #f8fafc;
        padding: 1rem;
        text-align: left;
        font-weight: 600;
        color: #475569;
        border-bottom: 2px solid #e2e8f0;
    }
    
    .modern-table td {
        padding: 1rem;
        border-bottom: 1px solid #e2e8f0;
    }
    
    .modern-table tr:last-child td {
        border-bottom: none;
    }
    
    /* Progress bars */
    .progress-container {
        background-color: #f8fafc;
        border-radius: 0.75rem;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .progress-bar {
        height: 0.5rem;
        border-radius: 9999px;
        background-color: #e2e8f0;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .progress-fill {
        height: 100%;
        border-radius: 9999px;
        transition: width 0.3s ease;
    }
    
    /* Sidebar styles */
    .sidebar-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    .penalty-counter {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

def create_progress_bar(count, limit):
    percentage = (count / limit) * 100
    color = "#10b981"  # success
    if percentage > 90: color = "#f59e0b"  # warning
    if percentage > 100: color = "#ef4444"  # error
    
    st.markdown(f'''
        <div class="progress-container">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="font-weight: 500;">{count} words</div>
                <div style="color: {color}; font-weight: 500;">{percentage:.1f}%</div>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {min(percentage, 100)}%; background-color: {color};"></div>
            </div>
            <div style="text-align: right; font-size: 0.875rem; color: #64748b;">
                Limit: {limit} words
            </div>
        </div>
    ''', unsafe_allow_html=True)

def create_badge(text, status="success", icon=""):
    return f'<span class="{status}-badge">{icon} {text}</span>'

def main():
    # Sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-title">Jessup Penalty Checker</div>', unsafe_allow_html=True)
        st.markdown(f'''
            <div style="font-size: 1.1rem; color: #475569;">
                Memorandum for the {initial_data["memorialType"]}
            </div>
            <div class="penalty-counter">
                <div style="font-size: 0.875rem; color: #991b1b;">Total Penalty Points</div>
                <div style="font-size: 2rem; font-weight: 700; color: #7f1d1d;">10</div>
            </div>
        ''', unsafe_allow_html=True)
        
        # Navigation
        st.markdown('<div class="section-header">Sections</div>', unsafe_allow_html=True)
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
                    <div style="display: flex; gap: 0.75rem; align-items: center;">
                        <div style="font-size: 1.25rem;">{icon}</div>
                        <div>
                            <div style="font-weight: 500; color: #1e293b;">{section}</div>
                            <div style="font-size: 0.875rem; color: #64748b;">{rule} - {points}</div>
                        </div>
                    </div>
                </div>
            ''', unsafe_allow_html=True)

    # Main content
    st.markdown('<h1 style="font-size: 2rem; font-weight: 700; color: #1e293b; margin-bottom: 2rem;">Jessup Memorial Penalty Checker</h1>', unsafe_allow_html=True)

    # Penalty Summary
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">⚠️ Penalty Score Summary</div>', unsafe_allow_html=True)
    st.markdown('''
        <table class="modern-table">
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
                    <td>
                        Missing Prayer for Relief
                        <div style="font-size: 0.875rem; color: #64748b;">2 points per part</div>
                    </td>
                    <td style="text-align: center;">4</td>
                    <td style="text-align: center;">2</td>
                </tr>
                <tr>
                    <td>Rule 5.17</td>
                    <td>
                        Non-Permitted Abbreviations (5 found)
                        <div style="font-size: 0.875rem; color: #64748b;">1 point each, max 3</div>
                    </td>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">0</td>
                </tr>
                <tr>
                    <td>Rule 5.13</td>
                    <td>
                        Improper Citation
                        <div style="font-size: 0.875rem; color: #64748b;">1 point per violation, max 5</div>
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
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Document Sections
    col1, col2 = st.columns(2)

    with col1:
        # Cover Page Check
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">📄 Cover Page Information</div>', unsafe_allow_html=True)
        for key, value in initial_data["coverPage"].items():
            status = "success" if value["present"] else "error"
            icon = "✅" if value["present"] else "❌"
            st.markdown(f'''
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem 0;">
                    <span style="color: #1e293b;">{key}</span>
                    {create_badge(value["found"], status, icon)}
                </div>
            ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Memorial Parts
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">✓ Memorial Parts</div>', unsafe_allow_html=True)
        st.markdown('<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">', unsafe_allow_html=True)
        for part, present in initial_data["memorialParts"].items():
            status = "success" if present else "error"
            icon = "✅" if present else "❌"
            st.markdown(create_badge(part, status, icon), unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

    # Word Count Analysis
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">
