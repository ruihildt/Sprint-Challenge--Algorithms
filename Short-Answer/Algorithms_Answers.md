#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This code has a time complexity of `O(n^3)`

```python
    a = 0 # O(1)
    while (a < n * n * n): # O(n^3)
      a = a + n * n # O(n^2)
```

b) This code has a time complexity of `O(n^2)`

```python
    sum = 0 # O(1)
    for i in range(n): # O(n)
      j = 1 # O(1)
      while j < n: # O(n)
        j *= 2 # O(1)
        sum += 1 # O(1)
```

c) This code has a time complexity of `O(n)`

```python
    def bunnyEars(bunnies):
      if bunnies == 0: # O(1)
        return 0 # O(1)

      return 2 + bunnyEars(bunnies-1) # O(n)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
```
    Step 1 - For a number `n` of floors, throw an egg from the floor `m` which has a value of `n / 2`.
        If the egg is broken,
            discard all floors with a number smaller than `m`.
            `m` is now your new `n`
            Proceed back to Step 1.

        If the egg isn't broken,
            discard all floors with a bigger than `m`.
            `m` is now your new `n`
            Proceed back to Step 1.
    
    Repeat until you have only one floor `n` left.
        If the egg breaks, the next floor is floor `f`.
        If the egg doesn't break, your are on floor `f`.
```

The runtime complexity is `O(n)`.