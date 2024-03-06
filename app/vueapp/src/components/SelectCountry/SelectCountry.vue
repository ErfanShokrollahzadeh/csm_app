<template>
  <div class="back">
    <router-link to="/signup" class="routback">⬅</router-link>
    <h3>Select your Country</h3>
  </div>
  <div class="searchbar">
    <input type="text" placeholder="Search" class="w" v-model="searchText" />
    <i class="search-icon fas fa-search"></i>
  </div>

  <ul class="country-list">
    <li v-for="country in countries" :key="country.id" class="data">
      <img :src="country.image" class="d-block" alt="Country image" />
      {{ country.title }}
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
      countries: [],
      searchText: "",
    };
  },
  async created() {
    try {
      const response = await api.getCountry();
      this.countries = response.data;
    } catch (error) {
      console.error("Error fetching countries:", error);
    }
  },
  computed: {
    filteredCountries() {
      return this.countries.filter((country) => {
        return (
          country.name &&
          country.name.toLowerCase().startsWith(this.searchText.toLowerCase())
        );
      });
    },
  },
  methods: {
    goto() {
      this.$router.push("/topics");
    },
  },
};
</script>

<style scoped>
.back {
  display: flex;
  justify-content: space-evenly;
  align-items: flex-start;
  font-size: 20px;
  margin-top: 30px;
  margin-left: -10px;
  margin-right: 30px;
}
.routback {
  text-decoration: none;
  color: #4e4b66;
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

.data {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 5px;
  flex-direction: row;
  margin-right: 160px;
  cursor: pointer;
}
.data:hover {
  background-color: #1877f2;
  color: white;
}
img {
  width: 45px;
  height: 45px;
}
h3 {
  font-weight: 700;
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
    margin-top: 10rem;
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
</style>
