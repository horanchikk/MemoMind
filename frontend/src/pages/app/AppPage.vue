<template>
  <main class="flex w-full h-full" v-if="user.config.username">
    <!-- popup -->
    <Transition name="opacity" mode="out-in">
      <div
        class="fixed flex items-center justify-center z-50 top-0 left-0 bg-black bg-opacity-60 w-full h-full"
        v-show="modal.show"
      >
        <Transition name="popup" mode="out-in">
          <div
            class="w-fit h-fit flex flex-col gap-5 bg-lwhite rounded-lg shadow-md p-2"
            ref="popupWindow"
            v-show="modal.show"
          >
            <div class="w-full flex justify-between gap-5 items-center">
              <div class="w-10 h-10"></div>
              <p class="text-xl font-semibold select-none">
                {{ modal.title }}
              </p>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                @click="modal.show = !modal.show"
                width="2.5rem"
                height="2.5rem"
                class="hover:opacity-70 active:opacity-50 transition-all duration-75 cursor-pointer select-none"
                viewBox="0 0 24 24"
              >
                <g fill="none">
                  <path
                    d="M24 0v24H0V0h24ZM12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035c-.01-.004-.019-.001-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427c-.002-.01-.009-.017-.017-.018Zm.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093c.012.004.023 0 .029-.008l.004-.014l-.034-.614c-.003-.012-.01-.02-.02-.022Zm-.715.002a.023.023 0 0 0-.027.006l-.006.014l-.034.614c0 .012.007.02.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01l-.184-.092Z"
                  />
                  <path
                    fill="currentColor"
                    d="M12 2c5.523 0 10 4.477 10 10s-4.477 10-10 10S2 17.523 2 12S6.477 2 12 2Zm0 2a8 8 0 1 0 0 16a8 8 0 0 0 0-16ZM9.879 8.464L12 10.586l2.121-2.122a1 1 0 1 1 1.415 1.415l-2.122 2.12l2.122 2.122a1 1 0 0 1-1.415 1.415L12 13.414l-2.121 2.122a1 1 0 0 1-1.415-1.415L10.586 12L8.465 9.879a1 1 0 0 1 1.414-1.415Z"
                  />
                </g>
              </svg>
            </div>
            <main class="flex-auto">
              <section v-show="modal.add" class="flex justify-between gap-5">
                <div class="p-2">
                  <MMButton
                    :transparent="false"
                    class="text-xl"
                    @click="
                      modal.show = false;
                      createNote();
                    "
                    >Создать страницу</MMButton
                  >
                </div>
                <div class="p-2">
                  <MMButton
                    :transparent="false"
                    class="text-xl"
                    @click="
                      modal.show = false;
                      createDesk();
                    "
                    >Создать доску</MMButton
                  >
                </div>
              </section>
              <section v-show="!modal.add" class="font-bold p-5">
                <!-- TODO -->
                Настройки аккаунта в разработке...
              </section>
            </main>
          </div>
        </Transition>
      </div>
    </Transition>
    <!-- left bar -->
    <div class="flex flex-col w-[222px] h-full bg-[#F2F2F2] relative show-left">
      <!-- icon -->
      <div
        class="w-full h-16 flex items-center justify-center cursor-pointer hover:scale-105 transition-all"
      >
        <router-link to="/">
          <img src="../../assets/icon.svg" class="w-full h-5" alt="icon" />
        </router-link>
      </div>
      <div class="flex-auto flex flex-col px-4 text-lg gap-4 overflow-y-scroll">
        <!-- notes/desks + trash -->
        <div class="flex flex-col gap-5">
          <!-- notes -->
          <p class="font-semibold cursor-default text-base">Страницы</p>
          <div v-if="user.config.user.notes.length > 0" class="flex flex-col">
            <TransitionGroup name="opacity">
              <div
                v-for="(note, index) in notes"
                :key="index"
                @click="selectNote(note.nid)"
                class="flex cursor-pointer select-none hover:opacity-100 px-2 py-1 hover:bg-black/10 rounded-md transition-all text-sm"
              >
                - {{ note.title }}
              </div>
            </TransitionGroup>
          </div>
          <div v-else class="text-sm">Страницы отстутствуют</div>
        </div>
        <div class="flex flex-col gap-5">
          <!-- desks -->
          <p class="font-semibold cursor-default text-base">Доски</p>
          <div v-if="user.config.user.desks.length > 0">
            <div
              v-for="(desk, index) in desks"
              :key="index"
              @click="selectDesk(desk.did)"
              class="flex cursor-pointer select-none hover:opacity-100 px-2 py-1 hover:bg-black/10 rounded-md transition-all text-sm"
            >
              - {{ desk.title }}
            </div>
          </div>
          <div v-else class="text-sm">Доски отстутствуют</div>
        </div>
        <button class="flex gap-4 items-center">
          <img src="../../assets/trash.svg" class="w-6 h-6" alt="trash" />
          <p class="font-semibold">Корзина</p>
        </button>
      </div>
      <!-- new page btn -->
      <button
        class="w-full opacity-70 border-t-[1px] bg-[#F2F2F2] border-black font-semibold border-opacity-70 flex items-center justify-center px-7 py-2 gap-3 text-xl hover:opacity-100 transition-all"
        @click="
          modal.show = true;
          modal.title = 'Создание страницы/доски';
          modal.add = true;
        "
      >
        <img src="../../assets/add.svg" class="w-5 h-5" alt="add" />
        <p>Добавить</p>
      </button>
    </div>
    <!-- main section -->
    <div class="flex-auto h-full flex flex-col" v-if="currentPage">
      <!-- header? -->
      <header
        class="w-full h-16 text-xl flex justify-between items-center px-8 bg-white show-down"
      >
        <div class="flex gap-4 cursor-default">
          <p class="text-2xl">😀</p>
          <p class="cursor-default">{{ currentPage.title }}</p>
        </div>
        <div class="flex gap-5">
          <img
            class="w-6 h-6 opacity-50 cursor-pointer hover:opacity-75 transition-all"
            src="../../assets/star1.svg"
            alt="star"
          /><img
            src="../../assets/exportsquare.svg"
            alt="exportsquare"
            class="w-6 h-6 opacity-50 cursor-pointer hover:opacity-75 transition-all"
          /><img
            src="../../assets/maximize4.svg"
            class="w-6 h-6 opacity-50 cursor-pointer hover:opacity-75 transition-all"
            alt="maximize"
          /><img
            src="../../assets/setting2.svg"
            class="w-6 h-6 opacity-50 cursor-pointer hover:opacity-75 transition-all"
            alt="setting2"
            @click="
              modal.show = !modal.show;
              modal.title = 'Настройки аккаунта';
            "
          />
        </div>
      </header>
      <main
        class="flex-auto flex flex-col overflow-y-scroll h-screen show-right"
      >
        <!-- gradient -->
        <div
          class="h-1/3 w-full bg-gradient-to-r from-green-300 via-blue-500 to-purple-600"
        >
          <div
            class="w-full h-full flex justify-end p-6 opacity-0 hover:opacity-100 transition-all"
          >
            <img
              src="../../assets/trash.svg"
              alt="Корзина"
              class="h-7 w-7 cursor-pointer"
              @click="removePage(currentPage.nid)"
            />
          </div>
        </div>
        <!-- smile of note -->
        <div class="text-end w-96 h-0.5 text-4xl text-align-center -my-5">
          😀
        </div>
        <!-- type place -->
        <div
          class="flex-auto w-full flex flex-col gap-8 items-start px-80 pt-20"
        >
          <div class="flex gap-5 w-full">
            <img
              src="../../assets/edit2.svg"
              class="w-10 h-10"
              alt="edit title)"
            />
            <input
              type="text"
              class="h-fit w-fit outline-0 border-0 opacity-80 focus:opacity-100 transition-all text-3xl"
              placeholder="Название страницы"
              v-model="currentPage.title"
            />
          </div>
          <!-- here is md -->
          <!-- https://www.youtube.com/watch?v=lXc0c1n6O-g -->
          <textarea
            class="flex-auto w-full outline-0 border-0 opacity-60 focus:opacity-100 transition-all text-xl"
            placeholder="Напишите что-нибудь здесь"
            v-model="currentPage.data"
          ></textarea>
        </div>
      </main>
    </div>
    <div
      class="flex-auto text-xl flex items-center justify-center bg-[#F2F2F2]"
      v-else
    >
      Выберите страницу/доску
    </div>
  </main>
