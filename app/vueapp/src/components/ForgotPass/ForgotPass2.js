export default {
  data() {
    return {
      input1: "",
      input2: "",
      input3: "",
      input4: "",
      countdown: 60,
      error: false,
      otp: "1234",
    };
  },
  methods: {
    limitInput(event) {
      event.target.value = event.target.value.slice(0, 1);
    },
    checkCode() {
      const enteredCode = this.input1 + this.input2 + this.input3 + this.input4;
      if (enteredCode !== this.otp) {
        this.error = true;
      }
    },
    goToVerification() {
      this.checkCode();
      if (!this.error) {
        this.$router.push("/verification");
      }
    },
  },
  created() {
    let intervalId = setInterval(() => {
      if (this.countdown === 0) {
        clearInterval(intervalId);
      } else {
        this.countdown--;
      }
    }, 1000);
  },
};
