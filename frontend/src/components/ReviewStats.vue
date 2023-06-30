<template>
	<!-- feedback-stats -->
	<div class="text-white flex justify-between align-center">
		<h4>{{ store.reviewsCount ? store.reviewsCount : 'No' }} 评分</h4>
		<h4>
			平均评分：{{ isNaN(store.averageRating) ? 0 : store.averageRating }}
		</h4>
	</div>
</template>

<script setup>
import { useReviewsStore } from '../store/reviews'

const store = useReviewsStore()
</script>
