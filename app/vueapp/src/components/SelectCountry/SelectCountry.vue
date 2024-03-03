<template>
  <div>
    <input type="text" v-model="searchText" placeholder="Search country" />
    <ul>
      <li v-for="country in filteredCountries" :key="country.id">
        {{ country.name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchText: "",
      countries: [
        { id: 1, name: "India" },
        { id: 2, name: "USA" },
        { id: 3, name: "UK" },
        { id: 4, name: "Australia" },
        { id: 5, name: "Canada" },
        { id: 6, name: "Germany" },
        { id: 7, name: "France" },
        { id: 8, name: "Italy" },
        { id: 9, name: "Japan" },
        { id: 10, name: "China" },
      ],
    };
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
