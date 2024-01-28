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
</template>

<script>
// import api from "@/api";
import axios from "axios";

export default {
  data() {
    return {
      //   categories: [],
      //   posts: [],
      Onbording: [],
    };
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
};
</script>
