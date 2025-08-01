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
    
    st.subheader("👤 Profile")
    st.subheader("📅 Events")
    st.subheader("📄 Documents")
    
    st.markdown("---")
    
    st.subheader("🔽 Case Filter")
    st.selectbox("Select Case", ["All Events"])
    
    st.subheader("📄 Document Type Filter")
    st.selectbox("Select Document Types", ["Choose an option"], key="doc_type_filter")
    
    st.subheader("👥 Entity Name Filter") 
    st.selectbox("Select Entity Names", ["Choose an option"], key="entity_filter")
    
    st.subheader("📅 Date Range") 
    st.text_input("Start Date", value="1926/12/17")
    st.text_input("End Date", value="2025/01/01")
    
    st.subheader("⚙️ Submissions Filter")
    st.checkbox("Addressed by party")
    st.checkbox("Disputed by parties")
    
    st.button("Download", type="primary")

# Main content
st.header("Case name: admissability; challenge; request_for_a_stay; statement_of_appeal")

tab1, tab2 = st.tabs(["Card View", "Table View"])

with tab1:
    st.text_input("Search", placeholder="Search...")
    
    with st.expander("🔵 2017-00-00 | In 2017, **Antani Ivanov** participated in the 50m, 100m, and 200m butterfly events at the World Championships, set a national record, and qualified for the 200m butterfly at the 2020 Olympic Games.", expanded=False):
        
        # Top section with sources and tags in a single horizontal row
        col1, col2, col3 = st.columns([0.6, 2.5, 2.5])
        with col1:
            with st.container(border=True):
                st.markdown(":blue[**2**]  \n:gray[Sources]")
        with col2:
            st.pills("PROCEEDINGS:", ["admissability"], selection_mode="single", default=["admissability"], key="proceedings_pill")
        with col3:
            st.pills("ADDRESSED BY:", ["Not Addressed"], selection_mode="single", default=["Not Addressed"], key="addressed_pill")
        
        st.markdown("")
        
        # Supporting Documents section
        st.markdown("#### Supporting Documents")
        
        # Document container
        with st.container(border=True):
            # Document title
            st.markdown("**Exhibit A17 - Request for Conciliation (English translation)**")
            
            # Document info with tags
            st.markdown("**Document Type:** :green[Procedural] | **Names mentioned:** :blue[Antani Ivanov], :blue[Husain Al Musallam], :blue[Brent J. Nowicki]")
            
            st.markdown("")
            
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

    # Second timeline item from the screenshot
    with st.expander("🔵 2006-06-20 | On 20 June 06, **Yves Dassonville**, as High Commissioner of the Republic in New Caledonia, repealed and replaced order no. 2006-2/AEM of 20 June 2006 with a new order regulating vessel access to the Leava wharf in Futuna. | :green[1 Source]", expanded=False):
        
        # Three column layout for this case
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Proceedings:**")
            st.markdown(":violet[Astute CASE N 28459_v2]")
        with col2:
            st.markdown("**Addressed by:**")
            st.markdown(":gray[None]")
        with col3:
            st.markdown("**Document Type:**")
            st.markdown(":violet[procedural]")
        
        st.markdown("")
        
        # Definitions section
        st.markdown("#### Definitions")
        
        definitions_data = {
            "Term": ["High Commissioner of th...", "New Caledonia", "Futuna", "Leava", "Yves Dassonville"],
            "Type": ["organization", "location", "location", "location", "person"],
            "Definition": [
                "French governmental authority in New Caledonia overseeing administrative and legal matters, including maritime regulation.",
                "French overseas territory in the South Pacific, the jurisdiction of the High Commissioner.",
                "Island in the French overseas collectivity of Wallis and Futuna; location of Leava wharf.",
                "Village and port on the island of Futuna, site of the regulated wharf.",
                "High Commissioner of the Republic in New Caledonia at the time of the order's issuance."
            ]
        }
        
        st.dataframe(definitions_data, use_container_width=True, hide_index=True)
        
        st.markdown("")
        
        # Source(s) section
        st.markdown("#### Source(s)")
        
        with st.container(border=True):
            st.markdown("**Appendix 4 Bis - ENG.pdf**")
            
            st.markdown("**Summary:** This is an official order (arrêté) dated 16 June 2009, issued by the High Commissioner of the Republic in New Caledonia, regulating the access of vessels to the Leava wharf in Futuna. It establishes procedural requirements for advance notification, operational limitations based on vessel size and equipment, and prescribes authorized procedures for docking, with penalties for violations and references to previous law. The order is signed by Yves Dassonville, High Commissioner, and replaces an earlier order from June 2006.")
            
            st.info("**Citation:** Appendix 4 Bis - ENG.pdf, page 2.")
            
            st.success("**Excerpt:** This order repeals and replaces order no. 2006-2/AEM dij 20 June 2006.")
            
            # Action buttons
            col1, col2 = st.columns(2)
            with col1:
                st.button("View Document ⌄", key="view_doc_2", use_container_width=True)
            with col2:
                st.button("📄 Download PDF", key="download_2", use_container_width=True)
    
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
