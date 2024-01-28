import { createRouter, createWebHistory } from "vue-router";
import HomeVue from "@/components/HomeVue.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeVue,
  },
  // Add more routes as needed
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
