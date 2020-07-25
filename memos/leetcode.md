# [ccss17.github.io](https://ccss17.github.io)


# uncrossed-lines/

https://leetcode.com/problems/uncrossed-lines/

## 증명 

모든 조합을 찾고 가장 많은 선 조합을 선택한다.

- 함수 $\text{idx}$ (인덱스 반환)

  (in) 튜플 $X$, $x \in X$

  (out) $x$ 의 인덱스 튜플

- 함수 $\text{comb}$ (조합 계산)

  (in) 집합 $X$ 

  (out) 집합 $X$ 의 부분집합의 집합족

- 함수 $l$ (선을 긋는다)

  (in)

  $\exists$ 선조합 공집합 $C$ 

  - $\text{if}\ d$ (선을 긋는다)

    $a_i \in A, a_i \in B$ 는 각각 인덱스 $i \in \{1,2,\dots,n(A)\}, j \in \{1,2,\dots,n(B)\}$ 를 갖는데, 이 $i, j$ 에 대한 튜플 $(i, j)$ 를 집합 $C$ 에 포함시킨다.

  - $\text{if not}\ d$

    이 경우 자체를 기각한다.
  
- 함수 $d$ ($n \in A, n \in B$ 에 대한 교차선이 존재하지 않는지 판단한다)

  다음 명제 $p, q$ 에 대하여 $p \land q$ 를 반환한다.

  - 명제 $p$ : $n \in A$ 보다 왼쪽 원소들이 $n \in B$ 보다 오른쪽 원소들과 연결되지 않았다. 즉, $n \in A$ 의 인덱스 $i$ 에 대한 인덱스 $a \in \{1,\dots, i-1\}$ 와 $n \in B$ 의 인덱스 $j$ 에 대한 인덱스 $b \in \{j+1, \dots, n(B)\}$ 에 대하여 $(a, b) \not \in C$ 이다.

  - 명제 $q$ : $n \in A$ 보다 오른쪽 원소들이 $n \in B$ 보다 왼쪽 원소들과 연결되지 않았다. 즉, $n \in A$ 의 인덱스 $i$ 에 대한 인덱스 $a \in \{i+1,\dots,n(A)\}$ 와 $n \in B$ 의 인덱스 $j$ 에 대한 인덱스 $b \in \{1, \dots, j-1\}$ 에 대하여 $(a, b) \not \in C$ 이다.

- 함수 $f$ (선조합 계산)

  (in) ? 선조합 집합 $C$, ? 시작인덱스 $i$

  $\text{if}\not \exists C$ : $\exists C := \varnothing$ (선조합 집합)
  
  $\text{if}\not \exists i$ : $\exists i := 1$ (시작인덱스)

  $\exists\ \text{result} := \varnothing$ (선조합 계산 결과)
  
  $\text{for-each}\ i\ \text{in}\ \{i, i+1, \dots, n(A)\}$ :

  - $\exists a_i \in A$ 에 대하여 $\text{if} \not \exists a_i \in B$ : $\text{continue}$

  - $\exists a_i \in A$ 에 대하여 $\text{if}\ \exists a_i \in B$ :

    $\exists S = \text{comb}(\text{idx}(B, a_i))$ (인덱스 리스트 집합족)

    $\text{for-each}\ s\ \text{in}\ S$ :

      - $\exists C = l(i, s)$ (선조합 집합) (조합대로 **선을 긋는다.**)

      - $f$ 에 $C$ 와 $i+1$ 을 전달한다. (각각의 선을 긋는 경우를 기반으로 $a_i \in A$ 다음 원소 $a _{i+1} \in A$ 에 대하여 $f$ 를 진행한다.)
  
  - $\text{if}\ a_i \equiv a _{n(A)}$ (마지막 원소)

    집합 $\text{result}$ 에 집합 $C$ 를 포함시킨다.