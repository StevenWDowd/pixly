import React, { useState } from 'react';

/** SearchForm
 *
 * State
 * -formData: a string
 *
 * Props
 * -searchPhoto: function from parent
 *
 * App -> RoutesList -> PhotoList -> SearchForm
 */
function SearchForm({ searchPhoto }) {
  const [formData, setFormData] = useState("");

  //Called to handle form submission.
  async function handleSubmit(evt) {
    evt.preventDefault();
    try {
      await searchPhoto(formData);
      setFormData("");
    } catch (err) {
      console.log(err, "err in search form");
      alert("Sorry, we couldn't complete your search.");
    }
  }

  //Keeps track of form input values
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