### 1. SQL Query

##### 	위 countries 테이블을 바탕으로 아래 문제에 해당하는 SQL query문을 작성하고 실행하시오.

#### 1) countries 테이블을 생성하시오

```
CREATE TABLE countries (
   ...> room_num TEXT,
   ...> check_in TEXT,
   ...> check_out TEXT,
   ...> grade TEXT,
   ...> price INTEGER
   ...> );
```



#### 2) 데이터를 입력하시오.

```
INSERT INTO countries VALUES('B203', '2019-12-31', '2020-01-03', 'suite', 900);
INSERT INTO countries VALUES('1102', '2019-01-04', '2020-01-08', 'suite', 850);
INSERT INTO countries VALUES('303', '2019-01-01', '2020-01-03', 'deluxe', 500);
INSERT INTO countries VALUES('807', '2019-01-304', '2020-01-07', 'superior', 300);
```



#### 3) 테이블의 이름을 hotels로 변경하시오.

```
ALTER TABLE countries RENAME TO hotels;
```



#### 4) 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num과 price를 조회하시오.

```
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;
```



#### 5) grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오.

```
SELECT grade, COUNT(grade) FROM hotels GROUP BY grade ORDER BY COUNT(grade) DESC;
```



#### 6) 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오.

```
SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade='deluxe';
```



#### 7) 지상층 객실이면서 2020년 1월 4일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오.

```
SELECT * FROM hotels WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04' ORDER BY price;
```



### 2. SQL ORM 비교하기

##### 	주어진 정보를 활용하여 작성된 SQL문과 대응하는 ORM문을 작성하고 실행하시오.

#### 1) user 테이블 전체 데이터를 조회하시오.

```
User.objects.all()
```



#### 2) id가 19인 사람의 age를 조회하시오.

```
User.objects.filter(id=19).first().age
```



#### 3) 모든 사람의 age를 조회하시오. 

```
User.objects.all().values('age')
```



#### 4) age가 40 이하인 사림들의 id와 balance를 조회하시오.

```
User.objects.filter(age__lte=40).values('id', 'balance')
```



#### 5) last_name이 ‘김’이고 balance가 500 이상인 사람들의 first_name을 조회하시오. 

```
User.objects.filter(last_name='김', balance__gte=500).values('first_name')
```



#### 6) first_name이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오. 

```
User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
```



#### 7) balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오. 

```
User.objects.filter(Q(balance__gte=2000) | Q(age__lte=40)).count()
```



#### 8) phone 앞자리가 ‘010’으로 시작하는 사람의 총원을 구하시오. 

```
User.objects.filter(phone__startswith='010').count()
```



#### 9) 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오. 

```
user = User.objects.get(first_name='옥자', last_name='김')
user.country = '경기도'
user.save()

User.objects.get(first_name='옥자', last_name='김').updqte(country='경기도')
```



#### 10)이름이 ‘백진호’인 사람을 삭제하시오. 

```
user = User.objects.get(first_name='진호', last_name='백')
user.delete()
```



#### 11)balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오. 

```
User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]
```



#### 12)phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오.

```
User.objects.filter(phone__contains='123', age__lt=30)
```



#### 13)phone이 ‘010’으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오. 

```
User.objects.filter(phone__startswith='010').values('country').distinct()
```



#### 14)모든 인원의 평균 age를 구하시오.

```
User.objects.aggregate(Avg('age'))
```



#### 15)박씨의 평균 balance를 구하시오.

```
User.objects.filter(last_name='박').aggregate(Avg('balance'))
```



#### 16)경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오. 

```
User.objects.filter(country='경상북도').aggregate(Max('balance'))
```



#### 17)제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오. 

```
max_balance_for_jeju = User.objects.filter(country='제주특별자치도').aggregate(Max('balance'))
User.objects.filter(country='제주특별자치도', balance=max_balance_for_jeju).values('first_name')
```

