def gamma(n):
    if n == 1:
        return 1

    tmp = 0
    for i in range(1, n):
        tmp += 10 ** (i - 1)

    return 9 * tmp

def delta(ak, k):
    return 0 if ak <= 3 else 9 ** (k - 1)

f_result = {}

def f(n):
    if n in f_result:
        return f_result[n]
    if n == '1':
        return 0

    n_int, k = int(n), 1
    while n_int >= 10 ** k:
        k += 1

    result, l = 0, len(n)
    for i in range(1, k+1):
        ai = int(n[l - i])
        result += ai * f(repr(gamma(i))) + delta(ai, i) 

    f_result[n] = result
    return result

if __name__ == '__main__':
    # i = 10 ** 100
    # i = 1399
    # i = 999999
    # i = 100
    # print(i, i - f(repr(i)))
    # print(7776, 7776 - f(repr(7776)))
    # print(7777, 7777 - f(repr(7777)))

    import matplotlib.pyplot as plt
    import numpy as np
    x = np.arange(100)

    x = [x for x in range(1, 100000)]
    y = [f(repr(i)) for i in x]
    
    plt.plot(x, y)
    plt.show()
