import streamlit as st
import pandas as pd
from typing import Dict, Any, List, Tuple
import json
from datetime import datetime

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': 'Jessup Memorial Penalty Checker v1.0'
    }
)

# Load data (keeping the same as before)
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

# Enhanced CSS with modern design elements
def load_custom_css():
    st.markdown("""
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* Main Layout */
        .stApp {
            background-color: #f8f9fa;
        }
        
        .main .block-container {
            padding: 3rem 2rem;
            max-width: 1400px;
        }
        
        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            color: #1a1f36;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Modern Card Design */
        .custom-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06);
            border: 1px solid rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .custom-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.06);
        }
        
        /* Enhanced Status Indicators */
        .status-indicator {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
            gap: 0.5rem;
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
            background-color: #fff7ed;
            color: #9a3412;
        }
        
        /* Modern Progress Bar */
        .progress-container {
            background: #f1f5f9;
            border-radius: 12px;
            height: 8px;
            overflow: hidden;
            margin: 0.5rem 0;
            position: relative;
        }
        
        .progress-bar {
            height: 100%;
            border-radius: 12px;
            transition: width 0.6s ease, background-color 0.3s ease;
        }
        
        /* Sidebar Enhancements */
        .css-1d391kg {
            background-color: white;
            border-right: 1px solid rgba(0,0,0,0.05);
        }
        
        .sidebar-item {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 0.75rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .sidebar-item:hover {
            background: #f8fafc;
            transform: translateX(4px);
        }
        
        /* Enhanced Table Design */
        .modern-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin: 1.5rem 0;
        }
        
        .modern-table th {
            background: #f8fafc;
            padding: 1rem;
            font-weight: 600;
            color: #475569;
            border-bottom: 2px solid #e2e8f0;
            text-align: left;
        }
        
        .modern-table td {
            padding: 1rem;
            border-bottom: 1px solid #e2e8f0;
            color: #1e293b;
        }
        
        .modern-table tr:hover td {
            background: #f8fafc;
        }
        
        /* Summary Cards */
        .summary-card {
            background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
            color: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }
        
        .summary-value {
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0.5rem 0;
        }
        
        /* Animations */
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .animate-slide-in {
            animation: slideIn 0.5s ease-out forwards;
        }
        
        /* Custom Expander */
        .streamlit-expander {
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        
        .streamlit-expander > div:first-child {
            padding: 1rem;
        }
        
        /* Word Count Labels */
        .word-count-label {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
            font-size: 0.875rem;
        }
        
        .word-count-value {
            font-weight: 500;
        }
        
        /* Tooltip styles */
        .tooltip {
            position: relative;
            display: inline-block;
        }
        
        .tooltip:hover::after {
            content: attr(data-tooltip);
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            padding: 0.5rem;
            background: #1e293b;
            color: white;
            border-radius: 4px;
            font-size: 0.75rem;
            white-space: nowrap;
            z-index: 1000;
        }
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #94a3b8;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #64748b;
        }
    </style>
    """, unsafe_allow_html=True)

class ModernWordCountDisplay:
    @staticmethod
    def create_progress_bar(count: int, limit: int) -> None:
        percentage = (count / limit) * 100
        status_color = "#10b981"  # Success green
        if percentage > 90:
            status_color = "#f59e0b"  # Warning yellow
        if percentage > 100:
            status_color = "#ef4444"  # Error red
        
        st.markdown(f"""
            <div class="custom-card">
                <div class="word-count-label">
                    <span class="word-count-value">{count:,} words</span>
                    <span style="color: {status_color};">{percentage:.1f}%</span>
                </div>
                <div class="progress-container">
                    <div class="progress-bar" 
                         style="width: {min(percentage, 100)}%; background-color: {status_color};">
                    </div>
                </div>
                <div style="text-align: right; font-size: 0.75rem; color: #64748b; margin-top: 0.5rem;">
                    Word limit: {limit:,}
                </div>
            </div>
        """, unsafe_allow_html=True)

class ModernNavigationMenu:
    @staticmethod
    def create_sidebar_item(icon: str, title: str, rule: str, points: str) -> None:
        st.markdown(f"""
            <div class="sidebar-item">
                <div style="display: flex; align-items: center; gap: 0.75rem;">
                    <span style="font-size: 1.25rem;">{icon}</span>
                    <span style="font-weight: 500;">{title}</span>
                </div>
                <div style="margin-top: 0.5rem; font-size: 0.75rem; color: #64748b;">
                    {rule} • {points}
                </div>
            </div>
        """, unsafe_allow_html=True)

class ModernStatusCard:
    @staticmethod
    def create_card(title: str, content: str, status: str = "default", icon: str = None) -> None:
        status_classes = {
            "success": "status-success",
            "error": "status-error",
            "warning": "status-warning"
        }
        
        st.markdown(f"""
            <div class="custom-card animate-slide-in">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <h3 style="font-size: 1.125rem; font-weight: 600;">{title}</h3>
                    {f'<span style="font-size: 1.25rem;">{icon}</span>' if icon else ''}
                </div>
                <div class="status-indicator {status_classes.get(status, '')}">
                    {content}
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    # Load data and CSS
    initial_data = load_initial_data()
    load_custom_css()
    
    # Sidebar
    with st.sidebar:
        st.title("Jessup Penalty Checker")
        
        # Memorial Type Display
        st.markdown(f"""
            <div class="summary-card">
                <div style="font-size: 0.875rem; opacity: 0.9;">Current Memorial</div>
                <div class="summary-value">Applicant</div>
                <div style="font-size: 0.75rem; opacity: 0.7;">
                    Last updated: {datetime.now().strftime('%B %d, %Y')}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Penalty Points Summary
        st.markdown("""
            <div class="custom-card">
                <div style="color: #64748b; font-size: 0.875rem;">Total Penalty Points</div>
                <div style="color: #ef4444; font-size: 3rem; font-weight: 700; margin: 0.5rem 0;">10</div>
                <div style="color: #64748b; font-size: 0.75rem;">
                    3 rule violations detected
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Navigation Items
        st.markdown("### Check Points")
        sections = [
            ("📄", "Cover Page", "Rule 5.6", "2 points"),
            ("✓", "Memorial Parts", "Rule 5.5", "2 points/part"),
            ("📏", "Length Check", "Rule 5.12", "varies"),
            ("🔒", "Anonymity", "Rule 5.14", "up to 10 points"),
            ("📝", "Tracked Changes", "Rule 5.4", "up to 5 points"),
            ("📚", "Citations", "Rule 5.13", "up to 5 points"),
            ("🖼️", "Media", "Rule 5.5(c)", "up to 5 points"),
            ("📑", "Abbreviations", "Rule 5.17", "max 3 points"),
            ("🔍", "Plagiarism", "Rule 11.2", "1-50 points")
        ]
        
        for icon, title, rule, points in sections:
            ModernNavigationMenu.create_sidebar_item(icon, title, rule, points)

    # Main Content
    st.title("Jessup Memorial Penalty Checker")
    
    # Score Breakdown
    with st.expander("📊 Penalty Score Summary", expanded=True):
        st.markdown("""
            <table class="modern-table">
                <thead>
                    <tr>
                        <th>Rule</th>
                        <th>Description</th>
                        <th>Points</th>
