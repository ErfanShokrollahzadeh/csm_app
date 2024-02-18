export default {
  data() {
    return {
      passwordVisible: false,
      username: "",
      password: "",
      usernameError: false,
      passwordError: false,
    };
  },
  computed: {
    passwordFieldType() {
      return this.passwordVisible ? "text" : "password";
    },
  },
  methods: {
    togglePasswordVisibility() {
      this.passwordVisible = !this.passwordVisible;
    },
    validateForm() {
      this.usernameError = !this.username;
      this.passwordError = !this.password;
    },
  },
};
