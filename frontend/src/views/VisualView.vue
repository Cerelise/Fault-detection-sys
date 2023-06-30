<template>
	<div class="home">
		<div class="container">
			<!-- <Card class="flex justify-center">
				<TheButton @click="init" :title="title" />
			</Card> -->
			<Card class="flex justify-center">
				<div ref="pie" style="width: 50%; height: 500px"></div>
				<div ref="bar" style="width: 50%; height: 500px"></div>
			</Card>
		</div>
	</div>
</template>

<script setup>
import TheButton from '../components/shared/TheButton.vue'
import Card from '../components/shared/Card.vue'
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'

const pie = ref()
const bar = ref()

async function init() {
	const pieChart = echarts.init(pie.value)
	const barChart = echarts.init(bar.value)

	const transformData = await chartData()

	const barDataxAxis = transformData.map((item) => {
		return item.name
	})

	const barDatayAxis = transformData.map((item) => {
		const value = Object.getOwnPropertyNames(item)[0]
		return item[value]
	})

	const barOption = {
		xAxis: {
			type: 'category',
			data: barDataxAxis,
		},
		yAxis: {
			type: 'value',
		},
		series: [
			{
				type: 'bar',
				showBackground: true,
				backgroundStyle: {
					color: 'rgba(180, 180, 180, 0.2)',
				},
				itemStyle: {
					color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
						{ offset: 0, color: '#83bff6' },
						{ offset: 0.5, color: '#188df0' },
						{ offset: 1, color: '#188df0' },
					]),
				},
				emphasis: {
					itemStyle: {
						color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
							{ offset: 0, color: '#2378f7' },
							{ offset: 0.7, color: '#2378f7' },
							{ offset: 1, color: '#83bff6' },
						]),
					},
				},
				data: barDatayAxis,
			},
		],
	}

	const pieOption = {
		tooltip: {
			trigger: 'item',
		},
		legend: {
			top: '5%',
			left: 'center',
		},
		series: [
			{
				type: 'pie',
				radius: ['40%', '70%'],
				avoidLabelOverlap: false,
				itemStyle: {
					borderRadius: 10,
					borderColor: '#fff',
					borderWidth: 2,
				},
				label: {
					show: false,
					position: 'center',
				},
				emphasis: {
					label: {
						show: true,
						fontSize: 40,
						fontWeight: 'bold',
					},
				},
				labelLine: {
					show: false,
				},
				data: transformData,
			},
		],
	}

	// 使用刚指定的配置项和数据显示图表。

	barChart.setOption(barOption)
	pieChart.setOption(pieOption)
}

const chartData = async () => {
	const data = await fetch('http://127.0.0.1:8000/api/result').then((res) => {
		return res.json()
	})
	// console.log('data :>> ', data)

	const handleData = data.map((item) => item.res)

	const stats = handleData.reduce((acc, curr) => {
		acc[curr] = (acc[curr] || 0) + 1
		return acc
	}, {})

	const transformData = Object.entries(stats).map(([key, value]) => ({
		value: value,
		name: `故障类型${key}`,
	}))

	return transformData
}

onMounted(() => {
	init()
})
</script>
