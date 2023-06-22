<script setup lang="ts">
import { ref, computed } from "vue";

const email = "test@gmail.com";
//const email = ref(); Email adress has to come from Backend

</script>

<template>
<body class="bg-gray-100 min-h-screen">
<div>
  <header>
      <div>
          <h1 class="text-center text-5xl pt-[249px] font-justMeAgainDownHere">fastnotes</h1>
      </div>
      <div class="text-center mt-10">
          <h1 class="mt-[39px] font-inter font-light text-sm inline">Hi </h1>
          <h1 class="inline font-inter text-sm inline">{{ email }}</h1>
          <h1 class="inline font-inter font-light text-sm inline">, do you want to reset your password? </h1>
          <p class="mt-[30px] font-inter font-light text-sm">Just tap the button below:</p>
      </div>
      <div class="text-center">
          <button type="submit" class="border rounded-xl bg-blue-600 w-96 ml-auto mr-auto h-12 mt-14 text-white font-inter font-light text-sm hover:bg-blue-700 active:bg-blue-800">Reset Password</button>
      </div>
      <div class="w-[360px] mx-auto text-center">
          <p class="mt-[101px] font-inter font-light text-sm">If you didn't request this, you can delete this message and carry on as you were.</p>
          <div class="mt-10">
            <h1 class="inline font-inter font-light text-sm">-Kindly your </h1>
            <h1 class="inline font-justMeAgainDownHere font-light">fastnotes </h1>
            <h1 class="inline font-inter font-light text-sm">Team</h1>
          </div>
      </div>
  </header>
  <main>

  </main>
</div>
</body>
</template>

<style scoped>
</style>
