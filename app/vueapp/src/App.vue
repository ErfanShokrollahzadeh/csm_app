<!-- App.vue -->
<template>
  <div id="app">
    <div v-if="showLogo">
      <img src="@/assets/Vector.svg" alt="Logo" />
    </div>
    <div v-else>
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showLogo: true,
    };
  },
  created() {
    // Hide the logo after 3 seconds
    setTimeout(() => {
      this.showLogo = false;
    }, 3000);
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

img {
  max-width: 100%;
  max-height: 100%;
}

/* Additional styles as needed */
</style>
