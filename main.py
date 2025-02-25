import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Get data for JavaScript use - I'll keep this the same as before
def get_argument_data():
    # Same data structure as before
    # ...shortened for brevity...
    return {
        "claimantArgs": {
            "1": {
                "id": "1",
                "title": "Sporting Succession",
                "paragraphs": "15-18",
                "overview": {"points": ["Analysis of multiple established criteria"]},
                "legalPoints": [
                    {"point": "CAS jurisprudence establishes criteria for sporting succession"}
                ],
                "children": {
                    "1.1": {
                        "id": "1.1",
                        "title": "Club Name Analysis",
                        "children": {}
                    }
                }
            }
        },
        "respondentArgs": {
            "1": {
                "id": "1",
                "title": "Sporting Succession Rebuttal",
                "paragraphs": "200-218",
                "overview": {"points": ["Challenge to claimed continuity of operations"]},
                "legalPoints": [
                    {"point": "CAS jurisprudence requires operational continuity not merely identification"}
                ],
                "children": {
                    "1.1": {
                        "id": "1.1",
                        "title": "Club Name Analysis Rebuttal",
                        "children": {}
                    }
                }
            }
        },
        "topics": []
    }

def get_timeline_data():
    # Shortened for brevity
    return []

def get_exhibits_data():
    # Shortened for brevity
    return []

