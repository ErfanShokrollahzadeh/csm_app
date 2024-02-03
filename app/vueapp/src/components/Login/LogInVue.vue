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

  <form class="register">
    <div class="mb-3">
      <label for="exampleInputText" class="form-label"
        >username<span class="star">*</span></label
      >
      <input
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
        :type="passwordFieldType"
        class="form-control border-black"
        id="exampleInputPassword1"
        required
      />
      <span class="password-toggle-icon"><i class="fas fa-eye"></i></span>
      <span
        ><i :class="`fa fa-eye${passwordVisible ? '-slash' : ''}`"></i
      ></span>
    </div>

    <div class="mb-3 form-check">
      <input type="checkbox" class="form-check-input" id="exampleCheck1" />
      <label class="form-check-label" for="exampleCheck1">Remmember me</label>
      <a href="#" class="forgot">Forgot the password ?</a>
      <div class="password-toggle-icon">
        <i :class="`bi ${passwordVisible ? 'bi-eye-slash' : 'bi-eye'}`"></i>
      </div>
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
      don’t have an account ?<a class="signuplink">Sign Up</a>
    </p>
  </form>
</template>

<script>
export default {
  data() {
    return {
      passwordVisible: false,
    };
  },
  //   computed: {
  //     passwordFieldType() {
  //       return this.passwordVisible ? "text" : "password";
  //     },
  //   },
  methods: {
    togglePasswordVisibility() {
      this.passwordVisible = !this.passwordVisible;
    },
  },
};
</script>

<style scoped>
.title {
  padding: 24px;
}
h1 {
  font-weight: revert;
  font-size: xxx-large;
}
h1 span {
  color: blue;
}
.star {
  color: red;
}
.register {
  padding: 24px;
}
.btnlogin {
  width: 100%;
}
.forgot {
  float: right;
  text-decoration: none;
}
.firstp {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
  color: #4e4b66;
}
.secondp {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
  color: #4e4b66;
}
.facgoogle {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-top: 10px;
}
.btnfacebook {
  width: 45%;
  height: 45px;
  background: #e5ecf4;
  color: #667080;
}
.btngoogle {
  width: 45%;
  height: 45px;
  background: #e5ecf4;
  color: #667080;
}
.signuplink {
  color: #1877f2;
  margin-left: 5px;
  text-decoration: none;
}
</style>
