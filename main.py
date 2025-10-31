import streamlit as st

# Page configuration
st.set_page_config(page_title="CAS Case Viewer", layout="wide")

# Custom CSS to reduce spacing
st.markdown("""
<style>
    .compact-container div[data-testid="stVerticalBlock"] > div {
        gap: 0rem !important;
        padding: 0rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Case Header
st.subheader("CAS 2022/A/8836 | Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje | 2023-05-08")

# Tags
col1, col2, col3 = st.columns([1, 1, 8])
with col1:
    st.success("✓ Contract")
with col2:
    st.error("✗ Dismissed")
with col3:
    st.info("⚽ Football")

# Case Details - Ultra Minimal
with st.container(border=True):
    st.write("**Parties:** Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje")
    st.write("**Procedure:** Appeal Arbitration Procedure")
    st.write("**Category:** Award")
    st.write("**President:** Olivier Carrard")
    st.write("**Arbitrators:** Unknown, Unknown")

# Buttons
col1, col2 = st.columns(2)
with col1:
    st.button("📄 PDF", use_container_width=True)
with col2:
    st.button("💾 Save", use_container_width=True)

# Relevant Passages
st.subheader("Relevant Passages")

with st.expander("Show adjacent sections | Page 22 | Section: a.", expanded=True):
    st.markdown("""
    **a. Termination of the Contract without just cause 90.** Article 14 FIFA RSTP provides that a contract may be terminated by either party 
    without consequences of any kind (either payment of compensation or imposition of sporting sanctions) where there is just cause.
    
    91. According to the Commentary on the Regulations for the Status and Transfer of Players edition 2021 (hereinafter: "RSTP Commentary") 
    on Article 14 (page 109):
    
    "Whether there is just cause for the early termination of a contract signed between a professional player and a club must be assessed in 
    consideration of all the specific circumstances of the individual case.
    
    The Regulations to do not provide a defined list of 'just causes".
    
    It is impossible to capture all potential conduct that might be considered just cause for the premature and unilateral termination of a 
    contract concluded between a professional player and a club.
    
    Over the years, jurisprudence has established several criteria that define, in abstract terms, which combinations of circumstances should be 
    considered just causes.
    
    A contract may be terminated with just cause where there is objective criteria [...] and there is a valid reason to do so.
    """)

st.caption("CAS Case Management System")
