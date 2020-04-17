# [ccss17.github.io](https://ccss17.github.io)

# 확률

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률(probability) : 모든 경우의 수에 대하여 특정한 사건이 발생하는 경우의 수의 비율이다. 

  </blockquote>

  - 다시 말해 일정한 조건 아래에서 어떤 사건이 일어날 가능성을 수로 나타낸 것이다.

  - 사건 $A$ 에 대한 확률을 

    $$ P(A) $$

    로 나타낸다. 

  - 모든 경우의 수가 $n$ 이고 사건 $A$ 가 일어나는 경우의 수가 $a$ 라면 사건 $A$ 가 일어날 확률 $p$ 는 다음과 같다.

    $$ P(A) = p = \frac{a}{n} $$

  - 확률 $p$ 는 $0 \leq p \leq 1$ 이다.

  - 사건 $A$ 가 일어나지 않을 확률은 $1 - p$ 이다. 

  - 예시 

    동전을 던질 때 앞면이 나오는 가능성은 앞면, 뒷면 $2$ 가지 경우 중 $1$ 가지이므로 $\dfrac{1}{2}$ 이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 사건의 경우의 수 : 사건 $A$ 에 대한 경우의 수를 $n(A)$ 로 정의한다. 

  </blockquote>

  - 전사건의 경우의 수, 즉 표본공간 $S$ 의 원소를 

    $$ n(S) $$

    로 나타낸다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 수학적 확률(mathematical probability) : 표본공간 $S$ 안에서 각각의 근원사건이 일어날 가능성이 같을 때

  사건 $A$ 가 일어날 수학적 확률은

  $$ \boxed{P(A) = \frac{n(A)}{n(S)}}  $$

  이다.

  </blockquote>

  - 예시 

    주사위를 던졌을 때 $6$ 이 나올 수학적 확률을 구해보자.

    주사위를 던졌을 때 각각의 눈($1,2,3,4,5,6$)이 나올 경우의 수는 $6$ 이고 

    그 중에서 $6$ 이 나오는 경우의 수는 $1$ 이므로 때 $6$ 이 나올 수학적 확률은 
    
    $$\therefore \dfrac{1}{6}$$
    
    이다. ■ 

  - 예시 

    흰 공, 검은 공, 파란 공이 $2$ 개씩 들어있는 주머니에서 공 $1$ 개를 꺼낼 때 

    파란 공이 $1$ 개 나올 확률을 구해보자. 

    $6$ 개의 공에서 $1$ 개를 꺼내는 경우의 수는 ${}_{6}C_{1} = 6$ 이고 

    파란 공 $1$ 개를 꺼내는 경우의 수는 ${}_{2}C_{1} = 2$ 이므로 구하고자 하는 확률은

    $$ \therefore \frac{2}{6} = \frac{1}{3} $$

    이다. ■ 

  - 예시 

    흰 공, 검은 공, 파란 공이 $2$ 개씩 들어있는 주머니에서 공 $3$ 개를 꺼낼 때 

    흰 공, 검은 공, 파란 공이 한 개씩 나올 확률을 구해보자. 

    $6$ 개의 공에서 $3$ 개의 공을 꺼내는 경우의 수는 ${}_{6}C_{3} = 20$ 이고 

    흰 공, 검은 공, 파란 공이 한 개씩 나오는 경우의 수는 

    $$ {}_{2}C_{1} \times {}_{2}C_{1} \times {}_{2}C_{1} = 8 $$

    이므로 구하고자 하는 확률은 

    $$ \therefore \frac{8}{20} = \frac{2}{5} $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 통계적 확률 : 같은 시행을 $n$ 번 반복하여 사건 $A$ 가 일어난 횟수를 $r _{n}$ 이라 할 때 

  시행 횟수 $n$ 을 한없이 크게 함에 따라 상대도수 

  $$ \boxed{\frac{r_n}{n}}  $$

  이 다가가는 일정한 값 $p$ 를 사건 $A$ 가 일어날 통계적 확률이라 한다. 

  </blockquote>

  - 즉 통계적 확률은 

    $$ P(A) = \lim_{n \to \infty} \frac{r_n}{n} = p $$

    이고 이 극한의 수렴값은 수학적 확률과 같아진다. 
  
  - 실제 자연 현상과 사회 현상에서는 근원사건이 일어날 가능성이 매번 똑같지 않다. 따라서 실제로는 여러 번의 시행을 반복하여 얻어지는 상대도수를 통하여 근원사건의 가능성을 근사적으로 추정한다. 

  - 예시 

    농구 선수가 자유투를 성공할 확률을 구한다고 하자. 

    농구 선수가 자유투를 성공시킬 근원사건의 확률은 매번 동일하지 않다. 그때그때의 컨디션과 상황과 조건과 환경에 영향을 받기 때문이다. 

    자유투를 성공한 횟수를 $r_n$, 자유투를 던진 횟수를 $n$ 이라고 할 때 이 경우 충분한 시행 횟수를 반복하여 

    $$ \frac{r_n}{n} $$

    으로 가능성을 계산한다. 

    이때 $n$ 이 크면 클수록 가능성은 정확한 수치를 갖게 될 것이다.

    $$ \lim_{n \to \infty} \frac{r_n}{n} $$

    즉 위와 같은 수식이 정확한 가능성을 보여준다. 그러나 실제 현실에서는 농구 선수에게 무한번 자유투를 던지게 할 수 없는 노릇이니 그냥 충분한 횟수를 던지게 해야 한다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 큰 수의 법칙(law of large number) : 통계적 확률에서 시행 횟수 $n$ 이 한없이 커질 때 그 극한이 수학적 확률과 같아진다.

  </blockquote>

  - 예시 

    동전을 던져 앞면이 나오는 통계적 확률을 구한다고 하자.
    
    시행 $10$ 을 했더니 수학적 확률이 $\dfrac{2}{10}$ 이 나왔고

    시행 $20$ 을 했더니 수학적 확률이 $\dfrac{9}{20}$ 이 나왔다고 하자.

    실제로 수학적 확률은 $\dfrac{1}{2}$ 이고 시행을 무한히 반복하면 통계적 확률이 이 $\dfrac{1}{2}$ 에 가까워진다. 

    

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 기하학적 확률 : 영역 $S$ 안에서 각각의 점을 잡을 가능성이 같고 $\text{sum} (A)$ 을 영역 $A$ 의 넓이라고 할 떄

  영역 $S$ 에서 임의로 잡은 점이 영역 $A$ 에 속할 기하학적 확률은

  $$ \boxed{P(A) = \frac{\text{sum}(A)}{\text{sum}(S)}}  $$

  이다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률의 성질 : 전사건 $S$ 과 임의의 사건 $A$ 에 대하여 다음이 성립한다. 

  1. $\boxed{ 0 \leq P(A) \leq 1}$

  2. $\boxed{ P(S) = 1}$

  3. $\boxed{ P(\emptyset ) = 0}$

  </blockquote>

  - 증명 

    어떤 시행에서 일어나는 모든 경우의 수를 $n$ 이라 하고

    특정 사건 $A$ 가 일어나는 경우의 수를 $r$ 이라 하자.

    그러면 자명하게 

    $$ 0 \leq r \leq n $$ 

    이 성립한다. 이때 양변을 $n$ 으로 나누어 

    $$ 0 \leq \frac{r}{n} \leq 1 $$

    를 얻는데 $\dfrac{r}{n}$ 은 수학적 확률 $P(A)$ 이므로

    $$ \therefore  0 \leq P(A) \leq 1 $$

    를 얻는다. ■ 

    이때 전사건 $S$ 가 일어날 경우의 수는 $n$ 이므로 

    $$ \therefore  P(S) = \frac{n}{n} = 1 $$

    이다. ■  
    
    또 공사건 $\emptyset$ 가 일어날 경우의 수는 $0$ 이므로 

    $$ \therefore  P(\emptyset ) = \frac{0}{n} = 0 $$

    이다. ■ 
  
  - 예시 

    $1, 3, 5, 7, 9, 11$ 이 적혀있는 주사위를 던져 짝수가 나올 확률을 구해보자. 

    주사위에 있는 눈이 모두 홀수이므로 짝수가 나올 경우의 수는 $0$ 이고 이것은 공사건이다. 그러므로 짝수가 나올 확률은

    $$ \therefore  \dfrac{0}{6} = 0 $$

    이다. ■ 

    그러면 홀수가 나올 확률을 구해보자. 

    주사위에 있는 눈이 모두 홀수이므로 홀수가 나올 경우의 수는 $6$ 이고 이것은 전사건이다. 그러므로 홀수가 나올 확률은

    $$ \therefore  \dfrac{6}{6} = 1 $$

    이다. ■ 

