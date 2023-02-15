<template>
  <main class="w-full h-full flex items-center justify-center">
    <div
      class="w-4/6 h-full shadow-sm shadow-black flex flex-col gap-7 items-center justify-center"
    >
      <div class="flex justify-between items-center gap-5 w-[266px]">
        <img src="../../../assets/icon.svg" alt="Icon" />
        <p class="tracking-widest select-none font-semibold text-3xl">
          MemoMind
        </p>
      </div>
      <form
        v-if="params === 'signIn'"
        class="flex flex-col items-center justify-center gap-5 rounded-md shadow-sm shadow-black p-5 w-80 text-lg font-bold select-none"
      >
        <p>Вход</p>

        <div class="flex flex-col gap-5">
          <MMInput type="text" v-model="login" placeholder="Логин" autofocus />
          <MMInput type="password" v-model="password" placeholder="Пароль" />
          <p class="text-[#f80000] text-sm text-center">Типо эксцепшон</p>
          <MMButton>Войти</MMButton>
          <MMButton transparent @click="params = 'signUp'"
            >Впервые в MemoMind?</MMButton
          >
        </div>
      </form>
      <form
        v-else-if="params === 'signUp'"
        class="flex flex-col items-center justify-center gap-5 rounded-md shadow-sm shadow-black p-5 w-80 text-lg font-bold select-none"
      >
        <p>Регистрация</p>

        <div class="flex flex-col gap-5">
          <MMInput type="text" v-model="login" placeholder="Логин" autofocus />
          <MMInput type="password" v-model="password" placeholder="Пароль" />
          <p class="text-[#f80000] text-sm text-center">Типо эксцепшон</p>
          <MMButton>Войти</MMButton>
          <MMButton transparent @click="params = 'signIn'"
            >У вас есть аккаунт?</MMButton
          >
        </div>
      </form>
      <MMButton
        class="flex items-center justify-center w-[266px] bg-black hover:bg-[#1e6659]"
        @click="yaAuth()"
      >
        <div v-if="!authLoading" class="flex gap-5">
          <img src="../../../assets/yandex.svg" alt="yandex" class="h-6 w-6" />
          <p>Войти с Яндекс ID</p>
        </div>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="25"
          height="25"
          viewBox="0 0 38 38"
          v-else
        >
          <defs>
            <linearGradient
              x1="8.042%"
              y1="0%"
              x2="65.682%"
              y2="23.865%"
              id="a"
            >
              <stop stop-color="#fff" stop-opacity="0" offset="0%" />
              <stop stop-color="#fff" stop-opacity=".631" offset="63.146%" />
              <stop stop-color="#fff" offset="100%" />
            </linearGradient>
          </defs>
          <g fill="none" fill-rule="evenodd">
            <g transform="translate(1 1)">
              <path
                d="M36 18c0-9.94-8.06-18-18-18"
                id="Oval-2"
                stroke="url(#a)"
                stroke-width="2"
              >
                <animateTransform
                  attributeName="transform"
                  type="rotate"
                  from="0 18 18"
                  to="360 18 18"
                  dur="0.9s"
                  repeatCount="indefinite"
                />
              </path>
              <circle fill="#fff" cx="36" cy="18" r="1">
                <animateTransform
                  attributeName="transform"
                  type="rotate"
                  from="0 18 18"
                  to="360 18 18"
                  dur="0.9s"
                  repeatCount="indefinite"
                />
              </circle>
            </g>
          </g>
        </svg>
      </MMButton>
    </div>
    <div class="w-2/6 h-full bg-auth"></div>
  </main>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";

import router from "../../../router";
import MMButton from "../../../components/MMButton.vue";
import MMInput from "../../../components/MMInput.vue";

const login = ref();
const password = ref();
const authLoading = ref(false);
const params = ref(router.currentRoute.value.params.type);

watch(
  () => params.value,
  () => {
    login.value = "";
    password.value = "";
  }
);

function yaAuth() {
  // http://oauth.yandex.ru/authorize?response_type=token&client_id=c5cd63cbaeb34647bfc55041968a942b
  authLoading.value = true;
  router.push("/app/goYandex");
}
</script>

<style scoped>
.bg-auth {
  background: radial-gradient(
      111.9% 65.04% at 53.38% 22.08%,
      rgba(189, 118, 144, 0.5) 0%,
      rgba(255, 255, 255, 0) 100%
    ),
    radial-gradient(
      67.79% 39.4% at 30.68% 47.72%,
      rgba(189, 118, 118, 0.5) 0%,
      rgba(255, 255, 255, 0) 100%
    ),
    radial-gradient(
      103.71% 60.28% at 84.83% 8.38%,
      rgba(118, 189, 185, 0.5) 0%,
      rgba(255, 255, 255, 0) 100%
    ),
    radial-gradient(
      44.65% 25.95% at 12.01% 88.2%,
      rgba(135, 172, 227, 0.5) 0%,
      rgba(255, 255, 255, 0) 100%
    ),
    radial-gradient(
      99.78% 57.99% at 89.19% 89.02%,
      rgba(141, 118, 189, 0.5) 0%,
      rgba(255, 255, 255, 0) 100%
    ),
    radial-gradient(
      89.19% 51.84% at 97.82% 46.26%,
      rgba(189, 118, 118, 0.5) 0%,
      rgba(255, 255, 255, 0) 100%
    ),
    radial-gradient(
      106% 61.61% at 15.5% 7.04%,
      rgba(189, 118, 174, 0.5) 0%,
      rgba(255, 255, 255, 0) 100%
    );
}
</style>
