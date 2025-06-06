import React, { useState } from 'react';
import { Upload, Clock, Search, FileText, Database, Scale } from 'lucide-react';

const Logo = () => (
  <svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" viewBox="0 0 175 175" className="w-10 h-10">
    <mask id="whatsapp-mask" maskUnits="userSpaceOnUse">
      <path d="M174.049 0.257812H0V174.258H174.049V0.257812Z" fill="white"/>
    </mask>
    <g mask="url(#whatsapp-mask)">
      <path d="M136.753 0.257812H37.2963C16.6981 0.257812 0 16.9511 0 37.5435V136.972C0 157.564 16.6981 174.258 37.2963 174.258H136.753C157.351 174.258 174.049 157.564 174.049 136.972V37.5435C174.049 16.9511 157.351 0.257812 136.753 0.257812Z" fill="#4D68F9"/>
      <path fillRule="evenodd" clipRule="evenodd" d="M137.367 54.0014C126.648 40.3105 110.721 32.5723 93.3045 32.5723C63.2347 32.5723 38.5239 57.1264 38.5239 87.0377C38.5239 96.9229 41.1859 106.155 45.837 114.103L45.6925 113.966L37.918 141.957L65.5411 133.731C73.8428 138.579 83.5458 141.355 93.8997 141.355C111.614 141.355 127.691 132.723 137.664 119.628L114.294 101.621C109.53 108.467 101.789 112.187 93.4531 112.187C79.4603 112.187 67.9982 100.877 67.9982 87.0377C67.9982 72.9005 79.6093 61.7396 93.751 61.7396C102.236 61.7396 109.679 65.9064 114.294 72.3052L137.367 54.0014Z" fill="white"/>
    </g>
  </svg>
);

const NavigationButton = ({ icon: Icon, title, description, active, color, iconColor }) => (
  <button className={`flex items-center gap-3 w-full p-3 rounded-lg hover:bg-gray-50 ${active ? 'bg-blue-50' : ''}`}>
    <div className={`${color} p-1 rounded-lg`}>
      <Icon className={`w-5 h-5 ${iconColor}`} />
    </div>
    <div className="text-left">
      <div className="text-sm font-medium text-gray-900">{title}</div>
      <div className="text-xs text-gray-500">{description}</div>
    </div>
  </button>
);

const DocumentPreview = ({ title, page, line, content, highlight, explanation }) => (
  <div className="border border-gray-100 rounded-xl bg-white shadow-sm hover:shadow-md transition-shadow duration-200">
    <div className="border-b border-gray-50 p-6">
      <div className="flex justify-between items-start gap-4">
        <div className="flex-1">
          <h4 className="text-lg font-semibold text-gray-900 mb-2">{title}</h4>
          <div className="flex items-center gap-2 text-sm text-gray-500">
            <FileText className="w-4 h-4" />
            <span>page: {page}</span>
            <span>•</span>
            <span>line(s): {line}</span>
          </div>
        </div>
        <button className="flex items-center gap-1 px-3 py-1.5 bg-blue-50 text-blue-600 text-xs font-medium hover:bg-blue-100 rounded-lg transition-all duration-200 border border-blue-200">
          <span>Preview</span>
          <span className="text-xs">↗</span>
        </button>
      </div>
    </div>
    <div className="p-6 space-y-4">
      <div className="bg-gray-50 border border-gray-100 rounded-lg mb-4">
        <div className="px-4 py-3 border-b border-gray-100 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 bg-gray-400 rounded-full"></div>
            <span className="text-sm font-medium text-gray-700">Context & Relevance</span>
          </div>
          <div className="px-2 py-1 bg-gray-100 rounded-md">
            <span className="text-xs font-medium text-gray-600">AI Analysis</span>
          </div>
        </div>
        <div className="p-4">
          <p className="text-sm text-gray-600 leading-relaxed">{explanation}</p>
        </div>
      </div>
      <div className="text-sm text-gray-600 leading-relaxed space-y-4">
        <div className="bg-white border border-gray-100 rounded-lg p-4">
          <p>
            <span className="bg-green-50 text-gray-800 px-2 mx-1 rounded-md border border-green-100">{highlight}</span>
            {content}
          </p>
        </div>
        <div className="flex items-center gap-2 text-xs text-gray-500">
          <div className="flex items-center gap-1">
            <div className="w-3 h-3 bg-green-50 border border-green-100 rounded"></div>
            <span>Highlighted sections indicate key relevance</span>
          </div>
        </div>
      </div>
    </div>
  </div>
);