### 확률의 덧셈정리

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률의 덧셈정리(addition theorem of probability) : 두 사건 $A$ 와 $B$ 가 동시에 일어나지 않을 때, 사건 $A$ 와 $B$ 가 발생할 확률을 각각 $p, q$ 라 하면 사건 $A$ 또는 $B$ 가 발생할 확률은 $p + q$ 이다. 

  </blockquote>

  - 증명 

    두 사건 집합 $A, B$ 에 대하여 합집합의 원소의 개수 

    $$ n(A \cup B) = n(A) + n(B) - n(A \cap B) $$

    가 성립함을 이미 알고 있다.

    여기에서 전사건 $n(S)$ 을 나누면

    $$ \dfrac{n(A \cup B)}{n(S)}  = \dfrac{n(A)}{n(S)}  + \dfrac{n(B)}{n(S)}  - \dfrac{n(A \cap B)}{n(S)}  $$

    을 얻는데 이것은 곧 확률이므로 

    $$ \therefore  P(A \cup B) = P(A) + P(B) - P(A \cap B) $$

    을 얻는다. ■ 

    

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률의 곱 : 두 사건 $A$ 와 $B$ 가 서로 영향을 미치지 않을 때, 사건 $A$ 와 $B$ 가 발생할 확률을 각각 $p, q$ 라 하면 사건 $A$ 또는 $B$ 가 동시에 발생할 확률은 $p \times q$ 이다. 

  </blockquote>

  - ???????? "동시에" 라는 말 때문에 혼란이 일어나는 것 같은데 서로 다른 사건을 동시에 일어나게 하는 건 순전히 전체 사건을 정의하는 사람 마음이 아닌가?

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률의 덧셈정리(addition theorem of probability) : 표본공간 $S$ 의 부분집합인 두 사건 $A, B$ 에 대하여 

  $$ P(A \cup B) = P(A)+P(B)-P(A \cap B) $$

  이다. 

  </blockquote>

  - 두 사건 $A, B$ 가 배반사건이면, 즉 $A \cap B = \emptyset$ 이면 

    $$ P(A \cup B) = P(A)+P(B) $$

    이다.

  - 증명 

    **구체화 필요**

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 여사건의 확률 : 표본공간 $S$ 의 부분집합인 사건 $A$ 의 여사건 $A ^{C}$ 가 일어날 확률은 

  $$ P(A ^{C}) = 1 - P(A) $$

  이다. 

  </blockquote>

  - 증명 

    **구체화 필요**

