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
import ForgotPass1 from "./ForgotPass1.js";

export default {
  name: "ForgotPass1",
  ...ForgotPass1,
};
</script>

<style scoped src="./ForgotPass1.css"></style>
