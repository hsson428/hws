### 1. Mutable & Immutable

```
immutable: String, Tuple, Range
mutable : List, Set, Dictionary
```



### 2. 홀수만 담기

```python
l = list(range(1, 51, 2))
print(l)
```



### 3. Dictionary 만들기

```python
students = {
    '손형선': 27,
    '서민기': 27,
    '손영배': 30,
    '안재영': 28,
    '이기진': 27,
 }
```



### 4. 반복문으로 네모 출력

```python
n = 5
m = 9

for i in range(m):
    print('*' * n)
```



### 5. 조건 표현식

```python
temp = 36.5
# print('입실 불가') if temp >=37.5 else print('입실 가능')
print('입실 불가' if temp >=37.5 else '입실 가능')
```



### 6. 평균 구하기

```python
scores = [80, 89, 99, 83]
print( round( sum(scores)/len(scores), 2 ) )
```

