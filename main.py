import streamlit as st

# Page configuration
st.set_page_config(page_title="CAS Case Viewer", layout="wide")

# Case Header
st.subheader("CAS 2022/A/8836 | Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje | 2023-05-08")

# Status Tags
col1, col2, col3 = st.columns([1, 1, 8])
with col1:
    st.success("✓ Contract")
with col2:
    st.error("✗ Dismissed")
with col3:
    st.info("⚽ Football")

# Case Details - Using Custom Badge Tags (MOST COMPACT)
st.markdown("""
<style>
.info-badge {
    display: inline-block;
    padding: 6px 14px;
    margin: 4px 8px 4px 0;
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    font-size: 13px;
    font-weight: 500;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.info-label {
    font-weight: 700;
    opacity: 0.9;
}
.info-value {
    opacity: 1;
    margin-left: 6px;
}
.tag-container {
    padding: 16px;
    background-color: #f8f9fa;
    border-radius: 8px;
    margin: 16px 0;
}
</style>

<div class="tag-container">
    <span class="info-badge"><span class="info-label">👥 Parties:</span><span class="info-value">Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje</span></span>
    <span class="info-badge"><span class="info-label">📋 Procedure:</span><span class="info-value">Appeal Arbitration Procedure</span></span>
    <span class="info-badge"><span class="info-label">🏷️ Category:</span><span class="info-value">Award</span></span>
    <span class="info-badge"><span class="info-label">👤 President:</span><span class="info-value">Olivier Carrard</span></span>
    <span class="info-badge"><span class="info-label">⚖️ Arbitrators:</span><span class="info-value">Unknown, Unknown</span></span>
</div>
""", unsafe_allow_html=True)

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
