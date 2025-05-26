import streamlit as st

def get_evidence_details(exhibits, args_data):
    """Get evidence details for given exhibit IDs"""
    evidence_details = []
    
    def find_evidence(args, exhibit_id):
        for arg_key in args:
            arg = args[arg_key]
            if 'evidence' in arg and arg['evidence']:
                for evidence in arg['evidence']:
                    if evidence['id'] == exhibit_id:
                        return evidence
            if 'children' in arg and arg['children']:
                child_evidence = find_evidence(arg['children'], exhibit_id)
                if child_evidence:
                    return child_evidence
        return None
    
    for exhibit_id in exhibits:
        evidence = (find_evidence(args_data['claimantArgs'], exhibit_id) or 
                   find_evidence(args_data['respondentArgs'], exhibit_id))
        
        if evidence:
            evidence_details.append({
                'id': exhibit_id,
                'title': evidence['title'],
                'summary': evidence['summary']
            })
        else:
            evidence_details.append({
                'id': exhibit_id,
                'title': exhibit_id,
                'summary': 'Evidence details not available'
            })
    
    return evidence_details

def render_streamlit_cards(filtered_facts, args_data):
    """Render facts as native Streamlit dropdown cards"""
    
    if not filtered_facts:
        st.info("No facts found matching the selected criteria.")
        return
    
    for i, fact in enumerate(filtered_facts):
        # Create card styling based on disputed status
        if fact['isDisputed']:
            card_container = st.container()
            with card_container:
                st.markdown("""
                <style>
                div[data-testid="stExpander"] > div:first-child {
                    border-left: 4px solid #e53e3e !important;
                    background-color: rgba(229, 62, 62, 0.02) !important;
                }
                </style>
                """, unsafe_allow_html=True)
        
        # Create the main expander for the fact
        with st.expander(f"**{fact['date']}** - {fact['event']}", expanded=False):
            
            # Add party badges
            badge_html = ""
            if fact['parties_involved']:
                for party in fact['parties_involved']:
                    if party == 'Appellant':
                        badge_html += '<span style="background-color: rgba(49, 130, 206, 0.1); color: #3182ce; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500; margin-right: 6px;">Appellant</span>'
                    else:
                        badge_html += '<span style="background-color: rgba(229, 62, 62, 0.1); color: #e53e3e; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500; margin-right: 6px;">Respondent</span>'
            
            if fact['isDisputed']:
                badge_html += '<span style="background-color: rgba(229, 62, 62, 0.1); color: #e53e3e; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 500;">Disputed</span>'
            
            if badge_html:
                st.markdown(badge_html, unsafe_allow_html=True)
                st.markdown("---")
            
            # Create two columns for document and argument info
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**📄 Document**")
                st.markdown(f"**{fact['doc_name'] or 'N/A'}**")
                if fact['page']:
                    st.markdown(f"*Page {fact['page']}*")
            
            with col2:
                st.markdown("**📋 Argument**")
                st.markdown(f"**{fact['argId']}. {fact['argTitle']}**")
                if fact['paragraphs']:
                    st.markdown(f"*Paragraphs: {fact['paragraphs']}*")
            
            # Source text
            if fact['source_text'] and fact['source_text'] != 'No specific submission recorded':
                st.markdown("**📝 Source Text:**")
                st.info(fact['source_text'])
            
            # Submissions
            if fact['claimant_submission'] and fact['claimant_submission'] != 'No specific submission recorded':
                st.markdown("**👤 Claimant Submission:**")
                st.markdown(f'<div style="background-color: rgba(49, 130, 206, 0.03); border-left: 4px solid #3182ce; padding: 12px; margin: 8px 0; border-radius: 0 6px 6px 0; font-style: italic;">{fact["claimant_submission"]}</div>', unsafe_allow_html=True)
            
            if fact['respondent_submission'] and fact['respondent_submission'] != 'No specific submission recorded':
                st.markdown("**👤 Respondent Submission:**")
                st.markdown(f'<div style="background-color: rgba(229, 62, 62, 0.03); border-left: 4px solid #e53e3e; padding: 12px; margin: 8px 0; border-radius: 0 6px 6px 0; font-style: italic;">{fact["respondent_submission"]}</div>', unsafe_allow_html=True)
            
            # Document summary
            if fact['doc_summary']:
                st.markdown("**📖 Document Summary:**")
                st.markdown(f"*{fact['doc_summary']}*")
            
            # Status and Evidence in two columns
            col3, col4 = st.columns([1, 2])
            
            with col3:
                st.markdown("**⚖️ Status**")
                if fact['isDisputed']:
                    st.markdown('<span style="background-color: rgba(229, 62, 62, 0.1); color: #e53e3e; padding: 4px 8px; border-radius: 12px; font-size: 12px; font-weight: 500;">Disputed</span>', unsafe_allow_html=True)
                else:
                    st.markdown("Undisputed")
            
            with col4:
                st.markdown("**📎 Evidence**")
                if fact['exhibits']:
                    evidence_details = get_evidence_details(fact['exhibits'], args_data)
                    
                    # Use checkboxes instead of nested expanders to avoid the error
                    for j, evidence in enumerate(evidence_details):
                        evidence_key = f"evidence_{i}_{j}"
                        if st.checkbox(f"📁 {evidence['id']}: {evidence['title']}", key=evidence_key):
                            st.markdown(f"*{evidence['summary']}*")
                else:
                    st.markdown("None")

# Example usage:
# render_streamlit_cards(filtered_facts, args_data)
