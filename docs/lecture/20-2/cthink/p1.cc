#include <iostream>
#include <string>
#include <map>

int num_digit(int n, int i)
{
    while (--i > 0)
        n /= 10;
    return n % 10;
}

int power(int n, unsigned int m)
{
    if (m == 0)
        return 1;

    int tmp = power(n, m / 2);
    if (m % 2 == 0)
        return tmp * tmp;
    else
        return n * tmp * tmp;
}

int epsilon(int k)
{
    if (k == 1)
        return 0;
    int tmp = 0;
    for (int i=1; i<k; i++)
        tmp += power(10, k - 1 - i) * power(9, i - 1);
    return tmp;
}

int delta(int ak, int k)
{
    if (ak <= 3)
        return -ak * epsilon(k);
    else
        return -(ak - 1) * epsilon(k) - power(10, k - 1);
}

int s(int n)
{
    int k = 1;
    while (n >= power(10, k))
        k += 1;
    int n_tmp = n;
    int d = 0;
    for (int i = 0; i <= k; i++)
    {
        d += delta(n_tmp % 10, i);
        n_tmp /= 10;
    }
    return n + d;
}

int gamma(int n)
{
    if (n == 1)
        return 1;

    int tmp = 0;
    for (int i = 1; i < n; i++)
        tmp += power(10, i - 1);
    return 9 * tmp;
}

int de(int ak, int k)
{
    if (ak <= 3)
        return 0;
    else
        return power(9, k - 1);
}

int f(int n)
{
    static std::map<int, int> f_result;

    if (f_result.find(n) != f_result.end())
        return f_result[n];
    if (n == 1)
        return 0;

    int k = 1;
    while (n >= power(10, k))
        k += 1;

    int result = 0;
    for (int i = 1; i <= k; i++)
    {
        int ai = num_digit(n, i);
        result += de(ai, i) + ai * f(gamma(i));
    }

    f_result[n] = result;
    return result;
}

int main(int c, char* v[])
{
    int in = 99999999;
    // std::cin >> in;
    //std::cout << in - f(in) << std::endl;
     std::cout << s(in) << std::endl;
    return 0;
}
