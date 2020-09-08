def epsilon(k):
    if k == 1:
        return 0
    tmp = 0
    for i in range(1, k):
        tmp += 10 ** (k - 1 - i) * 9 ** (i - 1)
    return tmp

def delta(ak, k):
    if ak <= 3:
        return -ak * epsilon(k)
    else:
        return -(ak - 1) * epsilon(k) - 10 ** (k - 1)
    
def s(n):
    k = 1
    while n >= 10 ** k:
        k += 1
    
    n_tmp = n
    d = 0
    for i in range(1, k+1):
        d += delta(n_tmp % 10, i)
        n_tmp = int(n_tmp / 10)
    
    return n + d

def gamma(n):
    if n == 1:
        return 1

    tmp = 0
    for i in range(1, n):
        tmp += 10 ** (i - 1)

    return 9 * tmp

def de(ak, k):
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
        result += ai * f(repr(gamma(i))) + de(ai, i) 

    f_result[n] = result
    return result

if __name__ == '__main__':
    # print(s(10))
    # for i in range(10, 21):
        # print(i, s(i))
    # for n in [13, 1399, 999999]:
        # print(s(n))
    print(s(10 ** 100))
    # print(s(100))
    # print(20 - f(repr(20)))
    # print(30 - f(repr(30)))
    # print(50 - f(repr(50)))
    # print(1000 - f(repr(1000)))