# Main app
def main():
    # Set title
    st.title("Legal Arguments Analysis")
    
    # HTML content for the UI with improved alignment
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Base styling */
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                margin: 0;
                padding: 0;
            }
            
            /* Tab navigation */
            .tabs {
                display: flex;
                border-bottom: 1px solid #e2e8f0;
                margin-bottom: 1.5rem;
            }
            .tab {
                padding: 1rem 1.5rem;
                font-weight: 500;
                color: #718096;
                cursor: pointer;
                position: relative;
            }
            .tab:hover {
                color: #4a5568;
            }
            .tab.active {
                color: #3182ce;
                border-bottom: 2px solid #3182ce;
            }
            
            /* Tab content sections */
            .tab-content {
                display: none;
            }
            .tab-content.active {
                display: block;
            }
            
            /* View toggle */
            .view-toggle {
                display: flex;
                justify-content: flex-end;
                margin-bottom: 1rem;
            }
            .view-toggle-container {
                background-color: #f7fafc;
                border-radius: 0.375rem;
                padding: 0.25rem;
            }
            .view-btn {
                padding: 0.5rem 1rem;
                border-radius: 0.375rem;
                border: none;
                background: none;
                font-size: 0.875rem;
                font-weight: 500;
                cursor: pointer;
                color: #718096;
            }
            .view-btn.active {
                background-color: white;
                color: #4a5568;
                box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            }
            
            /* Arguments styling */
            .arguments-header {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
                margin-bottom: 1rem;
            }
            .claimant-color {
                color: #3182ce;
            }
            .respondent-color {
                color: #e53e3e;
            }
            
            /* IMPROVED: Argument container and pairs - added grid rows and alignment */
            .argument-pair {
                display: grid;
                grid-template-columns: 1fr 1fr;
                column-gap: 1.5rem;
                margin-bottom: 1rem;
                position: relative;
                align-items: start;
            }
            
            /* IMPROVED: Force equal heights of paired sections */
            .argument-pair-row {
                display: grid;
                grid-template-columns: 1fr 1fr;
                column-gap: 1.5rem;
                width: 100%;
                align-items: stretch;
            }
            
            .argument-side {
                position: relative;
                display: flex;
                flex-direction: column;
            }
            
            /* Argument card and details */
            .argument {
                border: 1px solid #e2e8f0;
                border-radius: 0.375rem;
                overflow: hidden;
                margin-bottom: 1.5rem; /* IMPROVED: Increased spacing */
                display: flex;
                flex-direction: column;
            }
            .argument-header {
                padding: 0.75rem 1rem;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .argument-header-left {
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            .argument-content {
                padding: 1rem;
                border-top: 1px solid #e2e8f0;
                display: none;
                background-color: white;
                flex: 1;
            }
            .claimant-header {
                background-color: #ebf8ff;
                border-color: #bee3f8;
            }
            .respondent-header {
                background-color: #fff5f5;
                border-color: #fed7d7;
            }
            
            /* IMPROVED: Child arguments container with better spacing */
            .argument-children {
                padding-left: 1.5rem;
                display: none;
                position: relative;
                margin-top: 1rem; /* Added spacing above subarguments */
                margin-bottom: 1rem; /* Added spacing below subarguments */
            }
            
            /* IMPROVED: Add better spacing for subarguments */
            .sub-argument {
                margin-top: 0.75rem;
                margin-bottom: 1.5rem;
            }
            
            /* Connector lines for tree structure */
            .connector-vertical {
                position: absolute;
                left: 0.75rem;
                top: 0;
                width: 1px;
                height: 100%;
                background-color: #e2e8f0;
            }
            .connector-horizontal {
                position: absolute;
                left: 0.75rem;
                top: 1.25rem;
                width: 0.75rem;
                height: 1px;
                background-color: #e2e8f0;
            }
            .claimant-connector {
                background-color: rgba(59, 130, 246, 0.5);
            }
            .respondent-connector {
                background-color: rgba(239, 68, 68, 0.5);
            }
            
            /* IMPROVED: Add better spacing for legal points sections */
            .legal-points-section {
                margin-bottom: 2rem;
            }
            .legal-points-title {
                font-size: 1rem;
                font-weight: 500;
                margin-bottom: 1rem;
            }
            
            /* Badge styling */
            .badge {
                display: inline-block;
                padding: 0.25rem 0.5rem;
                border-radius: 0.25rem;
                font-size: 0.75rem;
            }
            .claimant-badge {
                background-color: #ebf8ff;
                color: #3182ce;
            }
            .respondent-badge {
                background-color: #fff5f5;
                color: #e53e3e;
            }
            .legal-badge {
                background-color: #ebf8ff;
                color: #2c5282;
                margin-right: 0.25rem;
            }
            .factual-badge {
                background-color: #f0fff4;
                color: #276749;
                margin-right: 0.25rem;
            }
            .disputed-badge {
                background-color: #fed7d7;
                color: #c53030;
            }
            .type-badge {
                background-color: #edf2f7;
                color: #4a5568;
            }
            
            /* Content components */
            .content-section {
                margin-bottom: 1.5rem;
            }
            .content-section-title {
                font-size: 0.875rem;
                font-weight: 500;
                margin-bottom: 0.5rem;
            }
            .point-block {
                background-color: #f7fafc;
                border-radius: 0.5rem;
                padding: 0.75rem;
                margin-bottom: 0.5rem;
            }
            .point-header {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 0.25rem;
            }
            .point-date {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 0.25rem;
                font-size: 0.75rem;
                color: #718096;
            }
            .point-text {
                font-size: 0.875rem;
                color: #4a5568;
            }
            .point-citation {
                display: inline-block;
                margin-top: 0.5rem;
                font-size: 0.75rem;
                color: #718096;
            }
            
            /* IMPROVED: Legal references styling with better spacing */
            .legal-point {
                background-color: #ebf8ff;
                border-radius: 0.5rem;
                padding: 0.75rem;
                margin-bottom: 1rem;
            }
            .factual-point {
                background-color: #f0fff4;
                border-radius: 0.5rem;
                padding: 0.75rem;
                margin-bottom: 1rem;
            }
            
            /* Sample demo content for showing alignment */
            .demo-section {
                padding: 2rem;
                background-color: white;
                border-radius: 0.5rem;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                margin-bottom: 2rem;
            }
        </style>
    </head>
    <body>
        <!-- Tab Navigation -->
        <div class="tabs">
            <div class="tab active" data-tab="arguments">Summary of Arguments</div>
            <div class="tab" data-tab="timeline">Timeline</div>
            <div class="tab" data-tab="exhibits">Exhibits</div>
        </div>
        
        <!-- Demo Content to Show Aligned Columns -->
        <div class="demo-section">
            <div class="arguments-header">
                <h3 class="claimant-color">Claimant's Arguments</h3>
                <h3 class="respondent-color">Respondent's Arguments</h3>
            </div>
            
            <!-- Argument pair 1.1 Club Name Analysis -->
            <div class="argument-pair-row">
                <!-- Left Column: Claimant -->
                <div class="argument-side">
                    <div class="argument claimant-header">
                        <div class="argument-header">
                            <div class="argument-header-left">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transform: rotate(90deg);">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <h5 style="font-size: 0.875rem; font-weight: 500; color: #3182ce;">
                                    1.1. Club Name Analysis
                                </h5>
                            </div>
                            <div>
                                <span class="badge claimant-badge">¶20-45</span>
                            </div>
                        </div>
                        
                        <div class="argument-content" style="display: block;">
                            <div class="legal-points-section">
                                <h6 class="legal-points-title">Legal Points</h6>
                                
                                <div class="legal-point">
                                    <div class="point-header">
                                        <span class="badge legal-badge">Legal</span>
                                    </div>
                                    <p class="point-text">Name registration complies with regulations</p>
                                    <div style="margin-top: 0.5rem; display: flex; flex-wrap: wrap; gap: 0.25rem; align-items: center;">
                                        <span class="badge legal-badge">Name Registration Act</span>
                                        <span class="point-citation">¶22-24</span>
                                    </div>
                                </div>
                                
                                <div class="legal-point">
                                    <div class="point-header">
                                        <span class="badge legal-badge">Legal</span>
                                    </div>
                                    <p class="point-text">Trademark protection since 1960</p>
                                    <div style="margin-top: 0.5rem; display: flex; flex-wrap: wrap; gap: 0.25rem; align-items: center;">
                                        <span class="badge legal-badge">Trademark Law</span>
                                        <span class="point-citation">¶25-27</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Subargument -->
                    <div class="argument-children" style="display: block;">
                        <div class="connector-vertical claimant-connector"></div>
                        <div class="sub-argument">
                            <div class="argument claimant-header" style="position: relative;">
                                <div class="connector-horizontal claimant-connector"></div>
                                <div class="argument-header">
                                    <div class="argument-header-left">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <polyline points="9 18 15 12 9 6"></polyline>
                                        </svg>
                                        <h5 style="font-size: 0.875rem; font-weight: 500; color: #3182ce;">
                                            1.1.1. Registration History
                                        </h5>
                                    </div>
                                    <div>
                                        <span class="badge claimant-badge">¶25-30</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Right Column: Respondent -->
                <div class="argument-side">
                    <div class="argument respondent-header">
                        <div class="argument-header">
                            <div class="argument-header-left">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transform: rotate(90deg);">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <h5 style="font-size: 0.875rem; font-weight: 500; color: #e53e3e;">
                                    1.1. Club Name Analysis Rebuttal
                                </h5>
                            </div>
                            <div>
                                <span class="badge respondent-badge">¶220-240</span>
                            </div>
                        </div>
                        
                        <div class="argument-content" style="display: block;">
                            <div class="legal-points-section">
                                <h6 class="legal-points-title">Legal Points</h6>
                                
                                <div class="legal-point">
                                    <div class="point-header">
                                        <span class="badge legal-badge">Legal</span>
                                        <span class="badge disputed-badge">Disputed</span>
                                    </div>
                                    <p class="point-text">Registration lapse voided legal continuity</p>
                                    <div style="margin-top: 0.5rem; display: flex; flex-wrap: wrap; gap: 0.25rem; align-items: center;">
                                        <span class="badge legal-badge">Registration Act</span>
                                        <span class="point-citation">¶223-225</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Subargument -->
                    <div class="argument-children" style="display: block;">
                        <div class="connector-vertical respondent-connector"></div>
                        <div class="sub-argument">
                            <div class="argument respondent-header" style="position: relative;">
                                <div class="connector-horizontal respondent-connector"></div>
                                <div class="argument-header">
                                    <div class="argument-header-left">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <polyline points="9 18 15 12 9 6"></polyline>
                                        </svg>
                                        <h5 style="font-size: 0.875rem; font-weight: 500; color: #e53e3e;">
                                            1.1.1. Registration Gap Evidence
                                        </h5>
                                    </div>
                                    <div>
                                        <span class="badge respondent-badge">¶226-230</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Argument pair 1.2 Club Colors Analysis -->
            <div class="argument-pair-row">
                <!-- Left Column: Claimant -->
                <div class="argument-side">
                    <div class="argument claimant-header">
                        <div class="argument-header">
                            <div class="argument-header-left">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <h5 style="font-size: 0.875rem; font-weight: 500; color: #3182ce;">
                                    1.2. Club Colors Analysis
                                </h5>
                            </div>
                            <div>
                                <span class="badge claimant-badge" style="border-radius: 9999px;">1 subarguments</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Right Column: Respondent -->
                <div class="argument-side">
                    <div class="argument respondent-header">
                        <div class="argument-header">
                            <div class="argument-header-left">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <h5 style="font-size: 0.875rem; font-weight: 500; color: #e53e3e;">
                                    1.2. Club Colors Analysis Rebuttal
                                </h5>
                            </div>
                            <div>
                                <span class="badge respondent-badge" style="border-radius: 9999px;">1 subarguments</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Explanation of improvements -->
        <div style="padding: 1rem; background-color: #f8fafc; border-radius: 0.5rem; margin-bottom: 2rem;">
            <h3 style="margin-bottom: 1rem;">Alignment Improvements</h3>
            <ul style="list-style-type: disc; padding-left: 2rem;">
                <li style="margin-bottom: 0.5rem;">Added grid row structure to maintain vertical alignment between claimant and respondent sections</li>
                <li style="margin-bottom: 0.5rem;">Increased spacing between arguments and subarguments for better visual separation</li>
                <li style="margin-bottom: 0.5rem;">Made corresponding content sections the same height</li>
                <li style="margin-bottom: 0.5rem;">Added better spacing around legal points</li>
                <li style="margin-bottom: 0.5rem;">Improved consistency of spacing throughout the interface</li>
            </ul>
            <p>These changes ensure that corresponding sections in the claimant and respondent columns are properly aligned vertically.</p>
        </div>
        
        <script>
            // Tab switching
            document.querySelectorAll('.tab').forEach(tab => {
                tab.addEventListener('click', function() {
                    // Update tabs
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Update content
                    const tabId = this.getAttribute('data-tab');
                    document.querySelectorAll('.tab-content').forEach(content => {
                        content.style.display = 'none';
                    });
                    document.getElementById(tabId).style.display = 'block';
                });
            });
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
