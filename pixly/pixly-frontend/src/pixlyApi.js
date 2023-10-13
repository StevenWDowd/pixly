const BASE_URL = "http://localhost:5001";

/** API class
 *
 * static class with methods used to get/send to the python/flask API.
 *
 *  image objects look like: {id, url, s3_key, image_description,
 *                                  camera_make, camera_model, date, gps_info}
 *            note: only id, s3_key, and url are mandatory.
 *
 */

class PixlyApi {

  // gets one image based on an id integer
  static async getImage(id) {
    const res = await fetch(`${BASE_URL}/photos/${id}`);
    const photo = await res.json();
    return photo;

  }

  //Gets all images from the database
  static async getAllImages() {
    const res = await fetch(`${BASE_URL}/photos`);
    const photos = await res.json();
    return photos;

  }

  //Uploads a .jpg image file to the back end.
  static async uploadImage(photo) {
    const formData = new FormData();
    formData.append('user_photo', photo);
    const res = await fetch(`${BASE_URL}/photos/add`, {
      method: 'POST',
      body: formData,
    });

    if (res.status === 400) {
      console.log("bad request");
    }
    return res;
  }

  //Returns a list of image objects based on a search string.
  static async getSearchedImages(searchTerm) {
    const data = JSON.stringify({ 'search_term': searchTerm });
    const res = await fetch(`${BASE_URL}/photos/search`, {
      method: 'POST',
      body: data,
      headers: { 'Content-Type': 'application/json' }
    });
    const photos = await res.json();
    return photos;
  }

  //Transforms an image into a grayscale version on the back end.
  //NOTE: not currently reversible.
  static async grayscaleImage(id){
    const data = JSON.stringify({command: "blackwhite"});
    const res = await fetch (`${BASE_URL}/photos/${id}`, {
      method: 'POST',
      body: data,
      headers: { 'Content-Type': 'application/json' }
    });

    const photo = await res.json();
    return photo;
  }

  //Transforms an image into a color version on the back end.
  //NOTE: not currently working.
  static async colorizeImage(id){
    const data = JSON.stringify({command: "colorize"});
    const res = await fetch (`${BASE_URL}/photos/${id}`, {
      method: 'POST',
      body: data,
      headers: { 'Content-Type': 'application/json' }
    });

    const photo = await res.json();
    return photo;
  }

}

export default PixlyApi;