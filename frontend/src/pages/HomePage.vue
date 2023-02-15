<template>
  <header class="w-full h-fit pt-2 px-32 flex flex-col font-semibold text-2xl">
    <div class="flex justify-between items-center w-full px-12">
      <div class="flex justify-between items-center gap-5">
        <img src="../assets/icon.svg" alt="Icon" />
        <p class="tracking-widest select-none text-3xl">MemoMind</p>
      </div>
      <div class="flex justify-between gap-20">
        <router-link
          to="/app/auth/signIn"
          class="hover:text-primary transition-all cursor-pointer select-none"
        >
          Вход
        </router-link>
        <router-link
          to="/app/auth/signUp"
          class="hover:text-primary transition-all cursor-pointer select-none"
        >
          Регистрация
        </router-link>
      </div>
    </div>
    <div
      class="border-b-[1px] border-black border-opacity-40 mt-3 mb-0 rounded-full"
    ></div>
  </header>
  <main
    class="flex-auto flex flex-col gap-20 bg-white px-32 overflow-y-scroll select-none py-20"
  >
    <section
      class="w-full flex items-center py-44 text-2xl font-semibold justify-center gap-10"
    >
      <div>What is MemoMind? (did like tree in Miro!!)</div>
    </section>
    <section class="w-full flex justify-between items-center gap-10">
      <div class="flex flex-col gap-5 w-1/2">
        <h1 class="font-bold text-2xl">Keep all your ideas in one place 💡</h1>
        <p class="font-medium text-xl">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam
          quibusdam nobis deleniti quia asperiores impedit voluptatem nisi
          laudantium accusamus quaerat blanditiis quae, hic omnis neque corrupti
          eligendi nesciunt iusto quas minima consequuntur facere! Velit
          consequatur voluptate aperiam a at veritatis! Commodi quidem
          necessitatibus quas soluta praesentium sapiente sequi exercitationem
          ducimus enim ipsa eius nesciunt odio obcaecati, iusto dignissimos,
          doloremque voluptatum.
        </p>
        <MMButton transparent class="w-fit p-2">hello</MMButton>
      </div>
      <div class="w-1/2">
        <img src="../assets/test.png" class="w-full h-full" alt="test" />
      </div>
    </section>
    <section
      class="w-full flex flex-row-reverse justify-between items-center gap-10"
    >
      <div class="flex flex-col gap-5 w-1/2">
        <h1 class="font-bold text-2xl">Keep all your ideas in one place 💡</h1>
        <p class="font-medium text-xl">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam
          quibusdam nobis deleniti quia asperiores impedit voluptatem nisi
          laudantium accusamus quaerat blanditiis quae, hic omnis neque corrupti
          eligendi nesciunt iusto quas minima consequuntur facere! Velit
          consequatur voluptate aperiam a at veritatis! Commodi quidem
          necessitatibus quas soluta praesentium sapiente sequi exercitationem
          ducimus enim ipsa eius nesciunt odio obcaecati, iusto dignissimos,
          doloremque voluptatum.
        </p>
        <MMButton transparent class="w-fit p-2">hello</MMButton>
      </div>
      <div class="w-1/2">
        <img src="../assets/test.png" class="w-full h-full" alt="test" />
      </div>
    </section>
    <section
      class="w-full flex flex-row-reverse justify-between items-center gap-10"
    >
      <div class="flex flex-col gap-5 w-1/2">
        <h1 class="font-bold text-2xl">Keep all your ideas in one place 💡</h1>
        <p class="font-medium text-xl">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam
          quibusdam nobis deleniti quia asperiores impedit voluptatem nisi
          laudantium accusamus quaerat blanditiis quae, hic omnis neque corrupti
          eligendi nesciunt iusto quas minima consequuntur facere! Velit
          consequatur voluptate aperiam a at veritatis! Commodi quidem
          necessitatibus quas soluta praesentium sapiente sequi exercitationem
          ducimus enim ipsa eius nesciunt odio obcaecati, iusto dignissimos,
          doloremque voluptatum.
        </p>
        <MMButton class="w-fit p-2">hello</MMButton>
      </div>
      <div class="w-1/2">
        <img src="../assets/test.png" class="w-full h-full" alt="test" />
      </div>
    </section>
    <section class="w-full flex justify-between items-center gap-10">
      <div class="flex flex-col gap-5 w-1/2">
        <h1 class="font-bold text-2xl">Keep all your ideas in one place 💡</h1>
        <p class="font-medium text-xl">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam
          quibusdam nobis deleniti quia asperiores impedit voluptatem nisi
          laudantium accusamus quaerat blanditiis quae, hic omnis neque corrupti
          eligendi nesciunt iusto quas minima consequuntur facere! Velit
          consequatur voluptate aperiam a at veritatis! Commodi quidem
          necessitatibus quas soluta praesentium sapiente sequi exercitationem
          ducimus enim ipsa eius nesciunt odio obcaecati, iusto dignissimos,
          doloremque voluptatum.
        </p>
        <MMButton transparent class="w-fit p-2">hello</MMButton>
      </div>
      <div class="w-1/2">
        <img src="../assets/test.png" class="w-full h-full" alt="test" />
      </div>
    </section>
    <footer class="w-full flex justify-center text-2xl">
      <MMButton class="px-10 text-2xl">Зарегистрироваться сейчас</MMButton>
    </footer>
  </main>
</template>

<script setup lang="ts">
import MMButton from "../components/MMButton.vue";
import router from "../router";
</script>
