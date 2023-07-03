<template>
	<div class="main">
		<div
			class="dropzone-container"
			@dragover="dragover"
			@dragleave="dragleave"
			@drop="drop"
		>
			<input
				type="file"
				multiple
				name="file"
				id="fileInput"
				class="hidden-input"
				@change="onChange"
				ref="fileInputRef"
			/>

			<label for="fileInput" class="file-label">
				<div v-if="isDragging">释放以将文件放到此处。</div>
				<div class="flex gap-[5px] items-center" v-else>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-2 h-2 text-center"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15m0-3l-3-3m0 0l-3 3m3-3V15"
						/>
					</svg>
					将文件拖到此处或单击此处上传。
				</div>
			</label>
			<div class="preview-container mt-4" v-if="files.length">
				<div v-for="file in files" :key="file.name" class="preview-card">
					<div>
						<p>
							{{ file.name }}
						</p>
					</div>
					<div>
						<button
							class="ml-2"
							type="button"
							@click="remove(files.indexOf(file))"
							title="Remove file"
						>
							<b>×</b>
						</button>
					</div>
				</div>
			</div>
		</div>

		<div class="flex gap-4 mt-3">
			<TheButton @click="trainUpload" :title="'上传训练集'" />
			<TheButton @click="testsetUpload" :title="'上传测试集'" />
		</div>
	</div>
</template>

<script setup>
import axios from 'axios'
import TheButton from '../shared/TheButton.vue'
import { ref } from 'vue'

const isDragging = ref(false)
const files = ref([])
const fileInputRef = ref(null)

function onChange() {
	files.value = [...fileInputRef.value.files]
}

function dragover(e) {
	e.preventDefault()
	isDragging.value = true
}

function dragleave() {
	isDragging.value = false
}

function drop(e) {
	e.preventDefault()
	fileInputRef.value.files = e.dataTransfer.files
	onChange()
	isDragging.value = false
}

function remove(i) {
	files.value.splice(i, 1)
}

// 单文件上传
function trainUpload() {
	const formData = new FormData()
	console.log(files.value)
	files.value.forEach((file) => {
		formData.append('train', file)
	})
	console.log('formData :>> ', formData)
	axios
		.post('/api/train/', formData, {
			headers: {
				'Content-Type': 'multipart/form-data',
			},
		})
		.then((res) => console.log(res.data.message))
		.catch((error) => {
			console.log('error :>> ', error)
		})
}

function testsetUpload() {
	const testset = new FormData()
	files.value.forEach((file) => {
		testset.append('test', file)
	})
	console.log('testset :>> ', testset)

	axios
		.post('/api/test/', testset, {
			headers: {
				'Content-Type': 'multipart/form-data',
			},
		})
		.then((res) => console.log(res.data.message))
		.catch((error) => {
			console.log('error :>> ', error)
		})
}

// 多文件上传
function multipleFilesUpload() {
	const formData = new FormData()
	files.value.forEach((file) => {
		formData.append('trains', file)
	})

	axios
		.post('/api/train/multiple_upload/', formData, {
			headers: {
				'Content-Type': 'multipart/form-data',
			},
		})
		.then((res) => console.log(res.data))
		.catch((error) => {
			console.log('error :>> ', error)
		})

	files.value = ''
}
</script>

<style scoped>
.main {
	display: flex;
	flex-grow: 1;
	height: 40vh;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	text-align: center;
	gap: 15px;
}

.dropzone-container {
	padding: 4rem;
	background: #f7fafc;
	border: 1px solid #e2e8f0;
}

.hidden-input {
	opacity: 0;
	overflow: hidden;
	position: absolute;
	width: 1px;
	height: 1px;
}

.file-label {
	font-size: 20px;
	display: block;
	cursor: pointer;
}

.preview-container {
	display: flex;
	margin-top: 2rem;
}

.preview-card {
	display: flex;
	border: 1px solid #a2a2a2;
	padding: 5px;
	margin-left: 5px;
}

.preview-img {
	width: 50px;
	height: 50px;
	border-radius: 5px;
	border: 1px solid #a2a2a2;
	background-color: #a2a2a2;
}
</style>
