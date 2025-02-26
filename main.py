# Get data structures as JSON for embedded components
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
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Historical Color Documentation",
                                    "paragraphs": "61-65",
                                    "evidence": [
                                        {
                                            "id": "C-5",
                                            "title": "Color Archives",
                                            "summary": "Detailed color specification documents from club archives, including official style guides, manufacturer specifications, and board meeting minutes about uniform decisions from 1950 to present day.",
                                            "citations": ["61", "62", "63"]
                                        }
                                    ]
                                }
                            }
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
                    "children": {
                        "1.1.1": {
                            "id": "1.1.1",
                            "title": "Registration Gap Evidence",
                            "paragraphs": "226-230",
                            "factualPoints": [
                                {
                                    "point": "Registration formally terminated on April 30, 1975",
                                    "date": "April 30, 1975",
                                    "isDisputed": False,
                                    "paragraphs": "226-227",
                                    "exhibits": ["R-2"]
                                },
                                {
                                    "point": "New entity registered on September 15, 1976",
                                    "date": "September 15, 1976",
                                    "isDisputed": False,
                                    "paragraphs": "228-229",
                                    "exhibits": ["R-2"]
                                }
                            ],
                            "evidence": [
                                {
                                    "id": "R-2",
                                    "title": "Termination Certificate",
                                    "summary": "Official government certificate of termination for the original club entity, stamped and notarized on April 30, 1975, along with completely new registration documents for a separate legal entity filed on September 15, 1976, with different founding members and bylaws.",
                                    "citations": ["226", "227"]
                                }
                            ]
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
                    "factualPoints": [
                        {
                            "point": "Significant color scheme change in 1976",
                            "date": "1976",
                            "isDisputed": True,
                            "source": "Claimant",
                            "paragraphs": "245-246",
                            "exhibits": ["R-4"]
                        }
                    ],
                    "evidence": [
                        {
                            "id": "R-4",
                            "title": "Historical Photographs Comparison",
                            "summary": "Side-by-side comparison of team uniforms from 1974 (pre-dissolution) and 1976 (post-new registration), showing significant differences in shade, pattern, and design elements. Includes expert color analysis report from textile historian confirming different dye formulations were used.",
                            "citations": ["245", "246", "247"]
                        }
                    ],
                    "children": {
                        "1.2.1": {
                            "id": "1.2.1",
                            "title": "Color Changes Analysis",
                            "paragraphs": "247-249",
                            "factualPoints": [
                                {
                                    "point": "Pre-1976 colors represented original city district",
                                    "date": "1950-1975",
                                    "isDisputed": False,
                                    "paragraphs": "247",
                                    "exhibits": ["R-5"]
                                },
                                {
                                    "point": "Post-1976 colors represented new ownership region",
                                    "date": "1976-present",
                                    "isDisputed": True,
                                    "source": "Claimant",
                                    "paragraphs": "248-249",
                                    "exhibits": ["R-5"]
                                }
                            ],
                            "children": {
                                "1.2.1.1": {
                                    "id": "1.2.1.1",
                                    "title": "Color Identity Documentation",
                                    "paragraphs": "250-255",
                                    "evidence": [
                                        {
                                            "id": "R-5",
                                            "title": "Marketing Materials",
                                            "summary": "Collection of promotional materials, merchandise, and internal design documents from both pre-1975 and post-1976 periods, showing the deliberate change in color symbolism used in marketing campaigns and communications with fans.",
                                            "citations": ["250", "251", "252"]
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
            }
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

# Arguments section HTML template for the component
def arguments_section_html(args_data):
    arguments_html = """
    <div id="arguments" class="content-section active">
        <div class="section-title">Issues</div>
        
        <!-- View toggle buttons -->
        <div class="view-toggle" style="display: flex; justify-content: space-between;">
            <div>
                <button id="both-parties-btn" class="active" onclick="switchPartyView('both')">Both Parties</button>
                <button id="appellant-btn" onclick="switchPartyView('appellant')">Appellant Only</button>
                <button id="respondent-btn" onclick="switchPartyView('respondent')">Respondent Only</button>
            </div>
            <div>
                <button id="detailed-view-btn" class="active" onclick="switchView('detailed')">Detailed View</button>
                <button id="table-view-btn" onclick="switchView('table')">Table View</button>
            </div>
        </div>
        
        <!-- Detailed view content -->
        <div id="detailed-view" class="view-content active">
            <div id="topics-container"></div>
        </div>
        
        <!-- Table view content -->
        <div id="table-view" class="view-content" style="display: none;">
            <table class="table-view">
                <thead>
                    <tr>
                        <th onclick="sortTable('table-view-body', 0)">ID</th>
                        <th onclick="sortTable('table-view-body', 1)">Argument</th>
                        <th onclick="sortTable('table-view-body', 2)">Party</th>
                        <th onclick="sortTable('table-view-body', 3)">Status</th>
                        <th onclick="sortTable('table-view-body', 4)">Evidence</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="table-view-body"></tbody>
            </table>
        </div>
    </div>
    
    <script>
        // Initialize data
        const argsData = {args_json};
        
        // Global variable to track current party view
        let currentPartyView = 'both';
        
        // Switch view between detailed and table
        function switchView(viewType) {
            const detailedBtn = document.getElementById('detailed-view-btn');
            const tableBtn = document.getElementById('table-view-btn');
            const detailedView = document.getElementById('detailed-view');
            const tableView = document.getElementById('table-view');
            
            if (viewType === 'detailed') {
                detailedBtn.classList.add('active');
                tableBtn.classList.remove('active');
                detailedView.style.display = 'block';
                tableView.style.display = 'none';
            } else {
                detailedBtn.classList.remove('active');
                tableBtn.classList.add('active');
                detailedView.style.display = 'none';
                tableView.style.display = 'block';
            }
        }
        
        // Switch party view
        function switchPartyView(partyType) {
            currentPartyView = partyType;
            const bothBtn = document.getElementById('both-parties-btn');
            const appellantBtn = document.getElementById('appellant-btn');
            const respondentBtn = document.getElementById('respondent-btn');
            
            // Remove active class from all
            bothBtn.classList.remove('active');
            appellantBtn.classList.remove('active');
            respondentBtn.classList.remove('active');
            
            // Add active to selected
            if (partyType === 'both') {
                bothBtn.classList.add('active');
            } else if (partyType === 'appellant') {
                appellantBtn.classList.add('active');
            } else {
                respondentBtn.classList.add('active');
            }
            
            // Re-render topics with selected view
            renderTopics();
        }
        
        // Render arguments in table format
        function renderArgumentsTable() {
            const tableBody = document.getElementById('table-view-body');
            tableBody.innerHTML = '';
            
            // Helper function to flatten arguments
            function flattenArguments(args, party) {
                let result = [];
                
                Object.values(args).forEach(arg => {
                    // Track if argument has disputed facts
                    const hasDisputedFacts = arg.factualPoints && 
                        arg.factualPoints.some(point => point.isDisputed);
                    
                    // Count pieces of evidence
                    const evidenceCount = arg.evidence ? arg.evidence.length : 0;
                    
                    // Add this argument
                    result.push({
                        id: arg.id,
                        title: arg.title,
                        party: party,
                        hasDisputedFacts: hasDisputedFacts,
                        evidenceCount: evidenceCount,
                        paragraphs: arg.paragraphs
                    });
                    
                    // Process children recursively
                    if (arg.children) {
                        Object.values(arg.children).forEach(child => {
                            result = result.concat(flattenArguments({[child.id]: child}, party));
                        });
                    }
                });
                
                return result;
            }
            
            // Get flattened arguments
            const appellantArgs = flattenArguments(argsData.claimantArgs, "Appellant");
            const respondentArgs = flattenArguments(argsData.respondentArgs, "Respondent");
            
            // Filter based on current party view
            let allArgs = [];
            if (currentPartyView === 'both') {
                allArgs = [...appellantArgs, ...respondentArgs];
            } else if (currentPartyView === 'appellant') {
                allArgs = appellantArgs;
            } else {
                allArgs = respondentArgs;
            }
            
            // Render rows
            allArgs.forEach(arg => {
                const row = document.createElement('tr');
                
                // ID column
                const idCell = document.createElement('td');
                idCell.textContent = arg.id;
                row.appendChild(idCell);
                
                // Title column
                const titleCell = document.createElement('td');
                titleCell.textContent = arg.title;
                row.appendChild(titleCell);
                
                // Party column
                const partyCell = document.createElement('td');
                const partyBadge = document.createElement('span');
                partyBadge.className = `badge ${arg.party === 'Appellant' ? 'appellant-badge' : 'respondent-badge'}`;
                partyBadge.textContent = arg.party;
                partyCell.appendChild(partyBadge);
                row.appendChild(partyCell);
                
                // Status column
                const statusCell = document.createElement('td');
                if (arg.hasDisputedFacts) {
                    const disputedBadge = document.createElement('span');
                    disputedBadge.className = 'badge disputed-badge';
                    disputedBadge.textContent = 'Disputed';
                    statusCell.appendChild(disputedBadge);
                } else {
                    statusCell.textContent = 'Undisputed';
                }
                row.appendChild(statusCell);
                
                // Evidence column
                const evidenceCell = document.createElement('td');
                evidenceCell.textContent = arg.evidenceCount > 0 ? `${arg.evidenceCount} items` : 'None';
                row.appendChild(evidenceCell);
                
                // Actions column
                const actionsCell = document.createElement('td');
                const viewBtn = document.createElement('button');
                viewBtn.textContent = 'View';
                viewBtn.style.padding = '4px 8px';
                viewBtn.style.marginRight = '8px';
                viewBtn.style.border = '1px solid #e2e8f0';
                viewBtn.style.borderRadius = '4px';
                viewBtn.style.backgroundColor = '#f7fafc';
                viewBtn.style.cursor = 'pointer';
                viewBtn.onclick = function() {
                    // Switch to detailed view and expand this argument
                    switchView('detailed');
                    // Logic to find and expand the argument would go here
                };
                actionsCell.appendChild(viewBtn);
                row.appendChild(actionsCell);
                
                tableBody.appendChild(row);
            });
        }
        
        // Render overview points
        function renderOverviewPoints(overview) {
            if (!overview || !overview.points || overview.points.length === 0) return '';
            
            const pointsList = overview.points.map(point => 
                `<li>
                    <span>${point}</span>
                    <span class="para-badge">¶${overview.paragraphs}</span>
                </li>`
            ).join('');
            
            return `
            <div class="item-block">
                <div class="item-title">Supporting Points</div>
                <ul class="point-list">
                    ${pointsList}
                </ul>
            </div>
            `;
        }
        
        // Render factual points (now called Events)
        function renderFactualPoints(points) {
            if (!points || points.length === 0) return '';
            
            const pointsHtml = points.map(point => {
                const disputed = point.isDisputed 
                    ? `<span class="badge disputed-badge">Disputed</span>` 
                    : '';
                
                // Exhibits badges
                const exhibitBadges = point.exhibits && point.exhibits.length > 0
                    ? point.exhibits.map(exhibitId => `<span class="badge exhibit-badge">${exhibitId}</span>`).join(' ')
                    : '';
                
                return `
                <div class="item-block">
                    <div style="display: flex; justify-content: space-between;">
                        <span>${point.point}</span>
                        <span>
                            ${disputed}
                            ${exhibitBadges}
                        </span>
                    </div>
                    <div style="font-size: 12px; color: #666; margin-top: 4px;">${point.date}</div>
                </div>
                `;
            }).join('');
            
            return `
            <div style="margin-top: 16px;">
                <div class="item-title">Events</div>
                ${pointsHtml}
            </div>
            `;
        }
        
        // Render evidence
        function renderEvidence(evidence) {
            if (!evidence || evidence.length === 0) return '';
            
            const evidenceHtml = evidence.map(item => {
                const citations = item.citations && item.citations.length > 0
                    ? item.citations.map(cite => `<span class="citation-tag">¶${cite}</span>`).join('')
                    : '';
                
                return `
                <div class="evidence-block">
                    <div class="item-title">${item.id}: ${item.title}</div>
                    <div style="margin: 6px 0;">${item.summary}</div>
                    <div style="margin-top: 8px; font-size: 12px;">
                        <span style="color: #666; margin-right: 5px;">Cited in:</span>
                        ${citations}
                    </div>
                </div>
                `;
            }).join('');
            
            return `
            <div style="margin-top: 16px;">
                <div class="item-title">Evidence</div>
                ${evidenceHtml}
            </div>
            `;
        }
        
        // Render case law
        function renderCaseLaw(cases) {
            if (!cases || cases.length === 0) return '';
            
            const casesHtml = cases.map(item => {
                const citedParagraphs = item.citedParagraphs && item.citedParagraphs.length > 0
                    ? item.citedParagraphs.map(cite => `<span class="citation-tag">¶${cite}</span>`).join('')
                    : '';
                
                return `
                <div class="caselaw-block">
                    <div class="item-title">${item.caseNumber}</div>
                    <div style="font-size: 12px; margin: 2px 0 8px 0;">¶${item.paragraphs}</div>
                    <div style="font-weight: 500; margin-bottom: 4px;">${item.title}</div>
                    <div style="margin: 6px 0;">${item.relevance}</div>
                    <div style="margin-top: 8px; font-size: 12px;">
                        <span style="color: #666; margin-right: 5px;">Key Paragraphs:</span>
                        ${citedParagraphs}
                    </div>
                </div>
                `;
            }).join('');
            
            return `
            <div style="margin-top: 16px;">
                <div class="item-title">Case Law</div>
                ${casesHtml}
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
        
        // Render a single argument including its children
        function renderArgument(arg, side) {
            if (!arg) return '';
            
            const hasChildren = arg.children && Object.keys(arg.children).length > 0;
            const argId = `${side}-${arg.id}`;
            
            // Store corresponding pair ID for synchronization
            const pairId = arg.id;
            
            // Style based on side
            const badgeClass = side === 'appellant' ? 'appellant-badge' : 'respondent-badge';
            
            // Render children if any - removed style="display: none;"
            let childrenHtml = '';
            if (hasChildren) {
                childrenHtml = `<div class="nested-content" id="children-${argId}">`;
                
                Object.values(arg.children).forEach(child => {
                    childrenHtml += renderArgument(child, side);
                });
                
                childrenHtml += `</div>`;
            }
            
            return `
            <div class="card">
                <div class="card-header" onclick="toggleArgument('${argId}', '${pairId}', '${side}')">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <svg id="chevron-${argId}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6"></polyline>
                        </svg>
                        <span>${arg.id}. ${arg.title}</span>
                    </div>
                    <span class="badge ${badgeClass}">¶${arg.paragraphs}</span>
                </div>
                <div class="card-content" id="content-${argId}">
                    ${renderArgumentContent(arg)}
                </div>
                ${childrenHtml}
            </div>
            `;
        }
        
        // Render arguments by topic
        function renderTopics() {
            const container = document.getElementById('topics-container');
            let html = '';
            
            argsData.topics.forEach(topic => {
                html += `
                <div class="card" style="margin-bottom: 24px;">
                    <div class="card-header" onclick="toggleCard('topic-${topic.id}')">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <svg id="chevron-topic-${topic.id}" class="chevron" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6"></polyline>
                            </svg>
                            <span>${topic.title}</span>
                        </div>
                    </div>
                    <div class="card-content" id="content-topic-${topic.id}">
                        <p>${topic.description}</p>
                        
                        ${topic.argumentIds.map(argId => {
                            let html = '';
                            const showAppellant = currentPartyView === 'both' || currentPartyView === 'appellant';
                            const showRespondent = currentPartyView === 'both' || currentPartyView === 'respondent';
                            
                            if (currentPartyView === 'both') {
                                // Two-column layout for both parties
                                html = `
                                <div style="margin-top: 16px;">
                                    <div class="arguments-row">
                                        ${showAppellant ? `
                                        <div>
                                            <h3 class="side-heading appellant-color">Appellant's Position</h3>
                                            ${renderArgument(argsData.claimantArgs[argId], 'appellant')}
                                        </div>` : ''}
                                        ${showRespondent ? `
                                        <div>
                                            <h3 class="side-heading respondent
