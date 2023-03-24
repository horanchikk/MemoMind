<template>
  <div class="w-full h-full flex flex-col items-center justify-center gap-7">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="50"
      height="50"
      viewBox="0 0 38 38"
    >
      <defs>
        <linearGradient x1="8.042%" y1="0%" x2="65.682%" y2="23.865%" id="a">
          <stop stop-color="black" stop-opacity="0" offset="0%" />
          <stop stop-color="black" stop-opacity=".631" offset="63.146%" />
          <stop stop-color="black" offset="100%" />
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
          <circle fill="black" cx="36" cy="18" r="1">
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
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import { useUser } from "../../../store/user";
import MMButton from "../../../components/MMButton.vue";
import { ref } from "vue";
import { MMAPI } from "../../../mixins/api";
import axios from "axios";

const router = useRouter();
let token = /access_token=([^&]+)/.exec(document.location.hash)![1];
const exception = ref();

if (token !== undefined) {
  axios
    .get(
      "https://login.yandex.ru/info?format=json&jwt_secret=73a87743fe2e406d96d537209a21c1c0&oauth_token=" +
        token
    )
    .then(async (res) => {
      let response = await MMAPI.logIn(res.data.emails[0], res.data.client_id);
      console.log(res.data);
      console.log(response)

      // user not created
      if (response.code === 404)
        response = await MMAPI.registerUser(
          res.data.emails[0],
          res.data.client_id,
          res.data.first_name,
          res.data.last_name,
          res.data.emails[0]
        );
      // successfully logged in
      useUser().config.api.setToken(response.access_token);
      useUser().config.username = res.data.emails[0];
      console.log(response);
      console.log(await MMAPI.getUserById(response.id));

      useUser().config.user = await MMAPI.getUserById(response.id);
      router.push("/app");
    })
    .catch((err) => console.error(err));

  // signUp-ya
  // app
} else {
  router.push("/");
}
</script>

<style scoped></style>
