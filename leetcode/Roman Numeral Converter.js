function convertToRoman(num) {
  const f = (x) => Math.floor(x)
  const thousands = ['', 'M', 'MM', 'MMM']
  const hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
  const tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
  const ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
  return (
    thousands[f(num / 1000)] +
    hundreds[f((num % 1000) / 100)] +
    tens[f((num % 100) / 10)] +
    ones[f(num % 10)]
  )
}
