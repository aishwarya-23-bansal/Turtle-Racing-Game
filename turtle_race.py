from turtle import Turtle,Screen,tracer,update
import random
import time

is_race_on=False
my_screen=Screen()
my_screen.setup(width=500,height=400)
my_screen.colormode(255)
t = Turtle(shape="turtle")
tracer(0)
def lanes():
    d=0
    for i in range(0,7):
        timmy=Turtle()
        timmy.hideturtle()
        timmy.speed("fastest")
        timmy.penup()
        timmy.goto(x=-250,y=-120+d)
        d+=50
        timmy.pendown()
        timmy.forward(450)
def finish_line(x):
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.color("red")
    
    y =180
    t.goto(x, y)
    t.begin_fill()
    t.forward(10)
    t.right(90)
    t.forward(301)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(301)
    t.right(90)
    t.end_fill()
def show_countdown():
    countdown =Turtle()
    countdown.hideturtle()
    countdown.penup()
    countdown.goto(0, 0)
    countdown.color("red")
    countdown.write("3", align="center", font=("Arial", 48, "bold"))
    time.sleep(1)
    countdown.clear()

    countdown.write("2", align="center", font=("Arial", 48, "bold"))
    time.sleep(1)
    countdown.clear()

    countdown.write("1", align="center", font=("Arial", 48, "bold"))
    time.sleep(1)
    countdown.clear()

    countdown.color("green")
    countdown.write("GO!", align="center", font=("Arial", 48, "bold"))
    time.sleep(1)
    countdown.clear()
def turtle_list():
    global turtles
    colors=["red","orange","yellow","green","blue","purple"]

    turtles=[]
    i=0
    for color in colors:
        new_turtle=Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=-230,y=-95+i)
        turtles.append(new_turtle)
        i+=50
def winner():
    t=Turtle(shape='turtle')
    t.color(winning_color)
    t.shapesize(3,3)
    winner =Turtle()
    winner.hideturtle()
    winner.penup()
    winner.goto(20, 30)
    winner.color(winning_color)
    winner.write("Winner!", align="center", font=("Arial", 48, "bold"))
    for _ in range(99):
        t.right(10)
        time.sleep(0.01)


lanes()
finish_line(200)
turtle_list()
update()
tracer(1)

user_input=my_screen.textinput(title="Make your bet",prompt="Which Turtle will win the race?Enter a color:")
if user_input:
    is_race_on=True

show_countdown()

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>200:
            winning_color=turtle.pencolor()
            if winning_color==user_input.lower():
                print(f"You won! The {winning_color} turlte is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")
            is_race_on=False
            break
        distance=random.randint(0,10)
        turtle.forward(distance)
my_screen.clear() 
winner()
my_screen.exitonclick()