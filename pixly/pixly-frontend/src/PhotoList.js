import Photo from "./Photo";
import "./PhotoList.css";

function PhotoList({ photos }) {
  return (
    <>
      <h1 className="PhotoList-title">Pixly</h1>
      <div className="PhotoList">
        {photos.map(p => <Photo key={p.id} photo={p} />)}
      </div>
    </>
  );
}

export default PhotoList;