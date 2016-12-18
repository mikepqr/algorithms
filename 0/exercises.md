# BPV Chapter 0

## 0.1

### a

f(n) =  n - 100
g(n) = n - 200

By the rules above, these two expressions reduce to the same thing, n,
therefore f = Θ(n).

### b

f(n) = n^(1/2)
g(n) = n^(2/3)

f = O(g) by the rules.

More formally, f/g <= 1 for all n, therefore there exists a c s.t. f(n) <= c
g(n). g/f = n^(1/6) which tends to infinity for large n, and there exists no
constant such that g = O(f), therefore f is not Ω(g), and therefore nor is it
Θ(g).

### c

f(n) = 100n + log(n)
g(n) = n + (log(n))^2

By the rules, f = Θ(g).

Formally, f/g -> a constant (100) for large n, so a c exists s.t. f = O(g) and
f = Ω(g).

### d

f(n) = n log(n)
g(n) = 10n log(10n)

g(n) = 10n log(10) + 10n log(n) so ignoring unimportant terms and
multiplicative constants then g becomes n log(n) and f = Θ(g).

### e

f = log(2n)
g = log(3n)

2 and 3 inside logs are additive constants and can be ignored. f = Θ(g).

### f

f(n) = 10 log(n)
g(n) = log(n^2)

g(n) = 2 log(n) so f = Θ(n).

### g

f(n) = n^(1.01)
g(n) = n log^2(n) ... which presumably means n log(n) log(n).

By the rules, polynomials dominate logs and 1.01 > 1 so f = Ω(g).

A bit more formally, f/g = n^0.01 / log^2(n), and all positive polynomials of n
eventually dominate all polynomials of log(n).

