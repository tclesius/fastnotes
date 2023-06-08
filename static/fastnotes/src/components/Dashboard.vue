<script setup>
import { computed, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';
import {OpenAPI} from "../client";
import {storeToRefs} from "pinia";

const authStore = useAuthStore()

const router = useRouter();

const logout = async () => {
  await authStore.signOut();
  await router.push('/');
};

onMounted(authStore.getCurrentUser);
</script>

<template>
  <div>
    <h1 class="text-3xl font-bold">Dashboard</h1>
    <p v-if="authStore.user">Welcome, {{ authStore.user.username }}!</p>
    <p v-if="authStore.user">Email: {{ authStore.user.email }}</p>
    <button @click="logout" class="px-4 py-2 mt-4 bg-red-500 text-white rounded-md">Logout</button>
  </div>
</template>

<style scoped>
/* Add your custom styles here */
</style>
