import streamlit as st
import pandas as pd
from typing import Dict, List, Any
import plotly.graph_objects as go

# Custom Components
def custom_card(title: str, content: Any, rule_text: str = None):
    """Custom card component with consistent styling"""
    st.markdown("""
        <div style='
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 16px;
            background-color: white;
            margin-bottom: 16px;
        '>
            <h3 style='
                font-size: 16px;
                margin-bottom: 8px;
                display: flex;
                align-items: center;
            '>
                {title}
                {rule_text_html}
            </h3>
            <div style='padding-top: 8px;'>
                {content}
            </div>
        </div>
    """.format(
        title=title,
        rule_text_html=f"<span style='font-size: 12px; color: #6b7280; margin-left: 8px;'>{rule_text}</span>" if rule_text else "",
        content=content
    ), unsafe_allow_html=True)

def word_count_bar(count: int, limit: int) -> go.Figure:
    """Create a custom word count progress bar using plotly"""
    percentage = (count / limit) * 100
    color = '#EF4444' if percentage > 100 else '#F59E0B' if percentage > 90 else '#10B981'
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=percentage,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
        },
        number={'suffix': "%", 'font': {'size': 20}},
        title={'text': f"{count} / {limit} words", 'font': {'size': 14}}
    ))
    
    fig.update_layout(
        height=100,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def create_sidebar():
    """Create the fixed sidebar"""
    with st.sidebar:
        st.image("https://placeholder.com/150x50", caption="Jessup Logo")
        st.markdown("### Memorandum for the Applicant")
        
        st.markdown("""
        <div style='
            background-color: #f9fafb;
            padding: 12px;
            border-radius: 8px;
            margin-top: 16px;
        '>
            <p style='
                font-size: 14px;
                font-weight: 600;
                color: #4b5563;
                margin-bottom: 8px;
            '>Penalty Points</p>
            <div style='display: flex; align-items: baseline;'>
                <span style='
                    font-size: 24px;
                    font-weight: 700;
                    color: #dc2626;
                '>10</span>
                <span style='
                    font-size: 14px;
                    color: #6b7280;
                    margin-left: 4px;
                '>points</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    st.set_page_config(layout="wide")
    
    # Add custom CSS
    st.markdown("""
        <style>
            .stApp {
                background-color: #f9fafb;
            }
            .main > div {
                padding: 1rem;
            }
            [data-testid="stSidebar"] {
                background-color: white;
                border-right: 1px solid #e5e7eb;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Sample data (same as React version)
    data = {
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
        }
    }
    
    # Create sidebar
    create_sidebar()
    
    # Main content
    st.title("Jessup Memorial Penalty Checker")
    
    # Penalty Summary
    penalties_df = pd.DataFrame([
        {"Rule": "Rule 5.5", "Description": "Missing Prayer for Relief", "Points": 4, "R": 2},
        {"Rule": "Rule 5.17", "Description": "Non-Permitted Abbreviations (5 found)", "Points": 3, "R": 0},
        {"Rule": "Rule 5.13", "Description": "Improper Citation", "Points": 3, "R": 0}
    ])
    
    custom_card(
        "Penalty Score Summary",
        st.dataframe(
            penalties_df,
            use_container_width=True,
            hide_index=True
        )
    )
    
    # Create two columns for the layout
    col1, col2 = st.columns(2)
    
    with col1:
        # Cover Page Information
        cover_page_content = "".join([
            f"""
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;'>
                <span>{key}</span>
                <div style='display: flex; align-items: center; gap: 8px;'>
                    <span>{'✅' if value['present'] else '❌'}</span>
                    <span>{value['found']}</span>
                </div>
            </div>
            """ for key, value in data["coverPage"].items()
        ])
        custom_card("Cover Page Information", cover_page_content, "(Rule 5.6 - 2 points)")
    
    with col2:
        # Memorial Parts
        parts_content = "".join([
            f"""
            <div style='display: flex; align-items: center; gap: 8px; margin-bottom: 8px;'>
                <span>{'✅' if present else '❌'}</span>
                <span>{part}</span>
            </div>
            """ for part, present in data["memorialParts"].items()
        ])
        custom_card("Memorial Parts", parts_content, "(Rule 5.5 - 2 points per part)")
    
    # Word Count Analysis
    st.markdown("### Word Count Analysis")
    word_count_cols = st.columns(2)
    for idx, (section, info) in enumerate(data["wordCounts"].items()):
        with word_count_cols[idx % 2]:
            st.plotly_chart(
                word_count_bar(info["count"], info["limit"]),
                use_container_width=True
            )
    
    # Abbreviations
    abbreviations_content = "".join([
        f"""
        <div style='
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 8px;
        '>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div style='display: flex; align-items: center; gap: 8px;'>
                    <span>❌</span>
                    <span style='font-weight: 500;'>{abbr}</span>
                    <span style='font-size: 12px; color: #6b7280;'>
                        ({info['count']} occurrence{'s' if info['count'] != 1 else ''})
                    </span>
                </div>
            </div>
            <div style='margin-top: 8px; padding-left: 24px; font-size: 12px; color: #6b7280;'>
                Found in: {', '.join(info['sections'])}
            </div>
        </div>
        """ for abbr, info in data["abbreviations"].items()
    ])
    custom_card(
        "Non-Permitted Abbreviations",
        abbreviations_content,
        "(Rule 5.17 - 1 point each, max 3)"
    )

if __name__ == "__main__":
    main()
