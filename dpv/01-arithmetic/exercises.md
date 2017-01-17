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

## 1.4

See [0/notes](../0/notes.md).

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

Recall  that if two numbers are equal then their prime factorizations are equal
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
