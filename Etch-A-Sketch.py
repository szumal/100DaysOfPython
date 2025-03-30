from turtle import Turtle, Screen

crush = Turtle()
screen = Screen()

def move_forward():
    crush.forward(10)

def move_backward():
    crush.backward(10)

def rotate_counter_clockwise():
    crush.left(10)

def rotate_clockwise():
    crush.right(10)

def clear_and_center():
    crush.reset()
    crush.clear()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=rotate_counter_clockwise, key="a")
screen.onkey(fun=rotate_clockwise, key="d")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=clear_and_center, key="c")
screen.exitonclick()
