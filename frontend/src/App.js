// frontend/src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://localhost:8000/query', { input: query });
    setResponse(res.data.answer);
  };

  return (
    <div className="App">
      <h1 className='Title'>Swoop Advisor</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Ask Swoop about a professor "
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{ width: '60%', padding: '0.5rem', fontSize: '1rem' }}
        />
        <button type="submit" style={{ padding: '0.5rem 1rem' }}>Send</button>
      </form>
      <div style={{ marginTop: '2rem' }}>
        <strong>Swoop Advisor: by DSK</strong>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;
