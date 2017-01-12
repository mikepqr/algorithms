# BPV Chapter 1

## 1.1

_Theorem_. In any base the sum of three one digit numbers is at most a 2 digit
number.

A 1-digit number in base b is at most b - 1. The sum of three of them is at
most 3b - 3.

The maximum value that can be represented in a 2-digit number in base b is
b^2 - 1.

∀ b >= 2, b^2 - 1 >= 3b - 3. QED.

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

## 1.18

Euclid's algorithm

gcd(210, 588) = gcd(168, 210) = gcd(42, 168) = gcd(0, 42) =  42

Factorization

    210 = 2.3.5.7
    588 = 2.2.3.7.7

gcd(A, B) = product of shared prime factors = 2.3.7 = 42
