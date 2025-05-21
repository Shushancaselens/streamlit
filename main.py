<!DOCTYPE html>
<html>
<head>
    <style>
        /* Base styling */
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.5;
            color: #333;
            margin: 0;
            padding: 0;
            background-color: #fff;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Form styling */
        .upload-section {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            margin-bottom: 30px;
        }
        
        .form-card {
            flex: 1;
            min-width: 300px;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            background-color: white;
        }
        
        .form-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #edf2f7;
            color: #4D68F9;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        .form-label {
            display: block;
            margin-bottom: 6px;
            font-weight: 500;
        }
        
        .form-input {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid #e2e8f0;
            border-radius: 4px;
            font-size: 14px;
        }
        
        .form-select {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid #e2e8f0;
            border-radius: 4px;
            font-size: 14px;
            background-color: white;
        }
        
        .form-button {
            background-color: #4D68F9;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 10px 16px;
            font-size: 14px;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        
        .form-button:hover {
            background-color: #3a56e4;
        }
        
        .file-drop-area {
            border: 2px dashed #e2e8f0;
            border-radius: 5px;
            padding: 25px;
            text-align: center;
            margin-bottom: 15px;
            background-color: #f8fafc;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        
        .file-drop-area:hover {
            background-color: #f0f4f8;
        }
        
        .file-icon {
            font-size: 2rem;
            color: #a0aec0;
            margin-bottom: 10px;
        }
        
        .dragover {
            background-color: #ebf4ff;
            border-color: #4D68F9;
        }
        
        /* Document sets display */
        .docsets-section {
            margin-top: 40px;
        }
        
        .docsets-header {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #edf2f7;
        }
        
        .docset-container {
            margin-bottom: 25px;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            overflow: hidden;
        }
        
        .docset-header {
            background-color: #f8fafc;
            padding: 15px;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .docset-header:hover {
            background-color: #f0f4f8;
        }
        
        .docset-title {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .docset-chevron {
            transition: transform 0.3s;
        }
        
        .docset-chevron.open {
            transform: rotate(90deg);
        }
        
        .docset-meta {
            display: flex;
            gap: 10px;
        }
        
        .docset-content {
            display: none;
            padding: 0 15px 15px 15px;
        }
        
        .docset-content.open {
            display: block;
        }
        
        /* Badge styling */
        .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .appellant-badge {
            background-color: rgba(49, 130, 206, 0.1);
            color: #3182ce;
        }
        
        .respondent-badge {
            background-color: rgba(229, 62, 62, 0.1);
            color: #e53e3e;
        }
        
        .shared-badge {
            background-color: rgba(128, 128, 128, 0.1);
            color: #666;
        }
        
        /* Document list styling */
        .documents-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        
        .documents-table th {
            text-align: left;
            padding: 12px;
            background-color: #f8fafc;
            border-bottom: 1px solid #edf2f7;
            font-weight: 600;
        }
        
        .documents-table td {
            padding: 12px;
            border-bottom: 1px solid #edf2f7;
        }
        
        .documents-table tr:hover {
            background-color: #f8fafc;
        }
        
        .doc-actions {
            display: flex;
            gap: 10px;
        }
        
        .action-button {
            padding: 4px 8px;
            border-radius: 4px;
            border: 1px solid #e2e8f0;
            background-color: #f8fafc;
            cursor: pointer;
            font-size: 12px;
        }
        
        .action-button:hover {
            background-color: #f0f4f8;
        }
        
        .info-message {
            padding: 15px;
            background-color: #ebf8ff;
            border-left: 4px solid #4299e1;
            margin: 15px 0;
            border-radius: 4px;
        }
        
        .empty-state {
            text-align: center;
            padding: 30px;
            color: #718096;
        }
        
        /* Upload progress */
        .upload-progress-container {
            margin-top: 15px;
        }
        
        .progress-bar {
            height: 8px;
            background-color: #edf2f7;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 8px;
        }
        
        .progress-fill {
            height: 100%;
            background-color: #4D68F9;
            width: 0%;
            transition: width 0.3s;
        }
        
        .progress-text {
            font-size: 12px;
            color: #718096;
        }
        
        /* Toast notification */
        .toast {
            position: fixed;
            bottom: 30px;
            right: 30px;
            padding: 15px 20px;
            background-color: #2d3748;
            color: white;
            border-radius: 4px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 1000;
        }
        
        .toast.show {
            opacity: 1;
        }
        
        /* Upload list */
        .uploaded-files {
            margin-top: 20px;
        }
        
        .upload-item {
            display: flex;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #edf2f7;
        }
        
        .upload-item:last-child {
            border-bottom: none;
        }
        
        .upload-item-icon {
            margin-right: 15px;
            color: #4D68F9;
        }
        
        .upload-item-details {
            flex-grow: 1;
        }
        
        .upload-item-name {
            font-weight: 500;
            margin-bottom: 4px;
        }
        
        .upload-item-meta {
            font-size: 12px;
            color: #718096;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="upload-section">
            <!-- Create Document Set Form -->
            <div class="form-card">
                <div class="form-title">Create New Document Set</div>
                <div class="form-group">
                    <label class="form-label" for="set-name">Set Name</label>
                    <input type="text" id="set-name" class="form-input" placeholder="e.g., Appeal Documents">
                </div>
                <div class="form-group">
                    <label class="form-label" for="set-party">Party</label>
                    <select id="set-party" class="form-select">
                        <option value="Appellant">Appellant</option>
                        <option value="Respondent">Respondent</option>
                        <option value="Mixed">Mixed</option>
                        <option value="Shared">Shared</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label" for="set-category">Category</label>
                    <input type="text" id="set-category" class="form-input" placeholder="e.g., Appeal">
                </div>
                <button id="create-set-btn" class="form-button">Create Document Set</button>
            </div>
            
            <!-- Upload Document Form -->
            <div class="form-card">
                <div class="form-title">Upload Document to Set</div>
                <div class="form-group">
                    <label class="form-label" for="select-set">Select Document Set</label>
                    <select id="select-set" class="form-select">
                        <option value="" disabled selected>Select a document set</option>
                        <!-- Options will be populated by JavaScript -->
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label" for="doc-name">Document Name</label>
                    <input type="text" id="doc-name" class="form-input" placeholder="e.g., Statement of Appeal">
                </div>
                <div class="form-group">
                    <label class="form-label" for="doc-party">Document Party</label>
                    <select id="doc-party" class="form-select">
                        <option value="Appellant">Appellant</option>
                        <option value="Respondent">Respondent</option>
                        <option value="Shared">Shared</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Upload File</label>
                    <div id="file-drop-area" class="file-drop-area">
                        <div class="file-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                                <polyline points="17 8 12 3 7 8"></polyline>
                                <line x1="12" y1="3" x2="12" y2="15"></line>
                            </svg>
                        </div>
                        <p>Drag & drop files here or click to browse</p>
                        <input type="file" id="file-upload" style="display: none;">
                    </div>
                </div>
                <div id="upload-progress-container" class="upload-progress-container" style="display: none;">
                    <div class="progress-bar">
                        <div id="progress-fill" class="progress-fill"></div>
                    </div>
                    <div id="progress-text" class="progress-text">Uploading 0%</div>
                </div>
                <div id="uploaded-file-info" style="display: none; margin-top: 15px;">
                    <div style="font-weight: 500; margin-bottom: 5px;">Uploaded File:</div>
                    <div id="uploaded-filename" style="font-size: 14px;"></div>
                </div>
                <button id="upload-doc-btn" class="form-button" style="margin-top: 15px;">Upload Document</button>
            </div>
        </div>
        
        <!-- Recently Uploaded Files Section -->
        <div class="uploaded-files">
            <div class="form-title">Recently Uploaded Files</div>
            <div id="upload-list">
                <!-- Will be populated by JavaScript -->
                <div class="empty-state">
                    <p>No files uploaded yet</p>
                </div>
            </div>
        </div>
        
        <!-- Document Sets Section -->
        <div class="docsets-section">
            <div class="docsets-header">Document Sets</div>
            <div id="docsets-container">
                <!-- Will be populated by JavaScript -->
            </div>
        </div>
        
        <div id="toast" class="toast">Document uploaded successfully!</div>
    </div>
    
    <script>
        // Sample document sets data - in real implementation this would come from the backend
        const documentSets = [
            {
                "id": "appeal",
                "name": "Appeal",
                "party": "Mixed",
                "category": "Appeal",
                "isGroup": true,
                "documents": [
                    {"id": "1", "name": "1. Statement of Appeal", "party": "Appellant", "category": "Appeal", "upload_date": "2023-04-15"},
                    {"id": "2", "name": "2. Request for a Stay", "party": "Appellant", "category": "Appeal", "upload_date": "2023-04-16"}
                ]
            },
            {
                "id": "provisional_messier",
                "name": "provisional messier",
                "party": "Respondent",
                "category": "provisional messier",
                "isGroup": true,
                "documents": [
                    {"id": "3", "name": "3. Answer to Request for PM", "party": "Respondent", "category": "provisional messier", "upload_date": "2023-04-20"}
                ]
            }
        ];
        
        // Populate document sets dropdown
        function populateDocSetsDropdown() {
            const selectSet = document.getElementById('select-set');
            selectSet.innerHTML = '<option value="" disabled selected>Select a document set</option>';
            
            documentSets.forEach(set => {
                const option = document.createElement('option');
                option.value = set.id;
                option.textContent = `${set.name} (${set.party})`;
                selectSet.appendChild(option);
            });
        }
        
        // Render document sets
        function renderDocumentSets() {
            const container = document.getElementById('docsets-container');
            container.innerHTML = '';
            
            if (documentSets.length === 0) {
                container.innerHTML = '<div class="empty-state"><p>No document sets created yet</p></div>';
                return;
            }
            
            documentSets.forEach((set, index) => {
                const docsetContainer = document.createElement('div');
                docsetContainer.className = 'docset-container';
                
                // Create header
                const header = document.createElement('div');
                header.className = 'docset-header';
                header.onclick = () => toggleDocsetContent(set.id);
                
                // Create badge class based on party
                const badgeClass = `${set.party.toLowerCase()}-badge`;
                
                header.innerHTML = `
                    <div class="docset-title">
                        <svg class="docset-chevron" id="chevron-${set.id}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6"></polyline>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                        </svg>
                        ${set.name}
                    </div>
                    <div class="docset-meta">
                        <span class="badge ${badgeClass}">${set.party}</span>
                        <span class="badge">${set.category}</span>
                        <span class="badge">${set.documents.length} documents</span>
                    </div>
                `;
                
                // Create content
                const content = document.createElement('div');
                content.className = 'docset-content';
                content.id = `docset-content-${set.id}`;
                
                if (set.documents.length > 0) {
                    // Create table
                    const table = document.createElement('table');
                    table.className = 'documents-table';
                    
                    // Create table header
                    const thead = document.createElement('thead');
                    thead.innerHTML = `
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Party</th>
                            <th>Upload Date</th>
                            <th>Actions</th>
                        </tr>
                    `;
                    table.appendChild(thead);
                    
                    // Create table body
                    const tbody = document.createElement('tbody');
                    
                    set.documents.forEach(doc => {
                        const docBadgeClass = `${doc.party.toLowerCase()}-badge`;
                        
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${doc.id}</td>
                            <td>${doc.name}</td>
                            <td><span class="badge ${docBadgeClass}">${doc.party}</span></td>
                            <td>${doc.upload_date}</td>
                            <td>
                                <div class="doc-actions">
                                    <button class="action-button" onclick="viewDocument('${set.id}', '${doc.id}')">View</button>
                                    <button class="action-button" onclick="editDocument('${set.id}', '${doc.id}')">Edit</button>
                                    <button class="action-button" onclick="deleteDocument('${set.id}', '${doc.id}')">Delete</button>
                                </div>
                            </td>
                        `;
                        
                        tbody.appendChild(row);
                    });
                    
                    table.appendChild(tbody);
                    content.appendChild(table);
                } else {
                    content.innerHTML = '<div class="info-message">No documents in this set yet</div>';
                }
                
                // Add set actions
                const actions = document.createElement('div');
                actions.style.marginTop = '15px';
                actions.style.display = 'flex';
                actions.style.gap = '10px';
                
                const editBtn = document.createElement('button');
                editBtn.className = 'form-button';
                editBtn.style.backgroundColor = '#718096';
                editBtn.textContent = 'Edit Set';
                editBtn.onclick = (e) => {
                    e.stopPropagation();
                    editDocumentSet(set.id);
                };
                
                const deleteBtn = document.createElement('button');
                deleteBtn.className = 'form-button';
                deleteBtn.style.backgroundColor = '#e53e3e';
                deleteBtn.textContent = 'Delete Set';
                deleteBtn.onclick = (e) => {
                    e.stopPropagation();
                    deleteDocumentSet(set.id);
                };
                
                actions.appendChild(editBtn);
                actions.appendChild(deleteBtn);
                content.appendChild(actions);
                
                docsetContainer.appendChild(header);
                docsetContainer.appendChild(content);
                container.appendChild(docsetContainer);
                
                // Open the first docset by default
                if (index === 0) {
                    toggleDocsetContent(set.id);
                }
            });
        }
        
        // Toggle docset content visibility
        function toggleDocsetContent(docsetId) {
            const content = document.getElementById(`docset-content-${docsetId}`);
            const chevron = document.getElementById(`chevron-${docsetId}`);
            
            if (content.classList.contains('open')) {
                content.classList.remove('open');
                chevron.classList.remove('open');
            } else {
                content.classList.add('open');
                chevron.classList.add('open');
            }
        }
        
        // File upload handling
        const fileDropArea = document.getElementById('file-drop-area');
        const fileUpload = document.getElementById('file-upload');
        
        fileDropArea.addEventListener('click', () => {
            fileUpload.click();
        });
        
        fileDropArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            fileDropArea.classList.add('dragover');
        });
        
        fileDropArea.addEventListener('dragleave', () => {
            fileDropArea.classList.remove('dragover');
        });
        
        fileDropArea.addEventListener('drop', (e) => {
            e.preventDefault();
            fileDropArea.classList.remove('dragover');
            
            if (e.dataTransfer.files.length) {
                handleFileUpload(e.dataTransfer.files[0]);
            }
        });
        
        fileUpload.addEventListener('change', (e) => {
            if (e.target.files.length) {
                handleFileUpload(e.target.files[0]);
            }
        });
        
        function handleFileUpload(file) {
            // Display file info
            const fileInfo = document.getElementById('uploaded-file-info');
            const filename = document.getElementById('uploaded-filename');
            
            filename.textContent = file.name;
            fileInfo.style.display = 'block';
            
            // Simulate upload progress
            const progressContainer = document.getElementById('upload-progress-container');
            const progressFill = document.getElementById('progress-fill');
            const progressText = document.getElementById('progress-text');
            
            progressContainer.style.display = 'block';
            
            let progress = 0;
            const interval = setInterval(() => {
                progress += 5;
                progressFill.style.width = `${progress}%`;
                progressText.textContent = `Uploading ${progress}%`;
                
                if (progress >= 100) {
                    clearInterval(interval);
                    progressText.textContent = 'Upload complete';
                    
                    // Hide progress after a delay
                    setTimeout(() => {
                        progressContainer.style.display = 'none';
                    }, 2000);
                }
            }, 100);
        }
        
        // Create document set
        document.getElementById('create-set-btn').addEventListener('click', () => {
            const setName = document.getElementById('set-name').value;
            const setParty = document.getElementById('set-party').value;
            const setCategory = document.getElementById('set-category').value;
            
            if (!setName) {
                alert('Please enter a set name');
                return;
            }
            
            // Create new document set
            const newSet = {
                id: 'set_' + Date.now().toString(36),
                name: setName,
                party: setParty,
                category: setCategory,
                isGroup: true,
                documents: []
            };
            
            documentSets.push(newSet);
            
            // Clear form
            document.getElementById('set-name').value = '';
            document.getElementById('set-category').value = '';
            
            // Update UI
            populateDocSetsDropdown();
            renderDocumentSets();
            
            // Show toast
            showToast('Document set created successfully!');
        });
        
        // Upload document
        document.getElementById('upload-doc-btn').addEventListener('click', () => {
            const setId = document.getElementById('select-set').value;
            const docName = document.getElementById('doc-name').value;
            const docParty = document.getElementById('doc-party').value;
            const fileInfo = document.getElementById('uploaded-file-info');
            
            if (!setId) {
                alert('Please select a document set');
                return;
            }
            
            if (!docName) {
                alert('Please enter a document name');
                return;
            }
            
            if (fileInfo.style.display === 'none') {
                alert('Please upload a file');
                return;
            }
            
            // Find document set
            const docSet = documentSets.find(set => set.id === setId);
            
            if (!docSet) {
                alert('Document set not found');
                return;
            }
            
            // Create new document
            const newDoc = {
                id: (docSet.documents.length + 1).toString(),
                name: `${docSet.documents.length + 1}. ${docName}`,
                party: docParty,
                category: docSet.category,
                upload_date: new Date().toISOString().split('T')[0]
            };
            
            docSet.documents.push(newDoc);
            
            // Clear form
            document.getElementById('doc-name').value = '';
            document.getElementById('uploaded-file-info').style.display = 'none';
            document.getElementById('upload-progress-container').style.display = 'none';
            
            // Update UI
            renderDocumentSets();
            updateRecentUploads(newDoc, docSet.name);
            
            // Show toast
            showToast('Document uploaded successfully!');
        });
        
        // Document actions
        function viewDocument(setId, docId) {
            alert(`View document ${docId} from set ${setId}`);
        }
        
        function editDocument(setId, docId) {
            alert(`Edit document ${docId} from set ${setId}`);
        }
        
        function deleteDocument(setId, docId) {
            const confirmed = confirm('Are you sure you want to delete this document?');
            
            if (confirmed) {
                const docSet = documentSets.find(set => set.id === setId);
                
                if (docSet) {
                    docSet.documents = docSet.documents.filter(doc => doc.id !== docId);
                    renderDocumentSets();
                    showToast('Document deleted successfully!');
                }
            }
        }
        
        // Document set actions
        function editDocumentSet(setId) {
            alert(`Edit document set ${setId}`);
        }
        
        function deleteDocumentSet(setId) {
            const confirmed = confirm('Are you sure you want to delete this document set? All documents in this set will be deleted as well.');
            
            if (confirmed) {
                const index = documentSets.findIndex(set => set.id === setId);
                
                if (index !== -1) {
                    documentSets.splice(index, 1);
                    populateDocSetsDropdown();
                    renderDocumentSets();
                    showToast('Document set deleted successfully!');
                }
            }
        }
        
        // Update recently uploaded files list
        function updateRecentUploads(document, setName) {
            const uploadList = document.getElementById('upload-list');
            
            // Remove empty state if exists
            const emptyState = uploadList.querySelector('.empty-state');
            if (emptyState) {
                uploadList.removeChild(emptyState);
            }
            
            // Create upload item
            const uploadItem = document.createElement('div');
            uploadItem.className = 'upload-item';
            
            // Determine icon based on file type
            let icon = `
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                    <line x1="16" y1="13" x2="8" y2="13"></line>
                    <line x1="16" y1="17" x2="8" y2="17"></line>
                    <polyline points="10 9 9 9 8 9"></polyline>
                </svg>
            `;
            
            uploadItem.innerHTML = `
                <div class="upload-item-icon">${icon}</div>
                <div class="upload-item-details">
                    <div class="upload-item-name">${document.name}</div>
                    <div class="upload-item-meta">
                        Uploaded to ${setName} • ${document.upload_date}
                    </div>
                </div>
            `;
            
            // Add to top of list
            uploadList.insertBefore(uploadItem, uploadList.firstChild);
            
            // Limit to 5 recent uploads
            if (uploadList.children.length > 5) {
                uploadList.removeChild(uploadList.lastChild);
            }
        }
        
        // Show toast notification
        function showToast(message) {
            const toast = document.getElementById('toast');
            toast.textContent = message;
            toast.classList.add('show');
            
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }
        
        // Initialize the page
        function init() {
            populateDocSetsDropdown();
            renderDocumentSets();
        }
        
        // Initialize when DOM is loaded
        document.addEventListener('DOMContentLoaded', init);
        
        // Initialize immediately (for preview purposes)
        init();
    </script>
</body>
</html>
