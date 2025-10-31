import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="CAS Case Viewer", layout="wide")

# Case Header
st.markdown("### CAS 2022/A/8836 | Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje | 2023-05-08")

# Tags using st.pills (not interactive, just for display)
st.pills("Status", ["Contract", "Dismissed", "Football"], selection_mode="multi", default=["Contract", "Dismissed", "Football"], disabled=True)

# Case Details in a bordered container - Compact and Beautiful
with st.container(border=True):
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("**Parties:**")
        st.markdown("**Procedure:**")
        st.markdown("**Category:**")
        st.markdown("**President:**")
        st.markdown("**Arbitrators:**")
    
    with col2:
        st.markdown("Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje")
        st.markdown("Appeal Arbitration Procedure")
        st.markdown("Award")
        st.markdown("Olivier Carrard")
        st.markdown("Unknown, Unknown")

# Buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("📄 PDF", use_container_width=True):
        st.info("PDF download would be triggered here")
with col2:
    if st.button("💾 Save", use_container_width=True):
        st.success("Case saved!")

# Relevant Passages Section
st.markdown("### Relevant Passages")

# Expandable section
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

# Footer
st.caption("CAS Case Management System")
