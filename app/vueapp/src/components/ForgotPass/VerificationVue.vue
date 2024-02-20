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
        type="password"
        class="form-control input"
        id="exampleInputPassword1"
      />
    </div>
    <div class="mb-3">
      <label for="exampleInputPassword1" class="form-label"
        >Confirm new password<span>*</span></label
      >
      <input
        type="password"
        class="form-control input"
        id="exampleInputPassword1"
      />
    </div>
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
  padding: 15px;
}
h1 {
  font-weight: 900;
  color: #4e4b66;
}
.rest-pass {
  padding: 20px;
}
span {
  color: red;
}
.input {
  width: 100%;
  border: 1px solid #4e4b66;
  height: 50px;
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
@media (max-width: 400px) {
  .button-container {
    margin-top: 25rem;
  }
}
@media (max-width: 320px) {
  .button-container {
    margin-top: 12rem;
  }
}
.btnforgot {
  width: 100%;
  height: 45px;
  font-weight: 700;
}
label {
  font-weight: 700;
  color: #4e4b66;
}
</style>
