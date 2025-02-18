# app/main.py

import streamlit as st
from .styles import STREAMLIT_STYLE, SEARCH_ICON
from .components import render_argument_card
from .data import argument_data, filter_arguments

def main():
    # Configure the page
    st.set_page_config(layout="wide", page_title="Legal Arguments Comparison")
    
    # Apply custom styling
    st.markdown(STREAMLIT_STYLE, unsafe_allow_html=True)
    
    # Add search icon
    st.markdown(SEARCH_ICON, unsafe_allow_html=True)
    
    # Search input
    search = st.text_input(
        "", 
        placeholder="Search issues, arguments, or evidence...",
        label_visibility="collapsed"
    )
    
    # Filter and display arguments
    filtered_args = filter_arguments(argument_data, search)
    for arg in filtered_args:
        render_argument_card(arg)

if __name__ == "__main__":
    main()
