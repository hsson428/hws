#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

```
- SPA는 Single Pattern Application의 약자이다.
- SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고,
이후부터는 페이지 갱신에 필요한 데이터만 전달받는다.
- Vue.js에서 말하는 ‘반응형’은 데이터가 변경되면 이에 반응하여,
연결된 DOM이 업데이트되는 것을 의미한다.
```

```
F -> Single Page Application
T
T
```



#### 2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시오.

```
M: Model
   JavaScript Object, Vue Instance내부에서 data로 사용되며, 값이 바뀌면 View(DOM)이 반응
V: View 
   DOM(HTML)
VM: ViewModel
	모든 Vue Instance, View와 Model 사이에서 data와 DOM 관련 모든 일을 처리
```



#### 3. 다음의 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

```
message
new Vue
'#app'
```

```html
<div id="app">
  {{  (a)  }}
</div>

<script>
  const app =  (b)  ({
      el:  (c)  ,
      data: {
          message: 'Hello World',
      },
  })
</script>
```

