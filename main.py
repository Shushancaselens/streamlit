import streamlit as st

# =============================================================================
# STREAMLIT SESSION STATE VIEW SWITCHING
# =============================================================================

# Initialize session state to track selected view
if 'view' not in st.session_state:
    st.session_state.view = "Facts"

# Sidebar with navigation buttons
with st.sidebar:
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

# =============================================================================
# HTML/JAVASCRIPT VIEW SWITCHING
# =============================================================================

# CSS for view switching
view_switching_css = """
<style>
/* View toggle buttons */
.view-toggle {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 16px;
}

.view-toggle button {
    padding: 8px 16px;
    border: 1px solid #e2e8f0;
    background-color: #f7fafc;
    cursor: pointer;
}

.view-toggle button.active {
    background-color: #4299e1;
    color: white;
    border-color: #4299e1;
}

.view-toggle button:first-child {
    border-radius: 4px 0 0 4px;
}

.view-toggle button:nth-child(2) {
    border-left: none;
    border-right: none;
}

.view-toggle button:nth-child(3) {
    border-left: none;
    border-right: none;
}

.view-toggle button:last-child {
    border-radius: 0 4px 4px 0;
}

/* Tab buttons */
.facts-header {
    display: flex;
    margin-bottom: 20px;
    border-bottom: 1px solid #dee2e6;
}

.tab-button {
    padding: 10px 20px;
    background: none;
    border: none;
    cursor: pointer;
}

.tab-button.active {
    border-bottom: 2px solid #4299e1;
    color: #4299e1;
    font-weight: 500;
}

/* Content sections */
.content-section {
    display: none;
}

.content-section.active {
    display: block;
}

.facts-content {
    margin-top: 20px;
}
</style>
"""

# JavaScript switching functions
view_switching_js = """
<script>
// =============================================================================
// VIEW SWITCHING FUNCTIONS
// =============================================================================

// Switch between main views (card, table, timeline, docset)
function switchView(viewType) {
    const tableBtn = document.getElementById('table-view-btn');
    const cardBtn = document.getElementById('card-view-btn');
    const timelineBtn = document.getElementById('timeline-view-btn');
    const docsetBtn = document.getElementById('docset-view-btn');
    
    const tableContent = document.getElementById('table-view-content');
    const cardContent = document.getElementById('card-view-content');
    const timelineContent = document.getElementById('timeline-view-content');
    const docsetContent = document.getElementById('docset-view-content');
    
    // Remove active class from all buttons
    tableBtn.classList.remove('active');
    cardBtn.classList.remove('active');
    timelineBtn.classList.remove('active');
    docsetBtn.classList.remove('active');
    
    // Hide all content
    tableContent.style.display = 'none';
    cardContent.style.display = 'none';
    timelineContent.style.display = 'none';
    docsetContent.style.display = 'none';
    
    // Activate the selected view
    if (viewType === 'card') {
        cardBtn.classList.add('active');
        cardContent.style.display = 'block';
        renderCardView();
    } else if (viewType === 'table') {
        tableBtn.classList.add('active');
        tableContent.style.display = 'block';
        renderTableView();
    } else if (viewType === 'timeline') {
        timelineBtn.classList.add('active');
        timelineContent.style.display = 'block';
        renderTimeline();
    } else if (viewType === 'docset') {
        docsetBtn.classList.add('active');
        docsetContent.style.display = 'block';
        renderDocumentSets();
    }
}

// Switch between fact tabs (all, disputed, undisputed)
function switchFactsTab(tabType) {
    const allBtn = document.getElementById('all-facts-btn');
    const disputedBtn = document.getElementById('disputed-facts-btn');
    const undisputedBtn = document.getElementById('undisputed-facts-btn');
    
    // Remove active class from all
    allBtn.classList.remove('active');
    disputedBtn.classList.remove('active');
    undisputedBtn.classList.remove('active');
    
    // Add active to selected
    if (tabType === 'all') {
        allBtn.classList.add('active');
        renderFacts('all');
    } else if (tabType === 'disputed') {
        disputedBtn.classList.add('active');
        renderFacts('disputed');
    } else {
        undisputedBtn.classList.add('active');
        renderFacts('undisputed');
    }
    
    // Update active view based on current view type
    const tableContent = document.getElementById('table-view-content');
    const cardContent = document.getElementById('card-view-content');
    const timelineContent = document.getElementById('timeline-view-content');
    const docsetContent = document.getElementById('docset-view-content');
    
    if (cardContent.style.display !== 'none') {
        renderCardView(tabType);
    } else if (tableContent.style.display !== 'none') {
        renderFacts(tabType);
    } else if (timelineContent.style.display !== 'none') {
        renderTimeline(tabType);
    } else if (docsetContent.style.display !== 'none') {
        renderDocumentSets(tabType);
    }
}

// Generic function to switch between content sections
function switchContentSection(sectionId) {
    // Hide all sections
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        section.classList.remove('active');
    });
    
    // Show selected section
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active');
    }
}

// =============================================================================
// UTILITY FUNCTIONS FOR BUTTON STATE MANAGEMENT
// =============================================================================

// Set active button in a button group
function setActiveButton(buttonId, groupSelector) {
    // Remove active from all buttons in group
    const buttons = document.querySelectorAll(groupSelector);
    buttons.forEach(btn => btn.classList.remove('active'));
    
    // Add active to target button
    const targetButton = document.getElementById(buttonId);
    if (targetButton) {
        targetButton.classList.add('active');
    }
}

// Toggle visibility of content with smooth transition
function toggleContent(contentId, isVisible = null) {
    const content = document.getElementById(contentId);
    if (!content) return;
    
    if (isVisible === null) {
        // Toggle current state
        isVisible = content.style.display === 'none';
    }
    
    if (isVisible) {
        content.style.display = 'block';
        content.classList.add('active');
    } else {
        content.style.display = 'none';
        content.classList.remove('active');
    }
}

// =============================================================================
// INITIALIZATION
// =============================================================================

// Initialize default view state
document.addEventListener('DOMContentLoaded', function() {
    // Set default active states
    switchView('card'); // Default to card view
    switchFactsTab('all'); // Default to all facts
});
</script>
"""

