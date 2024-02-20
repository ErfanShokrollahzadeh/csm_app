<template>
  <div class="back">
    <router-link to="/forgotpass1" class="routback">⬅</router-link>
  </div>
  <div class="title_pass">
    <h1>OTP Verification</h1>
    <p>Enter the OTP sent to +67-1234-5678-9</p>
  </div>

  <form action="" @submit.prevent="checkCode">
    <div class="input-row">
      <input
        type="tel"
        class="width"
        @input="limitInput"
        v-model="input1"
        :class="{ 'error-input': error }"
      />
      <input
        type="tel"
        class="width"
        @input="limitInput"
        v-model="input2"
        :class="{ 'error-input': error }"
      />
      <input
        type="tel"
        class="width"
        @input="limitInput"
        v-model="input3"
        :class="{ 'error-input': error }"
      />
      <input
        type="tel"
        class="width"
        @input="limitInput"
        v-model="input4"
        :class="{ 'error-input': error }"
      />
    </div>
    <p v-if="error" class="error-text">Invalid OTP</p>
    <p class="timer">
      Resend code in <span style="color: #c30052">{{ countdown }}s</span>
    </p>
    <div class="button-container">
      <button
        type="submit"
        class="btn btn-primary btnforgot"
        @click="goToVerification"
      >
        Verify
      </button>
    </div>
  </form>
</template>

<script>
import ForgotPass2 from "./ForgotPass2.js";
export default {
  name: "ForgotPass2",
  ...ForgotPass2,
};
</script>

<style scoped src="./ForgotPass2.css"></style>
