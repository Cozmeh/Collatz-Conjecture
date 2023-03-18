# Collatz Conjecture
The Collatz Conjecture, also known as the **`3n + 1 problem or the Hailstone sequence`**, is a famous mathematical problem that has fascinated mathematicians for decades. It is a simple problem to state, but despite numerous efforts, it remains unsolved to this day.

### Problem Statement
The problem can be stated as follows: Start with any positive integer n. If n is even, divide it by 2, otherwise, if it is odd, multiply it by 3 and add 1. Repeat this process with the resulting number, and continue iterating in this way. The conjecture states that no matter what starting number you choose, the sequence will eventually reach 1.

```
For example, let's start with n = 6:

6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```
> As you can see, the sequence eventually reaches 1. The conjecture suggests that this is true for all starting values of n.

### Properties
Despite its simplicity, the Collatz Conjecture has some interesting properties. For example, the sequence can be quite long before reaching 1. Additionally, there are some starting values that produce very long sequences before eventually reaching 1. For example, the starting value of 27 produces a sequence of 111 steps before eventually reaching 1. Similarly, the starting value 63728127 produces a sequece of 949 steps before reaching 1.
```
less than 10 is 9, which has 19 steps,
less than 100 is 97, which has 118 steps,
less than 1,000 is 871, which has 178 steps,
less than 10,000 is 6171, which has 261 steps,
less than 100,000 is 77031, which has 350 steps,
less than 1 million is 837799, which has 524 steps,
less than 10 million is 8400511, which has 685 steps,
less than 100 million is 63728127, which has 949 steps,
less than 1 billion is 670617279, which has 986 steps,
less than 10 billion is 9780657631, which has 1132 steps,
and
less than 100 billion is 75128138247, which has 1228 steps.
```
### Importance
The Collatz Conjecture has been studied extensively by mathematicians and computer scientists alike. While it may seem like a simple problem, it has implications for a wide range of mathematical fields. For example, **`it has connections to number theory, combinatorics, and even chaos theory`**. Additionally, it has been used to test the limits of computational power, as there are some starting values that produce extremely long sequences.

# Python Module


