<template>
	<div class="home">
		<div class="container">
			<Card>
				<DropFile />
			</Card>

			<Dashboard />
		</div>
	</div>
</template>

<script setup>
import Card from '../components/shared/Card.vue'
import DropFile from '../components/upload/DropFile.vue'
import Dashboard from '../components/dashboard/Dashboard.vue'
</script>
