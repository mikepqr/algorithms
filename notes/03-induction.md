# Induction

## Well-ordering principle

    Every non-empty set of nonnegative integers has a smallest element

Note this is false for the empty set, and false for the the set of all negative
integers.

This seemingly simple observation can be used to prove P(n).

 1. Define set C = {n ∈ ℕ | P(n) is false} of counter-examples to P(n).
 2. By well-ordering principle there is a smallest element n of C
 3. Reach a contradiction by using n to show there is an element of C smaller
    than n
 4. Conclude C must be empty, i.e. no counter-examples exists.

### Example of well-ordering principle

_Theorem_.

    Σ(i=0 to i=n) i = n(n+1)/2

_*Proof*_. By contradiction and the well-ordering principle. 

Let P(n) be the predicate Σ(i=0 to i=n) i = n(n+1)/2. 

C = {n ∈ ℕ | P(n) is false}. 

Assume counter-examples to P(n) exists. Then C ≠ {}. Then by the well-ordering
principle, C has a smallest element c, the smallest counter-example to P(n).

If c is the smallest counter-example then P(n) is true ∀ n ∈ N. n < c.

c-1 < c therefore P(c-1) is true, i.e.

    1 + 2 + ... + (c-1) = (c-1)c/2

Add c to both sides

    1 + 2 + ... + (c-1) + c = (c-1)c/2 + c
                            = c(c+1)/2

So P(n) is true for c. This is a contradiction so the assumption that C ≠ {}
must be false. QED.

### Example of well-ordering principle

_Theorem_.

Every integer greater than 1 can be written as the product of primes.

_*Proof*_. By contradiction and the well-ordering principle. 

C = {n ∈ N. n > 1 ∧ n cannot be factored as a product of primes}

Assume C ≠ {}. By well-ordering, C contains a smallest element n. n is not
prime, since a prime is a product of (one) prime.

So n is a product of two integers a, b, where 1 < a, b < n

a, b < n so are not in C. Both can therefore be written as the product of
primes, e.g. 

    a = p1 p2 p3 ... pk
    b = q1 q2 q3 ... ql

But if that's the case, then

    n = (p1 p2 p3 ... pk)(q1 q2 q3 ... ql)

i.e. P(n) is true and n is not in C. This is a contradiction so C = {}. QED.

## Proof by induction

Let P(n) be a predicate. If

 1. if P(0) is true
 2. ∀n ∈ ℕ, (P(n) ⇒ P(n+1)) is true

then ∀n ∈ ℕ, P(n) is true.

Usually prove 1. by manual check of _the base case_.

Usually prove 2. by standard method to prove an implication, i.e. assume the
lhs is true and then show that the rhs must also be true.

The assumption that P(n) is true in part 2. is the _inductive hypothesis_. The
proof that P(n) ⇒ P(n+1) is the _inductive step_.

## Example of proof by induction

_Theorem_.

    Σ(i=0 to i=n) i = n(n+1)/2

_*Proof*_. By induction. Let P(n) be the predicate Σ(i=0 to i=n) i = n(n+1)/2.

