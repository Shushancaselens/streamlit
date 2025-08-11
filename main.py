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
    st.text_input("End Date", value="2025/03/19")
    
    # Download section
    st.markdown("---")
    st.button("Download Timeline", type="primary", use_container_width=True)
    st.markdown("---")
    
    st.subheader("⚙️ Submissions Filter")
    st.toggle("Addressed by party")
    st.toggle("Disputed by parties")
    
    # Warning message
    st.warning("⚠️ No events selected - will download all events")

# Main content header
col1, col2 = st.columns([3, 1])
with col1:
    st.header("Case name: Astute CASE N 28459")
with col2:
    st.button("📥 Download", type="primary", use_container_width=True, key="main_download")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Card View", "Table View", "Definitions"])

with tab1:
    # Top controls row
    col1, col2, col3 = st.columns([0.05, 2, 1])
    with col1:
        master_check = st.checkbox("", key="master_checkbox", help="Select/Deselect All")
    with col2:
        st.text_input("Search", placeholder="Search...", key="search_input")
    with col3:
        st.button("📥 Download", type="primary", use_container_width=True, key="timeline_download")
    
    st.markdown("")
    
    # Timeline items
    timeline_items = [
        ("1926-12-17", "On 17 December 26, **France** issued laws establishing the disciplinary and penal codes for both the French navy and the merchant navy.", "2 Sources"),
        ("1961-10-05", "On 05 October 61, the **United Kingdom of Great Britain and Northern Ireland** signed the Hague Convention of 5 October 1961.", "1 Source"),
        ("1985-02-06", "On 06 February 85, **France** issued decree 85-185 regulating the passage of foreign ships and vessels through French territorial waters.", "2 Sources"),
        ("2004-00-00", "In 2004 Schedule A of the supply agreement between **Elfaag Travaux Maritimes et Fluviaux** and **Noksel Celik Boru Sanayi A.S.** referenced the production standard EN 10025:2004 for steel grade requirements for the **Wharf** **Futuna** project.", "1 Source"),
        ("2004-00-00", "In 2004 **OKEAN SHIPBUILDING YARD** built **MV Messila** in **Nikolayev**, **Ukraine**.", "1 Source"),
        ("2004-10-00", "In October 2004, Damen Shipyards built **MV Messila** in the Netherlands.", "1 Source")
    ]
    
    for i, (date, event, sources) in enumerate(timeline_items):
        col_check, col_exp = st.columns([0.05, 0.95])
        with col_check:
            st.checkbox("", key=f"check_{i}", value=master_check)
        with col_exp:
            with st.expander(f"🔵 {date} | {event} | :green[{sources}]", expanded=False):
                st.markdown("Timeline content...")

with tab2:
    # Table view
    data = {
        "Date": ["1926-12-17", "1961-10-05", "1985-02-06", "2004-00-00", "2004-00-00", "2004-10-00"],
        "Event": [
            "On 17 December 26, France issued laws establishing the disciplinary and penal codes for both the French navy and the merchant navy.",
            "On 05 October 61, the United Kingdom of Great Britain and Northern Ireland signed the Hague Convention of 5 October 1961.",
            "On 06 February 85, France issued decree 85-185 regulating the passage of foreign ships and vessels through French territorial waters.",
            "In 2004 Schedule A of the supply agreement between Elfaag Travaux Maritimes et Fluviaux and Noksel Celik Boru Sanayi A.S. referenced the production standard EN 10025:2004 for steel grade requirements for the Wharf Futuna project.",
            "In 2004 OKEAN SHIPBUILDING YARD built MV Messila in Nikolayev, Ukraine.",
            "In October 2004, Damen Shipyards built MV Messila in the Netherlands."
        ]
    }
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

with tab3:
    st.markdown("### Definitions")
    
    # Search for definitions
    search_term = st.text_input("Search definitions...", placeholder="Search for terms, people, locations...", key="def_search").lower()
    
    # All definitions in table format
    definitions_data = {
        "Term": ["France", "United Kingdom of Great Britain and Northern Ireland", "Elfaag Travaux Maritimes et Fluviaux", "Noksel Celik Boru Sanayi A.S.", "OKEAN SHIPBUILDING YARD", "Damen Shipyards", "MV Messila", "Wharf Futuna", "Nikolayev", "Ukraine", "Netherlands", "Hague Convention"],
        "Definition": [
            "European country that issued naval disciplinary codes and territorial waters regulations.",
            "Country that signed the Hague Convention of 5 October 1961.",
            "Maritime and fluvial construction company involved in supply agreement.",
            "Turkish steel pipe manufacturing company.",
            "Shipbuilding facility that constructed MV Messila in Ukraine.",
            "Dutch shipbuilding company that built MV Messila in the Netherlands.",
            "Vessel built by multiple shipyards in different locations.",
            "Port infrastructure project in Futuna requiring steel grade specifications.",
            "City in Ukraine where MV Messila was built.",
            "Country where OKEAN SHIPBUILDING YARD is located.",
            "Country where Damen Shipyards built MV Messila.",
            "International convention signed by the UK in 1961."
        ],
        "Type": ["Location", "Location", "Organization", "Organization", "Organization", "Organization", "Vessel", "Infrastructure", "Location", "Location", "Location", "Legal Document"]
    }
    
    df_def = pd.DataFrame(definitions_data)
    
    # Filter based on search
    if search_term:
        mask = df_def['Term'].str.lower().str.contains(search_term) | df_def['Definition'].str.lower().str.contains(search_term) | df_def['Type'].str.lower().str.contains(search_term)
        df_def = df_def[mask]
    
    st.dataframe(df_def, use_container_width=True, hide_index=True)
