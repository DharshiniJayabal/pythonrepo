import turtle
screen=turtle.Screen()
screen.bgcolor("white")
screen.title("expanding and contracting circle animation")
circle=turtle.Turtle()
circle.color("blue")
circle.speed(1)
circle.penup()
radius=50
expanding=True
def animate_circle():
    global radius,expanding
    circle.clear()
    circle.goto(0,-radius)
    circle.pendown()
    circle.circle(radius)
    circle.penup()
if expanding:
    radius+=2
    if radius>100:
        expanding=False
    else:
        radius-=2
        if radius<50:
            expanding=True
        screen.update()
        screen.ontimer(animate_circle,50)
        screen.tracer(0)
        animate_circle()
        screen.mainloop()
        