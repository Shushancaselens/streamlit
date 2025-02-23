import streamlit as st
from datetime import datetime
import pandas as pd

# [Previous CSS and other component functions remain the same...]

def render_sub_argument_section(title, content, points_data, paragraphs):
    with st.expander(title):
        # Section container
        st.markdown(f"""
            <div style="border: 1px solid rgb(229, 231, 235); border-radius: 0.5rem; margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; padding: 0.75rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span>▼</span>
                        <h5 style="margin: 0; font-weight: 500; font-size: 0.875rem;">{title}</h5>
                    </div>
                    <span style="font-size: 0.75rem; color: rgb(107, 114, 128);">¶{paragraphs}</span>
                </div>
                <div style="padding: 1rem; border-top: 1px solid rgb(229, 231, 235);">
            """, unsafe_allow_html=True)

        # Overview section
        st.markdown("""
            <div style="margin-bottom: 1rem;">
                <h6 style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Overview</h6>
            </div>
        """, unsafe_allow_html=True)
        st.write(content)

        # Legal Points
        if points_data.get('legal_direct') or points_data.get('legal_indirect'):
            st.markdown("##### Legal Supporting Points")
            
            if points_data.get('legal_direct'):
                st.markdown("**Direct Legal Points**")
                for point in points_data['legal_direct']:
                    render_supporting_point(point['content'], point['paragraphs'], is_legal=True, is_direct=True)
            
            if points_data.get('legal_indirect'):
                st.markdown("**Indirect Legal Points**")
                for point in points_data['legal_indirect']:
                    render_supporting_point(point['content'], point['paragraphs'], is_legal=True, is_direct=False)

        # Factual Points
        if points_data.get('factual_direct') or points_data.get('factual_indirect'):
            st.markdown("##### Factual Supporting Points")
            
            if points_data.get('factual_direct'):
                st.markdown("**Direct Factual Points**")
                for point in points_data['factual_direct']:
                    render_supporting_point(point['content'], point['paragraphs'], is_legal=False, is_direct=True)
            
            if points_data.get('factual_indirect'):
                st.markdown("**Indirect Factual Points**")
                for point in points_data['factual_indirect']:
                    render_supporting_point(point['content'], point['paragraphs'], is_legal=False, is_direct=False)

        # Evidence section
        if points_data.get('evidence'):
            st.markdown("##### Evidence")
            for exhibit in points_data['evidence']:
                render_exhibit_item(**exhibit)

        st.markdown("</div></div>", unsafe_allow_html=True)

def main():
    # [Rest of the main function implementation remains the same...]

if __name__ == "__main__":
    main()
