#### 1. M:N True or False

##### 	각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고, 틀렸다면 그 이유도 함께 작성하시오.

```
1) Django에서1:N 관계는 ForeignKeyField를 사용하고,
   M:N 관계는 ManyToManyField를 사용한다.
2) ManyToManyField를 설정하고 만들어지는 테이블 이름은
   “앱이름_클래스이름_지정한 필드이름”의 형태로 만들어진다.
3) ManyToManyField의 첫번째 인자는 참조할 모델,
   두번째 인자는 related_name이 작성 되는데 두 가지 모두 필수적으로 들어가야 한다.
```

```
1) T
2) T
3) F
```



#### 2. Like in templates

##### 	아래 빈 칸 (a)와 (b)에 들어갈 코드를 각각 작성하시오.

```
request.user
article.like_users
```



#### 3. Follow in views

##### 	모델 정보가 다음과 같을 때 빈칸 a, b, c, d, e에 들어갈 코드를 각각 작성하시오.

```
user_pk
followers
filter
remove
add
```



#### 4. User AttributeError

##### 	다음과 같은 에러 메시지가 발생하는 이유와 이를 해결하기 위한 방법과 코드를 작성하시오.

```
accounts앱에서 User model을 재정의하였는데, views.py에서 UserCreationForm을 재정의하지않고 그대로 사용하였기 때문에 에러가 발생하였다.

forms.py를 생성해
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class CustomUserCreationForm(UserCreationForm):
	class Meta():
		model = get_user_model()
		fields = UserCreationForm.Meta.fields
		
그 후 views.py에서 이것을 import해 사용하면 해결된다.
```



#### 5. follow templates

##### 	person 변수에는 view함수에서 넘어온 유저 정보가 담겨 있고, 모델 정보가 아래와 같을 때 빈칸 a, b, 	c, d, e에 들어갈 알맞은 코드를 각각 작성하시오.

```
person.followings.all
person.followers.all
user
person
person.pk
```

