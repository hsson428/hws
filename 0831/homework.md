### 1. MTV

​	Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며, 각	각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는 역할을 간략히 서술하시오.

```
M: Model - DB와 매핑하는 역할
T: Templete - 사용자에게 보여주는 역할
V: View - Model과 Templete간 연결고리
```



### 2. URL

​	__(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다. __(a)__는 무엇	인지 작성하시오.

```
variable routing
```



### 3. Django template path

​	Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴	더 안의 __(a)__ 폴더 내부를 탐색한다. __(a)__에 들어갈 폴더 이름을 작성하시오.

```
templates
```



## ❖ Django Template Language

##### 아래 링크를 참고하여 각 문제들을 해결하기 위한 코드를 작성하시오.



##### 1) menus 리스트를 반복문으로 출력하시오.

```
menu
```



##### 2) posts 리스트를 반목문을 활용하여 0번 글부터 출력하시오.

```
post.pk
```



##### 3) users 리스트가 비어있다면 현재 가입한 유저가 없습니다. 텍스트를 출력하시오.

```
empty
```



##### 4) 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

```
if
else
```



##### 5) 출력된 결과가 주석과 같아지도록 하시오.

```
length
```



##### 6) 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 작성하시오.

```
Y년 M월 d일 (D) A h:i
```



## ❖ Form tag with Django

##### 1) 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오.

```
양식 데이터를 처리할 프로그램의 URI
```



##### 2) 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오.

```
POST
```



##### 3) input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고 submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.

```
/create/
```

