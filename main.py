# streamlit_custom_css.py

CSS_STYLES = """
<style>
    /* Main container styles */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1rem;
    }
    
    /* Search bar styles */
    .stTextInput > div > div > input {
        padding: 0.75rem 1rem 0.75rem 2.5rem;
        border-radius: 0.75rem;
        border: 1px solid #E5E7EB;
        font-size: 0.875rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #6366F1;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
    }
    
    /* Argument section styles */
    .argument-section {
        padding: 1.5rem;
        background-color: white;
        border-radius: 1rem;
        margin-bottom: 1rem;
    }
    
    .section-title {
        font-size: 1.125rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .appellant-color {
        color: #4F46E5;
    }
    
    .respondent-color {
        color: #E11D48;
    }
    
    .main-argument {
        background-color: #F9FAFB;
        padding: 1rem;
        border-radius: 0.75rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
    }
    
    .subsection-title {
        font-size: 0.875rem;
        font-weight: 500;
        color: #374151;
        margin: 1rem 0;
    }
    
    /* Card styles */
    .argument-card {
        padding: 0.75rem;
        background-color: white;
        border: 1px solid #E5E7EB;
        border-radius: 0.75rem;
        margin-bottom: 0.5rem;
    }
    
    .evidence-card {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background-color: white;
        border: 1px solid #E5E7EB;
        border-radius: 0.75rem;
        margin-bottom: 0.5rem;
        transition: all 0.2s;
    }
    
    .evidence-card:hover {
        border-color: #818CF8;
        background-color: rgba(99, 102, 241, 0.05);
    }
    
    .evidence-id {
        padding: 0.25rem 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .appellant-color-bg {
        background-color: #EEF2FF;
        color: #4F46E5;
    }
    
    .respondent-color-bg {
        background-color: #FFF1F2;
        color: #E11D48;
    }
    
    .case-law-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem;
        background-color: white;
        border: 1px solid #E5E7EB;
        border-radius: 0.75rem;
        margin-bottom: 0.5rem;
    }
    
    /* Button styles */
    .stButton > button {
        padding: 0.75rem 1.25rem;
        border-radius: 0.75rem;
        background-color: #EEF2FF;
        color: #4F46E5;
        font-weight: 500;
        border: none;
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        background-color: #E0E7FF;
    }
    
    /* Expander styles */
    .streamlit-expanderHeader {
        border-radius: 1rem;
        background-color: white;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        transition: all 0.2s;
    }
    
    .streamlit-expanderHeader:hover {
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    
    .streamlit-expanderContent {
        border: none !important;
        background-color: white;
    }
</style>
"""
