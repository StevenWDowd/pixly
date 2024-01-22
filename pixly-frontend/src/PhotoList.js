import Photo from "./Photo";
import "./PhotoList.css";
import SearchForm from "./SearchForm";

/** Renders a component to hold and display all the photos
 *  Props:
 *    photos: a list of photo objects like: {id, url, s3_key, image_description,
 *                                  camera_make, camera_model, date, gps_info}
 *            note: only id, s3_key, and url are mandatory.
 *    searchPhoto: function from parent
 *
 *  State: none
 *
 *  App -> RoutesList -> PhotoList
 */
function PhotoList({ photos, searchPhoto }) {
  return (
    <>
      <h1 className="PhotoList-title">Pixly</h1>
      <SearchForm searchPhoto={searchPhoto} />
      <div className="PhotoList">
        {photos.map(p => <Photo key={p.id} photo={p} />)}
      </div>
    </>
  );
}

export default PhotoList;