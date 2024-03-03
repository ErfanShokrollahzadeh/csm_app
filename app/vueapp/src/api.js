// src/api.js
import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000/api/", // Address API Django
  headers: {
    "Content-Type": "application/json",
  },
});

export default {
  getOnbording() {
    return apiClient.get("onbording/");
  },
  getPosts() {
    return apiClient.get("posts/");
  },
  getCategories() {
    return apiClient.get("categories/");
  },
  getCountry() {
    return apiClient.get("select-country/");
  },
};
