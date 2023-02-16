<template>
  <main class="flex w-full h-full" v-if="user.config.token !== ''">
    <!-- left bar -->
    <div class="flex flex-col w-[200px] h-full bg-[#F2F2F2] relative show-left">
      <!-- icon -->
      <div
        class="w-full h-16 flex items-center justify-center cursor-pointer hover:scale-105 transition-all"
      >
        <img src="../../assets/icon.svg" class="w-full h-5" alt="icon" />
      </div>
      <div class="flex-auto flex flex-col px-4 text-lg gap-8 overflow-y-scroll">
        <!-- notes/desks + trash -->
        <div class="flex flex-col gap-5">
          <!-- notes -->
          <p class="font-semibold cursor-default">Страницы</p>
          <div v-if="user.config.user.notes.length > 0">
            <div v-for="(note, index) in user.config.user.notes" :key="index">
              {{ note }}
            </div>
          </div>
          <div v-else class="text-sm">Страницы отстутствуют</div>
        </div>
        <div class="flex flex-col gap-5">
          <!-- desks -->
          <p class="font-semibold cursor-default">Доски</p>
          <div v-if="user.config.user.desks.length > 0">
            <div v-for="(desk, index) in user.config.user.desks" :key="index">
              {{ desk }}
            </div>
          </div>
          <div v-else class="text-sm">Доски отстутствуют</div>
        </div>
        <button class="flex gap-4 items-center">
          <img src="../../assets/trash.svg" class="w-6 h-6" alt="trash" />
          <p class="font-semibold">Корзина</p>
        </button>
      </div>
      <!-- new page btn -->
      <button
        class="w-full opacity-70 border-t-[1px] bg-[#F2F2F2] border-black font-semibold border-opacity-70 flex items-center justify-center px-7 py-2 gap-3 text-xl hover:opacity-100 transition-all"
      >
        <img src="../../assets/add.svg" class="w-5 h-5" alt="add" />
        <p>Добавить</p>
      </button>
    </div>
    <!-- main section -->
    <div class="flex-auto h-full flex flex-col">
      <!-- header? -->
      <header
        class="w-full h-16 text-xl flex justify-between items-center px-16 bg-white show-down"
      >
        <p class="cursor-default">Name of page</p>
        <div class="flex gap-5">
          <img
            class="w-7 h-7 opacity-50 cursor-pointer hover:opacity-75 transition-all"
            src="../../assets/star1.svg"
            alt="star"
          /><img
            src="../../assets/exportsquare.svg"
            alt="exportsquare"
            class="w-7 h-7 opacity-50 cursor-pointer hover:opacity-75 transition-all"
          /><img
            src="../../assets/maximize4.svg"
            class="w-7 h-7 opacity-50 cursor-pointer hover:opacity-75 transition-all"
            alt="maximize"
          /><img
            src="../../assets/setting2.svg"
            class="w-7 h-7 opacity-50 cursor-pointer hover:opacity-75 transition-all"
            alt="setting2"
          />
        </div>
      </header>
      <main
        class="flex-auto flex flex-col overflow-y-scroll h-screen show-right"
      >
        <!-- gradient -->
        <div
          class="h-1/3 w-full bg-gradient-to-r from-green-300 via-blue-500 to-purple-600"
        ></div>
        <!-- smile of note -->
        <div class="text-end w-96 h-0.5 text-4xl text-align-center -my-5">
          😀
        </div>
        <!-- type place -->
        <div
          class="flex-auto w-full flex flex-col gap-8 items-start pl-80 pt-20"
        >
          <div class="flex gap-5 w-full">
            <img
              src="../../assets/edit2.svg"
              class="w-10 h-10"
              alt="edit title)"
            />
            <input
              type="text"
              class="h-fit w-fit outline-0 border-0 opacity-30 focus:opacity-100 transition-all text-3xl"
              value="Name of page"
            />
          </div>
          <!-- here is md -->
          <!-- https://www.youtube.com/watch?v=lXc0c1n6O-g -->
        </div>
      </main>
    </div>
  </main>
</template>

<script setup lang="ts">
import { reactive, onMounted, ref } from "vue";
import axios from "axios";

import { useRouter } from "vue-router";
import { useUser } from "../../store/user";

const currentType = ref(null);
const mdText = ref();
const user = useUser();

// class="h-fit w-fit outline-0 border-0 opacity-30 bg-red-400 focus:opacity-100 transition-all text-xl"
const router = useRouter();

onMounted(() => {
  if (user.config.token === "") {
    router.push("/app/auth/signIn");
  }
});

interface ConfigType {
  yaToken?: string | null;
}

const config = reactive<ConfigType>({
  yaToken: localStorage.getItem("yaToken"),
});

const movelyElem = ref({
  rows: 1,
  cols: 1,
  onlyRows: false,
});

if (config.yaToken) {
  axios
    .get(
      "https://login.yandex.ru/info?format=json&jwt_secret=73a87743fe2e406d96d537209a21c1c0&oauth_token=" +
        config.yaToken
    )
    .then((res) => console.log(res.data))
    .catch((err) => console.error(err));
}
</script>

<style>
.editor {
  background-color: #050505;
  border-radius: 0.25em;
  padding: 1em;
}
</style>
