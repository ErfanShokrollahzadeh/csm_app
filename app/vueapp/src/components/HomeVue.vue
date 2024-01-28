<template>
  <div>
    <!-- <h1>Posts</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <img />{{ post.image }}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
        <p>{{ post.category }}</p>
        <p>{{ post.user }}</p>
      </li>
    </ul>
    <p v-if="error" class="error">{{ error }}</p> -->

    <h1>Onbording</h1>
    <ul>
      <li v-for="item in Onbording" :key="item.id">
        <h2>{{ item.title }}</h2>
        <p>{{ item.discriptions }}</p>
        <img />{{ item.image }}
      </li>
    </ul>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
  <div class="navigation">
    <!-- Dots -->
    <div class="dots">
      <span
        v-for="(item, index) in [0, 1, 2]"
        :key="index"
        :class="{ active: currentSlide === index }"
      ></span>
    </div>

    <!-- Next button -->
    <button @click="next">Next</button>
  </div>
</template>

<script>
// import api from "@/api";
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  data() {
    return {
      //   categories: [],
      //   posts: [],
      Onbording: [],
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  async created() {
    try {
      //   const responsePosts = await axios.get("http://127.0.0.1:8000/api/posts/");
      //   this.posts = responsePosts.data;

      const responseOnbording = await axios.get(
        "http://127.0.0.1:8000/api/Onbording/"
      );
      this.Onbording = responseOnbording.data;

      //   const responseCategories = await axios.get(
      //     "http://127.0.0.1:8000/api/categories/"
      //   );
      //   this.categories = responseCategories.data;
    } catch (error) {
      this.error =
        "There was an error fetching the data. Please try again later.";
      console.error(error);
    }
  },
  async next() {
    if (this.currentSlide < 2) {
      // If it's not the last slide, go to the next slide
      this.currentSlide++;
    } else {
      // If it's the last slide, redirect to the login page
      this.router.push("/login");
    }
  },
};
</script>

<style scoped>
.dots {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.dots span {
  height: 10px;
  width: 10px;
  margin: 0 5px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
}

.dots span.active {
  background-color: #717171;
}
</style>
