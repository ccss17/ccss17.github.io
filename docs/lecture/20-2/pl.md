
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

## Type

타입 : 데이터의 추상적 정의이다. Java 에서 `class` 와 같은 개념이다.


Racket 의 Type 정의 

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