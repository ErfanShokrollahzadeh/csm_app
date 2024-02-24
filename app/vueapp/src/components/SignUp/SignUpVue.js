import axios from "axios";

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
    submitForm() {
      let formData = new FormData();
      formData.append("username", this.username);
      formData.append("password1", this.password);

      axios
        .post("/register/", formData)
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
