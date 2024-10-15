import turtle
screen=turtle.Screen()
screen.bgcolor("black")
screen.title("spinning star animation")
star=turtle.Turtle()
star.color("yellow")
star.speed(0)
def draw_star(size):
    for _ in range(5):
        star.forward(size)
        star.right(144)
def animate_star():
    try:
        star.clear()
        star.right(5)
        draw_star(100)
        screen.update()
        screen.ontimer(animate_star,50)
    except turtle.Terminator:
        pass
    animate_star()
    screen.mainloop()
    