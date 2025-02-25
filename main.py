def get_css():
    return """
    /* Base styling */
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        line-height: 1.5;
        color: #333;
        margin: 0;
        padding: 0;
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
        color: #4a5568;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* Arguments styling */
    .arguments-header {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-bottom: 1rem;
    }
    .claimant-color {
        color: #3182ce;
    }
    .respondent-color {
        color: #e53e3e;
    }
    
    /* Argument container and pairs */
    .argument-pair {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-bottom: 1rem;
        position: relative;
    }
    .argument-side {
        position: relative;
    }
    
    /* Argument card and details */
    .argument {
        border: 1px solid #e2e8f0;
        border-radius: 0.375rem;
        overflow: hidden;
        margin-bottom: 1rem;
    }
    .argument-header {
        padding: 0.75rem 1rem;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .argument-header-left {
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
    .claimant-header {
        background-color: #ebf8ff;
        border-color: #bee3f8;
    }
    .respondent-header {
        background-color: #fff5f5;
        border-color: #fed7d7;
    }
    
    /* Child arguments container */
    .argument-children {
        padding-left: 1.5rem;
        display: none;
        position: relative;
    }
    
    /* Connector lines for tree structure */
    .connector-vertical {
        position: absolute;
        left: 0.75rem;
        top: 0;
        width: 1px;
        height: 100%;
        background-color: #e2e8f0;
    }
    .connector-horizontal {
        position: absolute;
        left: 0.75rem;
        top: 1.25rem;
        width: 0.75rem;
        height: 1px;
        background-color: #e2e8f0;
    }
    .claimant-connector {
        background-color: rgba(59, 130, 246, 0.5);
    }
    .respondent-connector {
        background-color: rgba(239, 68, 68, 0.5);
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
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
    .legal-badge {
        background-color: #ebf8ff;
        color: #2c5282;
        margin-right: 0.25rem;
    }
    .factual-badge {
        background-color: #f0fff4;
        color: #276749;
        margin-right: 0.25rem;
    }
    .disputed-badge {
        background-color: #fed7d7;
        color: #c53030;
    }
    .type-badge {
        background-color: #edf2f7;
        color: #4a5568;
    }
    
    /* Content components */
    .content-section {
        margin-bottom: 1.5rem;
    }
    .content-section-title {
        font-size: 0.875rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .point-block {
        background-color: #f7fafc;
        border-radius: 0.5rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .point-header {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.25rem;
    }
    .point-date {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.25rem;
        font-size: 0.75rem;
        color: #718096;
    }
    .point-text {
        font-size: 0.875rem;
        color: #4a5568;
    }
    .point-citation {
        display: inline-block;
        margin-top: 0.5rem;
        font-size: 0.75rem;
        color: #718096;
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
    
    /* Evidence and Case Law */
    .reference-block {
        background-color: #f7fafc;
        border-radius: 0.5rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .reference-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.25rem;
    }
    .reference-title {
        font-size: 0.875rem;
        font-weight: 500;
    }
    .reference-summary {
        font-size: 0.75rem;
        color: #718096;
        margin-top: 0.25rem;
        margin-bottom: 0.5rem;
    }
    .reference-citations {
        display: flex;
        flex-wrap: wrap;
        gap: 0.25rem;
        margin-top: 0.5rem;
    }
    .citation-tag {
        background-color: #edf2f7;
        color: #4a5568;
        padding: 0.125rem 0.375rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
    }
    
    /* Legal references styling */
    .legal-point {
        background-color: #ebf8ff;
        border-radius: 0.5rem;
        padding: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .factual-point {
        background-color: #f0fff4;