### 조건부 확률 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 조건부확률(conditional probability) : 확률이 $0$ 이 아닌 사건 $A$ 가 일어났다고 가정할 때

  사건 $B$ 가 일어날 확률은 사건 $A$ 가 일어났을 때의 사건 $B$ 의 조건부확률이라 한다.

  </blockquote>

  - 기호로 $P(B|A)$ 로 나타낸다.

  - 조건부 확률의 값은

    $$ P(B|A) = \frac{n(A \cap B)}{n(A)} = \frac{P(A \cap B)}{P(A)} $$

    이다.

  - 사건 $A$ 가 일어나지 않으면 $P(B|A)$ 는 의미가 없기에 $P(A) \neq 0$ 인 경우만 생각하는 것이다. 

  - 예시 

    **구체화 필요**

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률의 곱셈정리 : $P(A) \neq 0, P(B) \neq 0$ 일 때 두 사건 $A, B$ 가 동시에 일어날 확률은 

  $$ P(A \cap B) = P(A)P(B|A) = P(B)P(A|B) $$

  이다. 

  </blockquote>

  - 예시 

    **구체화 필요**

## 사건의 독립과 종속

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 독립사건(independent) : 두 사건 A 와 B 에서 한 사건의 결과가 다른 사건에 영향을 주지 않을 때 A 와 B 를 독립사건이라 한다. 

  </blockquote>

  - 즉 다음 등식이 성립하면 두 사건 $A, B$ 는 서로 독립이다. 

    $$ P(B|A) = P(B) $$

    또는 

    $$ P(A|B) = P(A) $$

    또는 

    $$ P(B|A ^{C}) = P(B) $$

    또는 

    $$ P(A|B ^{C}) = P(A) $$

  - $P(A) \neq 0, P(B) \neq 0$ 인 두 사건 $A, B$ 가 독립일 필요충분조건은 

    $$ P(A \cap B) = P(A)P(B) $$

    이다. 

  - 예시 

    동전을 던지는 사건과 주사위를 던지는 사건 

  - 예시 

    **구체화 필요**

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 종속사건(dependent) : 두 사건 A 와 B 에서 한 사건의 결과가 다른 사건에 영향을 줄 때 A 와 B 를 종속사건이라 한다. 

  </blockquote>

  - 즉 다음 등식이 성립하면 두 사건 $A, B$ 는 서로 독립이다. 

    $$ P(B) \neq P(B|A), P(A) \neq P(A|B) $$

  - 예시 

    **구체화 필요**

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 독립시행(independent trials) : 동일한 시행을 반복하여 나타나는 시행의 결과가 서로 독립일 때, 이 시행을 독립시행이라고 한다.

  </blockquote>

  - 매회 시행에서 사건 $A$ 가 일어날 확률을 $p$, 일어나지않을 확률을 $q$ 라 할 때 

    $$ p + q = 1 \Leftrightarrow  q = 1 -p $$

    이다.

  - $n$ 회 반복하는 독립시행에서 사건 $A$ 가 $r$ 회 일어날 확률 $P_r$ 은 $r = 0, 1, 2, \dots, n$ 에 대하여

    $$ P_r = {}_{n}C_{r}p ^{r} q ^{n-r} $$

    이다. 

  - 예시 

    **구체화 필요**

