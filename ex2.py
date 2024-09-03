def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def verificar(f):
    i = 0
    fib = 0
    while True:
        fib = fibonacci(i)
        if fib == f:
            return 1
        if fib > f:
            return 0
        i += 1

n = 10
resultado = fibonacci(n)

if verificar(resultado):
    print(f"{resultado} pertence à sequência de Fibonacci.")
else:
    print(f"{resultado} não pertence à sequência de Fibonacci.")

print(f"O {n}º termo da sequência de Fibonacci é: {resultado}")
