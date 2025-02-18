def display_party_section(data, party_type):
    color_class = "appellant-color" if party_type == "appellant" else "respondent-color"
    evidence_class = "" if party_type == "appellant" else "evidence-id-respondent"
    
    # Main Argument as title
    st.markdown(f'<h3 class="{color_class}">{data["mainArgument"]}</h3>', unsafe_allow_html=True)
    
    # Key Arguments
    st.markdown("#### Key Arguments")
    for detail in data["details"]:
        st.markdown(f'<div class="evidence-box">{detail}</div>', unsafe_allow_html=True)
    
    # Evidence
    st.markdown("#### Evidence")
    for evidence in data["evidence"]:
        st.markdown(
            f'<div class="evidence-box">'
            f'<span class="evidence-id {evidence_class}">{evidence["id"]}</span>'
            f'{evidence["desc"]}</div>',
            unsafe_allow_html=True
        )
    
    # Case Law
    st.markdown("#### Case Law")
    for case in data["caselaw"]:
        st.markdown(f'<div class="case-law">{case}</div>', unsafe_allow_html=True)
