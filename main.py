import turtle
import random

ekran = turtle.Screen()
ekran.title("Catch The Turtle")
ekran.bgcolor("#B0E0E6")
YAZI = ('Arial',25,'normal')
skor=0
game_over = False

#score turtle
turtle_score = turtle.Turtle()

#turtle list
turtle_list = []

#geri sayim
geriSayim = turtle.Turtle()

grid_size = 10

x_koordinatlari = [-20,-10,0,10,20]
y_koordinatlari = [20,10,0,-10]
def setup_turtle_score():
    turtle_score.color("dark blue")
    turtle_score.hideturtle()
    turtle_score.penup()

    yukseklik=ekran.window_height() / 2
    y = yukseklik * 0.85
    turtle_score.setposition(0,y)
    turtle_score.write(arg="Score: {}".format(skor),move=False,align="center", font=YAZI)
def turtle_make(x,y):
    turtleMake=turtle.Turtle()
    def turtle_click(x,y):
        global skor
        skor+=1
        turtle_score.clear()
        turtle_score.write(arg="Score: {}".format(skor), move=False, align="center", font=YAZI)

    turtleMake.onclick(turtle_click)
    turtleMake.penup()
    turtleMake.shape("turtle")
    turtleMake.shapesize(2,2)
    turtleMake.color("#008000")
    turtleMake.goto(x * grid_size,y*grid_size)
    turtle_list.append(turtleMake)
def turtles_setup():
    for x in x_koordinatlari:
        for y in y_koordinatlari:
            turtle_make(x,y)
def turtle_hide():
    for t in turtle_list:
        t.hideturtle()
def random_turtle():
    if not game_over:
        turtle_hide()
        random.choice(turtle_list).showturtle()
        ekran.ontimer(random_turtle,500)
def geri_sayim(time):
    global game_over
    geriSayim.penup()
    geriSayim.hideturtle()
    yukseklik = ekran.window_height() / 2
    y = yukseklik * 0.85
    geriSayim.setposition(0, y - 40)
    geriSayim.write(arg="Time: {}".format(time), move=False, align="center", font=YAZI)
    geriSayim.clear()

    if time > 0:
        geriSayim.clear()
        geriSayim.write(arg="Time: {}".format(time), move=False, align="center", font=YAZI)
        ekran.ontimer(lambda: geri_sayim(time - 1),1000)

    else:
        game_over = True
        turtle_hide()
        geriSayim.clear()
        geriSayim.write(arg="Game Over!", move=False, align="center", font=YAZI)
def oyunu_baslat():
    turtle.tracer(0)
    setup_turtle_score()
    turtles_setup()
    turtle_hide()
    random_turtle()
    geri_sayim(20)
    turtle.tracer(1)

oyunu_baslat()
turtle.mainloop()
