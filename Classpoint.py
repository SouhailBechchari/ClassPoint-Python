class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def set_x(self, value):
        self.x = value

    def get_y(self):
        return self.y
    
    def set_y(self, value):
        self.y = value

    def distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    def norm(self):
        return ((self.x) ** 2 + (self.y) ** 2) ** 0.5

point1 = Point(4, 3)

print("Distance:", point1.distance(Point(0, 0)))
