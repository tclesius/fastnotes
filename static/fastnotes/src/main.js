import Vue, {createApp} from '@vue/compat';
import {createPinia} from 'pinia'
import {BootstrapVue, IconsPlugin, ButtonPlugin} from 'bootstrap-vue'
import App from './App.vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import {OpenAPI} from "./client";
import {createRouter, createWebHashHistory} from "vue-router";
import NavBar from "./components/NavBar.vue";
import NoteCreate from "./components/NoteCreate.vue";
import Notes from "./components/Notes.vue";

OpenAPI.BASE = 'http://localhost:8000';

const pinia = createPinia()
const app = createApp(App)

const routes = [                    //Hier werden Routes für Vue-Router erzeugt
    {path: "/", component: NavBar},
    {path: "/NoteCreate", component: NoteCreate},
    {path: "/Notes", component: Notes}]

const router = createRouter({
    history: createWebHashHistory(), routes: routes, linkActiveClass: "active"
})

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(ButtonPlugin)
Vue.use(pinia)
app.use(router)

app.mount('#app');