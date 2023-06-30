module.exports = {
	content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
	theme: {
		screens: {
			sm: '480px',
			md: '768px',
			lg: '976px',
			xl: '1440px',
		},
		// 保留Tailwind原本的样式版本的前提下的样式扩展
		extend: {
			spacing: {
				1: '10px',
				2: '20px',
				3: '30px',
				4: '40px',
				5: '50px',
				6: '60px',
				7: '70px',
			},
			colors: {
				tb_bg: '#212121',
				head_hover: '#4ecca3',
				congress: {
					100: '#b2bec3',
					935: '#636e72',
				},
			},

			fontSize: {
				xs: '12px',
				sm: '15px',
				base: '18px',
			},
			boxShadow: {
				// sm: '0 0 50px rgba(0,0,0,0.6)',
				sm: '5px 5px 10px rgb(0 0 0 / 0.2)',
			},
		},
	},
	plugins: [],
}
