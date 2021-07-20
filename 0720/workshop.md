### 1. 간단한 N의 약수 (SWEA #1933)

```python
N = int(input('1부터 1000까지의 정수를 입력하세요'))
l = []
for i in range(1, N+1):
    if N % i == 0:
        l.append(i)
for i in l:
    print(i, end =' ')
```



### 2. 중간값 찾기 (SWEA #2063 변형)

```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24, 
]
center = len(numbers)//2
if length % 2:
    print(sorted(numbers)[length//2])
else:
    print( round( ( ( sorted(numbers)[center] + sorted(numbers)[center-1] ) / 2 ), 2) )
```



### 3. 계단 만들기

```python
number = int(input('자연수를 입력하세요:'))
# for i in range(number):
#    for j in range(i+1):
#        print(j+1, end=' ')
#    print()
    
for i in range(1, number + 1):
    for j in range(i+1):
        print(j, end=' ')
    print()
```

