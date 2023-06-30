<template>
	<Card>
		<button class="close" @click="store.deleteReview(item)">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				stroke-width="1.5"
				stroke="currentColor"
				class="w-2 h-2"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M6 18L18 6M6 6l12 12"
				/>
			</svg>
		</button>
		<button class="edit" @click="store.editReview(item)">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				stroke-width="1.5"
				stroke="currentColor"
				class="w-2 h-2"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10"
				/>
			</svg>
		</button>
		<!-- class="num-display relative p-1 w-5 h-5 rounded-[25px] text-lg border border-[#ccc]" -->
		<div
			class="relative p-1 w-5 h-5 rounded-[25px] text-lg text-center num-display"
		>
			{{ item.rating }}
		</div>
		<div class="text-display">
			{{ item.text }}
		</div>
	</Card>
</template>

<script setup>
import Card from './shared/Card.vue'
import { useReviewsStore } from '../store/reviews'

const store = useReviewsStore()

defineProps({
	item: {
		type: Object,
	},
})
</script>

<style scoped>
.num-display {
	background: #4ecca3;
	color: #fff;
	position: absolute;
	top: -15px;
	left: -20px;
	transition: 0.3s;
}

.close,
.edit {
	position: absolute;
	top: 10px;
	right: 20px;
	cursor: pointer;
	background: none;
	border: none;
}

.edit {
	right: 45px;
}
</style>
