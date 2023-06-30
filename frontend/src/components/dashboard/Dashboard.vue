<template>
	<Card>
		<h1 class="text-3xl text-emerald-500">使用指南</h1>
		<div class="my-1">
			<p>
				1、选取想要用来生成模型的训练集上传，需要有标签数据，点击上传测试集，上传成功后等待执行，执行成功后点击下载训练模型进行模型下载。
			</p>
			<p>
				2、选取需要进行故障类型预测的测试集，点击上传测试集，支持单条或批量上传，执行成功后点击下载预测结果进行结果下载。
				（预测结果包含：样本ID和预测的类别）
			</p>
		</div>
		<div class="flex gap-5 justify-center items-center">
			<TheButton @click="toVisual" :title="'查看统计结果'" />
			<TheButton :title="'下载训练模型'" />
			<TheButton :title="'下载预测结果'" />
		</div>
	</Card>
</template>

<script setup>
import Card from '../shared/Card.vue'
import TheButton from '../shared/TheButton.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

function toVisual() {
	router.push('/visual')
}

// function
</script>

<style scoped></style>
