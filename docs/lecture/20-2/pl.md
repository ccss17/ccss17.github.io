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