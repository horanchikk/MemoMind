import { reactive } from "vue";
import { defineStore } from "pinia";

import type { User } from "../mixins/api";

export const useUser = defineStore("useUser", () => {
  const config = reactive<{
    token: string;
    username: string;
    user: User | "";
  }>({
    token: "",
    username: "",
    user: "",
  });

  return { config };
});