(P(n) is usally chosen to be the thing we're trying to prove.)

_Base case_. Is P(0) true?

    0 = n(n+1)/2 when n = 0. ✓

_Inductive step_. For n >= 0, show P(n) ⇒ P(n+1), i.e. 

    Σ(i=0 to i=n+1) = (n+1)(n+2)/2.

Make inductive hypothesis, i.e. assume P(n) is true, Σ(i=0 to i=n) i = n(n+1)/2

    Σ(i=0 to i=n+1) = P(n) + n + 1
                    = n(n+1)/2 + n + 1  (by the inductive hypothesis)
                    = (n+1)(n+2)/2

QED.

## Example of proof by induction

_Theorem_. 

    ∀n ∈ ℕ. 3|(n^3 - n)

Note x|y denotes that x divides y, i.e. y is an integer multiple of x. 

_Proof_. By induction. Let P(n) by the predicate 3|(n^3 - n).

_Base case_. Is P(0) true?

    (0^3 - 0)/3 = 0. ✓

_Inductive step_. For n >= 0, show P(n) ⇒ P(n+1), i.e. 3|((n+1)^3 - (n+1)).

Make inductive hypothesis, i.e. assume 3|(n^3 - n).

    (n+1)^3 - (n+1) = (n+1)(n^2+2n+1) - (n+1)
                    = (n+1)(n^2+2n)
                    = n^3 + 2n^2 + n^2 + 2n
                    = n^3 - n + 3n^2 + 3n

First two terms are n^3 - n, which is divisible by 3 by inductive hypothesis.
Last two terms are also divisible by 3. Hence 3|((n+1)^3 - (n+1)) and P(n+1) is
true.

QED.

## Base case

Need not start at n = 0. But whatever it does start at, the inductive step must
hold for all n greater than _or equal to_ base case. See false proof in section
3.2.6 of notes for an example of where this goes wrong.

## Induction and well-ordering

Any proof by one method can be written by the other method. It's an issue of
style.

## Stronger inductive hypotheses

A stronger inductive hypothesis is often more powerful. It allows you to make
stronger assumptions to prove P(n+1). For example...

_Theorem_.

∀n, ∃ a way to tile a 2^n x 2^n courtyard using L-shaped tiles with a center
tile missing for a statue.

P(n) is the proposition that a way exists with Bill in center.

_Base case_. If n = 0 the courtyard is a single tile for the statue.

_Inductive step_. For n >= 0 assume P(n) to verify P(n+1) is true.

Failed attempt. Seems natural to build on fact that a courtyard with n+1 is
simply 4 courtyards with n. However, if P(n) is true, n-sized courtyards give
you a way to tile the courtyard with statue in their center. Their center is
_not_ the centre of an n+1-sized courtyard made out of 4 of them.

Change P(n): a way exists with Bill in _any_ square (including the center)!
Base case unchanged.

_Inductive step_. For n >= 0 assume P(n) to verify P(n+1) is true.

Then if P(n) is true, you can tile an n+1-sized courtyard by using 4 n-sized
courtyards with statues in their corners, getting rid of 3 of the statues and
replacing them with an L-shaped tile.

QED.

## Proof of invariants

 1. Show a proposition about the value of an invariant is true at step t = 0
 2. Show that if it is true at P(t) it remains true at P(t+1)

QED.

### Example of proof of invariants

A robot starts at (0,0) and moves along a single diagonal. Can it reach (1,0)?

No. By inspection, it's clear that the robot's coordinates must sum to an even
number. But to prove this:

_*Theorem*_.

The sum of the robot's coordinates is always even.

_*Proof*_. By induction. Let P(0) by the predicate that the sum of the
coordinates is true after t moves.

_Base case_. At t = 0, (x,y) = (0,0), thus P(0) is true ✓.

_Inductive step_. Show P(t) ⇒ P(t+1) for t >= 0. The robot is at (x,y) after t
moves. Assume P(t), i.e. x+y is even. Enumerate possible coordinates after t+1
moves:

 1. x+1, y+1. Sum = x+y+2 which is even by inductive hypothesis.
 2. x+1, y-1. Sum = x+y which is even.
 3. x-1, y+1. Sum = x+y which is even.
 4. x-1, y-2. Sum = x+y-2 which is even.

In every case P(t+1) is true, thus P(t) ⇒ P(t+1). QED.

_Corollary_. The robot can never reach (1,0) because those coordinates sum to
an odd number.

See lecture and notes 3.3.3/4 for a more substantial proof by invariant.

## Strong induction

Instead of using P(n) to prove P(n+1), use P(0), P(1) ... P(n) together, i.e.

 1. Show P(0) is true
 2. Show P(0) ∧ P(1) ∧ P(2) ∧ ... ∧ P(n) ⇒ P(n+1)

Useful when the predicate depends on P(a) for all a < n. You're assuming more
things so it can only be easier (or no harder) to prove P(n+1).

### Example of proof by strong induction

_*Theorem*_.

Every integer greater than 1 can be written as the product of primes.

(Proved earlier by well-ordering.)

_*Proof*_ by strong induction.

_Base case_. P(2) is true because 2 is the product of one prime (2).

_Inductive step_. Assume P(a) is true for all a < n+1. Then show this implies
P(n+1) is true. By cases.

 1. If n+1 is prime then P(n+1) is true.
 2. If n+1 is not prime then it is the product of numbers smaller than itself.
    But all numbers smaller than itself are themselves the products of primes.
    QED.
