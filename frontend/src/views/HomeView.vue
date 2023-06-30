<template>
	<div class="home">
		<div class="container">
			<div class="flex space-x-2">
				<div class="w-1/2 py-[120px] pl-6">
					<h1 class="text-4xl font-bold">
						基于机器学习的分布式系统故障诊断系统
					</h1>
					<p class="mt-1 text-slate-500 font-medium leading-8">
						Welcome to use this system
					</p>
					<div class="mt-5 ml-3">
						<TheButton :title="title" />
					</div>
				</div>
				<div class="flex justify-end w-1/2">
					<img src="../assets/images/ill.svg" alt="" />
				</div>
			</div>

			<div class="px-2 py-1 text-center">
				<h1 class="text-4xl font-bold mx-auto">
					<span
						style="
							background: linear-gradient(315deg, #42d392 25%, #647eff);
							background-clip: text;
							-webkit-text-fill-color: transparent;
						"
						>网站介绍</span
					>
				</h1>

				<p class="w-2/3 text-center leading-6 mt-3 mb-4 mx-auto tracking-wide">
					该平台支持用户上传训练数据并在线训练，训练完成后可以下载训练模型，支持单条或者批量测试样本上传，并可视化分类结果，同时支持下载分类结果
				</p>
			</div>

			<div class="flex min-w-full space-x-1">
				<card
					class="w-1/3 flex flex-col gap-[3px] shadow-sm shadow-emerald-500"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-3 h-3 text-green-500"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z"
						/>
					</svg>
					<h3 class="text-3xl">业务场景一</h3>
					<span class="text-base font-semibold text-green-500"
						>用户上传训练集并进行在线训练</span
					>
					<p>
						实现用户提供训练集的上传，支持用户使用个人训练集进行在线训练，完成后可生成模型，并提供模型文件的下载。
					</p>
				</card>
				<card class="w-1/3 flex flex-col gap-[3px] shadow-sm shadow-orange-500">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-3 h-3 text-orange-500"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M15.59 14.37a6 6 0 01-5.84 7.38v-4.8m5.84-2.58a14.98 14.98 0 006.16-12.12A14.98 14.98 0 009.631 8.41m5.96 5.96a14.926 14.926 0 01-5.841 2.58m-.119-8.54a6 6 0 00-7.381 5.84h4.8m2.581-5.84a14.927 14.927 0 00-2.58 5.84m2.699 2.7c-.103.021-.207.041-.311.06a15.09 15.09 0 01-2.448-2.448 14.9 14.9 0 01.06-.312m-2.24 2.39a4.493 4.493 0 00-1.757 4.306 4.493 4.493 0 004.306-1.758M16.5 9a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z"
						/>
					</svg>
					<h3 class="text-3xl">业务场景二</h3>
					<span class="text-base font-semibold text-orange-500"
						>用户上传测试集，利用本平台已有模型进行计算</span
					>
					<p>
						用户提供上传数据集，支持单条或批量测试样本，通过本平台已训练好的模型计算预测结果，并提供预测结果下载。
					</p>
				</card>
				<card class="w-1/3 flex flex-col gap-[3px] shadow-sm shadow-indigo-500">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-3 h-3 text-indigo-500"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M16.5 18.75h-9m9 0a3 3 0 013 3h-15a3 3 0 013-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 01-.982-3.172M9.497 14.25a7.454 7.454 0 00.981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 007.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 002.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 012.916.52 6.003 6.003 0 01-5.395 4.972m0 0a6.726 6.726 0 01-2.749 1.35m0 0a6.772 6.772 0 01-3.044 0"
						/>
					</svg>
					<h3 class="text-3xl">业务场景三</h3>
					<span class="text-base font-semibold text-indigo-500"
						>用户在平台查看可视化分类结果</span
					>
					<p>
						用户上传测试集进行在线计算，并将产生的分类结果在前端网页可视化。
					</p>
				</card>
			</div>
		</div>
	</div>
</template>

<script setup>
import Card from '../components/shared/Card.vue'
import TheButton from '../components/shared/TheButton.vue'
import { ref } from 'vue'

const title = ref('Get started')
</script>
