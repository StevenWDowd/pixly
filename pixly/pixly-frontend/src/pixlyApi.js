const BASE_URL = "http://localhost:5001";

/** API class
 *
 * static class with methods used to get/send to the python/flask API.
 *
 */

class PixlyApi {

  static async getImage(id) {
    const res = await fetch(`${BASE_URL}/photos/${id}`);
    const photo = await res.json();
    return photo;

  }
  static async getAllImages() {
    const res = await fetch(`${BASE_URL}/photos`);
    const photos = await res.json();
    return photos;

  }

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

}

export default PixlyApi;