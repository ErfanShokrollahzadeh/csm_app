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
    filteredcountries() {
      return this.countries.filter((countries) => {
        return (
          countries.title &&
          countries.title
            .toLowerCase()
            .startsWith(this.searchText.toLowerCase())
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
