class Polygon():
    """A class to capture common utilities for dealing with shapes"""
    def __init__(self, side_lengths: list[int]):
        self.side_lengths = side_lengths

    def __str__(self):
        return 'Polygon with %s sides' % self.num_sides

    @property
    def num_sides(self):
        return len(self.side_lengths)

    @property
    def perimeter(self):
        return sum(self.side_lengths)


class Rectangle(Polygon):

    def __init__(self, height: int, width: int):
        super().__init__([height, width, height, width])


    @property
    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]


class Square(Rectangle):

    def __init__(self, side: int ):
        super().__init__(side, side)



myRectangle = Rectangle(5 , 12)
mySquare = Square(20)

print(myRectangle)
print(myRectangle.area)
print(mySquare)
print(mySquare.area)

