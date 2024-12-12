// src/components/Navbar.js
import React from 'react';
import { useTheme } from '../context/ThemeContext';

const Navbar = () => {
  const { isDarkMode, toggleTheme } = useTheme();

  return (
    <nav className={`navbar ${isDarkMode ? 'dark' : 'light'}`}>
      <h2>CryptoLedger</h2>
      <button onClick={toggleTheme}>
        {isDarkMode ? 'Light Mode' : 'Dark Mode'}
      </button>
    </nav>
  );
};

export default Navbar;
