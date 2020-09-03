import math

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

    k = math.ceil(math.log10(int(n)))
    l = len(n)
    result = 0
    for i in range(1, k+1):
        ai = int(n[l - i])
        result += ai * f(repr(gamma(i))) + delta(ai, i) 

    f_result[n] = result
    return result


if __name__ == '__main__':
    i = 10 ** 100
    # i = 1399
    # i = 999999
    print(i - f(repr(i)))
