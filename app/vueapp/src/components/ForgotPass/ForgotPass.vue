<template>
  <div class="back">
    <router-link to="/login" class="routback">⬅</router-link>
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

  <div class="form-check form-check selectradio">
    <input class="form-check-input" type="radio" value="" id="reverseCheck1" />
    <label class="form-check-label" for="reverseCheck1">
      <p>via Email: <br />example@youremail.com</p>
    </label>
  </div>
  <div class="form-check form-check selectradio">
    <input class="form-check-input" type="radio" value="" id="reverseCheck1" />
    <label class="form-check-label" for="reverseCheck1">
      <p>via SMS: <br />+62-8421-4512-2531</p>
    </label>
  </div>

  <p v-if="error" class="error-text">Please select an option</p>

  <div class="button-container">
    <button
      type="button"
      class="btn btn-primary btnforgot"
      @click="goToForgotPass1"
    >
      Submit
    </button>
  </div>
</template>

<script>
import ForgotPass from "./ForgotPass.js";
export default {
  name: "ForgotPass",
  ...ForgotPass,
};
</script>

<style scoped src="./ForgotPass.css"></style>
