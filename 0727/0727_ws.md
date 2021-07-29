#### 1. 무엇이 중복일까

문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 **duplicated_letters** 함수를 작성하시오.

```python
def duplicated_letters(string):
    duplicated = []
    for alphabet in string:
        if string.count(alphabet) > 1 and alphabet not in duplicated:
            duplicated.append(alphabet)
    return duplicated

print(low_and_up('apple'))
print(low_and_up('banana'))
```



#### 2. 소대소대

​	문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는 	**low_and_up** 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만 구성된다.

```python
def low_and_up(string):
    # new_str = []
    new_str = ''
    for i in range(len(string)):
        if i % 2 == 1:
           # new_str.append(string[i].upper())
        	new_str += string[i].upper()
        else:
           # new_str.append(string[i].lower())
    # return ''.join(new_str)
	return new_str
print(low_and_up('apple'))
print(low_and_up('banana'))
```



#### 3. 숫자의 의미

​	정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남 기고 제	거한 list를 반환하는 lonely 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담 긴 list의 요소	들은 기존의 순서를 유지해야 한다.

```python
def lonely(l):
    new_l = [l[0]]
    for i in l:
        if i != new_l[-1]:
            new_l.append(i)
    return new_l

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))
```

