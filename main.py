import streamlit as st
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Legal Arguments Analysis", layout="wide")

# Create data structures as JSON for embedded components
def get_argument_data():
    # Data structure remains unchanged
    # ...
    # All the original get_argument_data code

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
            /* All previous CSS styles remain unchanged */
            
            /* Added styles for main argument content */
            .main-argument-content {{
                margin-bottom: 20px;
                padding: 15px;
                background-color: #f9f9f9;
                border-radius: 8px;
                border: 1px solid #eaeaea;
            }}
            
            .main-argument-header {{
                font-weight: 600;
                margin-bottom: 10px;
                padding-bottom: 8px;
                border-bottom: 1px solid #eaeaea;
            }}
            
            /* Nested content now always visible */
            .nested-content {{
                padding-left: 20px;
                margin-top: 10px;
                border-left: 1px solid #f0f0f0;
                /* No display: none */
            }}
        </style>
    </head>
    <body>
        <!-- All previous HTML structure remains unchanged -->
        
        <script>
            // Initialize data
            const argsData = {args_json};
            const timelineData = {timeline_json};
            const exhibitsData = {exhibits_json};
            
            // Tab switching and other functions remain unchanged
            
            // Modified renderTopics function to show main argument content
            function renderTopics() {{
                const container = document.getElementById('topics-container');
                let html = '';
                
                argsData.topics.forEach(topic => {{
                    html += `
                    <div class="card" style="margin-bottom: 24px;">
                        <div class="card-header" onclick="toggleCard('topic-${{topic.id}}')">
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <svg id="chevron-topic-${{topic.id}}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="9 18 15 12 9 6"></polyline>
                                </svg>
                                <span>${{topic.title}}</span>
                            </div>
                        </div>
                        <div class="card-content" id="content-topic-${{topic.id}}">
                            <p>${{topic.description}}</p>
                            
                            ${{topic.argumentIds.map(argId => {{
                                if (argsData.claimantArgs[argId] && argsData.respondentArgs[argId]) {{
                                    const claimantArg = argsData.claimantArgs[argId];
                                    const respondentArg = argsData.respondentArgs[argId];
                                    
                                    // Show main argument content for both sides
                                    return `
                                    <div style="margin-top: 16px;">
                                        <div class="arguments-row">
                                            <div>
                                                <h3 class="side-heading appellant-color">Appellant's Position</h3>
                                                
                                                <!-- Main argument content for appellant -->
                                                <div class="main-argument-content">
                                                    <div class="main-argument-header">
                                                        ${{claimantArg.id}}. ${{claimantArg.title}} <span class="badge appellant-badge">¶${{claimantArg.paragraphs}}</span>
                                                    </div>
                                                    ${{renderArgumentContent(claimantArg)}}
                                                </div>
                                                
                                                <!-- Children arguments for appellant -->
                                                ${{renderChildren(claimantArg, 'appellant')}}
                                            </div>
                                            <div>
                                                <h3 class="side-heading respondent-color">Respondent's Position</h3>
                                                
                                                <!-- Main argument content for respondent -->
                                                <div class="main-argument-content">
                                                    <div class="main-argument-header">
                                                        ${{respondentArg.id}}. ${{respondentArg.title}} <span class="badge respondent-badge">¶${{respondentArg.paragraphs}}</span>
                                                    </div>
                                                    ${{renderArgumentContent(respondentArg)}}
                                                </div>
                                                
                                                <!-- Children arguments for respondent -->
                                                ${{renderChildren(respondentArg, 'respondent')}}
                                            </div>
                                        </div>
                                    </div>
                                    `;
                                }}
                                return '';
                            }}).join('')}}
                        </div>
                    </div>
                    `;
                }});
                
                container.innerHTML = html;
            }}
            
            // New function to render just the children of an argument
            function renderChildren(arg, side) {{
                if (!arg.children || Object.keys(arg.children).length === 0) return '';
                
                let childrenHtml = '';
                Object.values(arg.children).forEach(child => {{
                    childrenHtml += renderArgument(child, side);
                }});
                
                return childrenHtml;
            }}
            
            // Render a single argument
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
            
            // Remaining JavaScript functions (renderArgumentContent, renderOverviewPoints, etc.) remain unchanged
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    st.title("Legal Arguments Analysis")
    components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
