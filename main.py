import streamlit as st
import pandas as pd
from datetime import datetime

# Configure the page
st.set_page_config(layout="wide", page_title="Legal Arguments Comparison")

# Custom CSS to match the React design
st.markdown("""
<style>
    /* General styles */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Search bar styling */
    .search-container {
        background: white;
        padding: 0.75rem;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
        margin-bottom: 1.5rem;
    }
    
    /* Card styling */
    .argument-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 1rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.2s;
    }
    
    .argument-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    /* Category tag */
    .category-tag {
        background: #f3f4f6;
        color: #4b5563;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
        display: inline-block;
    }
    
    /* Position headers */
    .position-header {
        font-size: 1.125rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .appellant-color {
        color: #4f46e5;
    }
    
    .respondent-color {
        color: #e11d48;
    }
    
    /* Evidence styling */
    .evidence-item {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
        transition: all 0.2s;
    }
    
    .evidence-item:hover {
        border-color: #818cf8;
        background: #eef2ff;
    }
    
    .evidence-id {
        background: #eef2ff;
        color: #4f46e5;
        padding: 0.25rem 0.5rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        font-weight: 500;
        display: inline-block;
        margin-right: 0.5rem;
    }
    
    .evidence-id.respondent {
        background: #fef2f2;
        color: #e11d48;
    }
    
    /* Details section */
    .details-section {
        background: #f9fafb;
        border-radius: 0.75rem;
        padding: 1rem;
        margin-top: 0.5rem;
    }
    
    /* Custom bullet points */
    .custom-bullet {
        display: flex;
        align-items: start;
        margin-bottom: 0.5rem;
    }
    
    .bullet-point {
        width: 6px;
        height: 6px;
        background: #9ca3af;
        border-radius: 50%;
        margin-top: 0.5rem;
        margin-right: 0.75rem;
        flex-shrink: 0;
    }
</style>
""", unsafe_allow_html=True)

# Data
argument_data = [
    {
        "id": "1",
        "issue": "CAS Jurisdiction",
        "category": "jurisdiction",
        "appellant": {
            "mainArgument": "CAS Has Authority to Hear This Case",
            "details": [
                "The Federation's Anti-Doping Rules explicitly allow CAS to hear appeals",
                "Athlete has completed all required internal appeal procedures first",
                "Athlete signed agreement allowing CAS to handle disputes"
            ],
            "evidence": [
                {"id": "C1", "desc": "Federation Rules, Art. 60"},
                {"id": "C2", "desc": "Athlete's license containing arbitration agreement"},
                {"id": "C3", "desc": "Appeal submission documents"}
            ],
            "caselaw": ["CAS 2019/A/XYZ"]
        },
        "respondent": {
            "mainArgument": "CAS Cannot Hear This Case Yet",
            "details": [
                "Athlete skipped required steps in federation's appeal process",
                "Athlete missed important appeal deadlines within federation",
                "Must follow proper appeal steps before going to CAS"
            ],
            "evidence": [
                {"id": "R1", "desc": "Federation internal appeals process documentation"},
                {"id": "R2", "desc": "Timeline of appeals process"},
                {"id": "R3", "desc": "Federation handbook on procedures"}
            ],
            "caselaw": ["CAS 2019/A/123", "CAS 2018/A/456"]
        }
    },
    # ... (rest of the argument data)
]

# Search functionality
search = st.text_input("", placeholder="Search issues, arguments, or evidence...", 
                      help="Search through all fields")

def matches_search(arg, search_term):
    if not search_term:
        return True
    
    search_term = search_term.lower()
    
    # Check issue and category
    if search_term in arg["issue"].lower() or search_term in arg["category"].lower():
        return True
    
    # Check appellant details
    for detail in arg["appellant"]["details"]:
        if search_term in detail.lower():
            return True
    
    # Check respondent details
    for detail in arg["respondent"]["details"]:
        if search_term in detail.lower():
            return True
    
    # Check evidence
    for evidence in arg["appellant"]["evidence"] + arg["respondent"]["evidence"]:
        if search_term in evidence["desc"].lower():
            return True
    
    return False

# Filter arguments based on search
filtered_arguments = [arg for arg in argument_data if matches_search(arg, search)]

# Display arguments
for arg in filtered_arguments:
    with st.expander(f"{arg['issue']} ({arg['category']})"):
        cols = st.columns(2)
        
        # Appellant's position
        with cols[0]:
            st.markdown(f"""
            <div class='position-header appellant-color'>Appellant's Position</div>
            <div class='details-section'>
                <div style='font-weight: 500;'>{arg['appellant']['mainArgument']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("##### Supporting Points")
            for detail in arg['appellant']['details']:
                st.markdown(f"""
                <div class='custom-bullet'>
                    <div class='bullet-point'></div>
                    <div>{detail}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("##### Evidence")
            for evidence in arg['appellant']['evidence']:
                st.markdown(f"""
                <div class='evidence-item'>
                    <span class='evidence-id'>{evidence['id']}</span>
                    <a href='#'>{evidence['desc']}</a>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("##### Case Law")
            for case in arg['appellant']['caselaw']:
                st.markdown(f"- {case}")
        
        # Respondent's position
        with cols[1]:
            st.markdown(f"""
            <div class='position-header respondent-color'>Respondent's Position</div>
            <div class='details-section'>
                <div style='font-weight: 500;'>{arg['respondent']['mainArgument']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("##### Supporting Points")
            for detail in arg['respondent']['details']:
                st.markdown(f"""
                <div class='custom-bullet'>
                    <div class='bullet-point'></div>
                    <div>{detail}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("##### Evidence")
            for evidence in arg['respondent']['evidence']:
                st.markdown(f"""
                <div class='evidence-item'>
                    <span class='evidence-id respondent'>{evidence['id']}</span>
                    <a href='#'>{evidence['desc']}</a>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("##### Case Law")
            for case in arg['respondent']['caselaw']:
                st.markdown(f"- {case}")
