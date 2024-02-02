<template>
  <div>
    <h1>Onbording</h1>
    <div v-for="item in items" :key="item.id">
      <h2>{{ item.title }}</h2>
      <p>{{ item.discriptions }}</p>
      <img :src="item.image" alt="Onbording image" />
      <!-- <p>{{ item.image }}</p> -->
    </div>

    <p v-if="error" class="error">{{ error }}</p>
  </div>

  <div class="navigation">
    <!-- slide -->
    <div class="dots">
      <span
        v-for="(dot, index) in [1, 2, 3]"
        :key="index"
        :class="{ active: currentSlide === index }"
      ></span>
    </div>

    <!-- Next button -->
    <a href="#" @click.prevent="back" :class="{ disabled: currentSlide === 0 }"
      >Back</a
    >
    <button @click="next" :disabled="currentSlide === Onbording.length - 1">
      {{ nextButtonText }}
    </button>
  </div>
  <hr />

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
        <div class="carousel-item active">
          <img :src="item.image" class="d-block" alt="Onbording image" />
        </div>
      </div>
    </div>
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  <hr />

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
  </div>
</template>

<script>
import api from "@/api"; // Adjust the path according to your project structure

export default {
  data() {
    return {
      Onbording: [],
      currentSlide: 0,
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
      }
    },
    back() {
      if (this.currentSlide > 0) {
        this.currentSlide--;
      }
    },
  },
};
</script>

<style scoped>
/* .navigation {
  display: flex;
  justify-content: center;
  align-items: baseline;
  margin-top: 3rem;
} */

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

/* a {
  color: #bbb;
  cursor: pointer;
  text-decoration: none;
  margin-right: 0.5rem;
} */

/* button {
  background-color: #1877f2;
  border: none;
  border-radius: 5px;
  color: #fff;
  cursor: pointer;
  padding: 0.5rem 1rem;
} */
</style>
