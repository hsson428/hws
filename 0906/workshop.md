##### 1. Model Form을 정의하기 위해 빈칸에 들어갈 코드 (a), (b)를 작성하시오.

```python
forms.ModelForm

Meta()
```



##### 2. 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해	보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오.

```
유효하지 않은 글을 작성하였을 때, (예를 들어 칸이 비어있다던지)
실행될 코드가 없기 때문에 None을 반환하게 되어 에러가 나게 된다.
```



##### 3. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드 (a), (b)를 작성하시오.

```python
form = ArticleForm(request.POST, instance=reservation)

form = ArticleForm(instance=reservation)
```



##### 4. form 출력을 구현하기 위해 빈칸 (a)에 작성 할 수 있는 코드를 모두 작성하시오.

```
as_table
as_p
as_ul
```

