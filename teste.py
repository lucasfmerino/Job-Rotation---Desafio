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
    
    if fibonacci(x):
        print(f'The number {x} is a Fibonacci sequence!')
    else:
        print(f'The number {x} is not a Fibonacci sequence!')
    break
