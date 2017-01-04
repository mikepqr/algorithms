## Propositions

### Basic propositions

A proposition is a statement that is either true or false, usually denoted "P".

    P   NOT P
    T   F      
    F   T      

    P   Q   P AND Q     P OR Q
    T   T   T           T
    T   F   F           T
    F   T   F           T
    F   F   F           F

### Implications

"P implies Q" is weird. P is a hypothesis and Q is a conclusion. The compound
proposition is true if P is true and Q is true, or if P is false (regardless of
Q)! So:

    P   Q   P implies Q
    T   T   T          
    T   F   F          
    F   T   T
    F   F   T

e.g. If "the Riemann hypothesis is true" then "x^2 >= 0". Here the truth of P
is unknown. Q is certainly true. Therefore it doesn't matter than P is
uncertain. According the truth table, the compound proposition is true.

e.g. If "pigs can fly" then "you will get an A on this class". Here P is false.
So it doesn't matter what Q is: the compound is true.

Note therefore that there need not be a causal connection between the
hypothesis and the conclusion for the compound to be true.

To sum up: An implication is true exactly when the if-part is false or the
then-part is true.

Note that because an implication is always true if the hypothesis is false, you
can prove that it is is generally true by proving that it is true only if the
hypothesis is true.

### iff

P if-and-only-if Q asserts that P and Q are logically equivalent, i.e. they are
both true or both false.

    P   Q   P iff Q
    T   T   T          
    T   F   F          
    F   T   F
    F   F   T

### Notation

    not P = ¬P
    P and Q = P ∧ Q
    P or Q = P ∨ Q
    P implies Q = if P then Q = P ⇒ Q
    P iff Q = P and Q are logically equivalent = P ⇔ Q

### Contrapositives

    P implies Q

and 

    not Q implies not P

are contrapositives.

It turns out they are logically equivalent. One is true iff the other is. i.e.

    (P ⇒ Q) ⇔ (¬Q ⇒ ¬P)

Show this by inspection of truth table:

    P   Q   P ⇒ Q   ¬P  ¬Q  ¬Q ⇒ ¬P
    T   T   T       F   F   T
    T   F   F       F   T   F
    F   T   T       T   F   T
    F   F   T       T   T   T

e.g. let P = "I am hungry" and Q = "I am grumpy".

    If I am hungry then I am grumpy (P ⇒ Q)

is equivalent to (is true iff)

    If I am not grumpy then I am not hungry (¬P ⇒ ¬Q)

Note that 

    If I am grumpy then I am hungry (Q ⇒ P)

is not equivalent (I might be grumpy for other reasons!). This is the
"converse" of P ⇒ Q. Similarly,

    If I am not hungry then I am not grumpy 

is not equivalent (again, I might be grumpy for other reasons).

### Predicates and quantifiers

A predicate is a proposition whose truth depends on the value of a variable.

A quantifier asserts whether the proposition is true for always or sometimes
true.

e.g. The proposition "For every nonnegative integer, n, the value of n^2 +
n + 41 is prime" can be written as

    p(n) ::= n^2

    ∀ n ∈ ℕ. p(n) > 0

Here p(n) is the predicate and "∀ n ∈ ℕ" is the quantifier.

∀ is the universal quantifier (it asserts that predicate is true for all
members of the set).

∃ is the existential quantifier (it assers that there is a member of the set
for which the predicate is true).

### More notation

    ℕ = set of natural numbers, i.e. 0, 1, 2, 3...
    ℤ = set of integers, i.e. ... -3, -2, -1, 0, 1, 2, 3...
    ℤ+ = set of strictly positive integers, i.e. 1, 2, 3...
    ℝ = set of reals

Euler's conjecture (turns out to be false!):

    ∀ a, b, c, d ∈ ℤ+. a^4 + b^4 + c^4 ≠ d^4

Goldbach's conjecture (for every even number n greater than 2 there exists
primes such that p + q = n):

    ∀ n ∈ Evens. ∃ p, q ∈ Primes. p + q = n

where we have defined the sets Evens (all even numbers greater than 2) and
Primes (all primes).

"Every American has a dream" is an ambiguous proposition. Does every American
have the same dream?

If A is the set of Americans, D is the set of dreams, and H(a, d) indicates
that a particular American a has a dream d then

    ∀ a ∈ A. ∃ d ∈ D. H(a, d)

is the proposition that every American has a dream, but they don't necessarily
all have the same dream, while

    ∃ d ∈ D. ∀ a ∈ A. H(a, d)

means that there exists a dream they all share.

### Negating quantifiers

    P = Not everyone likes snowboarding
    Q = There exists someone who doesn't like snowboarding

Of course P ⇔ Q.

This follows from a general principle of equivalence of predicate quantifiers.

    ¬(∀ x. P(x)) ⇒ ∃ x. ¬P(x)

Similarly

    P = There does not exist anyone who likes skiing on magma
    Q = Everyone dislikes skiing over magma

P ⇔ Q follows from

    ¬(∃ x. P(x)) ⇔ ∀ x. ¬P(x)

Put simply: to move a NOT across a quantifier, change the quantifier.

### Validity

A proposition is valid if it is true not matter what truth values are assigned
to the individual variables.

e.g. consider the following proposition

    [P ∧ (Q ∨ R)] ⇔ [(P ∧ Q) ∨ (P ∧ R)]

it turns out that for all possible values of P, Q and R this reduces to T ⇔ T
or F ⇔ F, both of which are true from the defintion of ⇔

e.g. consider the following proposition

    ∃x ∀y. P(x, y) ⇒ ∀y ∃x. P(x, y)

This claim is obviously true regardless of the meaning of P or its domains. 

    If there exists an x (say x0) such that, for all y, P(x, y)
    then
    for all y, there exists an x (e.g. x0!) such that P(x, y) is true

It is therefore valid.

The following proposition is not valid

    ∀y ∃x. P(x, y) ⇒ ∃x ∀y. P(x, y).

For all y there exists an x such that P(x, y) is true does not in general imply
that there exists an x such that P(x, y) is true for all y!

### Satisfiability

A proposition is satisfiable if it can, in principle, be true for a particular
choice of variables.

e.g. P ∧ ¬Q is satisfiable if P is true and Q is false.

e.g. P ∧ ¬P is not satisfiable (it's false for both choices of P)
