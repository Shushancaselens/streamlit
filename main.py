# Case Law
    st.markdown("""
        <div style="margin: 40px 0 20px 0;">
            <h5 style="margin-bottom: 16px;">Case Law</h5>
        </div>
    """, unsafe_allow_html=True)import streamlit as st
import pandas as pd
import json
from streamlit.components.v1 import html

# Set page config for wide layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .evidence-link {
        color: #4338ca;
        text-decoration: none;
        transition: all 0.2s;
    }
    .evidence-link:hover {
        color: #3730a3;
        text-decoration: underline;
    }
    .evidence-card {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        margin-bottom: 0.5rem;
        transition: all 0.2s;
    }
    .evidence-card:hover {
        border-color: #818cf8;
        background-color: #f5f7ff;
    }
</style>
""", unsafe_allow_html=True)

# Complete argument data
def get_case_summary(case_id):
    # Database of case summaries
    case_summaries = {
        "CAS 2019/A/XYZ": "Athlete successfully established jurisdiction based on federation rules explicitly allowing CAS appeals. Court emphasized importance of clear arbitration agreements.",
        "CAS 2019/A/123": "Appeal dismissed due to non-exhaustion of internal remedies. CAS emphasized need to follow proper procedural steps.",
        "CAS 2018/A/456": "Case established precedent for requiring completion of federation's internal processes before CAS jurisdiction.",
        "CAS 2018/A/ABC": "Court found chain-of-custody errors significant enough to invalidate test results. Set standards for sample handling.",
        "CAS 2017/A/789": "Minor procedural defects held insufficient to invalidate otherwise valid test results.",
        "Smith v. Corp Inc. 2021": "Court found lack of documented warnings and positive performance reviews inconsistent with termination for cause.",
        "Jones v. Enterprise Ltd 2020": "Established standards for progressive discipline in employment termination cases.",
        "Brown v. MegaCorp 2022": "Upheld immediate termination where serious misconduct was clearly documented.",
        "Wilson v. Tech Solutions 2021": "Court emphasized importance of contemporaneous documentation of verbal warnings.",
        "TechCo v. Innovate Inc. 2022": "Found patent infringement based on post-publication copying and substantial similarity.",
        "Patent Holdings v. StartUp 2021": "Emphasized importance of timeline evidence in patent infringement cases.",
        "Innovation Corp v. PatentCo 2023": "Independent development defense succeeded with clear pre-dating evidence.",
        "Tech Solutions v. IP Holdings 2022": "Court invalidated overly broad patent claims in software industry.",
        "EcoCorp v. EPA 2022": "Facility compliance upheld based on comprehensive monitoring data and third-party audits.",
        "Green Industries v. State 2021": "Established standards for environmental compliance documentation.",
        "EPA v. Industrial Corp 2023": "Violations found due to inadequate monitoring and delayed incident reporting.",
        "State v. Manufacturing Co. 2022": "Court emphasized importance of timely violation reporting and equipment maintenance."
    }
    return case_summaries.get(case_id, "Summary not available.")

argument_data = [
    {
        "id": "1",
        "issue": "CAS Jurisdiction",
        "category": "jurisdiction",
        "appellant": {
            "mainArgument": "CAS Has Authority to Hear This Case",
            "details": [
                "The Federation's Anti-Doping Rules explicitly allow CAS to hear appeals",
                "Athlete has completed all required internal appeal procedures first",
                "Athlete signed agreement allowing CAS to handle disputes"
            ],
            "evidence": [
                {"id": "C1", "desc": "Federation Rules, Art. 60"},
                {"id": "C2", "desc": "Athlete's license containing arbitration agreement"},
                {"id": "C3", "desc": "Appeal submission documents"}
            ],
            "caselaw": ["CAS 2019/A/XYZ"]
        },
        "respondent": {
            "mainArgument": "CAS Cannot Hear This Case Yet",
            "details": [
                "Athlete skipped required steps in federation's appeal process",
                "Athlete missed important appeal deadlines within federation",
                "Must follow proper appeal steps before going to CAS"
            ],
            "evidence": [
                {"id": "R1", "desc": "Federation internal appeals process documentation"},
                {"id": "R2", "desc": "Timeline of appeals process"},
                {"id": "R3", "desc": "Federation handbook on procedures"}
            ],
            "caselaw": ["CAS 2019/A/123", "CAS 2018/A/456"]
        }
    },
    {
        "id": "2",
        "issue": "Presence of Substance X",
        "category": "substance",
        "appellant": {
            "mainArgument": "Chain-of-custody errors invalidate test results",
            "details": [
                "Sample had a 10-hour delay in transfer",
                "Sealing procedure was not properly documented",
                "Independent expert confirms potential degradation"
            ],
            "evidence": [
                {"id": "C4", "desc": "Lab reports #1 and #2"},
                {"id": "C5", "desc": "Expert Dr. A's statement"},
                {"id": "C6", "desc": "Chain of custody documentation"}
            ],
            "caselaw": ["CAS 2018/A/ABC"]
        },
        "respondent": {
            "mainArgument": "Minor procedural defects do not invalidate results",
            "details": [
                "WADA-accredited lab's procedures ensure reliability",
                "10-hour delay within acceptable limits",
                "No evidence of sample degradation"
            ],
            "evidence": [
                {"id": "R4", "desc": "Lab accreditation documents"},
                {"id": "R5", "desc": "Expert Dr. B's analysis"},
                {"id": "R6", "desc": "Testing protocols"}
            ],
            "caselaw": ["CAS 2017/A/789"]
        }
    },
    {
        "id": "3",
        "issue": "Contract Termination Validity",
        "category": "employment",
        "appellant": {
            "mainArgument": "Termination was wrongful and without cause",
            "details": [
                "No prior warnings were issued before termination",
                "Performance reviews were consistently positive",
                "Termination violated company policy on progressive discipline"
            ],
            "evidence": [
                {"id": "C7", "desc": "Employee performance reviews 2020-2023"},
                {"id": "C8", "desc": "Company handbook on disciplinary procedures"},
                {"id": "C9", "desc": "Email correspondence regarding termination"}
            ],
            "caselaw": ["Smith v. Corp Inc. 2021", "Jones v. Enterprise Ltd 2020"]
        },
        "respondent": {
            "mainArgument": "Termination was justified due to misconduct",
            "details": [
                "Multiple instances of policy violations documented",
                "Verbal warnings were given on several occasions",
                "Final incident warranted immediate termination"
            ],
            "evidence": [
                {"id": "R7", "desc": "Internal incident reports"},
                {"id": "R8", "desc": "Witness statements from supervisors"},
                {"id": "R9", "desc": "Security footage from incident date"}
            ],
            "caselaw": ["Brown v. MegaCorp 2022", "Wilson v. Tech Solutions 2021"]
        }
    },
    {
        "id": "4",
        "issue": "Patent Infringement",
        "category": "intellectual property",
        "appellant": {
            "mainArgument": "Defendant's product violates our patent claims",
            "details": [
                "Product uses identical method described in patent claims",
                "Infringement began after patent publication",
                "Similarities cannot be explained by independent development"
            ],
            "evidence": [
                {"id": "C10", "desc": "Patent documentation and claims analysis"},
                {"id": "C11", "desc": "Technical comparison report"},
                {"id": "C12", "desc": "Expert analysis of defendant's product"}
            ],
            "caselaw": ["TechCo v. Innovate Inc. 2022", "Patent Holdings v. StartUp 2021"]
        },
        "respondent": {
            "mainArgument": "Our technology was independently developed",
            "details": [
                "Development began before patent filing date",
                "Technology uses different underlying mechanism",
                "Patent claims are overly broad and invalid"
            ],
            "evidence": [
                {"id": "R10", "desc": "Development timeline documentation"},
                {"id": "R11", "desc": "Prior art examples"},
                {"id": "R12", "desc": "Technical differentiation analysis"}
            ],
            "caselaw": ["Innovation Corp v. PatentCo 2023", "Tech Solutions v. IP Holdings 2022"]
        }
    },
    {
        "id": "5",
        "issue": "Environmental Compliance",
        "category": "regulatory",
        "appellant": {
            "mainArgument": "Facility meets all environmental standards",
            "details": [
                "All required permits were obtained and maintained",
                "Emissions consistently below regulatory limits",
                "Regular maintenance and monitoring conducted"
            ],
            "evidence": [
                {"id": "C13", "desc": "Environmental impact assessments"},
                {"id": "C14", "desc": "Continuous monitoring data 2021-2023"},
                {"id": "C15", "desc": "Third-party compliance audit reports"}
            ],
            "caselaw": ["EcoCorp v. EPA 2022", "Green Industries v. State 2021"]
        },
        "respondent": {
            "mainArgument": "Significant violations of environmental regulations",
            "details": [
                "Multiple instances of excess emissions recorded",
                "Required monitoring equipment malfunctioned",
                "Failure to report incidents within required timeframe"
            ],
            "evidence": [
                {"id": "R13", "desc": "Violation notices and citations"},
                {"id": "R14", "desc": "Inspector field reports"},
                {"id": "R15", "desc": "Community complaint records"}
            ],
            "caselaw": ["EPA v. Industrial Corp 2023", "State v. Manufacturing Co. 2022"]
        }
    }
]

def create_position_section(position_data, position_type):
    """Create a section for appellant or respondent position"""
    color = "#4F46E5" if position_type == "Appellant" else "#E11D48"
    
    st.markdown(f"""
        <h3 style="color: {color}; font-size: 19.2px;">{position_type}'s Position</h3>
    """, unsafe_allow_html=True)
    
    # Main Argument
    st.markdown(f"""
        <div class="main-argument" style="
            margin: 20px 0; 
            font-size: 1.2rem;
            max-width: 95%;
            line-height: 1.5;
            padding-right: 15px;
        ">
            <strong>{position_data['mainArgument']}</strong>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Supporting Points
    st.markdown("""
        <div style="margin: 1.5rem 0;">
            <h5 style="margin-bottom: 2px;">Supporting Points</h5>
            <ul style="
                list-style-type: none;
                padding-left: 0;
                margin: 0;
                display: flex;
                flex-direction: column;
                gap: 12px;
            ">
    """, unsafe_allow_html=True)
    
    for detail in position_data['details']:
        st.markdown(f"""
            <li style="
                display: flex;
                align-items: flex-start;
                margin-bottom: 0;
                line-height: 1.5;
                padding-right: 20px;
            ">
                <span style="margin-right: 10px;">•</span>
                <span style="flex: 1;">{detail}</span>
            </li>
        """, unsafe_allow_html=True)
    
    st.markdown("</ul></div>", unsafe_allow_html=True)
    
    # Evidence
    st.markdown("##### Evidence")
    for evidence in position_data['evidence']:
        st.markdown(f"""
            <div class="evidence-card" style="
                display: flex;
                align-items: center;
                padding: 12px 16px;
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                margin-bottom: 8px;
                transition: all 0.2s;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
            ">
                <span style="
                    background-color: #F3F4F6;
                    color: #4B5563;
                    padding: 4px 8px;
                    border-radius: 4px;
                    font-size: 13px;
                    font-weight: 500;
                    margin-right: 12px;
                ">{evidence['id']}</span>
                <a href="/evidence/{evidence['id']}" 
                   style="
                    color: #4B5563;
                    text-decoration: none;
                    font-size: 14px;
                    flex-grow: 1;
                    transition: color 0.2s;
                   "
                   onmouseover="this.style.color='#4D68F9'"
                   onmouseout="this.style.color='#4B5563'"
                >
                    {evidence['desc']}
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    # Case Law
    st.markdown("##### Case Law")
    for case in position_data['caselaw']:
        summary = get_case_summary(case)
        st.markdown(f"""
            <div class="position-card">
                <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem;">
                    <div style="flex-grow: 1;">
                        <div style="font-weight: 500; color: #4B5563; margin-bottom: 0.5rem;">
                            {case}
                        </div>
                        <div style="font-size: 0.875rem; color: #6B7280;">
                            {summary}
                        </div>
                    </div>
                    <button onclick="navigator.clipboard.writeText('{case}')" 
                            style="background: none; border: none; cursor: pointer; padding: 0.25rem;">
                        📋
                    </button>
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.markdown("""
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 175 175">
          <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
            <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
          </mask>
          <g mask="url(#whatsapp-mask)">
            <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
          </g>
        </svg>
        """, unsafe_allow_html=True)
        st.title("Summary Overview")

    st.title("Summary of Arguments")
    
    # Create a string with all the content to be copied
    copy_content = []
    for arg in argument_data:
        copy_content.append(f"### {arg['issue']} ({arg['category']})")
        copy_content.append("\nAppellant's Position:")
        copy_content.append(f"• {arg['appellant']['mainArgument']}")
        copy_content.append("\nRespondent's Position:")
        copy_content.append(f"• {arg['respondent']['mainArgument']}\n")
    
    copy_text = "\n".join(copy_content)

    # Search bar and copy button in the same row
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        search = st.text_input("", 
                             placeholder="🔍 Search issues, arguments, or evidence...",
                             label_visibility="collapsed")
    with col2:
        # Create a hidden component that will handle the copy functionality
        copy_component = f"""
        <textarea id="copy-text" style="position: absolute; left: -9999px;">{copy_text}</textarea>
        <button
            onclick="copyToClipboard()"
            style="
                width: 100%;
                height: 38px;
                padding: 0 16px;
                background-color: #4D68F9;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 14px;
                font-weight: 500;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                transition: background-color 0.2s;
                margin-top: 4px;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            "
            onmouseover="this.style.backgroundColor='#4558D0'"
            onmouseout="this.style.backgroundColor='#4D68F9'"
        >
            <span style="font-size: 16px;">📋</span>
            <span>Copy</span>
        </button>
        <script>
        function copyToClipboard() {{
            const textArea = document.getElementById('copy-text');
            textArea.select();
            document.execCommand('copy');
            const button = document.querySelector('button');
            const originalContent = button.innerHTML;
            button.innerHTML = '<span style="font-size: 16px;">✓</span><span>Copied!</span>';
            setTimeout(() => button.innerHTML = originalContent, 2000);
        }}
        </script>
        """
        html(copy_component, height=46)
    
    # Filter arguments based on search
    filtered_arguments = argument_data
    if search:
        search = search.lower()
        filtered_arguments = [
            arg for arg in argument_data
            if (search in arg['issue'].lower() or
                any(search in detail.lower() for detail in arg['appellant']['details']) or
                any(search in detail.lower() for detail in arg['respondent']['details']) or
                any(search in e['desc'].lower() for e in arg['appellant']['evidence']) or
                any(search in e['desc'].lower() for e in arg['respondent']['evidence']))
        ]
    
    # Display arguments
    for arg in filtered_arguments:
        with st.expander(f"{arg['issue']} ({arg['category']})", expanded=arg['id'] == '1'):
            st.markdown("""
                <style>
                    .stMarkdown {
                        max-width: 100%;
                    }
                    .main-argument {
                        padding-right: 20px;
                        word-wrap: break-word;
                        overflow-wrap: break-word;
                        hyphens: auto;
                    }
                </style>
            """, unsafe_allow_html=True)
            # Content when expanded
            col1, col2 = st.columns([1, 1])
            with col1:
                create_position_section(arg['appellant'], "Appellant")
            with col2:
                create_position_section(arg['respondent'], "Respondent")
        
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
