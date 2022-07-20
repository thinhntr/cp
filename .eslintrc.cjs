module.exports = {
	env: {
		browser: true,
		es2021: true,
	},
	extends: ['xo'],
	parser: '@typescript-eslint/parser',
	parserOptions: {
		ecmaVersion: 'latest',
	},
	plugins: ['@typescript-eslint'],
	rules: {
		'comma-dangle': ['never'],
	},
};