import { Route, Routes, Navigate } from "react-router-dom";
import PhotoDetail from "./PhotoDetail";
import PhotoList from "./PhotoList";
import AddPhotoForm from "./AddPhotoForm";

function RoutesList({uploadPhoto, photoList}){
  return (
    <Routes>
      <Route path="/photos" element={<PhotoList photos={photoList}/>} />
      <Route path="/photos/:id" element={<PhotoDetail />} />
      <Route path="/add" element={<AddPhotoForm uploadPhoto={uploadPhoto} />} />
      <Route path="*" element={<Navigate to={"/photos"}/>}/>
    </Routes>
  )

}

export default RoutesList