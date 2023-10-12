import React, { useState } from 'react';

/** SearchForm
 *
 * State
 * -formData
 *
 * Props
 * -searchPhoto
 */
function SearchForm({ searchPhoto }) {
  const [formData, setFormData] = useState("");

  async function handleSubmit(evt) {
    evt.preventDefault();
    try {
      await searchPhoto(formData);
      setFormData("");
    } catch (err) {
      console.log(err, "err in search form");
    }
  }

  function handleChange(evt) {
    const { value } = evt.target;
    setFormData(value);
  }

  return (
    <form className="SearchForm" onSubmit={handleSubmit}>
      <label htmlFor="search-bar" className="SearchForm-label"></label>
      <input
        id="search-bar"
        name="searchTerm"
        value={formData}
        type="text"
        placeholder="Search..."
        className="SearchForm-input"
        onChange={handleChange}>
      </input>
      <button type="submit" className="SearchForm-button">Search</button>
    </form>
  );

}

export default SearchForm;