import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import PixlyApi from "./pixlyApi";
import "./PhotoDetail.css";

function PhotoDetail() {
  const initialData = {
    id: -1,
    url: "",
    camera_make: "",
    camera_model: "",
    image_description: "",
    gps_info: null,
  };
  const [image, setImage] = useState(initialData);
  const { id } = useParams();

  useEffect(function getPhoto() {
    async function fetchPhoto() {
      const photo = await PixlyApi.getImage(id);
      setImage(photo);
    }
    fetchPhoto();
  }, []);
  //TODO: add buttons for border/color change?

  return (
    <div className="PhotoDetail">
      <img className="PhotoDetail-img" src={image.url}></img>
      <div className="PhotoDetail-container"><h3>Image information:</h3>
        <p className="PhotoDetail-info">{image.image_description}</p>
        <p className="PhotoDetail-info">{image.camera_make}</p>
        <p className="PhotoDetail-info">{image.camera_model}</p>
      </div>
    </div>
  );


  // <p>{Photo.image_description}</p>


}

export default PhotoDetail;