import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling with updated colors
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .position-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 0.5rem;
    }
    .evidence-tag {
        background-color: #EEF2FF;
        color: #4D68F9;
        padding: 0.25rem 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .category-tag {
        background-color: #f3f4f6;
        color: #4B5563;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
        margin-left: 0.5rem;
    }
    .main-argument {
        background-color: #f9fafb;
        padding: 1rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
    }
    .preview-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-top: 0.5rem;
    }
    .preview-section {
        padding: 1rem;
        background-color: #f9fafb;
        border-radius: 0.75rem;
    }
    .preview-label {
        font-size: 0.875rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .preview-label.appellant, .preview-label.respondent {
        color: #4D68F9;
    }
    .preview-text {
        color: #6b7280;
        font-size: 0.875rem;
    }
    .evidence-card {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        margin-bottom: 0.5rem;
        transition: all 0.2s;
    }
    .evidence-card:hover {
        border-color: #4D68F9;
        background-color: #EEF2FF;
    }
    .evidence-link {
        color: #4D68F9;
        text-decoration: none;
        transition: all 0.2s;
    }
    .evidence-link:hover {
        color: #3D4ECA;
        text-decoration: underline;
    }
    
    /* Override Streamlit's default button colors */
    .stButton button {
        background-color: #EEF2FF;
        color: #4D68F9;
        border: 1px solid #4D68F9;
    }
    .stButton button:hover {
        background-color: #4D68F9;
        color: white;
        border: 1px solid #4D68F9;
    }
    .stButton button[data-baseweb="button"][kind="primary"] {
        background-color: #4D68F9;
        color: white;
    }
    .stButton button[data-baseweb="button"][kind="primary"]:hover {
        background-color: #3D4ECA;
    }
    
    /* Style the select box */
    .stSelectbox > div > div {
        background-color: white;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
    }
    
    /* Style the multiselect */
    .stMultiSelect > div > div {
        background-color: white;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
    }
    
    /* Style the slider */
    .stSlider > div > div > div {
        background-color: #4D68F9;
    }
    
    /* Style the radio buttons */
    .stRadio > div {
        gap: 1rem;
    }
    .stRadio > div > label > div:first-child {
        background-color: #4D68F9;
    }
</style>
""", unsafe_allow_html=True)
