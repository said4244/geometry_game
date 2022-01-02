from random import randint
# the idea:
#   the program'll give you 2 coordinates of a random rectangle
#   and you have to guess a coordinate that is inside the rectangle

#preplan
#first question to ask yourself if: what are the objects in this situation
                    #the answer is: The rectangle and the point

#now we need to think of a class for every object
#   class rectangle
#   class point

#now we need to think of method(s) for every class
#   class rectangle with a method that 1. creates 2 random x-coordinates that are not the same
#                                      2. creates 2 random y-coordinates that are not the same
#   class point with a method that 1. checks if the given x is not bigger than the biggest x coordinate and not smaller than the smallest x
#                                  2. checks if the given y is not bigger than the biggest x coordinate and not smaller than the smallest y
#                                  3. prints a sting saying False / True

class Point: # point class with the method above

  def __init__(self, x, y): #__init__ function where the x and y's should be
      self.x = x #defining the x with self so we can reach it from other function
      self.y = y
  
  def in_rectangle(self, rectangle): #the method with the coordinates of the rectangle(lowleft and upright)pointx = Point(6, 7)
    if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
      return True
    else:
      return False
    #comparting self.x with x.lowleft and x.upright. [0] means the first in the list

class Rectangle:
  def __init__(self, lowleft, upright):
    self.lowleft = lowleft
    self.upright = upright
  
  def area(self):
    return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)


# --> Rectangle then immediatly --> Point 5=x 6=y then this'll turn into 5=x=lowleft[0], 6=y=lowleft[1]
rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19))) 
print("coordinates of rectangle: ", rectangle.lowleft.x, ",", rectangle.lowleft.y, "and ", rectangle.upright.x, ',', rectangle.upright.y)

user_point = Point(float(input('Guess X: ')), float(input("Guess Y: ")))

user_area = float(input('Guess the area of the rectangle: '))
print("your area was off by: ", rectangle.area() - user_area)
print('Your point was in the rectangle: ', user_point.in_rectangle(rectangle))