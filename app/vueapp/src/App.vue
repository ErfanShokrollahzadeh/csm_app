<!-- App.vue -->
<template>
  <div id="app">
    <div v-if="showLogo" class="parent">
      <img src="@/assets/Vector.svg" alt="Logo" class="child" />
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
  /* height: 100vh; */
}

.parent {
  position: relative;
  height: 100vh; /* Adjust the height as needed */
}

.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
/* Additional styles as needed */
</style>
