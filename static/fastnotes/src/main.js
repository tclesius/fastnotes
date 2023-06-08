import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import { OpenAPI } from './client';
import './assets/main.css';
import router from "./routers/router";

OpenAPI.BASE = 'http://localhost:8000';

const pinia = createPinia();
const app = createApp(App);

app.use(pinia);
app.use(router)

app.mount('#app');
