# Number theory

## Divisibility

_Definition_. 

    a|b ⇔ ak = b for some k

_Facts_.

 1. a|b ⇒ a|bc for all c
 2. a|b ∧ b|c ⇒ a | c
 3. a|b ∧ a|c ⇒ a | sb + tc for all s, t
 4. a|b ⇔ ca|cb for all c
 5. a|0 for all a

_Proof_ e.g #3, if a divides b and c then it divides any linear combination of
them.

By defintion

    a|b ⇒ ak = b 
    a|c ⇒ aj = c

Then

    sb + tc = sak + taj.

which is divisible by a.

## Jug problem

a gallon jug, b gallon jug, a <= b.

### State machine

States are denoted (x, y) where x is volume in a gallon jug, y is volume in b
gallon jug.

Initial state is (0, 0).

### Transitions

 - _emptying_
    - (x, y) → (x, 0)
    - (x, y) → (0, y)
 - _filling_
    - (x, y) → (a, y)
    - (x, y) → (x, b)
 - _pouring_
    - (x, y) → (0, x+y) if x + y <= b
    - (x, y) → (x - (b-y), b) if x + y >= b
    - (x, y) → (x+y, 0) if x + y <= a
    - (x, y) → (a, y - (a-x)) if x + y <= a

### Die Hard solution

a=3, b=5, goal is 4 in one of the jugs.

(0, 0) → (3, 0) → (0, 3) → (3, 3) → (1, 5) → (1, 0) → (0, 1) → (3, 1) → (0, 4).

### Property true of all reachable states

_Theorem_. If m|a and m|b then m|any possible result of pouring one jug into
the other.

_Proof_. By induction. P(n) = "If (x, y) is the state after n transitions, then
m|x and m|y."

_Base step_. Clearly P(n) holds for (0, 0).

_Inductive step_. Assume P(n). Show this ⇒ P(n+1). Let (x, y) be the state
after n transitions. Because P(n), m|x and m|y. 

