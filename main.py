import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Create a single HTML component containing the full UI
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
        
        /* Card styling */
        .card {
            background-color: white;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            overflow: hidden;
            margin-bottom: 16px;
        }
        
        /* Argument grid layout */
        .arguments-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
        }
        
        /* Headers */
        .column-header {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 16px;
        }
        
        .section-header {
            font-size: 16px;
            font-weight: 500;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid #e2e8f0;
        }
        
        /* Argument styling */
        .argument {
            margin-bottom: 16px;
            border-radius: 8px;
            overflow: hidden;
        }
        
        .argument-header {
            padding: 12px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            position: relative;
        }
        
        .argument-header-left {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .argument-title {
            font-size: 14px;
            font-weight: 500;
        }
        
        .argument-content {
            padding: 16px;
            border-top: 1px solid rgba(0, 0, 0, 0.1);
        }
        
        /* Claimant/Respondent specific styling */
        .claimant {
            --primary-color: #3182ce;
            --light-color: #ebf8ff;
            --border-color: #bee3f8;
        }
        
        .respondent {
            --primary-color: #e53e3e;
            --light-color: #fff5f5;
            --border-color: #fed7d7;
        }
        
        .claimant .argument-header {
            background-color: var(--light-color);
            border: 1px solid var(--border-color);
        }
        
        .respondent .argument-header {
            background-color: var(--light-color);
            border: 1px solid var(--border-color);
        }
        
        .claimant .argument-title {
            color: var(--primary-color);
        }
        
        .respondent .argument-title {
            color: var(--primary-color);
        }
        
        /* Subargument styling */
        .subargument-container {
            margin-left: 20px;
            position: relative;
            border-left: 1px solid var(--border-color);
            padding-left: 16px;
            margin-top: 12px;
        }
        
        .subargument {
            margin-bottom: 12px;
        }
        
        .subargument-header {
            padding: 10px 12px;
            border-radius: 6px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: var(--light-color);
            border: 1px solid var(--border-color);
        }
        
        .subargument-title {
            font-size: 14px;
            font-weight: 500;
            color: var(--primary-color);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .subargument-content {
            padding: 12px;
            border: 1px solid var(--border-color);
            border-top: none;
            border-radius: 0 0 6px 6px;
            background-color: white;
        }
        
        /* Make connector lines between parent and child */
        .connector {
            position: absolute;
            width: 16px;
            height: 1px;
            background-color: var(--border-color);
            left: 0;
            top: 20px;
            transform: translateX(-16px);
        }
        
        /* Badges */
        .badge {
            display: inline-block;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .para-badge {
            color: var(--primary-color);
            background-color: rgba(0, 0, 0, 0.05);
        }
        
        .count-badge {
            color: var(--primary-color);
            background-color: var(--light-color);
            border-radius: 9999px;
        }
        
        .disputed-badge {
            background-color: #fed7d7;
            color: #c53030;
        }
        
        .legal-badge {
            background-color: #ebf8ff;
            color: #2c5282;
        }
        
        /* Legal points section */
        .legal-points-container {
            margin-bottom: 24px;
        }
        
        .legal-point {
            background-color: #ebf8ff;
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 12px;
        }
        
        .legal-point-content {
            margin: 8px 0;
            font-size: 14px;
        }
        
        .legal-point-footer {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 8px;
        }
        
        /* Chevron styling */
        .chevron {
            transition: transform 0.2s ease;
        }
        
        .chevron.expanded {
            transform: rotate(90deg);
        }
    </style>
</head>
<body>
    <div class="arguments-container">
        <!-- Claimant Side -->
        <div class="claimant">
            <h2 class="column-header" style="color: #3182ce;">Claimant's Arguments</h2>
            
            <!-- First main argument -->
            <div class="argument">
                <div class="argument-header" onclick="toggleArgument('claimant-1', 'respondent-1')">
                    <div class="argument-header-left">
                        <svg class="chevron" width="16" height="16" viewBox="0 0 24 24" id="chevron-claimant-1" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6"></polyline>
                        </svg>
                        <span class="argument-title">1. Club Name Analysis</span>
                    </div>
                    <span class="badge para-badge">¶20-45</span>
                </div>
                
                <div class="argument-content" id="content-claimant-1" style="display: none;">
                    <h4 class="section-header">Legal Points</h4>
                    
                    <div class="legal-point">
                        <div style="display: flex; gap: 4px;">
                            <span class="badge legal-badge">Legal</span>
                        </div>
                        <p class="legal-point-content">Name registration complies with regulations</p>
                        <div class="legal-point-footer">
                            <span class="badge legal-badge">Name Registration Act</span>
                            <span class="badge para-badge">¶22-24</span>
                        </div>
                    </div>
                    
                    <div class="legal-point">
                        <div style="display: flex; gap: 4px;">
                            <span class="badge legal-badge">Legal</span>
                        </div>
                        <p class="legal-point-content">Trademark protection since 1960</p>
                        <div class="legal-point-footer">
                            <span class="badge legal-badge">Trademark Law</span>
                            <span class="badge para-badge">¶25-27</span>
                        </div>
                    </div>
                    
                    <div class="subargument-container" id="children-claimant-1">
                        <div class="subargument">
                            <div class="connector"></div>
                            <div class="subargument-header" onclick="toggleArgument('claimant-1.1', 'respondent-1.1')">
                                <div class="subargument-title">
                                    <svg class="chevron" width="16" height="16" viewBox="0 0 24 24" id="chevron-claimant-1.1" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    1.1.1. Registration History
                                </div>
                                <span class="badge para-badge">¶25-30</span>
                            </div>
                            <div class="subargument-content" id="content-claimant-1.1" style="display: none;">
                                Registration history details would appear here.
                            </div>
                        </div>
                        
                        <div class="subargument">
                            <div class="connector"></div>
                            <div class="subargument-header" onclick="toggleArgument('claimant-1.2', 'respondent-1.2')">
                                <div class="subargument-title">
                                    <svg class="chevron" width="16" height="16" viewBox="0 0 24 24" id="chevron-claimant-1.2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    1.2. Club Colors Analysis
                                </div>
                                <span class="badge count-badge">1 subargument</span>
                            </div>
                            <div class="subargument-content" id="content-claimant-1.2" style="display: none;">
                                Club colors analysis details would appear here.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Respondent Side -->
        <div class="respondent">
            <h2 class="column-header" style="color: #e53e3e;">Respondent's Arguments</h2>
            
            <!-- First main argument -->
            <div class="argument">
                <div class="argument-header" onclick="toggleArgument('respondent-1', 'claimant-1')">
                    <div class="argument-header-left">
                        <svg class="chevron" width="16" height="16" viewBox="0 0 24 24" id="chevron-respondent-1" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6"></polyline>
                        </svg>
                        <span class="argument-title">1. Club Name Analysis Rebuttal</span>
                    </div>
                    <span class="badge para-badge">¶220-240</span>
                </div>
                
                <div class="argument-content" id="content-respondent-1" style="display: none;">
                    <h4 class="section-header">Legal Points</h4>
                    
                    <div class="legal-point">
                        <div style="display: flex; gap: 4px;">
                            <span class="badge legal-badge">Legal</span>
                            <span class="badge disputed-badge">Disputed</span>
                        </div>
                        <p class="legal-point-content">Registration lapse voided legal continuity</p>
                        <div class="legal-point-footer">
                            <span class="badge legal-badge">Registration Act</span>
                            <span class="badge para-badge">¶223-225</span>
                        </div>
                    </div>
                    
                    <div class="subargument-container" id="children-respondent-1">
                        <div class="subargument">
                            <div class="connector"></div>
                            <div class="subargument-header" onclick="toggleArgument('respondent-1.1', 'claimant-1.1')">
                                <div class="subargument-title">
                                    <svg class="chevron" width="16" height="16" viewBox="0 0 24 24" id="chevron-respondent-1.1" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    1.1.1. Registration Gap Evidence
                                </div>
                                <span class="badge para-badge">¶226-230</span>
                            </div>
                            <div class="subargument-content" id="content-respondent-1.1" style="display: none;">
                                Registration gap evidence details would appear here.
                            </div>
                        </div>
                        
                        <div class="subargument">
                            <div class="connector"></div>
                            <div class="subargument-header" onclick="toggleArgument('respondent-1.2', 'claimant-1.2')">
                                <div class="subargument-title">
                                    <svg class="chevron" width="16" height="16" viewBox="0 0 24 24" id="chevron-respondent-1.2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="9 18 15 12 9 6"></polyline>
                                    </svg>
                                    1.2. Club Colors Analysis Rebuttal
                                </div>
                                <span class="badge count-badge">1 subargument</span>
                            </div>
                            <div class="subargument-content" id="content-respondent-1.2" style="display: none;">
                                Club colors analysis rebuttal details would appear here.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Toggle argument expansion
        function toggleArgument(id, pairedId) {
            // Toggle this argument
            const contentEl = document.getElementById(`content-${id}`);
            const chevronEl = document.getElementById(`chevron-${id}`);
            const childrenEl = document.getElementById(`children-${id}`);
            
            const isExpanded = contentEl.style.display === 'block';
            contentEl.style.display = isExpanded ? 'none' : 'block';
            
            if (chevronEl) {
                if (isExpanded) {
                    chevronEl.classList.remove('expanded');
                } else {
                    chevronEl.classList.add('expanded');
                }
            }
            
            // Toggle paired argument
            const pairedContentEl = document.getElementById(`content-${pairedId}`);
            const pairedChevronEl = document.getElementById(`chevron-${pairedId}`);
            const pairedChildrenEl = document.getElementById(`children-${pairedId}`);
            
            if (pairedContentEl) {
                pairedContentEl.style.display = contentEl.style.display;
            }
            
            if (pairedChevronEl) {
                if (isExpanded) {
                    pairedChevronEl.classList.remove('expanded');
                } else {
                    pairedChevronEl.classList.add('expanded');
                }
            }
        }
    </script>
</body>
</html>
"""
    
# Title
st.title("Legal Arguments Analysis")
    
# Render the HTML in Streamlit
components.html(html_content, height=800, scrolling=True)
