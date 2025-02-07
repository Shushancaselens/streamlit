import streamlit as st
import pandas as pd
from typing import Dict, Any, List, Tuple
import json

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load initial data from a more maintainable structure
def load_initial_data() -> Dict[str, Any]:
    return {
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

# Enhanced CSS with better visual hierarchy and modern styling
def load_custom_css():
    st.markdown("""
    <style>
        /* Global Styles */
        .stApp {
            background-color: #f8f9fa;
        }
        
        /* Main Content Area */
        .main .block-container {
            padding-top: 2rem;
            max-width: 1200px;
        }
        
        /* Card Styling */
        .custom-card {
            background-color: white;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border: 1px solid #e9ecef;
        }
        
        /* Headers */
        .card-header {
            font-size: 1.25rem;
            font-weight: 600;
            color: #1a1f36;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        /* Progress Bars */
        .word-count-bar {
            background-color: #e9ecef;
            border-radius: 8px;
            height: 8px;
            overflow: hidden;
            margin: 0.5rem 0;
        }
        
        .word-count-progress {
            height: 100%;
            transition: width 0.3s ease;
        }
        
        /* Status Indicators */
        .status-icon {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.9rem;
        }
        
        .status-icon.success { color: #10b981; }
        .status-icon.error { color: #ef4444; }
        .status-icon.warning { color: #f59e0b; }
        
        /* Sidebar Enhancements */
        .css-1d391kg {
            background-color: white;
            padding: 2rem 1rem;
        }
        
        .sidebar-nav-item {
            padding: 0.75rem;
            border-radius: 6px;
            margin-bottom: 0.5rem;
            cursor: pointer;
            transition: all 0.2s;
            border: 1px solid #e9ecef;
        }
        
        .sidebar-nav-item:hover {
            background-color: #f8f9fa;
            transform: translateX(2px);
        }
        
        /* Tables */
        .styled-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin: 1rem 0;
        }
        
        .styled-table th {
            background-color: #f8f9fa;
            padding: 0.75rem;
            text-align: left;
            font-weight: 600;
            color: #4b5563;
            border-bottom: 2px solid #e5e7eb;
        }
        
        .styled-table td {
            padding: 0.75rem;
            border-bottom: 1px solid #e5e7eb;
        }
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .animate-fade-in {
            animation: fadeIn 0.3s ease-out;
        }
    </style>
    """, unsafe_allow_html=True)

class WordCountDisplay:
    @staticmethod
    def create_progress_bar(count: int, limit: int) -> None:
        percentage = (count / limit) * 100
        color = "#10b981"  # Default green
        if percentage > 90:
            color = "#f59e0b"  # Warning yellow
        if percentage > 100:
            color = "#ef4444"  # Error red
        
        st.markdown(f"""
            <div class="custom-card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span style="font-weight: 500;">{count:,} words</span>
                    <span style="color: {color};">{percentage:.1f}%</span>
                </div>
                <div class="word-count-bar">
                    <div class="word-count-progress" style="width: {min(percentage, 100)}%; background-color: {color};"></div>
                </div>
                <div style="text-align: right; font-size: 0.8rem; color: #6b7280;">
                    Limit: {limit:,} words
                </div>
            </div>
        """, unsafe_allow_html=True)

class NavigationMenu:
    @staticmethod
    def create_sidebar_navigation(sections: List[Tuple[str, str, str]]) -> None:
        for icon, title, rule, points in sections:
            st.markdown(f"""
                <div class="sidebar-nav-item">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span>{icon}</span>
                        <span style="font-weight: 500;">{title}</span>
                    </div>
                    <div style="font-size: 0.8rem; color: #6b7280; margin-top: 0.25rem;">
                        {rule} - {points}
                    </div>
                </div>
            """, unsafe_allow_html=True)

class StatusCard:
    @staticmethod
    def create_card(title: str, content: str, status: str = "default") -> None:
        status_classes = {
            "success": "success",
            "error": "error",
            "warning": "warning",
            "default": ""
        }
        st.markdown(f"""
            <div class="custom-card animate-fade-in">
                <div class="card-header">
                    {title}
                </div>
                <div class="status-icon {status_classes.get(status, '')}">
                    {content}
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    # Load data and CSS
    initial_data = load_initial_data()
    load_custom_css()
    
    # Sidebar Configuration
    with st.sidebar:
        st.title("Jessup Penalty Checker")
        st.markdown(f"### Memorandum for the {initial_data['memorialType']}")
        
        st.markdown("""
            <div class="custom-card">
                <div style="color: #6b7280; font-size: 0.9rem;">Total Penalty Points</div>
                <div style="color: #ef4444; font-size: 2.5rem; font-weight: 700;">10</div>
                <div style="color: #6b7280; font-size: 0.8rem;">points deducted</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Navigation Menu
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
        NavigationMenu.create_sidebar_navigation(sections)

    # Main Content
    st.title("Jessup Memorial Penalty Checker")
    
    # Score Breakdown
    with st.expander("Penalty Score Summary", expanded=True):
        st.markdown("""
            <table class="styled-table">
                <thead>
                    <tr>
                        <th>Rule</th>
                        <th>Description</th>
                        <th>Points</th>
                        <th>Reviewed</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Rule 5.5</td>
                        <td>Missing Prayer for Relief</td>
                        <td>4</td>
                        <td>✓</td>
                    </tr>
                    <tr>
                        <td>Rule 5.17</td>
                        <td>Non-Permitted Abbreviations (5 found)</td>
                        <td>3</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <td>Rule 5.13</td>
                        <td>Improper Citation</td>
                        <td>3</td>
                        <td>-</td>
                    </tr>
                    <tr style="font-weight: 600; background-color: #f8f9fa;">
                        <td colspan="2" style="text-align: right;">Total</td>
                        <td>10</td>
                        <td>1/3</td>
                    </tr>
                </tbody>
            </table>
        """, unsafe_allow_html=True)

    # Main content grid
    col1, col2 = st.columns(2)
    
    with col1:
        # Cover Page Information
        StatusCard.create_card(
            "Cover Page Information",
            "\n".join(f"{key}: {value['found']}" for key, value in initial_data['coverPage'].items())
        )
        
        # Word Count Analysis
        st.markdown("### Word Count Analysis")
        for section, data in initial_data['wordCounts'].items():
            WordCountDisplay.create_progress_bar(data['count'], data['limit'])
            
        # Citations Check
        StatusCard.create_card(
            "Citations Check",
            "⚠️ 5 instances of improper citation format detected",
            "warning"
        )
        
    with col2:
        # Memorial Parts
        StatusCard.create_card(
            "Memorial Parts",
            "\n".join(f"{'✓' if present else '✗'} {part}" 
                     for part, present in initial_data['memorialParts'].items())
        )
        
        # Anonymity Check
        StatusCard.create_card(
            "Anonymity Check",
            "✅ No anonymity violations found\nNo disclosure of school, team members, or country",
            "success"
        )
        
        # Tracked Changes
        StatusCard.create_card(
            "Tracked Changes",
            "✅ No tracked changes found\n✅ No comments found",
            "success"
        )
    
    # Full-width sections
    st.markdown("### Abbreviations")
    for abbr, info in initial_data['abbreviations'].items():
        with st.expander(f"{abbr} ({info['count']} occurrences)"):
            st.markdown(f"Found in: {', '.join(info['sections'])}")
    
    # Media and Plagiarism checks
    col1, col2 = st.columns(2)
    with col1:
        StatusCard.create_card(
            "Media Check",
            "\n".join(f"⚠️ Found in {item['section']}: {item['text']}" 
                     for item in initial_data['media']),
            "warning"
        )
    
    with col2:
        StatusCard.create_card(
            "Plagiarism Check",
            "✅ No plagiarism detected",
            "success"
        )

if __name__ == "__main__":
    main()