</template>

<script setup lang="ts">
import { reactive, onMounted, ref, toRaw } from "vue";
import { useRouter } from "vue-router";
import { onClickOutside } from "@vueuse/core";

import { useUser } from "../../store/user";
import { MMAPI } from "../../mixins/api";

import MMInput from "../../components/MMInput.vue";
import MMButton from "../../components/MMButton.vue";

import type { Ref } from "vue";
import type { Note, Desk } from "../../mixins/api";

const currentType = ref(null);
const mdText = ref("");
const popupWindow = ref(null);

// interface addModal {
//   show: boolean;
//   select: {
//     noteDesk: boolean;
//   };
// }

const modal = reactive<{
  title: string;
  show: boolean;
  add: boolean;
}>({
  title: "",
  show: false,
  add: false,
});

const user = useUser();
const router = useRouter();

const notes: Ref<Array<Note>> = ref([]);
const desks: Ref<Array<Desk>> = ref([]);

const currentPage: Ref<Note | Desk | undefined> = ref(undefined);

if (!user.config.username) {
  router.push("/app/auth/signIn");
} else {
  console.log(user.config.username);
}

onMounted(() => {
  getAll();
});

async function createNote() {
  const note = await user.config.api.getNote(
    (
      await user.config.api.createNote("")
    ).id
  );
  console.log(user.config.user);
  user.config.user = await MMAPI.getUserById(user.config.user.uid);
  console.log(note);
  notes.value.push(note);
}

