import streamlit as st
import pandas as pd
from pathlib import Path
import json
from typing import Dict, List, Union, Optional

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Data Models ---
class PenaltyData:
    def __init__(self, file_path: Optional[str] = None):
        self.data = {
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
        if file_path:
            self.load_from_file(file_path)

    def load_from_file(self, file_path: str):
        with open(file_path, 'r') as f:
            self.data = json.load(f)

    def calculate_total_penalties(self) -> int:
        total = 0
        # Add penalty calculations based on rules
        if not self.data["memorialParts"]["Prayer for Relief"]:
            total += 4
        total += min(len(self.data["abbreviations"]), 3)
        # Add other penalty calculations
        return total

# --- UI Components ---
def load_custom_css():
    st.markdown("""
        <style>
        /* Main container */
        .main {
            padding: 2rem;
            background-color: #f8f9fa;
        }
        
        /* Enhanced card styling */
        .stCard {
            background-color: white;
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .stCard:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        
        /* Progress bars */
        .progress-container {
            background: white;
            padding: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .progress-bar {
            height: 0.5rem;
            border-radius: 0.25rem;
            background: #e9ecef;
            margin: 0.5rem 0;
            overflow: hidden;
        }
        
        .progress-bar-fill {
            height: 100%;
            border-radius: 0.25rem;
            transition: width 0.3s ease;
        }
        
        /* Status indicators */
        .status-indicator {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
        }
        
        .status-success {
            background-color: #d1fae5;
            color: #047857;
        }
        
        .status-error {
            background-color: #fee2e2;
            color: #dc2626;
        }
        
        .status-warning {
            background-color: #fef3c7;
            color: #d97706;
        }
        
        /* Sidebar enhancements */
        .css-1d391kg {
            background-color: white;
            padding: 2rem 1rem;
        }
        
        /* Section titles */
        .section-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: #111827;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e5e7eb;
        }
        
        /* Enhanced tables */
        .styled-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin: 1rem 0;
        }
        
        .styled-table th {
            background-color: #f8f9fa;
            padding: 0.75rem;
            font-weight: 600;
            text-align: left;
            border-bottom: 2px solid #e5e7eb;
        }
        
        .styled-table td {
            padding: 0.75rem;
            border-bottom: 1px solid #e5e7eb;
        }
        
        /* Buttons and interactive elements */
        .custom-button {
            display: inline-flex;
            align-items: center;
            padding: 0.5rem 1rem;
            border-radius: 0.375rem;
            font-weight: 500;
            color: white;
            background-color: #3b82f6;
            transition: background-color 0.2s;
        }
        
        .custom-button:hover {
            background-color: #2563eb;
        }
        
        /* Tooltips */
        .tooltip {
            position: relative;
            display: inline-block;
        }
        
        .tooltip .tooltip-text {
            visibility: hidden;
            background-color: #374151;
            color: white;
            text-align: center;
            padding: 0.5rem;
            border-radius: 0.375rem;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.2s;
        }
        
        .tooltip:hover .tooltip-text {
            visibility: visible;
            opacity: 1;
        }
        </style>
    """, unsafe_allow_html=True)

def create_sidebar(data: PenaltyData):
    with st.sidebar:
        st.title("Jessup Penalty Checker")
        
        # Memorial Type with enhanced styling
        st.markdown(f"""
            <div style='
                background-color: #f8f9fa;
                padding: 1rem;
                border-radius: 0.5rem;
                border-left: 4px solid #3b82f6;
                margin-bottom: 1.5rem;
            '>
                <div style='color: #666; font-size: 0.875rem;'>Memorial Type</div>
                <div style='font-size: 1.25rem; font-weight: 600; color: #1f2937;'>
                    {data.data['memorialType']}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Penalty Points Summary
        total_penalties = data.calculate_total_penalties()
        st.markdown(f"""
            <div style='
                background-color: #fee2e2;
                padding: 1.5rem;
                border-radius: 0.75rem;
                text-align: center;
                margin-bottom: 2rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            '>
                <div style='color: #991b1b; font-size: 0.875rem; font-weight: 500;'>
                    Total Penalty Points
                </div>
                <div style='
                    color: #dc2626;
                    font-size: 2.5rem;
                    font-weight: 700;
                    line-height: 1;
                    margin: 0.5rem 0;
                '>
                    {total_penalties}
                </div>
                <div style='color: #991b1b; font-size: 0.75rem;'>points deducted</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Navigation Menu
        st.markdown("### Navigation")
        menu_items = [
            ("📄", "Cover Page", "Rule 5.6"),
            ("📋", "Memorial Parts", "Rule 5.5"),
            ("📏", "Word Counts", "Rule 5.12"),
            ("🔒", "Anonymity", "Rule 5.14"),
            ("📝", "Citations", "Rule 5.13"),
            ("🖼️", "Media", "Rule 5.5(c)"),
            ("📑", "Abbreviations", "Rule 5.17")
        ]
        
        for icon, title, rule in menu_items:
            st.markdown(f"""
                <div style='
                    padding: 0.75rem;
                    background-color: white;
                    border-radius: 0.5rem;
                    margin-bottom: 0.5rem;
                    cursor: pointer;
                    transition: all 0.2s;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    border: 1px solid #e5e7eb;
                '>
                    <div style='display: flex; align-items: center;'>
                        <span style='font-size: 1.25rem; margin-right: 0.5rem;'>{icon}</span>
                        <div>
                            <div style='font-weight: 500; color: #1f2937;'>{title}</div>
                            <div style='font-size: 0.75rem; color: #6b7280;'>{rule}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

def create_header():
    st.markdown("""
        <div style='
            background-color: white;
            padding: 2rem;
            border-radius: 0.75rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        '>
            <h1 style='
                margin: 0;
                color: #111827;
                font-size: 2rem;
                font-weight: 700;
            '>Jessup Memorial Penalty Checker</h1>
            <p style='
                margin: 0.5rem 0 0 0;
                color: #6b7280;
                font-size: 1rem;
            '>Automated compliance checking for Jessup Memorial submissions</p>
        </div>
    """, unsafe_allow_html=True)

def create_penalty_summary(data: PenaltyData):
    penalties = [
        ("Rule 5.5", "Missing Prayer for Relief", 4, "2 points per part"),
        ("Rule 5.17", "Non-Permitted Abbreviations", 3, "1 point each, max 3"),
        ("Rule 5.13", "Improper Citations", 3, "1 point per violation, max 5")
    ]
    
    st.markdown("""
        <div class="stCard">
            <h2 class="section-title">Penalty Summary</h2>
            <table class="styled-table">
                <thead>
                    <tr>
                        <th>Rule</th>
                        <th>Description</th>
                        <th>Points</th>
                        <th>Details</th>
                    </tr>
                </thead>
                <tbody>
    """, unsafe_allow_html=True)
    
    for rule, desc, points, details in penalties:
        st.markdown(f"""
            <tr>
                <td>{rule}</td>
                <td>{desc}</td>
                <td>{points}</td>
                <td>{details}</td>
            </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("""
                </tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)

def main():
    # Load custom CSS
    load_custom_css()
    
    # Initialize data
    data = PenaltyData()
    
    # Create sidebar
    create_sidebar(data)
    
    # Main content
    create_header()
    
    # Create penalty summary
    create_penalty_summary(data)
    
    # Create main content sections in tabs
    tabs = st.tabs(["Overview", "Word Counts", "Citations", "Media", "Abbreviations"])
    
    with tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                <div class="stCard">
                    <h3>Cover Page Information</h3>
                    <!-- Cover page content -->
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div class="stCard">
                    <h3>Memorial Parts</h3>
                    <!-- Memorial parts content -->
                </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.markdown("""
            <div class="stCard">
                <h3>Word Count Analysis</h3>
                <!-- Word count content -->
            </div>
        """, unsafe_allow_html=True)
    
    # Add other sections...

if __name__ == "__main__":
    main()
