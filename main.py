import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64
from datetime import datetime

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Facts"

# Function to get comprehensive facts data with chronology
def get_all_facts():
    facts = [
        {
            'date': '1950-01-12',
            'point': 'Club officially registered under current name',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '18-19',
            'exhibits': ['C-1'],
            'argId': '1',
            'argTitle': 'Sporting Succession',
            'sources': 3,
            'proceedings': 'registration',
            'addressedBy': 'Both Parties',
            'supportingDocs': [
                {
                    'id': 'C-1',
                    'title': 'Original Registration Certificate',
                    'summary': 'Official registration document dated January 12, 1950, establishing the football club under its current name. The certificate was issued by the Municipal Sports Authority and includes founding member signatures, initial bylaws, and the club\'s stated objectives of promoting football in the local community.',
                    'source': 'Municipal Registry Office, Document Archive Section',
                    'pageRef': 'Page 15: Certificate No. 1950-FB-012, Municipal Sports Authority Registration'
                }
            ]
        },
        {
            'date': '1950-03-15',
            'point': 'First official match played under club colors',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '51-52',
            'exhibits': ['C-4', 'C-6'],
            'argId': '1.2',
            'argTitle': 'Club Colors Analysis',
            'sources': 2,
            'proceedings': 'evidence',
            'addressedBy': 'Appellant',
            'supportingDocs': [
                {
                    'id': 'C-4',
                    'title': 'Historical Match Records',
                    'summary': 'Official match report from March 15, 1950, documenting the club\'s first competitive fixture. The report includes team lineup, final score (2-1 victory), and notably describes the team uniform as "traditional blue and white striped jerseys with blue shorts." Local newspaper coverage from the same date corroborates the uniform description.',
                    'source': 'Regional Football Association Archives',
                    'pageRef': 'Page 23: Match Report RFA-1950-003, Regional Football Association'
                },
                {
                    'id': 'C-6',
                    'title': 'Newspaper Coverage',
                    'summary': 'Contemporary newspaper article from the Local Daily Sports section, March 16, 1950, featuring a photograph of the team in their debut match. The black and white photograph clearly shows the striped pattern of the jerseys, and the accompanying article specifically mentions the club\'s choice of blue and white as representing the city\'s traditional colors.',
                    'source': 'Local Daily Sports Archive',
                    'pageRef': 'Page 12: Sports Section, Local Daily, March 16, 1950 Edition'
                }
            ]
        },
        {
            'date': '1975-04-30',
            'point': 'Registration formally terminated',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '206-207',
            'exhibits': ['R-1', 'R-2'],
            'argId': '1',
            'argTitle': 'Sporting Succession Rebuttal',
            'sources': 4,
            'proceedings': 'challenge',
            'addressedBy': 'Respondent Only',
            'supportingDocs': [
                {
                    'id': 'R-1',
                    'title': 'Official Termination Certificate',
                    'summary': 'Government-issued certificate of termination dated April 30, 1975, formally dissolving the original club entity. The document cites "financial insolvency and failure to meet regulatory requirements" as grounds for termination. Signed by the Regional Sports Commissioner and notarized by the Municipal Clerk.',
                    'source': 'Regional Sports Authority',
                    'pageRef': 'Page 45: Termination Certificate RSA-1975-089, Regional Sports Authority'
                },
                {
                    'id': 'R-2',
                    'title': 'Bankruptcy Proceedings',
                    'summary': 'Court documents from bankruptcy proceedings initiated against the club in early 1975. The filing shows debts totaling €127,000 to various creditors including players, suppliers, and the municipal stadium authority. The bankruptcy trustee\'s report details the liquidation of all club assets.',
                    'source': 'Municipal Court Records',
                    'pageRef': 'Page 67-89: Case No. MC-1975-234, Municipal Commercial Court'
                }
            ]
        },
        {
            'date': '1975-05-15',
            'point': 'Club ceased all competitive activities',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '208-209',
            'exhibits': ['R-3'],
            'argId': '1',
            'argTitle': 'Operational Continuity',
            'sources': 2,
            'proceedings': 'evidence',
            'addressedBy': 'Not Addressed',
            'supportingDocs': [
                {
                    'id': 'R-3',
                    'title': 'League Withdrawal Notice',
                    'summary': 'Official notification to the National Football League dated May 15, 1975, announcing the club\'s immediate withdrawal from all competitions for the remainder of the 1975 season and indefinitely thereafter. The letter cites "insurmountable financial difficulties" and was signed by the then-club president.',
                    'source': 'National Football League Archives',
                    'pageRef': 'Page 156: Correspondence File NFL-1975-WD-47, National Football League'
                }
            ]
        },
        {
            'date': '1976-09-15',
            'point': 'New entity registered with same name',
            'isDisputed': True,
            'party': 'Both',
            'paragraphs': '228-229',
            'exhibits': ['R-4', 'C-7'],
            'argId': '1.1.1',
            'argTitle': 'Registration Gap Evidence',
            'sources': 5,
            'proceedings': 'challenge',
            'addressedBy': 'Both Parties',
            'supportingDocs': [
                {
                    'id': 'R-4',
                    'title': 'New Registration Documents',
                    'summary': 'Registration papers for a new football club entity dated September 15, 1976, using the same name as the terminated club. The founding members listed are entirely different from the original 1950 registration, and the registered address is in a different district of the city. The stated objectives include "continuing the football tradition of the local community."',
                    'source': 'Municipal Registry Office',
                    'pageRef': 'Page 203: Certificate No. 1976-FB-156, Municipal Sports Authority Registration'
                },
                {
                    'id': 'C-7',
                    'title': 'Continuity Declaration',
                    'summary': 'Statutory declaration signed by three founding members of the 1976 entity, asserting their intention to continue the legacy and traditions of the original club. The document references the club\'s historical achievements and states the founders\' commitment to maintaining the same colors, name, and community connection.',
                    'source': 'Notary Public Records',
                    'pageRef': 'Page 78: Statutory Declaration SD-1976-445, Municipal Notary Office'
                }
            ]
        },
        {
            'date': '1976-10-22',
            'point': 'First match under new entity with modified colors',
            'isDisputed': True,
            'party': 'Respondent',
            'paragraphs': '245-246',
            'exhibits': ['R-5'],
            'argId': '1.2',
            'argTitle': 'Club Colors Analysis Rebuttal',
            'sources': 3,
            'proceedings': 'evidence',
            'addressedBy': 'Respondent Only',
            'supportingDocs': [
                {
                    'id': 'R-5',
                    'title': 'Match Report and Photographs',
                    'summary': 'Comprehensive match report from October 22, 1976, documenting the new entity\'s first competitive fixture. Color photographs clearly show jerseys in a darker shade of blue with white trim, distinctly different from the original light blue and white stripes. The match program notes this as a "new beginning" for the club.',
                    'source': 'Regional Football Association',
                    'pageRef': 'Page 34-36: Match Report RFA-1976-087, with Official Photography'
                }
            ]
        },
        {
            'date': '1982-01-10',
            'point': 'Temporary addition of third color (red trim)',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '58-59',
            'exhibits': ['C-5'],
            'argId': '1.2.1',
            'argTitle': 'Color Variations Analysis',
            'sources': 1,
            'proceedings': 'registration',
            'addressedBy': 'Appellant',
            'supportingDocs': [
                {
                    'id': 'C-5',
                    'title': 'Board Meeting Minutes',
                    'summary': 'Minutes from the club\'s board meeting on January 10, 1982, documenting the decision to add red trim to jerseys for the 1982-1988 period. The decision was made to commemorate the club\'s partnership with a local sponsor and was explicitly described as "temporary" with plans to revert to traditional colors.',
                    'source': 'Club Archive Records',
                    'pageRef': 'Page 91: Board Minutes BM-1982-002, Club Secretary Archives'
                }
            ]
        },
        {
            'date': '1988-06-30',
            'point': 'Return to traditional blue and white colors',
            'isDisputed': False,
            'party': 'Appellant',
            'paragraphs': '60-61',
            'exhibits': ['C-8'],
            'argId': '1.2.1',
            'argTitle': 'Color Restoration',
            'sources': 2,
            'proceedings': 'evidence',
            'addressedBy': 'Both Parties',
            'supportingDocs': [
                {
                    'id': 'C-8',
                    'title': 'Jersey Design Specifications',
                    'summary': 'Official design specifications dated June 30, 1988, showing the return to blue and white striped jerseys without red trim. The document includes color swatches and explicitly states the intention to "restore the club\'s traditional appearance as worn since 1950." Manufacturer invoices confirm the production of jerseys matching these specifications.',
                    'source': 'Kit Manufacturer Records',
                    'pageRef': 'Page 145: Design Spec DS-1988-034, Sports Kit Manufacturing Ltd.'
                }
            ]
        }
    ]
    
    return facts

