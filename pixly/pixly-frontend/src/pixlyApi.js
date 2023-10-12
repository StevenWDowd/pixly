const BASE_URL = "http://localhost:5001";

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
    const formData = new FormData();
    formData.append('user_photo', photo);
    const res = await fetch(`${BASE_URL}/add`, {
      method: "POST",
      body: formData,
    });

    if (res.status === 400) {
      console.log("bad request");
    }
    return res;
  }

}

export default PixlyApi;