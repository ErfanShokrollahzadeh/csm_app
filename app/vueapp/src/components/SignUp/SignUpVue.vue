<template>
  <div class="title">
    <h1>Hello!</h1>
    <p>Signup to get Started</p>
  </div>

  <form
    class="register"
    @submit.prevent="
      submitForm;
      validateForm;
    "
  >
    <div class="mb-3">
      <label for="exampleInputText" class="form-label"
        >username<span class="star">*</span></label
      >
      <input
        v-model="username"
        :class="{ error: usernameError }"
        type="text"
        class="form-control border-black"
        id="exampleInputText"
        aria-describedby="textHelp"
        required
      />
      <p v-if="usernameError" class="error-text">Invalid username</p>
    </div>
    <div class="mb-3">
      <label for="exampleInputPassword" class="form-label"
        >Password<span class="star">*</span></label
      >
      <input
        v-model="password"
        :class="{ error: passwordError }"
        :type="passwordFieldType"
        class="form-control border-black"
        id="exampleInputPassword1"
        required
      />
      <p v-if="passwordError" class="error-text">Invalid password</p>
      <div class="input-group-append show">
        <button
          class="btn btn-outline-secondary"
          type="button"
          @click="togglePasswordVisibility"
        >
          <i :class="`fa ${passwordVisible ? 'fa-eye-slash' : 'fa-eye'}`"></i>
        </button>
      </div>
    </div>
    <div class="mb-3 form-check">
      <input type="checkbox" class="form-check-input" id="exampleCheck1" />
      <label class="form-check-label" for="exampleCheck1">Remmember me</label>
    </div>
    <button type="submit" class="btn btn-primary btnlogin">Login</button>

    <p class="firstp">or continue with</p>

    <div class="facgoogle">
      <button class="btn btnfacebook" type="submit">
        <i class="fab fa-facebook-f"></i> Facebook
      </button>
      <button class="btn btngoogle">
        <i class="fab fa-google"></i> Google
      </button>
    </div>
    <p class="secondp">
      Already have an account ?<router-link
        to="/login"
        style="color: #1877f2; margin-left: 10px; text-decoration: none"
        >Login</router-link
      >
    </p>
  </form>
</template>

<script>
import SignUp from "./SignUpVue.js";

export default {
  name: "SignUpVue",
  ...SignUp,
};
</script>

<style scoped src="./SignUpVue.css"></style>
