import React, { useState } from 'react';

const AddBlock = () => {
  const [blockData, setBlockData] = useState('');
  const [message, setMessage] = useState('');

  // Handle input change
  const handleInputChange = (e) => {
    setBlockData(e.target.value);
  };

  // Handle form submission
  const handleAddBlock = async (e) => {
    e.preventDefault();

    if (!blockData) {
      setMessage("Data for the block is missing.");
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/add_block', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: blockData })
      });

      const data = await response.json();
      if (response.ok) {
        setMessage(`Block added successfully! Block index: ${data.new_block.index}`);
      } else {
        setMessage(data.message || 'An error occurred.');
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('Error adding block.');
    }
  };

  return (
    <div>
      <h2>Add a New Block</h2>
      <form onSubmit={handleAddBlock}>
        <input
          type="text"
          placeholder="Enter data for the block"
          value={blockData}
          onChange={handleInputChange}
        />
        <button type="submit">Add Block</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default AddBlock;
