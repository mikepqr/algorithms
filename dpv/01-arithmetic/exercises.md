# BPV Chapter 1

## 1.1

_Theorem_. In any base the sum of three one digit numbers is at most a 2 digit
number.

A 1-digit number in base b is at most b - 1. The sum of three of them is at
most 3b - 3.

The maximum value that can be represented in a 2-digit number in base b is
b^2 - 1.

∀ b >= 2, b^2 - 1 >= 3b - 3. QED.

## 1.2

### a

_Theorem_. Any binary integer is at most four times longer than the
corresponding decimal.

_Proof_. Let length of number N in binary be n2, decimal be n10. Then we want
to show n2/n10 <= 4 ∀ n ∈ ℕ

    n2 = floor(log2(N)) + 1
    n10 = floor(log10(N)) + 1

To show that the ratio of these quantities is always less than 4, it is
sufficient to show that n2/n10 is less than some other quantity that is less
than 4.

That quantity will be the largest possible value of n2/n10, given the most
extreme behaviour of the floor function possible, i.e. 

    floor(log2(N)) ~= log2(N) and
    floor(log10(N)) ~= log10(N) - 1

Then

    n2/n10 = [floor(log2(N)) + 1] / [floor(log10(N)) + 1]
           <= (log2(N) + 1)) / log10(N)

It is not simply to show this is generally true, but we can show it is true for
N > some number, and check smaller values by hand. Continuing...

If this quantity is <= 4 then n2/n10 is <= 4, i.e.

              log2(N) + 1 <= 4 log10(N)
    log10(N)/log10(2) + 1 <= 4 log10(N)
      log10(N) + log10(2) <= 4 log10(N).log10(2)
                 log10(2) <= [4 log10(2) - 1] log10(N)

Hence

    log10(N) >= log10(2)/[4 log10(2) - 1]
           N >= 29.8

The theorem thus holds for N >= 30. It is thus sufficient to check it manually
for smaller values:

```python
>>> all((len(bin(N)[2:])/len(str(N))) <= 4 for N in range(1, 30))
True
```

### b

For very large N

    n2/n10 = [floor(log2(N)) + 1] / [floor(log10(N)) + 1]
           ~= log2(N)/log10(N)
           = 1/log10(2)
           = 3.32

## 1.3

kmax, the deepest such a tree can be is n, the number of nodes.

If each node has the maximum number of children then the tree is its
shallowest, kmin. Consider such a tree. It has 1 node at the root, d at the
next level, d^2 at the next and d^kmin at the final kmin'th level. Hence

    N = 1 + d + d^2 ... d^kmin
      = (1 - d^kmin)/(1 - d)
      = (d^kmin - 1)/(d - 1)

Then

    d^kmin = N(d-1) + 1
      kmin = log(Nd - N + 1)/logd

For N >> d this is ~ log(Nd+1)/logd, which is Ω(log N/log d)

## 1.4

See [0/notes](../0/notes.md).

## 1.5

Harmonic series

    Σ(i=1 to n) 1/i 

Upper bound: change each denominator to a smaller number, namely the previous
power of 2.

    Σ(i=1 to n) 1/i < 1/1 + 1/2 + 1/2 + 1/4 + 1/4 + 1/4 + 1/4 + 1/8 ...
                    < 1/1 + 2/2 + 4/4 + 8/8 ... n/n

i.e. number of powers of 2 that are less than n, which is log n.

Lower bound: change each denominator to a bigger number, namely the next power
of 2
    
    Σ(i=1 to n) 1/i > 1/1 + 1/2 + 1/4 + 1/4 + 1/8 + 1/8 + 1/8 + 1/8 ...
                    < 1/1 + 1/2 + 2/4 + 4/8 ... n/2n

i.e. half the number of powers of 2 that are less than n, which is 1/2 log n.

Hence the series is Θ(log n).

p.s. turns out that this series ~= ln n + A for large n, where A is a constant.
Given that we can write down that it is Θ(log n), since ln n differs from log n
by a multiplicative constant.

## 1.6

## 1.7

School multiplication of a and b, where a is n and b is m bits long.

a is shifted right m bits (one for each bit in b). Each of these intermediate
products is no more than n+m bits long.

To combine them we sum m-1 pairs of numbers, each of which is no longer than
n+m bits.

Hence Θ(m(n+m)). Note this reduces to Θ(n^2) when n = m.

## 1.8

See [notes](notes.md) and [arithmetic.py](arithmetic.py).

## 1.9

Given:

 1. x ≡ x' mod N ⇔ N|x-x'
 2. x ≡ x' mod N
 3. y ≡ y' mod N

1. ⇒ x = x' + aN and y = y' + bN. Hence 

    x + y = x' + y' + (a+b)N.

Modulo N of both sides (i.e. drop any terms that are divisible by N) gives 

    x + y = x' + y' mod N.

Also 

    xy = x'y' + bNx' + aNy' + abN^2
       ≡ x'y' mod N

## 1.10

Given:

 1. a ≡ b mod N

    Hence a and b differ by a multiple of N, i.e. a + kN = b.

 2. M|N

    Hence jM = N

So a + jMN = b, i.e. a and b differ by a multiple of M ⇒ a ≡ b mod M

## 1.11

