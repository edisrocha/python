class ConversorUnidades:
    @staticmethod
    def celsius_para_fahrenheit(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def km_para_milhas(km):
        return km * 0.621371
    
    @staticmethod
    def kg_para_libras(kg):
        return kg * 2.20462
    
    @staticmethod
    def real_para_dolar(real, cotacao):
        return real / cotacao

def menu_conversor():
    print("🔄 CONVERSOR DE UNIDADES")
    print("1. Celsius → Fahrenheit")
    print("2. Km → Milhas")
    print("3. Kg → Libras")
    print("4. Real → Dólar")
    
    opcao = input("Escolha uma opção: ")
    valor = float(input("Digite o valor: "))
    
    conv = ConversorUnidades()
    
    if opcao == '1':
        resultado = conv.celsius_para_fahrenheit(valor)
        print(f"{valor}°C = {resultado:.2f}°F")
    elif opcao == '2':
        resultado = conv.km_para_milhas(valor)
        print(f"{valor} km = {resultado:.2f} milhas")
    elif opcao == '3':
        resultado = conv.kg_para_libras(valor)
        print(f"{valor} kg = {resultado:.2f} libras")
    elif opcao == '4':
        cotacao = float(input("Cotação do dólar: "))
        resultado = conv.real_para_dolar(valor, cotacao)
        print(f"R$ {valor} = US$ {resultado:.2f}")

# menu_conversor()
