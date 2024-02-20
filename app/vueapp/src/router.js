import { createRouter, createWebHistory } from "vue-router";
import OnbordingVue from "@/components/Onbording/OnbordingVue.vue";
import LogInVue from "@/components/Login/LogInVue.vue";
import SignUpVue from "@/components/SignUp/SignUpVue.vue";
import ForgotPass from "@/components/ForgotPass/ForgotPass.vue";
import ForgotPass1 from "@/components/ForgotPass/ForgotPass1.vue";
import ForgotPass2 from "@/components/ForgotPass/ForgotPass2.vue";
import Verification from "@/components/ForgotPass/VerificationVue.vue";

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
  {
    path: "/forgotpass1",
    name: "ForgotPass1",
    component: ForgotPass1,
  },
  {
    path: "/forgotpass2",
    name: "ForgotPass2",
    component: ForgotPass2,
  },
  {
    path: "/verification",
    name: "Verification",
    component: Verification,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
