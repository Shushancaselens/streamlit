import streamlit as st
import json
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Facts"

# Function to create CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Get all facts from the data
def get_all_facts():
    facts = [
        {
            'point': "Continuous operation under same name since 1950",
            'date': "1950-present",
            'isDisputed': False,
            'party': "Appellant",
            'paragraphs': "18-19",
            'exhibits': ["C-1"],
            'argId': "1",
            'argTitle': "Sporting Succession"
        },
        {
            'point': "Initial registration in 1950",
            'date': "1950",
            'isDisputed': False,
            'party': "Appellant",
            'paragraphs': "25-26",
            'exhibits': ["C-2"],
            'argId': "1.1.1",
            'argTitle': "Registration History"
        },
        {
            'point': "Brief administrative gap in 1975-1976",
            'date': "1975-1976",
            'isDisputed': True,
            'party': "Appellant",
            'paragraphs': "29-30",
            'exhibits': ["C-2"],
            'argId': "1.1.1",
            'argTitle': "Registration History"
        },
        {
            'point': "Operations ceased between 1975-1976",
            'date': "1975-1976",
            'isDisputed': True,
            'party': "Respondent",
            'paragraphs': "206-207",
            'exhibits': ["R-1"],
            'argId': "1",
            'argTitle': "Sporting Succession Rebuttal"
        },
        {
            'point': "Registration formally terminated on April 30, 1975",
            'date': "April 30, 1975",
            'isDisputed': False,
            'party': "Respondent",
            'paragraphs': "226-227",
            'exhibits': ["R-2"],
            'argId': "1.1.1",
            'argTitle': "Registration Gap Evidence"
        },
        {
            'point': "New entity registered on September 15, 1976",
            'date': "September 15, 1976",
            'isDisputed': False,
            'party': "Respondent",
            'paragraphs': "228-229",
            'exhibits': ["R-2"],
            'argId': "1.1.1",
            'argTitle': "Registration Gap Evidence"
        }
    ]
    return facts

# Main app - sidebar and facts page
def main():
    # Add Streamlit sidebar with navigation buttons only
    with st.sidebar:
        # Add the logo and CaseLens text
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
              <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
                <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
              </mask>
              <g mask="url(#whatsapp-mask)">
                <!-- Rounded square background -->
                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                <!-- WhatsApp phone icon -->
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
    
    # Show facts page (assuming we're only implementing the Facts view)
    st.title("Case Facts")
    
    # Create tabs for different fact views
    facts_tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
    
    # Get the facts data
    facts_data = get_all_facts()
    
    # Convert to DataFrame for easier manipulation
    facts_df = pd.DataFrame(facts_data)
    
    # Process for different tabs
    with facts_tabs[0]:  # All Facts
        # Convert exhibits to string for display
        facts_df_display = facts_df.copy()
        facts_df_display['exhibits'] = facts_df_display['exhibits'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
        facts_df_display['Status'] = facts_df_display['isDisputed'].apply(lambda x: 'Disputed' if x else 'Undisputed')
        
        # Display the table
        st.dataframe(
            facts_df_display[['date', 'point', 'party', 'Status', 'argId', 'argTitle', 'exhibits']].rename(
                columns={
                    'date': 'Date', 
                    'point': 'Event', 
                    'party': 'Party', 
                    'argId': 'Argument ID', 
                    'argTitle': 'Argument Title',
                    'exhibits': 'Exhibits'
                }
            ),
            use_container_width=True
        )
        
        # Add download link
        st.markdown(get_csv_download_link(facts_df_display, "all_facts.csv", "Download All Facts CSV"), unsafe_allow_html=True)
    
    with facts_tabs[1]:  # Disputed Facts
        # Filter for disputed facts
        disputed_df = facts_df[facts_df['isDisputed'] == True].copy()
        disputed_df['exhibits'] = disputed_df['exhibits'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
        disputed_df['Status'] = 'Disputed'
        
        # Display the table
        st.dataframe(
            disputed_df[['date', 'point', 'party', 'Status', 'argId', 'argTitle', 'exhibits']].rename(
                columns={
                    'date': 'Date', 
                    'point': 'Event', 
                    'party': 'Party', 
                    'argId': 'Argument ID', 
                    'argTitle': 'Argument Title',
                    'exhibits': 'Exhibits'
                }
            ),
            use_container_width=True
        )
        
        # Add download link
        st.markdown(get_csv_download_link(disputed_df, "disputed_facts.csv", "Download Disputed Facts CSV"), unsafe_allow_html=True)
    
    with facts_tabs[2]:  # Undisputed Facts
        # Filter for undisputed facts
        undisputed_df = facts_df[facts_df['isDisputed'] == False].copy()
        undisputed_df['exhibits'] = undisputed_df['exhibits'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
        undisputed_df['Status'] = 'Undisputed'
        
        # Display the table
        st.dataframe(
            undisputed_df[['date', 'point', 'party', 'Status', 'argId', 'argTitle', 'exhibits']].rename(
                columns={
                    'date': 'Date', 
                    'point': 'Event', 
                    'party': 'Party', 
                    'argId': 'Argument ID', 
                    'argTitle': 'Argument Title',
                    'exhibits': 'Exhibits'
                }
            ),
            use_container_width=True
        )
        
        # Add download link
        st.markdown(get_csv_download_link(undisputed_df, "undisputed_facts.csv", "Download Undisputed Facts CSV"), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
