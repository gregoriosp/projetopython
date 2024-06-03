def add(x, y):
    """Função para adicionar dois números."""
    return x + y

def subtract(x, y):
    """Função para subtrair dois números."""
    return x - y

def multiply(x, y):
    """Função para multiplicar dois números."""
    return x * y

def divide(x, y):
    """Função para dividir dois números."""
    if y == 0:
        return "Erros! Divisão por zero."
    return x / y

def calculator():
    """Função principal da calculadorass."""
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        choice = input("Digite sua escolha (1/2/3/4/5): ")

        if choice == '5':
            print("Encerrando a calculadora.")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, insira números válidos.")
                continue

            if choice == '1':
                print(f"Resultado: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"Resultado: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Resultado: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Erro! Divisão por zero.":
                    print(result)
                else:
                    print(f"Resultado: {num1} / {num2} = {result}")
        else:
            print("Escolha inválida! Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    calculator()
