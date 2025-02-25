import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Get argument data
def get_argument_data():
    # Data structure remains the same - abbreviated for clarity
    return {
        "claimantArgs": {...},
        "respondentArgs": {...},
        "topics": [...]
    }

def get_timeline_data():
    # Timeline data structure remains the same
    return [...]

def get_exhibits_data():
    # Exhibits data structure remains the same
    return [...]

# Main app
def main():
    # Title
    st.title("Legal Arguments Analysis")
    
    # Create basic HTML structure with embedded JavaScript that will render dynamically
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Base styles */
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                margin: 0;
                padding: 0;
                color: #333;
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
            .tab.active {
                color: #3182ce;
                border-bottom: 2px solid #3182ce;
            }
            
            /* Tab content */
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
                box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            }
            
            /* Column headers */
            .column-headers {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
                margin-bottom: 1rem;
            }
            .claimant-color { color: #3182ce; }
            .respondent-color { color: #e53e3e; }
            
            /* Argument containers */
            .argument-pair-container {
                margin-bottom: 1rem;
            }
            .argument-pair {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
            }
            .child-arguments {
                margin-left: 1.5rem;
                padding-left: 0.5rem;
                border-left: 1px solid #d1d5db;
                margin-top: 0.5rem;
                margin-bottom: 0.5rem;
                display: none;
            }
            .argument-pair .claimant-side .child-arguments {
                border-left-color: rgba(59, 130, 246, 0.5);
            }
            .argument-pair .respondent-side .child-arguments {
                border-left-color: rgba(239, 68, 68, 0.5);
            }
            
            /* Argument cards */
            .argument-card {
                border-radius: 0.375rem;
                overflow: hidden;
                margin-bottom: 0.5rem;
                border: 1px solid #e2e8f0;
            }
            .argument-header {
                padding: 0.75rem 1rem;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .header-left {
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            .argument-content {
                padding: 1rem;
                border-top: 1px solid #e2e8f0;
                display: none;
                background-color: white;
            }
            
            /* Claimant vs Respondent styling */
            .claimant-header {
                background-color: #ebf8ff;
                border-color: #bee3f8;
            }
            .respondent-header {
                background-color: #fff5f5;
                border-color: #fed7d7;
            }
            
            /* Badge styling */
            .badge {
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
            .round-badge {
                border-radius: 9999px;
            }
            
            /* Chevron icon */
            .chevron {
                transition: transform 0.2s ease;
            }
            
            /* Content blocks */
            .content-section {
                margin-bottom: 1rem;
            }
            .content-title {
                font-size: 0.875rem;
                font-weight: 500;
                margin-bottom: 0.5rem;
            }
            
            /* Overview points */
            .overview-block {
                background-color: #f7fafc;
                border-radius: 0.5rem;
                padding: 1rem;
                margin-bottom: 1rem;
            }
            .overview-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 0.5rem;
            }
            .overview-list {
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
            }
            .overview-item {
                display: flex;
                align-items: flex-start;
                gap: 0.5rem;
            }
            .overview-bullet {
                width: 6px;
                height: 6px;
                border-radius: 50%;
                background-color: #3182ce;
                margin-top: 0.5rem;
            }
            
            /* Point blocks */
            .point-block {
                border-radius: 0.5rem;
                padding: 0.75rem;
                margin-bottom: 0.5rem;
            }
            .legal-point {
                background-color: #ebf8ff;
            }
            .factual-point {
                background-color: #f0fff4;
            }
            .point-header {
                display: flex;
                align-items: center;
                flex-wrap: wrap;
                gap: 0.5rem;
                margin-bottom: 0.5rem;
            }
            .point-text {
                font-size: 0.875rem;
                color: #4a5568;
                margin-bottom: 0.5rem;
            }
            .point-citation {
                font-size: 0.75rem;
                color: #718096;
            }
            
            /* Point badges */
            .legal-badge {
                background-color: #ebf8ff;
                color: #2c5282;
            }
            .factual-badge {
                background-color: #f0fff4;
                color: #276749;
            }
            .disputed-badge {
                background-color: #fed7d7;
                color: #c53030;
            }
            
            /* Evidence and case law */
            .reference-block {
                background-color: #f7fafc;
                border-radius: 0.5rem;
                padding: 0.75rem;
                margin-bottom: 0.5rem;
            }
            .reference-header {
                display: flex;
                justify-content: space-between;
                margin-bottom: 0.5rem;
            }
            .reference-title {
                font-size: 0.875rem;
                font-weight: 500;
            }
            .reference-summary {
                font-size: 0.75rem;
                color: #718096;
                margin-bottom: 0.5rem;
            }
            .citation-tag {
                background-color: #edf2f7;
                color: #4a5568;
                padding: 0.125rem 0.375rem;
                border-radius: 0.25rem;
                font-size: 0.75rem;
                margin-right: 0.25rem;
            }
            
            /* Horizontal connector */
            .horizontal-connector {
                display: flex;
                margin-left: -1rem;
                margin-bottom: 0.5rem;
            }
            .connector-line {
                width: 1rem;
                height: 1px;
                background-color: #d1d5db;
                position: relative;
                top: 0.75rem;
            }
            .claimant-side .connector-line {
                background-color: rgba(59, 130, 246, 0.5);
            }
            .respondent-side .connector-line {
                background-color: rgba(239, 68, 68, 0.5);
            }
            
            /* Topic view */
            .topic-section {
                margin-bottom: 2rem;
            }
            .topic-title {
                font-size: 1.25rem;
                font-weight: 600;
                color: #2d3748;
                margin-bottom: 0.25rem;
            }
            .topic-description {
                font-size: 0.875rem;
                color: #718096;
                margin-bottom: 1rem;
            }
            
            /* Timeline table */
            .timeline-controls {
                display: flex;
                justify-content: space-between;
                margin-bottom: 1rem;
            }
            .search-container {
                position: relative;
                display: flex;
                gap: 0.5rem;
            }
            .search-input {
                padding: 0.625rem 1rem 0.625rem 2.5rem;
                border: 1px solid #e2e8f0;
                border-radius: 0.375rem;
                width: 16rem;
            }
            .search-icon {
                position: absolute;
                left: 12px;
                top: 11px;
            }
            .action-btn {
                padding: 0.5rem 1rem;
                background-color: white;
                border: 1px solid #e2e8f0;
                border-radius: 0.375rem;
                font-size: 0.875rem;
                cursor: pointer;
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
            }
            .data-table {
                width: 100%;
                border-collapse: collapse;
                border: 1px solid #e2e8f0;
                border-radius: 0.375rem;
                overflow: hidden;
            }
            .data-table th {
                background-color: #f7fafc;
                text-align: left;
                padding: 0.75rem 1rem;
                font-size: 0.875rem;
                font-weight: 500;
                color: #4a5568;
                border-bottom: 1px solid #e2e8f0;
            }
            .data-table td {
                padding: 0.75rem 1rem;
                font-size: 0.875rem;
                border-bottom: 1px solid #e2e8f0;
            }
            .data-table tr.disputed {
                background-color: #fff5f5;
            }
            .disputed-text {
                color: #c53030;
            }
            .undisputed-text {
                color: #2f855a;
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
        
        <!-- Arguments Tab -->
        <div id="arguments" class="tab-content active">
            <div class="view-toggle">
                <div class="view-toggle-container">
                    <button class="view-btn active" data-view="standard">Standard View</button>
                    <button class="view-btn" data-view="topic">Topic View</button>
                </div>
            </div>
            
            <!-- Standard View -->
            <div id="standard-view" class="view-content">
                <div class="column-headers">
                    <h3 class="claimant-color">Claimant's Arguments</h3>
                    <h3 class="respondent-color">Respondent's Arguments</h3>
                </div>
                <div id="arguments-container"></div>
            </div>
            
            <!-- Topic View -->
            <div id="topic-view" class="view-content" style="display: none;">
                <div id="topics-container"></div>
            </div>
        </div>
        
        <!-- Timeline Tab -->
        <div id="timeline" class="tab-content">
            <div class="actions-bar" style="display: flex; justify-content: flex-end; margin-bottom: 1rem;">
                <button class="action-btn">Copy</button>
                <button class="action-btn" style="margin-left: 0.5rem;">Export Data</button>
            </div>
            
            <div class="timeline-controls">
                <div class="search-container">
                    <div style="position: relative;">
                        <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                        <input type="text" id="timeline-search" class="search-input" placeholder="Search events...">
                    </div>
                    <button class="action-btn">Filter</button>
                </div>
                <div>
                    <label style="display: flex; align-items: center; gap: 0.5rem;">
                        <input type="checkbox" id="disputed-only" style="width: 1rem; height: 1rem;">
                        <span style="font-size: 0.875rem;">Disputed events only</span>
                    </label>
                </div>
            </div>
            
            <table id="timeline-table" class="data-table">
                <thead>
                    <tr>
                        <th>DATE</th>
                        <th>APPELLANT'S VERSION</th>
                        <th>RESPONDENT'S VERSION</th>
                        <th>STATUS</th>
                    </tr>
                </thead>
                <tbody id="timeline-body"></tbody>
            </table>
        </div>
        
        <!-- Exhibits Tab -->
        <div id="exhibits" class="tab-content">
            <div class="actions-bar" style="display: flex; justify-content: flex-end; margin-bottom: 1rem;">
                <button class="action-btn">Copy</button>
                <button class="action-btn" style="margin-left: 0.5rem;">Export Data</button>
            </div>
            
            <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                <div style="position: relative;">
                    <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a0aec0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    <input type="text" id="exhibits-search" class="search-input" placeholder="Search exhibits...">
                </div>
                
                <select id="party-filter" style="padding: 0.625rem 1rem; border: 1px solid #e2e8f0; border-radius: 0.375rem; background-color: white;">
                    <option value="All Parties">All Parties</option>
                    <option value="Appellant">Appellant</option>
                    <option value="Respondent">Respondent</option>
                </select>
                
                <select id="type-filter" style="padding: 0.625rem 1rem; border: 1px solid #e2e8f0; border-radius: 0.375rem; background-color: white;">
                    <option value="All Types">All Types</option>
                </select>
            </div>
            
            <table id="exhibits-table" class="data-table">
                <thead>
                    <tr>
                        <th>EXHIBIT ID</th>
                        <th>PARTY</th>
                        <th>TITLE</th>
                        <th>TYPE</th>
                        <th>SUMMARY</th>
                        <th style="text-align: right;">ACTIONS</th>
                    </tr>
                </thead>
                <tbody id="exhibits-body"></tbody>
            </table>
        </div>
        
        <script id="init-script">
            // Initialize with the provided data
            const argsData = {
                "claimantArgs": {
                    "1": {
                        "id": "1",
                        "title": "Sporting Succession",
                        "paragraphs": "15-18",
                        "overview": {
                            "points": [
                                "Analysis of multiple established criteria",
                                "Focus on continuous use of identifying elements",
                                "Public recognition assessment"
                            ],
                            "paragraphs": "15-16"
                        },
                        "legalPoints": [
                            {
                                "point": "CAS jurisprudence establishes criteria for sporting succession",
                                "isDisputed": false,
                                "regulations": ["CAS 2016/A/4576"],
                                "paragraphs": "15-17"
                            }
                        ],
                        "factualPoints": [
                            {
                                "point": "Continuous operation under same name since 1950",
                                "date": "1950-present",
                                "isDisputed": false,
                                "paragraphs": "18-19"
                            }
                        ],
                        "evidence": [
                            {
                                "id": "C-1",
                                "title": "Historical Registration Documents",
                                "summary": "Official records showing continuous name usage",
                                "citations": ["20", "21", "24"]
                            }
                        ],
                        "caseLaw": [
                            {
                                "caseNumber": "CAS 2016/A/4576",
                                "title": "Criteria for sporting succession",
                                "relevance": "Establishes key factors for succession",
                                "paragraphs": "45-48",
                                "citedParagraphs": ["45", "46", "47"]
                            }
                        ],
                        "children": {
                            "1.1": {
                                "id": "1.1",
                                "title": "Club Name Analysis",
                                "paragraphs": "20-45",
                                "overview": {
                                    "points": [
                                        "Historical continuity of name usage",
                                        "Legal protection of naming rights",
                                        "Public recognition of club name"
                                    ],
                                    "paragraphs": "20-21"
                                },
                                "legalPoints": [
                                    {
                                        "point": "Name registration complies with regulations",
                                        "isDisputed": false,
                                        "regulations": ["Name Registration Act"],
                                        "paragraphs": "22-24"
                                    },
                                    {
                                        "point": "Trademark protection since 1960",
                                        "isDisputed": false,
                                        "regulations": ["Trademark Law"],
                                        "paragraphs": "25-27"
                                    }
                                ],
                                "children": {
                                    "1.1.1": {
                                        "id": "1.1.1",
                                        "title": "Registration History",
                                        "paragraphs": "25-30",
                                        "factualPoints": [
                                            {
                                                "point": "Initial registration in 1950",
                                                "date": "1950",
                                                "isDisputed": false,
                                                "paragraphs": "25-26"
                                            },
                                            {
                                                "point": "Brief administrative gap in 1975-1976",
                                                "date": "1975-1976",
                                                "isDisputed": true,
                                                "source": "Respondent",
                                                "paragraphs": "29-30"
                                            }
                                        ],
                                        "evidence": [
                                            {
                                                "id": "C-2",
                                                "title": "Registration Records",
                                                "summary": "Official documentation of registration history",
                                                "citations": ["25", "26", "28"]
                                            }
                                        ],
                                        "children": {}
                                    }
                                }
                            },
                            "1.2": {
                                "id": "1.2",
                                "title": "Club Colors Analysis",
                                "paragraphs": "46-65",
                                "overview": {
                                    "points": [
                                        "Consistent use of club colors",
                                        "Minor variations analysis",
                                        "Color trademark protection"
                                    ],
                                    "paragraphs": "46-47"
                                },
                                "legalPoints": [
                                    {
                                        "point": "Color trademark registration valid since 1960",
                                        "isDisputed": false,
                                        "regulations": ["Trademark Act"],
                                        "paragraphs": "48-50"
                                    }
                                ],
                                "factualPoints": [
                                    {
                                        "point": "Consistent use of blue and white since founding",
                                        "date": "1950-present",
                                        "isDisputed": true,
                                        "source": "Respondent",
                                        "paragraphs": "51-52"
                                    }
                                ],
                                "evidence": [
                                    {
                                        "id": "C-4",
                                        "title": "Historical Photographs",
                                        "summary": "Visual evidence of consistent color usage",
                                        "citations": ["53", "54", "55"]
                                    }
                                ],
                                "children": {
                                    "1.2.1": {
                                        "id": "1.2.1",
                                        "title": "Color Variations Analysis",
                                        "paragraphs": "56-60",
                                        "factualPoints": [
                                            {
                                                "point": "Minor shade variations do not affect continuity",
                                                "date": "1970-1980",
                                                "isDisputed": false,
                                                "paragraphs": "56-57"
                                            },
                                            {
                                                "point": "Temporary third color addition in 1980s",
                                                "date": "1982-1988",
                                                "isDisputed": false,
                                                "paragraphs": "58-59"
                                            }
                                        ],
                                        "children": {}
                                    }
                                }
                            }
                        }
                    },
                    "2": {
                        "id": "2",
                        "title": "Doping Violation Chain of Custody",
                        "paragraphs": "70-125",
                        "overview": {
                            "points": [
                                "Analysis of sample collection and handling procedures",
                                "Evaluation of laboratory testing protocols",
                                "Assessment of chain of custody documentation"
                            ],
                            "paragraphs": "70-72"
                        },
                        "legalPoints": [
                            {
                                "point": "WADA Code Article 5 establishes procedural requirements",
                                "isDisputed": false,
                                "regulations": ["WADA Code 2021", "International Standard for Testing"],
                                "paragraphs": "73-75"
                            }
                        ],
                        "children": {}
                    }
                },
                "respondentArgs": {
                    "1": {
                        "id": "1",
                        "title": "Sporting Succession Rebuttal",
                        "paragraphs": "200-218",
                        "overview": {
                            "points": [
                                "Challenge to claimed continuity of operations",
                                "Analysis of discontinuities in club operations",
                                "Dispute over public recognition factors"
                            ],
                            "paragraphs": "200-202"
                        },
                        "legalPoints": [
                            {
                                "point": "CAS jurisprudence requires operational continuity not merely identification",
                                "isDisputed": false,
                                "regulations": ["CAS 2017/A/5465"],
                                "paragraphs": "203-205"
                            }
                        ],
                        "factualPoints": [
                            {
                                "point": "Operations ceased between 1975-1976",
                                "date": "1975-1976",
                                "isDisputed": true,
                                "source": "Claimant",
                                "paragraphs": "206-207"
                            }
                        ],
                        "evidence": [
                            {
                                "id": "R-1",
                                "title": "Federation Records",
                                "summary": "Records showing non-participation in 1975-1976 season",
                                "citations": ["208", "209", "210"]
                            }
                        ],
                        "caseLaw": [
                            {
                                "caseNumber": "CAS 2017/A/5465",
                                "title": "Operational continuity requirement",
                                "relevance": "Establishes primacy of operational continuity",
                                "paragraphs": "211-213",
                                "citedParagraphs": ["212"]
                            }
                        ],
                        "children": {
                            "1.1": {
                                "id": "1.1",
                                "title": "Club Name Analysis Rebuttal",
                                "paragraphs": "220-240",
                                "overview": {
                                    "points": [
                                        "Name registration discontinuities",
                                        "Trademark ownership gaps",
                                        "Analysis of public confusion"
                                    ],
                                    "paragraphs": "220-222"
                                },
                                "legalPoints": [
                                    {
                                        "point": "Registration lapse voided legal continuity",
                                        "isDisputed": true,
                                        "regulations": ["Registration Act"],
                                        "paragraphs": "223-225"
                                    }
                                ],
                                "children": {
                                    "1.1.1": {
                                        "id": "1.1.1",
                                        "title": "Registration Gap Evidence",
                                        "paragraphs": "226-230",
                                        "factualPoints": [
                                            {
                                                "point": "Registration formally terminated on April 30, 1975",
                                                "date": "April 30, 1975",
                                                "isDisputed": false,
                                                "paragraphs": "226-227"
                                            },
                                            {
                                                "point": "New entity registered on September 15, 1976",
                                                "date": "September 15, 1976",
                                                "isDisputed": false,
                                                "paragraphs": "228-229"
                                            }
                                        ],
                                        "evidence": [
                                            {
                                                "id": "R-2",
                                                "title": "Termination Certificate",
                                                "summary": "Official documentation of registration termination",
                                                "citations": ["226", "227"]
                                            }
                                        ],
                                        "children": {
                                            "1.1.1.1": {
                                                "id": "1.1.1.1",
                                                "title": "Legal Entity Discontinuity",
                                                "paragraphs": "231-235",
                                                "legalPoints": [
                                                    {
                                                        "point": "New registration created distinct legal entity",
                                                        "isDisputed": true,
                                                        "regulations": ["Company Law §15"],
                                                        "paragraphs": "231-232"
                                                    }
                                                ],
                                                "factualPoints": [
                                                    {
                                                        "point": "Different ownership structure post-1976",
                                                        "date": "1976",
                                                        "isDisputed": false,
                                                        "paragraphs": "233-234"
                                                    }
                                                ],
                                                "caseLaw": [
                                                    {
                                                        "caseNumber": "CAS 2018/A/5618",
                                                        "title": "Legal entity identity case",
                                                        "relevance": "Registration gap creating new legal entity",
                                                        "paragraphs": "235",
                                                        "citedParagraphs": ["235"]
                                                    }
                                                ],
                                                "children": {}
                                            }
                                        }
                                    }
                                }
                            },
                            "1.2": {
                                "id": "1.2",
                                "title": "Club Colors Analysis Rebuttal",
                                "paragraphs": "241-249",
                                "overview": {
                                    "points": [
                                        "Significant color variations",
                                        "Trademark registration gaps",
                                        "Multiple competing color claims"
                                    ],
                                    "paragraphs": "241-242"
                                },
                                "legalPoints": [
                                    {
                                        "point": "Color trademark lapsed during 1975-1976",
                                        "isDisputed": false,
                                        "regulations": ["Trademark Act"],
                                        "paragraphs": "243-244"
                                    }
                                ],
                                "factualPoints": [
                                    {
                                        "point": "Significant color scheme change in 1976",
                                        "date": "1976",
                                        "isDisputed": true,
                                        "source": "Claimant",
                                        "paragraphs": "245-246"
                                    }
                                ],
                                "evidence": [
                                    {
                                        "id": "R-4",
                                        "title": "Historical Photographs Comparison",
                                        "summary": "Visual evidence of color scheme changes",
                                        "citations": ["245", "246", "247"]
                                    }
                                ],
                                "children": {
                                    "1.2.1": {
                                        "id": "1.2.1",
                                        "title": "Color Symbolism Analysis",
                                        "paragraphs": "247-249",
                                        "factualPoints": [
                                            {
                                                "point": "Pre-1976 colors represented original city district",
                                                "date": "1950-1975",
                                                "isDisputed": false,
                                                "paragraphs": "247"
                                            },
                                            {
                                                "point": "Post-1976 colors represented new ownership region",
                                                "date": "1976-present",
                                                "isDisputed": true,
                                                "source": "Claimant",
                                                "paragraphs": "248-249"
                                            }
                                        ],
                                        "children": {}
                                    }
                                }
                            }
                        }
                    },
                    "2": {
                        "id": "2",
                        "title": "Doping Chain of Custody Defense",
                        "paragraphs": "250-290",
                        "overview": {
                            "points": [
                                "Defense of sample collection procedures",
                                "Validation of laboratory testing protocols",
                                "Completeness of documentation"
                            ],
                            "paragraphs": "250-252"
                        },
                        "legalPoints": [
                            {
                                "point": "Minor procedural deviations do not invalidate results",
                                "isDisputed": false,
                                "regulations": ["CAS 2019/A/6148"],
                                "paragraphs": "253-255"
                            }
                        ],
                        "children": {}
                    }
                },
                "topics": [
                    {
                        "id": "topic-1",
                        "title": "Sporting Succession and Identity",
                        "description": "Questions of club identity, continuity, and succession rights",
                        "argumentIds": ["1"]
                    },
                    {
                        "id": "topic-2",
                        "title": "Doping Violation and Chain of Custody",
                        "description": "Issues related to doping test procedures and evidence handling",
                        "argumentIds": ["2"]
                    }
                ]
            };
            
            const timelineData = [
                {
                    "date": "2023-01-15",
                    "appellantVersion": "Contract signed with Club",
                    "respondentVersion": "—",
                    "status": "Undisputed"
                },
                {
                    "date": "2023-03-20",
                    "appellantVersion": "Player received notification of exclusion from team",
                    "respondentVersion": "—",
                    "status": "Undisputed"
                },
                {
                    "date": "2023-03-22",
                    "appellantVersion": "Player requested explanation",
                    "respondentVersion": "—",
                    "status": "Undisputed"
                },
                {
                    "date": "2023-04-01",
                    "appellantVersion": "Player sent termination letter",
                    "respondentVersion": "—",
                    "status": "Undisputed"
                },
                {
                    "date": "2023-04-05",
                    "appellantVersion": "—",
                    "respondentVersion": "Club rejected termination as invalid",
                    "status": "Undisputed"
                },
                {
                    "date": "2023-04-10",
                    "appellantVersion": "Player was denied access to training facilities",
                    "respondentVersion": "—",
                    "status": "Disputed"
                },
                {
                    "date": "2023-04-15",
                    "appellantVersion": "—",
                    "respondentVersion": "Club issued warning letter",
                    "status": "Undisputed"
                },
                {
                    "date": "2023-05-01",
                    "appellantVersion": "Player filed claim with FIFA",
                    "respondentVersion": "—",
                    "status": "Undisputed"
                }
            ];
            
            const exhibitsData = [
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
            ];

            // Keep track of expanded arguments
            const expandedStates = {};
            
            // Render overview points
            function renderOverviewPoints(overview) {
                if (!overview || !overview.points || overview.points.length === 0) {
                    return '';
                }
                
                const pointsHtml = overview.points.map(point => `
                    <div class="overview-item">
                        <div class="overview-bullet"></div>
                        <span>${point}</span>
                    </div>
                `).join('');
                
                return `
                <div class="overview-block">
                    <div class="overview-header">
                        <div class="content-title">Key Points</div>
                        <span class="badge claimant-badge">¶${overview.paragraphs}</span>
                    </div>
                    <div class="overview-list">
                        ${pointsHtml}
                    </div>
                </div>
                `;
            }
            
            // Render legal points
            function renderLegalPoints(points) {
                if (!points || points.length === 0) {
                    return '';
                }
                
                const pointsHtml = points.map(point => {
                    const disputed = point.isDisputed 
                        ? `<span class="badge disputed-badge">Disputed</span>` 
                        : '';
                    
                    const regulations = point.regulations 
                        ? point.regulations.map(reg => `<span class="badge legal-badge">${reg}</span>`).join('') 
                        : '';
                    
                    return `
                    <div class="point-block legal-point">
                        <div class="point-header">
                            <span class="badge legal-badge">Legal</span>
                            ${disputed}
                        </div>
                        <p class="point-text">${point.point}</p>
                        <div style="display: flex; flex-wrap: wrap; gap: 0.25rem; align-items: center;">
                            ${regulations}
                            <span class="point-citation">¶${point.paragraphs}</span>
                        </div>
                    </div>
                    `;
                }).join('');
                
                return `
                <div class="content-section">
                    <div class="content-title">Legal Points</div>
                    ${pointsHtml}
                </div>
                `;
            }
            
            // Render factual points
            function renderFactualPoints(points) {
                if (!points || points.length === 0) {
                    return '';
                }
                
                const pointsHtml = points.map(point => {
                    const disputed = point.isDisputed 
                        ? `<span class="badge disputed-badge">Disputed by ${point.source || ''}</span>` 
                        : '';
                    
                    return `
                    <div class="point-block factual-point">
                        <div class="point-header">
                            <span class="badge factual-badge">Factual</span>
                            ${disputed}
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem; font-size: 0.75rem; color: #718096;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                <line x1="3" y1="10" x2="21" y2="10"></line>
                            </svg>
                            ${point.date}
                        </div>
                        <p class="point-text">${point.point}</p>
                        <span class="point-citation">¶${point.paragraphs}</span>
                    </div>
                    `;
                }).join('');
                
                return `
                <div class="content-section">
                    <div class="content-title">Factual Points</div>
                    ${pointsHtml}
                </div>
                `;
            }
            
            // Render evidence
            function renderEvidence(evidence) {
                if (!evidence || evidence.length === 0) {
                    return '';
                }
                
                const itemsHtml = evidence.map(item => {
                    const citations = item.citations 
                        ? item.citations.map(cite => `<span class="citation-tag">¶${cite}</span>`).join('') 
                        : '';
                    
                    return `
                    <div class="reference-block">
                        <div class="reference-header">
                            <span class="reference-title">${item.id}: ${item.title}</span>
                            <button class="action-btn" style="padding: 0; height: 20px; background: none; border: none;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3182ce" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                                </svg>
                            </button>
                        </div>
                        <p class="reference-summary">${item.summary}</p>
                        <div>
                            <span style="font-size: 0.75rem; color: #718096;">Cited in:</span>
                            ${citations}
                        </div>
                    </div>
                    `;
                }).join('');
                
                return `
                <div class="content-section">
                    <div class="content-title">Evidence</div>
                    ${itemsHtml}
                </div>
                `;
            }
            
            // Render case law
            function renderCaseLaw(cases) {
                if (!cases || cases.length === 0) {
                    return '';
                }
                
                const itemsHtml = cases.map(item => {
                    const citedParagraphs = item.citedParagraphs 
                        ? item.citedParagraphs.map(para => `<span class="citation-tag">¶${para}</span>`).join('') 
                        : '';
                    
                    return `
                    <div class="reference-block">
                        <div class="reference-header">
                            <div>
                                <span class="reference-title">${item.caseNumber}</span>
                                <span class="point-citation" style="margin-left: 0.5rem;">¶${item.paragraphs}</span>
                            </div>
                            <button class="action-btn" style="padding: 0; height: 20px; background: none; border: none;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3182ce" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                                </svg>
                            </button>
                        </div>
                        <p class="reference-summary">${item.title}</p>
                        <p class="point-text">${item.relevance}</p>
                        <div>
                            <span style="font-size: 0.75rem; color: #718096;">Key Paragraphs:</span>
                            ${citedParagraphs}
                        </div>
                    </div>
                    `;
                }).join('');
                
                return `
                <div class="content-section">
                    <div class="content-title">Case Law</div>
                    ${itemsHtml}
                </div>
                `;
            }
            
            // Render argument content
            function renderArgumentContent(arg) {
                let content = '';
                
                // Overview points
                if (arg.overview) {
                    content += renderOverviewPoints(arg.overview);
                }
                
                // Legal points
                if (arg.legalPoints) {
                    content += renderLegalPoints(arg.legalPoints);
                }
                
                // Factual points
                if (arg.factualPoints) {
                    content += renderFactualPoints(arg.factualPoints);
                }
                
                // Evidence
                if (arg.evidence) {
                    content += renderEvidence(arg.evidence);
                }
                
                // Case law
                if (arg.caseLaw) {
                    content += renderCaseLaw(arg.caseLaw);
                }
                
                return content;
            }
            
            // Recursively render a single argument with all its children
            function renderArgument(arg, side, pathPrefix = '', level = 0) {
                if (!arg) return '';
                
                const id = pathPrefix ? `${pathPrefix}.${arg.id}` : arg.id;
                const uniqueId = `${side}-${id}`;
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const childCount = hasChildren ? Object.keys(arg.children).length : 0;
                
                // Styling based on side
                const headerClass = side === 'claimant' ? 'claimant-header' : 'respondent-header';
                const badgeClass = side === 'claimant' ? 'claimant-badge' : 'respondent-badge';
                const textColor = side === 'claimant' ? 'claimant-color' : 'respondent-color';
                
                // Argument HTML
                let html = '';
                
                // Add horizontal connector for non-root arguments
                if (level > 0) {
                    html += `
                    <div class="horizontal-connector">
                        <div class="connector-line"></div>
                    </div>
                    `;
                }
                
                // Argument card
                html += `
                <div class="argument-card ${headerClass}" data-id="${uniqueId}" data-level="${level}">
                    <div class="argument-header" onclick="toggleArgument('${uniqueId}')">
                        <div class="header-left">
                            <svg class="chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6"></polyline>
                            </svg>
                            <h5 class="${textColor}" style="font-size: 0.875rem; font-weight: 500; margin: 0;">
                                ${arg.id}. ${arg.title}
                            </h5>
                        </div>
                        ${hasChildren 
                          ? `<span class="badge ${badgeClass} round-badge">${childCount} subarguments</span>` 
                          : `<span class="badge ${badgeClass}">¶${arg.paragraphs}</span>`
                        }
                    </div>
                    <div class="argument-content" id="content-${uniqueId}">
                        ${renderArgumentContent(arg)}
                    </div>
                </div>
                `;
                
                // Child arguments
                if (hasChildren) {
                    html += `<div class="child-arguments" id="children-${uniqueId}">`;
                    
                    // Render each child
                    Object.values(arg.children).forEach(child => {
                        html += renderArgument(child, side, id, level + 1);
                    });
                    
                    html += `</div>`;
                }
                
                return html;
            }
            
            // Render paired arguments side by side
            function renderArgumentPairs(claimantArgs, respondentArgs) {
                let html = '';
                
                // Process top-level arguments
                Object.keys(claimantArgs).forEach(argId => {
                    if (respondentArgs[argId]) {
                        const claimantArg = claimantArgs[argId];
                        const respondentArg = respondentArgs[argId];
                        
                        html += `
                        <div class="argument-pair-container">
                            <div class="argument-pair">
                                <div class="claimant-side">
                                    ${renderArgument(claimantArg, 'claimant')}
                                </div>
                                <div class="respondent-side">
                                    ${renderArgument(respondentArg, 'respondent')}
                                </div>
                            </div>
                        </div>
                        `;
                    }
                });
                
                return html;
            }
            
            // Render topic view
            function renderTopicView(topics, claimantArgs, respondentArgs) {
                let html = '';
                
                topics.forEach(topic => {
                    html += `
                    <div class="topic-section">
                        <h2 class="topic-title">${topic.title}</h2>
                        <p class="topic-description">${topic.description}</p>
                        
                        <div class="column-headers">
                            <h3 class="claimant-color">Claimant's Arguments</h3>
                            <h3 class="respondent-color">Respondent's Arguments</h3>
                        </div>
                    `;
                    
                    // Add arguments for this topic
                    topic.argumentIds.forEach(argId => {
                        if (claimantArgs[argId] && respondentArgs[argId]) {
                            html += `
                            <div class="argument-pair-container">
                                <div class="argument-pair">
                                    <div class="claimant-side">
                                        ${renderArgument(claimantArgs[argId], 'claimant')}
                                    </div>
                                    <div class="respondent-side">
                                        ${renderArgument(respondentArgs[argId], 'respondent')}
                                    </div>
                                </div>
                            </div>
                            `;
                        }
                    });
                    
                    html += `</div>`;
                });
                
                return html;
            }
            
            // Toggle argument expansion
            function toggleArgument(id) {
                const contentEl = document.getElementById(`content-${id}`);
                const chevronEl = document.querySelector(`.argument-card[data-id="${id}"] .chevron`);
                const childrenEl = document.getElementById(`children-${id}`);
                
                // Split ID to get side and argId
                const [side, argId] = id.split('-');
                
                // Get paired argument ID
                const otherSide = side === 'claimant' ? 'respondent' : 'claimant';
                const pairedId = `${otherSide}-${argId}`;
                
                // Get paired elements
                const pairedContentEl = document.getElementById(`content-${pairedId}`);
                const pairedChevronEl = document.querySelector(`.argument-card[data-id="${pairedId}"] .chevron`);
                const pairedChildrenEl = document.getElementById(`children-${pairedId}`);
                
                // Toggle expanded state
                expandedStates[id] = !expandedStates[id];
                const isExpanded = expandedStates[id];
                
                // Update elements
                if (contentEl) {
                    contentEl.style.display = isExpanded ? 'block' : 'none';
                }
                if (chevronEl) {
                    chevronEl.style.transform = isExpanded ? 'rotate(90deg)' : '';
                }
                if (childrenEl) {
                    childrenEl.style.display = isExpanded ? 'block' : 'none';
                }
                
                // Also update paired elements
                expandedStates[pairedId] = isExpanded;
                
                if (pairedContentEl) {
                    pairedContentEl.style.display = isExpanded ? 'block' : 'none';
                }
                if (pairedChevronEl) {
                    pairedChevronEl.style.transform = isExpanded ? 'rotate(90deg)' : '';
                }
                if (pairedChildrenEl) {
                    pairedChildrenEl.style.display = isExpanded ? 'block' : 'none';
                }
            }
            
            // Render timeline data
            function renderTimeline() {
                const tbody = document.getElementById('timeline-body');
                tbody.innerHTML = '';
                
                // Apply search and filter
                const searchTerm = document.getElementById('timeline-search').value.toLowerCase();
                const disputedOnly = document.getElementById('disputed-only').checked;
                
                timelineData.forEach(item => {
                    // Apply filters
                    if (
                        (searchTerm && 
                         !item.appellantVersion.toLowerCase().includes(searchTerm) && 
                         !item.respondentVersion.toLowerCase().includes(searchTerm))
                        ||
                        (disputedOnly && item.status !== 'Disputed')
                    ) {
                        return; // Skip this item
                    }
                    
                    const row = document.createElement('tr');
                    if (item.status === 'Disputed') {
                        row.classList.add('disputed');
                    }
                    
                    row.innerHTML = `
                        <td>${item.date}</td>
                        <td>${item.appellantVersion}</td>
                        <td>${item.respondentVersion}</td>
                        <td class="${item.status.toLowerCase()}-text">${item.status}</td>
                    `;
                    
                    tbody.appendChild(row);
                });
            }
            
            // Render exhibits data
            function renderExhibits() {
                const tbody = document.getElementById('exhibits-body');
                const typeFilter = document.getElementById('type-filter');
                tbody.innerHTML = '';
                
                // Populate type filter if needed
                if (typeFilter.options.length === 1) {
                    const types = [...new Set(exhibitsData.map(item => item.type))];
                    types.forEach(type => {
                        const option = document.createElement('option');
                        option.value = type;
                        option.textContent = type.charAt(0).toUpperCase() + type.slice(1);
                        typeFilter.appendChild(option);
                    });
                }
                
                // Apply search and filters
                const searchTerm = document.getElementById('exhibits-search').value.toLowerCase();
                const partyFilter = document.getElementById('party-filter').value;
                const typeValue = typeFilter.value;
                
                exhibitsData.forEach(item => {
                    // Apply filters
                    if (
                        (searchTerm && 
                         !item.id.toLowerCase().includes(searchTerm) && 
                         !item.title.toLowerCase().includes(searchTerm) &&
                         !item.summary.toLowerCase().includes(searchTerm))
                        ||
                        (partyFilter !== 'All Parties' && item.party !== partyFilter)
                        ||
                        (typeValue !== 'All Types' && item.type !== typeValue)
                    ) {
                        return; // Skip this item
                    }
                    
                    const row = document.createElement('tr');
                    const badgeClass = item.party === 'Appellant' ? 'claimant-badge' : 'respondent-badge';
                    
                    row.innerHTML = `
                        <td>${item.id}</td>
                        <td><span class="badge ${badgeClass}">${item.party}</span></td>
                        <td>${item.title}</td>
                        <td><span class="badge">${item.type}</span></td>
                        <td>${item.summary}</td>
                        <td style="text-align: right;"><a href="#" style="color: #3182ce; text-decoration: none;">View</a></td>
                    `;
                    
                    tbody.appendChild(row);
                });
            }
            
            // Tab switching
            document.querySelectorAll('.tab').forEach(tab => {
                tab.addEventListener('click', function() {
                    // Update active state
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Show correct content
                    const tabId = this.getAttribute('data-tab');
                    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
                    document.getElementById(tabId).classList.add('active');
                    
                    // Initialize if needed
                    if (tabId === 'timeline') renderTimeline();
                    if (tabId === 'exhibits') renderExhibits();
                });
            });
            
            // View mode switching
            document.querySelectorAll('.view-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    // Update active state
                    document.querySelectorAll('.view-btn').forEach(b => {
                        b.classList.remove('active');
                        b.style.backgroundColor = '';
                        b.style.boxShadow = '';
                    });
                    this.classList.add('active');
                    this.style.backgroundColor = 'white';
                    this.style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';
                    
                    // Show correct view
                    const viewId = this.getAttribute('data-view');
                    if (viewId === 'standard') {
                        document.getElementById('standard-view').style.display = 'block';
                        document.getElementById('topic-view').style.display = 'none';
                    } else {
                        document.getElementById('standard-view').style.display = 'none';
                        document.getElementById('topic-view').style.display = 'block';
                    }
                });
            });
            
            // Set up event listeners for timeline and exhibits
            document.getElementById('timeline-search')?.addEventListener('input', renderTimeline);
            document.getElementById('disputed-only')?.addEventListener('change', renderTimeline);
            document.getElementById('exhibits-search')?.addEventListener('input', renderExhibits);
            document.getElementById('party-filter')?.addEventListener('change', renderExhibits);
            document.getElementById('type-filter')?.addEventListener('change', renderExhibits);
            
            // Initialize the views
            document.getElementById('arguments-container').innerHTML = renderArgumentPairs(
                argsData.claimantArgs, 
                argsData.respondentArgs
            );
            
            document.getElementById('topics-container').innerHTML = renderTopicView(
                argsData.topics,
                argsData.claimantArgs,
                argsData.respondentArgs
            );
            
            // Make sure initial styling is set
            document.querySelector('.view-btn.active').style.backgroundColor = 'white';
            document.querySelector('.view-btn.active').style.boxShadow = '0 1px 2px rgba(0,0,0,0.05)';
        </script>
    </body>
    </html>
    """
    
    # Render the HTML
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
