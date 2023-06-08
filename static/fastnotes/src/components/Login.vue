<script setup>
import { ref } from 'vue';
import {useAuthStore} from "../stores/auth";
import router from "../routers/router";

const formData = ref({
  username: '',
  password: ''
});

const authStore = useAuthStore()

const { isAuthenticated, user } = authStore;

const handleLogin = async () => {
  try {
    const response = await authStore.signIn(formData.value);
    // Handle successful login, e.g., redirect to dashboard
    await router.push('/dashboard'); // Replace '/dashboard' with your desired route
  } catch (error) {
    // Handle login error, e.g., display error message
    console.error(error);
  }
};

if (isAuthenticated.value) {
  router.push('/dashboard');
}
</script>


<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-md w-full p-6 bg-white shadow-lg rounded-md">
      <h2 class="text-2xl font-bold mb-6">Login</h2>
      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
          <input type="text" id="username" v-model="formData.username" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
        </div>
        <div class="mb-4">
          <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
          <input type="password" id="password" v-model="formData.password" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
        </div>
        <div>
          <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">Login</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
/* Add your custom styles here */
</style>
