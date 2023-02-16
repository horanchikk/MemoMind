<template>
  <!-- eslint-disable -->
  <!-- we'll fix it later -->
  <header class="flex flex-col px-32 pt-2 w-full text-xl font-semibold h-fit">
    <div class="flex justify-between items-center px-24 w-full">
      <div class="flex gap-5 justify-between items-center">
        <img src="../assets/icon.svg" class="h-7 w-fit" alt="Icon" />
      </div>
      <div class="flex gap-20 justify-between">
        <router-link
          to="/app/auth/signIn"
          class="transition-all cursor-pointer select-none hover:text-primary"
        >
          Вход
        </router-link>
        <router-link
          to="/app/auth/signUp"
          class="transition-all cursor-pointer select-none hover:text-primary"
        >
          Регистрация
        </router-link>
      </div>
    </div>
    <div
      class="border-b-[1px] border-black border-opacity-40 mt-3 mb-0 rounded-full"
    ></div>
  </header>
  <main class="flex overflow-y-scroll flex-col flex-auto select-none">
    <div
      class="flex flex-col gap-5 justify-center items-center py-20 bg-white bgdark"
    >
      <div class="flex flex-col text-[40px] text-black">
        <img
          src="../assets/title.svg"
          class="-mb-5 pointer-events-none"
          alt="title"
        />
        <p>Миллионы ваших идей в одном месте</p>
      </div>
      <router-link
        to="/app/auth/signUp"
        class="px-8 py-4 font-bold text-2xl -mb-8 rounded-xl border-[3px] border-black hover:border-white hover:text-white hover:bg-black active:scale-95 transition-all"
      >
        Присоединиться сейчас
      </router-link>
      <img
        src="../assets/heroes.svg"
        class="pointer-events-none"
        alt="heroes"
      />
    </div>

    <div
      class="flex gap-48 justify-between items-center px-72 py-20 h-screen bg-lwhite"
    >
      <div class="flex flex-col gap-5">
        <div
          class="flex flex-col px-1 text-3xl font-semibold bg-white rounded-md"
        >
          <p class="flex justify-start">Контролируйте свои</p>
          <div class="flex gap-5 justify-start items-center">
            <p>задачи</p>
            <img
              src="../assets/bubliki.svg"
              class="pointer-events-none"
              alt="bibliki"
            />
          </div>
        </div>
        <div class="text-xl font-light">
          Контролируйте прогресс текущих задач по Вашим проектам с помощью
          досок!
        </div>
        <img src="../assets/heroes2.svg" alt="heroes2" />
      </div>
      <div class="w-full hover:scale-105 transition-all">
        <img
          src="../assets/screen1.svg"
          class="pointer-events-none"
          alt="screen1"
        />
      </div>
    </div>
    <div
      class="w-full px-72 py-24 h-fit flex items-center justify-center bg-lwhite"
    >
      <img src="../assets/woah.svg" class="pointer-events-none" alt="screen1" />
    </div>
    <div
      class="flex flex-row-reverse gap-48 justify-between items-center px-72 py-20 h-screen bg-lwhite"
    >
      <div class="flex flex-col gap-5">
        <div
          class="flex flex-col px-1 text-3xl font-semibold bg-white rounded-md"
        >
          <p class="flex justify-start">Храните все Ваши идеи</p>
          <div class="flex gap-5 justify-start items-center">
            <p>в одном месте</p>
            <img
              src="../assets/sun.svg"
              class="pointer-events-none"
              alt="sun"
            />
          </div>
        </div>
        <div class="text-xl font-light">
          Храните и редактируйте Ваши идеи с помощью профессиональных
          инструментов, предоставляемых MemoMind
        </div>
        <img
          src="../assets/heroes3.svg"
          class="pointer-events-none"
          alt="heroes3"
        />
      </div>
      <div class="w-full hover:scale-105 transition-all">
        <img
          src="../assets/screen2.svg"
          class="w-full pointer-events-none"
          alt="screen1"
        />
      </div>
    </div>
    <div
      class="flex flex-col gap-7 justify-center items-center px-[500px] py-20 h-screen bg-lwhite"
    >
      <h1 class="font-bold text-5xl text-center">
        <span class="text-primary">Бесконечные</span> пути <br />
        для применения
      </h1>
      <router-link
        to="/app/auth/signUp"
        class="text-primary underline text-3xl font-bold hover:text-accent transition-all duration-100"
        >Посмотреть все шаблоны</router-link
      >
      <div class="grid grid-cols-3 gap-8 mt-10">
        <div
          class="col-span-2 flex flex-col gap-8 bg-[#E0E0E0] rounded-lg pt-8 pl-8 hover:scale-105 transition-all"
        >
          <div class="flex gap-5">
            <img
              src="../assets/courthouse.svg"
              class="pointer-events-none"
              alt="courthouse"
            />
            <p class="font-bold text-2xl">
              Информационное поле <br />
              вашей компании
            </p>
          </div>
          <img
            src="../assets/screen3.svg"
            class="h-full w-full pointer-events-none"
            alt="screen3"
          />
        </div>
        <div class="grid col-span-1 grid-rows-2 gap-8">
          <div
            class="grid grid-rows-3 bg-[#E0E0E0] rounded-lg pt-8 pl-8 hover:scale-105 transition-all"
          >
            <img
              src="../assets/flag.svg"
              class="pointer-events-none"
              alt="flag"
            />
            <p class="font-bold text-3xl">Дорожная карта</p>
            <router-link
              to="/app/auth/signUp"
              class="text-primary underline text-xl font-bold hover:text-accent transition-all duration-100"
              >Запустить шаблон</router-link
            >
          </div>
          <div
            class="grid grid-rows-3 bg-[#E0E0E0] rounded-lg pt-8 pl-8 hover:scale-105 transition-all"
          >
            <img
              src="../assets/tickcircle.svg"
              class="pointer-events-none"
              alt="tickcircle"
            />
            <p class="font-bold text-3xl">Цели компании</p>
            <router-link
              to="/app/auth/signUp"
              class="text-primary underline text-xl font-bold hover:text-accent transition-all duration-100"
              >Запустить шаблон</router-link
            >
          </div>
        </div>
      </div>
      <div class="text-xl px-10 py-5 font-bold text-center transition-all">
        <span class="opacity-70">“</span>MemoMind может
        <span class="text-accent">подстраиваться</span>
        под
        <soan class="text-primary">любую</soan>
        <br />
        вашу задачу<span class="opacity-70"
          >” - Хуан Си (Software Engineer в Google)</span
        >
      </div>
    </div>

    <div
      class="grid grid-cols-2 grid-rows-5 px-[500px] gap-7 justify-center items-center w-screen py-20 bg-lwhite"
    >
      <div
        class="col-span-2 row-span-3 bg-[#E0E0E0] rounded-lg p-8 flex flex-col gap-8 hover:scale-105 transition-all"
      >
        <img
          src="../assets/filtersquare.svg"
          class="w-[50px] h-[50px] pointer-events-none"
          alt="filtersquare"
        />
        <div class="text-2xl font-semibold">
          <span class="text-primary">Визуализируйте</span>,
          <span class="text-primary">фильтруйте</span> и
          <span class="text-primary">сортируйте</span> как вы <br />
          захотите
        </div>

        <img
          src="../assets/screen4.svg"
          class="flex-auto pointer-events-none"
          alt="screen4"
        />
      </div>
      <div
        class="w-full col-span-1 row-span-2 h-full hover:scale-105 transition-all"
      >
        <img
          src="../assets/fefe.svg"
          alt="set up some info"
          class="pointer-events-none"
        />
      </div>
      <div
        class="w-full col-span-1 row-span-2 h-full hover:scale-105 transition-all"
      >
        <img
          src="../assets/fefe2.svg"
          alt="create any pages"
          class="pointer-events-none"
        />
      </div>
    </div>
    <div
      class="flex flex-col items-center gap-10 px-[500px] justify-center w-screen py-20 bg-lwhite"
    >
      <router-link
        to="/app/auth/signUp"
        class="px-8 py-4 font-bold text-2xl -mb-8 rounded-xl border-[3px] border-black hover:border-white hover:text-white hover:bg-black active:scale-95 transition-all"
      >
        Присоединиться сейчас
      </router-link>
      <img
        src="../assets/debils.svg"
        class="pointer-events-none"
        alt="debils"
      />
    </div>
  </main>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();
</script>

<style>
.bgdark {
  filter: drop-shadow(0 48px 20px #fff);
}
</style>
