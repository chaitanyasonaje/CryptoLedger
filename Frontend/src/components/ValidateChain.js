import React, { useState } from 'react';

const ValidateChain = () => {
  const [isValid, setIsValid] = useState(null);
  const [message, setMessage] = useState('');

  const validateChain = () => {
    fetch('http://127.0.0.1:5000/is_chain_valid')
      .then(response => response.json())
      .then(data => {
        setIsValid(data.is_valid);
        setMessage(data.message);
      })
      .catch(error => console.error('Error validating chain:', error));
  };

  return (
    <div>
      <button onClick={validateChain}>Validate Blockchain</button>
      {isValid !== null && (
        <div>
          <p>{message}</p>
        </div>
      )}
    </div>
  );
};

export default ValidateChain;  // Make sure this is the default export
