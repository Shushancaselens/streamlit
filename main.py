import streamlit as st

def word_count_progress(count: int, limit: int):
    """Create a word count progress indicator using basic Streamlit components"""
    percentage = (count / limit) * 100
    color = 'red' if percentage > 100 else 'yellow' if percentage > 90 else 'green'
    
    st.markdown(f"""
        <div style='display: flex; justify-content: space-between; margin-bottom: 5px;'>
            <span style='font-size: 0.9em;'>{count} words</span>
            <span style='font-size: 0.9em; color: {"#dc2626" if percentage > 100 else "#f59e0b" if percentage > 90 else "#10b981"};'>
                {percentage:.1f}%
            </span>
        </div>
    """, unsafe_allow_html=True)
    
    st.progress(min(percentage/100, 1.0))
    st.markdown(f"<div style='font-size: 0.8em; color: #666;'>Limit: {limit}</div>", unsafe_allow_html=True)

def main():
    st.set_page_config(layout="wide", page_title="Jessup Penalty Checker")
    
    # Custom CSS
    st.markdown("""
        <style>
            .stApp {
                background-color: #f9fafb;
            }
            div[data-testid="stSidebar"] {
                background-color: white;
                border-right: 1px solid #e5e7eb;
            }
            .custom-card {
                background-color: white;
                padding: 1rem;
                border-radius: 0.5rem;
                border: 1px solid #e5e7eb;
                margin-bottom: 1rem;
            }
            .stProgress > div > div {
                background-color: #10b981;
            }
            .warning .stProgress > div > div {
                background-color: #f59e0b;
            }
            .error .stProgress > div > div {
                background-color: #dc2626;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Sample data
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
    
    # Sidebar
    with st.sidebar:
        st.title("Jessup 2025")
        st.subheader(f"Memorial for the {data['memorialType']}")
        
        st.markdown("""
            <div style='
                background-color: #f3f4f6;
                padding: 1rem;
                border-radius: 0.5rem;
                margin-top: 1rem;
            '>
                <p style='
                    font-size: 0.875rem;
                    font-weight: 600;
                    color: #4b5563;
                    margin-bottom: 0.5rem;
                '>Total Penalty Points</p>
                <div style='display: flex; align-items: baseline;'>
                    <span style='
                        font-size: 1.875rem;
                        font-weight: 700;
                        color: #dc2626;
                    '>10</span>
                    <span style='
                        font-size: 0.875rem;
                        color: #6b7280;
                        margin-left: 0.25rem;
                    '>points</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Main content
    st.title("Jessup Memorial Penalty Checker")
    
    # Penalty Summary
    with st.container():
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.subheader("Penalty Score Summary")
        penalties = [
            ["Rule", "Description", "Points", "R", "Details"],
            ["Rule 5.5", "Missing Prayer for Relief", "4", "2", "2 points per part"],
            ["Rule 5.17", "Non-Permitted Abbreviations (5 found)", "3", "0", "1 point each, max 3"],
            ["Rule 5.13", "Improper Citation", "3", "0", "1 point per violation, max 5"]
        ]
        st.table(penalties)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Two-column layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.subheader("Cover Page Information")
        st.caption("Rule 5.6 - 2 points")
        for key, value in data["coverPage"].items():
            st.markdown(f"""
                <div style='display: flex; justify-content: space-between; align-items: center; margin: 5px 0;'>
                    <span>{key}</span>
                    <div style='display: flex; align-items: center; gap: 8px;'>
                        <span>{value['present'] and '✅' or '❌'}</span>
                        <span>{value['found']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.subheader("Memorial Parts")
        st.caption("Rule 5.5 - 2 points per part")
        cols = st.columns(2)
        for i, (part, present) in enumerate(data["memorialParts"].items()):
            with cols[i % 2]:
                st.markdown(f"{present and '✅' or '❌'} {part}")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Word Count Analysis
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.subheader("Word Count Analysis")
    st.caption("Rule 5.12")
    
    word_count_cols = st.columns(2)
    for i, (section, info) in enumerate(data["wordCounts"].items()):
        with word_count_cols[i % 2]:
            st.markdown(f"##### {section}")
            percentage = (info["count"] / info["limit"]) * 100
            class_name = "error" if percentage > 100 else "warning" if percentage > 90 else ""
            st.markdown(f"<div class='{class_name}'>", unsafe_allow_html=True)
            word_count_progress(info["count"], info["limit"])
            st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Abbreviations
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.subheader("Non-Permitted Abbreviations")
    st.caption("Rule 5.17 - 1 point each, max 3")
    
    for abbr, info in data["abbreviations"].items():
        with st.expander(f"❌ {abbr} ({info['count']} occurrence{'s' if info['count'] != 1 else ''})"):
            st.markdown(f"Found in: {', '.join(info['sections'])}")
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
