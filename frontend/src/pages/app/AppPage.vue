<template>
  <main
    class="w-full h-full flex flex-col bg-lwhite items-center justify-center"
  >
    <p class="text-4xl">Here is app page</p>
    <p class="text-sm">
      {{ yaToken ? "yaToken founded in localStorage" : "yaToken is undefined" }}
    </p>
  </main>
</template>

<script setup lang="ts">
// INTERACT JS

const yaToken = localStorage.getItem("yaToken");
</script>
