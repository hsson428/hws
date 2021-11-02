#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

```
- Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로
할당하는 역할을 한다.
- XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 JavaScript API이다.
XHR의 메서드로 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다.
- axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는
라이브러리이다.
```

```
T
T
T
```



#### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

```
1. 첫 코드가 call stack에 들어갑니다. (실행됨)
2. 두번째 코드가 Web api에 들어가 1초 대기합니다.
3. 세번째 코드가 call stack에 들어갑니다. (실행됨)
4. web api에 들어갔던 두번째 코드가 1초 후 task queue에 들어갑니다.
5. task queue에 두번째 코드 밖에 없기에 call stackd으로 들어갑니다.(실행됨)
```



```
Single Thread
한 명이 여러가지 일을 빠르게 왔다갔다하며 진행

여러 명이 일을 하는 느낌
```