## 전확률 공식과 베이즈 정리 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 전확률 공식(total probability) : 공사건이 아닌 $n$ 개의 사건 $A_1, A_2, \dots, A_n$ 이

  표본공간 $S$ 와 $i, j = 1, 2, \dots, n$ 이고 $i \neq j$ 인 $i, j$ 에 대하여 다음 두 조건을 만족할 때 

  $$ A_i \cap A_j = \emptyset $$

  $$ A_1 \cup A_2 \cup \dots \cup A_n = S $$

  공사건이 아닌 사건 $B (\subset S)$ 가 일어날 확률 $P(B)$ 는 

  $$ P(B) = \sum_{k=1}^{n}P(A_k)P(B|A_k) = P(A_1)B(B|A_1) +P(A_2)B(B|A_2)+\dots +P(A_n)B(B|A_n) $$

  이다. 

  </blockquote>

  - 예시 

    **구체화 필요**

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 베이즈 정리(bayes theorem) : 전확률 공식의 정의의 전제조건을 만족할 때 사건 $B$ 가 일어났을 때 사건 $A_i$ 의 조건부확률은 

  $$ P(A_i|B) = \frac{P(B \cap A_i)}{P(B)} = \frac{P(A_i)P(B|A_i)}{\displaystyle \sum_{k=1}^{n}P(A_k)P(B|A_k)} $$

  이다.

  </blockquote>

### 몬티홀 문제

어떤 게임 쇼는 게임 참가자에게 세 개의 문 중에서 하나를 고르라고 한다. 한 문 뒤에는 자동차가, 두 문 뒤에는 염소가 있고 그 중에서 자동차가 있는 문을 선택하면 참가자는 자동차를 얻을 수 있다. 

이때 참가자가 하나의 문을 선택했는데 진행자가 나머지 두 문 중 염소가 있는 한 문을 보여주고 다시 선택할 기회를 주었다고 하자. 그러면 자동차를 얻기 위하여 다시 선택하는 것이 좋을까 아니면 처음 했던 선택을 고수하는 것이 좋을까? 

자동차를 $S$, 염소를 $T$ 이라고 하자.

| | 처음 선택한 문 | 다른 문 $1$ |다른 문 $2$ |선택을 바꿨을 때 자동차 획득 여부|
|:---:|:---:|:---:|:---:|:---:|:---:|
| 경우 $1$  | $S$ | $T$ | $T$ | X | 
| 경우 $2$  | $T$ | $S$ | $T$ | O | 
| 경우 $3$  | $T$ | $T$ | $S$ | O | 

위 표에서 볼 수 있듯이 출연자가 선택을 바꾸면 자동차를 얻을 확률이 $\dfrac{1}{3}$ 에서 $\dfrac{2}{3}$ 으로 높아진다. 

그런데 이때 염소에 번호를 매겨보자.

