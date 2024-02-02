<template>
  <div id="carouselExampleIndicators" class="carousel slide">
    <div class="carousel-indicators">
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="0"
        class="active"
        aria-current="true"
        aria-label="Slide 1"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="1"
        aria-label="Slide 2"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="2"
        aria-label="Slide 3"
      ></button>
    </div>
    <div class="carousel-inner">
      <div v-for="item in items" :key="item.id">
        <div
          :class="
            item.id === currentIndex ? 'carousel-item active' : 'carousel-item'
          "
        >
          <img :src="item.image" class="d-block" alt="Onbording image" />
        </div>
      </div>
    </div>
  </div>

  <div v-for="item in items" :key="item.id">
    <div
      :class="
        item.id === currentIndex ? 'description-block' : 'description-none'
      "
    >
      <h2>{{ item.title }}</h2>
      <p>{{ item.discriptions }}</p>
    </div>
  </div>

  <div>
    <div class="dots">
      <span
        v-for="(dot, index) in [1, 2, 3]"
        :key="index"
        :class="{ active: currentSlide === index }"
      ></span>
    </div>

    <button
      class="btn btn-danger"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="next"
      @click="next"
      :disabled="currentSlide === Onbording.length - 1"
    >
      {{ nextButtonText }}
    </button>
    <button
      @click.prevent="back"
      :class="{ disabled: currentSlide === 0 }"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="prev"
    >
      Back
    </button>
  </div>
</template>

<script>
import api from "@/api"; // Adjust the path according to your project structure

export default {
  data() {
    return {
      Onbording: [],
      currentSlide: 0,
      currentIndex: 1,
      items: [],
    };
  },
  computed: {
    nextButtonText() {
      return this.currentSlide < 2 ? "Next" : "Get Started";
    },
  },
  async created() {
    try {
      const response = await api.getOnbording();
      this.items = response.data;
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    next() {
      if (this.currentSlide < this.items.length - 1) {
        this.currentSlide++;
        this.currentIndex++;
      }
    },
    back() {
      if (this.currentSlide > 0) {
        this.currentSlide--;
        this.currentIndex--;
      }
    },
  },
};
</script>

<style scoped>
.description-block {
  display: block;
}

.description-none {
  display: none;
}

.dots {
  display: flex;
  justify-content: center;
  margin-right: 12rem;
}

.dots span {
  height: 10px;
  width: 10px;
  margin: 0 5px;
  background-color: #a0a3bd;
  border-radius: 50%;
  display: inline-block;
}

.dots span.active {
  background-color: #1877f2;
}
</style>
