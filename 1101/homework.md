#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

```
- JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다.
- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이
완료되면 Call Stack에 바로 할당된다.
- Promise 객체를 생성할 때 인자로 받는 callback 함수인 resolve와 reject는
비동기 처리가 성공/실패했을 경우 전달할 인자와 함께 호출된다.
- Promise 객체의 .then 메서드는 오류 없이 resolve 되었을 때 실행되는 함수이며,
.catch 메서드는 도중에 오류가 발생하여 reject 되었을 때 실행되는 함수이다.
```

```
T
F
T
T
```



#### 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

```
동기 함수는 완료될 때까지 코드를 잔행할 수 없지만
비동기 함수는 다른 코드를 진행시킵니다.
```



#### 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```
get
then
response.data
```

