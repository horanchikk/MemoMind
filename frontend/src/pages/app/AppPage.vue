<template>
  <main
    class="flex flex-col justify-center items-center w-full h-full bg-lwhite"
  >
    <p class="text-4xl">В разработке)😁</p>
    <p class="text-sm">
      {{ yaToken ? "yaToken founded in localStorage" : "yaToken is undefined" }}
    </p>
  </main>
</template>

<script setup lang="ts">
// INTERACT JS

const yaToken = localStorage.getItem("yaToken");
</script>
