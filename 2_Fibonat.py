def fib(n):
    c = 0
    a = 1 
    b = 1
    if n == 0 or n == 1 or n == 2:
        print('Pertence')
    else:
        while c < n:
            c = a + b
            b = a
            a = c
            if c == n:
                print('Pertence')
                return 0
        print('Nao Pertence')

fib(987)