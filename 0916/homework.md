### 1. User Model BooleanField

##### 	django에서 기본적으로 사용하는 User 모델은 AbstractUser 모델을 상속받아 정의된다.

```python
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
```

​	• 아래의 models.py를 참고하여 User 모델에서 사용할 수 있는 칼럼 중 BooleanField 로 정의 된 컬럼		을 모두 작성하시오.

​		https://github.com/django/django/blob/master/django/contrib/auth/models.py

```
is_staff, is_active, is_superuser
```



### 2. username max length

##### 	django에서 기본적으로 사용하는 User 모델의 username 컬럼이 저장할 수 있는 최대 길이를 작성	하시오.

```
150

AbstractUser를 상속받기 때문에, 같은 django/contrib/auth/models.py의 AbstractUser class를 살펴보면 username에 대한 정의를 볼 수 있다.
```



### 3. login validation

##### 	단순히 사용자가 ‘로그인 된 사용자인지’만을 확인하기 위하여 User 모델 내부에 정의된 속성의 이름	을 작성하시오.

```
is_authenticated

위 2번 문제의 AbstractUser class는 또 AbstractBaseUser를 상속받음을 알 수 있고, django/contrib/auth/base_user.py에 위치한 해당 클래스 내부에 있다.
```



### 4. Login 기능 구현

##### 	다음은 로그인 기능을 구현한 코드이다. 빈 칸에 들어갈 코드를 작성하시오.

```
AuthenticationForm
login
form.get_user()
```



### 5. who are you?

##### 	로그인을 하지 않았을 경우 template에서 user 변수를 출력했을 때 나오는 클래스의 이름을 작성하	시오.

```
AnonymousUser
```



### 6. 암호화 알고리즘

##### 	Django에서 기본적으로 User 객체의 password 저장에 사용하는 알고리즘, 그리고 함께 사용된 해	시 함수를 작성하시오.

```
pbkdf2, sha256
```



### 7. Logout 기능 구현

##### 	로그아웃 기능을 구현하기 위하여 다음과 같이 코드를 작성하였다. 로그아웃 기능을 실행 시 문제가 	발생한다고 할 때 그 이유와 해결 방법을 작성하시오

```
logout은 함수명이기 때문에 무한 재귀에 빠진다.
장고의 logout함수를 import할 때에 as auth_logout을 붙여 import하면 해결된다.
```

