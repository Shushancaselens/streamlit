import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Caselens",
    page_icon="🔷",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.header("🔷 caselens")
    
    st.subheader("Profile")
    st.subheader("📅 Events")
    st.subheader("Documents")
    
    st.markdown("---")
    
    st.subheader("🔽 Case Filter")
    st.selectbox("Select Case", ["Admissibility"])
    
    st.subheader("📅 Date Range") 
    st.text_input("Start Date", value="1724/01/01")
    st.text_input("End Date", value="2025/07/21")
    
    st.subheader("⚙️ Submissions Filter")
    st.checkbox("Addressed by party")
    st.checkbox("Disputed by parties")
    
    st.button("Download", type="primary")

# Main content
st.title("Case name: admissability; challenge; request_for_a_stay; statement_of_appeal")

tab1, tab2 = st.tabs(["Card View", "Table View"])

with tab1:
    st.text_input("Search", placeholder="Search...")
    
    # Timeline items using expanders (native dropdowns)
    with st.expander("2017-00-00 | In 2017, Antani Ivanov participated in the 50m, 100m, and 200m butterfly events at the World Championships, set a national record, and qualified for the 200m butterfly at the 2020 Olympic Games.", expanded=False):
        st.write("Event details can be expanded here...")
    
    with st.expander("2017-00-00 | At the time of adoption of this Constitution, any term of office completed before 2017 shall be disregarded in calculating the number of full terms that a person has served as a Bureau or Executive Member.", expanded=False):
        st.write("Constitution details...")
    
    with st.expander("2020-00-00 | In 2020 Antani Ivanov qualified for the 200m butterfly at the Summer Olympic Games.", expanded=False):
        st.write("Olympic qualification details...")
    
    with st.expander("2022-12-12 | On 2022-12-12, the World Aquatics Integrity Code was issued and signed in Melbourne by Husain Al Musallam and Brent J. Nowicki for the Bureau.", expanded=False):
        st.write("Integrity Code details...")
    
    with st.expander("2023-01-01 | On 2023-01-01 the Constitution of World Aquatics came into force.", expanded=False):
        st.write("Constitution implementation details...")
    
    with st.expander("2023-01-01 | On 2023-01-01 the new composition of the Bureau as set out in Article 14 came into effect with the new additional positions within the Bureau.", expanded=False):
        st.write("Bureau composition details...")

with tab2:
    # Table view
    data = {
        "Date": ["2017-00-00", "2017-00-00", "2020-00-00", "2022-12-12", "2023-01-01", "2023-01-01"],
        "Event": [
            "In 2017, Antani Ivanov participated in the 50m, 100m, and 200m butterfly events at the World Championships, set a national record, and qualified for the 200m butterfly at the 2020 Olympic Games.",
            "At the time of adoption of this Constitution, any term of office completed before 2017 shall be disregarded in calculating the number of full terms that a person has served as a Bureau or Executive Member.",
            "In 2020 Antani Ivanov qualified for the 200m butterfly at the Summer Olympic Games.",
            "On 2022-12-12, the World Aquatics Integrity Code was issued and signed in Melbourne by Husain Al Musallam and Brent J. Nowicki for the Bureau.",
            "On 2023-01-01 the Constitution of World Aquatics came into force.",
            "On 2023-01-01 the new composition of the Bureau as set out in Article 14 came into effect with the new additional positions within the Bureau."
        ]
    }
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
