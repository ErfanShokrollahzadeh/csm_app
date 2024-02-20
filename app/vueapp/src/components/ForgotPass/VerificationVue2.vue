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

<script></script>

<style scoped>
.child-verify {
  position: absolute;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
}
h1 {
  font-weight: 900;
  color: #4e4b66;
  text-align: center;
  margin-top: 125%;
}
p {
  color: #4e4b66;
  font-weight: 300;
  text-align: center;
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
    margin-top: 13rem;
  }
}
@media (max-width: 320px) {
  .button-container {
    margin-top: 12rem;
  }
}
.btnforgot {
  width: 90%;
  height: 45px;
  font-weight: 700;
}
</style>
