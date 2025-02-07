Let me create a minimal working version first, then we can build upon it:

```python
import streamlit as st
import pandas as pd

# Basic page config
st.set_page_config(layout="wide")

# Basic data
penalties = pd.DataFrame([
    {"Rule": "Rule 5.5", "Description": "Missing Prayer for Relief", "Points": 4, "R": 2},
    {"Rule": "Rule 5.17", "Description": "Non-Permitted Abbreviations (5 found)", "Points": 3, "R": 0},
    {"Rule": "Rule 5.13", "Description": "Improper Citation", "Points": 3, "R": 0}
])

# Sidebar
with st.sidebar:
    st.title("Jessup Checker")
    st.markdown("### Penalty Points: 10")

# Main content
st.title("Jessup Memorial Penalty Checker")

# Tabs
tab1, tab2 = st.tabs(["Overview", "Details"])

with tab1:
    # Summary metrics
    cols = st.columns(4)
    with cols[0]:
        st.metric("Violations", "7", "Critical")
    with cols[1]:
        st.metric("Word Count", "98%", "Safe")
    with cols[2]:
        st.metric("Missing Parts", "1", "Warning")
    with cols[3]:
        st.metric("Abbreviations", "5", "Warning")
        
    # Penalties table
    st.subheader("Penalty Summary")
    st.dataframe(penalties, hide_index=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Cover Page")
        st.markdown("✅ Team Number: 349A")
        st.markdown("✅ Court Name: ICJ")
        st.markdown("✅ Year: 2025")
        
    with col2:
        st.subheader("Memorial Parts")
        st.markdown("✅ Table of Contents")
        st.markdown("✅ Statement of Facts")
        st.markdown("❌ Prayer for Relief")

    # Word counts
    st.subheader("Word Counts")
    word_counts = {
        "Statement of Facts": {"count": 1196, "limit": 1200},
        "Pleadings": {"count": 9424, "limit": 9500}
    }
    
    for section, data in word_counts.items():
        percentage = (data["count"] / data["limit"]) * 100
        st.write(f"**{section}**")
        st.progress(percentage/100)
        st.caption(f"{data['count']}/{data['limit']} words ({percentage:.1f}%)")

# Action buttons
if st.button("Check Memorial"):
    st.success("Check completed!")
```

This is a basic working version. Does it run without errors? Once you confirm it works, we can add more features and complexity step by step.
