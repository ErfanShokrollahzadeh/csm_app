import { createRouter, createWebHistory } from "vue-router";
import OnbordingVue from "@/components/Onbording/OnbordingVue.vue";
import LogInVue from "@/components/Login/LogInVue.vue";

const routes = [
  {
    path: "/",
    name: "Onbording",
    component: OnbordingVue,
  },
  {
    path: "/login",
    name: "LogIn",
    component: LogInVue,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
