<script setup lang="ts">
import { ref, computed } from "vue";

const password = ref();
const confirmPassword = ref();
const passwordsMatch = computed(() => {
    return password.value === confirmPassword.value;
});
</script>

<template>
<div class="bg-gray-100 min-h-screen">
<div>
  <header>
      <div>
          <h1 class="text-center pt-3 font-justMeAgainDownHere">fastnotes</h1>
          <h2 class="text-center text-3xl mt-40 mb-16 font-justMeAgainDownHere text-4xl">Get Started</h2>
      </div>
  </header>
  <main>
      <div class="border rounded-xl mx-auto py-8 bg-white shadow-xl" style="width: 650px">                                             <!--Outer Frame Div-->
          <div>
              <h1 class="text-center mb-6 text-3xl font-justMeAgainDownHere">Your place to take Notes in Peace</h1>
          </div>
          <div>                                                                                                                         <!--Form input Div-->
              <div class="w-[365px] mx-auto">
                  <form class="flex flex-col my-1">
                    <label for="e-mail" class="text-xs font-normal not-italic pb-1 font-inter">E-Mail</label>
                    <input type="email" id="e-mail" class="border border-gray-400 rounded h-8">
                  </form>
                  <form class="flex flex-col my-1">
                    <label for="password" class="text-xs font-normal not-italic pb-1 font-inter">Password</label>
                    <input type="password" id="password" v-model="password" class="border border-gray-400 rounded block h-8">
                  </form>
                  <form class="flex flex-col my-1">
                    <label for="confirm-password" :class="{ 'text-red-500': !passwordsMatch }" class="text-xs font-normal not-italic pb-1 font-inter">Confirm Password</label>
                    <input type="password" id="confirm-password" v-model="confirmPassword" :class="{ 'border-red-500': !passwordsMatch }" class="border border-gray-400 rounded block h-8">
                  </form>
                  <div class="h-1 pt-1">
                      <span class="font-light text-xs text-red-600" v-show="!passwordsMatch">Password fields don't match</span>
                  </div>
                  <div>
                      <button type="submit" :class="{ 'pointer-events-none bg-gray-400 hover:bg-gray-400': !passwordsMatch}" class="border rounded-xl bg-blue-600 w-full h-12 mt-10 text-white font-light hover:bg-blue-700 active:bg-blue-800">Register</button>
                  </div>
              </div>
          </div>
      </div>
  </main>
</div>
</div>
</template>

<style scoped>
</style>
