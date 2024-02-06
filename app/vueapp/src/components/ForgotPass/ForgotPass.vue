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

  <div class="form-check form-check-reverse">
    <input class="form-check-input" type="radio" value="" id="reverseCheck1" />
    <label class="form-check-label" for="reverseCheck1">
      Reverse checkbox
    </label>
  </div>
  <div class="form-check form-check-reverse">
    <input class="form-check-input" type="radio" value="" id="reverseCheck1" />
    <label class="form-check-label" for="reverseCheck1">
      Reverse checkbox
    </label>
  </div>
</template>

<script></script>

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
</style>
