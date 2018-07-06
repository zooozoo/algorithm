![problem](hackeRank-problem/hackerRank-2018-07-05.jpg)

### answer

```python
def rotLeft(a, d):
    left = a[:d]
    right = a[d:]
    return right + left
```