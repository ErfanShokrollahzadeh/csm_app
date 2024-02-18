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
    <button type="button" class="btn btn-primary btnforgot">Submit</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedOption: "",
      error: false,
    };
  },
  methods: {
    validateForm() {
      if (!this.selectedOption) {
        this.error = true;
      } else {
        // Continue with form submission
      }
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
  padding: 20px;
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
.button-container {
  display: flex;
  justify-content: center;
  margin-top: 25rem;
}
.btnforgot {
  width: 90%;
}
.selectradio {
  margin-left: 10px;
  background-color: #eef1f4;
}
.error-text {
  color: red;
}
</style>
