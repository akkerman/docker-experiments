const rndString = require('randomstring')
const min = 1000
const max = 5000

const loop = () => {
    const str = rndString.generate()
    console.log(new Date(), 'node', str)

    const num = Math.random() * (max - min) + min

    setTimeout(loop, num)
}

loop()
