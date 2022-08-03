def calculadora():
    while (True):
        print("1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n0- Sair\n")
        opcao = int(input("Informe a opção desejada: \n"))

        if (opcao == 1):
            valor1 = float(input("Informe o primeiro valor: "))
            valor2 = float(input("Informe o segundo valor: "))
            soma = valor1 + valor2
            print("Resultado: \n" + str(valor1) + " + " +
                  str(valor2) + " = " + str(soma) + "\n")
        elif (opcao == 2):
            valor1 = float(input("Informe o primeiro valor: "))
            valor2 = float(input("Informe o segundo valor: "))
            subt = valor1 - valor2
            print("Resultado: \n" + str(valor1) + " - " +
                  str(valor2) + " = " + str(subt) + "\n")
        elif (opcao == 3):
            valor1 = float(input("Informe o primeiro valor: "))
            valor2 = float(input("Informe o segundo valor: "))
            mult = valor1 * valor2
            print("Resultado: \n" + str(valor1) + " x " +
                  str(valor2) + " = " + str(mult) + "\n")
        elif (opcao == 4):
            valor1 = float(input("Informe o primeiro valor: "))
            valor2 = float(input("Informe o segundo valor: "))
            if (valor2 == 0.0):
                print("Ops! Não pode divisão por zero.\n")
                continue
            div = valor1 / valor2
            print("Resultado: \n" + str(valor1) + " / " +
                  str(valor2) + " = " + str(div) + "\n")
        elif (opcao == 0):
            print("Programa finalizado! Volte sempre!\n")
            break
        else:
            print("Erro! Essa opção não existe\n")


calculadora()
