import axios from "axios";

export default {
  data() {
    return {
      passwordVisible: false,
      username: "",
      password: "",
      usernameError: false,
      passwordError: false,
      password1: "",
      password2: "",
      phoneNumber: "",
      image: null,
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
      formData.append("password1", this.password1);
      formData.append("password2", this.password2);
      formData.append("phone_number", this.phoneNumber);
      formData.append("image", this.image);

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
