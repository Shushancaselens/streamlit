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
    
    # Create the facts header/tabs
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        all_facts_btn = st.button("All Facts", key="all_facts_btn", use_container_width=True)
    with col2:
        disputed_facts_btn = st.button("Disputed Facts", key="disputed_facts_btn", use_container_width=True)
    with col3:
        undisputed_facts_btn = st.button("Undisputed Facts", key="undisputed_facts_btn", use_container_width=True)
    
    # Initialize view in session state if not present
    if 'facts_view' not in st.session_state:
        st.session_state.facts_view = "all"
    
    # Update view based on button clicks
    if disputed_facts_btn:
        st.session_state.facts_view = "disputed"
    elif undisputed_facts_btn:
        st.session_state.facts_view = "undisputed"
    elif all_facts_btn:
        st.session_state.facts_view = "all"
    
    # Get the facts data
    facts_data = get_all_facts()
    
    # Define column styles for the table
    table_css = """
    <style>
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th {
        text-align: left;
        padding: 12px;
        background-color: #f8f9fa;
        border-bottom: 2px solid #dee2e6;
        position: sticky;
        top: 0;
        cursor: pointer;
    }
    td {
        padding: 12px;
        border-bottom: 1px solid #dee2e6;
    }
    tr:hover {
        background-color: #f8f9fa;
    }
    tr.disputed {
        background-color: rgba(229, 62, 62, 0.05);
    }
    .badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 500;
    }
    .appellant-badge {
        background-color: rgba(49, 130, 206, 0.1);
        color: #3182ce;
    }
    .respondent-badge {
        background-color: rgba(229, 62, 62, 0.1);
        color: #e53e3e;
    }
    .exhibit-badge {
        background-color: rgba(221, 107, 32, 0.1);
        color: #dd6b20;
        margin-right: 5px;
    }
    .disputed-badge {
        background-color: rgba(229, 62, 62, 0.1);
        color: #e53e3e;
    }
    </style>
    """
    
    st.markdown(table_css, unsafe_allow_html=True)
    
    # Filter facts based on selected view
    if st.session_state.facts_view == "disputed":
        filtered_facts = [fact for fact in facts_data if fact['isDisputed']]
    elif st.session_state.facts_view == "undisputed":
        filtered_facts = [fact for fact in facts_data if not fact['isDisputed']]
    else:
        filtered_facts = facts_data
    
    # Create the table HTML
    table_html = """
    <table class="table-view">
        <thead>
            <tr>
                <th onclick="sortTable('facts-table-body', 0)">Date</th>
                <th onclick="sortTable('facts-table-body', 1)">Event</th>
                <th onclick="sortTable('facts-table-body', 2)">Party</th>
                <th onclick="sortTable('facts-table-body', 3)">Status</th>
                <th onclick="sortTable('facts-table-body', 4)">Related Argument</th>
                <th onclick="sortTable('facts-table-body', 5)">Evidence</th>
            </tr>
        </thead>
        <tbody id="facts-table-body">
    """
    
    # Add rows to table
    for fact in filtered_facts:
        # Create party badge HTML
        if fact['party'] == "Appellant":
            party_badge = f'<span class="badge appellant-badge">{fact["party"]}</span>'
        else:
            party_badge = f'<span class="badge respondent-badge">{fact["party"]}</span>'
        
        # Create status cell content
        if fact['isDisputed']:
            status_cell = '<span class="badge disputed-badge">Disputed</span>'
            row_class = 'class="disputed"'
        else:
            status_cell = 'Undisputed'
            row_class = ''
        
        # Create exhibits badges
        exhibits_badges = ""
        if 'exhibits' in fact and fact['exhibits']:
            for exhibit in fact['exhibits']:
                exhibits_badges += f'<span class="badge exhibit-badge">{exhibit}</span>'
        
        # Add row to table
        table_html += f"""
        <tr {row_class}>
            <td>{fact['date']}</td>
            <td>{fact['point']}</td>
            <td>{party_badge}</td>
            <td>{status_cell}</td>
            <td>{fact['argId']}. {fact['argTitle']}</td>
            <td>{exhibits_badges if exhibits_badges else 'None'}</td>
        </tr>
        """
    
    # Close the table
    table_html += """
        </tbody>
    </table>
    """
    
    # Add script for sorting
    table_html += """
    <script>
    function sortTable(tableId, columnIndex) {
        const table = document.getElementById(tableId);
        const rows = Array.from(table.rows);
        let dir = 1; // 1 for ascending, -1 for descending
        
        // Check if already sorted in this direction
        if (table.getAttribute('data-sort-column') === String(columnIndex) &&
            table.getAttribute('data-sort-dir') === '1') {
            dir = -1;
        }
        
        // Sort the rows
        rows.sort((a, b) => {
            const cellA = a.cells[columnIndex].textContent.trim();
            const cellB = b.cells[columnIndex].textContent.trim();
            
            // Handle date sorting
            if (columnIndex === 0) {
                // Attempt to parse as dates
                const dateA = new Date(cellA);
                const dateB = new Date(cellB);
                
                if (!isNaN(dateA) && !isNaN(dateB)) {
                    return dir * (dateA - dateB);
                }
            }
            
            return dir * cellA.localeCompare(cellB);
        });
        
        // Remove existing rows and append in new order
        rows.forEach(row => table.appendChild(row));
        
        // Store current sort direction and column
        table.setAttribute('data-sort-column', columnIndex);
        table.setAttribute('data-sort-dir', dir);
    }
    </script>
    """
    
    # Display the table
    st.markdown(table_html, unsafe_allow_html=True)
    
    # Create a dataframe for CSV download
    df = pd.DataFrame(filtered_facts)
    if not df.empty:
        df['exhibits'] = df['exhibits'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
        df['Status'] = df['isDisputed'].apply(lambda x: 'Disputed' if x else 'Undisputed')
        df_csv = df[['date', 'point', 'party', 'Status', 'argId', 'argTitle', 'exhibits']].rename(
            columns={
                'date': 'Date', 
                'point': 'Event', 
                'party': 'Party', 
                'argId': 'Argument ID', 
                'argTitle': 'Argument Title',
                'exhibits': 'Exhibits'
            }
        )
        
        # Add download link
        view_name = st.session_state.facts_view
        st.markdown(get_csv_download_link(df_csv, f"{view_name}_facts.csv", f"Download {view_name.capitalize()} Facts CSV"), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