4^1536 - 9^4824 is divisible by 35 iff 4^1536 ≡ 9^4824 mod 35.

    4^1536 = 4^12^128 ≡ 1 mod 35
    9^4824 = 9^6^804 ≡ 1 mod 35

Hence they are congruent mod 35.

## 1.12

    2^2^2006 = 4^2006 ≡ 1^2006 mod 3 ≡ 1 mod 3

## 1.13

     5^30000 = 125^10000 ≡ 1^10000 mod 31 ≡ 1 mod 31
    6^123456 = 6^6^20576 ≡ 1^20576 mod 31 ≡ 1 mod 31

Hence the difference of 5^30000 and 6^123456 is divisible by 31.

(Note 6^6 ≡ 1 mod 31)

## 1.14

In 0.4 we derived an algorithm to compute the nth Fibonnaci number by
performing O(log n) multiplications.

In the regular algorithm the numbers get longer. In modulo p, they are never
larger than p and therfore of length O(log p). 

Multiplication of b bit numbers is O(b^2).

Hence the total running time is O((log p)^2 log n).

## 1.15

This is the "modulus cancellation law". See
http://math.stackexchange.com/q/392404/399542 and
http://home.scarlet.be/~ping1339/congr.htm.

_Theorem_. If gcd(c, x) = 1 then

    ax ≡ bx mod c ⇔ a ≡ b mod c

_Proof_.

    c|ax-bx or c|(a-b)x. 

If one number divides another then they differ only by a multiplicative
constant, s:

    sc = (a-b)x.

Recall that if two numbers are equal then their prime factorizations are equal
(fundamental theorem).

Hence the prime factorization of sc contains exactly the primes in the prime
factorization of (a-b)x

For example, if p is a prime dividing m then p must be a prime dividing either
a-b or x. 

But we know gcd(c, x) = 1 so there are no primes that divide both c and x.
Hence the prime p divides a-b. Apply this to all the primes in m, and you
deduce they are all factors of a-b, hence m itself divides a-b ∎

## 1.18

Euclid's algorithm

gcd(210, 588) = gcd(168, 210) = gcd(42, 168) = gcd(0, 42) =  42

Factorization

    210 = 2.3.5.7
    588 = 2.2.3.7.7

gcd(A, B) = product of shared prime factors = 2.3.7 = 42

## 1.19

_Lemma_. gcd(a + b, b) = gcd(a, b).

_Proof_. If some number d|a then d|a+b iff d|b. Hence:

 - all common divisors of a and a+b are also divisors of b
 - all common divisors of a and b are also divisors of a

Therefore (a, a+b) and (a, b) share the same common divisors, therefore they
share a _greatest_ common divisor ∎

_Theorem_. The nth and n+1th Fibonnaci numbers are relatively prime ∀ n >= 1.

_Proof_. By induction on n.

_Base step_. n = 1. F1 = 1. F2 = 1. gcd(F1, F2) = 1, i.e. F1 and F2 are
relatively prime.

_Inductive step_. Assume n and n+1th Fibonnaci numbers are relatively prime.
Now show n+1th and n+2th are relatively prime.

    gcd(Fn+2, Fn+1) = gcd(Fn+1 + Fn, Fn + 1)
                    = gcd(Fn, Fn+1)
                    = 1 by assumption ∎

## 1.20

Inverses:

    20 4 ≡ 1 mod 79
    3 21 ≡ 1 mod 62
    5 14 ≡ 1 mod 23

21 and 91 are not relatively prime (7 divides both) so there is no inverse.

## 1.21

    φ(n) = number of numbers < n that are relatively prime to n
         = number of numbers < n that have inverses mod n

Alternatively, φ(1331) is the number of numbers smaller than 1331 that are not
divisible by n. The number of numbers less than 1331 that _are_ divisible by n
is 1331/11 = 121. Hence φ(n) = 1331 - 121 = 1210.

## 1.24

If p is prime then p^n has only one distinct prime factor in its factorization,
namely p.

p^n is therefore relatively prime to all numbers that are not divisible by p.

There are p^n (1 - 1/p) such numbers.

## 1.25

>>> arithmetic.modexp(2, 125, 127) = 64

## 1.27

Given

    p = 17, q = 23, N = 391, e = 3, message = 41

ed ≡ 1 mod (p-1, q-1)

```python
>>> d = arithmetic.multinv(3, (17-1) * (23-1))
>>> print(d)
235
>>> public = (17 * 23, 3)
>>> private = (17 * 23, 235)
>>> print(rsa.encode(41, public))  # message = 41
105
>>> print(rsa.decode(105, private))  # check decryption
41
```

## 1.28

Given

    p = 7, q = 11

Using [rsa.py](rsa.py) e = 7 and d = 43 will work.

## 1.31

### a

n! is approximately log n! long.

We showed in [previous chapter](../00-big-oh/notes.md) that 

    log n! = Θ(n log n).

## 1.33

    lcm(a, b) = ab / gcd(a, b)

Use Euclid to compute gcd in Θ(n^3).

## 1.34

Expected number of coin tosses before getting a head. Each toss is independent
with probability p.

Clearly we must toss the coin at least once. With probability p we toss head
immediately, i.e. N=1. With probability 1-p we toss tails and start again,
facing the same expected number of tosses more, plus the one we already did.

Hence

    E(N) = p.1 + (1-p).(1 + E(N))

and

    E(N) = 1/p
