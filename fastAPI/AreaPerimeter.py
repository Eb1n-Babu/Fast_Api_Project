from fastapi import FastAPI

app = FastAPI()


class AreaPerimeter:
    def __init__(self, length,breadth):
        self.length = length
        self.breadth = breadth

    def rectangle(self):
        area = self.length*self.breadth
        perimeter = (self.length+self.breadth)*2
        print("area:",area)
        print("perimeter:",perimeter)
        return None

    @staticmethod
    def circle(radius):
        area = 3.14*radius**2
        perimeter = 2*radius*3
        print("area:",area)
        print("perimeter:",perimeter)
        return None

    @classmethod
    def square(cls,length):
        area = length*length
        perimeter = 2*length*2
        print("area:",area)
        print("perimeter:",perimeter)
        return None

cus = AreaPerimeter(10,5)
cus.rectangle()
cus.circle(5)
cus.square(5)