<template>
  <div class="back">
    <router-link to="/newssource" class="routback">⬅</router-link>
    <h1>Fill your Profile</h1>
  </div>

  <div>
    <form>
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
</style>
