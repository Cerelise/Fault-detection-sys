import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import router from './router'
import './assets/main.css'
import App from './App.vue'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(createPinia()).use(router).mount('#app')
