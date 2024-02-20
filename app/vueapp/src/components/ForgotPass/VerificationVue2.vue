<template>
  <div>
    <img src="@/assets/Vector.svg" alt="Logo" class="child-verify" />
  </div>
  <h1>Congratulations!</h1>
  <p>Your account is ready to use</p>

  <div class="button-container">
    <button
      type="submit"
      class="btn btn-primary btnforgot"
      @click="goToVerification2"
    >
      Go to Homepage
    </button>
  </div>
</template>

<script>
import VerificationVue2 from "./VerificationVue2.js";
export default {
  name: "VerificationVue2",
  ...VerificationVue2,
};
</script>

<style scoped src="./VerificationVue2.css"></style>
