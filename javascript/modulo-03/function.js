function hello() {
    return "Olá, seja bem-vindo(a)!"
}

function nomecomp(nome, sobrenome) {
    nomecomp = nome + " " + sobrenome
    return nomecomp
}

subtracao = (n1, n2) => {
    result = n1 - n2
    return result
}

console.log(hello())
console.log(nomecomp("Mariana", "Calado"))
console.log(subtracao(10, 5))
