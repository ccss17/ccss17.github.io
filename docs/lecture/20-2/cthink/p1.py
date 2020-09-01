def alpha(n):
    if n == 1:
        return 1
    a = 0
    for i in range(1, n):
        a += 10 ** (i - 1)
    return 9 * a

def delta(ak, k):
    if ak <= 3:
        return 0
    else:
        return 9 ** (k - 1)

f_result = {}
def f(n):
    if isinstance(n, int):
        n_int = n
        n = repr(n)
    else:
        n_int = int(n)
    if n in f_result:
        return f_result[n]
    if n == '1':
        return 0
    k = 1
    while n_int >= 10 ** k:
        k += 1
    d = 0
    l = len(n)
    for i in range(1, k+1):
        # ni_1 = int(n[::-1][i-1])
        ni_1 = int(n[l - i])
        d += delta(ni_1, i) + ni_1 * f(alpha(i))
    f_result[n] = d
    return d

if __name__ == '__main__':
    i = 999999
    d = f(i)
    print(int(i) - d)