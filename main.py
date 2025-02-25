import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# [All the data functions remain unchanged]
# ...

# Main app
def main():
    # Get the data for JavaScript
    args_data = get_argument_data()
    timeline_data = get_timeline_data()
    exhibits_data = get_exhibits_data()
    
    # Convert data to JSON for JavaScript use
    args_json = json.dumps(args_data)
    timeline_json = json.dumps(timeline_data)
    exhibits_json = json.dumps(exhibits_data)
    
    # Create a single HTML component containing the full UI with minimalistic design
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* [All the existing CSS remains unchanged] */
            
            /* Add this new style for nested content visibility */
            .nested-content {{
                padding-left: 20px;
                margin-top: 10px;
                border-left: 1px solid #f0f0f0;
                /* Remove display: none from here as we want them always visible */
            }}
        </style>
    </head>
    <body>
        <!-- [All the HTML structure remains unchanged] -->
        
        <script>
            // [Most JavaScript functions remain unchanged]
            
            // Modify the renderArgument function
            function renderArgument(arg, side) {{
                if (!arg) return '';
                
                const hasChildren = arg.children && Object.keys(arg.children).length > 0;
                const argId = `${{side}}-${{arg.id}}`;
                
                // Store corresponding pair ID for synchronization
                const pairId = arg.id;
                
                // Style based on side
                const badgeClass = side === 'appellant' ? 'appellant-badge' : 'respondent-badge';
                
                // Render children if any
                let childrenHtml = '';
                if (hasChildren) {{
                    childrenHtml = `<div class="nested-content" id="children-${{argId}}">`;
                    
                    Object.values(arg.children).forEach(child => {{
                        childrenHtml += renderArgument(child, side);
                    }});
                    
                    childrenHtml += `</div>`;
                }}
                
                return `
                <div class="card">
                    <div class="card-header" onclick="toggleArgument('${{argId}}', '${{pairId}}', '${{side}}')">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <svg id="chevron-${{argId}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6"></polyline>
                            </svg>
                            <span>${{arg.id}}. ${{arg.title}}</span>
                        </div>
                        <span class="badge ${{badgeClass}}">¶${{arg.paragraphs}}</span>
                    </div>
                    <div class="card-content" id="content-${{argId}}">
                        ${{renderArgumentContent(arg)}}
                    </div>
                    ${{childrenHtml}}
                </div>
                `;
            }}
            
            // Modify toggleCard to only toggle the content, not children
            function toggleCard(id) {{
                const contentEl = document.getElementById(`content-${{id}}`);
                const chevronEl = document.getElementById(`chevron-${{id}}`);
                
                if (contentEl) {{
                    contentEl.style.display = contentEl.style.display === 'block' ? 'none' : 'block';
                }}
                
                if (chevronEl) {{
                    chevronEl.classList.toggle('expanded');
                }}
            }}
            
            // Modify toggleArgument to only toggle content
            function toggleArgument(argId, pairId, side) {{
                // First, handle the clicked argument
                toggleCard(argId);
                
                // Then, determine and handle the counterpart
                const otherSide = side === 'appellant' ? 'respondent' : 'appellant';
                const counterpartId = `${{otherSide}}-${{pairId}}`;
                
                // Toggle the counterpart (if it exists)
                const counterpartContentEl = document.getElementById(`content-${{counterpartId}}`);
                if (counterpartContentEl) {{
                    const counterpartChevronEl = document.getElementById(`chevron-${{counterpartId}}`);
                    
                    // Make sure the counterpart's state matches the toggled argument
                    const originalDisplay = document.getElementById(`content-${{argId}}`).style.display;
                    counterpartContentEl.style.display = originalDisplay;
                    
                    if (counterpartChevronEl) {{
                        if (originalDisplay === 'block') {{
                            counterpartChevronEl.classList.add('expanded');
                        }} else {{
                            counterpartChevronEl.classList.remove('expanded');
                        }}
                    }}
                }}
            }}
            
            // [Rest of the JavaScript functions remain unchanged]
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Legal Arguments Analysis")
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
