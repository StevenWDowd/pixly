/** Renders a form to upload a photo
 *
 * Props:
 * -uploadPhoto
 *
 */
function AddPhotoForm({ uploadPhoto }) {

  function handleSubmit(evt) {
    evt.preventDefault();
    try {
      const { value } = evt.target;
      uploadPhoto(value);
    } catch (err) {
      console.log(err, "error caught in AddPhotoForm");
    }
  }
  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="photo"></label>
      <input id="photo" name="user_photo" type="file" accept=".jpg"></input>
    </form>
  );
}

export default AddPhotoForm;