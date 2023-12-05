import React, { useState } from 'react';
import '../styles/Form.css'

interface FormProps {
  onSubmit: (formData: { field1: string; field2: number }) => void;
}

const FormComponent: React.FC<FormProps> = ({ onSubmit }) => {
  const [selectedOption, setSelectedOption] = useState<string>('');
  const [numberInput, setNumberInput] = useState<number | ''>('');

  const handleOptionChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedOption(event.target.value);
  };

  const handleNumberChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value;
    // Check if the input is a number or empty string
    if (!isNaN(Number(value)) || value === '') {
      setNumberInput(value === '' ? '' : Number(value));
    }
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const numberFieldValue = typeof numberInput === 'string' ? parseInt(numberInput) : numberInput;

    if (numberFieldValue > 24) {
        onSubmit({ field1: selectedOption, field2: numberFieldValue });
    } else {
        console.log('Number must be greater than 24');
    }
  };

  return (
    <form onSubmit={handleSubmit} className='form-wrapper'>
      <h1>Enter data you want to analyse</h1>
      <div className='sector-input-wrapper'>
        <label htmlFor="dropdown">Choose a sector to analyse:</label>
        <select id="dropdown" value={selectedOption} onChange={handleOptionChange}>
          <option value="">Select an option</option>
          <option value="software development">Software Development</option>
          <option value="data science">Data Science</option>
          <option value="software engineering">Software Engineering</option>
          <option value="software engineering">Web Development</option>
        </select>
      </div>
      <div className='number-input-wrapper'>
        <label htmlFor="numberInput">Enter number of job posts you want to analyse:</label>
        <input
          type="number"
          id="numberInput"
          value={numberInput}
          onChange={handleNumberChange}
        />
      </div>
      <button type="submit" id='submit-button'>Submit</button>
    </form>
  );
};

export default FormComponent;