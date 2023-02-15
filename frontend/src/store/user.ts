import { reactive } from "vue";

import { defineStore } from "pinia";

export const useUser = defineStore("useUser", () => {
  const config = reactive({
    token: "",
    username: "",
  });

  return { config };
});
