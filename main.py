import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class PenaltyData:
    memorialType: str
    coverPage: Dict
    wordCounts: Dict
    penalties: List[Dict]
    totalPenalties: int

def create_word_count_chart(counts: Dict, title: str):
    sections = list(counts.keys())
    current = [counts[s]['count'] for s in sections]
    limits = [counts[s]['limit'] for s in sections]
    
    fig = go.Figure(data=[
        go.Bar(name='Current', x=sections, y=current),
        go.Bar(name='Limit', x=sections, y=limits, opacity=0.5)
    ])
    
    fig.update_layout(
        title=title,
        barmode='overlay',
        height=300,
        margin=dict(t=30, b=30)
    )
    
    return fig

def custom_metric(label, value, delta=None, color="normal"):
    color_map = {
        "normal": "rgb(55, 65, 81)",
        "warning": "rgb(234, 88, 12)",
        "danger": "rgb(220, 38, 38)"
    }
    
    return components.html(
        f"""
        <div style="padding: 1rem; background: white; border-radius: 0.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1)">
            <div style="color: {color_map[color]}; font-size: 0.875rem; font-weight: 500;">
                {label}
            </div>
            <div style="font-size: 1.875rem; font-weight: 700; margin-top: 0.25rem;">
                {value}
            </div>
            {f'<div style="color: rgb(156, 163, 175); font-size: 0.75rem;">{delta}</div>' if delta else ''}
        </div>
        """
    )

def main():
    st.set_page_config(layout="wide", page_title="Jessup Penalty Checker")
    
    # Sample data
    applicant_data = PenaltyData(
        memorialType="Applicant",
        coverPage={
            "Team Number": {"present": True, "found": "349A"},
            "Court Name": {"present": True, "found": "International Court of Justice"},
            "Year": {"present": True, "found": "2025"},
            "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
            "Memorial Type": {"present": True, "found": "Memorial for the Applicant"}
        },
        wordCounts={
            "Statement of Facts": {"count": 1196, "limit": 1200},
            "Summary of Pleadings": {"count": 642, "limit": 700},
            "Pleadings": {"count": 9424, "limit": 9500},
            "Prayer for Relief": {"count": 198, "limit": 200}
        },
        penalties=[
            {"rule": "Rule 5.17", "description": "Non-Permitted Abbreviations", "points": 3, "details": "1 point each"},
            {"rule": "Rule 5.13", "description": "Improper Citation", "points": 2, "details": "2 instances"}
        ],
        totalPenalties=5
    )
    
    respondent_data = PenaltyData(
        memorialType="Respondent",
        coverPage={
            "Team Number": {"present": True, "found": "349B"},
            "Court Name": {"present": True, "found": "International Court of Justice"},
            "Year": {"present": True, "found": "2025"},
            "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
            "Memorial Type": {"present": True, "found": "Memorial for the Respondent"}
        },
        wordCounts={
            "Statement of Facts": {"count": 1180, "limit": 1200},
            "Summary of Pleadings": {"count": 695, "limit": 700},
            "Pleadings": {"count": 9490, "limit": 9500},
            "Prayer for Relief": {"count": 195, "limit": 200}
        },
        penalties=[
            {"rule": "Rule 5.17", "description": "Non-Permitted Abbreviations", "points": 2, "details": "2 instances"},
            {"rule": "Rule 5.14", "description": "Anonymity Violation", "points": 5, "details": "School name mentioned"}
        ],
        totalPenalties=7
    )
    
    # Header
    st.title("Jessup Memorial Penalty Checker")
    
    # Top metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        custom_metric(
            "Total Penalties",
            f"{applicant_data.totalPenalties + respondent_data.totalPenalties} points",
            "Combined team penalties",
            "danger" if applicant_data.totalPenalties + respondent_data.totalPenalties > 10 else "warning"
        )
    with col2:
        custom_metric(
            "Applicant Penalties",
            f"{applicant_data.totalPenalties} points",
            color="warning"
        )
    with col3:
        custom_metric(
            "Respondent Penalties",
            f"{respondent_data.totalPenalties} points",
            color="danger"
        )
    
    # Memorial comparisons
    tab1, tab2 = st.tabs(["Word Counts", "Penalties"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(
                create_word_count_chart(applicant_data.wordCounts, "Applicant Word Counts"),
                use_container_width=True
            )
        with col2:
            st.plotly_chart(
                create_word_count_chart(respondent_data.wordCounts, "Respondent Word Counts"),
                use_container_width=True
            )
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Applicant Penalties")
            for penalty in applicant_data.penalties:
                with st.expander(f"{penalty['description']} ({penalty['points']} points)"):
                    st.write(f"Rule: {penalty['rule']}")
                    st.write(f"Details: {penalty['details']}")
        
        with col2:
            st.subheader("Respondent Penalties")
            for penalty in respondent_data.penalties:
                with st.expander(f"{penalty['description']} ({penalty['points']} points)"):
                    st.write(f"Rule: {penalty['rule']}")
                    st.write(f"Details: {penalty['details']}")
    
    # Cover page comparison
    st.header("Cover Page Analysis")
    df_cover = pd.DataFrame({
        'Field': applicant_data.coverPage.keys(),
        'Applicant': [v['found'] for v in applicant_data.coverPage.values()],
        'Respondent': [v['found'] for v in respondent_data.coverPage.values()]
    })
    st.dataframe(df_cover, use_container_width=True)

if __name__ == "__main__":
    main()
