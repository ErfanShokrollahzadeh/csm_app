import api from "@/api"; // Adjust the path according to your project structure

export default {
  data() {
    return {
      Onbording: [],
      currentSlide: 0,
      currentIndex: 1,
      items: [],
    };
  },
  computed: {
    nextButtonText() {
      return this.currentSlide < 2 ? "Next" : "Get Started";
    },
  },
  async created() {
    try {
      const response = await api.getOnbording();
      this.items = response.data;
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    next() {
      if (this.currentSlide < this.items.length - 1) {
        this.currentSlide++;
        this.currentIndex++;
      } else {
        this.$router.push("/login");
      }
    },
    back() {
      if (this.currentSlide > 0) {
        this.currentSlide--;
        this.currentIndex--;
      }
    },
  },
  beforeMount() {
    if (this.$route.path === "/login") {
      this.$router.push("/onboarding");
    }
  },
};
