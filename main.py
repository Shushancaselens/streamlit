import streamlit as st

# Page configuration
st.set_page_config(page_title="CAS Case Viewer", layout="wide")

st.title("Different UI Approaches")
st.markdown("---")

# ============ OPTION 1: Using st.metric() ============
st.subheader("Option 1: Using st.metric()")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Parties", "Samsunspor v. Dja Djedje")
with col2:
    st.metric("Procedure", "Appeal Arbitration")
with col3:
    st.metric("Category", "Award")
with col4:
    st.metric("President", "O. Carrard")
with col5:
    st.metric("Arbitrators", "Unknown, Unknown")

st.markdown("---")

# ============ OPTION 2: Horizontal Layout (All in one row) ============
st.subheader("Option 2: Single Row with Dividers")
cols = st.columns(5)
data = [
    ("👥 Parties", "Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje"),
    ("📋 Procedure", "Appeal Arbitration Procedure"),
    ("🏷️ Category", "Award"),
    ("👤 President", "Olivier Carrard"),
    ("⚖️ Arbitrators", "Unknown, Unknown")
]
for col, (label, value) in zip(cols, data):
    with col:
        st.markdown(f"**{label}**")
        st.caption(value)

st.markdown("---")

# ============ OPTION 3: Using Tabs ============
st.subheader("Option 3: Using Tabs")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["👥 Parties", "📋 Procedure", "🏷️ Category", "👤 President", "⚖️ Arbitrators"])
with tab1:
    st.write("Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje")
with tab2:
    st.write("Appeal Arbitration Procedure")
with tab3:
    st.write("Award")
with tab4:
    st.write("Olivier Carrard")
with tab5:
    st.write("Unknown, Unknown")

st.markdown("---")

# ============ OPTION 4: Status Containers ============
st.subheader("Option 4: Using st.status()")
col1, col2, col3 = st.columns(3)
with col1:
    with st.status("Parties", expanded=True):
        st.write("Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje")
with col2:
    with st.status("Procedure", expanded=True):
        st.write("Appeal Arbitration Procedure")
with col3:
    with st.status("Category", expanded=True):
        st.write("Award")

col4, col5, col6 = st.columns(3)
with col4:
    with st.status("President", expanded=True):
        st.write("Olivier Carrard")
with col5:
    with st.status("Arbitrators", expanded=True):
        st.write("Unknown, Unknown")

st.markdown("---")

# ============ OPTION 5: Compact Key-Value Pairs ============
st.subheader("Option 5: Simple Key-Value List")
with st.container(border=True):
    st.markdown("""
    | Field | Value |
    |-------|-------|
    | **Parties** | Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje |
    | **Procedure** | Appeal Arbitration Procedure |
    | **Category** | Award |
    | **President** | Olivier Carrard |
    | **Arbitrators** | Unknown, Unknown |
    """)

st.markdown("---")

# ============ OPTION 6: Badge Style ============
st.subheader("Option 6: Badge Style with Pills")
st.markdown("**Case Details**")
selection = st.pills(
    "Field",
    ["Parties", "Procedure", "Category", "President", "Arbitrators"],
    selection_mode="single",
    default="Parties"
)

# Show value based on selection
values = {
    "Parties": "Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje",
    "Procedure": "Appeal Arbitration Procedure",
    "Category": "Award",
    "President": "Olivier Carrard",
    "Arbitrators": "Unknown, Unknown"
}
if selection:
    st.info(values[selection])

st.markdown("---")

# ============ OPTION 7: Horizontal Container ============
st.subheader("Option 7: Horizontal Scrollable Container")
with st.container(border=True):
    flex = st.container()
    cols = flex.columns(5)
    for col, (label, value) in zip(cols, data):
        with col:
            st.markdown(f"**{label}**")
            st.write(value)
