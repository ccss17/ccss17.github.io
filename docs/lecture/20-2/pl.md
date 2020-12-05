# programming language

![](https://upload.wikimedia.org/wikipedia/commons/2/25/Genealogical_tree_of_programming_languages.svg)

## Why

프로그래밍 언어의 기본 원리를 배워서 다른 언어를 빠르게 습득할 수 있도록 하고, 프로그래밍 언어의 기본 설계를 어떻게 해야 하는지 알 수 있도록.

## How

인터프리터를 구현하면서.

인터프리터를 만들면서 언어를 이해해본다. 인터프리터는 컴파일러로도 변환된다. 다음 두 프로그램 실행 유형을 보자.

- Program &rarr; Parser &rarr; Interpreter &rarr; Results

- Program &rarr; Compiler &rarr; Running on a computer &rarr; Results

이 인터프리터를 다음과 같은 과정을 통하여 맹글어 볼 것이다.

1. Racket tutorials

2. Modeling languages

3. Interpreting arithmetic

4. Language principles

    - Substitution

    - Function

    - Deferring Substitution

    - First-class Functions

    - Laziness

    - Recursion

    - Mutable data structures

    - Variables

    - Continuations

    - Garbege collection

    - Semantics

    - Type

# 프로그래밍 언어의 기초 구성요소

- Numbers and Arithmetic

- Variables and Functions

- Conditional Expressions

- Conditional Functions

- Symbols

- Type Definitions

- Type Deconstruction

- Lists

# Racket 기본 문법

```racket
(operator operand1 operand2 ...)
```

!!! example

    ```racket
    (+ 1 2) ; Summate 1, 2
    ```

    ```racket
    (define (f x) (+ 1 x))
    ```

    ```racket
    (f 3)
    ```

## Numbers and Arithmetic

```racket
(+ 1 2 3)
(max 1 4 3)
```

## Variables and Functions

```racket
; define a function
(define (function-name param1 param2 ...)
    body)
```

```racket
; call the function
(function-name args1 args2 ...)
```

!!! example

    ```racket
    (define (sqr a)
        (* a a))
    ```

## Conditional Expressions

!!! example

    ```racket
    (and (> 4 3) (<= 10 100))
    (or (> 4 3) (<= 10 100))
    (not (= 4 3))
    ```

## Conditional Functions

```racket
(define (function-name param1 param2 ...)
    (cond 
        [ce1 body1]
        [ce2 body2]
        ...
        [else body]))
```

!!! example

    ```racket
    (define (interest-rate amount)
        (cond
            [(<= amount 1000) 0.040]
            [(<= amount 5000) 0.045]
            [else 0.050]))
    ```

## Symbols

Racket 에서의 심볼이란 따옴표 뒤에 나오는 식별자이다.

!!! example

    ```racket
    'the
    'dog
    'cat
    'two^3
    ```

심볼에는 오직 한 가지의 연산자 `symbol=?` 만이 적용된다.

!!! example

    ```racket
    (define (reply s)
        (cond
            [(symbol=? s 'GoodMorning) 'Hi]
            [(symbol=? s 'HowAreYou?) 'Fine]
            [(symbol=? s 'GoodAfternoon) 'INeedANap]
            [(symbol=? s 'GoodEvening) 'BoyAmITired]))
    ```

## Type Definitions

타입: 데이터의 추상적 정의이다. Java 에서 `class` 와 비슷한 개념이다.

Racket 의 타입 정의:

```racket
(define type-id
    [variant_id1 (field11 contract_expr11)
                 ...
                 (field1n contract_expr1n)
    [variant_id2 (field21 contract_expr21)
                 ...
                 (field2n contract_expr2n)
    ...
    [variant_idm (fieldm1 contract_exprm1)
                 ...
                 (fieldmn contract_exprmn)])
```

생성자 `variant_id1` 은 variant 를 정의한다. 각각의 생성자들은 variant 를 초기화하는 파라미터를 받는다. `field` 의 자료형은 `contract_expr` 로 검증된다.

`type_id?` 와 `variant_id?` 로 타입을 검사할 수 있고, `variant_id-field_id` 로 `field` 에 접근할 수 있다.

!!! example

    ```racket
    (define-type human
        [mother (name string?)
                (age number?)
                (job string?)
        [father (name string?)
                (age number?)
                (hobby string?)
        [child (name (list of string?))
               (first integer?)])
    
    (mother "A" 40 "B")
    (child '("A" "B") 1)
    (define m (mother "A" 40 "B"))
    (human? m)
    (mother? m)
    (mother-name? m)
    ```

## Type Deconstruction

Type Deconstruction 을 통하여 주어진 타입의 특정 값을 가져오거나 특정한 task 를 수행할 수 있다.

```racket
(type-case type-id expr
    [variant_id1 (field_id11 ...) expr1]
    ...
    [variant_idm (field_idm1 ...) exprm])
```

!!! example

    ```racket
    (define-type GUI
        [label (text string?)]
        [button (text string?)
                (enabled? boolean?)]
        [choice (items (listof string?))
                (selected integer?)])
    
    (define ch (choice '("Apple" "Strawberry" "Banana") 0))
    (choice? ch)
    (GUI? ch)
    (choice-selected ch)

    (define (GUI-to-list g)
        (type-case GUI g
            [label (t) (list t)]
            [button (t e?) (list t)]
            [choice (i s) i]))
    ```

## Lists

배열과 같은 개념의 데이터 구조이다.

!!! example

    ```racket
    (list 1 2 3)
    '(1 2 3)
    ```

List 생성:

```racket
(cons 1 empty)                  ; -> (list 1)
(list 1 2 3)                    ; -> (list 1 2 3)
'(1 2 3)
```

List 확장:

```racket
(append (list 1 2) empty)       ; -> (list 1 2)
(append (list 1 2) (list 3 4))  ; -> (list 1 2 3 4)
```

List 접근:

```racket
(first (list 1 2 3))            ; 1
(rest (list 1 2 3))             ; (list 2 3)
map, foldl, foldr, filter
```

# Modeling Syntax

인터프리터를 짜면서 프로그래밍 언어를 이해해보자고 했었다. 근데 프로그래밍 언어에서 가장 중요한 것은 문법이니 문법부터 짜볼 것이다.

expression 의 종류는 다음 세 가지이고, 프로그래밍 언어는 이것들 중 최소한 하나 이상을 사용한다.

- concrete syntax

    - infix: `3 + 4`

    - postfix: `3 4 +`

    - parenthesized prefix: `(+ 3 4)`

이 문법을 트리 형태로 다음과 같이 추상화된 일반 형태로 표현할 수 있다.

- abstract syntax

    ```
            3 ┬ 4
            +
    ```

## Modeling Arithmetic Expression

먼저 parenthesized prefix 로 AE(Arithmetic Expression) 를 다음과 같이 설계해보자.

```racket
(define-type AE
    [num (n number?)]
    [add (lhs AE?)
         (rhs AE?)]
    [sub (lhs AE?)
         (rhs AE?)])
```

이 설계를 통하여 다음과 같은 덧셈, 뺄셈 연산 표현이 가능해진다.

!!! example

    ```racket
    (add (num 1) (num 1))
    (sub (num 1) (num 1))
    (sub (add (num 1) (num 1)) (num 1))
    ```

# Parser

파서는 Interpreter 또는 Compiler 의 한 컴포넌트이다. 파서는 concrete syntax 를 abstract syntax 로 변환해주는 역할을 한다.

그러므로 파서를 설계하기에 앞서 concrete syntax 의 명확한 상세가 필요하다. 이를 위하여 일반적으로 Backus-Naur Form(BNF) 가 사용된다.

한편 BNF 는 concrete syntax 를 명확하게 정의해줄 뿐만 아니라 abstract syntax 까지 명시해주기 때문에 다른 언어들에서도 널리 사용된다.

- https://users-cs.au.dk/amoeller/RegAut/JavaBNF.html

- https://cs.wmich.edu/~gupta/teaching/cs4850/sumII06/The%20syntax%20of%20C%20in%20Backus-Naur%20form.htm

- https://docs.python.org/3/reference/grammar.html


## Backus-Naur Form

BNF 를 통해 grammer 를 대수적으로 표현할 수 있다.

```bnf
<expr> ::= (<expr> + <expr>)
         | (<expr> - <expr>)
         | <num>
<num>  ::= 1, 42, 17, ...
```

- `<var>` 은 재귀적으로 사용할 수 있는 메타 변수이다.

- `::=` 는 "Can be written as" 라는 뜻이다.

- `|` 는 또 다르게 "Can be written as" 될 수 있다는 것이다.

BNF 에서 `<expr>` 같은 메타 변수들은 집합을 정의하게 된다.

!!! example

    `<num>` 은 모든 숫자의 집합을 의미하게 된다. 그러므로 

    $$ 2 \in \text{<num>} \\ 298 \in \text{<num>} $$

    와 같이 표현할 수 있다.

위에서 정의한 BNF 에서 `<expr> ::= (<expr> + <expr>)` 는 덧셈 연산을 정의한 것이고, `| (<expr> - <expr>)` 는 뺄셈 연산을, `| <num>` 은 숫자를 정의한 것이다. 

그러므로 

$$ (\text{<expr>} + \text{<expr>}) \\ 8 \in \text{<num>} \subset \text{<expr>} \\ (8 + 8) \in \text{<expr>} \\ $$

등과 같이 표현할 수 있다.

## BNF for AE

우리는 간단한 산술 연산을 할 수 있는 AE 를 정의했는데, 이를 통하여 

```racket
(+ (- 3 4 ) 7)
```

과 같은 연산을 할 수 있길 원한다. 그러므로 BNF 를 

```
<AE> ::= (<AE> + <AE>)
         | (<AE> - <AE>)
         | <num>
```

와 같이 정의하면 된다.

## Implementation Parser

지금까지 BNF 를 통해 concrete syntax 를 명확하게 정의해보았다. Parser 의 역할이란 concrete syntax 를 abstract syntax 로 변환해주는 것이라고 하였다. 이 abstract syntax 가 Interpreter 로 입력되고 Interpreter 는 그것을 수행하여 결과를 출력하게 된다.

input(concrete syntax(code)) &rarr; Parser &rarr; abstract syntax &rarr; Interpreter &rarr; output

그러므로 Parser 는 기술적으로 expression 을 받아서 AE 로 변환하는 프로그램이다.

!!! example

    그러므로 Parser 는 다음과 같은 기능을 하게 된다.

    ```racket
    (test (parse '3) (num 3))
    (test (parse '{+ 3 4}) (add (num 3) (num 4)))
    (test (parse '{- 4 3}) (sub (num 4) (num 3)))
    (test (parse '{+ {+ 4 3} {- 4 3}}) (add (add (num 4) (num 3)) (sub (num 4) (num 3))))
    ```

이 Parser 는 다음과 같이 입력된 데이터의 타입에 따라서 그 데이터를 해당 AE 로 변환해주는 프로그램으로 구현할 수 있다. 

```racket
(define (parse sexp)
    (cond 
        [(number? sexp) (num sexp)]
        [(eq? (first sexp) '+) (add (parse (second sexp)) 
                                    (parse (third sexp)))]
        [(eq? (first sexp) '-) (sub (parse (second sexp)) 
                                    (parse (third sexp)))]))
```

이 프로그램은 

```racket
(test (parse '3) (num 3))
(test (parse '{+ 3 4}) (add (num 3) (num 4)))
```

와 같은 입력을 잘 처리한다. 그러나 `(parse '{+ 3 4 5})` 와 같은 입력은 잘 처리하지 못한다. 그러므로 `sexp` 리스트의 길이가 `3` 이어야 한다는 조건을 추가하고, 그 이외의 입력은 에러로 처리하는 Parser 를 다음과 같이 구현할 수 있다.

```racket
(define (parse sexp)
    (cond 
        [(number? sexp) (num sexp)]
        [(and (= 3 (length sexp)) (eq? (first sexp) '+))
         (add (parse (second sexp)) (parse (third sexp)))]
        [(and (= 3 (length sexp)) (eq? (first sexp) '-))
         (sub (parse (second sexp)) (parse (third sexp)))]
        [else (error 'parse "bad syntax")]))
```

# Interpreter

우리는 concrete syntax(code) 를 받아서 abstract syntax(AE) 로 변환하는 Parser 를 구현해보았다. 그러면 이제 abstract syntax 를 받아서 실행하고 결과를 출력하는 Interpreter 를 구현할 차례이다. 

Interpreter 구현에 있어서 Type Deconstruction 이 사용된다. Type Deconstruction 이 abstract syntax(AE) 의 타입에 따라 특정 task 를 수행해주기 때문이다. 

## Implementation Interpreter

Type Deconstruction 을 기반으로 다음과 같이 Interpreter 를 구현할 수 있다. 이 Interpreter 는 AE 를 받아서 특정 task 를 수행한다.

```racket
; interp: AE -> number
(define (interp an-ae)
    (type-case AE an-ae
        [num (n) n]    
        [add (l r) (+ (interp l) (interp r))]
        [sub (l r) (- (interp l) (interp r))]))
```

이 Interpreter 와 Parser 를 통해 다음과 같은 산술 연산을 수행할 수 있다. 

!!! example

    ```racket
    (test (interp (parse '3)) 3)
    (test (interp (parse '{+ 3 4})) 7)
    (test (interp (parse '{+ {- 3 4} 7})) 6)
    ```

    `parse` 는 concrete syntax(code) 를 abstract syntax(AE) 로 변환하고, `interp` 는 abstract syntax(AE) 를 받아서 task 를 수행한다. 

# Substitution

이제 기본적인 Parser, Interpreter 는 완성되었다. 이것들을 업그레이드 해나갈 건데, 먼저 Substitution 을 지원하는 Interpreter 를 만들어볼 것이다.

Substitution 은 반복되는 expression 을 불필요하게 계산하지 않도록 도입된 개념이다.

!!! example

    ```c
    int totalSum = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10) + (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10) + (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10);
    ```

    이 코드는 불필요한 연산이 2번 반복된다. 이 코드를 다음과 같이 최적화할 수 있다.

    ```c
    int partialSum = 1 + 2 + 3+ 4 + 5 + 6 + 7 + 8 + 9 + 10;
    int totalSum = partialSum + partialSum + partialSum;
    ```

이것이 Substitution 인데, Substitution 을 위해서는 identifier 가 필요하다. identifier 는 계산된 결과를 저장하는 장소이다. 위 예시에서 `partialSum` 이 identifier 이다.

## Identifier

Identifier 란 expression 의 값의 이름이다. 이 이름(identifier)을 다른 곳에서 다시 사용할 수 있다.

변수 vraiable 과 비슷한 개념이지만, 변수는 그 값이 변할 수 있다는 것에서 차이가 있다. Identifier 의 값은 불변한다.

가령 

```racket
(+ (+ 5 5) (+ 5 5))
```

와 같은 프로그램에서 `(+ 5 5)` 가 중복 계산되므로 이것을 identifier 에 저장하여 재사용하면 Substitution 을 하는 것이다. 이제 `with` 이라는 키워드가 identifier 를 정의한다고 하자. 그러면 위 프로그램을 다음과 같이 Substitution 할 수 있다.

```racket
(with (x (+ 5 5)) (+ x x))
```

이처럼 identifier 를 지원하는 AE 를 WAE 라고 하자.

## Concrete Syntax for WAE (BNF)

WAE 의 BNF 를 다음과 같이 만들 수 있다.

```
<WAE> ::= (<WAE> + <WAE>)
         | (<WAE> - <WAE>)
         | <num>
         | (with (<id> <WAE>) <WAE>)
         | <id>
<id> ::= x, y, plus, factorial, ...
```

단지 기존의 AE 의 BNF 에 2 가지가 추가된 것이다. `| (with (<id> <WAE>) <WAE>)` 를 통하여 identifier 를 사용할 수 있게 되고 `| <id>` 를 통하여 identifier 를 WAE 로 정의할 수 있게 되었다. 

## Identifier Type

```racket
(with (x (+ 1 2))
      (+ x x))
```

의 결과는 6 이다. 이떄 `(with (x (+ 1 2))` 에서 identifier `x` 는 Binding instance 이고 `(+ x x))` 에서 identifier `x` 는 Bound instance 이다.

만약 

```racket
(with (x (+ 1 2))
      (+ x y))
```

와 같이 되어있다면 `y` 라는 정의되지 않은 identifier 가 사용되었으므로 에러가 발생한다. 이 `y` 를 free identifier 라고 한다.

## Abstarct Syntax for WAE

WAE 를 구현하기 위하여 먼저 WAE 라는 abstract syntax 를 정의하자.

```racket
(define-type WAE
    [num (n number?)]
    [add (lhs WAE?) (rhs WAE?)]
    [sub (lhs WAE?) (rhs WAE?)]
    [with (name symbol?) (named-expr WAE?) (body WAE?)]
    [id (name symbol?)])
```

## Implement Parser for WAE

WAE 를 정의했으니 code(concrete syntax) 를 abstract syntax(WAE) 로 변환해주는 Parser 를 구현해보자.

```racket
(define (parse sexp)
  (cond
       [(number? sexp) (num sexp)]
       [(and (= 3 (length sexp)) (eq? (first sexp) '+))
                            (add (parse (second sexp)) (parse (third sexp)))]
       [(and (= 3 (length sexp)) (eq? (first sexp) '-))
                            (sub (parse (second sexp)) (parse (third sexp)))]
       [... (with ...)]
       [... (id ...)]
       [else (error 'parse "bad syntax:~a" sexp)]))
```

일단은 AE 를 위한 `parse` 를 기반으로 위와 같이 스켈레톤 코드를 짜볼 수 있을 것이다. 그런데 위 코드는 racket 의 `match` 키워드를 사용하여 최적화시킬 수 있다. 또한 동시에 `with` 와 `id` 의 케이스도 구현해보자.

```racket
(define (parse sexp)
  (match sexp
       [(? number?)    (num sexp)]
       [(list '+ l r)  (add (parse l) (parse r))]
       [(list '- l r)  (sub (parse I) (parse r))]
       [(list 'with (list i v) e) (with i (parse v) (parse e))]
       [(? symbol?) (id sexp)]
       [else (error 'parse "bad syntax:~a" sexp)]))
```

이 파서는 다음과 같이 concrete syntax(code) 를 abstract syntax(WAE) 로 바꿔준다.

!!! example

    ```racket
    (test (parse '{+ {- 3 4} 7}) (add (sub (num 3) (num 4)) (num 7)))
    (test (parse '{with {x 5} {+ 8 2}}) (with 'x (num 5) (add (num 8) (num 2))))
    (test (parse '{with {x 5} {+ x x}}) (with 'x (num 5) (add (id 'x) (id 'x))))
    ```

## Implement Substitution

Parser 를 구현했으니 이제 Interpreter 를 구현하면 된다. 하지만 그전에 Substitution 을 구현해야 한다. 이 Substitution 이 Interpreter 로 전달되는 WAE 의 identifier 를 모두 identifier 가 아닌 WAE 로 바꿔준다. 그러면 Interpreter 는 순수한 산술 연산 코드만 받고 산술 연산만 진행할 수 있다.

이 Substitution 을 함수 `subst` 로 구현할 것이다. 이 함수는 다음과 같은 기능을 하게 된다.

```racket
; {with {x 10} 5}              ⇒        10 for x in 5               ⇒ 5
(test (subst (num 5) 'x 10)   (num 5)) 
; {with {x 10} {+ 1 x}}         ⇒        10 for x in {+ 1 x}     ⇒  {+ 1 10}
(test (subst (add (num 1) (id 'x)) 'x 10)   (add (num 1) (num 10)))
; {with {x 10} x}                   ⇒        10 for x in x           ⇒ 10
(test (subst (id 'x) 'x 10)   (num 10))
; {with {x 10} y}                  ⇒         10 for x in y          ⇒   y (no substitution)
(test (subst (id 'y) 'x 10)   (id 'y))
```

`subst` 를 다음과 같이 구현할 수 있다.

```racket
(define (subst wae idtf val)
    (type-case WAE wae
        [num    (n)        wae]
        [add    (l r)      (add (subst l idtf val) (subst r idtf val))]
        [sub    (l r)      (sub (subst l idtf val) (subst r idtf val))]
        [with   (i v e)    (with i (subst v idtf val) (if (symbol=? i idtf) e
                                   (subst e idtf val)))]
        [id     (s)        (if (symbol=? s idtf) (num val) wae)]))
```

## Implement Interpreter for WAE

`subst` 를 기반으로 WAE 를 위한 Interpreter 를 다음과 같이 구현할 수 있다.

```racket
; interp: WAE -> number
(define (interp wae)
    (type-case WAE wae
        [num (n) n]
        [add (l r) (+ (interp l) (interp r))]
        [sub (l r) (- (interp l) (interp r))]
        [with (i v e) (interp (subst e i (interp v)))]
        [id (s)        (error 'interp "free identifier")]))
```

이 WAE Interpreter 를 다음고 같이 사용할 수 있다.

```racket
(test (interp (with 'x (num 5) (add (id 'x) (id 'x)))) 10)
```

# Function

이제 지금까지 만들어본 WAE 가 함수를 지원하도록 할 것이다. 따라서 우리의 프로그래밍 언어는 다음과 같이 발전해왔다.

AE &rarr; WAE &rarr; F1WAE

그러면 먼저 함수의 concrete syntax 와 abstract syntax 를 정의해보자.

## Concrete Syntax for Function (BNF)

먼저 간단한 함수 

$$ \text{identity}(x) = x \\ \text{twice}(x) = x + x $$

를 생각하자. twice 함수를 AE 로 표현하면 다음과 같다. 

```racket
(+ 10 10)
(+ 17 17)
```

twice 함수를 WAE 로 표현하면 다음과 같다.

```racket
(with (x 10) (+ x x))
(with (x 17) (+ x x))
```

이제 F1WAE 로 identity 함수와 twice 함수를 다음과 같은 concrete syntax 로 표현하기로 해보자.

```racket
(deffun (identity x) x)
(deffun (twice x) (+ x x))
```

그러면 다음과 같이 이 함수를 사용할 수 있다. 

```racket
(identity 8)
(twice 10)
(twice 17)
```

이 concrete syntax 를 BNF 로 정의해보자.

```
<FunDef> ::= {deffun {<id> <id>} <F1WAE>}
<F1WAE> ::= <num>
            | {+ <F1WAE> <F1WAE>}
            | {- <F1WAE> <F1WAE>}
            | {with {<id> <F1WAE>} <F1WAE>}
            | <id>
            | {<id> <F1WAE>}
```

`<FunDef> ::= {deffun {<id> <id>} <F1WAE>}` 가 함수 정의를 위한 규칙이고, `| {<id> <F1WAE>}` 는 함수 호출을 위한 규칙이다. 

## Abstarct Syntax for Function

concrete syntax 가 Parser 에 의하여 변환될 abstract syntax 를 다음과 같이 정의할 수 있다.

```racket
(define-type FunDef
    [fundef (fun-name symbol?)
            (arg-name symbol?)
            (body F1WAE?)])

(define-type F1WAE
    [num    (n number?)]
    [add     (lhs F1WAE?) (rhs F1WAE?)]
    [sub     (lhs F1WAE?) (rhs F1WAE?)]
    [with    (name symbol?) (named-expr F1WAE?) (body F1WAE?)]
    [id        (name symbol?)]
    [app     (ftn symbol?)    (arg F1WAE?)])
```

함수 정의를 위하여 `FunDef` 를 추가했고, 함수 호출을 위하여 `[app     (ftn symbol?)    (arg F1WAE?)])` 가 추가되었다. 

이를 통해 다음과 같이 함수 선언 및 호출을 할 수 있다.

```racket
(fundef    'identify 'x (id 'x))
(app 'identity (num 8))

(fundef 'twice 'x (add (id 'x) (id 'x)))
(app 'twice (num 10))
(app 'twice (num 17))
(app 'twice (num 3))
```

## Implement Parser for F1WAE

이제 concrete syntax 를 abstract syntax 로 변환할 F1WAE 의 Parser 를 구현할 차례이다.

```racket
; parse-fd: sexp -> FunDef
(define (parse-fd sexp)
    (match sexp
        [(list 'deffun (list f x) b)    (fundef f x (parse b))]))

; parse : sexp -> F1WAE
(define (parse sexp)
    (match sexp
        [(? number?)            (num sexp)]
        [(list '+ l r)            (add (parse l) (parse r))]
        [(list '- l r)                (sub (parse l) (parse r))]
        [(list 'with (list i v) e)    (with i (parse v) (parse e))]
        [(? symbol?)            (id sexp)]
        [(list f a)                (app f (parse a))]
        [else                 (error 'parse "bad syntax: ~a" sexp)]))
```

함수 선언을 `fundef` 라는 abstract syntax(F1WAE) 로 변환할 `parse-fd` 를 정의했고, 함수 호출문을 abstract syntax(F1WAE) 로 변환할 `[(list f a) (app f (parse a))]` 가 추가되었다.

## Implement Interpreter for F1WAE