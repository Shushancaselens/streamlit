import streamlit as st
import pandas as pd

# Configure page settings
st.set_page_config(layout="wide")

# Custom CSS to match the original design
st.markdown("""
<style>
    /* General styles */
    .stApp {
        background-color: #f9fafb;
    }
    
    /* Card styles */
    .card {
        background-color: white;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
    }
    
    /* Typography */
    .header-blue {
        color: #2563eb;
        font-size: 1.125rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .header-red {
        color: #dc2626;
        font-size: 1.125rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .section-header {
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 0.75rem;
    }
    
    /* Supporting point styles */
    .supporting-point {
        background-color: #f3f4f6;
        border-radius: 0.375rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    
    .legal-tag {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        margin-right: 0.5rem;
    }
    
    .factual-tag {
        background-color: #dcfce7;
        color: #166534;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        margin-right: 0.5rem;
    }
    
    .indirect-tag {
        background-color: #f3f4f6;
        color: #374151;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
    }
    
    /* Paragraph reference style */
    .paragraph-ref {
        color: #6b7280;
        font-size: 0.75rem;
    }

    /* Custom tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
    }

    .stTabs [data-baseweb="tab"] {
        padding: 0.5rem 1rem;
        font-size: 0.875rem;
        font-weight: 500;
    }

    .stTabs [data-baseweb="tab-border"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'detailed'

# Header with search and view options
st.markdown("### Arguments Analysis")

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.text_input("🔍 Search arguments...", placeholder="Enter keywords...")
with col2:
    view_type = st.radio("View Type:", ["Detailed", "Table"], horizontal=True, key="view_type")
with col3:
    st.button("📥 Export to Excel")
    st.button("📋 Copy")

# Tabs for main sections
tabs = st.tabs(["⏱️ Timeline", "⚖️ Arguments", "📎 Evidence"])

with tabs[1]:  # Arguments tab
    if view_type == "Detailed":
        # Two-column layout for detailed view
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<p class="header-blue">Appellant\'s Position</p>', unsafe_allow_html=True)
            
            # General Introduction
            with st.expander("General Introduction", expanded=True):
                st.markdown("""
                <div class="card">
                    <p style="font-size: 0.875rem; color: #374151; margin-bottom: 0.75rem;">
                        Assessment of sporting succession requires comprehensive analysis of multiple established criteria, 
                        including but not limited to the club's name, colors, logo, and public perception. Each element 
                        must be evaluated both independently and as part of the broader succession context.
                    </p>
                    <p style="font-size: 0.875rem; color: #374151;">
                        The analysis follows CAS jurisprudence on sporting succession, particularly focusing on continuous 
                        use and public recognition of club identity elements.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            # Public Perception Analysis
            with st.expander("Public Perception Analysis", expanded=True):
                st.markdown("""
                <div class="card">
                    <div style="margin-bottom: 1rem;">
                        <p style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Overview</p>
                        <p style="font-size: 0.875rem; color: #374151;">
                            Public perception strongly supports recognition as sporting successor, demonstrated through 
                            consistent fan support and media treatment.
                        </p>
                    </div>
                    
                    <div style="margin-bottom: 1rem;">
                        <p style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Legal Supporting Points</p>
                        <div class="supporting-point">
                            <span class="legal-tag">Legal</span>
                            <p style="font-size: 0.875rem; color: #374151; margin-top: 0.5rem;">
                                Public perception as key factor in CAS jurisprudence
                            </p>
                            <span class="paragraph-ref">¶15-17</span>
                        </div>
                    </div>
                    
                    <div>
                        <p style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Factual Supporting Points</p>
                        <div class="supporting-point">
                            <span class="factual-tag">Factual</span>
                            <p style="font-size: 0.875rem; color: #374151; margin-top: 0.5rem;">
                                Consistent media recognition since 1950
                            </p>
                            <span class="paragraph-ref">¶18-19</span>
                        </div>
                        <div class="supporting-point">
                            <span class="factual-tag">Factual</span>
                            <span class="indirect-tag">Indirect</span>
                            <p style="font-size: 0.875rem; color: #374151; margin-top: 0.5rem;">
                                Uninterrupted fan support and recognition
                            </p>
                            <span class="paragraph-ref">¶20-21</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown('<p class="header-red">Respondent\'s Position</p>', unsafe_allow_html=True)
            
            # General Introduction
            with st.expander("General Introduction", expanded=True):
                st.markdown("""
                <div class="card">
                    <p style="font-size: 0.875rem; color: #374151; margin-bottom: 0.75rem;">
                        Sporting succession analysis must consider practical realities beyond superficial similarities. 
                        Historical gaps and substantive changes in operations preclude finding of succession.
                    </p>
                    <p style="font-size: 0.875rem; color: #374151;">
                        Recent CAS jurisprudence emphasizes the need for continuous operational connection, not merely 
                        similar identifying elements.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            # Public Perception Analysis
            with st.expander("Public Perception Analysis", expanded=True):
                st.markdown("""
                <div class="card">
                    <div style="margin-bottom: 1rem;">
                        <p style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Overview</p>
                        <p style="font-size: 0.875rem; color: #374151;">
                            Public perception alone insufficient to establish sporting succession; substantial operational 
                            discontinuities override superficial recognition.
                        </p>
                    </div>
                    
                    <div style="margin-bottom: 1rem;">
                        <p style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Legal Supporting Points</p>
                        <div class="supporting-point">
                            <span class="legal-tag">Legal</span>
                            <p style="font-size: 0.875rem; color: #374151; margin-top: 0.5rem;">
                                CAS jurisprudence: public perception secondary to operational continuity
                            </p>
                            <span class="paragraph-ref">¶40-42</span>
                        </div>
                        <div class="supporting-point">
                            <span class="legal-tag">Legal</span>
                            <p style="font-size: 0.875rem; color: #374151; margin-top: 0.5rem;">
                                Legal precedent requiring comprehensive analysis beyond public opinion
                            </p>
                            <span class="paragraph-ref">¶43-44</span>
                        </div>
                    </div>
                    
                    <div>
                        <p style="font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;">Factual Supporting Points</p>
                        <div class="supporting-point">
                            <span class="factual-tag">Factual</span>
                            <p style="font-size: 0.875rem; color: #374151; margin-top: 0.5rem;">
                                Media coverage gaps between 1975-1976
                            </p>
                            <span class="paragraph-ref">¶45-46</span>
                        </div>
                        <div class="supporting-point">
                            <span class="factual-tag">Factual</span>
                            <p style="font-size: 0.875rem; color: #374151; margin-top: 0.5rem;">
                                Fan support divided between multiple claiming entities
                            </p>
                            <span class="paragraph-ref">¶47-48</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    else:  # Table view
        # Create sample data for the table view
        data = {
            'Issue': ['Jurisdiction', 'Public Perception', 'Club Name', 'Club Colors'],
            'Appellant Position': [
                'CAS has jurisdiction based on agreement',
                'Strong public recognition supports succession',
                'Continuous use of name since 1950',
                'Consistent use of colors'
            ],
            'Respondent Position': [
                'Agreement does not cover this dispute',
                'Public perception not decisive',
                'Registration gaps in name usage',
                'Color variations documented'
            ]
        }
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

with tabs[0]:  # Timeline tab
    st.markdown("### Event Timeline")
    # Add timeline implementation here

with tabs[2]:  # Evidence tab
    st.markdown("### Evidence Summary")
    # Add evidence implementation here
