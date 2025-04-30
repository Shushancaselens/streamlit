import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Adversarial Case Timeline", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Badge styling */
    .badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        display: inline-block;
        margin-right: 5px;
    }
    .appellant {
        background-color: #dbeafe;
        color: #1e40af;
    }
    .respondent {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    .disputed {
        background-color: #fef3c7;
        color: #92400e;
    }
    .undisputed {
        background-color: #d1fae5;
        color: #065f46;
    }
    .evidence {
        background-color: #f3f4f6;
        color: #4b5563;
    }
    
    /* Card styling */
    .card {
        padding: 15px;
        border-radius: 6px;
        margin-bottom: 15px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .appellant-card {
        border-left: 4px solid #3b82f6;
        background-color: #f0f7ff;
    }
    .respondent-card {
        border-left: 4px solid #ef4444;
        background-color: #fff5f5;
    }
    
    /* Adversarial layout */
    .versus-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px 0;
    }
    .versus-circle {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: #6b7280;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
    }
    .versus-line {
        height: 2px;
        background-color: #6b7280;
        width: 100px;
    }
    
    /* Connection lines */
    .connection-line {
        border-left: 2px dashed #9ca3af;
        height: 20px;
        margin-left: 15px;
    }
    
    /* Hide default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Document folders data
document_folders = [
    {"id": "1", "name": "1. Statement of Appeal", "party": "Appellant", "date": "January 15, 2024"},
    {"id": "2", "name": "2. Request for a Stay", "party": "Respondent", "date": "February 1, 2024"},
    {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent", "date": "February 15, 2024"},
    {"id": "4", "name": "4. Answer to PM", "party": "Respondent", "date": "March 1, 2024"},
    {"id": "5", "name": "5. Appeal Brief", "party": "Appellant", "date": "March 15, 2024"},
    {"id": "6", "name": "6. Brief on Admissibility", "party": "Court", "date": "March 30, 2024"},
    {"id": "7", "name": "7. Reply to Objection to Admissibility", "party": "Appellant", "date": "April 15, 2024"},
    {"id": "8", "name": "8. Challenge", "party": "Respondent", "date": "April 30, 2024"}
]

# Timeline events data with more details about contradictions
timeline_events = [
    {
        "date": "1950-present", 
        "event": "Continuous operation under same name since 1950", 
        "party": "Appellant", 
        "status": "Undisputed", 
        "related_argument": "1. Sporting Succession", 
        "evidence": "C-1", 
        "related_folder": "1",
        "contradicted_by": None,
        "supports": "Continuity of club's identity"
    },
    {
        "date": "1950", 
        "event": "Initial registration in 1950", 
        "party": "Appellant", 
        "status": "Undisputed", 
        "related_argument": "1.1.1. Registration History", 
        "evidence": "C-2", 
        "related_folder": "1",
        "contradicted_by": None,
        "supports": "Historical foundation of club"
    },
    {
        "date": "1950-present", 
        "event": "Consistent use of blue and white since founding", 
        "party": "Appellant", 
        "status": "Disputed", 
        "related_argument": "1.2. Club Colors Analysis", 
        "evidence": "C-4", 
        "related_folder": "5",
        "contradicted_by": "1950-1975",
        "supports": "Visual identity continuity"
    },
    {
        "date": "1950-1975", 
        "event": "Pre-1976 colors represented original city district", 
        "party": "Respondent", 
        "status": "Undisputed", 
        "related_argument": "1.2.1. Color Changes Analysis", 
        "evidence": "R-5", 
        "related_folder": "4",
        "contradicted_by": "1950-present",
        "supports": "Colors tied to location, not identity"
    },
    {
        "date": "1970-1980", 
        "event": "Minor shade variations do not affect continuity", 
        "party": "Appellant", 
        "status": "Undisputed", 
        "related_argument": "1.2.1. Color Variations Analysis", 
        "evidence": "C-5", 
        "related_folder": "5",
        "contradicted_by": None,
        "supports": "Consistency despite variations"
    },
    {
        "date": "1975-1976", 
        "event": "Brief administrative gap in 1975-1976", 
        "party": "Appellant", 
        "status": "Disputed", 
        "related_argument": "1.1.1. Registration History", 
        "evidence": "C-2", 
        "related_folder": "1",
        "contradicted_by": "1975-1976-2",
        "supports": "Gap was merely administrative"
    },
    {
        "date": "1975-1976-2", 
        "event": "Operations ceased between 1975-1976", 
        "party": "Respondent", 
        "status": "Disputed", 
        "related_argument": "1. Sporting Succession Rebuttal", 
        "evidence": "R-1", 
        "related_folder": "2",  # Changed to folder 2 for Request for Stay
        "contradicted_by": "1975-1976",
        "supports": "Complete cessation of activities"
    },
    {
        "date": "April 30, 1975", 
        "event": "Registration formally terminated on April 30, 1975", 
        "party": "Respondent", 
        "status": "Undisputed", 
        "related_argument": "1.1.1. Registration Gap", 
        "evidence": "R-2", 
        "related_folder": "2",  # Changed to folder 2 for Request for Stay
        "contradicted_by": None,
        "supports": "Legal discontinuity"
    }
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
    if 'compare_mode' not in st.session_state:
        st.session_state.compare_mode = False
    
    if 'selected_folder' not in st.session_state:
        st.session_state.selected_folder = "1"  # Default to first folder
        
    if 'compared_folder' not in st.session_state:
        st.session_state.compared_folder = "2"  # Default comparison folder
    
    # Add a toggle for comparison mode
    st.session_state.compare_mode = st.checkbox("Compare Documents", value=st.session_state.compare_mode)
    
    # Display document folders
    for folder in document_folders:
        folder_id = folder["id"]
        folder_name = folder["name"]
        
        # Create styled containers for each folder
        # Color the border based on party
        if folder["party"] == "Appellant":
            border_style = "border-left: 4px solid #3b82f6;"
            folder_icon = "🔵"
        elif folder["party"] == "Respondent":
            border_style = "border-left: 4px solid #ef4444;"
            folder_icon = "🔴"
        else:
            border_style = "border-left: 4px solid #9ca3af;"
            folder_icon = "⚪"
        
        # Highlight selected and compared folders
        if st.session_state.compare_mode:
            if folder_id == st.session_state.selected_folder:
                bg_color = "#dbeafe;"  # Light blue for primary selection
            elif folder_id == st.session_state.compared_folder:
                bg_color = "#fee2e2;"  # Light red for comparison
            else:
                bg_color = "white;"
        else:
            bg_color = "#f0f9ff;" if folder_id == st.session_state.selected_folder else "white;"
        
        # Create the folder container
        col1, col2 = st.columns([8, 2])
        
        with col1:
            st.markdown(
                f'<div style="padding: 8px; margin-bottom: 4px; border-radius: 4px; {border_style} background-color: {bg_color}">{folder_icon} {folder_name}</div>',
                unsafe_allow_html=True
            )
        
        with col2:
            # If in compare mode, show radio buttons for selecting primary and comparison
            if st.session_state.compare_mode:
                if st.button("1️⃣", key=f"primary_{folder_id}", help=f"Set as primary document"):
                    st.session_state.selected_folder = folder_id
                    if st.session_state.compared_folder == folder_id:
                        # Find another folder for comparison (preferably of opposite party)
                        opposite_party = "Respondent" if folder["party"] == "Appellant" else "Appellant"
                        opposite_folders = [f["id"] for f in document_folders if f["party"] == opposite_party]
                        if opposite_folders:
                            st.session_state.compared_folder = opposite_folders[0]
                        else:
                            # If no opposite party folder, just pick the next one
                            st.session_state.compared_folder = next((f["id"] for f in document_folders if f["id"] != folder_id), "2")
                    st.rerun()
                
                if st.button("2️⃣", key=f"compare_{folder_id}", help=f"Set as comparison document"):
                    st.session_state.compared_folder = folder_id
                    if st.session_state.selected_folder == folder_id:
                        # Find another folder for primary (preferably of opposite party)
                        opposite_party = "Respondent" if folder["party"] == "Appellant" else "Appellant"
                        opposite_folders = [f["id"] for f in document_folders if f["party"] == opposite_party]
                        if opposite_folders:
                            st.session_state.selected_folder = opposite_folders[0]
                        else:
                            # If no opposite party folder, just pick another one
                            st.session_state.selected_folder = next((f["id"] for f in document_folders if f["id"] != folder_id), "1")
                    st.rerun()
            else:
                # Regular select button for single document view
                if st.button("📄", key=f"select_{folder_id}", help=f"Select document"):
                    st.session_state.selected_folder = folder_id
                    st.rerun()

# Main content area
st.title("Case Document Analysis")

# Get details for selected document(s)
selected_folder = st.session_state.selected_folder
selected_folder_info = next((f for f in document_folders if f["id"] == selected_folder), None)

if st.session_state.compare_mode:
    compared_folder = st.session_state.compared_folder
    compared_folder_info = next((f for f in document_folders if f["id"] == compared_folder), None)
    
    # Show adversarial comparison view
    st.header("Adversarial Document Comparison")
    
    # Use columns to create side-by-side comparison
    col1, col_middle, col2 = st.columns([5, 1, 5])
    
    with col1:
        # Style based on party
        border_color = "#3b82f6" if selected_folder_info["party"] == "Appellant" else "#ef4444"
        bg_color = "#f0f7ff" if selected_folder_info["party"] == "Appellant" else "#fff5f5"
        
        st.markdown(
            f"""
            <div style="padding: 15px; border-radius: 6px; border-left: 4px solid {border_color}; background-color: {bg_color};">
                <h3>{selected_folder_info["name"]}</h3>
                <div>Filed by: <span class="badge {'appellant' if selected_folder_info["party"] == 'Appellant' else 'respondent'}">{selected_folder_info["party"]}</span></div>
                <div>Date: {selected_folder_info["date"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Get events related to this document
        related_events = events_df[events_df["related_folder"] == selected_folder]
        
        st.markdown(f"#### Facts in {selected_folder_info['name']}")
        
        # Display related events
        for _, event in related_events.iterrows():
            # Determine if this event is contradicted by any fact in the comparison document
            contradicting_events = events_df[(events_df["related_folder"] == compared_folder) & 
                                           ((events_df["contradicted_by"] == event["date"]) | 
                                            (events_df["date"] == event["contradicted_by"]))]
            
            has_contradiction = not contradicting_events.empty
            
            # Style based on contradiction status
            card_style = f"border-left: 4px solid {'#f59e0b' if has_contradiction else border_color};"
            
            st.markdown(
                f"""
                <div style="padding: 12px; margin-bottom: 10px; border-radius: 4px; background-color: {'#fffbeb' if has_contradiction else bg_color}; {card_style}">
                    <div style="font-weight: 500; margin-bottom: 6px;">{event["event"]}</div>
                    <div style="display: flex; margin-top: 5px;">
                        <span class="badge {'disputed' if event['status'] == 'Disputed' else 'undisputed'}">{event["status"]}</span>
                        <span class="badge evidence">Evidence: {event["evidence"]}</span>
                    </div>
                    <div style="margin-top: 8px; color: #4b5563;">
                        <div><strong>{event["related_argument"]}</strong></div>
                        <div>Supports: {event["supports"]}</div>
                    </div>
                    {f'<div style="margin-top: 8px; color: #b45309;"><strong>⚠️ Contradicted by facts in {compared_folder_info["name"]}</strong></div>' if has_contradiction else ''}
                </div>
                """,
                unsafe_allow_html=True
            )
    
    with col_middle:
        # Create the "VS" display
        st.markdown(
            """
            <div class="versus-container">
                <div class="versus-line"></div>
                <div class="versus-circle">VS</div>
                <div class="versus-line"></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        # Style based on party
        border_color = "#3b82f6" if compared_folder_info["party"] == "Appellant" else "#ef4444"
        bg_color = "#f0f7ff" if compared_folder_info["party"] == "Appellant" else "#fff5f5"
        
        st.markdown(
            f"""
            <div style="padding: 15px; border-radius: 6px; border-left: 4px solid {border_color}; background-color: {bg_color};">
                <h3>{compared_folder_info["name"]}</h3>
                <div>Filed by: <span class="badge {'appellant' if compared_folder_info["party"] == 'Appellant' else 'respondent'}">{compared_folder_info["party"]}</span></div>
                <div>Date: {compared_folder_info["date"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Get events related to comparison document
        compared_events = events_df[events_df["related_folder"] == compared_folder]
        
        st.markdown(f"#### Facts in {compared_folder_info['name']}")
        
        # Display related events
        for _, event in compared_events.iterrows():
            # Determine if this event contradicts any fact in the selected document
            contradicting_events = events_df[(events_df["related_folder"] == selected_folder) & 
                                           ((events_df["contradicted_by"] == event["date"]) | 
                                            (events_df["date"] == event["contradicted_by"]))]
            
            has_contradiction = not contradicting_events.empty
            
            # Style based on contradiction status
            card_style = f"border-left: 4px solid {'#f59e0b' if has_contradiction else border_color};"
            
            st.markdown(
                f"""
                <div style="padding: 12px; margin-bottom: 10px; border-radius: 4px; background-color: {'#fffbeb' if has_contradiction else bg_color}; {card_style}">
                    <div style="font-weight: 500; margin-bottom: 6px;">{event["event"]}</div>
                    <div style="display: flex; margin-top: 5px;">
                        <span class="badge {'disputed' if event['status'] == 'Disputed' else 'undisputed'}">{event["status"]}</span>
                        <span class="badge evidence">Evidence: {event["evidence"]}</span>
                    </div>
                    <div style="margin-top: 8px; color: #4b5563;">
                        <div><strong>{event["related_argument"]}</strong></div>
                        <div>Supports: {event["supports"]}</div>
                    </div>
                    {f'<div style="margin-top: 8px; color: #b45309;"><strong>⚠️ Contradicts facts in {selected_folder_info["name"]}</strong></div>' if has_contradiction else ''}
                </div>
                """,
                unsafe_allow_html=True
            )
    
    # Display a contradiction analysis section
    st.header("Contradiction Analysis")
    
    # Find all contradicting events between the two documents
    contradictions = []
    
    # Check for contradictions from selected document to compared document
    for _, event1 in events_df[events_df["related_folder"] == selected_folder].iterrows():
        for _, event2 in events_df[events_df["related_folder"] == compared_folder].iterrows():
            if event1["date"] == event2["contradicted_by"] or event2["date"] == event1["contradicted_by"]:
                contradictions.append((event1, event2))
    
    if contradictions:
        st.markdown("### Key Contradictions")
        
        for event1, event2 in contradictions:
            st.markdown(
                f"""
                <div style="padding: 15px; border-radius: 6px; background-color: #fffbeb; margin-bottom: 15px; border-left: 4px solid #f59e0b;">
                    <h4>Contradiction: {event1["related_argument"]} vs {event2["related_argument"]}</h4>
                    
                    <div style="display: flex; margin-top: 15px;">
                        <div style="flex: 1; padding: 12px; background-color: {'#f0f7ff' if event1['party'] == 'Appellant' else '#fff5f5'}; border-radius: 4px; margin-right: 10px;">
                            <div style="font-weight: 500;">{event1["event"]}</div>
                            <div style="margin-top: 5px; font-size: 13px;">
                                <span class="badge {'appellant' if event1['party'] == 'Appellant' else 'respondent'}">{event1["party"]}</span>
                                <span class="badge evidence">Evidence: {event1["evidence"]}</span>
                            </div>
                            <div style="margin-top: 8px; font-style: italic;">"{event1["supports"]}"</div>
                        </div>
                        
                        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 0 15px;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background-color: #f59e0b; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">VS</div>
                        </div>
                        
                        <div style="flex: 1; padding: 12px; background-color: {'#f0f7ff' if event2['party'] == 'Appellant' else '#fff5f5'}; border-radius: 4px; margin-left: 10px;">
                            <div style="font-weight: 500;">{event2["event"]}</div>
                            <div style="margin-top: 5px; font-size: 13px;">
                                <span class="badge {'appellant' if event2['party'] == 'Appellant' else 'respondent'}">{event2["party"]}</span>
                                <span class="badge evidence">Evidence: {event2["evidence"]}</span>
                            </div>
                            <div style="margin-top: 8px; font-style: italic;">"{event2["supports"]}"</div>
                        </div>
                    </div>
                    
                    <div style="margin-top: 15px; padding-top: 10px; border-top: 1px solid #fcd34d;">
                        <div style="font-weight: 500;">Key Issue:</div>
                        <div>This contradiction relates to {'the continuity of the club during 1975-1976' if '1975-1976' in event1['date'] or '1975-1976' in event2['date'] else 'the consistency of club colors and visual identity'}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("No direct contradictions found between these documents.")

else:
    # Single document view
    if selected_folder_info:
        # Style based on party
        party_color = "#3b82f6" if selected_folder_info["party"] == "Appellant" else "#ef4444" if selected_folder_info["party"] == "Respondent" else "#6b7280"
        
        st.header(f"Document: {selected_folder_info['name']}")
        
        # Document header
        st.markdown(
            f"""
            <div style="padding: 15px; border-radius: 6px; border-left: 4px solid {party_color}; background-color: #f8f9fa; margin-bottom: 20px;">
                <div style="font-weight: 500; font-size: 18px;">{selected_folder_info["name"]}</div>
                <div style="display: flex; margin-top: 10px;">
                    <div><span class="badge {'appellant' if selected_folder_info['party'] == 'Appellant' else 'respondent'}">{selected_folder_info["party"]}</span></div>
                    <div style="margin-left: 15px;">Filed: {selected_folder_info["date"]}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Get events related to selected document
        related_events = events_df[events_df["related_folder"] == selected_folder]
        
        if not related_events.empty:
            st.subheader("Facts in this Document")
            
            # Display timeline of events
            for _, event in related_events.iterrows():
                st.markdown(
                    f"""
                    <div style="padding: 12px; margin-bottom: 15px; border-radius: 4px; background-color: #f8f9fa; border-left: 4px solid {party_color};">
                        <div style="font-weight: 500; margin-bottom: 6px;">{event["event"]}</div>
                        <div style="display: flex; margin-top: 5px;">
                            <span class="badge {'disputed' if event['status'] == 'Disputed' else 'undisputed'}">{event["status"]}</span>
                            <span class="badge evidence">Evidence: {event["evidence"]}</span>
                            <span style="margin-left: auto; color: #6b7280;">{event["date"]}</span>
                        </div>
                        <div style="margin-top: 8px; color: #4b5563;">
                            <div><strong>{event["related_argument"]}</strong></div>
                            <div>Supports: {event["supports"]}</div>
                        </div>
                        
                        {f'<div style="margin-top: 12px; color: #b45309;"><strong>⚠️ Note:</strong> This fact is disputed by the opposing party.</div>' if event["status"] == "Disputed" else ''}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
            # Suggestion to compare
            st.info("Enable 'Compare Documents' in the sidebar to see how these facts relate to opposing documents.")
        else:
            st.info("No fact timeline events are associated with this document.")

# Add visualization of the adversarial workflow
st.header("Case Document Workflow")

# Create a visualization of the document flow
st.markdown(
    """
    <div style="padding: 20px; background-color: #f8fafc; border-radius: 8px; margin-top: 20px;">
        <h4 style="margin-bottom: 15px;">Document Timeline & Adversarial Relationships</h4>
        
        <div style="display: flex; overflow-x: auto; padding-bottom: 15px;">
            <div style="display: flex; flex-direction: column; align-items: center; min-width: 900px;">
                <div style="display: flex; width: 100%; justify-content: space-between; position: relative;">
                    <!-- Timeline arrow -->
                    <div style="position: absolute; top: 50%; left: 0; right: 0; height: 2px; background-color: #9ca3af; z-index: 0;"></div>
    """,
    unsafe_allow_html=True
)

# Create document timeline markers
for folder in document_folders:
    # Only show the first 8 documents (exclude auxiliary folders)
    if int(folder["id"]) > 8:
        continue
        
    # Determine marker style based on party
    if folder["party"] == "Appellant":
        color = "#3b82f6"
        bg_color = "#dbeafe"
    elif folder["party"] == "Respondent":
        color = "#ef4444"
        bg_color = "#fee2e2"
    else:
        color = "#6b7280"
        bg_color = "#f3f4f6"
    
    st.markdown(
        f"""
        <div style="z-index: 1; margin-bottom: 80px;">
            <div style="width: 20px; height: 20px; border-radius: 50%; background-color: {color}; margin-bottom: 10px;"></div>
            <div style="padding: 10px; border-radius: 6px; background-color: {bg_color}; border: 1px solid {color}; width: 180px; text-align: center;">
                <div style="font-weight: 500; font-size: 14px;">{folder["name"]}</div>
                <div style="font-size: 12px; margin-top: 5px;">{folder["date"]}</div>
                <div style="font-size: 12px; margin-top: 5px;">{folder["party"]}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Close the timeline visualization
st.markdown(
    """
                </div>
                
                <!-- Adversarial relationships -->
                <div style="margin-top: 30px; width: 100%;">
                    <h5>Adversarial Relationships</h5>
                    
                    <div style="display: flex; margin-top: 15px;">
                        <div style="flex: 1; padding: 15px; background-color: #dbeafe; border-radius: 6px; border-left: 4px solid #3b82f6;">
                            <div style="font-weight: 500; margin-bottom: 10px;">Appellant Documents</div>
                            <ul style="list-style-type: none; padding-left: 0;">
                                <li style="margin-bottom: 5px;">1. Statement of Appeal</li>
                                <li style="margin-bottom: 5px;">5. Appeal Brief</li>
                                <li>7. Reply to Objection to Admissibility</li>
                            </ul>
                        </div>
                        
                        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 0 20px;">
                            <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #6b7280; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 18px;">VS</div>
                            <div style="width: 2px; height: 50px; background-color: #6b7280; margin-top: 10px;"></div>
                            <div style="margin-top: 10px; font-weight: 500;">Opposing Arguments</div>
                        </div>
                        
                        <div style="flex: 1; padding: 15px; background-color: #fee2e2; border-radius: 6px; border-left: 4px solid #ef4444;">
                            <div style="font-weight: 500; margin-bottom: 10px;">Respondent Documents</div>
                            <ul style="list-style-type: none; padding-left: 0;">
                                <li style="margin-bottom: 5px;">2. Request for a Stay</li>
                                <li style="margin-bottom: 5px;">3. Answer to Request for PM</li>
                                <li style="margin-bottom: 5px;">4. Answer to PM</li>
                                <li>8. Challenge</li>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- Key contradictions -->
                    <div style="margin-top: 30px; padding: 15px; background-color: #fffbeb; border-radius: 6px; border-left: 4px solid #f59e0b;">
                        <div style="font-weight: 500; margin-bottom: 10px;">Key Contradicting Facts</div>
                        
                        <div style="display: flex; margin-top: 10px; gap: 20px;">
                            <div style="flex: 1; padding: 10px; background-color: #f0f7ff; border-radius: 4px;">
                                <div style="font-weight: 500; font-size: 14px;">Appellant Claim</div>
                                <div style="margin-top: 5px; font-size: 13px;">Brief administrative gap in 1975-1976</div>
                                <div style="margin-top: 5px; font-size: 13px; color: #4b5563;">Evidence: C-2</div>
                            </div>
                            
                            <div style="font-weight: bold; display: flex; align-items: center;">≠</div>
                            
                            <div style="flex: 1; padding: 10px; background-color: #fff5f5; border-radius: 4px;">
                                <div style="font-weight: 500; font-size: 14px;">Respondent Claim</div>
                                <div style="margin-top: 5px; font-size: 13px;">Operations ceased between 1975-1976</div>
                                <div style="margin-top: 5px; font-size: 13px; color: #4b5563;">Evidence: R-1</div>
                            </div>
                        </div>
                        
                        <div style="display: flex; margin-top: 15px; gap: 20px;">
                            <div style="flex: 1; padding: 10px; background-color: #f0f7ff; border-radius: 4px;">
                                <div style="font-weight: 500; font-size: 14px;">Appellant Claim</div>
                                <div style="margin-top: 5px; font-size: 13px;">Consistent use of blue and white since founding</div>
                                <div style="margin-top: 5px; font-size: 13px; color: #4b5563;">Evidence: C-4</div>
                            </div>
                            
                            <div style="font-weight: bold; display: flex; align-items: center;">≠</div>
                            
                            <div style="flex: 1; padding: 10px; background-color: #fff5f5; border-radius: 4px;">
                                <div style="font-weight: 500; font-size: 14px;">Respondent Claim</div>
                                <div style="margin-top: 5px; font-size: 13px;">Pre-1976 colors represented original city district</div>
                                <div style="margin-top: 5px; font-size: 13px; color: #4b5563;">Evidence: R-5</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Add a section for comparative analysis between Statement of Appeal and Request for Stay
st.header("Focused Comparison: Statement of Appeal vs. Request for Stay")

# Create a focused comparison between the first two documents
appellant_doc = document_folders[0]  # Statement of Appeal
respondent_doc = document_folders[1]  # Request for Stay

# Get related events for each document
appellant_events = events_df[events_df["related_folder"] == appellant_doc["id"]]
respondent_events = events_df[events_df["related_folder"] == respondent_doc["id"]]

st.markdown(
    f"""
    <div style="padding: 20px; background-color: #f8fafc; border-radius: 8px; margin-top: 20px;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
            <div style="flex: 1; padding: 15px; background-color: #f0f7ff; border-radius: 6px; border-left: 4px solid #3b82f6; margin-right: 10px;">
                <div style="font-weight: 500; font-size: 16px;">{appellant_doc["name"]}</div>
                <div style="margin-top: 5px; font-size: 14px;">Filed by Appellant on {appellant_doc["date"]}</div>
            </div>
            
            <div style="flex: 1; padding: 15px; background-color: #fff5f5; border-radius: 6px; border-left: 4px solid #ef4444; margin-left: 10px;">
                <div style="font-weight: 500; font-size: 16px;">{respondent_doc["name"]}</div>
                <div style="margin-top: 5px; font-size: 14px;">Filed by Respondent on {respondent_doc["date"]}</div>
            </div>
        </div>
        
        <div style="margin-top: 20px;">
            <h4>Key Differences in Facts</h4>
            
            <table style="width: 100%; border-collapse: collapse; margin-top: 15px;">
                <thead>
                    <tr>
                        <th style="padding: 10px; background-color: #dbeafe; text-align: left; width: 50%;">Statement of Appeal Claims</th>
                        <th style="padding: 10px; background-color: #fee2e2; text-align: left; width: 50%;">Request for Stay Counterclaims</th>
                    </tr>
                </thead>
                <tbody>
    """,
    unsafe_allow_html=True
)

# Add rows for each fact comparison
# For simplicity, we'll just use the events we've defined that relate to these documents
for idx, app_event in appellant_events.iterrows():
    # Try to find a contradicting event in respondent document
    contradicting = respondent_events[respondent_events["contradicted_by"] == app_event["date"]]
    if contradicting.empty:
        contradicting = respondent_events[respondent_events["date"] == app_event["contradicted_by"]]
    
    if not contradicting.empty:
        resp_event = contradicting.iloc[0]
        
        st.markdown(
            f"""
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #e5e7eb; background-color: #f0f7ff;">
                    <div style="font-weight: 500;">{app_event["event"]}</div>
                    <div style="margin-top: 5px; font-size: 13px;">
                        <span class="badge {"disputed" if app_event["status"] == "Disputed" else "undisputed"}">{app_event["status"]}</span>
                        <span class="badge evidence">Evidence: {app_event["evidence"]}</span>
                    </div>
                    <div style="margin-top: 8px; color: #4b5563;">Supports: {app_event["supports"]}</div>
                </td>
                
                <td style="padding: 10px; border-bottom: 1px solid #e5e7eb; background-color: #fff5f5;">
                    <div style="font-weight: 500;">{resp_event["event"]}</div>
                    <div style="margin-top: 5px; font-size: 13px;">
                        <span class="badge {"disputed" if resp_event["status"] == "Disputed" else "undisputed"}">{resp_event["status"]}</span>
                        <span class="badge evidence">Evidence: {resp_event["evidence"]}</span>
                    </div>
                    <div style="margin-top: 8px; color: #4b5563;">Supports: {resp_event["supports"]}</div>
                </td>
            </tr>
            """,
            unsafe_allow_html=True
        )
    else:
        # Show uncontradicted appellant facts
        st.markdown(
            f"""
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #e5e7eb; background-color: #f0f7ff;">
                    <div style="font-weight: 500;">{app_event["event"]}</div>
                    <div style="margin-top: 5px; font-size: 13px;">
                        <span class="badge {"disputed" if app_event["status"] == "Disputed" else "undisputed"}">{app_event["status"]}</span>
                        <span class="badge evidence">Evidence: {app_event["evidence"]}</span>
                    </div>
                    <div style="margin-top: 8px; color: #4b5563;">Supports: {app_event["supports"]}</div>
                </td>
                
                <td style="padding: 10px; border-bottom: 1px solid #e5e7eb; background-color: #fff5f5; font-style: italic; color: #6b7280;">
                    No direct contradiction to this fact
                </td>
            </tr>
            """,
            unsafe_allow_html=True
        )

# Check for any respondent facts that don't contradict appellant facts (unique facts)
for idx, resp_event in respondent_events.iterrows():
    # Skip if this event contradicts or is contradicted by an appellant event
    if not appellant_events[appellant_events["contradicted_by"] == resp_event["date"]].empty:
        continue
    if not appellant_events[appellant_events["date"] == resp_event["contradicted_by"]].empty:
        continue
        
    # This is a unique respondent fact
    st.markdown(
        f"""
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #e5e7eb; background-color: #f0f7ff; font-style: italic; color: #6b7280;">
                No related fact in Statement of Appeal
            </td>
            
            <td style="padding: 10px; border-bottom: 1px solid #e5e7eb; background-color: #fff5f5;">
                <div style="font-weight: 500;">{resp_event["event"]}</div>
                <div style="margin-top: 5px; font-size: 13px;">
                    <span class="badge {"disputed" if resp_event["status"] == "Disputed" else "undisputed"}">{resp_event["status"]}</span>
                    <span class="badge evidence">Evidence: {resp_event["evidence"]}</span>
                </div>
                <div style="margin-top: 8px; color: #4b5563;">Supports: {resp_event["supports"]}</div>
            </td>
        </tr>
        """,
        unsafe_allow_html=True
    )

# Close the table and container
st.markdown(
    """
                </tbody>
            </table>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Add a section explaining how to use the visualization
st.markdown(
    """
    <div style="margin-top: 30px; padding: 15px; background-color: #f3f4f6; border-radius: 6px;">
        <h4 style="margin-bottom: 10px;">How to Use This Visualization</h4>
        
        <ol style="margin-left: 20px;">
            <li style="margin-bottom: 5px;">Use the <strong>Compare Documents</strong> checkbox in the sidebar to enable adversarial view</li>
            <li style="margin-bottom: 5px;">Select primary document (1️⃣) and comparison document (2️⃣) to see opposing facts</li>
            <li style="margin-bottom: 5px;">Look for highlighted contradictions in yellow/amber color</li>
            <li>Focus on disputed facts (amber badges) when analyzing case strengths and weaknesses</li>
        </ol>
        
        <div style="margin-top: 15px; font-weight: 500;">Key Insight:</div>
        <div>The core dispute centers around continuity during 1975-1976 and whether the club's identity remained consistent through visual elements like colors.</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Function to run the app
if __name__ == "__main__":
    # This is already running in the Streamlit app
    pass
