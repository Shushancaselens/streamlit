import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { useEffect, useState } from "react"

const SearchBox = () => {
  const [searchTerm, setSearchTerm] = useState("")

  const handleSearch = (value) => {
    setSearchTerm(value)
    Streamlit.setComponentValue(value)
  }

  return (
    <div className="search-wrapper">
      <div className="search-container">
        <svg
          className="search-icon"
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => handleSearch(e.target.value)}
          placeholder="Search issues, arguments, or evidence..."
          className="search-input"
        />
      </div>
      <style jsx>{`
        .search-wrapper {
          max-width: 100%;
          padding: 0 1rem;
          margin-top: 1rem;
          margin-bottom: 1.5rem;
        }
        .search-container {
          position: relative;
          display: flex;
          align-items: center;
          background: white;
          border: 1px solid #e5e7eb;
          border-radius: 0.75rem;
          transition: all 0.2s;
        }
        .search-container:focus-within {
          border-color: #6366f1;
          box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
        }
        .search-icon {
          position: absolute;
          left: 1rem;
          color: #9ca3af;
          pointer-events: none;
        }
        .search-input {
          width: 100%;
          padding: 0.75rem 1rem 0.75rem 3rem;
          border: none;
          border-radius: 0.75rem;
          font-size: 0.875rem;
          color: #1f2937;
          outline: none;
        }
        .search-input::placeholder {
          color: #9ca3af;
        }
      `}</style>
    </div>
  )
}

export default withStreamlitConnection(SearchBox)
