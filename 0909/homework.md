### 1. Compiled Bootstrap

##### 	부트스트랩을 적용하기 위한 CSS, JS 파일을 다운로드 받아 Django 프로젝트에 Static 파일의 형태로 	추가하고, 이 파일들을 활용하여 부트스트랩이 적용되도록 하기 위해 작성해야 할 코드를 제출하시오.

```html
settings.py에
STATICFILES_DIRS = [ BASE_DIR / 'static']
추가하고

static/css폴더 생성 후 bootstrap.css이동
static/js폴더 생성 후 bootstrap.js이동

base.html에서
{% load static %}
<link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">

<script src="{% static 'js/bootstrap.js' %"></script>
```

