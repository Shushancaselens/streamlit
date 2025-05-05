import streamlit as st
import pandas as pd
import base64

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = "Facts"

# Function to get all facts from the data
def get_all_facts():
    # This is a simplified version with sample facts
    facts = [
        {
            'point': 'Continuous operation under same name since 1950',
            'date': '1950-present',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '18-19',
            'exhibits': ['C-1'],
            'argId': '1',
            'argTitle': 'Sporting Succession'
        },
        {
            'point': 'Operations ceased between 1975-1976',
            'date': '1975-1976',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '206-207',
            'exhibits': ['R-1'],
            'argId': '1',
            'argTitle': 'Sporting Succession Rebuttal'
        },
        {
            'point': 'Initial registration in 1950',
            'date': '1950',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '25-26',
            'exhibits': ['C-2'],
            'argId': '1.1.1',
            'argTitle': 'Registration History'
        },
        {
            'point': 'Brief administrative gap in 1975-1976',
            'date': '1975-1976',
            'isDisputed': True,
            'party': 'Appellant',
            'paragraphs': '29-30',
            'exhibits': ['C-2'],
            'argId': '1.1.1',
            'argTitle': 'Registration History'
        },
        {
            'point': 'Consistent use of blue and white since founding',
            'date': '1950-present',
            'isDisputed': True,
            'party': 'Appellant',
            'paragraphs': '51-52',
            'exhibits': ['C-4'],
            'argId': '1.2',
            'argTitle': 'Club Colors Analysis'
        },
        {
            'point': 'Significant color scheme change in 1976',
            'date': '1976',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '245-246',
            'exhibits': ['R-4'],
            'argId': '1.2',
            'argTitle': 'Club Colors Analysis Rebuttal'
        }
    ]
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
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            padding-left: 20px;
            padding-right: 20px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #4D68F9;
            color: white;
        }
        tr:hover td {
            background-color: #f8f9fa;
        }
        th {
            cursor: pointer;
        }
        th:hover {
            background-color: #e9ecef;
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
    
    # Facts Section
    if st.session_state.view == "Facts":
        st.title("Case Facts")
        
        # Get facts data
        facts_data = get_all_facts()
        
        # Create tabs for facts view
        tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
        
        with tab1:  # All Facts
            # Action buttons
            col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
            with col2:
                st.markdown("### ")  # Empty space for alignment
                if st.button("Copy", use_container_width=True):
                    st.info("Copy functionality would be implemented here")
            with col3:
                st.markdown("### ")  # Empty space for alignment
                if st.button("Export", use_container_width=True):
                    # Create DataFrame for export
                    df = pd.DataFrame(facts_data)
                    # Display download link
                    st.markdown(get_csv_download_link(df, "all_facts.csv", "Download CSV"), unsafe_allow_html=True)
            
            # Display all facts in a table
            df_all = pd.DataFrame(facts_data)
            st.dataframe(df_all, use_container_width=True)
        
        with tab2:  # Disputed Facts
            disputed_facts = [fact for fact in facts_data if fact['isDisputed']]
            df_disputed = pd.DataFrame(disputed_facts)
            st.dataframe(df_disputed, use_container_width=True)
        
        with tab3:  # Undisputed Facts
            undisputed_facts = [fact for fact in facts_data if not fact['isDisputed']]
            df_undisputed = pd.DataFrame(undisputed_facts)
            st.dataframe(df_undisputed, use_container_width=True)
    
    elif st.session_state.view == "Arguments":
        st.title("Arguments")
        st.markdown("Arguments functionality would be implemented here")
    
    elif st.session_state.view == "Exhibits":
        st.title("Exhibits")
        st.markdown("Exhibits functionality would be implemented here")

if __name__ == "__main__":
    main()
