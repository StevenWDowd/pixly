import Photo from "./Photo";
import "./PhotoList.css";
import SearchForm from "./SearchForm";

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