import Photo from "./Photo";

function PhotoList({photos}){
  return (
    <div className="PhotoList">
      <ul className="PhotoList-ul">
        {photos.map(p => <li key={p.id}><Photo photo={p}/></li>)}
      </ul>

    </div>
  )
}

export default PhotoList;