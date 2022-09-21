function calculadora() {

    let n1 = parseFloat(prompt("Digite o primeiro número: "))
    let operador = prompt("Digite o operador: ")
    let n2 = parseFloat(prompt("Digite o segundo número: "))


    switch (operador) {
        case '+':
            resultado = n1 + n2
            return alert(resultado)
            break
        case '-':
            resultado = n1 - n2
            return alert(resultado)
            break
        case '*':
            resultado = n1 * n2
            return alert(resultado)
            break
        case '/':
            resultado = n1 / n2
            resto = n1 % n2
            if (resto == 0) {
                return alert(resultado)
            } else if (resto != 0) {
                resto = n1 % n2
                return alert("Resultado =" + resultado + " e Resto= " + resto)
            }
    }
}

calculadora()