# HTML structure for the switchers
html_switcher_structure = """
<!-- Main View Toggle -->
<div class="view-toggle">
    <button id="card-view-btn" class="active" onclick="switchView('card')">Card View</button>
    <button id="table-view-btn" onclick="switchView('table')">Table View</button>
    <button id="docset-view-btn" onclick="switchView('docset')">Document Categories</button>
    <button id="timeline-view-btn" onclick="switchView('timeline')">Timeline View</button>
</div>

<!-- Facts Tab Header -->
<div class="facts-header">
    <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
    <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
    <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
</div>

<!-- Content Containers -->
<div id="card-view-content" class="facts-content">
    <!-- Card view content -->
</div>

<div id="table-view-content" class="facts-content" style="display: none;">
    <!-- Table view content -->
</div>

<div id="timeline-view-content" class="facts-content" style="display: none;">
    <!-- Timeline view content -->
</div>

<div id="docset-view-content" class="facts-content" style="display: none;">
    <!-- Document sets view content -->
</div>
"""

# Example usage function
def render_view_switcher():
    """
    Example function showing how to use the view switcher
    """
    # Check current session state view
    if st.session_state.view == "Facts":
        # Render the facts view with switchers
        st.markdown("### Facts Section")
        
        # Include the HTML with CSS and JavaScript
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            {view_switching_css}
        </head>
        <body>
            {html_switcher_structure}
            {view_switching_js}
        </body>
        </html>
        """
        
        st.components.v1.html(html_content, height=600)
        
    elif st.session_state.view == "Arguments":
        st.markdown("### Arguments Section")
        # Arguments content here
        
    elif st.session_state.view == "Exhibits":
        st.markdown("### Exhibits Section")
        # Exhibits content here
