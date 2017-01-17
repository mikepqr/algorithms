# DPV Chapter 1

## Length of a number = ceil(logb(N+1))

With k digits in base b we can represent numbers N <= b^k - 1.

Rearranging and noting that k is an integer, k = ceil(logb(N+1)). Hence about
logb N digits are needed to write N in base b

To convert from base a to base b:

    logb N = loga N / loga b

i.e. logs to different bases differ only by a multiplicative constant. So the
size of N in base a is the same as in base b, times a constant factor. In
big-oh the base is therefore irrelevant and

    n = O(log N).

## Length of a number = floor(logb(N)) + 1

_Theorom_ for all b and N, ceil(logb(N+1)) = floor(logb(N)) + 1

_Proof_ by exhaustive case analysis

 - N is a power of b, N+1 is not
   ```
   floor(logb(N)) = logb(N)
   ceil(logb(N+1)) = logb(N) + 1
   ```
 - N+1 is a power of b, N is not
   ```
   ceil(logb(N+1)) = logb(N+1)
   floor(logb(N)) = logb(N+1) - 1
   ```
 - Neither is a power of b
   ```
   ceil(logb(N+1)) = ceil(logb(N) = floor(logb(N)) + 1
   ```
 - Both are powers of b. This is only possible if N=1, b=2. In this case
   ```
   ceil(log2(2)) = 1
   floor(logb(1)) + 1 = 1
   ```

∎

## Effect of arithemtic operations on length of a number

 - The sum of three 1-bit numbers is at most 2-bit long (see ex 1.1).

 - The sum of two n-bit numbers is at most (n+1) bits long. Two n-bit numbers
   are <= b^n - 1 each. Their sum is therefore <= 2b^n, which is a number of
   length <= log(2b^n), which is <= n + 1 for all b.

 - The product of two n-bit numbers is at most 2n bits long because the product
   of a number of length na and a number of length nb is most

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

See below: division (i.e. formation of the multiplicative inverse modulo N) is
O(n^3) when possible. It is only possible when the greatest common divisor of
the operands is 1.

## Modulo exponentiation

