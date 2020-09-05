def epsilon(k):
    if k == 1:
        return 0
    tmp = 0
    for i in range(1, k):
        tmp += 10 ** (k - 1 - i) * 9 ** (i - 1)
    return tmp

def delta(ak, k):
    if ak <= 3:
        return ak * epsilon(k)
    else:
        return (ak - 1) * epsilon(k) + 10 ** (k - 1)
    
def f(n):
    k = 1
    while n >= 10 ** k:
        k += 1
    
    n_tmp = n
    d = 0
    for i in range(1, k+1):
        d += delta(n_tmp % 10, i)
        n_tmp = int(n_tmp / 10)
    
    return n - d

if __name__ == '__main__':
    # print(s(10))
    # for i in range(10, 21):
        # print(i, s(i))
    for n in [13, 1399, 999999]:
        print(f(n))
    # print(s(100))
    # print(20 - f(repr(20)))
    # print(30 - f(repr(30)))
    # print(50 - f(repr(50)))
    # print(1000 - f(repr(1000)))