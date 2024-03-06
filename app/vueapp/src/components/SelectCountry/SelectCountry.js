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
