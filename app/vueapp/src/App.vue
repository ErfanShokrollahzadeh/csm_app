<template>
  <div id="app">
    <div v-if="showLogo">
      <img src="@/assets/Vector.svg" alt="Logo" />
    </div>
    <div v-else>
      <Home />
      <router-view />
    </div>
    <!-- <CategoriesList :categories="categories" /> -->
    <!-- <PostsList :posts="posts" /> -->
  </div>
</template>

<script>
// import CategoriesList from "@/components/CategoriesList.vue";
// import PostsList from "@/components/PostsList.vue";
import Home from "@/components/HomeVue.vue";
import api from "@/api";

export default {
  data() {
    return {
      categories: [],
      posts: [],
      showLogo: true,
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
    // CategoriesList,
    // PostsList,
    Home,
  },
  created() {
    // Hide the logo after 3 seconds
    setTimeout(() => {
      this.showLogo = false;
    }, 3000);
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

img {
  max-width: 100%;
  max-height: 100%;
}
</style>