It is obviously true that

    x^y = { x^((y//2)^2)     if x is even
          { x * x^(y//2)^2   if y is odd

It's possible to implement a non-modulo multiplication algorithm (see
[expsq.py](../0/expsq.py)) that implements this non-recursively.

Recursively it can be written much like the French multiplication algorithm,
except we square z instead of doubling it, and the base case y = 0 yields 1.
See [arithmetic.py](arithmetic.py).

If x, y, and N are n bits, this recursive algorithm halts after n recursive
calls. Each call is a multiplication of n bit numbers (the numbers don't get
longer than this because we're working modulo N). Therfore total running time
is O(n^3).

## Euclid's rule

See [Khan
Academy](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)
(the proof in the book is very terse).

_Lemma_. If a, b ∈ ℕ where a >= b then gcd(a, b) = gcd(a - b, b)

_Proof_. Proof by showing gcd(a, b) no bigger than gcd(a - b, b) and also no
smaller than gcd(a - b, b).

    gcd(a, b) | a-b

because a = x gcd(a, b) and b = y gcd(a, b) where x, y ∈ ℕ.

    gcd(a, b) | b

by definition. gcd(a, b) is therefore a common divisor of a-b and b. 

Any common divisor of two numbers must be no bigger than the _greatest_ common
divisor. Hence,

    gcd(a, b) <= gcd(a-b, b).   [*]

Similarly

    gcd(a-b, b) | a

(same argument that shows gcd(a,b) | a-b) and 

    gcd(a-b, b) | b

by definition. gcd(a-b, b) is therefore a common divisor of a and b, and is
therefore no bigger than the _greatest_ common divisor.

    gcd(a, b) >= gcd(a-b, b).  [*]

The two equalities `[*]` ⇒ gcd(a, b) = gcd(a - b, b). ∎

_Theorem_. If x, y ∈ ℕ where x >= y then gcd(x, y) = gcd(x mod y, y)

_Proof_. The above lemma demonstrates that 

    gcd(x, y) = gcd(x - y, y).
    
But 

    gcd(x - y, y) = gcd(x - 2y, y)
    
also by the lemma. Repeated application yields

    gcd(x - y, y) = gcd(x - qy, y)

where q is the quotient in x = qy + r, and x mod y ≡ r. ∎

## Euclid's algorithm

Euclid's rule allows us to solve the smaller problem gcd(a mod b, b) instead of
gcd(a, b). And we can keep reducing the size of the problem until we reach a
base case, gcd(a, 0) = a.

This induces a recursive algorithm:

```python
def gcd(a, b):
    '''Return gcd(a, b) using Euclid's algorithm'''
    if b == 0:
        return a
    else:
        return gcd(b, mod(a, b))
```

## Euclid's algorithm running time

_Lemma_. If a >= b then a mod b <= a/2.

_Proof_. By exhaustive case analysis.

 - b <= a/2. a mod b < b ∀ b. Therefore a mod b < a/2
 - b > a/2. a mod b = a - b. Therefore a mod b < a/2

Therefore each recursion of Euclid's algorithm one of the two numbers at least
halves. Which number halves alternatves. So after two recursions both numbers
have halved. And after O(2n) = O(n) recursions the base case is reached. Each
recursion has a mod operation, which has the same big-Oh running time as
division, i.e. O(n^2).

Euclid's algorithm is therefore O(n^3).

## A test for a claimed gcd

_Lemma_. If d|a and d|b, and d = ax + by where x, y ∈ ℤ then d = gcd(a, b).

Which is to say, if presented with a claimed gcd(a, b) and two integer
coefficients x and y such that ax + by = d then d is indeed the gcd(a, b)

Note x, y need not be positive.

_Proof_. If d|a and d|b then d is a common divisor of a and b. Therefore 

    d <= gcd(a, b).

By definition gcd(a, b)|a and gcd(a, b)|b. gcd(a, b) divides any integer
coefficent linear combination of a and b, e.g. ax + by = d. 

    gcd(a, b)|d ⇒ gcd(a, b) <= d

    d <= gcd(a, b) ∧ gcd(a, b) <= d ⇒ d = gcd(a, b).

## Extended Euclid

This algorithms returns not just gcd(a, b), but the integers x and y that such
that ax + by = gcd(a, b).

```python
def egcd(a, b):
    '''Returns x, y, d such that d = gcd(a, b) and ax + by = d'''
    if b == 0:
        return 1, 0, a
    xprime, yprime, dprime = egcd(b, mod(a, b))
    x = yprime
    y = xprime - a//b * yprime
    d = dprime
    return x, y, d
```

_Proof_. Correctness of return value of d follows from gcd() above; if you
ignore x and y the algorithms are identical.

Correctness of x and y is proved by strong induction on b.

_Base step_. b = 0. egcd(a, 0) = 1, 0, a ∀ a. gcd(a, 0) = a. a = 1a + 0b ✓

_Inductive step_. Let I.H. be proposition that the algorithm is correct for all
values of a and all b < bi some specific choice of b.

The algorithm calculates egcd(a, bi) by calling egcd(b', a mod b'). 

a mod bi < bi by definition of mod. 

By inductive hypothesis the algorithm is correct for b < bi. 

Therefore the x' and y' it returns are correct for inputs bi and a mod bi, i.e.

    gcd(bi, a mod bi) = bx' + (a mod bi)y'

Now must show operations performed on x' and y' yield the desired x and y.

    d = gcd(a, bi) 
      = gcd(bi, a mod bi)
      = bi x' + (a mod bi)y'
      = bi x' + (a - a//bi bi)y'
      
Because p mod q = p - p//q * q by definition. Then

    d = ay' + bi (x' - a//bi y').

Therfore if x = y' and y = x' - a//bi y' then d = ax + bi y. ∎

The additional operations (floor division, multiplication and subtraction) in
Extended Euclid do not affect the running time. They are O(n^2) per recursion
as was the mod reduction. So the running time remains O(n^3).

## Modular inverse

x is the multiplicative inverse of a mod N if ax ≡ 1 (mod N)

The multiplicative inverse does not always exist. E.g. 2 mod 6 has no inverse
because no choice of x gives 2x ≡ 1 (mod 6). That's because 2x is even and the
possible values of 2x mod 6 are therefore 0, 2, or 6.

_Theorom_. if gcd(a, N) > 1 then no no multiplicative inverse of a mod N
exists, i.e. ax ≠ 1 (mod N) ∀ x ∈ ℕ.

_Proof_. gcd(a, N)|(ax mod N) because ax mod N can be written as an integer
coefficient linear sum of a and N. (ax mod N is simply N subtracted from ax a
bunch of times.)

If p|q and p > 1 then q > 1. Thus if gcd(a, N) > 1 then ax mod N > 1. 

ax mod N > 1 ⇒ ax ≠ 1 (mod N) ∀ x. ∎

## Relative primes

If gcd(a, N) = 1 then a and N are "relatively prime" and an inverse of a mod N
exists.

A prime number N is relatively prime to all non-zero integers.

## Finding multiplicative inverse

The extended Euclid algorithm gives a way of finding this inverse. It returns
integers x and y such that ax + Ny = 1.

Then ax ≡ 1 (mod N) because ax differs from 1 by an integer multiple of N.

And thus x is the multiplicative inverse of a mod N.

E.g. suppose we wish to compute the inverse of 11 mod 25. gcd(11, 25) = 1 so an
inverse exists. egcd(11, 25) tells us that

    -9*11 + 4*25 = 1

Reducing both sides modulo 25

    -9*11 ≡ 1 mod 25

So -9 ≡ 16 mod 25 is the inverse of 11 mod 25.

```python
def multinv(a, N):
    x, y, d = egcd(a, N)
    return mod(x, N)
```

## Modular division

      a has a multiplicative inverse modulo N 
    ⇔ a is relatively prime to N 
    ⇔ ax ≡ 1 mod N

where x is the multiplicative inverse, which can be found using Extended Euclid
in O(n^3).

## Fermat's little theorem

_Lemma_. If S the set of non-zero integers less than some prime number p i.e.
S = {1, 2, ... p-1} then pointwise multiplication by a mod p results in the same
set.

_Proof_. It suffices to prove that the result of the pointwise multiplication
is a set of distinct, non-zero elements all less than p, since there is only
one set with those properties.

 - The elements of the new set are non-zero because they were not, i.e. if 
   a.i ≡ 0 mod p then i must be 0, but no all elements of the original set were
   nonzero.

   (Note to show a.i ≡ 0 mod p we divide by a. This is possible because a and p
   are relatively prime. This is true because a is non-zero and p is prime by
   assumption.)

 - The elements are distinct because if they were not a.i ≡ a.j mod p and hence
   (dividing by a), i ≡ j (mod p). But the original elements of the set were
   all smaller than p, hence if i ≡ j (mod p) then i = j. But the original set
   was distinct.

 - The elements of the new set are < p because the new set is modulo p.

_Theorem_. If p is prime then ∀ 1 <= a < p

    a^(p-1) ≡ 1 (mod p)

_Proof_. Let S be the set of non-zero integers less than some prime number p,
i.e. S = {1, 2, ... p-1}.

The product of each element in this set is (p - 1)!

By lemma above, multipling every element in S by 1 <= a < p (modulo p) results
in the same set. 

i.e. if p is prime and 1 <= a < p then 

    {a.1 mod p, a.2 mod p, ... a.(p-1) mod p} = S

The product of each element in this set is a^(p-1) (p-1)! (mod p). Hence

    (p-1)! ≡ a^(p-1) (p-1)!   (mod p)

We can divide by (p-1)! because p is prime by assumption, so all other numbers
are relatively prime to it. Then

    a^(p-1) ≡ 1     (mod p)    

## Primality testing

Fermat's little theorem says that

    ∀ a ∈ ℕ, 1 <= a < N. N ∈ Primes ⇒ a^(N-1) ≡ 1    (mod N)

It therefore implies this testing strategy.

 - Choose 1 <= a < N at random. 
 - Is a^(N-1) ≡ 1 (mod N)
   - Yes ⇒ N might be prime
   - No ⇒ N is definitely not prime

How many a's do we need to test?

_Lemma_. Consider the claim a^(N-1) ≠ 1 mod N for some a relatively prime to N.
If this is true for >= 1 choice of 1 <= a < N then it must be true for at least
half of them.

_Proof_. Fix some value a for which a^(N-1) ≠ 1 (mod N).

For every element 1 <= b < N for which b^(N-1) ≡ 1 (mod N), there is an element
that fails the test a.b (mod N), because

    (a.b)^(N-1) = a^(N-1) b^(N-1)
                = a^(N-1)
                ≠ 1 (mod N)

All these a.b (mod N) are distinct for fixed a but different b. This is because
if a.i ≡ a.j mod N then, dividing by a (which is fine because a is relatively
prime to N by assumption), i ≡ j (mod N), but i, j < N and i ≠ j. 

So, if any item in the range 1 <= a < N fails the test then, for every number
that passes the test there is at least one number that fails it. ∎

Given this lemma, for a random choice of a:

 - Pr(N is prime and a^(N-1) ≡ 1 (mod N)) = 1
 - Pr(N is not prime and a^(N-1) ≡ 1 (mod N)) <= 1/2

For k random choices of a:

 - Pr(N is not prime and a^(N-1) ≡ 1 (mod N)) <= (1/2)^k

## Abundance of primes

_Lagrange's prime number theorem_. Let π(x) be the number of primes <= x. Then

    π(x) → (x/ln(x)) as x → infinity

So a random number < x has a change π(x)/x ~= 1 / ln(x) of being prime.

If x is n bits long, n = log2 x and

    ln(x) = log2(x)/log2(e) 
          = 1.44

So a ~1.44/n chance (or if x is n digits long in decimal, a ~0.43/n chance,
which is to say about 5% of 9-digit SSNs are prime).

## Generating random primes

 - Pick a random n-bit number N
 - Test it for primality
 - Repeat if not prime

If the primality test used is based on Fermat's little theorem, it is
sufficient to use it with relatively few bases (e.g. a = 2, 3, 5) since the
probability of a _random_ number being composite (i.e. passing Fermat's test
for any a ≠ 1) is extremely low.

See `randomprime()` in [arithmetic.py](arithmetic.py) for an implementation.

An event with chance 1/n of occuring halts on average within O(n) trials (see
exercises). Each trial is a constant number of modular exponentiations which
are O(n^3). The average running time is therefore O(n^4).

## One-time pad cryptography

x is a binary message. r is a binary string of the same length, previously
agreed upon by the participants. Let e(x, r) be a function that encodes the
message.

    e(x, r) ≡ x xor r

e is its own inverse and thus repeated application decodes the message

    e(e(x, r), r) = (x xor r) xor r
                  = x xor (r xor r)
                  = x xor 0
                  = x

But absent r, it is not easy to infer x from e(x, r).

    x   r   e(x, r)
    00  10  10
    01  11  10
    10  00  10
    11  01  10

Note that four different clear messages encode to the same encrypted message
for a different choice of r.

This scheme is single use, however. If you have two encrypted messages, (x xor
r) and (z xor r) then you can take their xor:

    (x xor r) xor (z xor r) = (x xor z) xor (r xor r)
                            = (x xor z) xor 0
                            = x xor z

If either message contains a string of zeros then the other message will appear
clear. If the messages have identical passages then this will show as a string
of 0s in x xor z.

## Bijection

f : X → Y is _injective_ iff each y ∈ Y is reached from exactly one x ∈ X

f : X → Y is _surjective_ iff each x ∈ X maps to exactly one y ∈ Y

So, if X = {x1, x2}, Y = {y1, y2}

    f(x) = {y1 if x1
           {y2 if x1

is injective, as each y ∈ Y is reached from one x ∈ X. But it is not surjective,
as x1 maps to both y1 and y2.

    f(x) = {y1 if x1
           {y1 if x2

is surjective as each x maps to one y, but it is not injective, as y1 can be
reached from two items in X.

A function that is both injective and surjective is _bijective_. Then each
element in each set has exactly one opposite number in the other set. This is
possible (but not necessary) ⇔ |X| = |Y|.

    f(x) = {y1 if x1
           {y2 if x2

This function is bijective.

A function is a bijection ⇔ The function is invertible.

## RSA encryption

A public key scheme to send a message x where x is a number modulo N (larger
numbers can be chunked).

The scheme is to exponentiate x to some number (the public key) modulo N. x can
then be recovered by exponentiating to some other number (the private key).
How are these numbers chosen?

_Theorem_. For any two primes p, q, let N = pq. For any e relatively prime to
(p - 1)(q - 1) the following properties hold:

  1. The mapping x → x^e (mod N) is a bijection on {0, 1 ... N-1}.
  2. If d is the multiplicative inverse of e modulo (p - 1)(q - 1). Then

     ```
     (x^e)^d ≡ x mod N
     ```

     i.e. exponentiation to d modulo N is the inverse of exponentiation to e
     modulo N.

_Proof_. Property 2 ⇔ Property 1 because a function that has an inverse iff it
is a bijection. 

Prove property 2, i.e. that exponentiation to d is the inverse of
expeonentiation to e (modulo N).

e is invertible modulo (p-1)(q-1) because it is chosen to be relatively prime
to this number.

The exponent ed in the putative inverse ≡ 1 mod (p-1)(q-1) by defintion of d.
Hence

    ed = 1 + k(p - 1)(q - 1)

for some integer k.

To show x^(ed) ≡ x mod N (as required is the inverse), we can show x^(ed) - x = 0
(mod N), i.e.

    x^(ed) - x = x^(1 + k(p - 1)(q - 1)) - x
               = x(x^(p-1)^k(q-1) - 1)

Fermat's Little Theorem tells us that if p is prime (which it is by assumption)
then x^(p - 1) ≡ 1 mod p. Hence

    x^(ed) - x ≡ 0 mod p

Similarly for q (which is also prime)

    x^(ed) - x ≡ 0 mod q

i.e. x^(ed) - x is divisible by both p and q.

Fundamental theorem of arithmetic says that every natural number can be
expressed as a product of a unique factorization of primes. If p and q are
among these primes for a given number then pq is also a factor of that number.
Hence if p and q divide (x^(ed) - x) then N = pq also divides it. Hence

    x^(ed) - x ≡ 0 mod N    ∎

## Fundamental theorem of arithmetic

(Not in the book)

    Every integer n >= 2 can be expressed as a product of primes and this
    factorization is unique up to rearrangement of the factors.

## Greatest common divisor by shared primes

Let

    A = p1^k1 p2^k2 ... pn^kn
    B = p1^j1 p2^j2 ... pn^jn

where p1..pn are primes and ki >= 0. (This is true ∀ A, B by fundamental
theorem.) Then

    gcd(A, B) = product(i=1, n) pi^min(ki,ji)

Or informally:

    gcd(A, B) is the product of their shared prime factors

For example:

    360 = 2^3 . 3^2 . 5
    756 = 2^2 . 3^3 . 7

2^2 3^2 = 36 is in both these lists. It's therefore a common divisor and by the
definition of gcd.

    gcd(360, 756) >= 36

But the bigger factors of 360 (any product of its primes) must be composed of
primes that are not factors of 756. 36 is therefore the _greatest_ common
divisor.

This is not a fast method to find gcd(A, B) since factorization is expensive.
But it allows you to derive an algorithm to compute the lcm.

## Lowest common multiple

Defined as the smallest positive m such that a|m and b|m.

Found by taking the product of the union of prime factors, e.g.

    360 = 2^3 . 3^2 . 5
    756 = 2^2 . 3^3 . 7

    lcm = 2^3 . 3^3 . 5. 7

Given a fast algorithm for gcd, however, there is a quicker way.

    gcd(a, b) . lcm(a, b) = ab

Hence

    lcm(a, b) = ab/gcd(a, b)

## Hash functions

Simple hash function (first digit, last digit, etc.) may suffer from
non-randomness in input.

Want to minimize collisions. If they hash to the same bucket then we must put a
list of numbers in the bucket, which increases lookup time. On the other hand,
we don't want as many buckets as there are possible inputs, since that number
is usually very large.

Example: IP addresses. There are 256^4 possible IP addresses. Perhaps we want
to story only 250.

Consider each IP quadruple of integers modulo n between 0 and 255, x = {x1,
..., x4}. We choose n > 255 so no harm in the modulo. As we'll see in a second,
we actually chose n = 257, because that's both greater than 255 and prime.

## Strategy to generate hash functions

Define a set of hash functions, and pick one randomly from this set. Each item
in the set is determined by k random numbers mod n, so there are n^k possible
hash functions.

    ha(x1, ..., xk) = Σ(i=1 to k) ai.xi mod n

e.g. For IP addresses with k=4 and n=257 we might have 

        a = {87, 23, 125, 4)
    ha(x) = (87x1 + 23x2 + 125x3 + 4x4) mod 257.

If the coefficients are selected at random then the following theorem is true.

_Theorem_. For any two distinct inputs x={x1, ... xk} and y={y1, ... yk}, and
for coefficients a={a1, ..., ak} chosen at random from {0, 1, ... n-1} where n
is some prime number

    Pr(ha(x) = ha(y)) = 1/n

_Proof_. A collision occurs when

    Σ(i=1 to k) ai.xi ≡ Σ(i=1 to k) ai.yi mod n

rearrange this equation to give

    Σ(i=1 to k-1) ai.(xi - yi) ≡ ak.(yk - xk) mod n
    
The lhs of this equation evaluates to some number, call it c. Thus the eqation
holds 

    ⇔ c = ak.(yk - xk) mod n.

n is chosen to be prime. Assume without loss of generality that x and y differ
in (at least) the kth part xk ≠ yk. 

Then we can take the inverse of yk - xk mod n:

    a4 = c.(yk - xk)^(-1) mod n

Which is to say, the equation holds ⇔ ak takes a unique number mod n (which
happens to be c). The probability of that if ak is randomly chosen is 1/n.

If the family of hash functions is of cardinality |H| then |H|/n of them result
in collisions for a particular distinct x and y.
