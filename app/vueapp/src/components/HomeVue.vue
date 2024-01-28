// در فایل مربوط به Component مورد نظر (مثلاً Home.vue)
<template>
  <div>
    <h1>Categories</h1>
    <ul>
      <li v-for="category in categories" :key="category.id">
        {{ category.name }}
      </li>
    </ul>

    <h1>Posts</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">{{ post.title }}</li>
    </ul>
  </div>
</template>

<script>
import api from "@/api";
import axios from "axios";

export default {
  data() {
    return {
      categories: [],
      posts: [],
    };
  },
  mounted() {
    // در هنگام لود شدن Component، داده‌ها را از API درخواست کنید
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.all([api.getCategories(), api.getPosts()]);
        this.categories = response[0].data;
        this.posts = response[1].data;
      } catch (error) {
        console.log(error);
      } finally {
        console.log("Done");
      }
    },
  },
};
</script>
