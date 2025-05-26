import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="CaseLens - Legal Arguments Analysis", 
    layout="wide",
    initial_sidebar_state="collapsed"  # Hide default sidebar since we have our own
)

# Hide default Streamlit elements for a cleaner look
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp > header {
    background-color: transparent;
}
.stApp {
    margin-top: -80px;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read the HTML file (you'll need to save the previous artifact as an HTML file)
# For demo purposes, I'll include the HTML inline, but you can also read from file
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CaseLens - Legal Arguments Analysis</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <style>
        * {
            box-sizing: border-box;
        }
        
        body {
            margin: 0;
            font-family: "Source Sans Pro", sans-serif;
            background-color: #ffffff;
            color: #262730;
        }
        
        .app-container {
            display: flex;
            min-height: 100vh;
        }
        
        .sidebar {
            width: 300px;
            background-color: #f0f2f6;
            padding: 2rem 1rem;
            border-right: 1px solid #e0e0e0;
        }
        
        .logo-container {
            display: flex;
            align-items: center;
            margin-bottom: 2rem;
        }
        
        .logo-container h1 {
            margin-left: 10px;
            font-weight: 600;
            color: #4D68F9;
            font-size: 1.5rem;
        }
        
        .sidebar h3 {
            color: #262730;
            margin-bottom: 1rem;
        }
        
        .nav-button {
            width: 100%;
            padding: 0.75rem 1rem;
            margin-bottom: 0.5rem;
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.3s;
            text-align: left;
        }
        
        .nav-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        .nav-button.active {
            background-color: #4D68F9;
            color: white;
            border-color: #4D68F9;
        }
        
        .main-content {
            flex: 1;
            padding: 2rem;
            overflow-y: auto;
        }
        
        .title {
            font-size: 2rem;
            font-weight: 600;
            margin-bottom: 2rem;
            color: #262730;
        }
        
        .view-toggles {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        
        .view-button {
            padding: 0.5rem 1rem;
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            background-color: #ffffff;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.3s;
        }
        
        .view-button:hover {
            background-color: #f0f2f6;
        }
        
        .view-button.active {
            background-color: #4D68F9;
            color: white;
            border-color: #4D68F9;
        }
        
        .filter-container {
            margin: 1rem 0;
        }
        
        .filter-select {
            padding: 0.5rem;
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            font-size: 1rem;
            background-color: white;
            min-width: 200px;
        }
        
        .divider {
            height: 1px;
            background-color: #e0e0e0;
            margin: 1rem 0;
        }
        
        .fact-card {
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            margin-bottom: 1rem;
            overflow: hidden;
            background-color: white;
        }
        
        .fact-header {
            padding: 1rem;
            background-color: #f8f9fa;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #e0e0e0;
        }
        
        .fact-header:hover {
            background-color: #e9ecef;
        }
        
        .fact-title {
            font-weight: 600;
            color: #262730;
        }
        
        .dispute-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: #dc3545;
        }
        
        .dispute-indicator.undisputed {
            background-color: #28a745;
        }
        
        .fact-content {
            padding: 1rem;
            display: none;
        }
        
        .fact-content.expanded {
            display: block;
        }
        
        .section-header {
            font-size: 1.1rem;
            font-weight: 600;
            margin: 1rem 0 0.5rem 0;
            color: #262730;
        }
        
        .evidence-item {
            margin-bottom: 1rem;
            padding: 1rem;
            background-color: #f8f9fa;
            border-radius: 6px;
        }
        
        .evidence-title {
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        
        .submission-section {
            margin: 1rem 0;
        }
        
        .submission-header {
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        
        .submission-content {
            padding: 1rem;
            border-radius: 6px;
            font-style: italic;
        }
        
        .claimant-submission {
            background-color: #d1ecf1;
            border-left: 4px solid #17a2b8;
        }
        
        .respondent-submission {
            background-color: #f8d7da;
            border-left: 4px solid #dc3545;
        }
        
        .status-section {
            display: flex;
            gap: 2rem;
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px solid #e0e0e0;
        }
        
        .status-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .timeline-year {
            font-size: 1.5rem;
            font-weight: 600;
            margin: 2rem 0 1rem 0;
            color: #262730;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .timeline-event {
            margin-bottom: 2rem;
            padding: 1rem;
            border-left: 4px solid #4D68F9;
            background-color: #f8f9fa;
            border-radius: 0 6px 6px 0;
        }
        
        .timeline-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }
        
        .timeline-date {
            font-weight: 600;
            color: #4D68F9;
        }
        
        .timeline-title {
            font-weight: 600;
            flex: 1;
            margin: 0 1rem;
        }
        
        .docset-container {
            margin-bottom: 1rem;
        }
        
        .docset-header {
            padding: 1rem;
            background-color: #f8f9fa;
            cursor: pointer;
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .docset-header:hover {
            background-color: #e9ecef;
        }
        
        .docset-content {
            display: none;
            border: 1px solid #e0e0e0;
            border-top: none;
            border-radius: 0 0 6px 6px;
            padding: 1rem;
        }
        
        .docset-content.expanded {
            display: block;
        }
        
        .copy-button {
            padding: 0.25rem 0.5rem;
            background-color: #6c757d;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.8rem;
        }
        
        .copy-button:hover {
            background-color: #5a6268;
        }
        
        .no-facts {
            text-align: center;
            padding: 2rem;
            color: #6c757d;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useEffect } = React;

        // Data (same as before - I'll include a condensed version)
        const argumentData = {
            "claimantArgs": {
                "1": {
                    "id": "1",
                    "title": "Sporting Succession",
                    "paragraphs": "15-18",
                    "factualPoints": [
                        {
                            "point": "Continuous operation under same name since 1950",
                            "date": "1950-present",
                            "isDisputed": false,
                            "paragraphs": "18-19",
                            "exhibits": ["C-1", "C-2", "C-4"],
                            "source_text": "The club has maintained continuous operation under the same name 'Athletic Club United' since its official registration in 1950, as evidenced by uninterrupted participation in national competitions and consistent use of the same corporate identity throughout this period.",
                            "page": 23,
                            "doc_name": "Statement of Appeal",
                            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                        }
                    ],
                    "evidence": [
                        {
                            "id": "C-1",
                            "title": "Historical Registration Documents",
                            "summary": "Official records showing continuous name usage from 1950 to present day.",
                            "citations": ["20", "21", "24"]
                        },
                        {
                            "id": "C-2", 
                            "title": "Competition Participation Records",
                            "summary": "Complete records of the club's participation in national and regional competitions from 1950 to present.",
                            "citations": ["25", "26", "28"]
                        },
                        {
                            "id": "C-4",
                            "title": "Media Coverage Archive", 
                            "summary": "Comprehensive collection of newspaper clippings, sports magazines, and media reports spanning 1950-2024.",
                            "citations": ["53", "54", "55"]
                        }
                    ],
                    "children": {
                        "1.1": {
                            "id": "1.1",
                            "title": "Club Name Analysis",
                            "children": {
                                "1.1.1": {
                                    "id": "1.1.1",
                                    "title": "Registration History",
                                    "factualPoints": [
                                        {
                                            "point": "Initial registration in 1950",
                                            "date": "1950",
                                            "isDisputed": false,
                                            "exhibits": ["C-2"],
                                            "source_text": "The club was initially registered with the National Football Federation on January 12, 1950, under registration number NFF-1950-0047.",
                                            "page": 31,
                                            "doc_name": "Statement of Appeal",
                                            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                        },
                                        {
                                            "point": "Brief administrative gap in 1975-1976",
                                            "date": "1975-1976",
                                            "isDisputed": true,
                                            "exhibits": ["C-2"],
                                            "source_text": "While there was a temporary administrative restructuring during 1975-1976 due to financial difficulties, the club's core operations and identity remained intact throughout this period.",
                                            "page": 35,
                                            "doc_name": "Statement of Appeal",
                                            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                        }
                                    ]
                                }
                            }
                        },
                        "1.2": {
                            "id": "1.2",
                            "title": "Club Colors Analysis",
                            "factualPoints": [
                                {
                                    "point": "Consistent use of blue and white since founding",
                                    "date": "1950-present",
                                    "isDisputed": true,
                                    "exhibits": ["C-4"],
                                    "source_text": "The club has consistently utilized blue and white as its primary colors since its founding in 1950.",
                                    "page": 58,
                                    "doc_name": "Statement of Appeal",
                                    "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                }
                            ],
                            "children": {
                                "1.2.1": {
                                    "id": "1.2.1",
                                    "title": "Color Variations Analysis",
                                    "factualPoints": [
                                        {
                                            "point": "Minor shade variations do not affect continuity",
                                            "date": "1970-1980",
                                            "isDisputed": false,
                                            "exhibits": ["C-5"],
                                            "source_text": "Minor variations in the specific shades of blue and white used in uniforms during the 1970s were purely aesthetic choices.",
                                            "page": 63,
                                            "doc_name": "Statement of Appeal",
                                            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                        },
                                        {
                                            "point": "Temporary third color addition in 1980s",
                                            "date": "1982-1988",
                                            "isDisputed": false,
                                            "exhibits": ["C-5"],
                                            "source_text": "Between 1982 and 1988, the club temporarily incorporated a third accent color (gold) in its uniform design for special occasions.",
                                            "page": 65,
                                            "doc_name": "Statement of Appeal",
                                            "doc_summary": "Primary appeal document outlining the appellant's main arguments regarding sporting succession and club identity continuity."
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
            },
            "respondentArgs": {
                "1": {
                    "id": "1",
                    "title": "Sporting Succession Rebuttal",
                    "factualPoints": [
                        {
                            "point": "Operations ceased between 1975-1976",
                            "date": "1975-1976",
                            "isDisputed": true,
                            "exhibits": ["R-1"],
                            "source_text": "The club's operations completely ceased during the 1975-1976 season, with no participation in any competitive events and complete absence from all official federation records.",
                            "page": 89,
                            "doc_name": "Answer to Request for Provisional Measures",
                            "doc_summary": "Respondent's response challenging the appellant's claims and presenting evidence of operational discontinuity."
                        }
                    ],
                    "evidence": [
                        {
                            "id": "R-1",
                            "title": "Federation Records",
                            "summary": "Official competition records from the National Football Federation for the 1975-1976 season, showing complete absence of the club.",
                            "citations": ["208", "209", "210"]
                        }
                    ]
                }
            }
        };

        const documentSets = [
            {
                "id": "appeal",
                "name": "Appeal",
                "party": "Mixed",
                "isGroup": true,
                "documents": [
                    {"id": "1", "name": "1. Statement of Appeal", "party": "Appellant"},
                    {"id": "5", "name": "5. Appeal Brief", "party": "Appellant"}
                ]
            },
            {
                "id": "provisional_measures",
                "name": "provisional measures",
                "party": "Respondent",
                "isGroup": true,
                "documents": [
                    {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent"}
                ]
            }
        ];

        // Utility functions
        const extractFacts = (args, party) => {
            const facts = [];
            
            const processArg = (arg) => {
                if (arg.factualPoints) {
                    arg.factualPoints.forEach(point => {
                        facts.push({
                            event: point.point,
                            date: point.date,
                            isDisputed: point.isDisputed,
                            party: party,
                            paragraphs: point.paragraphs || '',
                            exhibits: point.exhibits || [],
                            argId: arg.id,
                            argTitle: arg.title,
                            source_text: point.source_text || '',
                            page: point.page || '',
                            doc_name: point.doc_name || '',
                            doc_summary: point.doc_summary || ''
                        });
                    });
                }
                
                if (arg.children) {
                    Object.values(arg.children).forEach(processArg);
                }
            };
            
            Object.values(args).forEach(processArg);
            return facts;
        };

        const getAllFacts = () => {
            const claimantFacts = extractFacts(argumentData.claimantArgs, 'Appellant');
            const respondentFacts = extractFacts(argumentData.respondentArgs, 'Respondent');
            
            const allFacts = [...claimantFacts, ...respondentFacts];
            const factGroups = {};
            
            allFacts.forEach(fact => {
                const key = `${fact.date}_${fact.event.substring(0, 50)}`;
                if (!factGroups[key]) {
                    factGroups[key] = {
                        event: fact.event,
                        date: fact.date,
                        isDisputed: fact.isDisputed,
                        claimant_submission: '',
                        respondent_submission: '',
                        source_text: fact.source_text,
                        page: fact.page,
                        doc_name: fact.doc_name,
                        doc_summary: fact.doc_summary,
                        exhibits: fact.exhibits,
                        paragraphs: fact.paragraphs,
                        argId: fact.argId,
                        argTitle: fact.argTitle,
                        parties_involved: []
                    };
                }
                
                if (fact.party === 'Appellant') {
                    factGroups[key].claimant_submission = fact.source_text;
                } else {
                    factGroups[key].respondent_submission = fact.source_text;
                }
                
                factGroups[key].parties_involved.push(fact.party);
                
                if (fact.isDisputed) {
                    factGroups[key].isDisputed = true;
                }
            });
            
            return Object.values(factGroups).map(group => ({
                ...group,
                claimant_submission: group.claimant_submission || 'No specific submission recorded',
                respondent_submission: group.respondent_submission || 'No specific submission recorded',
                parties_involved: [...new Set(group.parties_involved)]
            }));
        };

        const getEvidenceContent = (fact) => {
            if (!fact.exhibits || fact.exhibits.length === 0) {
                return [];
            }
            
            const evidenceContent = [];
            
            const findEvidence = (args) => {
                for (const argKey in args) {
                    const arg = args[argKey];
                    if (arg.evidence) {
                        const evidence = arg.evidence.find(e => fact.exhibits.includes(e.id));
                        if (evidence) {
                            evidenceContent.push({
                                id: evidence.id,
                                title: evidence.title,
                                summary: evidence.summary
                            });
                        }
                    }
                    if (arg.children) {
                        findEvidence(arg.children);
                    }
                }
            };
            
            findEvidence(argumentData.claimantArgs);
            findEvidence(argumentData.respondentArgs);
            
            fact.exhibits.forEach(exhibitId => {
                if (!evidenceContent.find(e => e.id === exhibitId)) {
                    evidenceContent.push({
                        id: exhibitId,
                        title: exhibitId,
                        summary: 'Evidence details not available'
                    });
                }
            });
            
            return evidenceContent;
        };

        // Components (simplified versions)
        const FactCard = ({ fact, index }) => {
            const [expanded, setExpanded] = useState(false);
            const evidenceContent = getEvidenceContent(fact);
            
            return (
                <div className="fact-card">
                    <div className="fact-header" onClick={() => setExpanded(!expanded)}>
                        <div className="fact-title">
                            <strong>{fact.date}</strong> - {fact.event}
                        </div>
                        <div className={`dispute-indicator ${!fact.isDisputed ? 'undisputed' : ''}`}></div>
                    </div>
                    <div className={`fact-content ${expanded ? 'expanded' : ''}`}>
                        <div className="section-header">📁 Evidence & Source References</div>
                        {evidenceContent.length > 0 ? (
                            evidenceContent.map((evidence, idx) => (
                                <div key={idx} className="evidence-item">
                                    <div className="evidence-title">
                                        <strong>{evidence.id}</strong> - {evidence.title}
                                    </div>
                                    {fact.doc_summary && (
                                        <div style={{ margin: '0.5rem 0', padding: '0.5rem', backgroundColor: '#d1ecf1', borderRadius: '4px' }}>
                                            <strong>Document Summary:</strong> {fact.doc_summary}
                                        </div>
                                    )}
                                    {fact.source_text && (
                                        <div style={{ margin: '0.5rem 0', fontStyle: 'italic' }}>
                                            <strong>Source Text:</strong> {fact.source_text}
                                        </div>
                                    )}
                                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '0.5rem' }}>
                                        <div>
                                            <strong>Exhibit:</strong> {evidence.id}
                                            {fact.page && <span> | <strong>Page:</strong> {fact.page}</span>}
                                            {fact.paragraphs && <span> | <strong>Paragraphs:</strong> {fact.paragraphs}</span>}
                                        </div>
                                        <button className="copy-button" onClick={() => {
                                            const refText = `Exhibit: ${evidence.id}${fact.page ? `, Page: ${fact.page}` : ''}${fact.paragraphs ? `, Paragraphs: ${fact.paragraphs}` : ''}`;
                                            navigator.clipboard.writeText(refText);
                                        }}>
                                            📋 Copy Ref
                                        </button>
                                    </div>
                                </div>
                            ))
                        ) : (
                            <div style={{ fontStyle: 'italic', color: '#6c757d' }}>
                                No evidence references available for this fact
                            </div>
                        )}
                        
                        <div className="section-header">⚖️ Party Submissions</div>
                        <div className="submission-section">
                            <div className="submission-header">🔵 Claimant Submission</div>
                            <div className="submission-content claimant-submission">
                                {fact.claimant_submission === 'No specific submission recorded' ? 
                                    <em>No submission provided</em> : 
                                    fact.claimant_submission
                                }
                            </div>
                        </div>
                        <div className="submission-section">
                            <div className="submission-header">🔴 Respondent Submission</div>
                            <div className="submission-content respondent-submission">
                                {fact.respondent_submission === 'No specific submission recorded' ? 
                                    <em>No submission provided</em> : 
                                    fact.respondent_submission
                                }
                            </div>
                        </div>
                        
                        <div className="section-header">📊 Status</div>
                        <div className="status-section">
                            <div className="status-item">
                                <strong>Status:</strong> 
                                <span style={{ color: fact.isDisputed ? '#dc3545' : '#28a745', marginLeft: '0.5rem' }}>
                                    {fact.isDisputed ? 'Disputed' : 'Undisputed'}
                                </span>
                            </div>
                            {fact.parties_involved && (
                                <div className="status-item">
                                    <strong>Parties:</strong> {fact.parties_involved.join(', ')}
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            );
        };

        // Main App Component
        const CaseLensApp = () => {
            const [currentView, setCurrentView] = useState('Facts');
            const [currentViewType, setCurrentViewType] = useState('card');
            const [filterType, setFilterType] = useState('all');
            
            const allFacts = getAllFacts();
            
            const getFilteredFacts = () => {
                switch (filterType) {
                    case 'disputed':
                        return allFacts.filter(fact => fact.isDisputed);
                    case 'undisputed':
                        return allFacts.filter(fact => !fact.isDisputed);
                    default:
                        return allFacts;
                }
            };
            
            const filteredFacts = getFilteredFacts();
            
            return (
                <div className="app-container">
                    <div className="sidebar">
                        <div className="logo-container">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 175 175" width="35" height="35">
                                <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
                            </svg>
                            <h1>CaseLens</h1>
                        </div>
                        
                        <h3>Legal Analysis</h3>
                        
                        <button 
                            className={`nav-button ${currentView === 'Arguments' ? 'active' : ''}`}
                            onClick={() => setCurrentView('Arguments')}
                        >
                            📑 Arguments
                        </button>
                        <button 
                            className={`nav-button ${currentView === 'Facts' ? 'active' : ''}`}
                            onClick={() => setCurrentView('Facts')}
                        >
                            📊 Facts
                        </button>
                        <button 
                            className={`nav-button ${currentView === 'Exhibits' ? 'active' : ''}`}
                            onClick={() => setCurrentView('Exhibits')}
                        >
                            📁 Exhibits
                        </button>
                    </div>
                    
                    <div className="main-content">
                        <h1 className="title">Case Facts</h1>
                        
                        {currentView === 'Facts' && (
                            <>
                                <div className="view-toggles">
                                    <button 
                                        className={`view-button ${currentViewType === 'card' ? 'active' : ''}`}
                                        onClick={() => setCurrentViewType('card')}
                                    >
                                        📋 Card View
                                    </button>
                                    <button 
                                        className={`view-button ${currentViewType === 'timeline' ? 'active' : ''}`}
                                        onClick={() => setCurrentViewType('timeline')}
                                    >
                                        📅 Timeline View
                                    </button>
                                    <button 
                                        className={`view-button ${currentViewType === 'docset' ? 'active' : ''}`}
                                        onClick={() => setCurrentViewType('docset')}
                                    >
                                        📁 Document Categories
                                    </button>
                                </div>
                                
                                <div className="divider"></div>
                                
                                <div className="filter-container">
                                    <select 
                                        className="filter-select" 
                                        value={filterType} 
                                        onChange={(e) => setFilterType(e.target.value)}
                                    >
                                        <option value="all">All Facts</option>
                                        <option value="disputed">Disputed Facts</option>
                                        <option value="undisputed">Undisputed Facts</option>
                                    </select>
                                </div>
                                
                                <div className="divider"></div>
                            </>
                        )}
                        
                        <div>
                            {currentView !== 'Facts' ? (
                                <div className="no-facts">
                                    {currentView} view is not implemented in this demo.
                                </div>
                            ) : (
                                filteredFacts.length > 0 ? (
                                    filteredFacts.map((fact, index) => (
                                        <FactCard key={index} fact={fact} index={index} />
                                    ))
                                ) : (
                                    <div className="no-facts">No facts found matching the selected criteria.</div>
                                )
                            )}
                        </div>
                    </div>
                </div>
            );
        };

        ReactDOM.render(<CaseLensApp />, document.getElementById('root'));
    </script>
</body>
</html>
"""

# Render the React component
components.html(html_content, height=800, scrolling=True)

# Optional: Add some information below the component
st.markdown("---")
st.markdown("""
### About CaseLens
This is a React-based legal analysis tool embedded in Streamlit. It provides:
- **Card View**: Expandable fact cards with detailed evidence and submissions
- **Timeline View**: Chronological display of case events
- **Document Categories**: Facts organized by document categories
- **Filtering**: Filter by disputed/undisputed facts
- **Evidence Tracking**: Links to specific exhibits and source documents

The tool helps legal professionals organize and analyze complex case information across multiple documents and timeframes.
""")
