# DPV Chapter 0

## Big-oh notation

If there is a positive constant c such that f(n) <= c g(n) for all positive n
then we can say f = O(g).

More approximately f = O(g) means "f(n) grows no faster than g(n)" or  "f ~< g".

f = Ω(g) means the opposite, i.e. there is a c such that f(n) >= g(n) for all
positive n, or "f(n) grows no slower than g(n)" or "f >~ g".

Note that f = Ω(g) <-> g = O(f).

f = Θ(g) means f = Ω(g) and f = O(g), i.e. f(n) grows no slower and no faster
than g(n).

## Quick comparisons of functions

 - reduce each function by ignoring all terms except dominant one and ignoring
   multiplicative constants
 - n^a dominates n^b if a > b
 - any exponential dominates any polynomial, e.g. 3^n = Ω(n^5)
 - any polynomial dominates any logarithm, e.g. n = Ω((logn)^3)

The definitions also imply that if f(n)/g(n) tends to a constant for large n
then f = Θ(n).

## Some facts about logarithms useful for the exercises

log(x) denotes logarithm x to some base b. Then from the defn of logarithm

    x = b^(log(x))

From this...

x^log(y) = (b^log(x))^log(y) = b^(log(x) log(y))

...and equivalently...

y^log(x) = b^(log(x) log(y)).

...therefore

    x^log(y) = y^log(x)

## Moral of exercise 0.2

The sum of a geometric series is Θ(first term) if the series is decreasing,
Θ(last term) if increasing, and Θ(number of terms) if unchanging.

## Linear recursion relations

Assume there exists a choice of c s.t. F(n) = 2^(cn) satisfies a recurrence
relation, say F(n) = F(n-1) + F(n-2).

Then 2^(cn) = 2^(c(n-1)) + 2^(c(n-2)). 

Let x = 2^c, then the recurrence is the quadratic equation x^2 - x - 1 = 0.

Hence x = (1 + 5^0.5)/2. If x = 2^c then must choose positive root, and c =
log2(1 + 5^0.5)/2 ~= 0.69 and F(n) ~= 1.61^n.

For c >~ 0.69, F(n) <= 2^(cn). For c < 0.69, F(n) > 2^(cn).

You can do this for any linear recurrence relation. For the particular choice
of the Fibonnaci sequence, if the equality holds then c = log2((1 + 5^0.5)/2)
and 2^c, the ratio between successive terms of the sequence is the golden
ratio.
