import streamlit as st
import pandas as pd
from datetime import datetime

# Configure page settings
st.set_page_config(
    page_title="Legal Arguments Comparison",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px;
        border-radius: 4px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #E8F0FE;
    }
    .evidence-box {
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #E0E0E0;
        margin: 4px 0;
        transition: all 0.3s ease;
    }
    .evidence-box:hover {
        background-color: #F8F9FA;
        border-color: #6C63FF;
        transform: translateX(5px);
    }
    .case-badge {
        background-color: #F3F4F6;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.9em;
        display: inline-block;
        margin: 2px;
    }
    .filter-pill {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 16px;
        margin: 2px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Extended sample data
argument_data = [
    {
        "id": "1",
        "issue": "Patent Infringement - AI Technology",
        "category": "intellectual_property",
        "tags": ["AI", "patents", "technology", "software"],
        "appellant": {
            "mainArgument": "Our AI Patent Rights Were Infringed",
            "details": [
                "Defendant's AI system uses our patented neural network architecture",
                "Source code analysis shows identical implementation methods",
                "Patent was filed and granted before defendant's product launch"
            ],
            "evidence": [
                {"id": "C1", "desc": "Patent Filing #US123456 - Neural Network Architecture", "type": "document"},
                {"id": "C2", "desc": "Source Code Comparison Analysis by Dr. Smith", "type": "expert_report"},
                {"id": "C3", "desc": "Product Launch Timeline Documentation", "type": "timeline"}
            ],
            "caselaw": ["TechCorp v. AI Solutions 2023", "Neural Systems v. DataCo 2022"]
        },
        "respondent": {
            "mainArgument": "Independent Development with Different Architecture",
            "details": [
                "Our AI system uses fundamentally different architecture",
                "Development predates plaintiff's patent filing",
                "Implementation uses publicly available methods"
            ],
            "evidence": [
                {"id": "R1", "desc": "Technical Architecture Documentation", "type": "document"},
                {"id": "R2", "desc": "Development Timeline with Git Commits", "type": "timeline"},
                {"id": "R3", "desc": "Expert Analysis of Architectural Differences", "type": "expert_report"}
            ],
            "caselaw": ["AI Corp v. Tech Innovations 2023", "Software Patents LLC v. DevCo 2022"]
        }
    },
    {
        "id": "2",
        "issue": "Environmental Compliance - Carbon Emissions",
        "category": "environmental",
        "tags": ["emissions", "compliance", "regulations", "environmental"],
        "appellant": {
            "mainArgument": "Emissions Standards Fully Met",
            "details": [
                "All monitoring systems show compliance with regulations",
                "Third-party audits confirm emission levels within limits",
                "Implemented best available control technology"
            ],
            "evidence": [
                {"id": "C4", "desc": "Continuous Emissions Monitoring Data 2022-2023", "type": "data"},
                {"id": "C5", "desc": "Independent Environmental Audit Report", "type": "audit"},
                {"id": "C6", "desc": "Technology Implementation Certificates", "type": "certification"}
            ],
            "caselaw": ["GreenTech v. EPA 2023", "Clean Air Corp v. State 2022"]
        },
        "respondent": {
            "mainArgument": "Multiple Violations of Emission Standards",
            "details": [
                "Monitoring data shows repeated excess emissions",
                "Failed to implement required control measures",
                "Inadequate reporting of emission events"
            ],
            "evidence": [
                {"id": "R4", "desc": "EPA Violation Notices", "type": "notice"},
                {"id": "R5", "desc": "Inspector Field Reports", "type": "report"},
                {"id": "R6", "desc": "Emission Event Analysis", "type": "data"}
            ],
            "caselaw": ["EPA v. Industrial Co. 2023", "State v. Emissions Corp 2022"]
        }
    },
    {
        "id": "3",
        "issue": "Employment Discrimination",
        "category": "employment",
        "tags": ["discrimination", "HR", "workplace", "employment"],
        "appellant": {
            "mainArgument": "Systematic Discrimination in Promotion Practices",
            "details": [
                "Statistical evidence shows bias in promotion decisions",
                "Qualified candidates consistently overlooked",
                "Internal complaints were ignored"
            ],
            "evidence": [
                {"id": "C7", "desc": "Statistical Analysis of Promotion Data", "type": "data"},
                {"id": "C8", "desc": "Employee Qualification Comparisons", "type": "analysis"},
                {"id": "C9", "desc": "HR Complaint Records", "type": "document"}
            ],
            "caselaw": ["Smith v. Corp Inc 2023", "Workplace Rights v. BigCo 2022"]
        },
        "respondent": {
            "mainArgument": "Merit-Based Decisions Following Policy",
            "details": [
                "Promotions based on objective performance metrics",
                "All candidates evaluated using standard criteria",
                "Complete documentation of decision process"
            ],
            "evidence": [
                {"id": "R7", "desc": "Performance Evaluation Records", "type": "document"},
                {"id": "R8", "desc": "Promotion Policy Documentation", "type": "policy"},
                {"id": "R9", "desc": "Decision Committee Minutes", "type": "document"}
            ],
            "caselaw": ["Johnson v. Enterprise Corp 2023", "Merit Systems v. Workers Union 2022"]
        }
    }
]

def display_evidence(evidence_list, color):
    for item in evidence_list:
        type_icon = {
            "document": "📄",
            "expert_report": "👨‍🔬",
            "timeline": "📅",
            "data": "📊",
            "audit": "🔍",
            "certification": "✅",
            "notice": "⚠️",
            "report": "📝",
            "analysis": "📈",
            "policy": "📋"
        }.get(item.get('type', 'document'), "📄")
        
        st.markdown(
            f"""
            <div class="evidence-box" style="border-left: 4px solid {color}">
                <strong style="color: {color}">{item['id']}</strong> {type_icon}<br/>
                {item['desc']}
            </div>
            """,
            unsafe_allow_html=True
        )

def display_case_law(cases, color):
    for case in cases:
        st.markdown(
            f"""
            <span class="case-badge" style="color: {color}">
                {case} 📋
            </span>
            """,
            unsafe_allow_html=True
        )

# App header
st.title("⚖️ Legal Arguments Comparison")

# Advanced search and filtering
col1, col2 = st.columns([2, 1])

with col1:
    search = st.text_input("🔍 Search issues, arguments, or evidence...", "")

with col2:
    # Get all unique tags
    all_tags = set()
    for arg in argument_data:
        all_tags.update(arg.get('tags', []))
    selected_tags = st.multiselect("Filter by tags", list(all_tags))

# Get all unique evidence types
evidence_types = set()
for arg in argument_data:
    for evidence in arg['appellant']['evidence'] + arg['respondent']['evidence']:
        evidence_types.add(evidence.get('type', 'document'))

selected_types = st.multiselect("Filter by evidence type", list(evidence_types))

# Filter data based on search, tags, and evidence types
filtered_data = argument_data
if search:
    filtered_data = [
        arg for arg in filtered_data
        if (search.lower() in arg["issue"].lower() or
            search.lower() in arg["appellant"]["mainArgument"].lower() or
            search.lower() in arg["respondent"]["mainArgument"].lower() or
            any(search.lower() in detail.lower() for detail in arg["appellant"]["details"]) or
            any(search.lower() in detail.lower() for detail in arg["respondent"]["details"]) or
            any(search.lower() in ev["desc"].lower() for ev in arg["appellant"]["evidence"]) or
            any(search.lower() in ev["desc"].lower() for ev in arg["respondent"]["evidence"]))
    ]

if selected_tags:
    filtered_data = [
        arg for arg in filtered_data
        if any(tag in arg.get('tags', []) for tag in selected_tags)
    ]

if selected_types:
    filtered_data = [
        arg for arg in filtered_data
        if any(ev.get('type', 'document') in selected_types 
               for ev in arg['appellant']['evidence'] + arg['respondent']['evidence'])
    ]

# Display active filters
if selected_tags or selected_types:
    st.markdown("**Active Filters:**")
    for tag in selected_tags:
        st.markdown(f'<span class="filter-pill" style="background-color: #E8F0FE; color: #1A73E8;">#{tag}</span>', unsafe_allow_html=True)
    for type_ in selected_types:
        st.markdown(f'<span class="filter-pill" style="background-color: #FDE7F3; color: #B31B72;">{type_}</span>', unsafe_allow_html=True)

# Create tabs for different categories
categories = list(set(arg["category"] for arg in filtered_data))
tabs = st.tabs([category.replace('_', ' ').title() for category in categories])

for tab, category in zip(tabs, categories):
    with tab:
        category_data = [arg for arg in filtered_data if arg["category"] == category]
        
        for arg in category_data:
            with st.expander(f"**{arg['issue']}**", expanded=True):
                # Tags display
                for tag in arg.get('tags', []):
                    st.markdown(f'<span class="filter-pill" style="background-color: #E8F0FE; color: #1A73E8;">#{tag}</span>', unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📤 Appellant's Position")
                    st.markdown(f"**Main Argument:**")
                    st.info(arg["appellant"]["mainArgument"])
                    
                    st.markdown("**Supporting Points:**")
                    for point in arg["appellant"]["details"]:
                        st.markdown(f"• {point}")
                    
                    st.markdown("**Evidence:**")
                    display_evidence(arg["appellant"]["evidence"], "#6C63FF")
                    
                    st.markdown("**Case Law:**")
                    display_case_law(arg["appellant"]["caselaw"], "#6C63FF")
                
                with col2:
                    st.subheader("📥 Respondent's Position")
                    st.markdown(f"**Main Argument:**")
                    st.error(arg["respondent"]["mainArgument"])
                    
                    st.markdown("**Supporting Points:**")
                    for point in arg["respondent"]["details"]:
                        st.markdown(f"• {point}")
                    
                    st.markdown("**Evidence:**")
                    display_evidence(arg["respondent"]["evidence"], "#FF6B6B")
                    
                    st.markdown("**Case Law:**")
                    display_case_law(arg["respondent"]["caselaw"], "#FF6B6B")

# Summary table
if st.button("📊 Generate Summary Table"):
    summary_data = []
    for arg in filtered_data:
        summary_data.append({
            "Issue": arg["issue"],
            "Category": arg["category"].replace('_', ' ').title(),
            "Tags": ", ".join(arg.get('tags', [])),
            "Appellant Position": arg["appellant"]["mainArgument"],
            "Respondent Position": arg["respondent"]["mainArgument"],
            "Evidence Count": len(arg["appellant"]["evidence"]) + len(arg["respondent"]["evidence"])
        })
    
    df = pd.DataFrame(summary_data)
    st.dataframe(df, use_container_width=True)

# Export functionality
if st.download_button(
    label="📥 Export Data",
    data=pd.DataFrame(summary_data).to_csv(index=False),
    file_name=f"legal_arguments_summary_{datetime.now().strftime('%Y%m%d')}.csv",
    mime="text/csv"
):
    st.success("Data exported successfully!")

# Statistics
st.sidebar.markdown("### 📊 Case Statistics")
st.sidebar.markdown(f"Total Cases: {len(filtered_data)}")
st.sidebar.markdown(f"Total Evidence Items: {sum(len(arg['appellant']['evidence']) + len(arg['respondent']['evidence']) for arg in filtered_data)}")
st.sidebar.markdown(f"Active Filters: {len(selected_tags) + len(selected_types)}")

# Footer
st.markdown("---")
st.markdown("*Last updated: {}*".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
