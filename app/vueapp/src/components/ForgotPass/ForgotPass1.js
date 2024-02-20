export default {
  data() {
    return {
      inputValue: "",
      inputError: false,
    };
  },
  methods: {
    validateInput() {
      this.inputError = !this.inputValue;
    },
    goToForgotPass2() {
      this.$router.push("/forgotpass2");
    },
  },
};
