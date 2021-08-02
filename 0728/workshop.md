#### 1. pip

​	아래 명령어는 **(1) 무엇을 위한 명령인지 (2) 실행은 어디에서 해야하는지** 작성 하시오.

``` bash
$ pip install faker

(1) package 설치
(2) cmd
```



#### 2. Basic Usages

​	Faker는 다양한 메서드를 통해 임의의 결과값을 반환해준다. 임의의 영문 이름을 반환하	는 아래 코드에서 라인별 의미를 주석을 참고하여 작성하시오.

```python
from faker import Faker  # faker패키지에서 Faker클래스를 불러오기 위한 코드
fake = Faker()			 # Faker는 클래스, fake는 인스턴스 이름이다
fake.name()				 # name()은 Faker()클래스의 메소드이다.
```



#### 3. Localization

​	Faker는 다양한 언어의 Locale을 지원한다.

```python
class Faker():
    def __init__(self, lang)
    	pass
```



#### 4. Seeding the Generator

​	컴퓨터 프로그래밍에서 임의의 값을 반환하는 경우(난수 생성 등) 시드라는 개념이 있다. 	시드를 설정하게 되면 동일한 순서로 난수를 발생시킬 수 있어 일반적으로 디버깅을 위하	여 활용 된다.

​		**아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고, seed()는 어		떤 종류의 메서드인지 작성하시오.**

```python
from faker import Faker
fake = Faker('ko_KR')
Faker.seed(4321)			# seed()는 클래스 메소드

print(fake.name())			# 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())			# 이지후
```

**아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고, seed_instance()는 어떤 종류의 메서드인지 작성하시오.**

```python
fake = Faker('ko_KR')
fake.seed_instance(4321)	# seed.instance()는 인스턴스 메소드

print(fake.name())			# 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())			# 계속 바뀜
```

```python
클래스 메서드: 클래스 전체를 변경
인스턴스 메서드: 호출한 객체에만 영향
```

