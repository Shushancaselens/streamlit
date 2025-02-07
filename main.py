import streamlit as st
import pandas as pd
from typing import Dict, Any, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime
import json

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.ilsa.org/jessup-competition/',
        'Report a bug': "mailto:support@jessup.org",
        'About': "Jessup Memorial Penalty Checker v2.0"
    }
)

@dataclass
class PenaltyRule:
    """Data class for penalty rules"""
    rule_id: str
    title: str
    description: str
    max_points: int
    points_description: str
    icon: str

@dataclass
class PenaltyStatus:
    """Data class for penalty status"""
    points: int
    description: str
    details: Optional[str]
    status: str  # 'success', 'warning', 'error'

class JessupDataManager:
    """Manages Jessup memorial data and calculations"""
    
    @staticmethod
    def load_initial_data() -> Dict[str, Any]:
        # Your existing initial_data dictionary here
        return {
            "memorialType": "Applicant",
            "coverPage": {
                "Team Number": {"present": True, "found": "349A"},
                "Court Name": {"present": True, "found": "International Court of Justice"},
                "Year": {"present": True, "found": "2025"},
                "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
                "Memorial Type": {"present": True, "found": "Memorial for the Applicant"}
            },
            # ... rest of your initial data ...
        }

    @staticmethod
    def calculate_total_penalties(data: Dict[str, Any]) -> int:
        # Add logic to calculate total penalties
        return 10

    @staticmethod
    def get_penalty_rules() -> List[PenaltyRule]:
        return [
            PenaltyRule("cover", "Cover Page", "Basic memorial information", 2, "2 points", "📄"),
            PenaltyRule("parts", "Memorial Parts", "Required sections check", 16, "2 points per part", "✓"),
            # ... add all rules ...
        ]

