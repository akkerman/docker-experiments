const express = require('express')
const morgan = require('morgan')

const PORT = 3000

const app = express()
app.use(morgan('dev'))

app.get('/test', (req, res) => {
  res.send({
    test: 'test-value',
    updated: new Date().toString()
  })
})

const server = app.listen(PORT, () => {
  const { address, port } = server.address()
  console.log('Server listening @ http://%s:%s', address, port)
})
