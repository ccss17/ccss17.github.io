해석학, 기하학, 대수학 등의 무모순성이 산술(페아노 공리계, PA)의 무모순성으로 귀결된 이후 수학자들은 여러가지 방법으로 산술의 무모순성을 증명하려 했다. 한편 괴델은 PA 를 포함할 수 있을만큼 강력한 공리체계의 무모순성은 그 공리체계로 증명할 수 없다는 괴델의 불완전성 정리를 보였다. 이후에 겐첸이 PA 로 형식화 할 수 없는 초한귀납법으로 PA 의 무모순성을 증명했고, 2020년 6월에 Sergei Artemov 가 [PA 로 표현가능한 PA 의 무모순성 증명법](https://arxiv.org/pdf/1902.07404.pdf) 을 제안했다. 

이러한 산술의 무모순성 증명을 이해하려고 노력했는데 아직 수학에 대한 지식이 부족해서 제대로 이해할 수 없었고, 결국 math stackexchange 의 매우 rough 한 답변을 보고 대충이나마 이해할 수 있었다. PA 의 무모순성 증명을 제대로 이해하려면, 여러가지 개념과 표현법을 잘 알고 있어야 하는데, 대충 명제논리, 1차 논리, 대수학, 카테고리 이론 등을 알아야 하는 것 같다. 이해하려고 애썼던 논문 및 페이지들은 다음과 같다.

- https://plato.stanford.edu/entries/proof-theory/

- http://timothychow.net/consistent06.pdf

- https://en.wikipedia.org/wiki/Gentzen%27s_consistency_proof

- https://arxiv.org/pdf/1807.05641.pdf

- ...

# Gentzen's PA consistency proof (very rough outline)

> https://math.stackexchange.com/questions/2856263/contents-of-gentzens-consistency-proof-of-pa

겐첸은 먼저 PA 의 증명 집합 $P$ 와 서수 집합 $\Alpha = \{\alpha  : \alpha   < \epsilon _0 \}$ 에 대하여 원시 재귀 함수 $C:P \to \Alpha$ 와 $E: P \to P$ 를 정의했다. $\epsilon _0$ 은  $\omega , \omega ^{\omega }, \omega ^{\omega ^{\omega }}, \dots$ 의 극한에 있는 서수이다. 함수 $C$ 와 $E$ 는 $\forall p \in P$ 에 대하여 다음 성질을 만족한다.

1. $C(p)>0 \implies  C(E(p)) < C(p)$

2. 증명 $E(p)$ 의 결론은 증명 $p$ 와 같다.

3. $p \vdash \perp \implies C(p) > 0$

이 세 성질은 원시 재귀 산술로 형식적으로 증명가능하다.

## 증명 과정

만약 PA 의 어떤 증명 $p$ 가 모순을 도출한다고 하자. 즉, $\exists p \in P, p \vdash \perp$ 라고 하자. 그러면 다음과 같이 함수 $E$ 를 재귀적으로 정의함으로써 무한히 많은 모순을 도출하는 증명을 생성할 수 있다.

$$ p_0 = E(p), \quad p _{n+1} = E(p_n) $$

성질 2) 에 의하여 $\forall p_n \vdash \perp$ 이고, 3) 에 의하여 $\forall C(p_n) > 0$ 이며, 1) 에 의하여 $C(p _{n+1}) < C(p_n)$ 이다. 그러면 $C(p_n)$ 은 무한히 감소하는 서수의 수열이 되는데, 이는 [정렬집합의 가정](https://en.wikipedia.org/wiki/Well-order)에 모순된다. 그러므로 

$$ \therefore \not \exists p \in P \vdash \perp $$

이고, 페아노 공리계 PA 는 모순을 도출하지 않는다. ■ 

그래서 해석학도 모순을 도출하지 않고, 기하학도 그렇고, 통계학도 그렇다.