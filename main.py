import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Legal Arguments Analysis",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Card styling */
    .card {
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        background-color: white;
        margin-bottom: 1rem;
        padding: 1rem;
    }
    
    /* Header styling */
    h1 {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    h2 {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
    }
    h3 {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Tabs styling */
    .tab-container {
        display: flex;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
    .tab {
        padding: 0.75rem 1.5rem;
        cursor: pointer;
        font-weight: 500;
        font-size: 0.9rem;
        color: #6b7280;
    }
    .tab.active {
        color: #3b82f6;
        border-bottom: 2px solid #3b82f6;
    }
    
    /* Custom table */
    .styled-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin-bottom: 1rem;
    }
    .styled-table th {
        background-color: #f9fafb;
        padding: 0.75rem 1rem;
        text-align: left;
        font-size: 0.875rem;
        font-weight: 500;
        color: #6b7280;
        border-bottom: 1px solid #e5e7eb;
        border-top: 1px solid #e5e7eb;
    }
    .styled-table td {
        padding: 0.75rem 1rem;
        font-size: 0.875rem;
        color: #374151;
        border-bottom: 1px solid #e5e7eb;
    }
    
    /* Argument section styling */
    .argument-header {
        display: flex;
        padding: 0.75rem 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        cursor: pointer;
    }
    .claimant-header {
        background-color: #eff6ff;
        border: 1px solid #bfdbfe;
    }
    .respondent-header {
        background-color: #fee2e2;
        border: 1px solid #fecaca;
    }
    .argument-content {
        margin-bottom: 1rem;
        padding: 0 1rem;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 0.125rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
        margin-right: 0.25rem;
    }
    .badge-blue {
        background-color: #dbeafe;
        color: #1e40af;
    }
    .badge-red {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    .badge-green {
        background-color: #d1fae5;
        color: #065f46;
    }
    .badge-gray {
        background-color: #f3f4f6;
        color: #4b5563;
    }
    
    /* Point cards */
    .point-card {
        background-color: #f9fafb;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .legal-point {
        background-color: #eff6ff;
        border-radius: 8px;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .factual-point {
        background-color: #d1fae5;
        border-radius: 8px;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    
    /* Two column layout */
    .two-column {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }
    
    /* Disputed row styling */
    .disputed-row {
        background-color: #fee2e2;
    }
    
    /* Action button styling */
    .action-button {
        background-color: transparent;
        color: #3b82f6;
        border: none;
        padding: 0.25rem 0.5rem;
        font-size: 0.875rem;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Sample data - Timeline
timeline_data = pd.DataFrame([
    {
        "date": "2023-01-15",
        "appellant_version": "Contract signed with Club",
        "respondent_version": "—",
        "status": "Undisputed"
    },
    {
        "date": "2023-03-20",
        "appellant_version": "Player received notification of exclusion from team",
        "respondent_version": "—",
        "status": "Undisputed"
    },
    {
        "date": "2023-03-22",
        "appellant_version": "Player requested explanation",
        "respondent_version": "—",
        "status": "Undisputed"
    },
    {
        "date": "2023-04-01",
        "appellant_version": "Player sent termination letter",
        "respondent_version": "—",
        "status": "Undisputed"
    },
    {
        "date": "2023-04-05",
        "appellant_version": "—",
        "respondent_version": "Club rejected termination as invalid",
        "status": "Undisputed"
    },
    {
        "date": "2023-04-10",
        "appellant_version": "Player was denied access to training facilities",
        "respondent_version": "—",
        "status": "Disputed"
    },
    {
        "date": "2023-04-15",
        "appellant_version": "—",
        "respondent_version": "Club issued warning letter",
        "status": "Undisputed"
    },
    {
        "date": "2023-05-01",
        "appellant_version": "Player filed claim with FIFA",
        "respondent_version": "—",
        "status": "Undisputed"
    }
])

# Sample data - Exhibits
exhibits_data = pd.DataFrame([
    {
        "id": "C-1",
        "party": "Appellant",
        "title": "Employment Contract",
        "type": "contract",
        "summary": "Employment contract dated 15 January 2023 between Player and Club"
    },
    {
        "id": "C-2",
        "party": "Appellant",
        "title": "Termination Letter",
        "type": "letter",
        "summary": "Player's termination letter sent on 1 April 2023"
    },
    {
        "id": "C-3",
        "party": "Appellant",
        "title": "Email Correspondence",
        "type": "communication",
        "summary": "Email exchanges between Player and Club from 22-30 March 2023"
    },
    {
        "id": "C-4",
        "party": "Appellant",
        "title": "Witness Statement",
        "type": "statement",
        "summary": "Statement from team captain confirming Player's exclusion"
    },
    {
        "id": "R-1",
        "party": "Respondent",
        "title": "Club Regulations",
        "type": "regulations",
        "summary": "Internal regulations of the Club dated January 2022"
    },
    {
        "id": "R-2",
        "party": "Respondent",
        "title": "Warning Letter",
        "type": "letter",
        "summary": "Warning letter issued to Player on 15 April 2023"
    },
    {
        "id": "R-3",
        "party": "Respondent",
        "title": "Training Schedule",
        "type": "schedule",
        "summary": "Team training schedule for March-April 2023"
    }
])

# Main app container
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h1>Legal Arguments Analysis</h1>', unsafe_allow_html=True)

# Tab selection using simple radio buttons
tab = st.radio("", ["Summary of Arguments", "Timeline", "Exhibits"], horizontal=True, label_visibility="collapsed")

# Main content based on selected tab
if tab == "Summary of Arguments":
    # Simple view selector
    view_mode = st.radio("View Mode:", ["Standard View", "Topic View"], horizontal=True)
    
    if view_mode == "Standard View":
        # Claimant and Respondent headers
        st.markdown("""
        <div class="two-column">
            <div>
                <h2 style="color: #3b82f6;">Claimant's Arguments</h2>
            </div>
            <div>
                <h2 style="color: #ef4444;">Respondent's Arguments</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Sporting Succession Arguments
        st.markdown("""
        <div class="two-column">
            <!-- Claimant Argument -->
            <div>
                <div class="argument-header claimant-header">
                    <div>
                        <span style="font-weight: 500; font-size: 0.875rem;">1. Sporting Succession</span>
                        <span class="badge badge-blue">¶15-18</span>
                    </div>
                </div>
                <div class="argument-content">
                    <div class="point-card">
                        <div style="margin-bottom: 0.5rem;">
                            <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
                            <span class="badge badge-blue">¶15-16</span>
                        </div>
                        <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                            <li>Analysis of multiple established criteria</li>
                            <li>Focus on continuous use of identifying elements</li>
                            <li>Public recognition assessment</li>
                        </ul>
                    </div>
                    
                    <h5>Legal Points</h5>
                    <div class="legal-point">
                        <span class="badge badge-blue">Legal</span>
                        <p>CAS jurisprudence establishes criteria for sporting succession</p>
                        <div>
                            <span class="badge badge-blue">CAS 2016/A/4576</span>
                            <span style="font-size: 0.75rem; color: #6b7280;">¶15-17</span>
                        </div>
                    </div>
                    
                    <h5>Factual Points</h5>
                    <div class="factual-point">
                        <span class="badge badge-green">Factual</span>
                        <p>Continuous operation under same name since 1950</p>
                        <span style="font-size: 0.75rem; color: #6b7280;">1950-present</span>
                        <span style="font-size: 0.75rem; color: #6b7280;">¶18-19</span>
                    </div>
                </div>
            </div>
            
            <!-- Respondent Argument -->
            <div>
                <div class="argument-header respondent-header">
                    <div>
                        <span style="font-weight: 500; font-size: 0.875rem;">1. Sporting Succession Rebuttal</span>
                        <span class="badge badge-red">¶200-218</span>
                    </div>
                </div>
                <div class="argument-content">
                    <div class="point-card">
                        <div style="margin-bottom: 0.5rem;">
                            <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
                            <span class="badge badge-blue">¶200-202</span>
                        </div>
                        <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                            <li>Challenge to claimed continuity of operations</li>
                            <li>Analysis of discontinuities in club operations</li>
                            <li>Dispute over public recognition factors</li>
                        </ul>
                    </div>
                    
                    <h5>Legal Points</h5>
                    <div class="legal-point">
                        <span class="badge badge-blue">Legal</span>
                        <p>CAS jurisprudence requires operational continuity not merely identification</p>
                        <div>
                            <span class="badge badge-blue">CAS 2017/A/5465</span>
                            <span style="font-size: 0.75rem; color: #6b7280;">¶203-205</span>
                        </div>
                    </div>
                    
                    <h5>Factual Points</h5>
                    <div class="factual-point">
                        <span class="badge badge-green">Factual</span>
                        <span class="badge badge-red">Disputed by Claimant</span>
                        <p>Operations ceased between 1975-1976</p>
                        <span style="font-size: 0.75rem; color: #6b7280;">1975-1976</span>
                        <span style="font-size: 0.75rem; color: #6b7280;">¶206-207</span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Doping Arguments
        st.markdown("""
        <div class="two-column">
            <!-- Claimant Argument -->
            <div>
                <div class="argument-header claimant-header">
                    <div>
                        <span style="font-weight: 500; font-size: 0.875rem;">2. Doping Violation Chain of Custody</span>
                        <span class="badge badge-blue">¶70-125</span>
                    </div>
                </div>
                <div class="argument-content">
                    <div class="point-card">
                        <div style="margin-bottom: 0.5rem;">
                            <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
                            <span class="badge badge-blue">¶70-72</span>
                        </div>
                        <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                            <li>Analysis of sample collection and handling procedures</li>
                            <li>Evaluation of laboratory testing protocols</li>
                            <li>Assessment of chain of custody documentation</li>
                        </ul>
                    </div>
                    
                    <h5>Legal Points</h5>
                    <div class="legal-point">
                        <span class="badge badge-blue">Legal</span>
                        <p>WADA Code Article 5 establishes procedural requirements</p>
                        <div>
                            <span class="badge badge-blue">WADA Code 2021</span>
                            <span class="badge badge-blue">International Standard for Testing</span>
                            <span style="font-size: 0.75rem; color: #6b7280;">¶73-75</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Respondent Argument -->
            <div>
                <div class="argument-header respondent-header">
                    <div>
                        <span style="font-weight: 500; font-size: 0.875rem;">2. Doping Chain of Custody Defense</span>
                        <span class="badge badge-red">¶250-290</span>
                    </div>
                </div>
                <div class="argument-content">
                    <div class="point-card">
                        <div style="margin-bottom: 0.5rem;">
                            <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
                            <span class="badge badge-blue">¶250-252</span>
                        </div>
                        <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                            <li>Defense of sample collection procedures</li>
                            <li>Validation of laboratory testing protocols</li>
                            <li>Completeness of documentation</li>
                        </ul>
                    </div>
                    
                    <h5>Legal Points</h5>
                    <div class="legal-point">
                        <span class="badge badge-blue">Legal</span>
                        <p>Minor procedural deviations do not invalidate results</p>
                        <div>
                            <span class="badge badge-blue">CAS 2019/A/6148</span>
                            <span style="font-size: 0.75rem; color: #6b7280;">¶253-255</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    else:  # Topic View
        # Sporting Succession and Identity Topic
        st.markdown("""
        <h2>Sporting Succession and Identity</h2>
        <p style="color: #6b7280; margin-bottom: 1rem;">Questions of club identity, continuity, and succession rights</p>
        
        <div class="two-column">
            <div>
                <h3 style="color: #3b82f6;">Claimant's Arguments</h3>
            </div>
            <div>
                <h3 style="color: #ef4444;">Respondent's Arguments</h3>
            </div>
        </div>
        
        <div class="two-column">
            <!-- Claimant Argument -->
            <div>
                <div class="argument-header claimant-header">
                    <div>
                        <span style="font-weight: 500; font-size: 0.875rem;">1. Sporting Succession</span>
                        <span class="badge badge-blue">¶15-18</span>
                    </div>
                </div>
                <div class="argument-content">
                    <div class="point-card">
                        <div style="margin-bottom: 0.5rem;">
                            <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
                            <span class="badge badge-blue">¶15-16</span>
                        </div>
                        <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                            <li>Analysis of multiple established criteria</li>
                            <li>Focus on continuous use of identifying elements</li>
                            <li>Public recognition assessment</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Respondent Argument -->
            <div>
                <div class="argument-header respondent-header">
                    <div>
                        <span style="font-weight: 500; font-size: 0.875rem;">1. Sporting Succession Rebuttal</span>
                        <span class="badge badge-red">¶200-218</span>
                    </div>
                </div>
                <div class="argument-content">
                    <div class="point-card">
                        <div style="margin-bottom: 0.5rem;">
                            <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
                            <span class="badge badge-blue">¶200-202</span>
                        </div>
                        <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                            <li>Challenge to claimed continuity of operations</li>
                            <li>Analysis of discontinuities in club operations</li>
                            <li>Dispute over public recognition factors</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Doping Violation Topic -->
        <h2 style="margin-top: 2rem;">Doping Violation and Chain of Custody</h2>
        <p style="color: #6b7280; margin-bottom: 1rem;">Issues related to doping test procedures and evidence handling</p>
        
        <div class="two-column">
            <div>
                <h3 style="color: #3b82f6;">Claimant's Arguments</h3>
            </div>
            <div>
                <h3 style="color: #ef4444;">Respondent's Arguments</h3>
            </div>
        </div>
        
        <div class="two-column">
            <!-- Claimant Argument -->
            <div>
                <div class="argument-header claimant-header">
                    <div>
                        <span style="font-weight: 500; font-size: 0.875rem;">2. Doping Violation Chain of Custody</span>
                        <span class="badge badge-blue">¶70-125</span>
                    </div>
                </div>
                <div class="argument-content">
                    <div class="point-card">
                        <div style="margin-bottom: 0.5rem;">
                            <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
                            <span class="badge badge-blue">¶70-72</span>
                        </div>
                        <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                            <li>Analysis of sample collection and handling procedures</li>
                            <li>Evaluation of laboratory testing protocols</li>
                            <li>Assessment of chain of custody documentation</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Respondent Argument -->
            <div>
                <div class="argument-header respondent-header">
                    <div>
                        <span style="font-weight: 500; font-size: 0.875rem;">2. Doping Chain of Custody Defense</span>
                        <span class="badge badge-red">¶250-290</span>
                    </div>
                </div>
                <div class="argument-content">
                    <div class="point-card">
                        <div style="margin-bottom: 0.5rem;">
                            <span style="font-size: 0.875rem; font-weight: 500;">Key Points</span>
                            <span class="badge badge-blue">¶250-252</span>
                        </div>
                        <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                            <li>Defense of sample collection procedures</li>
                            <li>Validation of laboratory testing protocols</li>
                            <li>Completeness of documentation</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif tab == "Timeline":
    # Timeline view
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.button("Copy")
        st.button("Export Data")
    
    # Search and filter
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search = st.text_input("Search events...")
    with col2:
        disputed_only = st.checkbox("Disputed events only")
    
    # Filter data
    filtered_data = timeline_data
    if search:
        filtered_data = filtered_data[
            filtered_data["appellant_version"].str.contains(search, case=False, na=False) |
            filtered_data["respondent_version"].str.contains(search, case=False, na=False)
        ]
    if disputed_only:
        filtered_data = filtered_data[filtered_data["status"] == "Disputed"]
    
    # Display timeline table
    st.markdown('<table class="styled-table">', unsafe_allow_html=True)
    
    # Table header
    st.markdown("""
    <tr>
        <th>DATE</th>
        <th>APPELLANT'S VERSION</th>
        <th>RESPONDENT'S VERSION</th>
        <th>STATUS</th>
    </tr>
    """, unsafe_allow_html=True)
    
    # Table rows
    for _, row in filtered_data.iterrows():
        status_color = "text-red-600" if row["status"] == "Disputed" else "text-green-600"
        row_class = "disputed-row" if row["status"] == "Disputed" else ""
        
        st.markdown(f"""
        <tr class="{row_class}">
            <td>{row["date"]}</td>
            <td>{row["appellant_version"]}</td>
            <td>{row["respondent_version"]}</td>
            <td style="color: {'#b91c1c' if row['status'] == 'Disputed' else '#047857'}">{row["status"]}</td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown('</table>', unsafe_allow_html=True)

else:  # Exhibits tab
    # Exhibits view
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.button("Copy", key="copy_exhibits")
        st.button("Export Data", key="export_exhibits")
    
    # Search and filters
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        search_exhibits = st.text_input("Search exhibits...", key="search_exhibits")
    with col2:
        party_filter = st.selectbox("Party", ["All Parties", "Appellant", "Respondent"])
    with col3:
        type_options = ["All Types"] + sorted(exhibits_data["type"].unique().tolist())
        type_filter = st.selectbox("Type", type_options)
    
    # Filter data
    filtered_exhibits = exhibits_data
    if search_exhibits:
        filtered_exhibits = filtered_exhibits[
            filtered_exhibits["title"].str.contains(search_exhibits, case=False) |
            filtered_exhibits["summary"].str.contains(search_exhibits, case=False) |
            filtered_exhibits["id"].str.contains(search_exhibits, case=False)
        ]
    if party_filter != "All Parties":
        filtered_exhibits = filtered_exhibits[filtered_exhibits["party"] == party_filter]
    if type_filter != "All Types":
        filtered_exhibits = filtered_exhibits[filtered_exhibits["type"] == type_filter]
    
    # Display exhibits table
    st.markdown('<table class="styled-table">', unsafe_allow_html=True)
    
    # Table header
    st.markdown("""
    <tr>
        <th>EXHIBIT ID</th>
        <th>PARTY</th>
        <th>TITLE</th>
        <th>TYPE</th>
        <th>SUMMARY</th>
        <th>ACTIONS</th>
    </tr>
    """, unsafe_allow_html=True)
    
    # Table rows
    for _, row in filtered_exhibits.iterrows():
        party_class = "badge-blue" if row["party"] == "Appellant" else "badge-red"
        
        st.markdown(f"""
        <tr>
            <td>{row["id"]}</td>
            <td><span class="badge {party_class}">{row["party"]}</span></td>
            <td>{row["title"]}</td>
            <td><span class="badge badge-gray">{row["type"]}</span></td>
            <td>{row["summary"]}</td>
            <td><button class="action-button">View</button></td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown('</table>', unsafe_allow_html=True)

# Close the card container
st.markdown('</div>', unsafe_allow_html=True)
