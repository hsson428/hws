### 1. Model 반영하기

​	*“Django가 Model에 생긴 변화를 DB에 반영하는 방법”* 을 뜻하는 용어를 작성하시오.

```
Migrations
```



### 2. Model 변경사항 저장하기

1.

```python
# 추천하지 않음, 검사하는 과정을 거칠 수 없음
Article.objects.create(title=title, content=content)

article = Article(title=title, content-content)
article.save()

article = Article()
article.title = title
article.content = content
article.save()
```



2. 이로 인해 생성된 마이그레이션 파일에 대응되는 SQL문을 확인하기 위한 명령어와 출력결과를 작성하시오. (app의 이름은 articles이다.)

```
python manage.py sqlmigrate

CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL);
```



### 3. Python Shell

​	Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 어떤 명령어를 	통해 해당 Shell을 실행할 수 있는지 작성하시오.

```
python manage.py shell_plus
```



### 4. Django Model Field

​	Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성하시오.

```
CharField(max_length= ), TextField(), DateTimeField(), DateField(), AutoField
```

