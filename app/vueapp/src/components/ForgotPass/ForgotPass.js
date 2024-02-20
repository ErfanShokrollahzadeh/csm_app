export default {
  data() {
    return {
      selectedOption: "",
      error: false,
    };
  },
  methods: {
    validateForm() {
      if (!this.selectedOption) {
        this.error = true;
      } else {
        // Continue with form submission
      }
    },
    goToForgotPass1() {
      this.$router.push("/forgotpass1");
    },
  },
};
