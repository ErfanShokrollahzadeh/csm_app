<template>
  <div id="app">
    <img
      v-if="showLogo"
      src="@/assets/Vector.svg"
      alt="Logo"
      class="logo-animation"
    />
    <router-view v-if="!showLogo" />
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

<style scoped>
.logo-animation {
  animation: fadeInOut 3s ease-out;
}

@keyframes fadeInOut {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}
</style>
