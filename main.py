import React, { useState } from 'react';
import { 
  FileText, 
  Clock, 
  AlertCircle, 
  Activity, 
  Search, 
  Upload, 
  Database, 
  CircleEllipsis, 
  Eye, 
  ChevronDown, 
  ChevronRight 
} from 'lucide-react';

// Fixed color components
const GrayIcon = ({ children }) => (
  <div className="w-6 h-6 rounded-lg flex items-center justify-center bg-gray-50">
    {children}
  </div>
);

const BlueIcon = ({ children }) => (
  <div className="w-6 h-6 rounded-lg flex items-center justify-center bg-blue-50">
    {children}
  </div>
);

const RedIcon = ({ children }) => (
  <div className="w-6 h-6 rounded-lg flex items-center justify-center bg-red-50">
    {children}
  </div>
);

const GreenIcon = ({ children }) => (
  <div className="w-6 h-6 rounded-lg flex items-center justify-center bg-green-50">
    {children}
  </div>
);

const OrangeIcon = ({ children }) => (
  <div className="w-6 h-6 rounded-lg flex items-center justify-center bg-orange-50">
    {children}
  </div>
);

const ModernLegalInterface = () => {
  const [expandedEvents, setExpandedEvents] = useState({0: true});

  const toggleEvent = (index) => {
    setExpandedEvents((prev) => ({
      ...prev,
      [index]: !prev[index]
    }));
  };

  const timelineEvents = [
    {
      date: '14 March 2000',
      title: 'Contract Execution - Al-Ghaida Road Project',
      tags: ['Contract', 'Phase II', 'Construction'],
      description: 'The Parties concluded a contract for the construction of 19 km of Phase II of the Al-Ghaida internal roads.',
      citations: 6,
      parties: ['Claimant', 'Respondent']
    },
    {
      date: '15 April 2000',
      title: 'Notice to Proceed Issued',
      tags: ['Notice', 'Commencement'],
      description: 'Official notice to proceed with construction works was issued by the Ministry of Public Works.',
      citations: 4,
      parties: ['Claimant']
    },
    {
      date: '30 June 2000',
      title: 'Site Access Delay',
      tags: ['Delay', 'Site Access'],
      description: 'Contractor reported difficulties accessing certain sections of the project site due to local disputes.',
      citations: 8,
      parties: ['Claimant', 'Respondent']
    },
    {
      date: '15 September 2000',
      title: 'First Progress Payment',
      tags: ['Payment', 'Milestone'],
      description: 'First milestone payment of USD 2.5M processed for completed earthworks and preliminary road foundation.',
      citations: 3,
      parties: ['Claimant']
    },
    {
      date: '22 December 2000',
      title: 'Force Majeure Notice',
      tags: ['Force Majeure', 'Delay'],
      description: 'Contractor submitted force majeure notice due to unprecedented rainfall causing significant site flooding.',
      citations: 12,
      parties: ['Claimant', 'Respondent']
    }
  ];

  const documents = [
    {
      title: 'DLP Board Minutes',
      exhibit: 'Exh. C-22, p. 3-4',
      type: 'Minutes',
      description: 'Minutes of DLP Board of Directors\' extraordinary meeting approving Al-Ghaida roads contract.',
      date: '14 March 2000',
      size: '1.2 MB'
    },
    {
      title: 'DLP-Yemen Contract',
      exhibit: 'Exh. C-21, p. 1-15',
      type: 'Contract',
      description: 'Contract for Phase II Al-Ghaida roads project (19km), value: USD 12.5M with 24-month completion period.',
      date: '14 March 2000',
      size: '2.4 MB'
    }
  ];

  const agents = [
    { icon: Database, title: 'Central Database', desc: 'Connected to all agents', color: 'gray' },
    { icon: Clock, title: 'Event Timeline', desc: 'Create case event chronology', color: 'blue' },
    { icon: Search, title: 'Document Investigation', desc: 'Autoreview document for specific tasks', color: 'red' },
    { icon: CircleEllipsis, title: 'Compliance Check', desc: 'Checking submission against procedural rules', color: 'green' },
    { icon: FileText, title: 'Citation Check', desc: 'Validate your citation against facts', color: 'orange' }
  ];

  const renderAgentIcon = (agent) => {
    const Icon = agent.icon;
    switch (agent.color) {
      case 'blue':
        return <BlueIcon><Icon className="w-5 h-5 text-blue-500" /></BlueIcon>;
      case 'red':
        return <RedIcon><Icon className="w-5 h-5 text-red-500" /></RedIcon>;
      case 'green':
        return <GreenIcon><Icon className="w-5 h-5 text-green-500" /></GreenIcon>;
      case 'orange':
        return <OrangeIcon><Icon className="w-5 h-5 text-orange-500" /></OrangeIcon>;
      default:
        return <GrayIcon><Icon className="w-5 h-5 text-gray-500" /></GrayIcon>;
    }
  };

  const AgentItem = ({ agent }) => {
    let containerClass = "flex items-center gap-3 p-4 rounded-lg cursor-pointer ";
    switch (agent.color) {
      case 'blue':
        containerClass += "hover:bg-blue-50";
        break;
      case 'red':
        containerClass += "hover:bg-red-50";
        break;
      case 'green':
        containerClass += "hover:bg-green-50";
        break;
      case 'orange':
        containerClass += "hover:bg-orange-50";
        break;
      default:
        containerClass += "hover:bg-gray-50";
    }

    return (
      <div className={containerClass}>
        {renderAgentIcon(agent)}
        <div>
          <div className="text-sm font-medium text-gray-900">{agent.title}</div>
          <div className="text-xs text-gray-500">{agent.desc}</div>
        </div>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="flex p-4 h-full">
        <div className="w-72 bg-white rounded-2xl border border-gray-100 m-4 flex flex-col justify-between">
          <div>
            <div className="p-6">
              <div className="flex items-center gap-2 mb-12">
                <div className="bg-blue-600 rounded-lg p-1.5">
                  <FileText className="w-6 h-6 text-white" />
                </div>
                <span className="text-3xl font-bold">caselens</span>
              </div>
              <button className="w-full bg-blue-50 text-blue-600 rounded-lg py-2.5 px-4 flex items-center justify-center gap-2 border border-blue-100">
                <Upload className="w-4 h-4" />
                <span className="text-sm font-medium">Upload records</span>
              </button>
            </div>

            <div className="px-4 pb-4 mt-8">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-sm font-medium text-gray-500">Legal Agents</h2>
                <span className="text-xs text-gray-400">Drag to connect</span>
              </div>
              <div className="flex items-center gap-4 mb-4">
                <span className="flex-1 h-px bg-gray-100"></span>
                <span className="text-xs text-gray-400">5 agents available</span>
                <span className="flex-1 h-px bg-gray-100"></span>
              </div>
              <div className="space-y-3">
                {agents.map((agent, index) => (
                  <AgentItem key={index} agent={agent} />
                ))}
              </div>
            </div>
          </div>
          
          <div className="p-4 mt-auto border-t border-gray-100">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center text-white font-medium">
                JD
              </div>
              <div>
                <div className="text-sm font-medium text-gray-900">John Doe</div>
                <div className="text-xs text-gray-500">Senior Legal Analyst</div>
              </div>
            </div>
          </div>
        </div>

        <div className="flex-1 p-4">
          <div className="bg-white rounded-2xl p-8 mb-6 border border-gray-100">
            <h2 className="text-lg font-semibold text-gray-900 mb-6">Timeline Events</h2>
            <div className="border-l-2 border-gray-100 pl-8 space-y-12">
              {timelineEvents.map((event, index) => (
                <div key={index} className="relative group">
                  <div className="absolute -left-10 w-5 h-5 rounded-full bg-blue-600 shadow-md border-2 border-white transition-all duration-200 group-hover:scale-110 group-hover:bg-blue-700" />
                  <div className="absolute -left-[3.25rem] h-full w-px bg-blue-200 opacity-0 group-hover:opacity-100 transition-opacity duration-200" />
                  <div className="mb-3">
                    <span className="text-blue-600 text-sm font-medium bg-blue-50 px-3 py-1 rounded-full">{event.date}</span>
                  </div>
                  <div className="bg-white rounded-xl shadow-sm border border-gray-100 transition-all duration-200 hover:shadow-md">
                    <button 
                      onClick={() => toggleEvent(index)}
                      className="w-full flex items-start justify-between p-5 hover:bg-gray-50 transition-colors duration-200"
                    >
                      <div className="flex flex-col gap-3">
                        <h3 className="text-lg font-medium text-gray-900 hover:text-blue-600 transition-colors duration-200">{event.title}</h3>
                        <div className="flex flex-wrap items-center gap-2">
                          {event.tags.map((tag, tagIndex) => {
                            let tagClass = "px-3 py-1 rounded-full text-sm font-medium transition-all duration-200 ";
                            if (tag === 'Delay' || tag === 'Force Majeure') {
                              tagClass += "text-amber-600 bg-amber-50 hover:bg-amber-100";
                            } else if (tag === 'Payment') {
                              tagClass += "text-emerald-600 bg-emerald-50 hover:bg-emerald-100";
                            } else if (tag === 'Contract') {
                              tagClass += "text-blue-600 bg-blue-50 hover:bg-blue-100";
                            } else {
                              tagClass += "text-gray-600 bg-gray-50 hover:bg-gray-100";
                            }
                            return (
                              <span key={tagIndex} className={tagClass}>
                                {tag}
                              </span>
                            );
                          })}
                        </div>
                      </div>
                      <div className="flex items-center gap-3">
                        <span className="text-sm text-gray-500 bg-gray-50 px-3 py-1 rounded-full">
                          {event.citations} citations
                        </span>
                        {expandedEvents[index] ? (
                          <ChevronDown className="w-5 h-5 text-gray-400" />
                        ) : (
                          <ChevronRight className="w-5 h-5 text-gray-400" />
                        )}
                      </div>
                    </button>
                    
                    {expandedEvents[index] && (
                      <div className="p-4 border-t border-gray-100">
                        <p className="text-gray-900 mb-4">{event.description}</p>
                        <div className="flex items-center gap-4">
                          <span className="text-blue-600 text-sm">{event.citations} Citations</span>
                          <span className="text-gray-500 text-sm">Addressed by:</span>
                          {event.parties.map((party, partyIndex) => (
                            <span 
                              key={partyIndex} 
                              className={party === 'Claimant' ? 'text-blue-600 text-sm' : 'text-red-600 text-sm'}
                            >
                              {party}
                            </span>
                          ))}
                        </div>
                        
                        {index === 0 && (
                          <>
                            <div className="mt-8">
                              <div className="flex items-center justify-between mb-4">
                                <h3 className="font-medium text-gray-600">Supporting Documents</h3>
                                <div className="flex gap-2">
                                  <button className="text-sm text-gray-500 flex items-center gap-1">Filter</button>
                                  <button className="text-sm text-gray-500 flex items-center gap-1">Sort by Date</button>
                                </div>
                              </div>

                              <div className="space-y-4">
                                {documents.map((doc, docIndex) => (
                                  <div key={docIndex} className="flex items-start gap-4 bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                    <div className="p-3 bg-white rounded-lg">
                                      <FileText className="w-5 h-5 text-gray-400" />
                                    </div>
                                    <div className="flex-1">
                                      <div className="flex items-center gap-2 mb-1">
                                        <span className="font-medium">{doc.title}</span>
                                        <span className="text-gray-500">({doc.exhibit})</span>
                                        <span className="text-blue-600">{doc.type}</span>
                                      </div>
                                      <p className="text-sm text-gray-600 mb-2">{doc.description}</p>
                                      <div className="flex items-center gap-4 text-sm text-gray-500">
                                        <span>{doc.date}</span>
                                        <span>PDF • {doc.size}</span>
                                      </div>
                                    </div>
                                    <button className="p-2">
                                      <Eye className="w-5 h-5 text-gray-400" />
                                    </button>
                                  </div>
                                ))}
                              </div>
                            </div>

                            <div className="mt-6">
                              <h3 className="font-medium text-gray-600 mb-4">Party Submissions</h3>
                              <div className="grid grid-cols-2 gap-4">
                                <div className="bg-blue-50 p-4 rounded-lg">
                                  <div className="flex items-center gap-2 mb-3">
                                    <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                                      <FileText className="w-4 h-4 text-blue-600" />
                                    </div>
                                    <div>
                                      <div className="font-medium">Claimant Memorial</div>
                                      <div className="text-blue-600 text-sm">¶145-148</div>
                                    </div>
                                  </div>
                                  <p className="text-sm text-gray-600">
                                    The contract was signed after a competitive bidding process where the Claimant's bid was found to be the most technically and financially advantageous.
                                  </p>
                                </div>

                                <div className="bg-red-50 p-4 rounded-lg">
                                  <div className="flex items-center gap-2 mb-3">
                                    <div className="w-8 h-8 bg-red-100 rounded-full flex items-center justify-center">
                                      <FileText className="w-4 h-4 text-red-600" />
                                    </div>
                                    <div>
                                      <div className="font-medium">Respondent Counter-Memorial</div>
                                      <div className="text-red-600 text-sm">¶203-205</div>
                                    </div>
                                  </div>
                                  <p className="text-sm text-gray-600">
                                    While the contract was indeed signed on the stated date, the Respondent maintains that the Claimant failed to properly mobilize within the timeframe.
                                  </p>
                                </div>
                              </div>
                            </div>
                          </>
                        )}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ModernLegalInterface;
