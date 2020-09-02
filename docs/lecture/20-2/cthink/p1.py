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
        result += delta(ai, i) + ai * f(repr(gamma(i)))

    f_result[n] = result
    return result


if __name__ == '__main__':
    i = 10 ** 100
    print(i - f(repr(i)))
