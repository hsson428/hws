#### 1. Type Class

​	Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스	를 최소 5가지 이상 작성하시오.

```python
int, str, map, list, dict
```



#### 2. Magic Method

​	아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오

```python
__init()
# 객체 생성시 실행되는 함수
__del__()
# 객체 소멸시 실행되는 함수
__str__()
# print()함수로 객체 출력 시 출력할 내용을 정의
__repr__()
# 사용자가 객체를 이해할 수 있게 표현해주는 함수
```



#### 3. Instance Method

​	.sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정	의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3	가지 이상 그 역할과 함께 작성하시오.

```python
list.sort()
# 리스트를 정렬
list.count(a)
# 리스트에 a의 개수를 반환
list.append(a)
# 리스트에 a를 추가
```



#### 4. Module Import

```python
from fibo import fibo_recursion as recursion
```

