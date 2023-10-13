import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import PixlyApi from "./pixlyApi";
import "./PhotoDetail.css";

/** PhotoDetail function: renders a component for viewing a single photo
 *  -Props: none
 *  -state:
 *    isLoading: boolean
 *    image: an image object like {id, url, s3_key, image_description,
 *                                  camera_make, camera_model, date, gps_info}
 *            note: only id, s3_key, and url are mandatory.
 *
 * App -> RoutesList -> PhotoDetail
 */
function PhotoDetail() {
  const initialData = {
    id: -1,
    url: "",
    camera_make: "",
    camera_model: "",
    image_description: "",
    gps_info: null,
  };

  const [image, setImage] = useState({photo: initialData, isLoading: true})
  const { id } = useParams();

  useEffect(function getPhoto() {
    async function fetchPhoto() {
      const photo = await PixlyApi.getImage(id);
      setImage({photo: photo, isLoading: false});
    }
    fetchPhoto();
  }, []);

  //Called on clicking of button to change to black and white.
  function handleBWButtonClick(){
    setImage({photo: image.photo, isLoading: true});
    grayScale();
  }

  //Called on clicking of button to change photo to color.
  function handleColorButtonClick(){
    setImage({photo: image.photo, isLoading: true});
    colorize();
  }

  //Handles function to change photo to grayscale.
  async function grayScale(){
    const newImage = await PixlyApi.grayscaleImage(id);
    setImage({photo: newImage, isLoading:false});


  }

  //Handles function to change photo to color.
  async function colorize(){
    const newImage = await PixlyApi.colorizeImage(id);
    setImage({photo: newImage, isLoading:false});

  }

  return (
    image.isLoading ?
    <p>Loading ...</p>
    :
    <div className="PhotoDetail">
      <img className="PhotoDetail-img" src={image.photo.url}></img>
      <div className="PhotoDetail-container"><h3>Image information:</h3>
        <p className="PhotoDetail-info">
          Image Description: {image.photo.image_description}
        </p>
        <p className="PhotoDetail-info">Camera Make: {image.photo.camera_make}</p>
        <p className="PhotoDetail-info">Camera Model: {image.photo.camera_model}</p>
        <p className="PhotoDetail-info">Date Taken: {image.photo.date}</p>
      </div>
      <button className="PhotoDetail-bw-btn"
              onClick={handleBWButtonClick}>
              Change to Black and White
      </button>
      <button className="PhotoDetail-color-btn"
              onClick={handleColorButtonClick}>
              Change to Color
      </button>
    </div>
  );
}

export default PhotoDetail;