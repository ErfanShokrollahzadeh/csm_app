<template>
  <div class="back">
    <router-link to="/topics" class="routback">⬅</router-link>
    <h3>Choose your News Sources</h3>
  </div>

  <div class="searchbar">
    <input type="text" placeholder="Search" class="w" v-model="searchText" />
    <i class="search-icon fas fa-search"></i>
  </div>

  <ul class="news-list">
    <li v-for="news in filteredNews" :key="news.id" class="news">
      <img :src="news.image" class="d-block" alt="news image" />
      {{ news.name }}
    </li>
  </ul>

  <div class="button-container">
    <button type="button" class="btn btn-primary btnforgot" @click="goto">
      Next
    </button>
  </div>
</template>

<script>
import api from "@/api";

export default {
  data() {
    return {
      news: [],
      searchText: "",
    };
  },
  async created() {
    try {
      const response = await api.getNews();
      this.news = response.data;
    } catch (error) {
      console.error("Error fetching news:", error);
    }
  },
  computed: {
    filteredNews() {
      return this.news.filter((news) => {
        return (
          news.name &&
          news.name.toLowerCase().startsWith(this.searchText.toLowerCase())
        );
      });
    },
  },
  methods: {
    goto() {
      this.$router.push("/newssource");
    },
  },
};
</script>

<style scoped>
.search-container {
  margin-bottom: 20px;
}

.search {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.back {
  display: flex;
  justify-content: space-evenly;
  align-items: flex-start;
  font-size: 20px;
  margin-top: 30px;
  margin-right: 45px;
}
.routback {
  text-decoration: none;
  color: #4e4b66;
  margin-right: 10px;
}

.search-container {
  position: relative;
}

.search-icon {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  color: #4e4b66;
}
.searchbar {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 10px;
}
.w {
  width: 85%;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid #4e4b66;
  outline: none;
  font-size: 16px;
  color: #4e4b66;
}
.button-container {
  display: flex;
  justify-content: center;
}
@media (max-width: 992px) {
  .button-container {
    margin-top: 17rem;
  }
}

/* For mobile phones */
@media (max-width: 380px) {
  .button-container {
    margin-top: 0rem;
  }
}
@media (max-width: 320px) {
  .button-container {
    margin-top: 0rem;
  }
}
.btnforgot {
  width: 90%;
  height: 45px;
  font-weight: 700;
}
img {
  width: 70px;
  height: 70px;
  border-radius: 50%;
}
.news-list {
  list-style: none;
  margin: 20px 10px 0px -15px;
  display: flex;
  justify-content: space-around;
}
.news {
  display: flex;
  margin-bottom: 10px;
  flex-direction: column;
  align-items: center;
}
</style>
