import { createRouter, createWebHistory } from "vue-router";
import OnbordingVue from "@/components/Onbording/OnbordingVue.vue";

const routes = [
  {
    path: "/",
    name: "Onbording",
    component: OnbordingVue,
  },
  // Add more routes as needed
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
