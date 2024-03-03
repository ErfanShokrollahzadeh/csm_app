<template>
  <div class="back">
    <router-link to="/forgotpass1" class="routback">⬅</router-link>
  </div>
  <div class="title_pass">
    <h1>OTP Verification</h1>
    <p>Enter the OTP sent to +67-1234-5678-9</p>
  </div>

  <div v-for="country in countries" :key="country.id">
    <div>
      {{ country.title }}
      <img :src="country.image" class="d-block w-100" alt="Country image" />
    </div>
  </div>
</template>

<script>
import api from "@/api";

export default {
  data() {
    return {
      countries: [],
    };
  },
  async created() {
    try {
      const response = await api.getCountry();
      this.items = response.data;
    } catch (error) {
      console.error(error);
    }
  },
  computed: {
    filteredCountries() {
      return this.countries.filter((country) => {
        return country.name
          .toLowerCase()
          .includes(this.searchText.toLowerCase());
      });
    },
  },
};
</script>

<style scoped>
.back {
  margin-top: 20px;
  margin-left: 20px;
  font-size: 20px;
}
.routback {
  text-decoration: none;
  color: #4e4b66;
}
.title_pass {
  margin-top: 30px;
  padding: 11px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
