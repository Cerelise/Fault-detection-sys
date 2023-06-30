<template>
	<Card>
		<form @submit.prevent="handleSubmit">
			<h2 class="text-xl font-semibold text-center">
				您对这个系统的评分与建议是什么？
			</h2>
			<!-- Reating Component -->
			<RatingSelect :rating="rating" @setRating="setRating" />
			<div
				class="flex flex-row border-2 border-solid border-slate-400 rounded-lg px-1 py-1"
			>
				<input
					class="rounded-lg mr-1"
					type="text"
					placeholder="请输入评论"
					v-model="text"
				/>
				<button type="submit" class="btn btn-primary" :disabled="btnDisabled">
					提交
				</button>
			</div>
			<div v-if="message != ''" class="pt-1 text-center text-red-500">
				{{ message }}
			</div>
		</form>
	</Card>
</template>

<script setup>
import Card from './shared/Card.vue'
import RatingSelect from './RatingSelect.vue'
import { storeToRefs } from 'pinia'
import { ref, watch } from 'vue'
import { useReviewsStore } from '../store/reviews'

const store = useReviewsStore()
const text = ref('')
const btnDisabled = ref(false)
const message = ref('请至少输入10个字以上的评论')
const rating = ref(10)

const { editedContent } = storeToRefs(store)

watch(editedContent, (newData) => {
	if (newData.editable) {
		text.value = newData.item.text
		rating.value = newData.item.rating
	}
})

watch(text, (newVal) => {
	if (newVal.trim().length <= 10) {
		btnDisabled.value = true
		message.value = '请至少输入10个字以上的评论'
	} else {
		btnDisabled.value = false
		message.value = ''
	}
})

const setRating = (val) => {
	rating.value = val
}

const handleSubmit = () => {
	const newReview = {
		text: text.value,
		rating: rating.value,
	}
	if (!store.editedContent.editable) {
		store.addReview(newReview)
	} else {
		store.updateReview({
			...newReview,
			id: store.editedContent.item.id,
		})
	}
	text.value = ''
}
</script>
