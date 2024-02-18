<template>
  <div class="back">
    <router-link to="/forgotpass" class="routback">⬅</router-link>
  </div>
  <div class="title_pass">
    <h1>
      Forgot? <br />
      Password?
    </h1>
    <p>
      Don’t worry! it happens. Please select the email or number associated with
      your account.
    </p>
  </div>

  <div class="email-number">
    <label>Email ID / Mobile number</label>
    <input
      type="text"
      class="firstinput"
      v-model="inputValue"
      :class="{ error: inputError }"
    />
  </div>

  <p v-if="inputError" class="error-text">Enter your email or number</p>

  <div class="button-container">
    <button
      type="button"
      class="btn btn-primary btnforgot"
      @click="goToForgotPass2"
    >
      Submit
    </button>
  </div>
</template>

<script>
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
</script>

<style scoped>
.back {
  margin-top: 20px;
  margin-left: 20px;
  font-size: 20px;
}
.routback {
  text-decoration: none;
  color: #4e4b66;
}
.title_pass {
  padding: 11px;
}
h1 {
  font-weight: 900;
  color: #4e4b66;
}
p {
  padding-top: 5px;
  color: #4e4b66;
  font-weight: 300;
}
.email-number {
  padding: 0px 15px;
}
.firstinput {
  width: 100%;
  height: 50px;
  border-radius: 6px;
}
.error {
  border: 1px solid red;
}
.error-text {
  color: red;
}
.button-container {
  display: flex;
  justify-content: center;
}
@media (max-width: 992px) {
  .button-container {
    margin-top: 30rem;
  }
}

/* For mobile phones */
@media (max-width: 380px) {
  .button-container {
    margin-top: 18rem;
  }
}
@media (max-width: 320px) {
  .button-container {
    margin-top: 12rem;
  }
}
.btnforgot {
  width: 90%;
}
</style>
