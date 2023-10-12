import React, { useState, useEffect } from 'react';
import './App.css';
import AddPhotoForm from './AddPhotoForm';
import PixlyApi from './pixlyApi';
<<<<<<< Updated upstream
import { BrowserRouter, Navigate } from "react-router-dom";
import RoutesList from './RoutesList';
=======
import NavBar from './NavBar';
>>>>>>> Stashed changes

/** App
 *
 * State:
 * -photoList
 *
 * App -> AddPhotoForm
 */
function App() {
  const [photoList, setPhotoList] = useState([]);

  useEffect(function getPhotos() {
    async function fetchPhotos() {
      try {
        const allPhotos = await PixlyApi.getAllImages();
        setPhotoList(allPhotos)
      } catch (err) {
        console.log("error fetching photos");
        setPhotoList([]);
      }
    }
    fetchPhotos();
  }, []);

  async function uploadPhoto(formData) {
    const img = formData
    const resp = await PixlyApi.uploadImage(img);
    console.log(resp, "response")
    const newPhoto = await resp.json() //{obj of photo info} or {message: photo failed to upload}
    setPhotoList([...photoList, newPhoto])
  }

  return (
    <div className="App">
<<<<<<< Updated upstream
      <BrowserRouter>
        <RoutesList uploadPhoto={uploadPhoto} photoList={photoList}/>
        {/* <AddPhotoForm uploadPhoto={uploadPhoto} /> */}
      </BrowserRouter>
=======
      <NavBar />
      <AddPhotoForm uploadPhoto={uploadPhoto} />
>>>>>>> Stashed changes
    </div>
  );
}

export default App;
