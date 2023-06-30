import { createRouter, createWebHistory } from 'vue-router'

const routes = [
	{
		path: '/',
		name: 'home',
		component: () => import('../views/HomeView.vue'),
	},
	{
		path: '/models',
		name: 'models',
		component: () => import('../views/ModelView.vue'),
	},
	{
		path: '/visual',
		name: 'visual',
		component: () => import('../views/VisualView.vue'),
	},
	{
		path: '/rate',
		name: 'rate',
		component: () => import('../views/RateView.vue'),
	},
]

const router = createRouter({
	history: createWebHistory(),
	routes,
})

export default router
