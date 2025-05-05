import streamlit as st
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Function to create CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Get all facts from the data
def get_all_facts():
    return [
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
            'point': "Consistent use of blue and white since founding",
            'date': "1950-present",
            'isDisputed': True,
            'party': "Appellant",
            'paragraphs': "51-52",
            'exhibits': ["C-4"],
            'argId': "1.2",
            'argTitle': "Club Colors Analysis"
        },
        {
            'point': "Minor shade variations do not affect continuity",
            'date': "1970-1980",
            'isDisputed': False,
            'party': "Appellant",
            'paragraphs': "56-57",
            'exhibits': ["C-5"],
            'argId': "1.2.1",
            'argTitle': "Color Variations Analysis"
        },
        {
            'point': "Temporary third color addition in 1980s",
            'date': "1982-1988",
            'isDisputed': False,
            'party': "Appellant",
            'paragraphs': "58-59",
            'exhibits': ["C-5"],
            'argId': "1.2.1",
            'argTitle': "Color Variations Analysis"
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
        },
        {
            'point': "Significant color scheme change in 1976",
            'date': "1976",
            'isDisputed': True,
            'party': "Respondent",
            'paragraphs': "245-246",
            'exhibits': ["R-4"],
            'argId': "1.2",
            'argTitle': "Club Colors Analysis Rebuttal"
        },
        {
            'point': "Pre-1976 colors represented original city district",
            'date': "1950-1975",
            'isDisputed': False,
            'party': "Respondent",
            'paragraphs': "247",
            'exhibits': ["R-5"],
            'argId': "1.2.1",
            'argTitle': "Color Changes Analysis"
        },
        {
            'point': "Post-1976 colors represented new ownership region",
            'date': "1976-present",
            'isDisputed': True,
            'party': "Respondent",
            'paragraphs': "248-249",
            'exhibits': ["R-5"],
            'argId': "1.2.1",
            'argTitle': "Color Changes Analysis"
        }
    ]

# Function to create the sidebar
def create_sidebar():
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
        
        # Initialize session state if not already done
        if 'view' not in st.session_state:
            st.session_state.view = "Arguments"
        
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

# Function to create the facts page
def create_facts_page():
    st.title("Case Facts")
    
    # Create tabs for different fact views
    fact_tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
    
    # Get all facts
    all_facts = get_all_facts()
    
    # Create dataframes for each tab
    all_facts_df = pd.DataFrame(all_facts)
    disputed_facts_df = pd.DataFrame([fact for fact in all_facts if fact['isDisputed']])
    undisputed_facts_df = pd.DataFrame([fact for fact in all_facts if not fact['isDisputed']])
    
    # Format facts for display
    def format_facts_df(df):
        # Create a copy to avoid modifying the original
        formatted_df = df.copy()
        
        # Format the exhibits column
        formatted_df['exhibits'] = formatted_df['exhibits'].apply(lambda x: ', '.join(x) if x else 'None')
        
        # Rename columns for display
        formatted_df = formatted_df.rename(columns={
            'point': 'Event',
            'date': 'Date',
            'party': 'Party',
            'paragraphs': 'Paragraphs',
            'exhibits': 'Exhibits',
            'argId': 'Argument ID',
            'argTitle': 'Argument Title'
        })
        
        # Add a status column
        formatted_df['Status'] = formatted_df.apply(lambda row: 'Disputed' if row['isDisputed'] else 'Undisputed', axis=1)
        
        # Select and order columns for display
        return formatted_df[['Date', 'Event', 'Party', 'Status', 'Argument ID', 'Argument Title', 'Paragraphs', 'Exhibits']]
    
    # Display dataframes in tabs
    with fact_tabs[0]:
        st.dataframe(format_facts_df(all_facts_df), use_container_width=True)
        st.markdown(get_csv_download_link(format_facts_df(all_facts_df), "all_facts.csv", "Download All Facts"), unsafe_allow_html=True)
    
    with fact_tabs[1]:
        st.dataframe(format_facts_df(disputed_facts_df), use_container_width=True)
        st.markdown(get_csv_download_link(format_facts_df(disputed_facts_df), "disputed_facts.csv", "Download Disputed Facts"), unsafe_allow_html=True)
    
    with fact_tabs[2]:
        st.dataframe(format_facts_df(undisputed_facts_df), use_container_width=True)
        st.markdown(get_csv_download_link(format_facts_df(undisputed_facts_df), "undisputed_facts.csv", "Download Undisputed Facts"), unsafe_allow_html=True)
    
    # Add additional analysis section
    st.header("Facts Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Count facts by party
        party_counts = all_facts_df['party'].value_counts()
        st.subheader("Facts by Party")
        st.bar_chart(party_counts)
    
    with col2:
        # Count disputed vs undisputed
        dispute_counts = all_facts_df['isDisputed'].value_counts().rename(index={True: 'Disputed', False: 'Undisputed'})
        st.subheader("Disputed vs Undisputed Facts")
        st.bar_chart(dispute_counts)

# Main function
def main():
    # Create the sidebar
    create_sidebar()
    
    # Check which view to show
    if st.session_state.view == "Facts":
        create_facts_page()
    elif st.session_state.view == "Arguments":
        st.title("Arguments Section")
        st.write("This is the Arguments Section. Select 'Facts' in the sidebar to view the Facts page.")
    else:  # Exhibits
        st.title("Exhibits Section")
        st.write("This is the Exhibits Section. Select 'Facts' in the sidebar to view the Facts page.")

if __name__ == "__main__":
    main()
