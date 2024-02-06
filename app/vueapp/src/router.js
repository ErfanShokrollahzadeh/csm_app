import { createRouter, createWebHistory } from "vue-router";
import OnbordingVue from "@/components/Onbording/OnbordingVue.vue";
import LogInVue from "@/components/Login/LogInVue.vue";
import SignUpVue from "@/components/SignUp/SignUpVue.vue";
import ForgotPass from "@/components/ForgotPass/ForgotPass.vue";

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
  {
    path: "/signup",
    name: "SignUp",
    component: SignUpVue,
  },
  {
    path: "/forgotpass",
    name: "ForgotPass",
    component: ForgotPass,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
