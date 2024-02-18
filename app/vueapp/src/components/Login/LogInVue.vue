<template>
  <div class="title">
    <h1>
      Hello <br />
      <span>Again!</span>
    </h1>
    <p>
      Welcome back you’ve <br />
      been missed
    </p>
  </div>

  <form class="register" @submit.prevent="validateForm">
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
      <router-link to="/forgotpass" class="fogotpass"
        >Forgot the password ?</router-link
      >
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
      don’t have an account ?<router-link
        to="/signup"
        style="color: #1877f2; margin-left: 10px; text-decoration: none"
        >Sign Up</router-link
      >
    </p>
  </form>
</template>

<script>
import LogIn from "./LogInVue.js";

export default {
  name: "LogInVue",
  ...LogIn,
};
</script>

<style scoped src="./LogInVue.css"></style>