async function removePage(nid) {
  await user.config.api.deleteNote(nid);
  selectNote(currentPage.value.nid - 1);
  getAll();
}

async function createDesk() {
  const desk = await user.config.api.getDesk(
    (
      await user.config.api.createDesk("")
    ).did
  );
  user.config.user = await MMAPI.getUserById(user.config.user.uid);
  desks.value.push(desk);
}

async function selectNote(noteId: number) {
  if (currentPage.value) {
    await MMAPI.editNote(
      currentPage.value.nid,
      currentPage.value.title,
      currentPage.value.data,
      currentPage.value.cover,
      currentPage.value.gradient
    );
    notes.value[
      notes.value.indexOf(
        notes.value.find((n) => n.nid == currentPage.value.nid)
      )
    ].title = currentPage.value.title;
    getAll();
  }
  currentPage.value = await user.config.api.getNote(noteId);
}

async function selectDesk(deskId: number) {
  currentPage.value = await user.config.api.getDesk(deskId);
}

function getAll() {
  notes.value = [];

  user.config.user.notes.forEach((noteId) => {
    user.config.api.getNote(noteId).then((note) => {
      notes.value.push(note);
    });

    notes.value.sort((prevNote, nextNote) => {
      if (prevNote.nid < nextNote.nid) {
        return -1;
      }
      if (prevNote.nid > nextNote.nid) {
        return 1;
      }
      return 0;
    });
  });
  user.config.user.desks.forEach((deskId) => {
    user.config.api.getDesk(deskId).then((desk) => {
      // desks.value.push(desk);
    });
  });
}

onClickOutside(popupWindow, () => {
  if (modal.show) {
    modal.show = !modal.show;
  }
});
</script>

<style>
.editor {
  background-color: #050505;
  border-radius: 0.25em;
  padding: 1em;
}
</style>
