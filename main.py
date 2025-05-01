import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import json
import random

st.set_page_config(layout="wide", page_title="CaseLens - Legal Document Timeline")

# Custom CSS for styling similar to the reference image
st.markdown("""
<style>
    .folder {
        background-color: #f8f9fa;
        border-radius: 4px;
        padding: 8px 12px;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
        cursor: pointer;
    }
    .folder:hover {
        background-color: #e9ecef;
    }
    .folder-icon {
        color: #4285f4;
        margin-right: 10px;
    }
    .selected {
        background-color: #e9ecef;
        border-left: 3px solid #4285f4;
    }
    .timeline-item {
        border-left: 2px solid #ccc;
        padding-left: 15px;
        padding-bottom: 15px;
        position: relative;
    }
    .timeline-item:before {
        content: '';
        width: 12px;
        height: 12px;
        background-color: white;
        border: 2px solid #4285f4;
        border-radius: 50%;
        position: absolute;
        left: -7px;
    }
    .timeline-date {
        font-weight: bold;
        color: #666;
    }
    .timeline-event {
        margin-top: 5px;
    }
    .party-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8em;
        margin-right: 8px;
    }
    .appellant {
        background-color: #e6f2ff;
        color: #0066cc;
    }
    .respondent {
        background-color: #ffebe6;
        color: #cc3300;
    }
    .status-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8em;
        margin-right: 8px;
    }
    .disputed {
        background-color: #ffebe6;
        color: #cc3300;
    }
    .undisputed {
        background-color: #e6f7e6;
        color: #008000;
    }
    .evidence-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8em;
        background-color: #f8f9fa;
        color: #666;
    }
    .header {
        font-weight: bold;
        margin-bottom: 10px;
    }
    .main-container {
        display: flex;
        margin-top: 20px;
    }
    .file-structure {
        width: 30%;
        padding-right: 20px;
    }
    .timeline-view {
        width: 70%;
        border-left: 1px solid #ddd;
        padding-left: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Header with logo and title
col1, col2 = st.columns([1, 11])
with col1:
    st.markdown('<div style="background-color: #4285f4; width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">CL</div>', unsafe_allow_html=True)
with col2:
    st.title("CaseLens")

# Sidebar navigation
st.sidebar.markdown("## Legal Analysis")
st.sidebar.button("📄 Arguments")
st.sidebar.button("📊 Facts", type="primary")
st.sidebar.button("📁 Exhibits")

# Sample data - in a real app, this would come from a database
document_folders = [
    {"id": 1, "name": "1. Statement of Appeal", "type": "folder", "party": "Appellant"},
    {"id": 2, "name": "2. Request for a Stay", "type": "folder", "party": "Respondent"},
    {"id": 3, "name": "3. Answer to Request for PM", "type": "folder", "party": "Appellant"},
    {"id": 4, "name": "4. Answer to PM", "type": "folder", "party": "Appellant"},
    {"id": 5, "name": "5. Appeal Brief", "type": "folder", "party": "Appellant"},
    {"id": 6, "name": "6. Brief on Admissibility", "type": "folder", "party": "Respondent"},
    {"id": 7, "name": "7. Reply to Objection to Admissibility", "type": "folder", "party": "Appellant"},
    {"id": 8, "name": "8. Challenge", "type": "folder", "party": "Respondent"},
    {"id": 9, "name": "ChatGPT", "type": "folder", "party": "N/A"},
    {"id": 10, "name": "Jurisprudence", "type": "folder", "party": "N/A"},
    {"id": 11, "name": "Objection to Admissibility", "type": "folder", "party": "Respondent"},
    {"id": 12, "name": "Swiss Court", "type": "folder", "party": "N/A"}
]

# Function to generate a larger sample dataset of events
def generate_sample_events(num_events=100):
    base_events = [
        {"id": 1, "date": "1950-01-01", "end_date": "present", "event": "Continuous operation under same name since 1950", "party": "Appellant", "status": "Undisputed", "argument": "1. Sporting Succession", "evidence": "C-1", "document_id": 1},
        {"id": 2, "date": "1950-01-01", "end_date": None, "event": "Initial registration in 1950", "party": "Appellant", "status": "Undisputed", "argument": "1.1.1. Registration History", "evidence": "C-2", "document_id": 1},
        {"id": 3, "date": "1950-01-01", "end_date": "present", "event": "Consistent use of blue and white since founding", "party": "Appellant", "status": "Disputed", "argument": "1.2. Club Colors Analysis", "evidence": "C-4", "document_id": 5},
        {"id": 4, "date": "1950-01-01", "end_date": "1975-12-31", "event": "Pre-1976 colors represented original city district", "party": "Respondent", "status": "Undisputed", "argument": "1.2.1. Color Changes Analysis", "evidence": "R-5", "document_id": 2},
        {"id": 5, "date": "1970-01-01", "end_date": "1980-12-31", "event": "Minor shade variations do not affect continuity", "party": "Appellant", "status": "Undisputed", "argument": "1.2.1. Color Variations Analysis", "evidence": "C-5", "document_id": 5},
        {"id": 6, "date": "1975-01-01", "end_date": "1976-12-31", "event": "Brief administrative gap in 1975-1976", "party": "Appellant", "status": "Disputed", "argument": "1.1.1. Registration History", "evidence": "C-2", "document_id": 3},
        {"id": 7, "date": "1975-01-01", "end_date": "1976-12-31", "event": "Operations ceased between 1975-1976", "party": "Respondent", "status": "Disputed", "argument": "1. Sporting Succession", "evidence": "R-1", "document_id": 2},
        {"id": 8, "date": "1976-01-01", "end_date": None, "event": "Filed objection to new registration application", "party": "Respondent", "status": "Disputed", "argument": "1.1.2. Legal Identity", "evidence": "R-3", "document_id": 11},
        {"id": 9, "date": "1977-05-15", "end_date": None, "event": "Court ruling on trademark rights", "party": "N/A", "status": "Undisputed", "argument": "2.1. Legal Precedents", "evidence": "J-1", "document_id": 10},
        {"id": 10, "date": "2023-01-10", "end_date": None, "event": "Statement of Appeal filed", "party": "Appellant", "status": "Undisputed", "argument": "Procedural", "evidence": "A-1", "document_id": 1},
        {"id": 11, "date": "2023-01-25", "end_date": None, "event": "Request for stay submitted", "party": "Respondent", "status": "Undisputed", "argument": "Procedural", "evidence": "R-10", "document_id": 2},
        {"id": 12, "date": "2023-02-15", "end_date": None, "event": "Answer to PM filed", "party": "Appellant", "status": "Undisputed", "argument": "Procedural", "evidence": "A-5", "document_id": 4},
        {"id": 13, "date": "2023-03-01", "end_date": None, "event": "Appeal Brief submitted", "party": "Appellant", "status": "Undisputed", "argument": "Substantive", "evidence": "A-8", "document_id": 5},
        {"id": 14, "date": "2023-03-20", "end_date": None, "event": "Objection to Admissibility filed", "party": "Respondent", "status": "Disputed", "argument": "Procedural", "evidence": "R-15", "document_id": 11},
        {"id": 15, "date": "2023-04-05", "end_date": None, "event": "Reply to Objection submitted", "party": "Appellant", "status": "Undisputed", "argument": "Procedural", "evidence": "A-12", "document_id": 7},
    ]
    
    if num_events <= 15:
        return base_events[:num_events]
    
    additional_events = []
    event_templates = [
        {"event": "Submission of exhibit {}", "argument": "Evidence Submission", "status": "Undisputed"},
        {"event": "Filing of supplementary brief on {}", "argument": "Legal Argumentation", "status": "Undisputed"},
        {"event": "Expert witness testimony on {}", "argument": "Expert Evidence", "status": "Disputed"},
        {"event": "Motion to dismiss {} claim", "argument": "Procedural Challenge", "status": "Disputed"},
        {"event": "Amendment to {} submission", "argument": "Procedural", "status": "Undisputed"},
        {"event": "Request for extension due to {}", "argument": "Procedural", "status": "Undisputed"},
        {"event": "Dispute over {} evidence authenticity", "argument": "Evidence Challenge", "status": "Disputed"},
        {"event": "Supplementary evidence on {}", "argument": "Evidence Submission", "status": "Undisputed"},
        {"event": "Challenge to jurisdiction based on {}", "argument": "Jurisdictional Challenge", "status": "Disputed"},
        {"event": "Response to {} allegations", "argument": "Substantive Defense", "status": "Disputed"},
    ]
    
    topics = ["trademark", "operational continuity", "brand identity", "historical records", 
             "fan recognition", "merchandising rights", "competition participation",
             "sporting heritage", "club constitution", "international recognition"]
    
    dates = pd.date_range(start='1980-01-01', end='2023-04-30', periods=num_events-15)
    dates = dates.strftime('%Y-%m-%d').tolist()
    
    for i in range(16, num_events + 1):
        template = random.choice(event_templates)
        topic = random.choice(topics)
        party = random.choice(["Appellant", "Respondent"])
        doc_id = random.randint(1, 12)
        
        event = {
            "id": i,
            "date": random.choice(dates),
            "end_date": None if random.random() > 0.3 else random.choice(dates),
            "event": template["event"].format(topic),
            "party": party,
            "status": template["status"],
            "argument": template["argument"],
            "evidence": f"{'C' if party == 'Appellant' else 'R'}-{random.randint(1, 50)}",
            "document_id": doc_id
        }
        additional_events.append(event)
    
    # Ensure end_date is after date if both exist
    for event in additional_events:
        if event["end_date"] and event["date"] > event["end_date"]:
            event["date"], event["end_date"] = event["end_date"], event["date"]
    
    return base_events + additional_events

# Generate sample events - can adjust the number as needed
events = generate_sample_events(100)

# Convert to DataFrames
df_folders = pd.DataFrame(document_folders)
df_events = pd.DataFrame(events)

# Main content area
st.markdown("# Summary of arguments")

# Create two tabs
tab1, tab2, tab3 = st.tabs(["Case Facts", "Document Timeline", "Connected View"])

with tab1:
    # Add filter controls at the top
    st.markdown("### Filters")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        # Date range filter
        min_date = pd.to_datetime(df_events["date"].min())
        max_date = pd.to_datetime(datetime.now().strftime('%Y-%m-%d'))
        date_range = st.date_input(
            "Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )
    
    with col2:
        # Party filter
        parties = ["All"] + sorted(df_events["party"].unique().tolist())
        selected_party = st.selectbox("Party", parties)
    
    with col3:
        # Status filter
        statuses = ["All"] + sorted(df_events["status"].unique().tolist())
        selected_status = st.selectbox("Status", statuses)
    
    with col4:
        # Document filter
        documents = ["All"] + [f"{doc['id']}. {doc['name']}" for doc in document_folders]
        selected_document = st.selectbox("Document", documents)
    
    # Search box
    search_term = st.text_input("Search events", "")
    
    # Subtabs for filtering facts
    fact_tabs = st.tabs(["All Facts", "Disputed Facts", "Undisputed Facts"])
    
    # Filter data based on user selections
    filtered_df = df_events.copy()
    
    # Apply date filter
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (pd.to_datetime(filtered_df["date"]) >= pd.to_datetime(start_date)) & 
            (pd.to_datetime(filtered_df["date"]) <= pd.to_datetime(end_date))
        ]
    
    # Apply party filter
    if selected_party != "All":
        filtered_df = filtered_df[filtered_df["party"] == selected_party]
    
    # Apply status filter
    if selected_status != "All":
        filtered_df = filtered_df[filtered_df["status"] == selected_status]
    
    # Apply document filter
    if selected_document != "All":
        doc_id = int(selected_document.split(".")[0])
        filtered_df = filtered_df[filtered_df["document_id"] == doc_id]
    
    # Apply search filter
    if search_term:
        filtered_df = filtered_df[
            filtered_df["event"].str.contains(search_term, case=False) |
            filtered_df["argument"].str.contains(search_term, case=False)
        ]
    
    # Format data for display
    display_df = filtered_df[["date", "event", "party", "status", "argument", "evidence"]].copy()
    
    # Add end_date if available
    display_df["date_display"] = display_df["date"]
    for idx, row in filtered_df.iterrows():
        if pd.notna(row["end_date"]) and row["end_date"] != "None" and row["end_date"] != "present":
            display_df.loc[idx, "date_display"] = f"{row['date']} to {row['end_date']}"
        elif row["end_date"] == "present":
            display_df.loc[idx, "date_display"] = f"{row['date']} to present"
    
    display_df = display_df.rename(columns={
        "date_display": "Date", 
        "event": "Event", 
        "party": "Party", 
        "status": "Status", 
        "argument": "Related Argument", 
        "evidence": "Evidence"
    })
    
    # Reorder columns
    display_df = display_df[["Date", "Event", "Party", "Status", "Related Argument", "Evidence"]]
    
    # Set up pagination for the data display
    items_per_page = 15
    total_rows = len(display_df)
    total_pages = (total_rows + items_per_page - 1) // items_per_page
    
    # Initialize pagination state
    if "facts_page" not in st.session_state:
        st.session_state.facts_page = 1
    
    # Function to render a stylized table
    def render_styled_table(df):
        # Apply styling using a custom HTML table
        html_table = "<table style='width:100%; border-collapse: collapse;'>"
        
        # Table header
        html_table += "<thead><tr style='background-color: #f2f2f2;'>"
        for col in df.columns:
            html_table += f"<th style='padding: 8px; text-align: left; border-bottom: 2px solid #ddd;'>{col}</th>"
        html_table += "</tr></thead>"
        
        # Table body
        html_table += "<tbody>"
        for _, row in df.iterrows():
            html_table += "<tr style='border-bottom: 1px solid #ddd;'>"
            
            # Date column
            html_table += f"<td style='padding: 8px;'>{row['Date']}</td>"
            
            # Event column
            html_table += f"<td style='padding: 8px;'>{row['Event']}</td>"
            
            # Party column with styling
            party_style = ""
            if row['Party'] == "Appellant":
                party_style = "background-color: #e6f2ff; color: #0066cc; padding: 2px 8px; border-radius: 12px; font-size: 0.9em;"
            elif row['Party'] == "Respondent":
                party_style = "background-color: #ffebe6; color: #cc3300; padding: 2px 8px; border-radius: 12px; font-size: 0.9em;"
            html_table += f"<td style='padding: 8px;'><span style='{party_style}'>{row['Party']}</span></td>"
            
            # Status column with styling
            status_style = ""
            if row['Status'] == "Disputed":
                status_style = "background-color: #ffebe6; color: #cc3300; padding: 2px 8px; border-radius: 12px; font-size: 0.9em;"
            elif row['Status'] == "Undisputed":
                status_style = "background-color: #e6f7e6; color: #008000; padding: 2px 8px; border-radius: 12px; font-size: 0.9em;"
            html_table += f"<td style='padding: 8px;'><span style='{status_style}'>{row['Status']}</span></td>"
            
            # Related Argument column
            html_table += f"<td style='padding: 8px;'>{row['Related Argument']}</td>"
            
            # Evidence column with styling
            evidence_style = "background-color: #f8f9fa; color: #666; padding: 2px 8px; border-radius: 4px; font-size: 0.9em;"
            html_table += f"<td style='padding: 8px;'><span style='{evidence_style}'>{row['Evidence']}</span></td>"
            
            html_table += "</tr>"
        html_table += "</tbody></table>"
        
        return html_table
    
    with fact_tabs[0]:  # All Facts
        # Display the count of events
        st.markdown(f"### Showing {len(display_df)} events")
        
        # Add export options
        col1, col2 = st.columns([1, 5])
        with col1:
            st.download_button(
                label="Export CSV",
                data=display_df.to_csv(index=False).encode('utf-8'),
                file_name='case_facts.csv',
                mime='text/csv',
            )
        
        # Pagination controls
        if total_pages > 1:
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col1:
                if st.button("← Previous", key="prev_facts", disabled=(st.session_state.facts_page == 1)):
                    st.session_state.facts_page = max(1, st.session_state.facts_page - 1)
                    st.rerun()
            
            with col2:
                st.markdown(f"<div style='text-align: center;'>Page {st.session_state.facts_page} of {total_pages}</div>", unsafe_allow_html=True)
                page_selector = st.slider("Go to page", min_value=1, max_value=total_pages, value=st.session_state.facts_page, key="facts_page_slider")
                if page_selector != st.session_state.facts_page:
                    st.session_state.facts_page = page_selector
                    st.rerun()
            
            with col3:
                if st.button("Next →", key="next_facts", disabled=(st.session_state.facts_page == total_pages)):
                    st.session_state.facts_page = min(total_pages, st.session_state.facts_page + 1)
                    st.rerun()
        
        # Calculate slice for current page
        start_idx = (st.session_state.facts_page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, total_rows)
        
        # Display the current page of data
        page_df = display_df.iloc[start_idx:end_idx]
        
        # Render the styled table
        st.markdown(render_styled_table(page_df), unsafe_allow_html=True)
    
    with fact_tabs[1]:  # Disputed Facts
        disputed_df = display_df[display_df["Status"] == "Disputed"]
        
        # Display the count of events
        st.markdown(f"### Showing {len(disputed_df)} disputed events")
        
        # Pagination for disputed facts
        disputed_total_pages = (len(disputed_df) + items_per_page - 1) // items_per_page
        
        # Initialize pagination state for disputed
        if "disputed_page" not in st.session_state:
            st.session_state.disputed_page = 1
        st.session_state.disputed_page = min(st.session_state.disputed_page, max(1, disputed_total_pages))
        
        # Pagination controls
        if disputed_total_pages > 1:
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col1:
                if st.button("← Previous", key="prev_disputed", disabled=(st.session_state.disputed_page == 1)):
                    st.session_state.disputed_page = max(1, st.session_state.disputed_page - 1)
                    st.rerun()
            
            with col2:
                st.markdown(f"<div style='text-align: center;'>Page {st.session_state.disputed_page} of {disputed_total_pages}</div>", unsafe_allow_html=True)
            
            with col3:
                if st.button("Next →", key="next_disputed", disabled=(st.session_state.disputed_page == disputed_total_pages)):
                    st.session_state.disputed_page = min(disputed_total_pages, st.session_state.disputed_page + 1)
                    st.rerun()
        
        # Calculate slice for current page
        start_idx = (st.session_state.disputed_page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, len(disputed_df))
        
        # Display the current page of data
        page_df = disputed_df.iloc[start_idx:end_idx]
        
        # Render the styled table
        st.markdown(render_styled_table(page_df), unsafe_allow_html=True)
    
    with fact_tabs[2]:  # Undisputed Facts
        undisputed_df = display_df[display_df["Status"] == "Undisputed"]
        
        # Display the count of events
        st.markdown(f"### Showing {len(undisputed_df)} undisputed events")
        
        # Pagination for undisputed facts
        undisputed_total_pages = (len(undisputed_df) + items_per_page - 1) // items_per_page
        
        # Initialize pagination state for undisputed
        if "undisputed_page" not in st.session_state:
            st.session_state.undisputed_page = 1
        st.session_state.undisputed_page = min(st.session_state.undisputed_page, max(1, undisputed_total_pages))
        
        # Pagination controls
        if undisputed_total_pages > 1:
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col1:
                if st.button("← Previous", key="prev_undisputed", disabled=(st.session_state.undisputed_page == 1)):
                    st.session_state.undisputed_page = max(1, st.session_state.undisputed_page - 1)
                    st.rerun()
            
            with col2:
                st.markdown(f"<div style='text-align: center;'>Page {st.session_state.undisputed_page} of {undisputed_total_pages}</div>", unsafe_allow_html=True)
            
            with col3:
                if st.button("Next →", key="next_undisputed", disabled=(st.session_state.undisputed_page == undisputed_total_pages)):
                    st.session_state.undisputed_page = min(undisputed_total_pages, st.session_state.undisputed_page + 1)
                    st.rerun()
        
        # Calculate slice for current page
        start_idx = (st.session_state.undisputed_page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, len(undisputed_df))
        
        # Display the current page of data
        page_df = undisputed_df.iloc[start_idx:end_idx]
        
        # Render the styled table
        st.markdown(render_styled_table(page_df), unsafe_allow_html=True)

with tab2:
    # Create columns for the document structure and timeline
    col1, col2 = st.columns([3, 7])
    
    with col1:
        st.markdown("### Document Structure")
        
        # Initialize session state for selected folder if not already set
        if "selected_folder" not in st.session_state:
            st.session_state.selected_folder = 1
            
        # Add search for documents
        doc_search = st.text_input("Search documents", "")
        
        # Filter documents based on search
        filtered_folders = document_folders
        if doc_search:
            filtered_folders = [
                folder for folder in document_folders 
                if doc_search.lower() in folder["name"].lower() or 
                   (folder["party"] != "N/A" and doc_search.lower() in folder["party"].lower())
            ]
        
        # Display folders with selection capability using Streamlit components
        for i, folder in enumerate(filtered_folders):
            col1, col2 = st.columns([4, 1])
            
            # Style based on selection
            bg_color = "#e9ecef" if folder["id"] == st.session_state.selected_folder else "#f8f9fa"
            border_left = "3px solid #4285f4" if folder["id"] == st.session_state.selected_folder else "none"
            
            # Style based on party
            party_color = "#ffffff"
            party_bg = "#dddddd"
            if folder["party"] == "Appellant":
                party_color = "#0066cc"
                party_bg = "#e6f2ff"
            elif folder["party"] == "Respondent":
                party_color = "#cc3300"
                party_bg = "#ffebe6"
            
            with col1:
                # Use a button styled as a folder
                if st.button(
                    f"📁 {folder['name']}", 
                    key=f"folder_{folder['id']}",
                    use_container_width=True,
                    type="secondary" if folder["id"] != st.session_state.selected_folder else "primary"
                ):
                    st.session_state.selected_folder = folder["id"]
                    st.rerun()
            
            with col2:
                # Show party tag if applicable
                if folder["party"] != "N/A":
                    st.markdown(
                        f'<div style="background-color: {party_bg}; color: {party_color}; border-radius: 12px; padding: 4px 8px; text-align: center; font-size: 0.7em;">{folder["party"]}</div>',
                        unsafe_allow_html=True
                    )
    
    with col2:
        st.markdown("### Document Timeline")
        
        # Get the selected folder
        selected_folder = st.session_state.selected_folder
        
        # Find the folder info
        selected_folder_info = next((f for f in document_folders if f["id"] == selected_folder), None)
        
        if selected_folder_info:
            st.markdown(f"#### {selected_folder_info['name']}")
            
            # Party tag if applicable
            if selected_folder_info["party"] != "N/A":
                party_class = "appellant" if selected_folder_info["party"] == "Appellant" else "respondent"
                st.markdown(
                    f'<span class="party-tag {party_class}">{selected_folder_info["party"]}</span>',
                    unsafe_allow_html=True
                )
        
        # Filter events for the selected folder
        folder_events = df_events[df_events["document_id"] == selected_folder]
        
        # Add search and filter for events within the document
        event_search = st.text_input("Search events in this document", "")
        
        # Add date sorting
        sort_by = st.radio("Sort by", ["Newest First", "Oldest First"], horizontal=True)
        
        # Filter and sort events
        if event_search:
            folder_events = folder_events[
                folder_events["event"].str.contains(event_search, case=False) |
                folder_events["argument"].str.contains(event_search, case=False)
            ]
        
        if sort_by == "Newest First":
            folder_events = folder_events.sort_values(by="date", ascending=False)
        else:
            folder_events = folder_events.sort_values(by="date", ascending=True)
        
        # Show number of events
        st.markdown(f"##### Showing {len(folder_events)} events")
        
        # Create a paginator if there are many events
        items_per_page = 10
        total_pages = (len(folder_events) + items_per_page - 1) // items_per_page
        
        if total_pages > 1:
            col1, col2, col3 = st.columns([2, 3, 2])
            with col2:
                page = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1)
        else:
            page = 1
        
        # Calculate start and end indices
        start_idx = (page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, len(folder_events))
        
        # Display paginated events
        if len(folder_events) > 0:
            events_to_display = folder_events.iloc[start_idx:end_idx]
            
            for _, event in events_to_display.iterrows():
                # Format the date range
                if pd.notna(event["end_date"]) and event["end_date"] != "None" and event["end_date"] != "present":
                    date_display = f"{event['date']} to {event['end_date']}"
                elif event["end_date"] == "present":
                    date_display = f"{event['date']} to present"
                else:
                    date_display = event["date"]
                
                # Format the party tag
                party_class = ""
                if event["party"] == "Appellant":
                    party_class = "appellant"
                elif event["party"] == "Respondent":
                    party_class = "respondent"
                
                # Format the status tag
                status_class = ""
                if event["status"] == "Disputed":
                    status_class = "disputed"
                elif event["status"] == "Undisputed":
                    status_class = "undisputed"
                
                # Create timeline item
                st.markdown(
                    f"""
                    <div class="timeline-item">
                        <div class="timeline-date">{date_display}</div>
                        <div class="timeline-event">
                            <strong>{event["event"]}</strong>
                        </div>
                        <div style="margin-top: 5px;">
                            <span class="party-tag {party_class}">{event["party"]}</span>
                            <span class="status-tag {status_class}">{event["status"]}</span>
                            <span class="evidence-tag">{event["evidence"]}</span>
                        </div>
                        <div style="margin-top: 5px;">
                            <span>{event["argument"]}</span>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            # Pagination controls
            if total_pages > 1:
                col1, col2, col3 = st.columns([1, 3, 1])
                with col1:
                    if st.button("← Previous", disabled=(page == 1)):
                        st.session_state.page = max(1, page - 1)
                        st.rerun()
                
                with col2:
                    st.markdown(f"<div style='text-align: center;'>Page {page} of {total_pages}</div>", unsafe_allow_html=True)
                
                with col3:
                    if st.button("Next →", disabled=(page == total_pages)):
                        st.session_state.page = min(total_pages, page + 1)
                        st.rerun()
        else:
            st.info("No events associated with this document.")

with tab3:
    st.markdown("### Connected Timeline View")
    
    # Add visualization controls for the connected view
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Filter by date range
        min_date = pd.to_datetime(df_events["date"].min())
        max_date = pd.to_datetime(datetime.now().strftime('%Y-%m-%d'))
        timeline_date_range = st.date_input(
            "Timeline Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            key="timeline_dates"
        )
    
    with col2:
        # Filter by document type
        doc_type = st.multiselect(
            "Document Type",
            options=["Appellant Documents", "Respondent Documents", "Other Documents"],
            default=["Appellant Documents", "Respondent Documents", "Other Documents"]
        )
    
    with col3:
        # Filter by status
        timeline_status = st.multiselect(
            "Event Status",
            options=["Disputed", "Undisputed"],
            default=["Disputed", "Undisputed"]
        )
    
    # Search box for timeline
    timeline_search = st.text_input("Search timeline events", "")
    
    # Group events by document
    document_events = {}
    
    # Apply filters to events
    filtered_events = df_events.copy()
    
    # Apply date filter
    if len(timeline_date_range) == 2:
        start_date, end_date = timeline_date_range
        filtered_events = filtered_events[
            (pd.to_datetime(filtered_events["date"]) >= pd.to_datetime(start_date)) & 
            (pd.to_datetime(filtered_events["date"]) <= pd.to_datetime(end_date))
        ]
    
    # Apply status filter
    if timeline_status:
        filtered_events = filtered_events[filtered_events["status"].isin(timeline_status)]
    
    # Apply search filter
    if timeline_search:
        filtered_events = filtered_events[
            filtered_events["event"].str.contains(timeline_search, case=False) |
            filtered_events["argument"].str.contains(timeline_search, case=False)
        ]
    
    # Group filtered events by document
    for _, event in filtered_events.iterrows():
        doc_id = event["document_id"]
        if doc_id not in document_events:
            doc_info = df_folders[df_folders["id"] == doc_id].iloc[0]
            document_events[doc_id] = {
                "document": doc_info["name"],
                "party": doc_info["party"],
                "events": []
            }
        
        # Format date display
        if pd.notna(event["end_date"]) and event["end_date"] != "None" and event["end_date"] != "present":
            date_display = f"{event['date']} to {event['end_date']}"
        elif event["end_date"] == "present":
            date_display = f"{event['date']} to present"
        else:
            date_display = event["date"]
        
        document_events[doc_id]["events"].append({
            "date": event["date"],
            "date_display": date_display,
            "event": event["event"],
            "party": event["party"],
            "status": event["status"],
            "argument": event["argument"],
            "evidence": event["evidence"]
        })
    
    # Sort documents by type if requested
    filtered_docs = []
    for doc_id, doc_data in document_events.items():
        include = False
        if "Appellant Documents" in doc_type and doc_data["party"] == "Appellant":
            include = True
        elif "Respondent Documents" in doc_type and doc_data["party"] == "Respondent":
            include = True
        elif "Other Documents" in doc_type and doc_data["party"] == "N/A":
            include = True
        
        if include:
            filtered_docs.append(doc_data)
    
    # Sort documents by name
    filtered_docs.sort(key=lambda x: x["document"])
    
    # Display filtered document count
    st.markdown(f"### Showing {len(filtered_docs)} documents with {sum(len(doc['events']) for doc in filtered_docs)} events")
    
    # Display the connected timeline
    for i, doc in enumerate(filtered_docs):
        # Create expandable section for each document
        with st.expander(f"{doc['document']} ({len(doc['events'])} events)", expanded=i < 3):  # Auto-expand first 3
            # Style based on party
            party_class = ""
            if doc["party"] == "Appellant":
                party_class = "appellant"
            elif doc["party"] == "Respondent":
                party_class = "respondent"
            
            if doc["party"] != "N/A":
                st.markdown(f"<span class='party-tag {party_class}'>{doc['party']}</span>", unsafe_allow_html=True)
            
            # Sort events by date
            doc["events"].sort(key=lambda x: x["date"], reverse=True)
            
            # Check if there are many events - if so, add pagination
            if len(doc["events"]) > 10:
                # Create a unique key for this document's pagination
                pagination_key = f"doc_{i}_page"
                
                # Initialize pagination in session state if not exists
                if pagination_key not in st.session_state:
                    st.session_state[pagination_key] = 1
                
                # Calculate pagination
                items_per_page = 10
                total_pages = (len(doc["events"]) + items_per_page - 1) // items_per_page
                
                # Pagination controls
                col1, col2, col3 = st.columns([1, 3, 1])
                with col2:
                    page = st.slider(
                        f"Page for {doc['document']}", 
                        min_value=1, 
                        max_value=total_pages, 
                        value=st.session_state[pagination_key],
                        key=f"slider_{pagination_key}"
                    )
                    st.session_state[pagination_key] = page
                
                # Get events for current page
                start_idx = (page - 1) * items_per_page
                end_idx = min(start_idx + items_per_page, len(doc["events"]))
                events_to_display = doc["events"][start_idx:end_idx]
            else:
                events_to_display = doc["events"]
            
            # Display events in a timeline
            for event in events_to_display:
                # Format status
                status_class = ""
                if event["status"] == "Disputed":
                    status_class = "disputed"
                elif event["status"] == "Undisputed":
                    status_class = "undisputed"
                
                # Format party (for event party, which might differ from document party)
                event_party_class = ""
                if event["party"] == "Appellant":
                    event_party_class = "appellant"
                elif event["party"] == "Respondent":
                    event_party_class = "respondent"
                
                # Create timeline item
                timeline_html = f"""
                <div class="timeline-item">
                    <div class="timeline-date">{event["date_display"]}</div>
                    <div class="timeline-event">
                        <strong>{event["event"]}</strong>
                    </div>
                    <div style="margin-top: 5px;">
                        <span class="party-tag {event_party_class}">{event["party"]}</span>
                        <span class="status-tag {status_class}">{event["status"]}</span>
                        <span class="evidence-tag">{event["evidence"]}</span>
                    </div>
                    <div style="margin-top: 5px;">
                        <span>{event["argument"]}</span>
                    </div>
                </div>
                """
                st.markdown(timeline_html, unsafe_allow_html=True)
    
    # If no documents match filters
    if not filtered_docs:
        st.info("No documents match the selected filters. Try adjusting your search criteria.")
    
    # Add timeline visualization option
    if st.checkbox("Show chronological timeline view", value=False):
        st.markdown("### Chronological Timeline")
        
        # Get all events across all documents
        all_events = []
        for doc_id, doc_data in document_events.items():
            for event in doc_data["events"]:
                all_events.append({
                    "date": event["date"],
                    "date_display": event["date_display"],
                    "event": event["event"],
                    "party": event["party"],
                    "status": event["status"],
                    "argument": event["argument"],
                    "evidence": event["evidence"],
                    "document": doc_data["document"]
                })
        
        # Sort all events by date
        all_events.sort(key=lambda x: x["date"])
        
        # Group events by year
        events_by_year = {}
        for event in all_events:
            year = event["date"].split("-")[0]
            if year not in events_by_year:
                events_by_year[year] = []
            events_by_year[year].append(event)
        
        # Display events by year
        for year in sorted(events_by_year.keys()):
            with st.expander(f"{year} ({len(events_by_year[year])} events)", expanded=False):
                for event in events_by_year[year]:
                    # Format styles
                    status_class = "disputed" if event["status"] == "Disputed" else "undisputed"
                    party_class = "appellant" if event["party"] == "Appellant" else "respondent" if event["party"] == "Respondent" else ""
                    
                    # Create timeline item with document reference
                    st.markdown(f"""
                    <div class="timeline-item">
                        <div class="timeline-date">{event["date_display"]}</div>
                        <div class="timeline-event">
                            <strong>{event["event"]}</strong>
                        </div>
                        <div style="margin-top: 5px;">
                            <span class="party-tag {party_class}">{event["party"]}</span>
                            <span class="status-tag {status_class}">{event["status"]}</span>
                            <span class="evidence-tag">{event["evidence"]}</span>
                        </div>
                        <div style="margin-top: 5px;">
                            <span>{event["argument"]}</span>
                        </div>
                        <div style="margin-top: 5px; font-style: italic; color: #666;">
                            Document: {event["document"]}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

# Add custom JavaScript to handle click events and update state
st.markdown("""
<script>
// Listen for messages from Streamlit
window.addEventListener('message', function(event) {
    // Check if the message is from Streamlit
    if (event.data.type === 'streamlit:componentReady') {
        // Make folders clickable
        const folders = document.querySelectorAll('.folder');
        folders.forEach(folder => {
            folder.addEventListener('click', function() {
                // Get the folder ID from the data attribute
                const folderId = this.getAttribute('data-id');
                
                // Update Streamlit state
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    value: folderId
                }, '*');
            });
        });
    }
});
</script>
""", unsafe_allow_html=True)
