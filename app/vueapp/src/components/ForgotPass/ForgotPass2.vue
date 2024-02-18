<template>
  <div class="back">
    <router-link to="/forgotpass1" class="routback">⬅</router-link>
  </div>
  <div class="title_pass">
    <h1>OTP Verification</h1>
    <p>Enter the OTP sent to +67-1234-5678-9</p>
  </div>

  <form action="">
    <input type="number" />
    <input type="number" />
    <input type="number" />
    <input type="number" />
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
</style>
