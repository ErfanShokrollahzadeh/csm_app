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
    fetchData() {
      api.getCategories().then((response) => {
        this.categories = response.data;
      });

      api.getPosts().then((response) => {
        this.posts = response.data;
      });
    },
  },
};
</script>
