import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

    def distance(self, A):
        return math.sqrt((self.x-A.x)**2 + (self.y-A.y)**2)

    @staticmethod
    def get_distance(A, B):
        return math.sqrt((A.x-B.x)**2 + (A.y-B.y)**2)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


# Using Point Class
point1 = Point(4, 4)
point2 = Point(6, 8)

point1.move()
point1.draw()

print(Point.get_distance(point1, point2))
print(point1.distance(point2))
print(point2.distance(point1))


# Using Person Class
person1 = Person("John Doe")
print(person1.name)
person1.talk()

person2 = Person("Aaman Rahman")
person2.talk()