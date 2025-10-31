import streamlit as st

# Page configuration
st.set_page_config(page_title="CAS Case Viewer", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .case-header {
        font-size: 20px;
        font-weight: bold;
        color: #0066cc;
        margin-bottom: 10px;
    }
    .tag {
        display: inline-block;
        padding: 4px 12px;
        margin-right: 8px;
        border-radius: 4px;
        font-size: 14px;
        font-weight: 500;
    }
    .tag-green {
        background-color: #d4edda;
        color: #155724;
    }
    .tag-gray {
        background-color: #e2e3e5;
        color: #383d41;
    }
    .tag-blue {
        background-color: #d1ecf1;
        color: #0c5460;
    }
    .case-detail {
        margin: 8px 0;
        font-size: 15px;
    }
    .case-detail strong {
        font-weight: 600;
    }
    .section-header {
        font-size: 18px;
        font-weight: 600;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .passage-text {
        line-height: 1.6;
        color: #333;
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #0066cc;
    }
</style>
""", unsafe_allow_html=True)

# Case Header
st.markdown(
    '<div class="case-header">CAS 2022/A/8836 | Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje | 2023-05-08</div>',
    unsafe_allow_html=True
)

# Tags
st.markdown(
    '<span class="tag tag-green">Contract</span>'
    '<span class="tag tag-gray">Dismissed</span>'
    '<span class="tag tag-blue">Football</span>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Case Details
st.markdown('<div class="case-detail"><strong>Parties:</strong> Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje</div>', unsafe_allow_html=True)
st.markdown('<div class="case-detail"><strong>Procedure:</strong> Appeal Arbitration Procedure</div>', unsafe_allow_html=True)
st.markdown('<div class="case-detail"><strong>Category:</strong> Award</div>', unsafe_allow_html=True)
st.markdown('<div class="case-detail"><strong>President:</strong> Olivier Carrard</div>', unsafe_allow_html=True)
st.markdown('<div class="case-detail"><strong>Arbitrators:</strong> Unknown, Unknown</div>', unsafe_allow_html=True)

# Buttons
col1, col2, col3 = st.columns([1, 1, 10])
with col1:
    if st.button("📄 PDF", use_container_width=True):
        st.info("PDF download would be triggered here")
with col2:
    if st.button("💾 Save", use_container_width=True):
        st.success("Case saved!")

# Relevant Passages Section
st.markdown('<div class="section-header">Relevant Passages</div>', unsafe_allow_html=True)

# Expandable section
with st.expander("Show adjacent sections | Page 22 | Section: a.", expanded=True):
    st.markdown("""
    <div class="passage-text">
    <strong>a. Termination of the Contract without just cause 90.</strong> Article 14 FIFA RSTP provides that a contract may be terminated by either party 
    without consequences of any kind (either payment of compensation or imposition of sporting sanctions) where there is just cause.
    <br><br>
    91. According to the Commentary on the Regulations for the Status and Transfer of Players edition 2021 (hereinafter: "RSTP Commentary") 
    on Article 14 (page 109):
    <br><br>
    "Whether there is just cause for the early termination of a contract signed between a professional player and a club must be assessed in 
    consideration of all the specific circumstances of the individual case.
    <br><br>
    The Regulations to do not provide a defined list of 'just causes".
    <br><br>
    It is impossible to capture all potential conduct that might be considered just cause for the premature and unilateral termination of a 
    contract concluded between a professional player and a club.
    <br><br>
    Over the years, jurisprudence has established several criteria that define, in abstract terms, which combinations of circumstances should be 
    considered just causes.
    <br><br>
    A contract may be terminated with just cause where there is objective criteria [...] and there is a valid reason to do so.
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("CAS Case Management System")