(Indeed if you check, these two functions cross when n^0.01 = log^2(n), which
happens at about 10^669, see [Wolfram
Alpha](https://www.wolframalpha.com/input/?i=x%5E0.01+%3D+(log2(x))%5E2))

### h

f(n) = n^2 / log(n)
g(n) = n log^2(n)

f/g = n / log^3(n) so by the rules f = Ω(g).

### i

f(n) = n^0.1
g(n) = log^10(n)

By the rules f = Ω(g) (f dominates g for n > 10^299).

### j

f(n) = log(n)^log(n)
g(n) = n/log(n)

Recall x^log(y) = y^log(x). If we say x = log(n) and y = n then
f(n) = n^(log log(n)).

n(^log log(n)) > n (and certainly > n/log(n)), so f = Ω(g).

### k

f(n) = n^(1/2)
g(n) = log^3(n)

By the rules, f = Ω(g)

### l

f(n) = n^(1/2)
g(n) = 5^(log2(n)) (where log2 = log to base 2)

Recall x^log2(y) = y^log2(x). If we say x = 5 and y = n then
f(n) = n^log2(5). log2(5) > (1/2) so f = O(g).

### m

f(n) = n 2^n
g(n) = 3^n

By the rules, ignore the leading n, and 2^n = O(3^n) therefore f = O(g).

### n

f(n) = 2^n
g(n) = 2^(n+1)

g(n) = 2(f) therefore f = Θ(g)

### o

f(n) = n!
g(n) = 2^n

f = Ω(g). This seems obvious but to prove it recall Stirling's approximation
for large n, which states that n! ~ constants * n^n / n^0.5 ~ n^(n - 0.5). This
is much larger than 2^n.

### p

f(n) = log(n)^log(n)
g(n) = 2^(log2(n)^2)

f(n) = n^(log log(n)) (see question (g))

g(n) = (2^(log2(n))^log2(n) = n^log2(n) (because x = b^(logb(x)))

(log log(n)) = O(log2(n)) regardless of base so f = O(g).

### q

f(n) = sum (i = 1 to n) of i^k
g(n) = n^(k+1)

[Faulhaber's formula](https://en.wikipedia.org/wiki/Faulhaber%27s_formula) says
that this sum is a polynomial in n where the leading term is n^(k+1).

So f = Θ(g).

## 0.2

g(n) = sum (i = 0 to n) of c^i where c > 0

This is a geometric series. g(n) > 1 for all positive c and all n (series is
additive, first term is 1).

### a

If 0 < c < 1 then the standard formula for the sum of this series applies, i.e.
g(n) = (1 - c^n)/(1 - c).

For c > 0 then g(n) < 1/(1 - c). This is a constant > 1.

Therefore 1 < g(n) < a constant greater than 1 for all n.

This means there exists a multiplier that makes g(n) < 1 for all n -> g = O(1).

This also means there exists a multiplier that makes g(n) > 1 for all n -> g =
Ω(1).

Taken together, g = Θ(1).

### b

c = 1 so the standard formula does not apply. 

g(n) = sum (i = 0 to n) of 1 = n + 1.

Clearly g(n) = Θ(n).

### c

c > 1

Rearrange g(n) = (c c^n - 1)/(c - 1).

g(n) < c c^n / (c - 1) for all n. Therefore g(n) = O(c^n).

Now show that g(n) is > c^n to complete the proof.

Assume g(n) > c^n then c c^n /(c - 1) - 1/(c - 1) > c^n. Group terms in c^n and
simplify to yield c^n > 1, which implies n > 0.

All of which is to say, g(n) > c^n for all n > 0, i.e. g(n) = Ω(c^n).

So g(n) = Θ(n).

## 0.3

Fibonnaci's sequence:

F(0) = 0, F(1) = 1, Fn = F(n-1) + F(n-2)

### a

Show F(n) >= 2^(0.5n) for n >= 6

For n = 6, F(n) = 8, and 2^(0.5n) = 8, so inequality satisfied
For n = 7, F(n) = 13, and 2^(0.5n) = 11.3, so inequality satisfied

Proof by induction, i.e. show that if 
F(n) >= 2^(0.5n), F(n-1) >= 2^(0.5(n-1))
then F(n+1) >= 2^(0.5(n+1)).

F(n+1) >= 2^(0.5n) + 2(0.5(n-1)) 
= 2(0.5(n-1)) (2^0.5 + 1)

(2^0.5 + 1) > 2 so F(n+1) >= 2 x 2(0.5(n-1)) 

F(n+1) >= 2(0.5(n-1) + 1) = 2(0.5(n+1))

### b

Find a c < 1 s.t. F(n) <= 2^(cn)

If F(n) <= 2^(cn) then F(n-1) + F(n-2) <= 2^(cn) from defn of sequence.

Make inductive hypothesis: F(m) <= 2^(cm) for all m < n.

Then F(n) >= 2^(c(n-1)) + 2^(c(n-2)) since these two terms are <= than F(n-1)
and F(n-2) respectively.

F(n) = F(n-1) + F(n-2) so 2^(cn) >= 2^(c(n-1)) + 2^(c(n-2)).

Let x = 2^c then x^n >= x^(n-1) + x^(n-2) so x^2 - x - 1 >= 0

For positive x this is true for x > (1 + 5^0.5)/2.

Hence c = log2(x) >= log2((1+5^0.5)/2) ~= 0.694

Establish truth of base cases given the condition required for the induction
relation:
F(0) = 0 < 2^0
F(1) = 1 < ((1 + 5^0.5)/2)

See ex3.py for experimental confirmation.

### c

From part b F(n) = O(2^(cn)) for c >= log2((1 + 5^0.5)/2)

Therefore F(n) = Ω(2^0.5n) for c < log2((1 + 5^0.5)/2)

## 0.4

### a 

AB = C. If A, B and C are R^(2x2) then to form an element in C requires two
multiplications and one addition.

Therefore to form C requires 8 multiplications and four additions.

### b 

How many multiplications does it take to calculate X^n?

This can be done using exponentiation by squaring, i.e break the calculation of
X^n down into a series of squarings and multiplications.

e.g. X^25 = X^16 X^8 X^1 = ((((X^2)^2)^2)^2) (((X^2)^2)^2) X

In this case there are 9 multiplications.

Generally there largest term is formed by floor(log2(X)) squarings, e.g.
log2(25) = 4.6.

All other terms are formed as by-products of this, so floor(log2(X)) squarings
are necessary.

The squared numbers are combined with no more than floor(log2(x)) - 1
multiplications, since that is the number of digits in the binary expansion of
x.

Squarings are multiplications so the total number of multiplications is 
2 floor(log2(x)) - 1, which is O(log2(x)) as required by the question (and is
also Ɵ(log2(x))).

### c

F(n) is log2(F(n) bits long.

F(n) = O(2^n) from 0.3(b). From the definition of O, F(n) < c 2^n for all n
where c is a positive constant.

log2(F(n)) < log2(c 2^n) = log2(c) + n

Length of F(n) = log2(F(n)) = O(n) 

All intermediate results, i.e. F(0) ... F(n-1) are no longer than F(n),
therefore all intermediate results are O(n) long.

### d

From the question: there exists an algorithm for multiplying to n-bit numbers
with running time M(n). n here is the number of bits in a general number, not
the number denoting which Fibonnaci number we're calculating, so I will use b
to denote number of bits. 

Multiplication running time = Ɵ(M(b))

The running time of fib3 is Ɵ(running time of forming X^n), where X is a 2x2
matrix.

To calcualate X^n we must do O(log(n)) multiplications. 

The numbers being multiplied are O(n) bits (from part c).

The multiplications have running time M(b) = O(M(n)) for all multiplications
since n >= b.

So: we do O(log(n)) operaations which have running time O(M(n)), therefore fib3
has running time O(log(n) M(n)).

Note: The question tells us in particular that M(b) = O(b^2) (the worst-case
school algorithm for multiplication achieves this). We don't actually use this
information, except to note that M(b) is an increasing function of b, which we
use to show that M(b) = O(M(n)) for b <= n.

### e

Assume M(n) = Ɵ(n^a) where 1 <= a <= 2. I think this is infact true for
multiplication, but the constraints on a are not used in the solution.

The running time of fib3 is O(log(n)) multiplications, each of which has a
running time of Ɵ(b^a), where b is the number of bits in the number. 

The numbers are initially 1 bit long, but double with every squaring. They
continue to do this until they are O(n) long.

Therefore the running time of fib3 is O(1 + 2^a + 4^a ... n^a).

This is a geometric series with ratio 2^a and log(n) terms. The sum is thus 
(2^a^log(n) - 1) / (2^a - 1)

(this is the usual sum of geometric series formula x -1)

The running time is therefore is O(2^a^log(n)). 2^log(n) = n so this simplifies
to O(n^a) = O(M(n)).
