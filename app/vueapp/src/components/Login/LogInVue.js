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
      const hasNumber = /\d/;
      this.usernameError = hasNumber.test(this.username);
      this.passwordError = !this.password;
    },
  },
};
