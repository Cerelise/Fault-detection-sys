<template>
	<div class="home">
		<div class="container">
			<!-- Reviews Form -->
			<ReviewForm />
			<!-- Reviews Stats -->
			<ReviewStats />
			<!-- Review List -->
			<ReviewList />
		</div>
	</div>
</template>

<script setup>
import ReviewForm from '../components/ReviewForm.vue'
import ReviewList from '../components/ReviewList.vue'
import ReviewStats from '../components/ReviewStats.vue'
import { onMounted } from 'vue'
import { useReviewsStore } from '../store/reviews'

const store = useReviewsStore()
onMounted(() => {
	store.fetchReviews()
})
</script>
