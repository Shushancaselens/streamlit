import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64
import os

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Facts"
if 'facts_view_mode' not in st.session_state:
    st.session_state.facts_view_mode = "table"

# Sample document sets structure
def get_document_sets():
    return {
        "claimant": [
            "1. Statement of Appeal",
            "3. Answer to Request for PM",
            "5. Appeal Brief",
            "7. Reply to Objection to Admissibility"
        ],
        "respondent": [
            "2. Request for a Stay", 
            "4. Answer to PM",
            "6. Brief on Admissibility",
            "8. Challenge",
            "Objection to Admissibility"
        ],
        "other": [
            "ChatGPT",
            "Jurisprudence",
            "Swiss Court"
        ]
    }

# Get all facts from the data
def get_all_facts(uploaded_files=None):
    # If there are uploaded files, extract facts from them
    if uploaded_files:
        facts = []
        for file in uploaded_files:
            # Determine which document set the file belongs to
            set_name = determine_document_set(file.name)
            party = determine_party(set_name)
            
            # Read the file content
            content = file.getvalue().decode("utf-8")
            
            # Extract facts from the content (simple example - would need to be more sophisticated)
            file_facts = extract_facts_from_content(content, file.name, set_name, party)
            facts.extend(file_facts)
        
        return facts
    
    # If no uploaded files, return sample facts
    return [
        {
            'point': "Continuous operation under same name since 1950",
            'date': "1950-present",
            'isDisputed': False,
            'party': "Claimant",
            'paragraphs': "18-19",
            'exhibits': ["C-1"],
            'argId': "1",
            'argTitle': "Sporting Succession",
            'document_set': "5. Appeal Brief"
        },
        {
            'point': "Brief administrative gap in 1975-1976",
            'date': "1975-1976",
            'isDisputed': True,
            'party': "Claimant",
            'paragraphs': "29-30",
            'exhibits': ["C-2"],
            'argId': "1.1.1",
            'argTitle': "Registration History",
            'document_set': "1. Statement of Appeal"
        },
        {
            'point': "Operations ceased between 1975-1976",
            'date': "1975-1976",
            'isDisputed': True,
            'party': "Respondent",
            'paragraphs': "206-207",
            'exhibits': ["R-1"],
            'argId': "1",
            'argTitle': "Sporting Succession Rebuttal",
            'document_set': "6. Brief on Admissibility"
        },
        {
            'point': "Registration formally terminated on April 30, 1975",
            'date': "April 30, 1975",
            'isDisputed': False,
            'party': "Respondent",
            'paragraphs': "226-227",
            'exhibits': ["R-2"],
            'argId': "1.1.1",
            'argTitle': "Registration Gap Evidence",
            'document_set': "Objection to Admissibility"
        },
        {
            'point': "CAS precedent on sporting succession",
            'date': "2016",
            'isDisputed': False,
            'party': "Other",
            'paragraphs': "N/A",
            'exhibits': [],
            'argId': "N/A",
            'argTitle': "Legal Framework",
            'document_set': "Jurisprudence"
        }
    ]

# Helper function to determine which document set a file belongs to
def determine_document_set(filename):
    doc_sets = get_document_sets()
    
    # Flatten all document sets
    all_sets = []
    for category, sets in doc_sets.items():
        all_sets.extend(sets)
    
    # Find the matching document set
    for set_name in all_sets:
        if set_name in filename:
            return set_name
    
    return "Other"

# Helper function to determine which party a document set belongs to
def determine_party(set_name):
    doc_sets = get_document_sets()
    
    if set_name in doc_sets["claimant"]:
        return "Claimant"
    elif set_name in doc_sets["respondent"]:
        return "Respondent"
    else:
        return "Other"

# Helper function to extract facts from content
def extract_facts_from_content(content, filename, set_name, party):
    # This would be a more sophisticated parser in a real application
    # Here we'll just return some dummy facts based on the filename
    
    facts = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if "fact:" in line.lower() or ":" in line:
            # Simple heuristic - lines with "fact:" or containing a colon might be facts
            parts = line.split(":", 1)
            if len(parts) > 1:
                fact = {
                    'point': parts[1].strip(),
                    'date': "N/A",  # Would need more sophisticated extraction
                    'isDisputed': "disputed" in line.lower(),
                    'party': party,
                    'paragraphs': f"{i+1}",
                    'exhibits': [],
                    'argId': "N/A",
                    'argTitle': parts[0].strip(),
                    'document_set': set_name
                }
                facts.append(fact)
    
    # If no facts found, add a placeholder
    if not facts:
        facts.append({
            'point': f"Content from {filename}",
            'date': "N/A",
            'isDisputed': False,
            'party': party,
            'paragraphs': "N/A",
            'exhibits': [],
            'argId': "N/A",
            'argTitle': "Document Content",
            'document_set': set_name
        })
    
    return facts

