<template>
  <button
    :class="`rounded-md text-md p-2 ${
      transparent === true
        ? 'bg-none text-primary text-bold hover:bg-primary hover:bg-opacity-10 active:bg-opacity-20 active:scale-95 transition-all'
        : 'text-white bg-accent hover:bg-primary active:opacity-80 active:scale-95 transition-all'
    }`"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
const { transparent = false } = defineProps<{
  transparent?: boolean;
}>();
</script>
