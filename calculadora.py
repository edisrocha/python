def calculadora():
    while True:
        print("\nOperações: +, -, *, /, sair")
        operacao = input("Escolha uma operação: ")
        
        if operacao.lower() == 'sair':
            break
            
        try:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
            
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                    continue
                resultado = num1 / num2
            else:
                print("Operação inválida!")
                continue
                
            print(f"Resultado: {resultado}")
            
        except ValueError:
            print("Por favor, digite números válidos!")

if __name__ == "__main__":
    calculadora()
