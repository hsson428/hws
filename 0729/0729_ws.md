#### #. 도형 만들기

​	아래의 명세를 읽고 Python 클래스를 활용하여 점(Point)과 사각형(Rectangle)을 표현하	시오

```python
class Point:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
    
    def get_area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)

    def get_perimeter(self):
        return ((self.p2.x - self.p1.x) + (self.p1.y - self.p2.y)) * 2

    def is_sqaure(self):
        return self.p2.x - self.p1.x == self.p1.y - self.p2.y

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())		# 4
print(r1.get_perimeter())	# 8
print(r1.is_sqaure())		# True
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())		# 9
print(r2.get_perimeter())	# 12
print(r2.is_sqaure())		# True
```

