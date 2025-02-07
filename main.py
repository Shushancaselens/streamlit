import streamlit as st
import pandas as pd
from typing import Dict, Any, List, Tuple, Optional
from dataclasses import dataclass
import json

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

@dataclass
class PenaltyRule:
    rule: str
    description: str
    points: int
    reviewed: bool
    details: str

@dataclass
class WordCount:
    count: int
    limit: int
    section: str

class ThemeColors:
    PRIMARY = "#4D68F9"  # Matches the React logo color
    SUCCESS = "#10B981"
    WARNING = "#F59E0B"
    ERROR = "#EF4444"
    GRAY = {
        50: "#F9FAFB",
        100: "#F3F4F6",
        200: "#E5E7EB",
        300: "#D1D5DB",
        400: "#9CA3AF",
        500: "#6B7280",
        600: "#4B5563",
        700: "#374151",
        800: "#1F2937",
        900: "#111827"
    }

def load_custom_css():
    st.markdown("""
    <style>
        /* Reset and Base Styles */
        .stApp {
            background-color: #f8f9fa;
        }
        
        /* Typography */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Layout */
        .main .block-container {
            padding-top: 2rem;
            max-width: 1200px;
        }
        
        /* Card Components */
        .card {
            background-color: white;
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06);
            border: 1px solid rgb(229, 231, 235);
            transition: all 0.2s ease;
        }
        
        .card:hover {
            box-shadow: 0 4px 6px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.06);
        }
        
        /* Headers */
        .section-header {
            font-size: 1.25rem;
            font-weight: 600;
            color: #111827;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        /* Progress Bars */
        .progress-container {
            margin: 0.75rem 0;
        }
        
        .progress-bar {
            width: 100%;
            height: 6px;
            background-color: #E5E7EB;
            border-radius: 9999px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            transition: width 0.3s ease, background-color 0.3s ease;
        }
        
        /* Status Indicators */
        .status-indicator {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
        }
        
        .status-success {
            background-color: rgba(16, 185, 129, 0.1);
            color: #10B981;
        }
        
        .status-error {
            background-color: rgba(239, 68, 68, 0.1);
            color: #EF4444;
        }
        
        .status-warning {
            background-color: rgba(245, 158, 11, 0.1);
            color: #F59E0B;
        }
        
        /* Sidebar Enhancements */
        .css-1d391kg {
            background-color: white;
            border-right: 1px solid #E5E7EB;
        }
        
        .sidebar-item {
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            margin-bottom: 0.5rem;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 1px solid #E5E7EB;
            background-color: white;
        }
        
        .sidebar-item:hover {
            background-color: #F9FAFB;
            transform: translateX(2px);
        }
        
        /* Table Styles */
        .styled-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin: 1rem 0;
        }
        
        .styled-table th {
            background-color: #F9FAFB;
            padding: 0.75rem 1rem;
            text-align: left;
            font-weight: 600;
            color: #4B5563;
            border-bottom: 2px solid #E5E7EB;
        }
        
        .styled-table td {
            padding: 0.75rem 1rem;
            border-bottom: 1px solid #E5E7EB;
            color: #374151;
        }
        
        /* Animations */
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .animate-slide-in {
            animation: slideIn 0.3s ease-out forwards;
        }
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #F3F4F6;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #9CA3AF;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #6B7280;
        }

        /* Alert Components */
        .alert {
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
        }

        .alert-title {
            font-weight: 600;
            margin-bottom: 0.25rem;
        }

        .alert-success {
            background-color: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.2);
        }

        .alert-warning {
            background-color: rgba(245, 158, 11, 0.1);
            border: 1px solid rgba(245, 158, 11, 0.2);
        }

        .alert-error {
            background-color: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.2);
        }

        /* Logo */
        .logo-container {
            margin-bottom: 1.5rem;
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

        /* Expandable Sections */
        .expandable-section {
            border: 1px solid #E5E7EB;
            border-radius: 0.5rem;
            margin-bottom: 0.5rem;
        }

        .expandable-header {
            padding: 1rem;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #F9FAFB;
        }

        .expandable-content {
            padding: 1rem;
            border-top: 1px solid #E5E7EB;
        }
    </style>
    """, unsafe_allow_html=True)

