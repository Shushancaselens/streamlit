import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Case Document Timeline", layout="wide")

# Custom CSS to match the screenshot styling
st.markdown("""
<style>
    /* Main UI styling */
    .main .block-container {
        padding-top: 1rem;
    }
    
    /* Badge styling */
    .badge-appellant {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
    }
    .badge-respondent {
        background-color: #fee2e2;
        color: #b91c1c;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
    }
    .badge-disputed {
        background-color: #fef3c7;
        color: #92400e;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
    }
    .badge-undisputed {
        background-color: #d1fae5;
        color: #065f46;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
    }
    .badge-evidence {
        background-color: #f3f4f6;
        color: #4b5563;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
    }
    .badge-document {
        background-color: #e0e7ff;
        color: #4338ca;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        margin-left: 5px;
    }
    
    /* Hide default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Document folders data
document_folders = [
    {"id": "1", "name": "1. Statement of Appeal", "party": "Appellant"},
    {"id": "2", "name": "2. Request for a Stay", "party": "Respondent"},
    {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent"},
    {"id": "4", "name": "4. Answer to PM", "party": "Respondent"},
    {"id": "5", "name": "5. Appeal Brief", "party": "Appellant"},
    {"id": "6", "name": "6. Brief on Admissibility", "party": "Court"},
    {"id": "7", "name": "7. Reply to Objection to Admissibility", "party": "Appellant"},
    {"id": "8", "name": "8. Challenge", "party": "Respondent"},
    {"id": "9", "name": "ChatGPT", "party": "Other"},
    {"id": "10", "name": "Jurisprudence", "party": "Other"},
    {"id": "11", "name": "Objection to Admissibility", "party": "Respondent"},
    {"id": "12", "name": "Swiss Court", "party": "Court"}
]

# Timeline events data
timeline_events = [
    {"date": "1950-present", "event": "Continuous operation under same name since 1950", "party": "Appellant", "status": "Undisputed", "related_argument": "1. Sporting Succession", "evidence": "C-1", "related_folder": "1"},
    {"date": "1950", "event": "Initial registration in 1950", "party": "Appellant", "status": "Undisputed", "related_argument": "1.1.1. Registration History", "evidence": "C-2", "related_folder": "1"},
    {"date": "1950-present", "event": "Consistent use of blue and white since founding", "party": "Appellant", "status": "Disputed", "related_argument": "1.2. Club Colors Analysis", "evidence": "C-4", "related_folder": "5"},
    {"date": "1950-1975", "event": "Pre-1976 colors represented original city district", "party": "Respondent", "status": "Undisputed", "related_argument": "1.2.1. Color Changes Analysis", "evidence": "R-5", "related_folder": "4"},
    {"date": "1970-1980", "event": "Minor shade variations do not affect continuity", "party": "Appellant", "status": "Undisputed", "related_argument": "1.2.1. Color Variations Analysis", "evidence": "C-5", "related_folder": "5"},
    {"date": "1975-1976", "event": "Brief administrative gap in 1975-1976", "party": "Appellant", "status": "Disputed", "related_argument": "1.1.1. Registration History", "evidence": "C-2", "related_folder": "1"},
    {"date": "1975-1976", "event": "Operations ceased between 1975-1976", "party": "Respondent", "status": "Disputed", "related_argument": "1. Sporting Succession Rebuttal", "evidence": "R-1", "related_folder": "3"},
    {"date": "April 30, 1975", "event": "Registration formally terminated on April 30, 1975", "party": "Respondent", "status": "Undisputed", "related_argument": "1.1.1. Registration Gap", "evidence": "R-2", "related_folder": "4"}
]

# Convert to DataFrame for easier manipulation
events_df = pd.DataFrame(timeline_events)

# Create sidebar with document folders
with st.sidebar:
    # Add logo/title
    st.markdown('<h2 style="color:#3b82f6;">CaseLens</h2>', unsafe_allow_html=True)
    st.markdown("<h3>Legal Analysis</h3>", unsafe_allow_html=True)
    
    # Add sidebar navigation
    st.markdown("---")
    st.markdown("<h4>Documents</h4>", unsafe_allow_html=True)
    
    # Create session state for tracking selected folders
    if 'selected_folder' not in st.session_state:
        st.session_state.selected_folder = "1"  # Default to first folder
    
    # Display document folders
    for folder in document_folders:
        folder_id = folder["id"]
        folder_name = folder["name"]
        
        # Create styled containers for each folder
        # Color the border based on party
        if folder["party"] == "Appellant":
            border_style = "border-left: 4px solid #3b82f6;"
        elif folder["party"] == "Respondent":
            border_style = "border-left: 4px solid #ef4444;"
        else:
            border_style = "border-left: 4px solid #9ca3af;"
        
        # Highlight the selected folder
        bg_color = "#f0f9ff;" if folder_id == st.session_state.selected_folder else "white;"
        
        # Create a container for each folder
        folder_container = st.container()
        
        # Apply styling to the container
        folder_container.markdown(
            f'<div style="padding: 8px; margin-bottom: 4px; border-radius: 4px; {border_style} background-color: {bg_color}">{folder_name}</div>',
            unsafe_allow_html=True
        )
        
        # Make the folder clickable with a button
        if folder_container.button(f"Select", key=f"btn_{folder_id}", use_container_width=True, help=f"View {folder_name}"):
            st.session_state.selected_folder = folder_id
            st.rerun()

# Main content area
st.title("Summary of arguments")
st.header("Case Facts")

# Create tabs for filtering facts
tab1, tab2, tab3 = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])

with tab1:
    # Display all facts using native Streamlit components
    # Filter based on selected folder if needed
    filtered_df = events_df.copy()
    
    # Add a new column for highlighting rows related to selected folder
    filtered_df['highlight'] = filtered_df['related_folder'] == st.session_state.selected_folder
    
    # Create a DataFrame with formatted columns for display
    display_df = pd.DataFrame()
    display_df['Date'] = filtered_df['date']
    display_df['Event'] = filtered_df['event']
    
    # Format Party column with badges
    def format_party(row):
        party = row['party']
        if party == 'Appellant':
            return '<span class="badge-appellant">Appellant</span>'
        else:
            return '<span class="badge-respondent">Respondent</span>'
    
    # Format Status column with badges  
    def format_status(row):
        status = row['status']
        if status == 'Disputed':
            return '<span class="badge-disputed">Disputed</span>'
        else:
            return '<span class="badge-undisputed">Undisputed</span>'
    
    # Format Evidence column with badges
    def format_evidence(row):
        evidence = row['evidence']
        folder = row['related_folder']
        return f'<span class="badge-evidence">Evidence: {evidence}</span> <span class="badge-document">Document {folder}</span>'
    
    # Apply formatting
    filtered_df['Party_Formatted'] = filtered_df.apply(format_party, axis=1)
    filtered_df['Status_Formatted'] = filtered_df.apply(format_status, axis=1)
    filtered_df['Evidence_Formatted'] = filtered_df.apply(format_evidence, axis=1)
    
    # Display the formatted table
    st.markdown("### All Facts", unsafe_allow_html=True)
    
    # Use AgGrid or similar for advanced table formatting
    # For now, we'll use simpler Streamlit methods
    
    # Display each row as a card instead of using HTML table
    for idx, row in filtered_df.iterrows():
        background = "#f0f9ff" if row['highlight'] else "white"
        
        st.markdown(
            f"""
            <div style="padding: 12px; margin-bottom: 10px; border-radius: 4px; background-color: {background}; border-left: 4px solid {'#d97706' if row['status'] == 'Disputed' else '#10b981'};">
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <div style="font-weight: 500; margin-bottom: 6px;">{row['event']}</div>
                        <div>{row['date']}</div>
                    </div>
                    <div style="text-align: right;">
                        <div>{row['Party_Formatted']}</div>
                        <div style="margin-top: 5px;">{row['Status_Formatted']}</div>
                    </div>
                </div>
                <div style="margin-top: 8px;">
                    <div><strong>{row['related_argument']}</strong></div>
                    <div>{row['Evidence_Formatted']}</div>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

with tab2:
    # Filter for disputed facts
    disputed_df = events_df[events_df['status'] == 'Disputed'].copy()
    disputed_df['highlight'] = disputed_df['related_folder'] == st.session_state.selected_folder
    
    st.markdown("### Disputed Facts", unsafe_allow_html=True)
    
    # Display disputed facts
    for idx, row in disputed_df.iterrows():
        background = "#f0f9ff" if row['highlight'] else "white"
        
        st.markdown(
            f"""
            <div style="padding: 12px; margin-bottom: 10px; border-radius: 4px; background-color: {background}; border-left: 4px solid #d97706;">
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <div style="font-weight: 500; margin-bottom: 6px;">{row['event']}</div>
                        <div>{row['date']}</div>
                    </div>
                    <div style="text-align: right;">
                        <div>{'<span class="badge-appellant">Appellant</span>' if row['party'] == 'Appellant' else '<span class="badge-respondent">Respondent</span>'}</div>
                        <div style="margin-top: 5px;"><span class="badge-disputed">Disputed</span></div>
                    </div>
                </div>
                <div style="margin-top: 8px;">
                    <div><strong>{row['related_argument']}</strong></div>
                    <div><span class="badge-evidence">Evidence: {row['evidence']}</span> <span class="badge-document">Document {row['related_folder']}</span></div>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

with tab3:
    # Filter for undisputed facts
    undisputed_df = events_df[events_df['status'] == 'Undisputed'].copy()
    undisputed_df['highlight'] = undisputed_df['related_folder'] == st.session_state.selected_folder
    
    st.markdown("### Undisputed Facts", unsafe_allow_html=True)
    
    # Display undisputed facts
    for idx, row in undisputed_df.iterrows():
        background = "#f0f9ff" if row['highlight'] else "white"
        
        st.markdown(
            f"""
            <div style="padding: 12px; margin-bottom: 10px; border-radius: 4px; background-color: {background}; border-left: 4px solid #10b981;">
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <div style="font-weight: 500; margin-bottom: 6px;">{row['event']}</div>
                        <div>{row['date']}</div>
                    </div>
                    <div style="text-align: right;">
                        <div>{'<span class="badge-appellant">Appellant</span>' if row['party'] == 'Appellant' else '<span class="badge-respondent">Respondent</span>'}</div>
                        <div style="margin-top: 5px;"><span class="badge-undisputed">Undisputed</span></div>
                    </div>
                </div>
                <div style="margin-top: 8px;">
                    <div><strong>{row['related_argument']}</strong></div>
                    <div><span class="badge-evidence">Evidence: {row['evidence']}</span> <span class="badge-document">Document {row['related_folder']}</span></div>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

# Add buttons for copy and export
col1, col2 = st.columns([1, 10])
with col1:
    st.button("Copy")
with col2:
    st.button("Export")

# Document-Event connection visualization
st.markdown("## Document-Event Connections", unsafe_allow_html=True)

# Get selected folder
selected_folder = st.session_state.selected_folder
selected_folder_name = next((f['name'] for f in document_folders if f['id'] == selected_folder), "Unknown")
related_events = events_df[events_df['related_folder'] == selected_folder]

# Display selected folder details
st.markdown(f"### Selected Document: {selected_folder_name}", unsafe_allow_html=True)

# Create two columns for selected document details
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Document Details", unsafe_allow_html=True)
    folder_party = next((f['party'] for f in document_folders if f['id'] == selected_folder), "Unknown")
    
    # Color based on party
    color = "#3b82f6" if folder_party == "Appellant" else "#ef4444" if folder_party == "Respondent" else "#6b7280"
    
    st.markdown(
        f"""
        <div style="padding: 15px; border-radius: 6px; border-left: 4px solid {color}; background-color: #f8f9fa;">
            <div style="font-weight: 500; margin-bottom: 10px;">{selected_folder_name}</div>
            <div style="color: #6b7280;">
                <div>Party: {folder_party}</div>
                <div>Connected Events: {len(related_events)}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown("#### Connected Timeline Events", unsafe_allow_html=True)
    
    if len(related_events) > 0:
        for _, event in related_events.iterrows():
            status_class = "badge-disputed" if event['status'] == "Disputed" else "badge-undisputed"
            party_class = "badge-appellant" if event['party'] == "Appellant" else "badge-respondent"
            
            st.markdown(
                f"""
                <div style="padding: 10px; margin-bottom: 8px; border-radius: 4px; background-color: #f8f9fa; border-left: 3px solid {color};">
                    <div style="font-weight: 500;">{event['event']}</div>
                    <div style="display: flex; margin-top: 8px; justify-content: space-between;">
                        <div>
                            <span class="{status_class}">{event['status']}</span>
                            <span class="{party_class}" style="margin-left: 5px;">{event['party']}</span>
                        </div>
                        <div>{event['date']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("No timeline events are connected to this document.")

# Function to run the app
if __name__ == "__main__":
    # This is already running in the Streamlit app
    pass
