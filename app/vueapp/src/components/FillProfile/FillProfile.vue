<template>
  <div class="back">
    <router-link to="/newssource" class="routback">⬅</router-link>
    <h1>Fill your Profile</h1>
  </div>

  <div>
    <form class="register">
      <div class="profile-photo">
        <label for="photo-upload" class="photo-label">
          <input
            type="file"
            id="photo-upload"
            accept="image/*"
            @change="handlePhotoUpload"
          />
        </label>
      </div>

      <label class="input1"> Username</label>
      <input type="text" class="input2" />

      <label class="input1"> Full Name</label>
      <input type="text" class="input2" />

      <label class="input1">Email Address <span>*</span></label>
      <input type="email" class="input2" />

      <label class="input1">Phone Number <span>*</span></label>
      <input type="number" class="input2" />

      <div class="button-container">
        <button type="button" class="btn btn-primary btnforgot" @click="goto">
          Next
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.back {
  display: flex;
  justify-content: space-evenly;
  align-items: flex-start;
  font-size: 20px;
  margin-top: 30px;
  margin-right: 60px;
  align-items: center;
}
.routback {
  text-decoration: none;
  color: #4e4b66;
  margin-right: 10px;
}
.profile-photo {
  display: flex;
  justify-content: center;
  align-items: center;
}

.photo-label {
  position: relative;
}

.photo-preview {
  border-radius: 50%;
  width: 100px; /* adjust as needed */
  height: 100px; /* adjust as needed */
}

#photo-upload {
  top: 0;
  width: 100px;
  height: 100px;
  cursor: pointer;
  border-radius: 50%;
  border: 1px solid #4e4b66;
  background-color: #eef1f4;
}
.register {
  display: flex;
  flex-direction: column;
  padding: 15px;
}
.input1 {
  margin-top: 10px;
  font-weight: 700;
  color: #4e4b66;
}
.input2 {
  height: 45px;
  border-radius: 5px;
  border: 1px solid #4e4b66;
}
span {
  color: red;
  font-size: 20px;
}
.button-container {
  display: flex;
  justify-content: center;
}
@media (max-width: 992px) {
  .button-container {
    margin-top: 16rem;
  }
}

/* For mobile phones */
@media (max-width: 380px) {
  .button-container {
    margin-top: 0rem;
  }
}
@media (max-width: 320px) {
  .button-container {
    margin-top: 0rem;
  }
}
.btnforgot {
  width: 90%;
  height: 45px;
  font-weight: 700;
}
</style>
