<template>
  <div class="container">
    <div class="back">
      <a href="/" class="routback">Back</a>
      <h1>Topics</h1>
    </div>
    <div class="search-container">
      <input
        type="text"
        v-model="searchText"
        placeholder="Search for topics..."
        class="search"
      />
    </div>
    <div class="topics">
      <div v-for="topic in filteredTopics" :key="topic.id" class="topic">
        <h2>{{ topic.name }}</h2>
        <p>{{ topic.description }}</p>
      </div>
    </div>
    <button class="btn btn-primary" @click="goto">Submit</button>
  </div>
</template>

<script>
import api from "@/api";

export default {
  data() {
    return {
      topics: [],
      searchText: "",
    };
  },
  async created() {
    try {
      const response = await api.getTopics();
      this.topics = response.data;
    } catch (error) {
      console.error("Error fetching topics:", error);
    }
  },
  computed: {
    filteredTopics() {
      return this.topics.filter((topic) => {
        return (
          topic.name &&
          topic.name.toLowerCase().startsWith(this.searchText.toLowerCase())
        );
      });
    },
  },
  methods: {
    goto() {
      this.$router.push("/signup");
    },
  },
};
</script>
