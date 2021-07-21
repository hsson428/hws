### 1. Built-in 함수

sum(), print(), sorted(), min(), max(), list.append(), list.sort()



### 2. 정중앙 문자

```python
def get_middle_char(string):
    middle = len(string) // 2
    if len(string) % 2:
        middle = string[middle]
    else:
        middle = string[middle-1:middle]
    return middle
```



###  3. 위치 인자와 키워드 인자

```python
(4)
매개변수 지정한 인자가 위치인자보다 먼저 나올 수 없음
```



### 4. 나의 반환값은

```python
None
```



### 5.  가변 인자 리스트

```python
def my_avg(*args):
    length = len(args)
    mean = sum(args)/length
    return round(mean, 1)

print(my_avg(77, 83, 95, 80, 70))
```















