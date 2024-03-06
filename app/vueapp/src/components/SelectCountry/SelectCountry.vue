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
import SelectCountry from "./SelectCountry.js";

export default {
  name: "SelectCountry",
  ...SelectCountry,
};
</script>

<style scoped src="./SelectCountry.css"></style>
