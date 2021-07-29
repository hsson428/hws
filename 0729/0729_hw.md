#### 1. Circle 인스턴스 만들기

​	아래와 같은 Circle 클래스가 있을 때, 반지름이 3이고 x, y좌표가 (2, 4)인 Circle 인스턴스	를 만들어 넓이와 둘레를 출력하시오.

```python
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.pi

    def center(self):
        return (self.x, self.y)

c1 = Circle(3, 2, 4)
print(c1.area())			# 28.259999999999998
print(c1.circumference())	# 19.7192
```



#### 2. Dog과 Bird는 Animal이다

​	다음과 같이 Animal 클래스가 주어질 때, 해당 클래스를 상속 받아 아래의 보기와 같이 동	작하는 Dog 클래스와 Bird 클래스를 작성하시오.

```python
class Animal:
    def __init__(self, name):
        self.name = name
       
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):

    def walk(self):
        print(f'{self.name}! 달린다!')
    
    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):

    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
```



#### 3. 오류의 종류

​	아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.

```python
ZerodivisionError: 0으로 나눌 시
NameError: 지역 또는 전역 이름을 찾을 수 없을 때 발생합니다.
TypeError: 지정된 타입이 수행할 수 없는 명령을 내릴 시
IndexError: 범위를 벗어날 때
KeyError: Key가 없을 시
ModuleNotFoundError: 모듈을 찾을 수 없을 때, sys.modules 에서 None 이 발견될 					   때도 발생
ImportError: 모듈을 로드라는데 문제가 있을 때
```

