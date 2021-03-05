# HW1

1. $\int_{}^{}\sinh ^{3}xdx$ 의 적분 풀기

    $$ \int_{}^{}\sinh ^{3}xdx = \int_{}^{}\bigg (\dfrac{e ^{x} - e ^{-x}}{2}\bigg ) ^{3}dx = \int_{}^{}\dfrac{e ^{3x}-e ^{-3x}-3 e ^{x} + 3 e ^{-x}}{8}dx $$

    $$ = \dfrac{e ^{3x} + e ^{-3x}}{8 \cdot 3} - \dfrac{3}{8}(e ^{x} + e ^{-x}) + C = \dfrac{\cosh 3x}{12} - \dfrac{3}{4}\cosh x + C $$

2. $\int_{}^{}x ^{2} \tanh ^{-1}xdx$ 의 적분 풀기

    $u = \tanh ^{-1}x, v' = x ^{2}$ 로 두면 $\int_{}^{}uv'dx = uv - \int_{}^{}u'vdx$ 이므로 

    $$ \int_{}^{}x ^{2}\tanh ^{-1}xdx = \dfrac{1}{3}x ^{3}\tanh ^{-1}x - \int_{}^{}\dfrac{1}{3}x ^{3}\dfrac{1}{1 - x ^{2}}dx = \dfrac{x ^{3}}{3}\tanh ^{-1}x - \dfrac{1}{3}\int_{}^{}\dfrac{x ^{3}}{1- x ^{2}} dx $$

    이다. 이때
    
    $$\dfrac{x ^{3}}{1 - x ^{2}} = \dfrac{x}{1 - x ^{2}} - x = -x + \dfrac{1}{2}\bigg (\dfrac{x}{1-x} + \dfrac{x}{1+x}\bigg ) = -x + \dfrac{1}{2}\bigg (\dfrac{1}{1-x} - \dfrac{1}{1+x} \bigg )$$

    이므로 

    $$ \int_{}^{} -x + \dfrac{1}{2} \bigg (\dfrac{1}{1-x} - \dfrac{1}{1+x}\bigg ) dx = - \dfrac{1}{2}x ^{2} + \dfrac{1}{2}\ln \bigg |\dfrac{1-x}{1+x}\bigg | + C$$

    이다. 따라서 

    $$ \int_{}^{}x ^{2}\tanh ^{-1}xdx = \dfrac{x ^{3}}{3}\tanh ^{-1}x - \dfrac{1}{3} \bigg (- \dfrac{1}{2}x ^{2} + \dfrac{1}{2}\ln \bigg |\dfrac{1-x}{1+x}\bigg | + C\bigg ) $$

    이다.