class WordCountBar:
    @staticmethod
    def render(word_count: WordCount) -> None:
        percentage = (word_count.count / word_count.limit) * 100
        color = ThemeColors.SUCCESS
        if percentage > 90:
            color = ThemeColors.WARNING
        if percentage > 100:
            color = ThemeColors.ERROR
            
        st.markdown(f"""
            <div class="card progress-container">
                <div class="word-count-label">
                    <span>{word_count.section}</span>
                    <span class="word-count-value" style="color: {color}">
                        {percentage:.1f}%
                    </span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" 
                         style="width: {min(percentage, 100)}%; background-color: {color};">
                    </div>
                </div>
                <div style="text-align: right; font-size: 0.75rem; color: #6B7280; margin-top: 0.25rem;">
                    {word_count.count:,} / {word_count.limit:,} words
                </div>
            </div>
        """, unsafe_allow_html=True)

class Alert:
    @staticmethod
    def render(title: str, description: Optional[str] = None, alert_type: str = "success") -> None:
        icon = "✓" if alert_type == "success" else "⚠️" if alert_type == "warning" else "✗"
        st.markdown(f"""
            <div class="alert alert-{alert_type}">
                <div class="alert-icon">{icon}</div>
                <div>
                    <div class="alert-title">{title}</div>
                    {f'<div class="alert-description">{description}</div>' if description else ''}
                </div>
            </div>
        """, unsafe_allow_html=True)

class SidebarNavigation:
    @staticmethod
    def render(items: List[Dict[str, str]]) -> None:
        for item in items:
            st.markdown(f"""
                <div class="sidebar-item">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span>{item['icon']}</span>
                        <span style="font-weight: 500;">{item['label']}</span>
                    </div>
                    <div style="font-size: 0.75rem; color: #6B7280; margin-top: 0.25rem;">
                        {item['rule']} - {item['points']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

def create_penalty_card(title: str, rule: str, points: str, content: str) -> None:
    st.markdown(f"""
        <div class="card">
            <div class="section-header">
                {title}
                <span style="font-size: 0.75rem; color: #6B7280;">({rule} - {points})</span>
            </div>
            <div>{content}</div>
        </div>
    """, unsafe_allow_html=True)

def main():
    # Load initial data
    data = {
        # ... (Your existing data structure here)
    }
    
    # Load custom CSS
    load_custom_css()
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
            <div class="logo-container">
                <svg viewBox="0 0 1007 261" style="height: 48px;">
                    <!-- Your existing SVG path data here -->
                </svg>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="card" style="text-align: center;">
                <div style="color: #6B7280; font-size: 0.875rem;">Total Penalty Points</div>
                <div style="color: #EF4444; font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0;">10</div>
                <div style="color: #6B7280; font-size: 0.75rem;">points deducted</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Navigation items
        nav_items = [
            {"icon": "📄", "label": "Cover Page", "rule": "Rule 5.6", "points": "2 points"},
            # ... (Your existing navigation items)
        ]
        SidebarNavigation.render(nav_items)

    # Main content
    st.title("Jessup Memorial Penalty Checker")
    
    # Penalty Score Summary
    with st.expander("Penalty Score Summary", expanded=True):
        penalties = [
            PenaltyRule("Rule 5.5", "Missing Prayer for Relief", 4, True, "2 points per part"),
            # ... (Your existing penalties)
        ]
        
        st.markdown("""
            <table class="styled-table">
                <!-- Your existing table structure -->
            </table>
        """, unsafe_allow_html=True)

    # Main content grid
    col1, col2 = st.columns(2)
    
    with col1:
        # Cover Page Information
        create_penalty_card(
            "Cover Page Information",
            "Rule 5.6",
            "2 points",
            # Your existing cover page content
        )
        
        # Word Count Analysis
        st.markdown("### Word Count Analysis")
        word_counts = [
            WordCount(1196, 1200, "Statement of Facts"),
            # ... (Your existing word counts)
        ]
        for wc in word_counts:
            WordCountBar.render(wc)
    
    with col2:
        # Memorial Parts
        create_penalty_card(
            "Memorial Parts",
            "Rule 5.5",
            "2 points per part",
            # Your existing memorial parts content
        )
        
        # Alerts
        Alert.render(
            "No anonymity violations found",
            "No disclosure of school, team members, or country",
            "success"
        )
        
        Alert.render(
            "Found improper citations",
            "5 instances of improper citation format detected",
            "warning"
        )

    # Additional sections...
    # (Continue with your existing sections, using the new components and styling)

if __name__ == "__main__":
    main()
