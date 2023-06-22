<script setup>
import {ref} from 'vue';
import {useAuthStore} from '../stores/auth';
import router from '../routers/router';

const loginFailed = ref(false);
const formData = ref({
  email: '',
  password: ''
});

const authStore = useAuthStore();
const {isAuthenticated} = authStore;

const handleLogin = async () => {
  try {
    const response = await authStore.signIn(formData.value);
    // Handle successful login, e.g., redirect to dashboard
    await router.push('/dashboard');
  } catch (error) {
    // Handle login error, e.g., display error message
    console.error(error);
    loginFailed.value = true;
  }
};

if (isAuthenticated.value) {
  router.push('/dashboard');
}
</script>

<template>
  <div class="bg-gray-100 min-h-screen">
    <header>
      <div>
        <h1 class="text-center pt-3 font-justMeAgainDownHere">fastnotes</h1>
        <h2 class="text-center text-4xl font-justMeAgainDownHere uppercase mt-40 mb-16">Login</h2>
      </div>
    </header>
    <main>
      <div class="border rounded-xl mx-auto py-8 bg-white shadow-xl" style="width: 650px">
        <div>
          <h1 class="w-[365px] pb-2 mx-auto mb-7 text-3xl font-justMeAgainDownHere">Your place to take Notes in Peace</h1>
        </div>
        <div class="w-[365px] mx-auto">
          <form action="#" class="space-y-4 md:space-y-3">
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="email">E-mail</label>
              <input id="email" class="border border-gray-300 text-gray-900 sm:text-sm rounded-md focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" name="email"
                     placeholder="name@fastnotes.com"
                     required="" type="email">
            </div>
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                     for="password">Password</label>
              <input id="password" class=" border border-gray-300 text-gray-900 sm:text-sm rounded-md focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" name="password" placeholder="••••••••"
                     required=""
                     type="password">
            </div>
            <div class="pb-4 flex justify-end">
              <a class="text-xs font-medium text-primary-600 hover:underline dark:text-primary-500" href="#">Forgot
                password?</a>
            </div>
            <button class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                    type="submit">
              Sign in
            </button>
            <p class="pb-5 text-sm dark:text-gray-400">
              Don’t have an account yet? <a class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                                            href="#">Get started</a>
            </p>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
</style>


