// src/api.js
import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000/api/", // آدرس API Django
  headers: {
    "Content-Type": "application/json",
  },
});

export default {
  getCategories() {
    return apiClient.get("categories/");
  },
  getPosts() {
    return apiClient.get("posts/");
  },
};
