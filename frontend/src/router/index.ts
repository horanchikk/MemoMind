import { createWebHashHistory, createRouter } from "vue-router";

import YandexAuth from "../pages/app/auth/YandexAuth.vue";
import AuthPage from "../pages/app/auth/AuthPage.vue";
import goya from "../pages/app/auth/goya.vue";

import HomePage from "../pages/HomePage.vue";

import AppPage from "../pages/app/AppPage.vue";

import type { RouteRecordRaw } from "vue-router";

const routes = <RouteRecordRaw[]>[
  {
    path: "/",
    component: HomePage,
    name: "Home",
  },
  {
    path: "/app/auth/:type",
    component: AuthPage,
    name: "Auth",
  },
  {
    path: "/access_token:id",
    component: YandexAuth,
    name: "Yandex",
  },
  {
    path: "/app/goYandex",
    component: goya,
    beforeEnter(to, from, next) {
      window.location.replace(
        "https://oauth.yandex.ru/authorize?response_type=token&client_id=c5cd63cbaeb34647bfc55041968a942b"
      );
    },
  },
  {
    path: "/app",
    component: AppPage,
    name: "App",
  },
];

const router = createRouter({
  routes: routes,
  history: createWebHashHistory(),
});

export default router;
