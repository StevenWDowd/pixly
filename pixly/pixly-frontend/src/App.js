import React, { useState, useEffect } from 'react';
import './App.css';
import AddPhotoForm from './AddPhotoForm';
import uploadImage from './pixlyApi';

/** App
 *
 * State:
 * -photoList
 *
 * App -> AddPhotoForm
 */
function App() {
  const [photoList, setPhotoList] = useState([]);

  async function uploadPhoto(img) {
    const resp = await PixlyApi.uploadImage(img);
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
