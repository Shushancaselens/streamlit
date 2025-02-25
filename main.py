import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Create data structures as JSON for embedded components
def get_argument_data():
    # Simplified data structure for demonstration
    claimant_args = {
        "1": {
            "id": "1",
            "title": "Sporting Succession",
            "paragraphs": "15-18"
        },
        "2": {
            "id": "2",
            "title": "Doping Violation Chain of Custody",
            "paragraphs": "70-125"
        }
    }
    
    respondent_args = {
        "1": {
            "id": "1",
            "title": "Sporting Succession Rebuttal",
            "paragraphs": "200-218"
        },
        "2": {
            "id": "2",
            "title": "Doping Chain of Custody Defense",
            "paragraphs": "250-290"
        }
    }
    
    topics = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "argumentIds": ["1"]
        },
        {
            "id": "topic-2",
            "title": "Doping Violation and Chain of Custody",
            "description": "Issues related to doping test procedures and evidence handling",
            "argumentIds": ["2"]
        }
    ]
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args,
        "topics": topics
    }

def display_arguments():
    # Title
    st.title("Legal Arguments Analysis")
    
    # Create a basic structure
    st.markdown("## Claimant vs. Respondent Arguments")
    
    # Get the data
    args_data = get_argument_data()
    
    # Create a two-column layout for arguments
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Claimant's Arguments")
        for arg_id, arg in args_data["claimantArgs"].items():
            with st.expander(f"{arg['id']}. {arg['title']} (¶{arg['paragraphs']})"):
                st.write(f"This would display detailed legal and factual points for {arg['title']}.")
                st.markdown("---")
                st.write("Overview points would be here.")
                st.markdown("---")
                st.write("Evidence would be here.")
    
    with col2:
        st.subheader("Respondent's Arguments")
        for arg_id, arg in args_data["respondentArgs"].items():
            with st.expander(f"{arg['id']}. {arg['title']} (¶{arg['paragraphs']})"):
                st.write(f"This would display detailed legal and factual points for {arg['title']}.")
                st.markdown("---")
                st.write("Overview points would be here.")
                st.markdown("---")
                st.write("Evidence would be here.")

def display_timeline():
    st.title("Timeline of Events")
    
    # Sample timeline data
    timeline_data = [
        {"date": "2023-01-15", "event": "Contract signed with Club", "status": "Undisputed"},
        {"date": "2023-03-20", "event": "Player received notification of exclusion", "status": "Undisputed"},
        {"date": "2023-04-01", "event": "Player sent termination letter", "status": "Undisputed"},
        {"date": "2023-04-10", "event": "Player denied access to training facilities", "status": "Disputed"}
    ]
    
    # Display timeline
    for item in timeline_data:
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.write(item["date"])
        with col2:
            st.write(item["event"])
        with col3:
            status_color = "green" if item["status"] == "Undisputed" else "red"
            st.markdown(f"<span style='color:{status_color};'>{item['status']}</span>", unsafe_allow_html=True)
        st.markdown("---")

def display_exhibits():
    st.title("Exhibits")
    
    # Sample exhibits data
    exhibits_data = [
        {"id": "C-1", "title": "Employment Contract", "party": "Appellant"},
        {"id": "C-2", "title": "Termination Letter", "party": "Appellant"},
        {"id": "R-1", "title": "Club Regulations", "party": "Respondent"}
    ]
    
    # Display exhibits table
    table_data = {"ID": [], "Title": [], "Party": []}
    for exhibit in exhibits_data:
        table_data["ID"].append(exhibit["id"])
        table_data["Title"].append(exhibit["title"])
        table_data["Party"].append(exhibit["party"])
    
    st.dataframe(table_data)

# Main app
def main():
    # Create tab structure
    tab1, tab2, tab3 = st.tabs(["Arguments", "Timeline", "Exhibits"])
    
    with tab1:
        display_arguments()
    
    with tab2:
        display_timeline()
    
    with tab3:
        display_exhibits()

if __name__ == "__main__":
    main()
