<!-- Home.vue -->
<template>
  <div>
    <h1>Home Page</h1>
    <div v-if="dataLoading">Loading...</div>
    <ul v-else>
      <li v-for="item in data" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      data: null,
      dataLoading: true,
    };
  },
  mounted() {
    // Fetch data from the Django backend
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get("http://your-django-api-endpoint");
        this.data = response.data;
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        this.dataLoading = false;
      }
    },
  },
};
</script>
