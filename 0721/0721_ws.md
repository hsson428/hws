### 1. List의 합 구하기

``` python
def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(list_sum([1, 2, 3, 4, 5]))
```



### 2. Dictionary로 이루어진 List의 합 구하기

```python
def dict_list_sum(people):
    total_age = 0
    for person in people:
        total_age += person['age']
    return total_age

print(dict_list_sum([{'name': 'kim', 'age': 12},
               {'name': 'lee', 'age': 4}]) )
```



### 3. 2차원 List의 전체 합 구하기

```python
def all_list_sum(numberss):
    total = 0
    for numbers in numberss:
        for number in numbers:
            total += number
    return total
print(
    all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
)
```

