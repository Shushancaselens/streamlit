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
st.header("Case name: admissability; challenge; request_for_a_stay; statement_of_appeal")

tab1, tab2 = st.tabs(["Card View", "Table View"])

with tab1:
    st.text_input("Search", placeholder="Search...")
    
    # Timeline items using expanders (native dropdowns)
    with st.expander("🔵 2017-00-00 | In 2017, **Antani Ivanov** participated in the 50m, 100m, and 200m butterfly events at the World Championships, set a national record, and qualified for the 200m butterfly at the 2020 Olympic Games.", expanded=False):
        
        # Top section with sources and tags in a single horizontal row
        col1, col2, col3, col4, col5 = st.columns([0.6, 1.2, 1.2, 1.2, 1.2])
        with col1:
            with st.container(border=True):
                st.markdown(":blue[**2**]  \n:gray[Sources]")
        with col2:
            st.markdown("**PROCEEDINGS:**")
        with col3:
            st.markdown(":blue[admissability]")
        with col4:
            st.markdown("**ADDRESSED BY:**")
        with col5:
            st.markdown(":gray[Not Addressed]")
        
        st.markdown("")
        
        # Supporting Documents section
        st.markdown("#### Supporting Documents")
        
        # Names mentioned as pills
        st.pills("Names mentioned:", ["Antani Ivanov", "Husain Al Musallam", "Brent J. Nowicki"], selection_mode="multi", key="names_pills")
        
        # Proceedings and status as pills
        st.pills("Tags:", ["admissability", "Not Addressed"], selection_mode="multi", key="tags_pills")
        
        st.markdown("")
        
        # Document container
        with st.container(border=True):
            # Document title
            st.markdown("**Exhibit A17 - Request for Conciliation (English translation)**")
            
            # Summary
            st.markdown("**Summary:** This document, titled 'Request for Conciliation - **Antani Ivanov** v. World Aquatics,' was filed on June 24, 2024, with the Lausanne District Court in Switzerland. On behalf of Bulgarian swimmer **Antani Ivanov**, it challenges a decision by the Aquatics Integrity Unit (AQIU) of World Aquatics, which extended a disciplinary suspension issued by the Bulgarian Swimming Federation (BSF) to all World Aquatics competitions worldwide. The application seeks to declare the AQIU's May 23, 2024 decision null and void (or, alternatively, to annul it) on the grounds of lack of due process, violation of the right to be heard, and failure to properly assess the legality of the original BSF decision.")
            
            # Citation in gray container
            st.info("**Citation:** Exhibit A17 - Request for Conciliation (English translation), page 6.")
            
            # Source in green container  
            st.success("**Source:** 34. Mr. **Antani Ivanov** is a professional swimmer from Bulgaria, aged 24. He participated in the 50m, 100m, and 200m butterfly events at the 2017 World Championships, setting a national record and qualifying for the 200m butterfly at the 2020 Olympic Games.")
            
            # Action buttons
            col1, col2 = st.columns(2)
            with col1:
                st.button("View Document ⌄", key="view_doc_1", use_container_width=True)
            with col2:
                st.button("📄 Download PDF", key="download_1", use_container_width=True)
        
        st.markdown("")
        
        # Second exhibit
        st.markdown("**Exhibit A17 - REQUETE de conciliation 24.6.2024**")
        
        st.markdown("**Summary:** This document, titled 'Requête de conciliation **Antani Ivanov** c. World Aquatics' and dated June 24, 2024, is a legal petition filed before the Tribunal d'arrondissement de Lausanne by the attorneys representing Bulgarian swimmer **Antani Ivanov**. The request seeks to declare null and void, or alternatively annul, the decision of the Aquatics Integrity Unit (AQIU) of World Aquatics made on May 23, 2024, which globally extended the effects of a disciplinary sanction originally imposed by the Bulgarian Swimming Federation (BSF). The petition argues that both the BSF and AQIU decisions gravely violated **Ivanov's** right to be heard and procedural safeguards, urging the Swiss civil court to intervene due to the lack of a valid arbitration clause covering such recognition actions.")
    
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
