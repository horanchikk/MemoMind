import { reactive } from "vue";
import { defineStore } from "pinia";

import type { User } from "../mixins/api";
import { MMAPI } from "../mixins/api";

export const useUser = defineStore("useUser", () => {
  const config = reactive<{
    api: MMAPI;
    username: string;
    user: User;
  }>({
    api: new MMAPI(),
    username: "",
    user: {},
  });

  return { config };
});