# Main app
def main():
    # Get the facts data
    facts_data = get_all_facts()
    
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
        </style>
        """, unsafe_allow_html=True)
        
        # Define button click handlers
        def set_arguments_view():
            st.session_state.view = "Arguments"
            
        def set_facts_view():
            st.session_state.view = "Facts"
            
        def set_exhibits_view():
            st.session_state.view = "Exhibits"
        
        # Create buttons with names (keep all buttons but only Facts will work)
        st.button("📑 Arguments", key="args_button", on_click=set_arguments_view, use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_facts_view, use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_exhibits_view, use_container_width=True)
    
    # Custom CSS for badges and styling
    st.markdown("""
    <style>
    .badge {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 500;
        margin-right: 8px;
    }
    
    .appellant-badge {
        background-color: rgba(49, 130, 206, 0.1);
        color: #3182ce;
    }
    
    .respondent-badge {
        background-color: rgba(229, 62, 62, 0.1);
        color: #e53e3e;
    }
    
    .both-badge {
        background-color: rgba(128, 90, 213, 0.1);
        color: #805ad5;
    }
    
    .disputed-badge {
        background-color: rgba(229, 62, 62, 0.1);
        color: #e53e3e;
    }
    
    .undisputed-badge {
        background-color: rgba(72, 187, 120, 0.1);
        color: #38a169;
    }
    
    .sources-count {
        background: #3182ce;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: 500;
        font-size: 12px;
    }
    
    .proceedings-tab {
        padding: 6px 12px;
        border-radius: 4px;
        font-size: 12px;
        text-transform: capitalize;
        margin-left: 8px;
    }
    
    .proceedings-registration {
        background: #e6fffa;
        color: #00695c;
    }
    
    .proceedings-challenge {
        background: #fff5f5;
        color: #c53030;
    }
    
    .proceedings-evidence {
        background: #f0f4ff;
        color: #3182ce;
    }
    
    .document-source {
        background-color: #f8f9fa;
        padding: 12px;
        border-radius: 6px;
        margin-top: 12px;
        border-left: 4px solid #28a745;
    }
    
    .source-label {
        font-weight: 600;
        color: #2d5016;
        margin-bottom: 4px;
    }
    
    .page-ref {
        font-style: italic;
        color: #5a5a5a;
        margin-top: 4px;
        font-size: 12px;
    }
    
    .metadata-row {
        display: flex;
        gap: 20px;
        margin-bottom: 16px;
        align-items: center;
        flex-wrap: wrap;
    }
    
    .addressed-status {
        font-size: 12px;
        color: #666;
        margin-left: 8px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main content
    st.title("Case Chronology")
    
    # Sort facts by date
    facts_sorted = sorted(facts_data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
    
    # Display each fact as a static card
    for fact in facts_sorted:
        # Format date
        date_obj = datetime.strptime(fact['date'], '%Y-%m-%d')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        
        # Create card container
        with st.container():
            st.markdown("---")
            
            # Card header with date and event
            st.markdown(f"## {formatted_date}")
            st.markdown(f"**{fact['point']}**")
            
            # Metadata row
            col1, col2, col3 = st.columns([2, 3, 3])
            
            with col1:
                st.markdown(f'<span class="sources-count">{fact["sources"]}</span> Sources', unsafe_allow_html=True)
            
            with col2:
                proceedings_class = f"proceedings-{fact['proceedings']}"
                st.markdown(f'**PROCEEDINGS:** <span class="proceedings-tab {proceedings_class}">{fact["proceedings"]}</span>', unsafe_allow_html=True)
            
            with col3:
                st.markdown(f'**ADDRESSED BY:** <span class="addressed-status">{fact["addressedBy"]}</span>', unsafe_allow_html=True)
            
            # Party and status badges
            st.markdown("")  # Add some space
            
            # Party badge
            if fact['party'] == 'Both':
                party_badge = '<span class="badge both-badge">Both Parties</span>'
            elif fact['party'] == 'Appellant':
                party_badge = '<span class="badge appellant-badge">Appellant</span>'
            else:
                party_badge = '<span class="badge respondent-badge">Respondent</span>'
            
            # Status badge
            status_badge = '<span class="badge disputed-badge">Disputed</span>' if fact['isDisputed'] else '<span class="badge undisputed-badge">Undisputed</span>'
            
            st.markdown(f'{party_badge} {status_badge}', unsafe_allow_html=True)
            
            # Supporting Documents section
            st.markdown("### Supporting Documents")
            
            for doc in fact['supportingDocs']:
                with st.container():
                    st.markdown(f"**{doc['id']} - {doc['title']}**")
                    st.markdown(f"**Summary:** {doc['summary']}")
                    
                    # Source information
                    st.markdown(f"""
                    <div class="document-source">
                        <div class="source-label">Source</div>
                        <div>{doc['source']}</div>
                        <div class="page-ref">{doc['pageRef']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Action buttons
                    col1, col2, col3, col4 = st.columns([2, 2, 2, 6])
                    
                    with col1:
                        if st.button("📄 View Document", key=f"view_{doc['id']}"):
                            st.info(f"Opening document: {doc['id']}")
                    
                    with col2:
                        if st.button("📥 Download PDF", key=f"pdf_{doc['id']}"):
                            st.info(f"Downloading PDF for: {doc['id']}")
                    
                    with col3:
                        if st.button("📋 Copy Source", key=f"copy_{doc['id']}"):
                            st.info("Source copied to clipboard!")
                    
                    st.markdown("")  # Space between documents

if __name__ == "__main__":
    main()