# Function to create CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Main app
def main():
    # Add Streamlit sidebar with navigation buttons
    with st.sidebar:
        # Add the logo and CaseLens text
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
              <mask id="app-mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#app-mask)">
                <!-- Rounded square background -->
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                <!-- App icon -->
                <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
              </g>
            </svg>
            <h1 style="margin-left: 10px; font-weight: 600; color: #4D68F9;">CaseLens</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
        
        # Custom CSS for button styling
        st.markdown("""
        <style>
        .stButton > button {
            width: 100%;
            border-radius: 6px;
            height: 50px;
            margin-bottom: 10px;
            transition: all 0.3s;
        }
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Define button click handlers
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Create buttons with names
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
    
    # Facts page content
    if st.session_state.view == "Facts":
        st.title("Case Facts")
        
        # File uploader for document sets
        uploaded_files = st.file_uploader("Upload documents", accept_multiple_files=True)
        
        # Get facts data
        facts_data = get_all_facts(uploaded_files)
        
        # View selector
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("Facts View")
        with col2:
            view_mode = st.radio(
                "View Mode:",
                ["Table View", "Document Sets View"],
                horizontal=True,
                key="view_mode",
                label_visibility="collapsed"
            )
            st.session_state.facts_view_mode = "table" if view_mode == "Table View" else "sets"
        
        # Create tabs for filtering facts
        tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
        
        # Convert facts list to dataframe
        facts_df = pd.DataFrame(facts_data)
        
        # Create custom styling for the dataframe
        def highlight_disputed(row):
            if row['isDisputed']:
                return ['background-color: rgba(229, 62, 62, 0.05)'] * len(row)
            return [''] * len(row)
        
        with tab1:
            if st.session_state.facts_view_mode == "table":
                # Standard table view
                if not facts_df.empty:
                    styled_df = facts_df.style.apply(highlight_disputed, axis=1)
                    st.dataframe(styled_df, use_container_width=True)
                    st.markdown(get_csv_download_link(facts_df, "all_facts.csv", "Download All Facts CSV"), unsafe_allow_html=True)
            else:
                # Document sets view
                if not facts_df.empty:
                    # Group by document set
                    doc_sets = facts_df['document_set'].unique()
                    
                    for doc_set in sorted(doc_sets):
                        st.subheader(doc_set)
                        set_facts = facts_df[facts_df['document_set'] == doc_set]
                        styled_set = set_facts.style.apply(highlight_disputed, axis=1)
                        st.dataframe(styled_set, use_container_width=True)
                        st.markdown(get_csv_download_link(set_facts, f"{doc_set.replace(' ', '_')}_facts.csv", f"Download {doc_set} Facts CSV"), unsafe_allow_html=True)
                        st.markdown("---")
        
        with tab2:
            disputed_facts = facts_df[facts_df['isDisputed'] == True]
            
            if st.session_state.facts_view_mode == "table":
                # Standard table view for disputed facts
                if not disputed_facts.empty:
                    styled_disputed = disputed_facts.style.apply(highlight_disputed, axis=1)
                    st.dataframe(styled_disputed, use_container_width=True)
                    st.markdown(get_csv_download_link(disputed_facts, "disputed_facts.csv", "Download Disputed Facts CSV"), unsafe_allow_html=True)
                else:
                    st.info("No disputed facts found.")
            else:
                # Document sets view for disputed facts
                if not disputed_facts.empty:
                    # Group by document set
                    doc_sets = disputed_facts['document_set'].unique()
                    
                    for doc_set in sorted(doc_sets):
                        st.subheader(doc_set)
                        set_facts = disputed_facts[disputed_facts['document_set'] == doc_set]
                        styled_set = set_facts.style.apply(highlight_disputed, axis=1)
                        st.dataframe(styled_set, use_container_width=True)
                        st.markdown(get_csv_download_link(set_facts, f"disputed_{doc_set.replace(' ', '_')}_facts.csv", f"Download Disputed {doc_set} Facts CSV"), unsafe_allow_html=True)
                        st.markdown("---")
                else:
                    st.info("No disputed facts found.")
        
        with tab3:
            undisputed_facts = facts_df[facts_df['isDisputed'] == False]
            
            if st.session_state.facts_view_mode == "table":
                # Standard table view for undisputed facts
                if not undisputed_facts.empty:
                    st.dataframe(undisputed_facts, use_container_width=True)
                    st.markdown(get_csv_download_link(undisputed_facts, "undisputed_facts.csv", "Download Undisputed Facts CSV"), unsafe_allow_html=True)
                else:
                    st.info("No undisputed facts found.")
            else:
                # Document sets view for undisputed facts
                if not undisputed_facts.empty:
                    # Group by document set
                    doc_sets = undisputed_facts['document_set'].unique()
                    
                    for doc_set in sorted(doc_sets):
                        st.subheader(doc_set)
                        set_facts = undisputed_facts[undisputed_facts['document_set'] == doc_set]
                        st.dataframe(set_facts, use_container_width=True)
                        st.markdown(get_csv_download_link(set_facts, f"undisputed_{doc_set.replace(' ', '_')}_facts.csv", f"Download Undisputed {doc_set} Facts CSV"), unsafe_allow_html=True)
                        st.markdown("---")
                else:
                    st.info("No undisputed facts found.")

if __name__ == "__main__":
    main()
