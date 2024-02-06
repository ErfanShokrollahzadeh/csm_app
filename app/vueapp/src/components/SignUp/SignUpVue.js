export default {
  data() {
    return {
      passwordVisible: false,
    };
  },
  //   computed: {
  //     passwordFieldType() {
  //       return this.passwordVisible ? "text" : "password";
  //     },
  //   },
  methods: {
    togglePasswordVisibility() {
      this.passwordVisible = !this.passwordVisible;
    },
  },
};
