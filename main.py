import streamlit as st

# Must be the first Streamlit command
st.set_page_config(
    page_title="Jessup Memorial Penalty Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initial data setup
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

def create_section_card(title, icon, content, rule="", points=""):
    st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px; margin: 10px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">{icon}</span>
                    <span style="font-size: 1.1em; font-weight: 600;">{title}</span>
                </div>
                {f'<span style="font-size: 0.8em; color: #666;">({rule} - {points})</span>' if rule else ''}
            </div>
            {content}
        </div>
    """, unsafe_allow_html=True)

def create_progress_bar(count, limit):
    percentage = (count / limit) * 100
    color = "#10b981"  # success
    if percentage > 90:
        color = "#f59e0b"  # warning
    if percentage > 100:
        color = "#ef4444"  # error
    
    return f"""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin: 10px 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                <span>{count} words</span>
                <span style="color: {color};">{percentage:.1f}%</span>
            </div>
            <div style="width: 100%; background-color: #e5e7eb; height: 6px; border-radius: 3px;">
                <div style="width: {min(percentage, 100)}%; height: 100%; border-radius: 3px; background-color: {color};"></div>
            </div>
            <div style="text-align: right; font-size: 0.8em; color: #666; margin-top: 5px;">
                Limit: {limit}
            </div>
        </div>
    """

def main():
    # Sidebar
    with st.sidebar:
        st.markdown("""
            <h1 style="margin-bottom: 20px;">Jessup Penalty Checker</h1>
            <div style="font-size: 1.1em; color: #4b5563;">
                Memorandum for the Applicant
            </div>
            <div style="background: #fee2e2; padding: 15px; border-radius: 8px; margin-top: 15px;">
                <div style="font-size: 0.9em; color: #991b1b;">Total Penalty Points</div>
                <div style="font-size: 2em; font-weight: bold; color: #dc2626;">10</div>
            </div>
        """, unsafe_allow_html=True)

        # Navigation menu
        st.markdown("<div style='margin-top: 30px;'><h3>Sections</h3></div>", unsafe_allow_html=True)
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
                <div style="padding: 10px; border-radius: 5px; margin: 5px 0; cursor: pointer; 
                            transition: background-color 0.2s;" onmouseover="this.style.backgroundColor='#f3f4f6'">
                    <div style="display: flex; gap: 10px; align-items: center;">
                        <div>{icon}</div>
                        <div>
                            <div style="font-weight: 500;">{section}</div>
                            <div style="font-size: 0.8em; color: #666;">{rule} - {points}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Main content
    st.title("Jessup Memorial Penalty Checker")

    # Penalty Summary
    penalty_summary = """
        <table style="width: 100%; border-collapse: separate; border-spacing: 0;">
            <thead>
                <tr style="background-color: #f8f9fa;">
                    <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e5e7eb;">Rule</th>
                    <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e5e7eb;">Description</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e5e7eb;">A</th>
                    <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e5e7eb;">R</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding: 12px; border-bottom: 1px solid #e5e7eb;">Rule 5.5</td>
                    <td style="padding: 12px; border-bottom: 1px solid #e5e7eb;">
                        Missing Prayer for Relief
                        <div style="font-size: 0.8em; color: #666;">2 points per part</div>
                    </td>
                    <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e5e7eb;">4</td>
                    <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e5e7eb;">2</td>
                </tr>
                <tr>
                    <td style="padding: 12px; border-bottom: 1px solid #e5e7eb;">Rule 5.17</td>
                    <td style="padding: 12px; border-bottom: 1px solid #e5e7eb;">
                        Non-Permitted Abbreviations (5 found)
                        <div style="font-size: 0.8em; color: #666;">1 point each, max 3</div>
                    </td>
                    <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e5e7eb;">3</td>
                    <td style="padding: 12px; text-align: center; border-bottom: 1px solid #e5e7eb;">0</td>
                </tr>
                <tr style="background-color: #f8f9fa; font-weight: 600;">
                    <td colspan="2" style="padding: 12px; text-align: right;">TOTAL</td>
                    <td style="padding: 12px; text-align: center;">10</td>
                    <td style="padding: 12px; text-align: center;">2</td>
                </tr>
            </tbody>
        </table>
    """
    create_section_card("Penalty Score Summary", "⚠️", penalty_summary)

    # Document Sections in two columns
    col1, col2 = st.columns(2)

    with col1:
        # Cover Page Check
        cover_page_content = "".join([
            f"""
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0;">
                <span>{key}</span>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="color: {'#10b981' if value['present'] else '#ef4444'}">
                        {'✅' if value['present'] else '❌'}
                    </span>
                    <span>{value['found']}</span>
                </div>
            </div>
            """ for key, value in initial_data["coverPage"].items()
        ])
        create_section_card("Cover Page Information", "📄", cover_page_content, "Rule 5.6", "2 points")

    with col2:
        # Memorial Parts
        memorial_parts_content = """
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
        """ + "".join([
            f"""
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="color: {'#10b981' if present else '#ef4444'}">
                    {'✅' if present else '❌'}
                </span>
                <span>{part}</span>
            </div>
            """ for part, present in initial_data["memorialParts"].items()
        ]) + "</div>"
        create_section_card("Memorial Parts", "✓", memorial_parts_content, "Rule 5.5", "2 points per part")

    # Word Count Analysis
    word_count_content = """
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
    """
    for section, data in initial_data["wordCounts"].items():
        word_count_content += f"""
            <div>
                <div style="font-weight: 500; margin-bottom: 8px;">{section}</div>
                {create_progress_bar(data['count'], data['limit'])}
            </div>
        """
    word_count_content += "</div>"
    create_section_card("Word Count Analysis", "📏", word_count_content, "Rule 5.12", "varies")

    # Abbreviations
    abbreviations_content = "".join([
        f"""
        <div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 12px; margin-bottom: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="color: #ef4444;">❌</span>
                    <span style="font-weight: 500;">{abbr}</span>
                    <span style="font-size: 0.8em; color: #666;">
                        ({info['count']} occurrence{'s' if info['count'] != 1 else ''})
                    </span>
                </div>
            </div>
            <div style="margin-top: 8px; padding-left: 24px; font-size: 0.9em; color: #666;">
                Found in: {', '.join(info['sections'])}
            </div>
        </div>
        """ for abbr, info in initial_data["abbreviations"].items()
    ])
    create_section_card("Non-Permitted Abbreviations", "📑", abbreviations_content, "Rule 5.17", "1 point each, max 3")

    # Additional Checks
    col3, col4 = st.columns(2)

    with col3:
        # Anonymity Check
        anonymity_content = """
            <div style="background-color: #d1fae5; color: #065f46; padding: 12px; border-radius: 8px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span>✅</span>
                    <span>No anonymity violations found</span>
                </div>
                <div style="margin-top: 8px; font-size: 0.9em;">
                    No disclosure of school, team members, or country
                </div>
            </div>
        """
        create_section_card("Anonymity Check", "🔒", anonymity_content, "Rule 5.14", "up to 10 points")

        # Citations Check
        citations_content = """
            <div style="background-color: #fee2e2; color: #991b1b; padding: 12px; border-radius: 8px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span>⚠️</span>
                    <span>5 instances of improper citation format detected</span>
                </div>
            </div>
        """
        create_section_card("Citations", "📚", citations_content, "Rule 5.13", "up to 5 points")

    with col4:
        # Tracked Changes
        tracked_changes_content = """
            <div style="background-color: #d1fae5; color: #065f46; padding: 12px; border-radius: 8px;">
                <div style="display:
