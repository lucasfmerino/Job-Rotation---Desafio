"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre se
rá a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""

def fibonacci(x):
    a, b = 0, 1
    while b < int(x):
        a, b = b, a + b
        if b == int(x):
            return True


while True:
    x = input("Enter a integer: ")
    try:
        int(x)
    except Exception:
        print("Invalid number!")
        continue
    
    if fibonacci(x):
        print(f'The number {x} is a Fibonacci sequence!')
    else:
        print(f'The number {x} is not a Fibonacci sequence!')
        
    break
