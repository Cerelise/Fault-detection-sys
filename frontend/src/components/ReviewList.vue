<template>
	<div>
		<p
			v-if="!store.reviewsContent || store.reviewsContent.length === 0"
			class="text-[#ccc]"
		>
			现在还没有评论
		</p>
		<div v-else class="reviewList">
			<ReviewItem
				v-for="(item, index) in store.reviews"
				:key="index"
				:item="item"
			/>
		</div>
	</div>
</template>

<script setup>
import ReviewItem from './ReviewItem.vue'
import { useReviewsStore } from '../store/reviews'

const store = useReviewsStore()
</script>

<style scoped></style>