| | 처음 선택한 문 | 다른 문 $1$ |다른 문 $2$ |선택을 바꿨을 때 자동차 획득 여부|
|:---:|:---:|:---:|:---:|:---:|:---:|
| 경우 $1$  | $S$ | $T_1$ | $T_2$ | X | 
| 경우 $2$  | $S$ | $T_2$ | $T_1$ | X | 
| 경우 $3$  | $T_1$ | $S$ | $T_2$ | O | 
| 경우 $4$  | $T_1$ | $T_2$ | $S$ | O | 
| 경우 $5$  | $T_2$ | $S$ | $T_1$ | O | 
| 경우 $6$  | $T_2$ | $T_1$ | $S$ | O | 

처음 선택했을 때 자동차를 얻을 확률이 $\dfrac{2}{6} = \dfrac{1}{3}$ 이었지만 선택을 바꾸었을 때 자동차를 얻을 확률이 $\dfrac{4}{6} = \dfrac{2}{3}$ 으로 높아졌다. 

이제 문의 순서를 생각하지 말아보자. 

| | 처음 선택한 문 | 다른 문 |다른 문|선택을 바꿨을 때 자동차 획득 여부|
|:---:|:---:|:---:|:---:|:---:|:---:|
| 경우 $1$  | $S$ | $T_1$ | $T_2$ | X | 
| 경우 $2$  | $T_1$ | $S$ | $T_2$ | O | 
| 경우 $3$  | $T_2$ | $S$ | $T_1$ | O | 

아, 하지만 자유의지에 의하여 임의의 문을 선택할 수 있다는 것은 문을 특정할 수 있다는 전제가 필요하다. 그런데 문의 순서를 없애면 문을 특정할 수 없으므로 의도적으로 임의의 문을 선택할 수 있다는 조건에 위배된다. 따라서 문의 순서는 항상 있어야 한다. 그러므로 위의 표로 나타낸 경우의 수들은 존재 자체가 성립되지 않는다. 

| | 문 $1$ | 문 $2$ |문 $3$ |자동차 획득 여부|
|:---:|:---:|:---:|:---:|:---:|:---:|
| 선택 $1$, 바꿈 O  | $S$ | $T$ | $T$ | X | 
| 선택 $1$, 바꿈 X  | $S$ | $T$ | $T$ | O | 
| 선택 $2$, 바꿈 O  | $S$ | $T$ | $T$ | O | 
| 선택 $2$, 바꿈 X  | $S$ | $T$ | $T$ | X | 
| 선택 $3$, 바꿈 O  | $S$ | $T$ | $T$ | O | 
| 선택 $3$, 바꿈 X  | $S$ | $T$ | $T$ | X | 
| 선택 $1$, 바꿈 O  | $T$ | $S$ | $T$ | O | 
| 선택 $1$, 바꿈 X  | $T$ | $S$ | $T$ | X | 
| 선택 $2$, 바꿈 O  | $T$ | $S$ | $T$ | X | 
| 선택 $2$, 바꿈 X  | $T$ | $S$ | $T$ | O | 
| 선택 $3$, 바꿈 O  | $T$ | $S$ | $T$ | O | 
| 선택 $3$, 바꿈 X  | $T$ | $S$ | $T$ | X | 
| 선택 $1$, 바꿈 O  | $T$ | $T$ | $S$ | O | 
| 선택 $1$, 바꿈 X  | $T$ | $T$ | $S$ | X | 
| 선택 $2$, 바꿈 O  | $T$ | $T$ | $S$ | O | 
| 선택 $2$, 바꿈 X  | $T$ | $T$ | $S$ | X | 
| 선택 $3$, 바꿈 O  | $T$ | $T$ | $S$ | X | 
| 선택 $3$, 바꿈 X  | $T$ | $T$ | $S$ | O | 

위의 $18$ 가지 경우의 수는 선택을 바꾼 $9$ 가지 경우와 바꾸지 않은 $9$ 가지 경우로 구분된다.

$9$ 가지의 선택을 바꾸었을 경우에 대하여 자동차를 획득할 수 있는 경우는 $6$, 획득할 수 없는 경우는 $3$ 경우이다.

반면 $9$ 가지의 선택을 바꾸지 않을 경우에 대하여 자동차를 획득할 수 있는 경우는 $3$, 획득할 수 없는 경우는 $6$ 가지이다. 

따라서 선택을 바꾸었을 때 자동차를 획득할 수 있는 확률은 $\dfrac{6}{9} = \dfrac{2}{3}$ 이고 선택을 바꾸지 않았을 때 자동차를 획득할 수 있는 확률은 $\dfrac{3}{9} = \dfrac{1}{3}$ 이다. 

