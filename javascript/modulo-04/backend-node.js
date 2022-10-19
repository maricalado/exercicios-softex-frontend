const porta = 6060

const express = require('express')
const app = express()

app.get('/user', (req, res, next) => {
    res.send({
        usuario1: {
            nome: "Mariana Calado",
            email: "marianacalado@gmail.com"
        },
        usuario2: {
            nome: "Maria Clara",
            email: "mariaclara@gmail.com"
        }
    })
})

app.listen(porta, () => {
    console.log(`Servidor executado na porta ${porta}.`)
})