const DocumentViewer = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [activeTab, setActiveTab] = useState('All');
  const [showResults, setShowResults] = useState(false);

  const handleSearch = (e) => {
    setSearchQuery(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && searchQuery.trim()) {
      setShowResults(true);
      e.preventDefault();
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="flex gap-6 h-[calc(100vh-48px)]">
        {/* Sidebar - Fixed */}
        <div className="w-72 bg-white rounded-2xl border border-gray-100 px-4 py-6 flex flex-col h-full sticky top-6">
          <div className="flex items-center mb-8">
            <div className="bg-white p-3 rounded-lg">
              <Logo />
            </div>
            <span className="text-2xl font-semibold">caselens</span>
          </div>

          <button className="w-full bg-blue-50 text-blue-700 px-4 py-2 rounded-lg flex items-center justify-center gap-2 mb-12 border border-blue-200 text-sm">
            <Upload className="w-4 h-4" />
            <span>Upload records</span>
          </button>

          <div className="space-y-6">
            <div className="flex justify-between mb-6">
              <h3 className="text-sm font-medium text-gray-500">Legal Agents</h3>
              <p className="text-xs text-gray-400">Drag to connect</p>
            </div>

            <div className="space-y-4">
              <NavigationButton
                icon={Database}
                title="Central Database"
                description="Connected to all agents"
                iconColor="text-gray-600"
                color="bg-gray-100"
              />
              <NavigationButton
                icon={Clock}
                title="Event Timeline"
                description="Create case event chronology"
                iconColor="text-blue-500"
                color="bg-blue-100"
              />
              <NavigationButton
                icon={Search}
                title="Document Investigation"
                description="Autoreview document for specific tasks"
                active={true}
                iconColor="text-blue-600"
                color="bg-blue-100"
              />
              <NavigationButton
                icon={Scale}
                title="Compliance Check"
                description="Checking submission against procedural rules"
                iconColor="text-green-400"
                color="bg-green-50"
              />
              <NavigationButton
                icon={FileText}
                title="Citation Check"
                description="Validate your citation against facts"
                iconColor="text-orange-500"
                color="bg-orange-50"
              />
            </div>
          </div>

          <div className="mt-6 pt-4 flex items-center gap-3 px-2">
            <div className="bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm font-semibold">
              JD
            </div>
            <div>
              <div className="text-sm font-medium text-gray-900">John Doe</div>
              <div className="text-sm text-gray-500">Senior Legal Analyst</div>
            </div>
            <div className="ml-auto w-2 h-2 bg-green-500 rounded-full"></div>
          </div>
        </div>

        {/* Main Content - Scrollable */}
        <div className="flex-1 overflow-y-auto">
          <div className="bg-white rounded-xl">
            <div className="border-b border-gray-100 p-6">
              <h2 className="text-xl font-semibold">Document Investigation</h2>
            </div>
            
            <div className="p-6">
              <form onSubmit={(e) => e.preventDefault()} className="flex items-center gap-2 p-2 border rounded-lg bg-gray-50 mb-6">
                <Search className="w-4 h-4 text-gray-400" />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={handleSearch}
                  onKeyPress={handleKeyPress}
                  placeholder="Provide all the documents relevant to the satellite collision"
                  className="flex-1 bg-transparent outline-none"
                />
              </form>

              {showResults && (
                <div className="space-y-8">
                  <div className="flex flex-col gap-4">
                    <div className="space-y-4 mb-2">
                      <div className="flex items-center justify-between">
                        <div className="bg-white p-1.5 rounded-2xl border border-gray-100 flex items-center">
                          {['All', 'Respondent', 'Claimant'].map((tab) => {
                            const isActive = activeTab === tab;
                            const count = tab === 'All' ? 2 : 1;
                            return (
                              <button
                                key={tab}
                                onClick={() => setActiveTab(tab)}
                                className={`relative px-6 py-2.5 rounded-xl text-sm font-medium transition-all duration-300 flex items-center gap-2 group
                                  ${isActive 
                                    ? 'bg-blue-50/80 text-blue-600' 
                                    : 'text-gray-400 hover:bg-gray-50 hover:text-gray-600'
                                  }`}
                              >
                                <div className={`w-2 h-2 rounded-full transition-all duration-300
                                  ${isActive
                                    ? 'bg-blue-200'
                                    : tab === 'All'
                                      ? 'bg-gray-100 group-hover:bg-gray-200'
                                      : tab === 'Respondent'
                                        ? 'bg-emerald-300'
                                        : 'bg-amber-300'
                                  }`}
                                />
                                <span>{tab}</span>
                                {isActive && (
                                  <div className="px-1.5 py-0.5 bg-blue-100/50 rounded-full text-xs ml-1">
                                    {count}
                                  </div>
                                )}
                              </button>
                            );
                          })}
                        </div>

                        <div className="flex items-center gap-3">
                          <div className="flex items-center gap-6 px-4 py-2 bg-gray-50/50 rounded-xl">
                            <div className="flex items-center gap-2">
                              <div className="w-2 h-2 rounded-full bg-emerald-300"></div>
                              <span className="text-sm text-gray-600">Respondent</span>
                              <span className="text-sm font-medium text-gray-700">1 doc</span>
                            </div>
                            <div className="flex items-center gap-2">
                              <div className="w-2 h-2 rounded-full bg-amber-300"></div>
                              <span className="text-sm text-gray-600">Claimant</span>
                              <span className="text-sm font-medium text-gray-700">1 doc</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div className="bg-gradient-to-r from-blue-50 to-blue-50/50 border border-blue-100 rounded-xl shadow-sm">
                      <div className="px-6 py-4 border-b border-blue-100">
                        <div className="flex items-center gap-3">
                          <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                          <h3 className="text-lg font-semibold text-gray-900">General Answer</h3>
                          <div className="ml-auto flex items-center gap-2">
                            <div className="px-2 py-1 bg-blue-100/50 rounded-md">
                              <span className="text-xs font-medium text-blue-700">AI Generated</span>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div className="px-6 py-6">
                        <div className="space-y-4">
                          <p className="text-sm text-gray-700 leading-relaxed">
                            Based on the provided query, I've identified two key documents that are highly relevant to the satellite collision incident:
                          </p>
                          <div className="pl-4 border-l-2 border-blue-200">
                            <ul className="space-y-3">
                              <li className="text-sm text-gray-700">
                                <span className="font-medium text-blue-700">DoD Investigation Report:</span> A comprehensive analysis of the collision event, including detailed telemetry data and system logs.
                              </li>
                              <li className="text-sm text-gray-700">
                                <span className="font-medium text-blue-700">DoD Order (March 1, 2021):</span> Official directive addressing system deficiencies and mandating operational changes for satellites at 400 km orbits.
                              </li>
                            </ul>
                          </div>
                          <div className="flex items-center gap-2 pt-2">
                            <div className="w-1 h-1 bg-blue-400 rounded-full"></div>
                            <p className="text-xs text-gray-500">Documents are sorted by relevance and chronological order</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div className="grid gap-6">
                    <div className="flex items-center gap-3">
                      <h3 className="text-lg font-semibold text-gray-900">Found 5 matching documents</h3>
                      <div className="px-3 py-1 bg-blue-50 text-blue-700 rounded-full text-sm font-medium">100% match</div>
                    </div>
                    
                    <DocumentPreview
                      title="Exhibit C-9: DoD Order of 1 March 2021 to Adjust Orbits of 400 km Satellites and Continue to Suspend Operation"
                      page="27"
                      line="650"
                      highlight="Based on the Department of Defense's investigation of the AS100 satellite collision, we have identified both software and hardware deficiencies in the collision avoidance system of the Astra satellites."
                      content=" Following this discovery, we conducted a thorough review of all operational protocols and implemented immediate corrective measures to address these identified deficiencies. The findings have led to a comprehensive overhaul of our satellite management systems and the establishment of new safety protocols to prevent similar incidents in the future."
                      explanation="This is a pivotal regulatory document issued by the Department of Defense that directly addresses the satellite collision incident. The order outlines specific findings from their investigation, particularly focusing on technical system failures. It mandates immediate operational changes for satellites in 400 km orbits and establishes new safety requirements. This document is crucial as it provides official confirmation of system deficiencies and forms the basis for subsequent corrective actions."
                    />

                    <DocumentPreview
                      title="Exhibit C-12: Collision Incident Report"
                      page="69"
                      line="1690"
                      highlight="This report analyses the events and key undertakings of a collision that occurred on 1 January 2021 at 08:54:32 CET between the CubeSat (CS007)"
                      content=" The Department of Defense's Space Surveillance Division has completed its comprehensive investigation of the recent orbital incident. This investigation was conducted in accordance with International Space Safety Protocol Section 7.2. Through detailed analysis of telemetry data and system logs, our investigation team has reconstructed the sequence of events leading to the incident."
                      explanation="This is the primary incident report documenting the satellite collision. Created immediately after the event, it provides the most detailed chronological account of the incident, including precise timing and satellite identification. The report's findings are based on real-time telemetry data and follow strict international protocols for space incident investigation. This document serves as the foundation for understanding the technical circumstances of the collision."
                    />

                    <DocumentPreview
                      title="Exhibit C-15: Technical Analysis Report on Satellite Control Systems"
                      page="42"
                      line="892"
                      highlight="Analysis of the control system logs revealed critical vulnerabilities in the collision avoidance algorithms, particularly in their response to rapidly changing orbital parameters."
                      content=" The investigation team identified multiple instances where the system failed to properly calculate approach vectors, leading to delayed or insufficient avoidance maneuvers. This technical analysis provides detailed recommendations for algorithm improvements and system redundancy measures."
                      explanation="This technical report provides an in-depth analysis of the satellite control systems involved in the collision. It identifies specific technical failures in the collision avoidance algorithms and provides crucial insights into the system's vulnerabilities. The document is particularly valuable for understanding the technical root causes of the incident."
                    />

                    <DocumentPreview
                      title="Exhibit C-18: Orbital Debris Assessment Report"
                      page="15"
                      line="337"
                      highlight="Post-collision analysis indicates the creation of approximately 2,300 trackable debris fragments measuring larger than 10cm, significantly impacting the operational safety of neighboring satellite networks."
                      content=" The report outlines the projected orbital paths of major debris fragments and their potential impact on other satellite operations in Low Earth Orbit. Our tracking systems have implemented enhanced monitoring protocols for these debris clouds."
                      explanation="This report details the aftermath of the satellite collision, focusing on the resulting orbital debris field. It provides critical information about the scope of the debris spread and its implications for other satellite operations. The document is essential for understanding the broader impact of the incident on space operations."
                    />

                    <DocumentPreview
                      title="Exhibit C-21: International Space Station Safety Protocol Amendment"
                      page="8"
                      line="175"
                      highlight="In response to the January 2021 satellite collision event, new safety protocols have been implemented requiring all commercial satellites operating within 100km of the ISS to maintain enhanced communication channels."
                      content=" These amended protocols establish stricter requirements for real-time position reporting and mandate immediate response procedures for potential collision scenarios. All commercial operators must now demonstrate compliance with these enhanced safety measures."
                      explanation="This document outlines the regulatory changes implemented in response to the satellite collision. It details new safety requirements and operational procedures that directly resulted from the incident. The document demonstrates the broader regulatory impact of the collision on space operations near the International Space Station."
                    />
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DocumentViewer;
