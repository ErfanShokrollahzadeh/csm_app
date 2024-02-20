<template>
  <div class="back">
    <router-link to="/forgotpass2" class="routback">⬅</router-link>
  </div>
  <div class="title_pass">
    <h1>Reset <br />Password</h1>
  </div>

  <form action="" class="rest-pass">
    <div class="mb-3">
      <label for="exampleInputPassword1" class="form-label"
        >New Password<span>*</span></label
      >
      <input
        :type="passwordFieldType"
        class="form-control input"
        id="exampleInputPassword1"
      />
      <div class="input-group-append show">
        <button
          class="btn btn-outline-secondary icon"
          type="button"
          @click="togglePasswordVisibility"
        >
          <i :class="`fa ${passwordVisible ? 'fa-eye-slash' : 'fa-eye'}`"></i>
        </button>
      </div>
    </div>
    <div class="mb-3">
      <label for="exampleInputPassword1" class="form-label"
        >Confirm new password<span>*</span></label
      >
      <input
        :type="passwordFieldType"
        class="form-control input"
        id="exampleInputPassword1"
      />
      <div class="input-group-append show">
        <button
          class="btn btn-outline-secondary icon"
          type="button"
          @click="togglePasswordVisibility"
        >
          <i :class="`fa ${passwordVisible ? 'fa-eye-slash' : 'fa-eye'}`"></i>
        </button>
      </div>
    </div>
    <div class="button-container">
      <button
        type="submit"
        class="btn btn-primary btnforgot"
        @click="goToVerification2"
      >
        Submit
      </button>
    </div>
  </form>
</template>

<script>
import VerificationVue from "./VerificationVue.js";

export default {
  name: "VerificationVue",
  ...VerificationVue,
};
</script>

<style scoped src="./VerificationVue.css"></style>
