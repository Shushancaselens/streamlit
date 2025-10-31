import streamlit as st

# Page configuration
st.set_page_config(page_title="CAS Case Viewer", layout="wide")

st.subheader("CAS 2022/A/8836 | Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje | 2023-05-08")

# Tags
col1, col2, col3 = st.columns([1, 1, 8])
with col1:
    st.success("✓ Contract")
with col2:
    st.error("✗ Dismissed")
with col3:
    st.info("⚽ Football")

st.divider()

# ============= OPTION 1: Simple inline with dividers =============
st.markdown("### Option 1: Inline Format")
st.markdown("""
**Parties:** Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje  |  
**Procedure:** Appeal Arbitration Procedure  |  
**Category:** Award  |  
**President:** Olivier Carrard  |  
**Arbitrators:** Unknown, Unknown
""")

st.divider()

# ============= OPTION 2: Two-column compact table =============
st.markdown("### Option 2: Two-Column Table")
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("**Parties:**  \n**Procedure:**  \n**Category:**  \n**President:**  \n**Arbitrators:**")
with col2:
    st.markdown("Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje  \nAppeal Arbitration Procedure  \nAward  \nOlivier Carrard  \nUnknown, Unknown")

st.divider()

# ============= OPTION 3: Using st.columns with NO borders =============
st.markdown("### Option 3: Inline Columns (No Borders)")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.caption("PARTIES")
    st.markdown("Samsunspor v. Dja Djedje")
with col2:
    st.caption("PROCEDURE")
    st.markdown("Appeal Arbitration")
with col3:
    st.caption("CATEGORY")
    st.markdown("Award")
with col4:
    st.caption("PRESIDENT")
    st.markdown("O. Carrard")
with col5:
    st.caption("ARBITRATORS")
    st.markdown("Unknown")

st.divider()

# ============= OPTION 4: Using tabs =============
st.markdown("### Option 4: Tabs")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Parties", "Procedure", "Category", "President", "Arbitrators"])
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

st.divider()

# ============= OPTION 5: Badge-style with st.pills =============
st.markdown("### Option 5: Interactive Pills")
st.write("**Parties:** Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje")
st.pills("Info", ["Appeal Arbitration Procedure", "Award", "Olivier Carrard", "Unknown Arbitrators"], selection_mode=None)

st.divider()

# ============= OPTION 6: Single line compact =============
st.markdown("### Option 6: Ultra Compact Single Line")
st.text("Parties: Samsunspor v. Dja Djedje | Procedure: Appeal Arbitration | Category: Award | President: O. Carrard | Arbitrators: Unknown")

st.divider()

# ============= OPTION 7: Expander (collapsible) =============
st.markdown("### Option 7: Collapsible Section")
with st.expander("📋 Case Details", expanded=True):
    st.write("**Parties:** Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje")
    st.write("**Procedure:** Appeal Arbitration Procedure")
    st.write("**Category:** Award")
    st.write("**President:** Olivier Carrard")
    st.write("**Arbitrators:** Unknown, Unknown")
