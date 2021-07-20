# workshop

### 1.

```python
number = int(input('자연수를 입력하세요: '))
for i in range(1, number+1):
    print(i)
```



### 2.

```python
number = int(input('자연수를 입력하세요: '))
# l = list(range(number, -1, -1))
# for i in l:
#     print(i)

# for i in range(number, -1, -1):
#    print(i)

for i in range(number+1):
    print(number-i)
```



### 3.

```python
number = int(input('1000이하의 자연수를 입력하세요: '))
print(sum(range(number+1)))
```

