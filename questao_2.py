def fibonacci(num):
    """
    Função para calcular a sequência de Fibonacci até o número escolhido pelo usuário
    """
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1]+fib[-2])
    return fib

def check_fibonacci(n):
    """
    Função para verificar se o número que o usuário escolheu
    """
    fib = fibonacci(num)
    if n in fib:
        return f"{n} foi encontrado na sequência fibonacci: {fib}"
    else:
        return f"{n} não foi encontrado na sequência fibonacci: {fib}"

# Input do usuário para gerar a sequência de fibonacci
while True:
    try:
        num = int(input("Digite um número para verificar se está presente na sequência de Fibonacci: "))
        break
    except ValueError:
        print("Erro! Por favor, apenas números inteiros.")

print(check_fibonacci(num))