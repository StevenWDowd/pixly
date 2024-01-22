import { Link } from "react-router-dom";
import "./Photo.css";

/** Renders a photo on the list of all photos
 *
 *  Props: a photo object: {id, url, s3_key, image_description,
 *                                  camera_make, camera_model, date, gps_info}
 *            note: only id, s3_key, and url are mandatory.
 *  State: none
 *
 *  App -> RoutesList -> PhotoList -> Photo
 */
function Photo({photo}){
  return (
    <Link to={`/photos/${photo.id}`}>
    <div className="Photo">
      <img className="Photo-img" src={photo.url}></img>
    </div>
    </Link>
  )
}

export default Photo;