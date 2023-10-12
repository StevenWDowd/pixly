import React, { useState, useEffect } from 'react';
import './App.css';
import AddPhotoForm from './AddPhotoForm';
import PixlyApi from './pixlyApi';
import { BrowserRouter, Navigate } from "react-router-dom";
import RoutesList from './RoutesList';
import NavBar from './NavBar';

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
        setPhotoList(allPhotos);
      } catch (err) {
        setPhotoList([]);
      }
    }
    fetchPhotos();
  }, []);

  async function uploadPhoto(formData) {
    const img = formData;
    const response = await PixlyApi.uploadImage(img);
    const newPhoto = await response.json(); //{obj of photo info} or {message: photo failed to upload}
    setPhotoList([...photoList, newPhoto]);
  }

  async function searchPhoto(formData) {
    const photos = await PixlyApi.getSearchedImages(formData);
    setPhotoList(photos);
  }

  return (
    <div className="App">
      <BrowserRouter>
        <NavBar />
        <RoutesList
          uploadPhoto={uploadPhoto}
          photoList={photoList}
          searchPhoto={searchPhoto} />
      </BrowserRouter>
    </div>
  );
}

export default App;
