import streamlit as st
import pandas as pd

# Data structures [same as before]
applicant_data = {
    "memorialType": "Applicant",
    "coverPage": {
        "Team Number": {"present": True, "found": "349A"},
        "Court Name": {"present": True, "found": "International Court of Justice"},
        "Year": {"present": True, "found": "2025"},
        "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
        "Memorial Type": {"present": True, "found": "Memorial for the Applicant"}
    },
    "wordCounts": {
        "Statement of Facts": {"count": 1196, "limit": 1200},
        "Summary of Pleadings": {"count": 642, "limit": 700},
        "Pleadings": {"count": 9424, "limit": 9500},
        "Prayer for Relief": {"count": 198, "limit": 200}
    },
    "penalties": [
        {"rule": "Rule 5.17", "description": "Non-Permitted Abbreviations", "points": 3, "details": "1 point each"},
        {"rule": "Rule 5.13", "description": "Improper Citation", "points": 2, "details": "2 instances"}
    ],
    "totalPenalties": 5
}

respondent_data = {
    "memorialType": "Respondent",
    "coverPage": {
        "Team Number": {"present": True, "found": "349B"},
        "Court Name": {"present": True, "found": "International Court of Justice"},
        "Year": {"present": True, "found": "2025"},
        "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
        "Memorial Type": {"present": True, "found": "Memorial for the Respondent"}
    },
    "wordCounts": {
        "Statement of Facts": {"count": 1180, "limit": 1200},
        "Summary of Pleadings": {"count": 695, "limit": 700},
        "Pleadings": {"count": 9490, "limit": 9500},
        "Prayer for Relief": {"count": 195, "limit": 200}
    },
    "penalties": [
        {"rule": "Rule 5.17", "description": "Non-Permitted Abbreviations", "points": 2, "details": "2 instances"},
        {"rule": "Rule 5.14", "description": "Anonymity Violation", "points": 5, "details": "School name mentioned"}
    ],
    "totalPenalties": 7
}

def create_word_count_chart(word_counts):
    df = pd.DataFrame({
        'Section': list(word_counts.keys()),
        'Count': [word_counts[s]["count"] for s in word_counts.keys()],
        'Limit': [word_counts[s]["limit"] for s in word_counts.keys()]
    })
    df['Percentage'] = (df['Count'] / df['Limit'] * 100).round(1)
    return df

def display_memorial_section(data):
    st.subheader(f"{data['memorialType']} Memorial")
    st.metric("Total Penalties", f"{data['totalPenalties']} points")
    
    with st.expander("Cover Page Information", expanded=True):
        for key, value in data["coverPage"].items():
            col1, col2 = st.columns([1, 1])
            with col1:
                st.write(key)
            with col2:
                if value["present"]:
                    st.success(value["found"])
                else:
                    st.error("Missing")
    
    with st.expander("Penalties", expanded=True):
        for penalty in data["penalties"]:
            st.warning(
                f"{penalty['description']} ({penalty['rule']})\n\n"
                f"**Points:** {penalty['points']}\n\n"
                f"*{penalty['details']}*"
            )
    
    with st.expander("Word Counts", expanded=True):
        df = create_word_count_chart(data["wordCounts"])
        for _, row in df.iterrows():
            st.write(f"**{row['Section']}**")
            progress = row['Percentage'] / 100
            color = 'green' if progress <= 0.9 else 'orange' if progress <= 1 else 'red'
            st.progress(min(progress, 1.0), text=f"{row['Count']}/{row['Limit']} ({row['Percentage']}%)")

def main():
    st.set_page_config(layout="wide", page_title="Jessup Memorial Penalty Checker")
    
    st.title("Jessup Memorial Penalty Checker")
    
    if applicant_data["totalPenalties"] > respondent_data["totalPenalties"]:
        st.warning(f"Applicant memorial has higher penalties ({applicant_data['totalPenalties']} points vs {respondent_data['totalPenalties']} points)")
    elif respondent_data["totalPenalties"] > applicant_data["totalPenalties"]:
        st.warning(f"Respondent memorial has higher penalties ({respondent_data['totalPenalties']} points vs {applicant_data['totalPenalties']} points)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        display_memorial_section(applicant_data)
    
    with col2:
        display_memorial_section(respondent_data)

if __name__ == "__main__":
    main()
