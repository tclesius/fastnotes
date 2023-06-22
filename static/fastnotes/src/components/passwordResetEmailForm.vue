<script setup lang="ts">
import { computed } from "vue";
const resetSuccess = computed(() => {
    return false
})
</script>

<template>
<body class="bg-gray-100 min-h-screen">
<div>
  <header>
      <div>
          <h1 class="text-center pt-3 font-justMeAgainDownHere">fastnotes</h1>
          <h2 class="text-center text-4xl font-justMeAgainDownHere mt-40 mb-12">Request to reset your Password</h2>
      </div>
  </header>
  <main>
      <div class="border rounded-xl mx-auto py-8 bg-white shadow-xl" style="width: 650px">                                             <!--Outer Frame Div-->
          <div class="text-center mt-10">
              <h1 class="font-inter text-xs inline">Lost your Password? </h1>
              <h1 class="font-inter font-light text-xs inline">Please enter your email adress.</h1>
              <h1 class="font-inter font-light text-xs mt-3">You will receive a link to create a new password via email.</h1>
          </div>
          <div>                                                                                                                       <!--Form input Div-->
              <div class="mx-32 mt-[44px]">
                  <form class="flex flex-col my-1">
                    <label for="e-mail" class="text-xs font-normal not-italic pb-1 font-inter">E-Mail</label>
                    <input type="email" id="e-mail" class="border border-gray-400 rounded h-8">
                  </form>
                  <div>
                      <button type="submit" class="font-inter text-sm border rounded-xl bg-blue-600 w-full h-12 mt-[24px] text-white font-light hover:bg-blue-700 active:bg-blue-800">Reset Password</button>
                  </div>
                  <div class="h-24">
                      <div class="text-center pt-10" v-show="resetSuccess">
                          <h1 class="inline font-inter font-medium text-green-600 text-xs">Email send! </h1>
                          <h1 class="inline font-inter text-green-600 text-xs">Check your inbox.</h1>
                      </div>
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
