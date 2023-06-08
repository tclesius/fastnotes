import {defineStore} from 'pinia';
import {Body_signin, OpenAPI, UserCreate, UserRead, UsersService} from "../client";
import {computed, ref} from "vue";

export const useAuthStore = defineStore('auth', () => {
  const user = ref<UserRead | null>(null);
  const isAuthenticated = computed(() => !!OpenAPI.TOKEN);

  async function signUp(userCreate: UserCreate) {
    user.value = await UsersService.signup(userCreate)
  }

  async function signIn(formData: Body_signin) {
      const response = await UsersService.signin(formData);
      localStorage.setItem('token', response.access_token)
      OpenAPI.TOKEN = response.access_token
  }
  async function signOut() {
    OpenAPI.TOKEN = null;
    user.value = null;
  }
  async function getCurrentUser() {
    if(OpenAPI.TOKEN == null) OpenAPI.TOKEN = localStorage.getItem('token')
    user.value = await UsersService.getCurrentUser()
  }
  return { user, isAuthenticated, getCurrentUser, signUp, signIn, signOut };
});
