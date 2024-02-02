<template>
  <div>
    <h1>Onbording</h1>
    <ul>
      <li v-if="Onbording.length">
        <h2>{{ Onbording[currentSlide].title }}</h2>
        <p>{{ Onbording[currentSlide].discriptions }}</p>
        <img :src="Onbording[currentSlide].image" alt="Onbording image" />
      </li>
    </ul>
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
</template>

<script>
// import api from "@/api";
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  data() {
    return {
      Onbording: [],
      currentSlide: 0,
    };
  },
  computed: {
    nextButtonText() {
      return this.currentSlide < 2 ? "Next" : "Get Started";
    },
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  async mounted() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/Onbording/");
      this.Onbording = response.data;
    } catch (error) {
      this.error =
        "There was an error fetching the data. Please try again later.";
      console.error(error);
    }
  },
  methods: {
    next() {
      if (this.currentSlide < this.Onbording.length - 1) {
        this.currentSlide++;
      }
    },
  },
};
</script>

<style scoped>
.navigation {
  display: flex;
  justify-content: center;
  align-items: baseline;
  margin-top: 3rem;
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

a {
  color: #bbb;
  cursor: pointer;
  text-decoration: none;
  margin-right: 0.5rem;
}

button {
  background-color: #1877f2;
  border: none;
  border-radius: 5px;
  color: #fff;
  cursor: pointer;
  padding: 0.5rem 1rem;
}
</style>
