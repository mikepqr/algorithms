## Proofs

### Definitions

An axiom is a proposition that is assumed to be true.

Important propositions are called theorems.

A lemma is a preliminary proposition useful for proving later propositions.

A corrolary is a proposition whose proof follows in a few steps from a lemma or
theorem.

### Rules of inference

Modus ponens is an inference rule that says that a proof of P and a proof that
P ⇒ Q is a proof of Q.

Other rules follow from analysis of truth tables; when the antecendets are
proved, the consequents are proved.

    Antecendets         Consequents
    P ⇒ Q ∧ Q ⇒ R       P ⇒ R
    P ⇒ Q ∧ ¬Q          ¬P
    ¬P ⇒ ¬Q             Q ⇒ P

### Proof by cases

This is proof by enumerating an exhaustive set of possible cases and verifying
the proposition for each case.

### Proof of implication by assumption of P

An implication is a proposition of the form P ⇒ Q. Such a proposition is always
true if P is false. So you can prove it by assuming that P is true and
verifying that under that assumption Q is also true.

### Proof of implication by contrapositive

Recall that the statements

    P ⇒ Q

and

    ¬Q ⇒ ¬P

are logically equivalent. A proof of the contrapositive is therefore a proof of
the original proposition. This can make things easier.

e.g. The proposition "If p is irrational then sqrt(p) is irrational" is the
contrapositive of "If sqrt(p) is rational then so is p". So you just need to
prove that (by assumption that the sqrt(p) is a rational).

### Proof of an iff

The assertion that two statements are logically equivalent is the assertion
that P holds if and only if Q does.

P ⇔ Q is equivalent to P ⇒ Q and Q ⇒ P. You can therefore prove P ⇔ Q by
proving _both_ implications (e.g. by assumption or by contrapositive).

Alternatively you can prove it by a chain of iffs, e.g. P ⇔ R and R ⇔ Q means
that P ⇔ Q.

### Proof by contradiction

Suppose P is false. Deduce something known to be false. This is a
contradiction, therefore P must be true.

Note this is essentially proof by contrapositive of T ⇒ P. The contrapositive
of this proposition is ¬P ⇒ F.

### Set notation

    A ⊂ B   proper subset, i.e. every member of A is a member of B, but A ≠ B
    A ⊆ B   subset, i.e. every member of A is a member of B
    A ∪ B   the union of A and B
    A ∩ B   the intersection of A and B
    ∅ or {} the empty set

A = B iff all elements of A are in B and all elements of B are in A. Formally

    (∀ z. (z ∈ A ⇔ z ∈ B)) ⇒ A = B
    
A and B are disjoint iff A ∩ B = {}

The cardinality of a set A is the number of elements it contains, denoted |A|.

The powerset of A is the set of all subsets of A, denoted ℙ(A).

So the powerset of {1, 2, 4} is 

    {{}, {1}, {2}, {4}, {1, 2}, {1, 4}, {2, 4}, {1, 2, 4}}

Note the cardinality of the powerset of a set A is 2^|A| (easy to prove
by induction).

Set builder notation is like list comprehensions in Python, e.g.

    {n ∈ ℕ | n is prime and n = 4k + 1 where k is an integer}

### Sequences

Collections with ordering, in which elements may occur more than once. The
empty sequence is often denoted λ. 