class UIComponents:
    """Enhanced UI components with animations and interactions"""
    
    @staticmethod
    def custom_css() -> None:
        st.markdown("""
        <style>
            /* Add your existing CSS here and these new styles */
            
            /* Modern Dashboard Layout */
            .dashboard-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 1.5rem;
                padding: 1.5rem;
            }
            
            /* Enhanced Card Design */
            .modern-card {
                background: white;
                border-radius: 12px;
                padding: 1.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
                           0 2px 4px -1px rgba(0, 0, 0, 0.06);
                transition: transform 0.2s, box-shadow 0.2s;
            }
            
            .modern-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
                           0 4px 6px -2px rgba(0, 0, 0, 0.05);
            }
            
            /* Glassmorphism Effects */
            .glass-card {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.125);
            }
            
            /* Progress Indicators */
            .circular-progress {
                position: relative;
                width: 120px;
                height: 120px;
                border-radius: 50%;
                background: conic-gradient(from 0deg,
                    var(--progress-color) calc(var(--progress) * 1%),
                    #eceff1 calc(var(--progress) * 1%));
            }
            
            /* Improved Typography */
            .section-title {
                font-size: 1.25rem;
                font-weight: 600;
                color: #1a1f36;
                margin-bottom: 1rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            
            /* Interactive Elements */
            .hover-action {
                transition: all 0.2s;
                cursor: pointer;
            }
            
            .hover-action:hover {
                background-color: #f8f9fa;
                transform: scale(1.01);
            }
            
            /* Status Badges */
            .status-badge {
                display: inline-flex;
                align-items: center;
                padding: 0.25rem 0.75rem;
                border-radius: 9999px;
                font-size: 0.875rem;
                font-weight: 500;
            }
            
            .status-badge.success {
                background-color: #d1fae5;
                color: #065f46;
            }
            
            .status-badge.warning {
                background-color: #fef3c7;
                color: #92400e;
            }
            
            .status-badge.error {
                background-color: #fee2e2;
                color: #991b1b;
            }
            
            /* Tooltips */
            [data-tooltip] {
                position: relative;
            }
            
            [data-tooltip]:before {
                content: attr(data-tooltip);
                position: absolute;
                bottom: 100%;
                left: 50%;
                transform: translateX(-50%);
                padding: 0.5rem;
                background: #1f2937;
                color: white;
                border-radius: 0.375rem;
                font-size: 0.875rem;
                opacity: 0;
                pointer-events: none;
                transition: opacity 0.2s;
            }
            
            [data-tooltip]:hover:before {
                opacity: 1;
            }
            
            /* Advanced Data Tables */
            .advanced-table {
                width: 100%;
                border-spacing: 0;
                border-collapse: separate;
                border-radius: 8px;
                overflow: hidden;
            }
            
            .advanced-table th {
                background-color: #f8fafc;
                padding: 1rem;
                text-align: left;
                font-weight: 600;
                color: #475569;
            }
            
            .advanced-table td {
                padding: 1rem;
                border-top: 1px solid #e2e8f0;
            }
            
            .advanced-table tr:hover td {
                background-color: #f8fafc;
            }
        </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def create_penalty_card(rule: PenaltyRule, status: PenaltyStatus) -> None:
        st.markdown(f"""
            <div class="modern-card glass-card hover-action">
                <div class="section-title">
                    {rule.icon} {rule.title}
                    <span class="status-badge {status.status}">
                        {status.points} points
                    </span>
                </div>
                <div>
                    {status.description}
                    {f'<div class="text-sm text-gray-600 mt-2">{status.details}</div>' if status.details else ''}
                </div>
            </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def create_word_count_display(section: str, count: int, limit: int) -> None:
        percentage = (count / limit) * 100
        progress_color = (
            "#10b981" if percentage <= 90 else
            "#f59e0b" if percentage <= 100 else
            "#ef4444"
        )
        
        st.markdown(f"""
            <div class="modern-card">
                <div class="section-title">{section}</div>
                <div class="circular-progress" style="
                    --progress: {min(percentage, 100)};
                    --progress-color: {progress_color};
                ">
                    <div class="progress-label">
                        {percentage:.1f}%
                    </div>
                </div>
                <div class="mt-4 flex justify-between text-sm">
                    <span>Current: {count:,} words</span>
                    <span>Limit: {limit:,} words</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

class JessupPenaltyChecker:
    """Main application class"""
    
    def __init__(self):
        self.data_manager = JessupDataManager()
        self.ui = UIComponents()
        self.initial_data = self.data_manager.load_initial_data()
        
    def run(self):
        self.ui.custom_css()
        self.render_sidebar()
        self.render_main_content()
    
    def render_sidebar(self):
        with st.sidebar:
            st.title("Jessup Penalty Checker")
            self.render_penalty_summary()
            self.render_navigation()
    
    def render_penalty_summary(self):
        total_penalties = self.data_manager.calculate_total_penalties(self.initial_data)
        st.markdown(f"""
            <div class="modern-card glass-card">
                <div class="text-sm text-gray-600">Total Penalty Points</div>
                <div class="text-4xl font-bold text-red-600">{total_penalties}</div>
                <div class="text-xs text-gray-500">Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}</div>
            </div>
        """, unsafe_allow_html=True)
    
    def render_navigation(self):
        for rule in self.data_manager.get_penalty_rules():
            st.markdown(f"""
                <div class="sidebar-nav-item hover-action" data-tooltip="{rule.points_description}">
                    <div class="flex items-center gap-2">
                        {rule.icon} {rule.title}
                    </div>
                    <div class="text-sm text-gray-600">{rule.rule_id}</div>
                </div>
            """, unsafe_allow_html=True)
    
    def render_main_content(self):
        st.title("Memorial Analysis Dashboard")
        
        # Score Summary
        with st.expander("Detailed Penalty Analysis", expanded=True):
            self.render_penalty_table()
        
        # Main Grid Layout
        self.render_analysis_grid()
    
    def render_penalty_table(self):
        st.markdown("""
            <table class="advanced-table">
                <thead>
                    <tr>
                        <th>Rule</th>
                        <th>Description</th>
                        <th>Points</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Add your penalty rows here -->
                </tbody>
            </table>
        """, unsafe_allow_html=True)
    
    def render_analysis_grid(self):
        st.markdown('<div class="dashboard-grid">', unsafe_allow_html=True)
        # Add your analysis cards here
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    app = JessupPenaltyChecker()
    app.run()

if __name__ == "__main__":
    main()
