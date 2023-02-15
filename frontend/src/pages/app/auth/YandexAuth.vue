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
    <p>{{ token ? "Token is finded" : "Token not found" }}</p>
  </div>
</template>

<script setup lang="ts">
import router from "../../../router";

let token = /access_token=([^&]+)/.exec(document.location.hash)![1];

setTimeout(() => {
  if (token !== undefined) {
    localStorage.setItem("yaToken", token);
    router.push("/app");
  } else {
    router.push("/");
  }
}, 5000);
</script>

<style scoped></style>
