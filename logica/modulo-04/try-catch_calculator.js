function calculator() {
    let n1 = parseFloat(prompt("Digite o primeiro número: "))
    let operador = parseFloat(prompt("Digite o operador: "))
    let n2 = parseFloat(prompt("Digite o segundo número: "))

    try {
        if (n2 == '0' && operador == '/') {
            throw "Divisão inválida! Não é possível dividir por zero."
        } else if (isNaN(n1) || isNaN(n2) || (n1 == '' || n2 == '')) {
            throw "Número inválido!"
        }
    }
    catch (erro) {
        return alert("Erro: " + erro)
    }

    switch (operador) {
        case '+':
            return alert(n1 + n2)
            break
        case '-':
            return alert(n1 - n2)
            break
        case '*':
            return (n1 * n2)
            break
        case '/':
            return alert(n1 / n2)
            break
        default:
            return alert("Operador inválido!")
    }
}

calculator()