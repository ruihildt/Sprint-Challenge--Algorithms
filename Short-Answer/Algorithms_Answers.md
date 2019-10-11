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


