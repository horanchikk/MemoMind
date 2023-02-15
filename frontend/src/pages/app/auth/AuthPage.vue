<template>
  <main class="flex justify-center items-center w-full h-full">
    <div
      class="flex flex-col gap-7 justify-center items-center w-2/6 h-full shadow-sm shadow-black"
    >
      <div class="flex justify-center items-center gap-5 w-[266px]">
        <img src="../../../assets/icon.svg" alt="Icon" />
      </div>
      <form
        v-if="config.params === 'signIn'"
        @submit.prevent="auth('in')"
        class="flex flex-col gap-5 justify-center items-center p-5 w-80 text-lg font-bold rounded-md shadow-sm select-none shadow-black show-up"
      >
        <p>Вход</p>

        <div class="flex flex-col gap-5">
          <MMInput
            type="text"
            v-model="inputData.login"
            placeholder="Логин"
            autofocus
          />
          <MMInput
            type="password"
            v-model="inputData.password"
            placeholder="Пароль"
          />
          <p
            v-show="config.exception"
            class="text-[#f80000] text-sm text-center"
          >
            {{ config.exception }}
          </p>
          <MMButton type="submit" class="flex items-center justify-center"
            ><p v-if="!config.loading">Войти</p>
            <svg
              class="self-center"
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
                  <stop
                    stop-color="#fff"
                    stop-opacity=".631"
                    offset="63.146%"
                  />
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
              </g></svg
          ></MMButton>
          <MMButton transparent @click="config.params = 'signUp'"
            >Впервые в MemoMind?</MMButton
          >
        </div>
      </form>
      <form
        v-else-if="config.params === 'signUp'"
        @submit.prevent="auth('up')"
        class="flex flex-col gap-5 justify-center items-center p-5 w-80 text-lg font-bold rounded-md shadow-sm select-none shadow-black show-up"
      >
        <p>Регистрация</p>

        <div class="flex flex-col gap-5">
          <MMInput
            type="text"
            v-model="inputData.firstName"
            placeholder="Имя"
            autofocus
          />
          <MMInput
            type="text"
            v-model="inputData.lastName"
            placeholder="Фамилия"
          />
          <MMInput type="email" v-model="inputData.email" placeholder="Почта" />
          <MMInput type="text" v-model="inputData.login" placeholder="Логин" />
          <MMInput
            type="password"
            v-model="inputData.password"
            placeholder="Пароль"
          />
          <p
            v-show="config.exception"
            class="text-[#f80000] text-sm text-center"
          >
            {{ config.exception }}
          </p>
          <MMButton type="submit" class="flex items-center justify-center"
            ><p v-if="!config.loading">Зарегистрироваться</p>
            <svg
              class="self-center"
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
                  <stop
                    stop-color="#fff"
                    stop-opacity=".631"
                    offset="63.146%"
                  />
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
          <MMButton transparent @click="config.params = 'signIn'"
            >У вас есть аккаунт?</MMButton
          >
        </div>
      </form>

      <button
        class="p-2 w-[266px] text-white flex justify-center bg-black rounded-md transition-all text-md hover:bg-opacity-90 active:opacity-80 active:scale-90"
        @click="auth('ya')"
      >
        <div v-if="!config.loadingYa" class="flex gap-5">
          <img src="../../../assets/yandex.svg" alt="yandex" class="w-6 h-6" />
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
      </button>
    </div>
    <div class="w-4/6 h-full bg-auth"></div>
  </main>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";

import router from "../../../router";
import MMButton from "../../../components/MMButton.vue";
import MMInput from "../../../components/MMInput.vue";
import { MMAPI } from "../../../mixins/api";
import { useUser } from "../../../store/user";

const inputData = reactive<{
  login: string;
  password: string;
  firstName: string;
  lastName: string;
  email: string;
}>({
  login: "",
  password: "",
  firstName: "",
  lastName: "",
  email: "",
});

const config = reactive<{
  loadingYa: boolean;
  loading: boolean;
  params: string;
  exception: string | undefined;
}>({
  loadingYa: false,
  loading: false,
  params: router.currentRoute.value.params.type as string,
  exception: undefined,
});

function reset() {
  inputData.login = "";
  inputData.password = "";
  inputData.firstName = "";
  inputData.lastName = "";
  inputData.email = "";

  config.exception = undefined;
  config.loadingYa = false;
  config.loading = false;
}

watch(
  () => config.params,
  () => {
    reset();
  }
);

async function auth(
  mode: "ya" | "in" | "up",
  username?: string,
  password?: string
) {
  if (mode === "ya") {
    config.loadingYa = true;
    router.push("/app/goYandex");
  } else if (mode === "in") {
    config.loading = true;
    const inToken = await MMAPI.logIn(inputData.login, inputData.password);
    if (inToken.message) {
      config.exception = inToken.message;
    } else {
      useUser().config.token = inToken.access_token;
      useUser().config.username = inputData.login;
      router.push("/app");
    }
    config.loading = false;
  } else if (mode === "up") {
    config.loading = true;
    const upToken = await MMAPI.registerUser(
      inputData.login,
      inputData.password,
      inputData.firstName,
      inputData.lastName,
      inputData.email
    );
    if (upToken.message) {
      config.exception = upToken.message;
    } else {
      useUser().config.token = upToken.access_token;
      useUser().config.username = inputData.login;
      router.push("/app");
    }
    config.loading = false;
  }
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
