<template>
  <main class="flex w-full h-full">
    <!-- left bar -->
    <div class="flex flex-col w-[200px] h-full bg-[#F2F2F2] relative">
      <!-- icon -->
      <div
        class="w-full h-16 flex items-center justify-center cursor-pointer hover:scale-105 transition-all"
      >
        <img src="../../assets/icon.svg" alt="icon" />
      </div>
      <div class="flex-auto overflow-y-scroll">
        <!-- notes/desks + trash -->
      </div>
      <!-- new page btn -->
      <button
        class="w-full border-t-[1px] bg-[#F2F2F2] border-black border-opacity-70 flex items-center justify-center px-7 gap-3 text-xl hover:opacity-100 transition-all"
      >
        <img src="../../assets/add.svg" class="w-5 h-5" alt="add" />
        <p>New note</p>
      </button>
    </div>
    <!-- main section -->
    <div class="flex-auto h-full"></div>
  </main>
</template>

<script setup lang="ts">
import { reactive, onMounted, watch } from "vue";
import axios from "axios";

interface ConfigType {
  yaToken?: string | null;
}

const config = reactive<ConfigType>({
  yaToken: localStorage.getItem("yaToken"),
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
