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

int gamma(int n)
{
    if (n == 1)
        return 1;

    int tmp = 0;
    for (int i = 1; i < n; i++)
        tmp += power(10, i - 1);
    return 9 * tmp;
}

int delta(int ak, int k)
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
    while (n >= pow(10, k))
        k += 1;

    int result = 0;
    for (int i = 1; i <= k; i++)
    {
        int ai = num_digit(n, i);
        result += delta(ai, i) + ai * f(gamma(i));
    }

    f_result[n] = result;
    return result;
}

int main(int c, char* v[])
{
    int in;
    std::cin >> in;
    std::cout << in - f(in) << std::endl;
    return 0;
}