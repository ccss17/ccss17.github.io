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
(define-type type-id
    [variant_id1 (field_id11 contract_expr11)
                 ...
                 (field_id1n contract_expr1n)]
    ...
    [variant_idm (field_idm1 contract_exprm1)
                 ...
                 (field_idmn contract_exprmn)])
```
