#include <iostream>

int power(int n, unsigned int m) {
    if (m == 0)
        return 1;
    int tmp = power(n, m / 2);
    if (m % 2 == 0)
        return tmp * tmp;
    else
        return n * tmp * tmp;
}

int epsilon(int k) {
    if (k == 1)
        return 0;
    int tmp = 0;
    for (int i = 1; i < k; i++)
        tmp += power(10, k - 1 - i) * power(9, i - 1);
    return tmp;
}

int delta(int ak, int k) {
    if (ak <= 3)
        return -ak * epsilon(k);
    else
        return -(ak - 1) * epsilon(k) - power(10, k - 1);
}

int f(int n) {
    int k = 1;
    while (n >= power(10, k))
        k += 1;
    int n_tmp = n;
    int diff = 0;
    for (int i = 1; i <= k; i++) {
        diff += delta(n_tmp % 10, i);
        n_tmp /= 10;
    }
    return n + diff;
}

int main(int c, char *v[]) {
    int in;
    std::cin >> in;
    std::cout << f(in) << std::endl;
    return 0;
}