After a transition the possible states are:

 - _emptying_
    - (x, 0) ✓ by IH
    - (0, y) ✓ by IH
 - _filling_
    - (a, y) ✓ by IH and m|a
    - (x, b) ✓ by IH and m|b
 - _pouring_
    - (0, x+y) ✓ m|x and m|y ⇒ m|x+y (divisibility fact #3 above)
    - (x - (b-y), b) ✓ fact #3
    - (x+y, 0) ✓ fact #3
    - (a, y - (a-x)) ✓ fact #3 ∎

This theorem tells you a property true about reachable states. If therefore
tells you about states you _cannot_ reach. E.g. if a=15 and b=30 then any
reachable state is divisible by 3 and 5 and you therefore cannot reach 4.

If doesn't necessarily follow that all states for which the property holds are
reachable.

### Proof that all states with a property are reachable

_Lemma_. L = sa + tb ⇒ ∃ s' > 0 such that L = s'a + t'b.

_Proof_.

    L = sa + tb
      = (s + mb)a + (t - ma)b

For any integer m. This means that ∃ s', t'

    L = s'a t'b

where s' > 0 simply by making m large enough.

So if there exists one linear combination that sums to L, there exists at least
one that sums to L where the coefficient of a is positive.

This is important because it allows us to use an algorithm that is repated s'
times.

_Theorem_. Any linear combination L = sa + tb with 0 <= L <= b is reachable. 

_Proof_. We're going to prove it by proving a specific algorithm works.

Repeat s' times:
 - Fill the a jug
 - Pour into the b jug
 - If b jug is full, empty it out, pour rest of a jug in

Note: Assume 0 < L < b (ignore L = 0 and L = b which are trivially reached with
0 loops of the algorithm).

e.g. 
 1. (0, 0) → (3, 0) → (0, 3) → 
 2. (0, 3) → (3, 3) → (1, 5) → (1, 0) → (0, 1) 
 3. (0, 1) → (3, 1) → (0, 4)

This algorithm fills the a-jug s' times. Suppose the b-jug is emptied u times.

Let r be water in b-jug. We know r = s'a - ub (the difference of what we
added to the b-jug and took away). Hence

    r = s'a - ub
      = L - t'b - ub  (from definition of L by assumption above)
      = L - (u + t')b

u + t' is an integer. Recall 0 < L < b. Then

    u + t' ≠ 0 ⇒ r < 0 or r > b

But r is the volume in the b-jug, so r < 0 or r > b is not possible. Hence

    u + t' = 0 ⇒ r = L

Volume left in b-jug after this algorithm = L where L is any linear combination
of a and b ∎

## Division theorem

_Theorem_. There exists a unique q and r such that

    b = qa + r

where 0 <= r < a. q = "quotient", r = "remainder".

    r = rem(b, a)

## Smallest linear combination of a and b divides a and b

_Theorem_. If m is the smallest positive linear combination of a and b then m|a
and m|b.

Let smallest possible positive linear combination of a and b be m where

    m = sa + tb

for some s and t. By the division theorem

    a = qm + r (where r < m)

Hence

    r = a(1 - qs) - tbq

i.e. r is a linear combination of a and b. m is the _smallest_ such linear
combination that is positive, but r < m by its definition in terms of the
division theorem. Hence it must by true that r = 0, and m|a. Proof is same for
b. ∎

## Bezout's Lemma

_Theorem_. The smallest possible positive linear combination of a and b is
gcd(a, b)

_Proof_. Let smallest possible positive linear combination of a and b be m.
Proceed by showing that m <= gcd and m >= gcd, therefore m = gcd.

 1. gcd|a and gcd|b hence gcd|(sa + tb) for any s, t (see facts about division
    above; if a number divides two others, then it also divides any combination
    of them). m is a linear combination, hence gcd|m. This implies gcd <= m.

 2. From above, m|a and m|b if m is the smallest linear combination. Hence m is
    a common divisor of a and b. Hence m <= gcd. ∎

Note this also says that gcd(a, b) is a linear combination of a and b.

## All linear cominbations are multiples of greatest common divisor

_Theorem_. An integer is linear combination of a and b ⇔ it is a multiple of
gcd(a, b).

_Proof_. iff so must prove implication both ways:

 1. If a number divides two others then it also divides any combination of them
    (fact #3). Hence gcd|(sa + tb) for any s, t. Hence gcd is a multiple of any
    linear combination.
 2. gcd is linear combination of a and b by Bezout, hence any multiple of gcd
    is also a linear combination. ∎

## Every common divisor divides the greatest common divisor

For some s, t

    gcd(a, b) = sa + tb

(by Bezout). Let m|a and m|b. a = um, b = vm. Hence

    gcd(a, b) = sum + tvm
              = m(su + tv)

Hence m|gcd(a,b) ∎

## gcd(ka, kb) = k gcd(a, b) for all k

    gcd(a, b) = sa + tb

(by Bezout). Hence

    k gcd(a, b) = ksa + ktb 

All linear combinations are multiplies of the greatest common divisor (see
above), so

    gcd(ka, kb) | k gcd(a, b)

Now,

    gcd(a, b)|a ⇒ k gcd(a, b)|ka.
    gcd(a, b)|b ⇒ k gcd(a, b)|kb.

This means k gcd(a, b) is a common divisor of ka and kb. We showed above that
every common divisor divides the greatest common divisor:

    k gcd(a, b) | gcd(ka, kb)

x|y and y|x ⇔ x = y ∎

## If gcd(a, b) = 1 and gcd(a, c) = 1 then gcd(a, bc) = 1

Recall gcd(a, b) is a linear combination of a and b. Then

    sa + tb = 1
    ua + vc = 1

Hence

    (sa + tb)(ua + vc) = 1
    a(asu + csv + btu) + bc(vt) = 1

This is a linear combination of a and bc = 1. Hence the smallest positive
linear combination of a and bc is 1. Hence gcd(a, bc) = 1 ∎

## If a|bc and gcd(a, b) = 1 then a|c

Recall gcd(ac, bc) is a linear combination of ac and bc.

a|ac trivially. a|bc by assumption. Hence a divides _every_ linear combination
of ac and bc. In particular a|gcd(ac, bc).

    gcd(ac, bc) = c gcd(a, b) by theorem above
                = c . 1 by assumption of gcd(a, b) = 1
                = c

a|gcd(ac, bc). gcd(ac, bc) = c. Hence a|c ∎

## gcd(a, b) = gcd(rem(b, a), a)

This gives is Euclid's algorithm.

_Proof_. First prove gcd(a, b) <= gcd(rem(b, a), a). Then prove >=.

 1. For some m
    ```
    [m|a and m|b] ⇒ m|sa + tb for any s, t
                  ⇒ m|bq - a where q is the quotient
                  ⇒ m|rem(b, a)
    ```
    Recall a = bq + r, where r = rem(b, a).

    This shows that anything that divides a and b also divides their remainder.

 2. If rem(b, a) ≠ 0 then for some m
    ```
    m|rem(b, a) and m|a ⇒ m|b-qa and m|a
                        ⇒ m|a and m|b
    ```
    (m|b because if m divides two numbers then it divides any linear
    combination of those numbers, and we know m|b-qa and m|a)
    
    If rem(b, a) = 0 then b=qa.
    ```
    m|a ⇒ m|b
    ```
    This shows that anything that divides a and the remainder of a with b also
    divides b.

Now, let m in argument 1 be gcd(a, b).

    ⇒ gcd(a, b) is a common divisor of a (by defn) and rem(b, a)
    ⇒ gcd(a, b) <= gcd(rem(b, a), a)

because common divisors are no bigger than greatest common divisors. Similarly
let m in argument 2 be gcd(rem(b, a), a). Then 

    ⇒ gcd(rem(b, a), a) is a common divisor of a (by defn) and b
    ⇒ gcd(rem(b, a), a) <= gcd(a, b)

x <= y and x >= y ⇒ x = y. ∎

## Alternative proof that gcd is a linear combination

_Theorem_. gcd(a, b) is a linear combination of a and b.

_Proof_. By induction. Let P(n) be claim that "if Euclid's algorithm reaches
(x, y) after n steps then both x and y are linear combinations of a and b, and
gcd(a, b) = gcd(x, y)"

_Base case_. After zero steps, x = a, y = b ✓

_Inductive step_. Assume P(n). Show this ⇒ P(n+1).

Notice that ∃ q such that rem(y, x) = y - qx. y is a linear combination of a
and b, and so is x (by I.H.), hence so is rem(y, x). I.H. also gives us that
gcd(x, y) = gcd(a, b).
