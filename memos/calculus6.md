# [ccss17.github.io](https://ccss17.github.io)

# Calculus6 Memo

# 상미분과 편미분 

실제로 많은 함수들이 하나의 독립 변수에 의존하는 것이 아니라 두 개 이상의 독립 변수에 종속되기 때문에 많은 경우 일변수 함수에 대한 미분을 다변수 함수로 확장한 미분이 필요하다.

- 상미분(ordinary derivative) : 변수가 하나만 있는 함수에 대한 미분이다.

  - 지금까지 해오던 미분이 바로 상미분이다. 

- 편미분(partial derivative) : 다변수 함수의 특정 변수를 제외한 나머지 변수를 상수로 취급하여 미분하는 것이다.

  - 변수 $x$ 에 대한 다변수 함수 $f(x, y, \dots)$ 의 편미분을 

    $$ f'_x, f_x, \partial _x f, \frac{\partial }{\partial x}f, \frac{\partial f}{\partial x} $$

    등의 형식 언어로 표기한다.

    - 혹은 함수로서 편미분이 종속되는 변수를 강조하기 위해 

      $$ f'_x(x, y, \dots), \frac{\partial f}{\partial x}(x, y, \dots) $$

      로 표기할 수도 있다. 

  - 예시 

    밑면의 반지름이 $r$, 높이가 $h$ 인 원뿔의 부피 $V$ 는 

    $$ V = \frac{\pi r ^{2}h}{3} $$

    으로써 두 독립변수 $r, h$ 에 의존하는 종속변수이다.
    
    이 $V$ 를 다변수 함수로 보고 $r$ 에 대해 편미분하면

    $$ \frac{\partial V}{\partial r} = \frac{2 \pi rh}{3} $$

    이고 $h$ 에 대해 편미분하면

    $$ \frac{\partial V}{\partial h} = \frac{\pi r ^{2}}{3} $$

    이다.

    