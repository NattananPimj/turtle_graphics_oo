import turtle
import random


def get_new_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class Polygon:
    def __init__(self, num_sides: int = 3, size: float = 1, orientation: float = 0, location_x=0, location_y=0,
                 color: tuple[int, int, int] = (0, 0, 0), border_size: int = 1):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.x = location_x
        self.y = location_y
        self.color = color
        self.border_size = border_size
        self.num = 1
        self.reduction_ratio = .618

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def draw_smaller(self):
        for _ in range(2):
            self.size *= self.reduction_ratio
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.right(90)
            self.x = turtle.pos()[0]
            self.y = turtle.pos()[1]
            self.draw_polygon()

    def setup(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)


class Run(Polygon):
    def run_choice(self):
        choice = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive:'))
        if choice == 1:
            self.run(3)
            turtle.done()
        elif choice == 2:
            self.run(3)
            turtle.done()
        elif choice == 3:
            self.run(5)
            turtle.done()
        elif choice == 4:
            self.run(3, (3, 12))
            self.run(4, (3, 12))
            self.run(5, (3, 12))
            turtle.done()
        elif choice == 5:
            self.run(3, t=1)
            turtle.done()
        elif choice == 6:
            self.run(4, t=1)
            turtle.done()
        elif choice == 7:
            self.run(5, t=1)
            turtle.done()
        elif choice == 8:
            self.run(3, (3, 12), t=1)
            self.run(4, (3, 12), t=1)
            self.run(5, (3, 12), t=1)
            turtle.done()
        elif choice == 9:
            self.run(3, (1, 10))
            self.run(4, (1, 10))
            self.run(5, (1, 10))
            self.run(3, (1, 10), t=1)
            self.run(4, (1, 10), t=1)
            self.run(5, (1, 10), t=1)
            turtle.done()

    def random_input(self):
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.x = random.randint(-300, 300)
        self.y = random.randint(-200, 200)
        self.color = get_new_color()
        self.border_size = random.randint(1, 10)

    def run(self, sides: int, num_range=(20, 40), t: int = 0):
        self.num_sides = sides
        self.num = random.randint(num_range[0], num_range[1])
        self.setup()
        for _ in range(self.num):
            self.random_input()
            self.draw_polygon()
            if t == 1:
                self.draw_smaller()


art = Run()
art.run_choice()
