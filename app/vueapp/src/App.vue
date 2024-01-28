<!-- در فایل App.vue -->
<template>
  <div id="app">
    <CategoriesList :categories="categories" />
    <PostsList :posts="posts" />
  </div>
</template>

<script>
import CategoriesList from "@/components/CategoriesList.vue";
import PostsList from "@/components/PostsList.vue";
import api from "@/api";

export default {
  data() {
    return {
      categories: [],
      posts: [],
    };
  },
  mounted() {
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
  components: {
    CategoriesList,
    PostsList,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h2 {
  color: #35424a;
}
</style>
