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

## Length of items in sequence

If a sequence grows as O(2^n) then the nth item has O(n) bits.

See 0.4(c).

## Proving Θ of a sequence with n terms

See 0.1(q) and http://stackoverflow.com/a/2095472/409879 for examples.

All the terms are smaller than the biggest term (duh) and there are n of them
therefore sequence is O(n x biggest term).

To prove lower bound, discard the first half of the sequence. f(n) is obviously
>= what remains. What remains is >= first term in second half of sequence x
n/2, since all later terms are larger.

For example, to prove that log(n!) = Θ(n log(n)):

log(n!) = log(1) + log(2) + log(3) ... log(n) = O(n log(n)) because the largest
term is log(n) and there are n terms so clearly the sum is no larger than n
log(n).

Now discard first half. Then log(n!) >= log(n/2) + ... + log(n)
>= log(n/2) ... log(n/2) = n/2 log(n/2) = Ω(n log(n))

log(n!) = O(n log(n)) and Ω(n log(n)) therefore Θ(n log(n)).
