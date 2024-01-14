import { createRouter, createWebHistory } from "vue-router";
import Home from "components/HomeVue.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  // Add more routes as needed
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
