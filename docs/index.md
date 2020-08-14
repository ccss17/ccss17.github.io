# Home

!!! tldr ""

    $n$ 차 단항 함수 $y=x^n$ 의 부정적분 : $n \neq 1$ 인 실수일 때
    
    $$ \int_{}^{}x ^{n} dx = \frac{1}{n+1}x ^{n+1}+C $$
    
    이고, $n = 1$ 일 때 
    
    $$ \int_{}^{} \frac{1}{x} dx = \ln |x| + C $$
    
    이다.

- 증명

    $n \neq -1$ 일 때, 함수 $y= x ^{n}$ 의 미분법에서 

    $$ \bigg( \frac{1}{n+1}x ^{n+1}\bigg)' = x ^{n} $$

    이므로 부정적분의 정의에 의하여 

    $$ \therefore  \int_{}^{}x ^{n} dx = \frac{1}{n+1}x ^{n+1}+C $$

    이고, $n = -1$ 일 때 로그함수의 미분법에서 $(\ln |x|)' = \frac{1}{x}$ 이므로 부정적분의 정의에 의하여

    $$ \therefore \int_{}^{} \frac{1}{x} dx = \ln |x| + C $$

    이다. 

- 예시 

    $$ \int_{}^{}\frac{1}{x^2}dx = \int_{}^{}x ^{-2}dx = \frac{1}{-2+1}x ^{-2+1}+C = -\frac{1}{x}+C $$