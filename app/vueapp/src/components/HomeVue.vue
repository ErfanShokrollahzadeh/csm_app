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
      <li v-if="Onbording.length">
        <h2>{{ Onbording[currentSlide].title }}</h2>
        <p>{{ Onbording[currentSlide].discriptions }}</p>
        <img :src="Onbording[currentSlide].image" alt="Onbording image" />
      </li>
    </ul>
    <p v-if="error" class="error">{{ error }}</p>
  </div>

  <div class="navigation">
    <!-- slide -->
    <div class="dots">
      <span
        v-for="(dot, index) in [1, 2, 3]"
        :key="index"
        :class="{ active: currentSlide === index }"
      ></span>
    </div>

    <!-- Next button -->
    <a href="#" @click.prevent="back" :class="{ disabled: currentSlide === 0 }"
      >Back</a
    >
    <button @click="next" :disabled="currentSlide === Onbording.length - 1">
      {{ nextButtonText }}
    </button>
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
      currentSlide: 0,
    };
  },
  computed: {
    nextButtonText() {
      return this.currentSlide < 2 ? "Next" : "Get Started";
    },
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  async mounted() {
    try {
      //   const responsePosts = await axios.get("http://127.0.0.1:8000/api/posts/");
      //   this.posts = responsePosts.data;

      const response = await axios.get("http://127.0.0.1:8000/api/Onbording/");
      this.Onbording = response.data;

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
  methods: {
    next() {
      if (this.currentSlide < this.Onbording.length - 1) {
        this.currentSlide++;
      }
    },
  },
};
</script>

<style scoped></style>
