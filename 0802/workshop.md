#### 1. img tag

​	아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image 폴더 	안의 my_photo.png를 보여주는 <img> tag를 작성하시오. 단, 이미지가 제대로 출력되지 	않을 때는 ssafy 문자열이 출력 되도록 작성하시오.

```html
<img src="C:\Users\Windows 10\Desktop\image\my_photo.png" onerror="document.write('ssafy')"
alt="ssafy">
```



#### 2. 파일 경로

​	위와 같이 경로를 __(a)__로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되	었을 때 이미지를 불러 올 수 없게 된다. 이를 해결 하려면 이미지 경로를 __(b)__ 로 바꾸어 작	성하면 된다. __(a)__와 __(b)__에 들어갈 말과 __(b)__ 로 변경한 코드를 작성하시오.

```
(a) 절대경로
(b) 상대경로

../image/my_photo.png
```



#### 3. Hyper Link

```html
<a href="ssafy.com">
  <img src="C:\Users\Windows 10\Desktop\image\my_photo.png">
</a>
```



#### 4. 선택자

	1) 아래의 코드를 작성하고 결과를 확인 하시오.
 	2) nth-child를 nth-of-type으로 변경하고 결과를 확인 하시오.
 	3) 작성한 코드를 참고하여 nth-child()와 nth-of-type()의 차이점을 작성하시오

```html
<div id="ssafy">
  <h2>어떻게 선택 될까?</h2>
  <p>첫번째 단락</p>
  <p>두번째 단락</p>
  <p>세번째 단락</p>
  <p>네번째 단락</p>
</div>

#ssafy > p:nth-child(2) {
  color: red;
}					<!-- 첫번째 단락이 바뀜-->

#ssafy > p:nth-of-type(2) {
  color: blue;
}					<!-- 두번쩨 단락이 바뀜 -->

<!-- 
:nth-child(n)는 부모의 n번째 자식인 요소에 적용
:nth-of-type(n)은 부모의 지정 요소 중 n번째 자식에 적용
-->
```

