import React from 'react';
import AddBlock from './components/AddBlock';  // Correct path for AddBlock component
import ViewChain from './components/ViewChain';  // Correct path for ViewChain component
import ValidateChain from './components/ValidateChain';  // Correct path for ValidateChain component
import Navbar from './components/Navbar';  // Assuming you have a Navbar component
import { ThemeProvider } from './context/ThemeContext';  // Assuming ThemeContext for dark/light mode
import './App.css';  // Your main styles file

function App() {
  return (
    <ThemeProvider>
      <div className="App">
        <Navbar />  {/* Navbar with dark/light mode toggle */}
    

        {/* Add block form */}
        <AddBlock />

        {/* View Blockchain */}
        <ViewChain />

        {/* Validate Blockchain */}
        <ValidateChain />

        <footer>
          <p>Created by Chaitanya Sonaje</p>
          <p>2024 CryptoLedger. All rights reserved.</p>
        </footer>
      </div>
    </ThemeProvider>
  );
}

export default App;
