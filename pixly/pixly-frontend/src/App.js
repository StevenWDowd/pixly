import React, { useState, useEffect } from 'react';
import './App.css';
import AddPhotoForm from './AddPhotoForm';
import PixlyApi from './pixlyApi';

/** App
 *
 * State:
 * -photoList
 *
 * App -> AddPhotoForm
 */
function App() {
  const [photoList, setPhotoList] = useState([]);

  async function uploadPhoto(formData) {
    const img = formData
    const resp = await PixlyApi.uploadImage(img);
    console.log(resp, "response")
    const newPhoto = await resp.json() //{obj of photo info} or {message: photo failed to upload}
    setPhotoList([...photoList, newPhoto])
  }

  return (
    <div className="App">
      <AddPhotoForm uploadPhoto={uploadPhoto} />
    </div>
  );
}

export default App;
