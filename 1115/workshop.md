#### 1. Todo 데이터를 가져오는 과정에서발생하는CORS Policy 관련 이슈 해결

```python
pip install django-cors-headers

# settings.py
INSTALLED_APPS = [
    'corsheaders',  # 추가(근데 이거 안해줘도 작동함...)
]
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",  # 요건 이미 있음
]
```



#### 2. Todo Create & Read

```javascript
// 2번 문제
      const title = this.title
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/todos/',
        data: { title }
      })
        .then(() => {
          this.$router.push({ name: 'TodoList' })
        })

// TodoList.vue
created: function () {
    this.getTodos()
  }
```



#### 3. Todo Delete

```js
// 3번 문제
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/todos/${todo.id}`
      })
        .then(() => {
          this.getTodos()
        })
```



#### 4. Todo Update (+ 실시간취소선 toggle)

```js
// 4번 문제
      const todoItem = {
        ...todo,
        is_completed: !todo.is_completed
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todoItem, // 왜 Object로 주면 안되는건가요
      })
        .then(() => {
          todo.is_completed = !todo.is_completed
        })
```

