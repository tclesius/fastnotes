<script setup lang="ts">
import { ref, computed } from "vue";

const password = ref();
const confirmPassword = ref();
const passwordsMatch = computed(() => {
    return password.value === confirmPassword.value;
});
</script>

<template>
<body class="bg-gray-100 min-h-screen">
<div>
  <header>
      <div>
          <h1 class="text-center pt-3 font-justMeAgainDownHere">fastnotes</h1>
          <h2 class="text-center text-4xl font-justMeAgainDownHere mt-40 mb-16">Reset your Password</h2>
      </div>
  </header>
  <main>
      <div class="border rounded-xl mx-auto py-8 bg-white shadow-xl" style="width: 650px">                                             <!--Outer Frame Div-->
          <div class="text-center mt-10">
              <h1 class="font-inter text-xs inline">Tip: </h1>
              <h1 class="font-inter font-light text-xs inline">Strong passwords include</h1>
              <h1 class="font-inter font-light text-xs mt-3">numbers, letters and punctuation marks.</h1>
          </div>
          <div>                                                                                                                       <!--Form input Div-->
              <div class="mx-32 mt-[44px]">
                  <form class="flex flex-col my-1">
                    <label for="password" class="text-xs font-normal not-italic pb-1 font-inter">Password</label>
                    <input v-model="password" type="password" id="password" class="border border-gray-400 rounded h-8">
                  </form>
                  <form class="flex flex-col mt-[12px]">
                    <label for="confirm-Password" :class="{ 'text-red-500': !passwordsMatch }" class="text-xs font-normal not-italic pb-1 font-inter">Confirm Password</label>
                    <input v-model="confirmPassword" type="password" id="confirm-Password" :class="{ 'border-red-500': !passwordsMatch}" class="border border-gray-400 rounded h-8">
                  </form>
                  <div class="h-12 pt-3">
                      <span class="font-light text-xs text-red-600" v-show="!passwordsMatch">Password fields don't match</span>
                  </div>
                  <div>
                      <button type="submit" :class="{ 'pointer-events-none bg-gray-400': !passwordsMatch}" class="font-inter text-sm border rounded-xl bg-blue-600 w-full h-12 mt-[24px] mb-4 text-white font-light hover:bg-blue-700 active:bg-blue-800">Reset Password</button>
                  </div>
              </div>
          </div>
      </div>
  </main>
</div>
</body>
</template>

<style scoped>
</style>
