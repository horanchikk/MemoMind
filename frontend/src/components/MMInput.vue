<template>
  <input
    :value="modelValue"
    class="outline-0 border-black border-[1px] py-1 px-5 rounded-md cursor-pointer border-opacity-40 focus:border-opacity-100 transition-all"
    @input="
      $emit(
        'update:modelValue',
        $event && $event.target && ($event.target as HTMLTextAreaElement).value
      )
    "
  />
</template>

<script setup lang="ts">
defineEmits(["update:modelValue"]);
defineProps(["modelValue"]);
</script>
