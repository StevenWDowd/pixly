import React, { useState, useEffect } from 'react';
import './App.css';
import PixlyApi from './pixlyApi';
import { BrowserRouter } from "react-router-dom";
import RoutesList from './RoutesList';
import NavBar from './NavBar';

/** App
 *
 * Props: none
 * State:
 * -photoList: array of photo objects like:{id, url, s3_key, image_description,
 *                                  camera_make, camera_model, date, gps_info}
 *            note: only id, s3_key, and url are mandatory.
 * -isLoading: boolean
 *
 * App -> {NavBar, RoutesList}
 */
function App() {
  const [photoList, setPhotoList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);


  useEffect(function getPhotos() {
    async function fetchPhotos() {
      try {
        const allPhotos = await PixlyApi.getAllImages();
        setPhotoList(allPhotos);
        setIsLoading(false);
      } catch (err) {
        setPhotoList([]);
        setIsLoading(false);
      }
    }
    fetchPhotos();
  }, []);

  //Handles photo uploading from AddPhotoForm
  async function uploadPhoto(formData) {
    const img = formData;
    const response = await PixlyApi.uploadImage(img);
    const newPhoto = await response.json();
    setPhotoList([...photoList, newPhoto]);
  }

  //Handles searching of photos with scraped EXIF data
  async function searchPhoto(formData) {
    if (formData) {
      const photos = await PixlyApi.getSearchedImages(formData);
      setPhotoList(photos);
    } else {
      const photos = await PixlyApi.getAllImages();
      setPhotoList(photos);
    }
  }

  return (
    isLoading ?
      <p>Loading ...</p>
      :
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
