import streamlit as st
import json
import streamlit.components.v1 as components
import pandas as pd
import base64
import os
from datetime import datetime
import re

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Sample document sets for demonstrating the document set view
def get_document_sets():
    return [
        {
            "id": "appeal",
            "name": "Appeal",
            "party": "Mixed",
            "category": "Appeal",
            "isGroup": True,
            "documents": [
                {"id": "1", "name": "1. Statement of Appeal", "party": "Appellant", "category": "Appeal", "status": "Processed", "file_type": "PDF"},
                {"id": "2", "name": "2. Request for a Stay", "party": "Appellant", "category": "Appeal", "status": "Processed", "file_type": "PDF"},
                {"id": "5", "name": "5. Appeal Brief", "party": "Appellant", "category": "Appeal", "status": "Processed", "file_type": "PDF"},
                {"id": "10", "name": "Jurisprudence", "party": "Shared", "category": "Appeal", "status": "Processed", "file_type": "PDF"}
            ]
        },
        {
            "id": "provisional_messier",
            "name": "provisional messier",
            "party": "Respondent",
            "category": "provisional messier",
            "isGroup": True,
            "documents": [
                {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent", "category": "provisional messier", "status": "Processed", "file_type": "PDF"},
                {"id": "4", "name": "4. Answer to PM", "party": "Respondent", "category": "provisional messier", "status": "Processing", "file_type": "DOCX"}
            ]
        },
        {
            "id": "admissibility",
            "name": "admissibility",
            "party": "Mixed",
            "category": "admissibility",
            "isGroup": True,
            "documents": [
                {"id": "6", "name": "6. Brief on Admissibility", "party": "Respondent", "category": "admissibility", "status": "Processed", "file_type": "PDF"},
                {"id": "7", "name": "7. Reply to Objection to Admissibility", "party": "Appellant", "category": "admissibility", "status": "Processed", "file_type": "PDF"},
                {"id": "11", "name": "Objection to Admissibility", "party": "Respondent", "category": "admissibility", "status": "Error", "file_type": "PDF"}
            ]
        },
        {
            "id": "challenge",
            "name": "challenge",
            "party": "Mixed",
            "category": "challenge",
            "isGroup": True,
            "documents": [
                {"id": "8", "name": "8. Challenge", "party": "Appellant", "category": "challenge", "status": "Processed", "file_type": "PDF"},
                {"id": "9", "name": "ChatGPT", "party": "Shared", "category": "challenge", "status": "Processed", "file_type": "TXT"},
                {"id": "12", "name": "Swiss Court", "party": "Shared", "category": "challenge", "status": "Processed", "file_type": "PDF"}
            ]
        }
    ]

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = "Upload"  # Start with Upload view

if 'document_sets' not in st.session_state:
    st.session_state.document_sets = get_document_sets()

if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = {}

if 'selected_set' not in st.session_state:
    st.session_state.selected_set = None

if 'creating_set' not in st.session_state:
    st.session_state.creating_set = False

if 'viewing_set' not in st.session_state:
    st.session_state.viewing_set = None

if 'viewing_document' not in st.session_state:
    st.session_state.viewing_document = None

if 'breadcrumbs' not in st.session_state:
    st.session_state.breadcrumbs = []

if 'recent_activities' not in st.session_state:
    st.session_state.recent_activities = []

# Smart file analysis function
def analyze_document_content(filename, file_content=None):
    """Analyze document and extract key information"""
    filename_lower = filename.lower()
    
    # Extract potential dates from filename
    dates = re.findall(r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}', filename)
    
    # Smart categorization based on filename
    if any(word in filename_lower for word in ["appeal", "motion", "brief", "petition"]):
        category = "Appeals"
        confidence = 0.9
    elif any(word in filename_lower for word in ["evidence", "exhibit", "proof", "document"]):
        category = "Evidence"
        confidence = 0.8
    elif any(word in filename_lower for word in ["contract", "agreement", "terms", "deal"]):
        category = "Contracts"
        confidence = 0.85
    elif any(word in filename_lower for word in ["witness", "testimony", "statement"]):
        category = "Witness Statements"
        confidence = 0.8
    elif any(word in filename_lower for word in ["expert", "report", "analysis"]):
        category = "Expert Reports"
        confidence = 0.85
    elif any(word in filename_lower for word in ["correspondence", "email", "letter"]):
        category = "Correspondence"
        confidence = 0.7
    else:
        category = "General Documents"
        confidence = 0.5
    
    # Smart party detection
    party = "Shared"
    if any(word in filename_lower for word in ["plaintiff", "appellant", "claimant"]):
        party = "Appellant"
    elif any(word in filename_lower for word in ["defendant", "respondent"]):
        party = "Respondent"
    
    # Extract key information
    key_facts = []
    if dates:
        key_facts.append(f"Contains dates: {', '.join(dates)}")
    
    # Detect document importance
    importance = "Normal"
    if any(word in filename_lower for word in ["final", "judgment", "order", "ruling"]):
        importance = "High"
    elif any(word in filename_lower for word in ["draft", "preliminary", "temp"]):
        importance = "Low"
    
    return {
        "suggested_category": category,
        "confidence": confidence,
        "suggested_party": party,
        "extracted_dates": dates,
        "key_facts": key_facts,
        "importance": importance,
        "file_size_category": "Small" if file_content and len(file_content) < 100000 else "Large"
    }

# Get file type icon
def get_file_icon(file_type):
    """Return appropriate icon for file type"""
    icons = {
        "PDF": "📄",
        "DOCX": "📝",
        "DOC": "📝", 
        "TXT": "📋",
        "XLSX": "📊",
        "CSV": "📈",
        "JPG": "🖼️",
        "PNG": "🖼️",
        "JPEG": "🖼️"
    }
    return icons.get(file_type.upper(), "📎")

# Enhanced file processing function
def process_uploaded_file(uploaded_file):
    """Enhanced file processing with analysis"""
    try:
        file_content = uploaded_file.read()
        
        # Analyze document content
        analysis = analyze_document_content(uploaded_file.name, file_content)
        
        doc_data = {
            "id": f"doc_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "name": uploaded_file.name,
            "party": analysis["suggested_party"],
            "category": analysis["suggested_category"],
            "upload_date": datetime.now().strftime("%Y-%m-%d"),
            "file_type": uploaded_file.type.split('/')[-1].upper() if uploaded_file.type else "Unknown",
            "size": f"{uploaded_file.size/1024:.1f} KB" if uploaded_file.size else "Unknown",
            "status": "Processed",
            "preview": f"Document analyzed: {uploaded_file.name}",
            "key_facts": analysis["key_facts"],
            "analysis": analysis,
            "icon": get_file_icon(uploaded_file.type.split('/')[-1] if uploaded_file.type else "")
        }
        
        # Store file data
        st.session_state.uploaded_files[doc_data["id"]] = {
            "content": file_content,
            "original_name": uploaded_file.name,
            "type": uploaded_file.type,
            "size": uploaded_file.size
        }
        
        # Add to recent activities
        st.session_state.recent_activities.insert(0, {
            "action": "Document Uploaded",
            "item": uploaded_file.name,
            "time": datetime.now().strftime("%H:%M"),
            "type": "upload"
        })
        
        # Keep only last 10 activities
        st.session_state.recent_activities = st.session_state.recent_activities[:10]
        
        return doc_data
        
    except Exception as e:
        st.error(f"Error processing file: {e}")
        return None

# Update breadcrumbs function
def update_breadcrumbs(view, additional_info=None):
    """Update navigation breadcrumbs"""
    breadcrumbs = [("🏠 Home", "Upload")]
    
    if view != "Upload":
        breadcrumbs.append((f"📑 {view}", view))
    
    if additional_info:
        breadcrumbs.append(additional_info)
    
    st.session_state.breadcrumbs = breadcrumbs

# Function to add a document set (enhanced)
def add_document_set(set_name, set_party):
    set_id = set_name.lower().replace(' ', '_')
    set_category = set_name.lower().replace(' ', '_')
    
    existing_ids = [ds["id"] for ds in st.session_state.document_sets]
    if set_id in existing_ids:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        set_id = f"{set_id}_{timestamp}"
    
    new_set = {
        "id": set_id,
        "name": set_name,
        "party": set_party,
        "category": set_category,
        "isGroup": True,
        "documents": [],
        "created_date": datetime.now().strftime("%Y-%m-%d"),
        "status": "Active"
    }
    
    st.session_state.document_sets.append(new_set)
    
    # Add to recent activities
    st.session_state.recent_activities.insert(0, {
        "action": "Document Set Created",
        "item": set_name,
        "time": datetime.now().strftime("%H:%M"),
        "type": "create"
    })
    
    return set_id

# Function to add a document to a set (enhanced)
def add_document_to_set(doc_name, doc_party, set_id, doc_data=None):
    for doc_set in st.session_state.document_sets:
        if doc_set["id"] == set_id:
            if doc_set["documents"]:
                existing_ids = [int(doc["id"]) for doc in doc_set["documents"] if doc["id"].isdigit()]
                next_id = str(max(existing_ids) + 1) if existing_ids else "1"
            else:
                next_id = "1"
            
            new_doc = {
                "id": next_id,
                "name": doc_name,
                "party": doc_party,
                "category": doc_set["category"],
                "status": "Processed",
                "file_type": doc_data.get("file_type", "Unknown") if doc_data else "Unknown",
                "upload_date": datetime.now().strftime("%Y-%m-%d")
            }
            
            if doc_data:
                new_doc.update({
                    "analysis": doc_data.get("analysis", {}),
                    "key_facts": doc_data.get("key_facts", []),
                    "icon": doc_data.get("icon", "📎")
                })
            
            doc_set["documents"].append(new_doc)
            return next_id
    
    return None

# Function to save uploaded file (enhanced)
def save_uploaded_file(uploaded_file, set_id, doc_id):
    try:
        file_content = uploaded_file.read()
        
        file_key = f"{set_id}-{doc_id}"
        st.session_state.uploaded_files[file_key] = {
            "filename": uploaded_file.name,
            "content": file_content,
            "type": uploaded_file.type,
            "size": uploaded_file.size,
            "upload_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return True
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return False

# Function to get CSV download link
def get_csv_download_link(df, filename="data.csv", text="Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Create data structures as JSON for embedded components
def get_argument_data():
    claimant_args = {
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
            "factualPoints": [
                {
                    "point": "Continuous operation under same name since 1950",
                    "date": "1950-present",
                    "isDisputed": False,
                    "paragraphs": "18-19",
                    "exhibits": ["C-1"]
                }
            ],
            "evidence": [
                {
                    "id": "C-1",
                    "title": "Historical Registration Documents",
                    "summary": "Official records showing continuous name usage from 1950 to present day. Includes original registration certificate dated January 12, 1950, and all subsequent renewal documentation without interruption.",
                    "citations": ["20", "21", "24"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2016/A/4576",
                    "title": "Criteria for sporting succession",
                    "relevance": "Establishes key factors for succession including: (1) continuous use of identifying elements, (2) public recognition of the entity's identity, (3) preservation of sporting records and achievements, and (4) consistent participation in competitions under the same identity.",
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
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration History",
                            "paragraphs": "25-30",
                            "factualPoints": [
                                {
                                    "point": "Initial registration in 1950",
                                    "date": "1950",
                                    "isDisputed": False,
                                    "paragraphs": "25-26",
                                    "exhibits": ["C-2"]
                                },
                                {
                                    "point": "Brief administrative gap in 1975-1976",
                                    "date": "1975-1976",
                                    "isDisputed": True,
                                    "source": "Respondent",
                                    "paragraphs": "29-30",
                                    "exhibits": ["C-2"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "C-2",
                                    "title": "Registration Records",
                                    "summary": "Comprehensive collection of official documentation showing the full registration history of the club from its founding to present day. Includes original application forms, government certificates, and renewal documentation.",
                                    "citations": ["25", "26", "28"]
                                }
                            ]
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
                    "factualPoints": [
                        {
                            "point": "Consistent use of blue and white since founding",
                            "date": "1950-present",
                            "isDisputed": True,
                            "source": "Respondent",
                            "paragraphs": "51-52",
                            "exhibits": ["C-4"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "C-4",
                            "title": "Historical Photographs",
                            "summary": "Collection of 73 photographs spanning from 1950 to present day showing the team's uniforms, promotional materials, and stadium decorations. Images are chronologically arranged and authenticated by sports historians.",
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
                                    "isDisputed": False,
                                    "paragraphs": "56-57",
                                    "exhibits": ["C-5"]
                                },
                                {
                                    "point": "Temporary third color addition in 1980s",
                                    "date": "1982-1988",
                                    "isDisputed": False,
                                    "paragraphs": "58-59",
                                    "exhibits": ["C-5"]
                                }
                            ],
                            "children": {}
                        }
                    }
                }
            }
        }
    }
    
    respondent_args = {
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
            "factualPoints": [
                {
                    "point": "Operations ceased between 1975-1976",
                    "date": "1975-1976",
                    "isDisputed": True,
                    "source": "Claimant",
                    "paragraphs": "206-207",
                    "exhibits": ["R-1"]
                }
            ],
            "evidence": [
                {
                    "id": "R-1",
                    "title": "Federation Records",
                    "summary": "Official competition records from the National Football Federation for the 1975-1976 season, showing complete absence of the club from all levels of competition that season. Includes official withdrawal notification dated May 15, 1975.",
                    "citations": ["208", "209", "210"]
                }
            ],
            "caseLaw": [
                {
                    "caseNumber": "CAS 2017/A/5465",
                    "title": "Operational continuity requirement",
                    "relevance": "Establishes that actual operational continuity (specifically participation in competitions) is the primary determinant of sporting succession, outweighing factors such as name, colors, or stadium usage when they conflict. The panel specifically ruled that a gap in competitive activity creates a presumption against continuity that must be overcome with substantial evidence.",
                    "paragraphs": "211-213",
                    "citedParagraphs": ["212"]
                }
            ],
            "children": {}
        }
    }
    
    topics = [
        {
            "id": "topic-1",
            "title": "Sporting Succession and Identity",
            "description": "Questions of club identity, continuity, and succession rights",
            "argumentIds": ["1"]
        }
    ]
    
    return {
        "claimantArgs": claimant_args,
        "respondentArgs": respondent_args,
        "topics": topics
    }

# Get all facts from the data
def get_all_facts():
    args_data = get_argument_data()
    facts = []
    
    def extract_facts(arg, party):
        if not arg:
            return
            
        if 'factualPoints' in arg and arg['factualPoints']:
            for point in arg['factualPoints']:
                fact = {
                    'point': point['point'],
                    'date': point['date'],
                    'isDisputed': point['isDisputed'],
                    'party': party,
                    'paragraphs': point.get('paragraphs', ''),
                    'exhibits': point.get('exhibits', []),
                    'argId': arg['id'],
                    'argTitle': arg['title'],
                    'source': point.get('source', party)
                }
                facts.append(fact)
                
        if 'children' in arg and arg['children']:
            for child_id, child in arg['children'].items():
                extract_facts(child, party)
    
    for arg_id, arg in args_data['claimantArgs'].items():
        extract_facts(arg, 'Appellant')
        
    for arg_id, arg in args_data['respondentArgs'].items():
        extract_facts(arg, 'Respondent')
        
    return facts

# Get enhanced timeline data with additional events
def get_timeline_data():
    timeline_events = [
        {
            "point": "Club founded and officially registered in the Football Federation",
            "date": "1950-01-12",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-1"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Statement of Appeal"
        },
        {
            "point": "First National Championship won",
            "date": "1955-05-20",
            "isDisputed": False,
            "party": "Appellant",
            "exhibits": ["C-3"],
            "argId": "1",
            "argTitle": "Sporting Succession",
            "source": "Appeal - Appeal Brief"
        },
        {
            "point": "Operations ceased between 1975-1976",
            "date": "1975-1976",
            "isDisputed": True,
            "party": "Respondent",
            "exhibits": ["R-1"],
            "argId": "1",
            "argTitle": "Sporting Succession Rebuttal",
            "source": "provisional messier - Answer to PM"
        }
    ]
    
    timeline_events.sort(key=lambda x: x['date'])
    return timeline_events

# Render breadcrumbs
def render_breadcrumbs():
    """Render navigation breadcrumbs"""
    if st.session_state.breadcrumbs:
        breadcrumb_html = ""
        for i, (label, view) in enumerate(st.session_state.breadcrumbs):
            if i == len(st.session_state.breadcrumbs) - 1:
                # Current page
                breadcrumb_html += f'<span style="color: #6b7280;">{label}</span>'
            else:
                # Clickable breadcrumb
                breadcrumb_html += f'<a href="#" onclick="navigateTo(\'{view}\')" style="color: #4D68F9; text-decoration: none;">{label}</a>'
                if i < len(st.session_state.breadcrumbs) - 1:
                    breadcrumb_html += ' <span style="color: #d1d5db; margin: 0 8px;">›</span> '
        
        st.markdown(f"""
        <div style="margin-bottom: 20px; padding: 8px 0; border-bottom: 1px solid #f3f4f6;">
            <nav style="font-size: 14px;">
                {breadcrumb_html}
            </nav>
        </div>
        """, unsafe_allow_html=True)

# Render dashboard
def render_dashboard():
    """Enhanced dashboard with better metrics and recent activity"""
    update_breadcrumbs("Dashboard")
    render_breadcrumbs()
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; margin-bottom: 30px; color: white; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
        <h1 style="margin: 0; font-size: 2.5rem; font-weight: 700;">📋 Case Dashboard</h1>
        <p style="margin: 10px 0 0 0; font-size: 1.1rem; opacity: 0.9;">Your legal documents and case analysis overview</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced metrics
    all_docs = []
    for doc_set in st.session_state.document_sets:
        all_docs.extend(doc_set["documents"])
    
    facts = get_all_facts()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📄 Total Documents", len(all_docs), delta=f"+{len(st.session_state.uploaded_files)} uploaded")
    with col2:
        processing = sum(1 for doc in all_docs if doc.get("status") == "Processing")
        processed = sum(1 for doc in all_docs if doc.get("status") == "Processed")
        st.metric("✅ Processed", processed, delta=f"{processing} processing")
    with col3:
        disputed_facts = sum(1 for fact in facts if fact.get("isDisputed"))
        st.metric("⚠️ Disputed Facts", disputed_facts, delta=f"{len(facts) - disputed_facts} undisputed")
    with col4:
        categories = len(set(doc_set["category"] for doc_set in st.session_state.document_sets))
        st.metric("📂 Document Sets", len(st.session_state.document_sets), delta=f"{categories} categories")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick actions with improved design
    st.subheader("🚀 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📤 Upload Documents", use_container_width=True, type="primary"):
            st.session_state.view = "Upload"
            st.rerun()
    
    with col2:
        if st.button("📊 Analyze Facts", use_container_width=True):
            st.session_state.view = "Facts"
            st.rerun()
    
    with col3:
        if st.button("📁 Browse Documents", use_container_width=True):
            st.session_state.view = "Documents"
            st.rerun()
    
    with col4:
        if st.button("📈 View Timeline", use_container_width=True):
            st.session_state.view = "Timeline"
            st.rerun()
    
    # Two-column layout for recent activity and document sets
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📈 Recent Activity")
        if st.session_state.recent_activities:
            for activity in st.session_state.recent_activities[:5]:
                icon = "📤" if activity["type"] == "upload" else "➕" if activity["type"] == "create" else "👁️"
                st.markdown(f"""
                <div style="background: white; padding: 12px; margin-bottom: 8px; border-radius: 6px; border-left: 3px solid #4D68F9; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <div style="display: flex; justify-content: between; align-items: center;">
                        <span style="font-weight: 500;">{icon} {activity['action']}</span>
                        <span style="color: #6b7280; font-size: 12px; margin-left: auto;">{activity['time']}</span>
                    </div>
                    <div style="color: #6b7280; font-size: 14px; margin-top: 4px;">{activity['item']}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No recent activity. Start by uploading some documents!")
    
    with col2:
        st.subheader("📁 Document Sets Overview")
        if st.session_state.document_sets:
            for doc_set in st.session_state.document_sets[:5]:
                doc_count = len(doc_set["documents"])
                party_color = "#3b82f6" if doc_set["party"] == "Appellant" else "#ef4444" if doc_set["party"] == "Respondent" else "#6b7280"
                
                st.markdown(f"""
                <div style="background: white; padding: 12px; margin-bottom: 8px; border-radius: 6px; border-left: 3px solid {party_color}; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <div style="display: flex; justify-content: between; align-items: center;">
                        <span style="font-weight: 500;">📂 {doc_set['name']}</span>
                        <span style="color: {party_color}; font-size: 12px; font-weight: 500; margin-left: auto;">{doc_set['party']}</span>
                    </div>
                    <div style="color: #6b7280; font-size: 14px; margin-top: 4px;">{doc_count} documents</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No document sets created yet.")

# Main application
def main():
    # Get data for JavaScript in facts view
    args_data = get_argument_data()
    facts_data = get_all_facts()
    document_sets = st.session_state.document_sets
    timeline_data = get_timeline_data()
    
    # Add Streamlit sidebar with navigation buttons
    with st.sidebar:
        # Add the logo and CaseLens text (original design)
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
        
        # Enhanced CSS
        st.markdown("""
        <style>
        /* Enhanced button styling */
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            height: 50px;
            margin-bottom: 12px;
            transition: all 0.3s ease;
            font-weight: 500;
            border: none;
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        }
        
        .stButton > button:active {
            transform: translateY(0);
        }
        
        /* Enhanced badge styling */
        .badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-right: 6px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: all 0.2s ease;
        }
        
        .badge:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        
        .appellant-badge {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            color: white;
        }
        
        .respondent-badge {
            background: linear-gradient(135deg, #ef4444, #dc2626);
            color: white;
        }
        
        .shared-badge {
            background: linear-gradient(135deg, #6b7280, #4b5563);
            color: white;
        }
        
        .status-processed {
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
        }
        
        .status-processing {
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: white;
        }
        
        .status-error {
            background: linear-gradient(135deg, #ef4444, #dc2626);
            color: white;
        }
        
        /* Enhanced file uploader */
        [data-testid="stFileUploader"] {
            border: 2px dashed #cbd5e1;
            border-radius: 12px;
            padding: 20px;
            background: linear-gradient(135deg, #f8fafc, #f1f5f9);
            transition: all 0.3s ease;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #4D68F9;
            background: linear-gradient(135deg, #f0f5ff, #e0e7ff);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(77, 104, 249, 0.15);
        }
        
        /* Enhanced form styling */
        [data-testid="stForm"] {
            background: white;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        
        /* Enhanced metric styling */
        [data-testid="metric-container"] {
            background: white;
            border: 1px solid #e1e5e9;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        [data-testid="metric-container"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        
        /* Progress bar styling */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #4D68F9, #667eea);
        }
        
        /* Enhanced dataframe styling */
        .dataframe {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        /* Loading animation */
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .loading {
            animation: pulse 1.5s infinite;
        }
        
        /* Success animation */
        @keyframes bounce {
            0%, 20%, 60%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            80% { transform: translateY(-5px); }
        }
        
        .success-bounce {
            animation: bounce 0.6s ease;
        }
        
        /* File type icons with better styling */
        .file-icon {
            font-size: 24px;
            margin-right: 8px;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
        }
        
        /* Document card enhancements */
        .document-card {
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .document-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Button click handler
        def set_view(view_name):
            st.session_state.view = view_name
        
        # Original order of buttons with Upload Documents first
        st.button("📤 Upload Documents", key="upload_button", on_click=set_view, args=("Upload",), use_container_width=True)
        st.button("📑 Arguments", key="args_button", on_click=set_view, args=("Arguments",), use_container_width=True)
        st.button("📊 Facts", key="facts_button", on_click=set_view, args=("Facts",), use_container_width=True)
        st.button("📁 Exhibits", key="exhibits_button", on_click=set_view, args=("Exhibits",), use_container_width=True)
    
    # Render the appropriate view based on session state
    if st.session_state.view == "Upload":
        render_upload_page()
    elif st.session_state.view == "Facts":
        render_facts_page(facts_data, document_sets, timeline_data, args_data)
    else:
        # Placeholder for other views        
        st.title(f"{st.session_state.view} View")
        st.info(f"This is a placeholder for the {st.session_state.view} view.")

# Function to render the enhanced upload page
def render_upload_page():
    """Enhanced upload page with better UX"""
    st.title("📤 Document Management")
    
    # Enhanced quick upload section
    st.markdown("### 🚀 Quick Upload")
    st.markdown("Drop files here for intelligent auto-categorization, or use organized upload below for manual control.")
    
    # Enhanced drag-and-drop area
    st.markdown("""
    <div style="border: 2px dashed #4D68F9; border-radius: 12px; padding: 40px; text-align: center; background: linear-gradient(135deg, #f0f5ff, #e0e7ff); margin-bottom: 30px; transition: all 0.3s ease;">
        <div style="font-size: 48px; margin-bottom: 15px;">📁</div>
        <h3 style="color: #4D68F9; margin-bottom: 10px;">Smart Document Upload</h3>
        <p style="color: #6b7280; margin-bottom: 20px;">Files will be automatically analyzed and categorized</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced file uploader
    quick_upload = st.file_uploader(
        "Drag and drop files here or click to browse",
        type=["pdf", "docx", "txt", "jpg", "png", "xlsx", "csv"],
        accept_multiple_files=True,
        help="Supported: PDF, Word, Text, Images, Excel, CSV. Files will be analyzed automatically.",
        key="quick_upload"
    )
    
    if quick_upload:
        st.success(f"📁 {len(quick_upload)} file(s) ready for processing")
        
        # Show file analysis preview
        with st.expander("📋 View File Analysis Preview", expanded=True):
            for uploaded_file in quick_upload:
                analysis = analyze_document_content(uploaded_file.name)
                
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"""
                    <div style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 4px solid #4D68F9;">
                        <div style="display: flex; align-items: center; margin-bottom: 8px;">
                            <span style="font-size: 20px; margin-right: 10px;">{get_file_icon(uploaded_file.type.split('/')[-1] if uploaded_file.type else "")}</span>
                            <strong>{uploaded_file.name}</strong>
                        </div>
                        <div style="font-size: 14px; color: #6b7280;">
                            📂 Suggested Category: <strong>{analysis['suggested_category']}</strong> ({analysis['confidence']:.0%} confidence)<br>
                            ⚖️ Suggested Party: <strong>{analysis['suggested_party']}</strong><br>
                            📏 Size: {uploaded_file.size/1024:.1f} KB
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"**Confidence: {analysis['confidence']:.0%}**")
                    if analysis['confidence'] < 0.7:
                        st.warning("⚠️ Low confidence - manual review recommended")
                    else:
                        st.success("✅ High confidence")
        
        if st.button("🔄 Process All Files Automatically", type="primary", use_container_width=True):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, uploaded_file in enumerate(quick_upload):
                status_text.text(f"📄 Processing {uploaded_file.name}...")
                progress_bar.progress((i + 1) / len(quick_upload))
                
                # Process the file with enhanced analysis
                doc_data = process_uploaded_file(uploaded_file)
                if doc_data:
                    analysis = doc_data['analysis']
                    category = analysis['suggested_category']
                    
                    # Auto-create or find document set
                    existing_set = next((ds for ds in st.session_state.document_sets if ds["name"] == category), None)
                    if not existing_set:
                        set_id = add_document_set(category, analysis['suggested_party'])
                    else:
                        set_id = existing_set["id"]
                    
                    # Add document to set
                    doc_id = add_document_to_set(uploaded_file.name, analysis['suggested_party'], set_id, doc_data)
                    if doc_id:
                        save_uploaded_file(uploaded_file, set_id, doc_id)
            
            progress_bar.progress(1.0)
            status_text.text("✅ All documents processed successfully!")
            
            st.balloons()
            st.success(f"🎉 Successfully processed {len(quick_upload)} documents with AI analysis!")
            
            # Show processing results
            st.markdown("### 📊 Processing Results")
            for uploaded_file in quick_upload:
                st.markdown(f"✅ **{uploaded_file.name}** - Categorized and analyzed")
    
    st.markdown("---")
    
    # Enhanced organized upload tabs
    tab1, tab2, tab3 = st.tabs(["📄 Organized Upload", "📁 Manage Document Sets", "🕒 Recent Activity"])
    
    with tab1:
        st.subheader("📄 Organized Upload")
        st.markdown("Upload documents to specific categories with manual control.")
        
        # Enhanced document set selection
        if st.session_state.document_sets:
            st.markdown("#### 📂 Select Document Set")
            
            # Grid layout for document sets
            cols = st.columns(2)
            for i, doc_set in enumerate(st.session_state.document_sets):
                with cols[i % 2]:
                    party_color = "#3b82f6" if doc_set["party"] == "Appellant" else "#ef4444" if doc_set["party"] == "Respondent" else "#6b7280"
                    
                    if st.button(
                        f"📂 {doc_set['name']}\n{len(doc_set['documents'])} documents | {doc_set['party']}",
                        key=f"select_set_{doc_set['id']}",
                        use_container_width=True
                    ):
                        st.session_state.selected_set = doc_set["id"]
                        st.session_state.creating_set = False
        
        # Enhanced upload form
        if st.session_state.selected_set:
            selected_set = next((ds for ds in st.session_state.document_sets if ds["id"] == st.session_state.selected_set), None)
            if selected_set:
                st.markdown(f"#### 📤 Uploading to: **{selected_set['name']}**")
                
                with st.form("organized_upload_form", clear_on_submit=True):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        doc_name = st.text_input("📝 Document Name", placeholder="Enter document name or title")
                        
                        party_options = ["Appellant", "Respondent", "Shared"]
                        default_party = selected_set["party"] if selected_set["party"] != "Mixed" else "Shared"
                        default_index = party_options.index(default_party) if default_party in party_options else 0
                        doc_party = st.selectbox("⚖️ Party", party_options, index=default_index)
                    
                    with col2:
                        uploaded_file = st.file_uploader(
                            "📎 Select File",
                            type=["pdf", "docx", "txt", "jpg", "png", "xlsx", "csv"]
                        )
                        
                        if uploaded_file:
                            st.success(f"✅ File selected: {uploaded_file.name}")
                    
                    col1, col2, col3 = st.columns([1, 1, 1])
                    with col2:
                        submit_btn = st.form_submit_button("📤 Upload Document", use_container_width=True, type="primary")
                    
                    if submit_btn:
                        if not doc_name:
                            st.error("❌ Please provide a document name")
                        elif not uploaded_file:
                            st.error("❌ Please select a file")
                        else:
                            # Enhanced processing
                            with st.spinner("🔄 Processing document..."):
                                doc_data = process_uploaded_file(uploaded_file)
                                if doc_data:
                                    doc_id = add_document_to_set(doc_name, doc_party, st.session_state.selected_set, doc_data)
                                    if doc_id:
                                        if save_uploaded_file(uploaded_file, st.session_state.selected_set, doc_id):
                                            st.success(f"🎉 Successfully uploaded: {doc_name}")
                                            st.session_state.selected_set = None
                                            st.rerun()
                                        else:
                                            st.error("❌ Error saving file")
                                    else:
                                        st.error("❌ Error adding document")
        
        # Enhanced create new set option
        st.markdown("---")
        st.markdown("#### ➕ Create New Document Set")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Create New Document Set", use_container_width=True):
                st.session_state.creating_set = True
        
        if st.session_state.creating_set:
            with st.form("new_set_form", clear_on_submit=True):
                st.markdown("**📁 Create Document Set**")
                
                col1, col2 = st.columns(2)
                with col1:
                    set_name = st.text_input("📝 Set Name", placeholder="e.g., Expert Reports, Contracts")
                with col2:
                    party_options = ["Appellant", "Respondent", "Mixed", "Shared"]
                    set_party = st.selectbox("⚖️ Party", party_options)
                
                col1, col2, col3 = st.columns([1, 1, 1])
                with col2:
                    create_btn = st.form_submit_button("✨ Create Set", use_container_width=True, type="primary")
                
                if create_btn:
                    if not set_name:
                        st.error("❌ Please provide a name for this document set")
                    else:
                        set_id = add_document_set(set_name, set_party)
                        st.session_state.selected_set = set_id
                        st.session_state.creating_set = False
                        st.success(f"🎉 Created: {set_name}")
                        st.rerun()
    
    with tab2:
        st.subheader("📁 Manage Document Sets")
        
        if not st.session_state.document_sets:
            st.markdown("""
            <div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #f8fafc, #f1f5f9); border-radius: 12px; border: 2px dashed #cbd5e1;">
                <div style="font-size: 48px; margin-bottom: 15px;">📂</div>
                <h3 style="color: #374151; margin-bottom: 10px;">No Document Sets Yet</h3>
                <p style="color: #6b7280;">Create your first document set to organize your legal documents</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Enhanced search
            search_term = st.text_input("🔍 Search document sets", placeholder="Search by name, category, or party...")
            
            filtered_sets = st.session_state.document_sets
            if search_term:
                filtered_sets = [ds for ds in st.session_state.document_sets 
                                if search_term.lower() in ds['name'].lower() or 
                                   search_term.lower() in ds['category'].lower() or
                                   search_term.lower() in ds['party'].lower()]
            
            # Enhanced document set display
            for doc_set in filtered_sets:
                with st.expander(f"📂 {doc_set['name']} ({len(doc_set['documents'])} documents)", expanded=False):
                    # Enhanced set details
                    party_color = "#3b82f6" if doc_set["party"] == "Appellant" else "#ef4444" if doc_set["party"] == "Respondent" else "#6b7280"
                    
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.markdown(f"""
                        <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid {party_color};">
                            <h4 style="margin: 0; color: #1f2937;">{doc_set['name']}</h4>
                            <div style="margin-top: 10px;">
                                <span style="background: {party_color}; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;">
                                    {doc_set["party"]}
                                </span>
                                <span style="background: #f3f4f6; color: #374151; padding: 4px 12px; border-radius: 20px; font-size: 12px; margin-left: 8px;">
                                    {doc_set["category"]}
                                </span>
                            </div>
                            <div style="margin-top: 10px; font-size: 14px; color: #6b7280;">
                                📅 Created: {doc_set.get('created_date', 'Unknown')} | 📊 Status: {doc_set.get('status', 'Active')}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        # Quick stats
                        total_docs = len(doc_set["documents"])
                        uploaded_docs = sum(1 for doc in doc_set["documents"] 
                                           if f"{doc_set['id']}-{doc['id']}" in st.session_state.uploaded_files)
                        completion = int(uploaded_docs/total_docs*100) if total_docs > 0 else 0
                        
                        st.metric("📊 Completion", f"{completion}%", delta=f"{uploaded_docs}/{total_docs}")
                    
                    # Enhanced document table
                    if doc_set["documents"]:
                        doc_data = []
                        for doc in doc_set["documents"]:
                            file_key = f"{doc_set['id']}-{doc['id']}"
                            status = "✅ Uploaded" if file_key in st.session_state.uploaded_files else "❌ Missing"
                            size = f"{st.session_state.uploaded_files[file_key]['size']/1024:.1f} KB" if file_key in st.session_state.uploaded_files else ""
                            
                            doc_data.append({
                                "📄 Name": f"{doc.get('icon', '📎')} {doc['name']}",
                                "⚖️ Party": doc["party"],
                                "📊 Status": doc.get("status", "Unknown"),
                                "📁 File Status": status,
                                "📏 Size": size
                            })
                        
                        df = pd.DataFrame(doc_data)
                        st.dataframe(df, use_container_width=True, height=200)
                        
                        # Enhanced action buttons
                        col1, col2, col3, col4 = st.columns(4)
                        
                        with col1:
                            if st.button(f"➕ Add Document", key=f"add_to_{doc_set['id']}"):
                                st.session_state.selected_set = doc_set["id"]
                                st.session_state.view = "Upload"
                                st.rerun()
                        
                        with col2:
                            csv = df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label="📥 Export CSV",
                                data=csv,
                                file_name=f"{doc_set['name']}_documents.csv",
                                mime='text/csv',
                                key=f"export_{doc_set['id']}"
                            )
                        
                        with col3:
                            if st.button(f"📊 Analytics", key=f"analytics_{doc_set['id']}"):
                                st.info("📈 Analytics feature coming soon!")
                        
                        with col4:
                            if st.button(f"🔍 View Details", key=f"view_{doc_set['id']}"):
                                st.session_state.viewing_set = doc_set["id"] if st.session_state.viewing_set != doc_set["id"] else None
    
    with tab3:
        st.subheader("🕒 Recent Activity")
        
        if st.session_state.recent_activities:
            for activity in st.session_state.recent_activities:
                icon = "📤" if activity["type"] == "upload" else "➕" if activity["type"] == "create" else "👁️"
                
                st.markdown(f"""
                <div style="background: white; border-radius: 10px; padding: 20px; margin-bottom: 15px; border-left: 4px solid #4D68F9; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <div style="display: flex; justify-content: between; align-items: center;">
                        <div style="display: flex; align-items: center;">
                            <span style="font-size: 20px; margin-right: 12px;">{icon}</span>
                            <div>
                                <div style="font-weight: 600; color: #1f2937;">{activity['action']}</div>
                                <div style="color: #6b7280; font-size: 14px; margin-top: 2px;">{activity['item']}</div>
                            </div>
                        </div>
                        <span style="color: #9ca3af; font-size: 12px; margin-left: auto;">{activity['time']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #f8fafc, #f1f5f9); border-radius: 12px;">
                <div style="font-size: 48px; margin-bottom: 15px;">📊</div>
                <h3 style="color: #374151; margin-bottom: 10px;">No Recent Activity</h3>
                <p style="color: #6b7280;">Your recent document uploads and activities will appear here</p>
            </div>
            """, unsafe_allow_html=True)

# Function to render the facts page (kept the same but with breadcrumbs)
def render_facts_page(facts_data, document_sets, timeline_data, args_data):
    # Convert data to JSON for JavaScript
    args_json = json.dumps(args_data)
    facts_json = json.dumps(facts_data)
    document_sets_json = json.dumps(document_sets)
    timeline_json = json.dumps(timeline_data)
    
    # Create HTML content for the Facts view (same as before)
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Same styles as before */
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                margin: 0;
                padding: 0;
                background-color: #fff;
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            .content-section {{
                display: none;
            }}
            
            .content-section.active {{
                display: block;
            }}
            
            .badge {{
                display: inline-block;
                padding: 3px 8px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 500;
            }}
            
            .appellant-badge {{
                background-color: rgba(49, 130, 206, 0.1);
                color: #3182ce;
            }}
            
            .respondent-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            .shared-badge {{
                background-color: rgba(128, 128, 128, 0.1);
                color: #666;
            }}
            
            .exhibit-badge {{
                background-color: rgba(221, 107, 32, 0.1);
                color: #dd6b20;
            }}
            
            .disputed-badge {{
                background-color: rgba(229, 62, 62, 0.1);
                color: #e53e3e;
            }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            
            th {{
                text-align: left;
                padding: 12px;
                background-color: #fafafa;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            td {{
                padding: 12px;
                border-bottom: 1px solid #f0f0f0;
            }}
            
            tr.disputed {{
                background-color: rgba(229, 62, 62, 0.05);
            }}
            
            .action-buttons {{
                position: absolute;
                top: 20px;
                right: 20px;
                display: flex;
                gap: 10px;
            }}
            
            .action-button {{
                padding: 8px 16px;
                background-color: #f9f9f9;
                border: 1px solid #e1e4e8;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                cursor: pointer;
            }}
            
            .action-button:hover {{
                background-color: #f1f1f1;
            }}
            
            .copy-notification {{
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: #2d3748;
                color: white;
                padding: 10px 20px;
                border-radius: 4px;
                z-index: 1000;
                opacity: 0;
                transition: opacity 0.3s;
            }}
            
            .copy-notification.show {{
                opacity: 1;
            }}
            
            .facts-container {{
                margin-top: 20px;
            }}
            
            .facts-header {{
                display: flex;
                margin-bottom: 20px;
                border-bottom: 1px solid #dee2e6;
            }}
            
            .tab-button {{
                padding: 10px 20px;
                background: none;
                border: none;
                cursor: pointer;
            }}
            
            .tab-button.active {{
                border-bottom: 2px solid #4299e1;
                color: #4299e1;
                font-weight: 500;
            }}
            
            .facts-content {{
                margin-top: 20px;
            }}
            
            .section-title {{
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1rem;
                padding-bottom: 0.5rem;
                border-bottom: 1px solid #eaeaea;
            }}
            
            .table-view {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            
            .table-view th {{
                padding: 12px;
                text-align: left;
                background-color: #f8f9fa;
                border-bottom: 2px solid #dee2e6;
                position: sticky;
                top: 0;
                cursor: pointer;
            }}
            
            .table-view th:hover {{
                background-color: #e9ecef;
            }}
            
            .table-view td {{
                padding: 12px;
                border-bottom: 1px solid #dee2e6;
            }}
            
            .table-view tr:hover {{
                background-color: #f8f9fa;
            }}
            
            .view-toggle {{
                display: flex;
                justify-content: flex-end;
                margin-bottom: 16px;
            }}
            
            .view-toggle button {{
                padding: 8px 16px;
                border: 1px solid #e2e8f0;
                background-color: #f7fafc;
                cursor: pointer;
            }}
            
            .view-toggle button.active {{
                background-color: #4299e1;
                color: white;
                border-color: #4299e1;
            }}
            
            .view-toggle button:first-child {{
                border-radius: 4px 0 0 4px;
            }}
            
            .view-toggle button:not(:first-child):not(:last-child) {{
                border-radius: 0;
                border-left: none;
                border-right: none;
            }}
            
            .view-toggle button:last-child {{
                border-radius: 0 4px 4px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div id="copy-notification" class="copy-notification">Content copied to clipboard!</div>
            
            <div class="action-buttons">
                <button class="action-button" onclick="copyAllContent()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                    Copy
                </button>
            </div>
            
            <div id="facts" class="content-section active">
                <div class="section-title">Case Facts</div>
                
                <div class="view-toggle">
                    <button id="table-view-btn" class="active" onclick="switchView('table')">Table View</button>
                    <button id="docset-view-btn" onclick="switchView('docset')">Document Categories</button>
                    <button id="timeline-view-btn" onclick="switchView('timeline')">Timeline View</button>
                </div>
                
                <div class="facts-header">
                    <button class="tab-button active" id="all-facts-btn" onclick="switchFactsTab('all')">All Facts</button>
                    <button class="tab-button" id="disputed-facts-btn" onclick="switchFactsTab('disputed')">Disputed Facts</button>
                    <button class="tab-button" id="undisputed-facts-btn" onclick="switchFactsTab('undisputed')">Undisputed Facts</button>
                </div>
                
                <div id="table-view-content" class="facts-content">
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
                        <tbody id="facts-table-body"></tbody>
                    </table>
                </div>
                
                <div id="timeline-view-content" class="facts-content" style="display: none;">
                    Timeline content would go here
                </div>
                
                <div id="docset-view-content" class="facts-content" style="display: none;">
                    Document categories content would go here
                </div>
            </div>
        </div>
        
        <script>
            const factsData = {facts_json};
            const documentSets = {document_sets_json};
            const timelineData = {timeline_json};
            
            function switchView(viewType) {{
                const tableBtn = document.getElementById('table-view-btn');
                const timelineBtn = document.getElementById('timeline-view-btn');
                const docsetBtn = document.getElementById('docset-view-btn');
                
                const tableContent = document.getElementById('table-view-content');
                const timelineContent = document.getElementById('timeline-view-content');
                const docsetContent = document.getElementById('docset-view-content');
                
                tableBtn.classList.remove('active');
                timelineBtn.classList.remove('active');
                docsetBtn.classList.remove('active');
                
                tableContent.style.display = 'none';
                timelineContent.style.display = 'none';
                docsetContent.style.display = 'none';
                
                if (viewType === 'table') {{
                    tableBtn.classList.add('active');
                    tableContent.style.display = 'block';
                    renderFacts();
                }} else if (viewType === 'timeline') {{
                    timelineBtn.classList.add('active');
                    timelineContent.style.display = 'block';
                }} else if (viewType === 'docset') {{
                    docsetBtn.classList.add('active');
                    docsetContent.style.display = 'block';
                }}
            }}
            
            function switchFactsTab(tabType) {{
                const allBtn = document.getElementById('all-facts-btn');
                const disputedBtn = document.getElementById('disputed-facts-btn');
                const undisputedBtn = document.getElementById('undisputed-facts-btn');
                
                allBtn.classList.remove('active');
                disputedBtn.classList.remove('active');
                undisputedBtn.classList.remove('active');
                
                if (tabType === 'all') {{
                    allBtn.classList.add('active');
                }} else if (tabType === 'disputed') {{
                    disputedBtn.classList.add('active');
                }} else {{
                    undisputedBtn.classList.add('active');
                }}
                
                renderFacts(tabType);
            }}
            
            function copyAllContent() {{
                const notification = document.getElementById('copy-notification');
                notification.classList.add('show');
                
                setTimeout(() => {{
                    notification.classList.remove('show');
                }}, 2000);
            }}
            
            function sortTable(tableId, columnIndex) {{
                // Sorting logic would go here
            }}
            
            function renderFacts(type = 'all') {{
                const tableBody = document.getElementById('facts-table-body');
                tableBody.innerHTML = '';
                
                let filteredFacts = factsData;
                
                if (type === 'disputed') {{
                    filteredFacts = factsData.filter(fact => fact.isDisputed);
                }} else if (type === 'undisputed') {{
                    filteredFacts = factsData.filter(fact => !fact.isDisputed);
                }}
                
                filteredFacts.forEach(fact => {{
                    const row = document.createElement('tr');
                    if (fact.isDisputed) {{
                        row.classList.add('disputed');
                    }}
                    
                    const dateCell = document.createElement('td');
                    dateCell.textContent = fact.date;
                    row.appendChild(dateCell);
                    
                    const eventCell = document.createElement('td');
                    eventCell.textContent = fact.point;
                    row.appendChild(eventCell);
                    
                    const partyCell = document.createElement('td');
                    partyCell.innerHTML = `<span class="badge ${{fact.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}}">${{fact.party}}</span>`;
                    row.appendChild(partyCell);
                    
                    const statusCell = document.createElement('td');
                    statusCell.innerHTML = fact.isDisputed ? 
                        '<span class="badge disputed-badge">Disputed</span>' : 
                        'Undisputed';
                    row.appendChild(statusCell);
                    
                    const argCell = document.createElement('td');
                    argCell.textContent = `${{fact.argId}}. ${{fact.argTitle}}`;
                    row.appendChild(argCell);
                    
                    const evidenceCell = document.createElement('td');
                    if (fact.exhibits && fact.exhibits.length > 0) {{
                        evidenceCell.innerHTML = fact.exhibits.map(ex => 
                            `<span class="badge exhibit-badge">${{ex}}</span>`
                        ).join(' ');
                    }} else {{
                        evidenceCell.textContent = 'None';
                    }}
                    row.appendChild(evidenceCell);
                    
                    tableBody.appendChild(row);
                }});
            }}
            
            document.addEventListener('DOMContentLoaded', function() {{
                renderFacts('all');
            }});
            
            renderFacts('all');
        </script>
    </body>
    </html>
    """
    
    st.title("📊 Case Facts")
    components.html(html_content, height=800, scrolling=True)

# Run the main app
if __name__ == "__main__":
    main()
