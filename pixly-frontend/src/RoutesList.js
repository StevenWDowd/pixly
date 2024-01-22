import { Route, Routes, Navigate } from "react-router-dom";
import PhotoDetail from "./PhotoDetail";
import PhotoList from "./PhotoList";
import AddPhotoForm from "./AddPhotoForm";

/** Renders a list of Routes
 *  Props: uploadPhoto: function from parent
 *         searchPhoto: function from parent
 *         photoList: array of image objects like:
 *                    {id, url, s3_key, image_description, camera_make,
 *                      camera_model, date, gps_info}
 *            note: only id, s3_key, and url are mandatory.
 *
 * App -> RoutesList -> {PhotoList, PhotoDetail, AddPhotoForm}
 */
function RoutesList({ uploadPhoto, photoList, searchPhoto }) {
  return (
    <Routes>
      <Route
        path="/photos"
        element={<PhotoList photos={photoList} searchPhoto={searchPhoto} />}
      />
      <Route path="/photos/:id" element={<PhotoDetail />} />
      <Route path="/add" element={<AddPhotoForm uploadPhoto={uploadPhoto} />} />
      <Route path="*" element={<Navigate to={"/photos"} />} />
    </Routes>
  );

}

export default RoutesList;