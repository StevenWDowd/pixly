const BASE_URL = "http://localhost:5001"

/** API class
 *
 * static class with methods used to get/send to the python/flask API.
 *
 */

class PixlyApi {

  static async getImage() {

  }
  static async getAllImages() {

  }

  static async uploadImage(photo) {
    let res = await fetch(`${BASE_URL}/add`, {
      method: "POST",
      body: { 'user_photo': photo },
      headers: { 'content-type': "multipart/form-data" }
    });
    return res;
  }

}