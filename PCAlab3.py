from turtle import *
import turtle
import time

ws = turtle.Screen()
ws.bgcolor("white")
ws.setup(width=530, height=530)
ws.title("Analog Clock")
ws.tracer(0)
tur = turtle.Turtle()
#tur.hideturtle()
tur.shape("turtle")
tur.speed(0)
tur.pensize(3)
def draw_clock(hour, min, second, tur):
    #drawing outer red circle
    tur.up()
    tur.goto(0, 210)
    tur.setheading(180)
    tur.color("red")
    tur.pendown()
    tur.circle(210)
    tur.up()
    tur.goto(0, 0)
    tur.setheading(90)
    
    for i in range(12):
        tur.fd(190)
        tur.pendown()
        tur.fd(20)
        #tur.stamp()
        tur.penup()
        tur.goto(0, 0)
        tur.rt(30)

    clockhands = [("red", 80, 12), ("black", 150, 60), ("blue", 110, 60)]
    timeset = (hour, min, second)

    for hand in clockhands:
        timepart = timeset[clockhands.index(hand)]
        angle = (timepart/hand[2])*360
        tur.penup()
        tur.stamp()
        tur.goto(0, 0)
        tur.color(hand[0])
        tur.setheading(90)
        tur.rt(angle)
        tur.pendown()
        tur.fd(hand[1])
    
while True:
    hour = int(time.strftime("%I"))
    min = int(time.strftime("%M"))
    second = int(time.strftime("%S"))
    draw_clock(hour, min, second, tur)
    ws.update()
    time.sleep(1)
    tur.clear()
window.mainloop()