3. $ty' + 3y = \dfrac{\sinh t}{t ^{2}}$ 의 일반해 구하기.

    주어진 미분방정식을 표준형으로 정리하면 $y' + y \dfrac{3}{t} = \dfrac{\sinh t}{t ^{3}}$ 이므로 적분인자는 

    $$ \mu = \pm e ^{\int_{}^{}3/t dt} = \pm e ^{3 \ln t} = e ^{\ln t ^{3}} \quad (t>0) $$

    $$ = t ^{3} $$

    이다. $\mu$ 를 주어진 방정식의 양변에 곱하면 

    $$ t ^{3} (y' + y \dfrac{3}{t}) = \sinh t \iff \dfrac{d}{dt}(t ^{3}y) = \sinh t $$

    $$ \iff t ^{3} y = \int_{}^{}\sinh t dt = \cosh t + C_1 $$

    이므로 

    $$ \therefore y = \dfrac{\cosh t}{t ^{3}} + \dfrac{C_1}{t ^{3}} $$

    이다.

4. $y' + (\tanh t)y = \operatorname{sech} t$ 의 일반해 구하기.

    주어진 방정식의 적분인자는 

    $$ \mu = \pm e ^{\int_{}^{}\tanh tdt} = \pm e ^{\ln (\cosh x)} = \pm \cosh t $$

    이므로 이것을 주어진 방정식의 양변에 곱하면 식이 

    $$ \dfrac{d}{dt}(y \cosh t) = \cosh t \cdot \operatorname{sech} t = 1 $$

    로 정리된다. 그러므로 

    $$ y \cosh t = t + C_1 \iff y = \dfrac{t}{\cosh t} + \dfrac{C_2}{\cosh t} $$

    이다.

5. $\displaystyle \sum_{n=1}^{\infty}\dfrac{3n-1}{(n+1) ^{2}}$ 이 수렴하는지 조사.

    $f(x) = \dfrac{3x - 1}{(x + 1) ^{2}}$ 로 두면 $f'(x) = \dfrac{5 - 3x}{(1+n)^{3}}$ 가 $f' \bigg (\dfrac{5}{3}\bigg ) = 0$ 이고, $x > \dfrac{5}{3}$ 에서 $f'(x) < 0$ 이므로 $f(x)$ 는 $x > \dfrac{5}{3}$ 에서 단조감소함수이다. 또한 $f \bigg (\dfrac{1}{3}\bigg ) = 0$ 이고 $x > \dfrac{1}{3}$ 에서 $f(x) \geq 0$ 이다.

    $$ \int_{1}^{R} f(x) dx = \int_{1}^{R} \dfrac{3x - 1}{(x + 1) ^{2}} dx $$

    에서 $x + 1 = t$ 로 두면 $dt = dx$ 이므로 

    $$ = \int_{1}^{R} \dfrac{3t-4}{t ^{2}}dt = 3\int_{1}^{R}\dfrac{1}{t}dt - 4 \int_{1}^{R}\dfrac{1}{t ^{2}}dt = 3 [\ln t] ^{R} _{1} - 4 [-t ^{-1}] ^{R} _{1} $$

    $$ = 3 \ln R - 3 \ln 1 - 4 (-R ^{-1} - (-1 ^{-1})) = 3 \ln R + \dfrac{4}{R} - 1 $$

    이다. $R \to \infty \implies 3 \ln R + \dfrac{4}{R} - 1 \to \infty$ 이므로 주어진 급수는 적분판정법에 의하여 발산한다.

6. $\displaystyle \sum_{n=1}^{\infty}(-1) ^{n+1}\dfrac{3n-1}{(n+1) ^{2}}$ 이 수렴하는지 조사.

    $a_n = \dfrac{3n - 1}{(n + 1) ^{2}}$ 로 두고, $a _{n+1} = \dfrac{3n+2}{(n+2) ^{2}}$ 로 두자.

    이때 $a_n - a _{n+1} = \dfrac{3n - 1}{(n + 1) ^{2}} - \dfrac{3n+2}{(n+2) ^{2}} = \dfrac{3 n ^{2} + n - 6}{(n+1) ^{2}(n+2) ^{2}}$ 이다. 그러므로 $n = 1$ 일 때만 $a_n - a _{n+1} < 0$ 이고 $n > 1$ 일 때 $a_n - a _{n+1} > 0$ 이다.

    따라서 $n > 1$ 에서 $a_n \geq a _{n+1}$ 이고, $a_n > 0$ 이다. 그러므로 교대급수 판정법에 의하여 $n > 1$ 에서 주어진 급수가 수렴한다.

    이때 $n = 1$ 일 때도 급수가 수렴하므로 모든 자연수 $n \in \N$ 에 대하여 주어진 급수가 수렴한다.

7. $\displaystyle \sum_{n=1}^{\infty} \dfrac{(3n-1) ^{n}}{(n+1) ^{n}}$ 이 수렴하는지 조사.

    $a_n = \bigg (\dfrac{3n-1}{n+1}\bigg ) ^{n}$ 로 두면 

    $$ \lim_{n \to \infty} \sqrt[n]{ \bigg(\dfrac{3n-1}{n+1}\bigg )^{n}} = \lim_{n \to \infty} \dfrac{3n-1}{n+1} = 3 $$

    이므로 제곱근 판정법에 의하여 주어진 급수가 발산한다.

8. $\displaystyle \sum_{n=1}^{\infty}\dfrac{\ln n}{n ^{2}}$ 수렴 조사.

    $\ln n < \sqrt[]{n}$ 이므로 만약 급수 $\displaystyle \sum_{n=1}^{\infty} \dfrac{\sqrt[]{n}}{n ^{2}}$ 가 수렴하면 비교판정법에 의하여 주어진 급수도 수렴한다.

    $\dfrac{\sqrt[]{n}}{n ^{2}} = n ^{-3/2}$ 이므로 $f(x) = x ^{-3/2}$ 로 두면

    $f'(x) = - \dfrac{3}{2x ^{5/2}} < 0$ 이므로 $f(x)$ 는 단조감소수열이고 $f(x) \geq 0$ 이다.

    $$ \int_{1}^{R} f(x) dx = \int_{1}^{R} x ^{-3/2} dx = [-2 x ^{-1/2}] ^{R} _{1} = -2 R ^{-1/2} - (-2 \cdot 1 ^{-1/2}) = -2 \dfrac{1}{\sqrt[]{R}} + 2 $$

    이므로 $\displaystyle \lim_{R \to \infty} \int_{1}^{R} f(x) = 2$ 이다. 따라서 적분판정법에 의하여 급수 $\displaystyle \sum_{n=1}^{\infty} \dfrac{\sqrt[]{n}}{n ^{2}}$ 가 수렴한다.

    그러므로 비교판정법에 의하여 주어진 급수도 수렴한다.

9. $\displaystyle \sum_{n=1}^{\infty}\dfrac{\ln n}{n ^{1/2}}$ 수렴 조사.

    $n > e$ 일 때 $1 < \ln n$ 이므로 $\dfrac{1}{n ^{1/2}}$ 이 발산하면 주어진 급수는 $n > e$ 의 범위에서 발산한다.

    $f(x) = \dfrac{1}{x ^{1/2}} = x ^{-1/2}$ 로 두면 $f'(x) = - \dfrac{1}{2}x ^{-3/2} < 0$ 이므로 $f(x)$ 는 단조감수함소이며 $f(x) \geq 0$ 이다. 

    $$ \int_{1}^{R} x ^{-1/2} dx = [2x ^{1/2}] ^{R} _{1} = 2 R ^{1/2} - 2 \cdot 1 ^{1/2} $$

    이므로 $R \to \infty \implies \int_{1}^{R} f(x) dx \to \infty$ 이다. 그러므로 적분판정법에 의하여 $\dfrac{1}{x ^{1/2}}$ 가 발산한다. 

    그러므로 비교판정법에 의하여 주어진 급수는 $n > e$ 범위에서 발산한다. 그런데 $n = 1, n = 2$ 를 포함시켜도 발산하는 것은 마찬가지이므로 주어진 급수는 $\forall n \in \N$ 에서 발산한다.

10. $\displaystyle \sum_{n=1}^{\infty}\dfrac{1}{{}_{2n}C_{n}}$ 수렴 조사.

    ${}_{2n}C_{n} = \dfrac{2n!}{n!n!}$ 이므로 $a_n = \dfrac{1}{{}_{2n}C_{n}} = \dfrac{n!n!}{2n!}$ 로 두면 

    $$ \lim_{n \to \infty}  \dfrac{a _{n+1}}{a_n} = \lim_{n \to \infty}  \dfrac{(n+1)!(n+1)!}{(2n+2)!} \cdot \dfrac{2n!}{n!n!} = \lim_{n \to \infty}  \dfrac{n ^{2}}{(2n + 2)(2n + 1)} $$

    $$ = \lim_{n \to \infty} \dfrac{n ^{2}}{4n ^{2} + 6n + 1} = \lim_{n \to \infty} \dfrac{1}{4 + 6/n + 1/n ^{2}} = \dfrac{1}{4} $$

    이므로 비율판정법에 의하여 주어진 급수는 수렴한다.

11. $\displaystyle \sum_{n=1}^{\infty}\dfrac{(n+1) ^{n}}{n ^{n}}$ 수렴 조사.

    $\dfrac{n ^{n}}{n ^{n}} < \dfrac{(n+1) ^{n}}{n ^{n}}$ 이므로 급수 $\displaystyle \sum_{n=1}^{\infty} \dfrac{n ^{n}}{n ^{n}}$ 가 발산하면 비교판정법에 의하여 주어진 급수도 발산한다. 그런데 

    $$ \sum_{n=1}^{\infty} \dfrac{n ^{n}}{n ^{n}} = \sum_{n=1}^{\infty} 1 \to \infty $$

    이므로 급수 $\displaystyle \sum_{n=1}^{\infty} \dfrac{n ^{n}}{n ^{n}}$ 는 발산한다. 따라서 비교판정법에 의하여 주어진 급수도 발산한다.

12. $\displaystyle \sum_{n=1}^{\infty}\dfrac{4 ^{n}}{(2n)!}$ 수렴 조사.

    $a_n = \dfrac{4 ^{n}}{(2n)!}$ 에 대하여

    $$ \lim_{n \to \infty} \dfrac{a _{n+1}}{a_n} = \lim_{n \to \infty} \dfrac{4 ^{n+1}}{2(n+1)!} \cdot \dfrac{2n!}{4 ^{n}} = \lim_{n \to \infty} \dfrac{4}{2(n+1)} = 0 $$

    이므로 비율판정법에 의하여 주어진 급수는 수렴한다.

13. $\displaystyle \sum_{n=1}^{\infty}\dfrac{1 + n \ln n}{n ^{2} + 5}$ 수렴 조사.

    $a_n = \dfrac{1 + n \ln n}{n ^{2} + 5}$ 와 $b_n =  \dfrac{\ln n}{n}$ 에 대하여 

    $$ \lim_{n \to \infty} \dfrac{a_n}{b_n} = \lim_{n \to \infty}  \dfrac{1 + n \ln n}{n ^{2} + 5} \cdot \dfrac{n}{\ln n} = \lim_{n \to \infty} \dfrac{n + n ^{2}\ln n}{n ^{2}\ln n + 5 \ln n} $$

    $$ = \lim_{n \to \infty} \dfrac{ \dfrac{n}{n ^{2} \ln n} + 1}{1 + 5/n ^{2}} = 1 $$

    이므로 극한비교 판정법을 사용할 수 있다.

    $f(x) = \dfrac{\ln x}{x}$ 로 두면 $f'(x) = \dfrac{1 - \ln x}{x ^{2}}$ 는 $x > e$ 에서 $f'(x) < 0$ 이므로 $f(x)$ 는 $x > e$ 에서 단조감소함수이고 $f(x) \geq 0$ 이다. 

    $$ \int_{1}^{R} f(x) dx = \int_{1}^{R} \dfrac{\ln x}{x} dx $$

    에서 $\ln x = t$ 로 두면 $\dfrac{dt}{dx} = \dfrac{1}{x} \iff dt = \dfrac{dx}{x}$ 이므로 

    $$ = \int_{1}^{R} t dt = \bigg [\dfrac{1}{2} t ^{2} \bigg ] ^{R} _{1} = \dfrac{1}{2} R ^{2} - \dfrac{1}{2} $$

    이다. 그러므로 $R \to \infty \implies \int_{1}^{R}f(x) dx \to \infty$ 이므로 적분판정법에 의하여 급수 $\displaystyle \sum_{n=1}^{\infty}\dfrac{\ln n}{n}$ 이 발산한다.

    그러므로 극한비교 판정법에 의하여 주어진 급수도 발산한다.

14. $\displaystyle \sum_{n=1}^{\infty}\dfrac{1}{n \sqrt[]{(\ln n) ^{5} + 4}}$ 수렴 조사.

    $a_n = \dfrac{1}{n \sqrt[]{(\ln n) ^{5} + 4}}, b_n = \dfrac{1}{n \sqrt[]{(\ln n) ^{5}}}$ 라고 두면 

    $$ \dfrac{b_n}{a_n} = \dfrac{n \sqrt[]{(\ln n) ^{5} + 4}}{n \sqrt[]{(\ln n) ^{5}}} = \sqrt[]{\dfrac{(\ln n) ^{5} + 4}{(\ln n) ^{5}}} = \sqrt[]{\dfrac{1 + 4/ (\ln n) ^{5}}{1}} $$

    이므로 $\displaystyle \lim_{n \to \infty} \dfrac{b_n}{a_n} = 1$ 이다. 따라서 극한비교 판정법을 쓸 수 있다.

    $f(x) = \dfrac{1}{x \sqrt[]{(\ln x) ^{5}}}$ 로 두면 $f'(x) = - \dfrac{(x \sqrt[]{(\ln x) ^{5}} )'}{x ^{2} \sqrt[]{(\ln x) ^{10}}} = \dfrac{-\sqrt[]{(\ln x) ^{5}} - x (\sqrt[]{(\ln x)^{5}})'}{x ^{2} \sqrt[]{(\ln x) ^{10}}} < 0$ 이므로 $f(x)$ 는 단조감소함수이고, $f(x) \geq 0$ 이다.

    $$ \int_{1}^{R} f(x) dx = \int_{1}^{R}\dfrac{1}{x \sqrt[]{(\ln x) ^{5}}}dx $$

    에서 $\ln x = t$ 로 두면 $dt = \dfrac{dx}{x}$ 이므로 

    $$ = \int_{1}^{R}\dfrac{1}{\sqrt[]{t ^{5}}}dt = \int_{1}^{R}t ^{-5/2}dt = [- \dfrac{2}{3} t ^{-3/2}] ^{R} _{1} $$

    $$ = - \dfrac{2}{3} R ^{-3/2} + \dfrac{2}{3} = - \dfrac{2}{3} \dfrac{1}{R ^{3/2}} + \dfrac{2}{3}$$

    이다. 따라서 $R \to \infty \implies \int_{1}^{R}f(x)dx \to \dfrac{2}{3}$ 이므로 적분판정법에 의하여 급수 $\dfrac{1}{n \sqrt[]{(\ln n) ^{5}}}$ 가 수렴한다.

    그러므로 극한비교 판정법에 의하여 주어진 급수가 수렴한다.

15. $\displaystyle \sum_{n=1}^{\infty}\dfrac{\sin n}{n ^{2}}$ 수렴 조사.

    $-1 \leq \sin n \leq 1$ 이므로

    $$ -\dfrac{1}{n ^{2}} \leq \dfrac{\sin n}{n ^{2}} \leq \dfrac{1}{n ^{2}} $$

    이다. 

    $a_n = \dfrac{1}{n ^{2}}$ 에서 $f(x) = \dfrac{1}{x ^{2}}$ 로 두면 $f(x)$ 는 단조감소함수이고, $f(x) \geq 0$ 이다. 

    $$ \int_{1}^{R}f(x)dx = \int_{1}^{R}x ^{-2} dx = [-x ^{-1}] ^{R}_{1} = - \dfrac{1}{R} + 1 $$

    이므로 $R \to \infty \implies \int_{1}^{R}f(x)dx \to 1$ 이다. 그러므로 적분판정법에 의하여 급수 $\displaystyle \sum_{n=1}^{\infty}\dfrac{1}{n ^{2}}$ 가 수렴하고, 이에따라 비교 판정법에 의하여 주어진 급수도 수렴한다.