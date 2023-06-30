<template>
	<ul class="flex align-center justify-around my-5">
		<li
			class="p-1 w-5 h-5 rounded-[25px] text-lg border border-[#ccc]"
			v-for="n in 10"
			:key="`rating-${n}`"
		>
			<input
				type="radio"
				:id="`num${n}`"
				name="rating"
				:value="n"
				:checked="selected === n"
				v-model="selected"
			/>
			<label
				class="w-5 h-5 p-1 text-center rounded-[25px] cursor-pointer"
				:for="`num${n}`"
			>
				{{ n }}
			</label>
		</li>
	</ul>
</template>

<script>
export default {
	name: 'RatingSelect',
	data() {
		return {
			selected: this.rating,
		}
	},

	props: {
		rating: {
			type: Number,
		},
	},

	watch: {
		selected(newVal) {
			this.$emit('setRating', newVal)
		},
		rating(newVal) {
			this.selected = newVal
		},
	},
}
</script>

<style scoped>
/* rating */
li {
	position: relative;
	transition: 0.3s;
}

li label {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}

li:hover,
.num-display {
	background: #4ecca3;
	color: #fff;
}

[type='radio'] {
	opacity: 0;
}

[type='radio']:checked ~ label {
	background: #4ecca3;
	color: #fff;
}
</style>
