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

st.markdown("---")

# ============ OPTION 1: Using st.pills() as Display Tags ============
st.markdown("#### Option 1: Pills as Tags (Read-Only)")
st.pills("Parties", ["Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje"], disabled=True, default=["Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje"])
st.pills("Procedure", ["Appeal Arbitration Procedure"], disabled=True, default=["Appeal Arbitration Procedure"])
st.pills("Category", ["Award"], disabled=True, default=["Award"])
st.pills("President", ["Olivier Carrard"], disabled=True, default=["Olivier Carrard"])
st.pills("Arbitrators", ["Unknown, Unknown"], disabled=True, default=["Unknown, Unknown"])

st.markdown("---")

# ============ OPTION 2: Inline Badges using Markdown ============
st.markdown("#### Option 2: Custom Badge Style")
st.markdown("""
<style>
.badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    margin: 0.25rem;
    border-radius: 0.5rem;
    background-color: #f0f2f6;
    border: 1px solid #d1d5db;
    font-size: 0.875rem;
}
.badge-label {
    font-weight: 600;
    color: #374151;
}
.badge-value {
    color: #6b7280;
}
</style>

<div>
    <span class="badge"><span class="badge-label">Parties:</span> <span class="badge-value">Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje</span></span>
    <span class="badge"><span class="badge-label">Procedure:</span> <span class="badge-value">Appeal Arbitration Procedure</span></span>
    <span class="badge"><span class="badge-label">Category:</span> <span class="badge-value">Award</span></span>
    <span class="badge"><span class="badge-label">President:</span> <span class="badge-value">Olivier Carrard</span></span>
    <span class="badge"><span class="badge-label">Arbitrators:</span> <span class="badge-value">Unknown, Unknown</span></span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============ OPTION 3: Using st.tag (if available) or colored pills ============
st.markdown("#### Option 3: Colored Badge Style")

# Using columns to create badge-like layout
col1, col2 = st.columns([1, 5])
with col1:
    st.info("**Parties:**", icon="👥")
with col2:
    st.write("Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje")

col1, col2 = st.columns([1, 5])
with col1:
    st.info("**Procedure:**", icon="📋")
with col2:
    st.write("Appeal Arbitration Procedure")

col1, col2 = st.columns([1, 5])
with col1:
    st.info("**Category:**", icon="🏷️")
with col2:
    st.write("Award")

col1, col2 = st.columns([1, 5])
with col1:
    st.info("**President:**", icon="👤")
with col2:
    st.write("Olivier Carrard")

col1, col2 = st.columns([1, 5])
with col1:
    st.info("**Arbitrators:**", icon="⚖️")
with col2:
    st.write("Unknown, Unknown")

st.markdown("---")

# ============ OPTION 4: Compact Tags in Grid ============
st.markdown("#### Option 4: Grid of Tags")
with st.container(border=True):
    cols = st.columns(2)
    
    with cols[0]:
        st.markdown("🏷️ **Parties:** Samsunspor Futbol Kulübü A.S. v. Brice Dja Djedje")
        st.markdown("🏷️ **Procedure:** Appeal Arbitration Procedure")
        st.markdown("🏷️ **Category:** Award")
    
    with cols[1]:
        st.markdown("🏷️ **President:** Olivier Carrard")
        st.markdown("🏷️ **Arbitrators:** Unknown, Unknown")

st.markdown("---")

# ============ OPTION 5: Status/Success/Info Tags ============
st.markdown("#### Option 5: Using Status Elements as Tags")
cols = st.columns(5)

with cols[0]:
    st.success("**Parties**  \nSamsunspor v. Dja Djedje", icon="👥")

with cols[1]:
    st.info("**Procedure**  \nAppeal Arbitration", icon="📋")

with cols[2]:
    st.warning("**Category**  \nAward", icon="🏷️")

with cols[3]:
    st.info("**President**  \nO. Carrard", icon="👤")

with cols[4]:
    st.error("**Arbitrators**  \nUnknown, Unknown", icon="⚖️")

st.markdown("---")

# Buttons
col1, col2 = st.columns(2)
with col1:
    st.button("📄 PDF", use_container_width=True)
with col2:
    st.button("💾 Save", use_container_width=True)

st.caption("CAS Case Management System")
