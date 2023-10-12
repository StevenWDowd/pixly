import { useState } from "react";

/** Renders a form to upload a photo
 *
 * Props:
 * -uploadPhoto
 *
 */
function AddPhotoForm({ uploadPhoto }) {
  const [formData, setFormData] = useState({user_photo: ""});

  function handleChange(evt) {
    const { value, name } = evt.target;
    setFormData(f => ({
      ...f,
      [name]: value,
    }));
  }

  async function handleSubmit(evt) {
    evt.preventDefault();
    try {
      const { value } = evt.target;
      console.log("formData is ", formData);
      await uploadPhoto(formData);
    } catch (err) {
      console.log(err, "error caught in AddPhotoForm");
    }
  }
  return (
    <form className="AddPhotoForm" onSubmit={handleSubmit}>
      <label htmlFor="photo"></label>
      <input id="photo" name="user_photo" type="file" accept=".jpg" value={formData.user_photo} onChange={handleChange}></input>
      <button className="AddPhotoForm-submit-btn">Submit Photo</button>
    </form>
  );
}

export default AddPhotoForm;