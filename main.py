import streamlit as st
import pandas as pd

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': 'Jessup Memorial Penalty Checker - Version 1.0'
    }
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

# Enhanced CSS with modern design principles
st.markdown("""
    <style>
        /* Global styles */
        [data-testid="stSidebar"] {
            background-color: #f8fafc;
            border-right: 1px solid #e2e8f0;
        }
        
        .main {
            background-color: #f1f5f9;
        }
        
        /* Modern card design */
        .modern-card {
            background-color: white;
            border-radius: 1rem;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            margin-bottom: 1.5rem;
            border: 1px solid #e2e8f0;
        }
        
        /* Section headers */
        .section-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: #0f172a;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        /* Status badges */
        .status-badge {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
        }
        
        .status-success {
            background-color: #dcfce7;
            color: #166534;
        }
        
        .status-error {
            background-color: #fee2e2;
            color: #991b1b;
        }
        
        .status-warning {
            background-color: #fef3c7;
            color: #92400e;
        }
        
        /* Navigation items */
        .nav-item {
            padding: 0.75rem;
            border-radius: 0.5rem;
            margin-bottom: 0.5rem;
            transition: all 0.2s;
            cursor: pointer;
        }
        
        .nav-item:hover {
            background-color: #e2e8f0;
        }
        
        /* Progress bars */
        .modern-progress {
            background-color: #f8fafc;
            border-radius: 0.75rem;
            padding: 1rem;
            margin: 0.5rem 0;
        }
        
        .progress-bar {
            height: 0.5rem;
            border-radius: 0.25rem;
            background-color: #e2e8f0;
            margin: 0.5rem 0;
            overflow: hidden;
        }
        
        /* Custom table styles */
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
            color: #64748b;
            border-bottom: 2px solid #e2e8f0;
        }
        
        .modern-table td {
            padding: 1rem;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .modern-table tr:hover {
            background-color: #f8fafc;
        }
        
        /* Action buttons */
        .action-button {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            font-weight: 500;
            transition: all 0.2s;
            cursor: pointer;
        }
        
        .action-button-primary {
            background-color: #2563eb;
            color: white;
        }
        
        .action-button-primary:hover {
            background-color: #1d4ed8;
        }
        
        /* Summary cards */
        .summary-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .summary-card {
            background-color: white;
            border-radius: 0.75rem;
            padding: 1.25rem;
            border: 1px solid #e2e8f0;
        }
        
        /* Abbreviation item */
        .abbr-item {
            background-color: #f8fafc;
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 0.5rem;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .abbr-item:hover {
            background-color: #e2e8f0;
        }
    </style>
""", unsafe_allow_html=True)

def create_status_badge(status, text):
    return f'<span class="status-badge status-{status}">{text}</span>'

def create_progress_bar(count, limit):
    percentage = (count / limit) * 100
    status = "success"
    if percentage > 90:
        status = "warning"
    if percentage > 100:
        status = "error"
    
    color_map = {
        "success": "#22c55e",
        "warning": "#f59e0b",
        "error": "#ef4444"
    }
    
    st.markdown(f"""
        <div class="modern-progress">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 500;">{count} words</span>
                <span class="status-badge status-{status}">{percentage:.1f}%</span>
            </div>
            <div class="progress-bar">
                <div style="width: {min(percentage, 100)}%; height: 100%; 
                     background-color: {color_map[status]}; transition: width 0.3s;">
                </div>
            </div>
            <div style="text-align: right; font-size: 0.875rem; color: #64748b;">
                Limit: {limit}
            </div>
        </div>
    """, unsafe_allow_html=True)

def main():
    # Sidebar content
    with st.sidebar:
        st.markdown("""
            <div style="padding: 1.5rem 1rem;">
                <h1 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">
                    Jessup Penalty Checker
                </h1>
                <div style="font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;">
                    Memorandum for the Applicant
                </div>
                <div style="background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
                            padding: 1.5rem; border-radius: 1rem; margin-bottom: 2rem;">
                    <div style="font-size: 0.875rem; color: #991b1b; margin-bottom: 0.5rem;">
                        Total Penalty Points
                    </div>
                    <div style="font-size: 2.5rem; font-weight: 700; color: #dc2626;">10</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Navigation
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
                <div class="nav-item">
                    <div style="display: flex; gap: 0.75rem; align-items: center;">
                        <div style="font-size: 1.25rem;">{icon}</div>
                        <div>
                            <div style="font-weight: 500; color: #0f172a;">{section}</div>
                            <div style="font-size: 0.75rem; color: #64748b;">{rule} - {points}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Main content
    st.markdown("""
        <h1 style="font-size: 2rem; font-weight: 700; color: #0f172a; margin-bottom: 2rem;">
            Jessup Memorial Penalty Checker
        </h1>
    """, unsafe_allow_html=True)

    # Summary Cards
    st.markdown("""
        <div class="summary-grid">
            <div class="summary-card">
                <div style="font-size: 0.875rem; color: #64748b;">Total Violations</div>
                <div style="font-size: 1.5rem; font-weight: 600; color: #dc2626;">3</div>
            </div>
            <div class="summary-card">
                <div style="font-size: 0.875rem; color: #64748b;">Word Count Status</div>
                <div style="font-size: 1.5rem; font-weight: 600; color: #22c55e;">Within Limits</div>
            </div>
            <div class="summary-card">
                <div style="font-size: 0.875rem; color: #64748b;">Required Parts</div>
                <div style="font-size: 1.5rem; font-weight: 600; color: #f59e0b;">7/8 Complete</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Penalty Score Table
    st.markdown("""
        <div class="modern-card">
            <div class="section-title">⚠️ Penalty Score Summary</div>
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
                            <div style="font-size: 0.75rem; color: #64748b;">2 points per part</div>
                        </td>
                        <td style="text-align: center;">4</td>
                        <td style="text-align: center;">2</td>
                    </tr>
                    <tr>
                        <td>Rule 5.17</td>
                        <td>
                            Non-Permitted Abbreviations (5 found)
                            <div style="font-size: 0.75rem; color: #64748b;">1 point each, max 3</div>
                        </td>
                        <td style="text-align: center;">3</td>
                        <td style="text-align: center;">0</td>
                    </tr>
                    <tr style="background-color: #f8fafc; font-weight: 600;">
                        <td colspan="2" style="text-align: right;">TOTAL</td>
                        <td style="text-align: center;">10</td>
                        <td style="text-align: center;">2</td>
                    </tr>
                </tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)

    # Create two columns for the layout
    col1, col2 = st.columns(2)

    with col1:
        # Cover Page Information
        st.markdown("""
            <div class="modern-card">
                <div class="section-title">📄 Cover Page Information</div>
        """, unsafe_allow_html=True)
        
        for key, value in initial_data["coverPage"].items():
            status = "success" if value["present"] else "error"
            st.markdown(f"""
                <div style="display: flex; justify-content: space-between; align-items: center; 
                            padding: 0.75rem; border-bottom: 1px solid #e2e8f0;">
                    <span style="color: #0f172a;">{key}</span>
                    {create_status_
