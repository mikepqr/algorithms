# DPV Chapter 1

## Length of a number

With k digits in base b we can represent numbers N <= b^k - 1.

Rearranging and noting that k is an integer, k = ceil(logb(N+1)). Hence about
logb N digits are needed to write N in base b

To convert from base a to base b:

    logb N = loga N / loga b

i.e. logs to different bases differ only by a multiplicative constant. So the
size of N in base a is the same as in base b, times a constant factor. In
big-oh the base is therefore irrelevant and

    n = O(log N).

## Effect of arithemtic operations on length of a number

 - The sum of three 1-bit numbers is at most 2-bit long (see ex 1.1).

 - The sum of two n-bit numbers is at most (n+1) bits long. Two n-bit numbers
   are <= b^n - 1 each. Their sum is therefore <= 2b^n, which is a number of
   length <= log(2b^n), which is <= n + 1 for all b.

 - The product of two n-bit numbers is at most 2n bits long because the product
   of a number of length na and a nubmer of length nb is most

       ```
       Na Nb = (b^na - 1)(b^nb - 1) 
             <= b^(na+nb)
       ```
   
   The length of Na Nb <= log(Na Nb) <= log 2N if Na = Nb

## School addition

The school addition algorithm on two summands of length n produces a sum of
length <= n + 1. 

Each bit of the sum is found by summing at most 3 1-bit numbers the addition of
at most 3 1-bit numbers for each bit in the sum (the corresponding bits of the
summand, plus any carry bit), which is a constant time operation.

Running time is therefore O(n).

There is no faster algorithm in big-oh terms because it takes O(n) to even give
the input.

## School multiplication

Let x and y be two numbers of n bits. The school multiplication algorithm
shifts x right n times (once for each digit in y), forming n intermediate
products of length <= 2n. These n terms must be summed, which is n-1 pairs of
sums of O(2n) = O(n) digit numbers.

n-1 sums of cost O(n) each means running time is O(n^2).

## French method of multiplication

It's obviously true that

    x y = { 2x(y//2)        if y is even
          { x + 2x(y//2)    if y is odd

This yields a recursive algorithm, e.g. x = 8, y = 7 with a base case y = 0
(anything times 0 is zero) and a primitive operation of doubling.

    8 * 7 = 8 + (2 * 8 * 7//2)
          = 8 + (2 * 8 * 3)
          = 8 + (2 * (8 + (2 * 8 * 3//2)))
          = 8 + (2 * (8 + (2 * 8 * 1)))
          = 8 + (2 * (8 + (2 * (8 + 2 * 1//2))))
          = 8 + (2 * (8 + (2 * (8 + 2 * 0))))       # base case
          = 8 + (2 * (8 + (2 * 8)))
          = 8 + (2 * (8 + 16))
          = 8 + (2 * 24)
          = 8 + 48
          = 56

Note what we are effectively doing is breaking 7 down into binary:

    8 * 7 = 8*1 + 8*2 + 8*4

where each summand is reached by doubling the previous.

In python

```python
def double(x):
    return 2 * x


def fmult(x, y):
    print(x, y)
    if y == 0:
        return 0
    z = fmult(x, y//2)
    if y % 2 == 0:
        return double(z)
    else:
        return x + double(z)
```

If y is n bits long then this algorithm makes O(n) recursive calls (each
halving reduces the length of the number by 1 bit). Each recursive call
requires some constant time operations (multiply and divide by 2, i.e. bit
shifts; check final bit for parity) and a summation that is O(n) if x is n bits
long.

The running time is therefore O(n^2).

## Division

A simple recursive halving algorithm will allow you to perform integer
division returning quotient and remainder. Division by 2 is a constant time
operation (right shift).

To get x/y you simply double the quotient and remainder of (x/2)/y = q, r

There are a couple of edge cases.

 - If 2r > y then you must add one to q, and subtract y from r (so you don't
   use 5/3 = 1, 2 to say, e.g. 10/3 = 2, 4)

 - If x is odd then you add one to 2r. E.g. to get 12/5 (x is even)
   you simply double 6/5, i.e. 1, 1 → 2, 2. But to get 13/5, you start with
   
       ```
       (13//2)/5 = 6/5
                 = 1, 1
       ```

   then you double q and r and add 1 to r, i.e. 1, 1 → 2, 2 → 2, 3.

As with French multiplication, if x is n bits long this algorithm makes O(n)
recursive calls. Each recursion potentially involves addition/subtraction of an
n-bit number (y) and O(n) bit numbers q and r.

The running time is therefore O(n^2).

## Modulo arithmetic

The `mod` infix operator returns the remainder of x/N, e.g. 5 mod 3 = 2.

Two numbers are equivalent modulo N if they have the same remainder when
divided by N.

If this is true N divides x - y exactly, i.e. N|x-y or (x-y) mod N = 0.

    x ≡ y (mod N) ⇔ N|x-y

If x ≡ x' (mod N) and y ≡ y' (mod N):

 - x + y ≡ x' + y' (mod N)
 - xy ≡ x'y' (mod N)

i.e. it's possible to form the sum of x and y (mod N) by taking the sum of two
other numbers that are modulo equivalent to x and y.

The usual rules of associativity, commutativity and distributivity apply:

 - x + (y + z) ≡ (x + y) + z (mod N)
 - xy = yx (mod N)
 - x(y + z) = xy + xz (mod N)

## Modulo arithmetic running times

 - Addition modulo N involves taking the sum of two numbers < N. This sum is
   smaller than 2N. If it's greater than N then we must subtract N from it.
   Addition therefore involves addition and subtraction of numbers that never
   exceed 2N. Running time is therefore linear in the size of these numbers,
   i.e. O(n) = O(log N).

 - Multiplication modulo N of two numbers < N forms a product < N^2. We must
   divide the product by N 0 or 1 times to ensure it is less than N.
   Multiplication therefore involves multiplication of n-bit numbers and,
   potentially, division of n-bit numbers. Each of these operations can be done
   in O(n^2) using the non-modulo algorithms above. The running time is
   therefore O(n^2).

Note we don't need to divide (or equivalently do many subtractions) to do
modulo addition because we know the sum is less than 2N, so at most 1
subtraction of N will be required to make it less than N.

## Modulo exponentiation

It is obviously true that

    x^y = { x^((y//2)^2)     if x is even
          { x * x^(y//2)^2   if y is odd

It's possible to implement a non-modulo multiplication algorithm (see
[expsq.py](../0/expsq.py)) that implements this non-recursively. Recursively it
can be written much like the French multiplication algorithm, except we square
z instead of doubling it, and the base case y = 0 yields 1. See
[arithmetic.py](arithmetic.py).
