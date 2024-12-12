// src/components/ViewChain.js
import React, { useState, useEffect } from 'react';
import { useTheme } from '../context/ThemeContext';

const ViewChain = () => {
  const [chain, setChain] = useState([]);
  const { isDarkMode } = useTheme();

  useEffect(() => {
    fetch('http://127.0.0.1:5000/get_chain')
      .then(response => response.json())
      .then(data => setChain(data.chain))
      .catch(error => console.error('Error fetching chain:', error));
  }, []);

  return (
    <div>
      <h2>Blockchain</h2>
      <div>
        {chain.map((block, index) => (
          <div className={`card ${isDarkMode ? 'dark' : 'light'}`} key={index}>
            <strong>Block {block.index}</strong>
            <p>Data: {block.data}</p>
            <p>Hash: {block.hash}</p>
            <p>Previous Hash: {block.previous_hash}</p>
            <p>Timestamp: {block.timestamp}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ViewChain;
