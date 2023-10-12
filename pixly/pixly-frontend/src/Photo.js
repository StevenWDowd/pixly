import { Link } from "react-router-dom";
import "./Photo.css";

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