#include <iostream>
#include <map>
using namespace std;

map<string, int> f_result;

long long pow(int n, unsigned int m)
{
    int tmp;
    if (m == 0)
        return 1;
    tmp = pow(n, m / 2);
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
        tmp += pow(10, i - 1);
    return 9 * tmp;
}

int delta(int ak, int k)
{
    if (ak <= 3)
        return 0;
    else
        return pow(9, k - 1);
}

long long f(string n);
long long f(int n);
long long _f(string n, int n_int)
{
    if (f_result.find(n) != f_result.end())
        return f_result[n];
    if (n == "1")
        return 0;
    int k = 1;
    while (n_int >= pow(10, k))
        k += 1;
    int result = 0;
    size_t l = n.size();
    for (int i = 1; i < k + 1; i++)
    {
        int ai = n[l - i] - '0';
        result += delta(ai, i) + ai * f(gamma(i));
    }
    f_result[n] = result;
    return result;
}

long long f(string n) { return _f(n, stoi(n)); }
long long f(int n) { return _f(to_string(n), n); }

int main(int c, char *v[])
{
    int in = 999999;
    cout << in - f(in) << endl;
    return 0;
}