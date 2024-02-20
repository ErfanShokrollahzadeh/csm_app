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
export default {
  data() {
    return {
      input1: "",
      input2: "",
      input3: "",
      input4: "",
      countdown: 60,
      error: false,
      otp: "1234",
    };
  },
  methods: {
    limitInput(event) {
      event.target.value = event.target.value.slice(0, 1);
    },
    checkCode() {
      const enteredCode = this.input1 + this.input2 + this.input3 + this.input4;
      if (enteredCode !== this.otp) {
        this.error = true;
      }
    },
    goToVerification() {
      this.checkCode();
      if (!this.error) {
        this.$router.push("/verification");
      }
    },
  },
  created() {
    let intervalId = setInterval(() => {
      if (this.countdown === 0) {
        clearInterval(intervalId);
      } else {
        this.countdown--;
      }
    }, 1000);
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
  margin-top: 30px;
  padding: 11px;
  display: flex;
  flex-direction: column;
  align-items: center;
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
.input-row {
  display: flex;
  justify-content: space-evenly;
}
.width {
  width: 50px;
  height: 50px;
  border: 1px solid #4e4b66;
  border-radius: 5px;
  font-size: xx-large;
  padding: 15px;
}
.timer {
  text-align: center;
  color: #4e4b66;
  font-weight: 900;
  margin-top: 15px;
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
@media (max-width: 380px) {
  .button-container {
    margin-top: 18rem;
  }
}
@media (max-width: 320px) {
  .button-container {
    margin-top: 12rem;
  }
}
.btnforgot {
  width: 90%;
  font-weight: 700;
}
.error-text {
  color: red;
  margin-left: 40px;
}
.error-input {
  border: 1px solid #c30052;
  background-color: #fff3f8;
}
</style>
