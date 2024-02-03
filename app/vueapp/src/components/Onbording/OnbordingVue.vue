<template>
  <div class="scrollable">
    <div id="carouselExampleIndicators" class="carousel slide">
      <div class="carousel-inner">
        <div v-for="item in items" :key="item.id">
          <div
            :class="
              item.id === currentIndex
                ? 'carousel-item active'
                : 'carousel-item'
            "
          >
            <img
              :src="item.image"
              class="d-block w-100"
              alt="Onbording image"
            />
          </div>
        </div>
      </div>
    </div>

    <div v-for="item in items" :key="item.id" class="test">
      <div
        :class="
          item.id === currentIndex ? 'description-block' : 'description-none'
        "
      >
        <h2>{{ item.title }}</h2>
        <p>{{ item.discriptions }}</p>
      </div>
    </div>

    <div class="controls">
      <div class="dots">
        <span
          v-for="(dot, index) in [1, 2, 3]"
          :key="index"
          :class="{ active: currentSlide === index }"
        ></span>
      </div>

      <button
        class="btnback"
        @click.prevent="back"
        :class="{ disabled: currentSlide === 0 }"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide="prev"
      >
        Back
      </button>
      <button
        class="btn btn-primary"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide="next"
        @click="next"
        :disabled="currentSlide === Onbording.length - 1"
      >
        {{ nextButtonText }}
      </button>
    </div>
  </div>
</template>

<script>
import Onbording from "./OnbordingVue.js";

export default {
  name: "OnbordingVue",
  ...Onbording,
};
</script>

<style scoped src="./OnbordingVue.css"></style>
