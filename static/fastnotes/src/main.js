import Vue, { createApp } from '@vue/compat';
import { createPinia } from 'pinia'
import { BootstrapVue, IconsPlugin, ButtonPlugin } from 'bootstrap-vue'
import App from './App.vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import {OpenAPI} from "./client";

OpenAPI.BASE = 'http://localhost:8000';

const pinia = createPinia()
const app = createApp(App)

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(ButtonPlugin)
Vue.use(pinia)

app.mount('#app');