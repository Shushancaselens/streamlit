import streamlit as st
import pandas as pd

def render_fact_item(fact, is_disputed, source="", paragraphs="", classified=True):
    with st.container():
        st.markdown(f"""
            <div class="fact-item">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span>📅</span>
                    <p style="margin: 0; color: rgb(55, 65, 81);">{fact}</p>
                </div>
                <div style="margin-top: 0.5rem; padding-left: 1.25rem;">
                    <span style="font-size: 0.875rem; color: {'red' if is_disputed else 'green'}">
                        {f'Disputed by {source}' if is_disputed else 'Undisputed'}
                    </span>
                    <span style="font-size: 0.875rem; color: rgb(107, 114, 128); margin-left: 1rem;">
                        ¶{paragraphs}
                    </span>
                </div>
            </div>
        """, unsafe_allow_html=True)

def render_supporting_point(content, paragraphs, is_legal=True, is_direct=True):
    with st.container():
        st.markdown(f"""
            <div class="supporting-point">
                <div style="display: flex; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; background-color: {'rgb(219, 234, 254)' if is_legal else 'rgb(220, 252, 231)'};
                          color: {'rgb(30, 64, 175)' if is_legal else 'rgb(22, 101, 52)'};
                          border-radius: 0.25rem;">
                        {'Legal' if is_legal else 'Factual'}
                    </span>
                    {f'<span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; background-color: rgb(243, 244, 246); color: rgb(31, 41, 55); border-radius: 0.25rem;">Indirect</span>' if not is_direct else ''}
                </div>
                <p style="margin: 0; color: rgb(55, 65, 81);">{content}</p>
                <span style="font-size: 0.75rem; color: rgb(107, 114, 128); display: block; margin-top: 0.25rem;">
                    ¶{paragraphs}
                </span>
            </div>
        """, unsafe_allow_html=True)

def render_exhibit_item(id, title, summary, citations):
    with st.container():
        st.markdown(f"""
            <div class="exhibit-item">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <p style="margin: 0; font-weight: 500;">{id}: {title}</p>
                        <p style="font-size: 0.875rem; color: rgb(75, 85, 99); margin-top: 0.25rem;">{summary}</p>
                        <div style="margin-top: 0.5rem;">
                            <span style="font-size: 0.75rem; color: rgb(107, 114, 128);">Cited in: </span>
                            {' '.join([f'<span style="font-size: 0.75rem; background-color: rgb(229, 231, 235); border-radius: 0.25rem; padding: 0.125rem 0.5rem; margin-left: 0.25rem;">¶{cite}</span>' for cite in citations])}
                        </div>
                    </div>
                    <button style="background: none; border: none; color: rgb(107, 114, 128); cursor: pointer;">🔗</button>
                </div>
            </div>
        """, unsafe_allow_html=True)

def render_sub_argument_section(title, content, points_data, paragraphs):
    with st.expander(title):
        st.write(content)
        
        if points_data.get('legal_direct'):
            st.markdown("### Direct Legal Points")
            for point in points_data['legal_direct']:
                render_supporting_point(point['content'], point['paragraphs'], True, True)
                
        if points_data.get('legal_indirect'):
            st.markdown("### Indirect Legal Points")
            for point in points_data['legal_indirect']:
                render_supporting_point(point['content'], point['paragraphs'], True, False)
                
        if points_data.get('factual_direct'):
            st.markdown("### Direct Factual Points")
            for point in points_data['factual_direct']:
                render_supporting_point(point['content'], point['paragraphs'], False, True)
                
        if points_data.get('factual_indirect'):
            st.markdown("### Indirect Factual Points")
            for point in points_data['factual_indirect']:
                render_supporting_point(point['content'], point['paragraphs'], False, False)
                
        if points_data.get('evidence'):
            st.markdown("### Evidence")
            for exhibit in points_data['evidence']:
                render_exhibit_item(**exhibit)

def main():
    st.set_page_config(layout="wide", page_title="Legal Arguments Analysis")
    
    # Custom CSS
    st.markdown("""
        <style>
        .fact-item, .supporting-point, .exhibit-item {
            background-color: rgb(249, 250, 251);
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 0.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Main tabs
    tab1, tab2, tab3 = st.tabs(["📅 Timeline", "⚖️ Arguments", "🔗 Evidence"])
    
    with tab1:
        st.header("Event Timeline")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Appellant's Timeline")
            render_fact_item(
                "Agreement signed on February 19, 2025",
                False,
                paragraphs="15-16"
            )
            
        with col2:
            st.subheader("Respondent's Timeline")
            render_fact_item(
                "Authorization request filed on February 15, 2025",
                True,
                source="Appellant",
                paragraphs="22-23"
            )
    
    with tab2:
        st.header("Arguments")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Appellant's Position")
            club_name_data = {
                'legal_direct': [
                    {'content': "Name registration complies with regulations", 'paragraphs': "20-22"}
                ],
                'evidence': [
                    {
                        'id': "A-1",
                        'title': "Historical Registration Documents",
                        'summary': "Official records showing name usage",
                        'citations': ["20", "21", "24"]
                    }
                ]
            }
            render_sub_argument_section(
                "Club Name Analysis",
                "Analysis of the club name demonstrates continuity.",
                club_name_data,
                "20-45"
            )
            
        with col2:
            st.subheader("Respondent's Position")
    
    with tab3:
        st.header("Evidence")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Appellant's Exhibits")
            render_exhibit_item(
                "A-1",
                "Historical Registration Documents",
                "Official records showing club name usage since 1950",
                ["20", "21", "24"]
            )

if __name__ == "__main__":
    main()
