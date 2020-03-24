import random, math, turtle

pi = 3.14
wn = turtle.Screen()
wn.title('Simulated Annealing :)')

t = turtle.Turtle()
t.speed(5)
t.hideturtle()

def cartesian():
    t.pencolor("black")
    t.width(3)
    t.penup()
    t.setposition(-350,0)
    t.pendown()
    t.forward(700)
    t.penup()
    t.setposition(-355,-20)
    t.pendown()
    x = -10
    while (t.xcor() <= 350):
        if (x != 0):
            t.write(x)
        t.penup()
        t.forward(35)
        t.pendown()
        x += 1
    t.penup()
    t.setposition(0, -300)
    t.pendown()
    t.left(90)
    t.forward(600)
    t.penup()
    t.setposition(10,-305)
    t.pendown()
    x = -10
    while (t.ycor() <= 300):
        if (x != 0):
            t.write(x)
        t.penup()
        t.forward(30)
        t.pendown()
        x += 1

def marker(x1b, x2b, score):
    t.color("red")
    x1cor = x1b * 35
    x2cor = x2b * 30
    t.penup()
    t.setposition(x1cor, x2cor)
    t.pendown()
    t.circle(1)
    t.penup()
    t.setposition(x1cor-55, x2cor+10)
    t.write(score)

def marker2(x1b, x2b, score):
    t.color("green")
    x1cor = x1b * 35
    x2cor = x2b * 30
    t.penup()
    t.setposition(x1cor, x2cor)
    t.pendown()
    t.circle(1)
    t.penup()
    t.setposition(x1cor-55, x2cor+10)
    t.write(score)

def screenboard(x1b, x2b, best):
    t.penup()
    t.setposition(-150, -250)
    t.pendown()
    t.color("white")
    t.pencolor("black")
    t.width(1)
    t.begin_fill()
    i = 1
    t.setheading(0)
    while (i <= 2):
        t.forward(300)
        t.left(90)
        t.forward(100)
        t.left(90)
        i += 1
    t.end_fill()
    t.penup()
    t.setposition(-110, -190)
    t.pendown()
    t.color("black")
    text = "Hasil Optimum = " + str(best)
    t.write(text, font=("Arial",10,"normal"))
    text = "x1 = " + str(x1b)
    t.penup()
    t.setposition(-65, -210)
    t.pendown()
    t.write(text, font=("Arial", 10, "normal"))
    text = "x2 = " + str(x2b)
    t.penup()
    t.setposition(-65, -230)
    t.pendown()
    t.write(text, font=("Arial", 10, "normal"))

def randomNumber():
    return random.uniform(-10, 10)

def evaluated (x1, x2):
    ev = -math.fabs(math.sin(x1)*(math.cos(x2)*(math.exp(math.fabs(1-(math.sqrt(math.pow(x1,2)+math.pow(x2,2))/pi))))))
    return ev

def main():
    Tawal = 250
    alpha = 0.95
    Takhir = 1
    x1 = randomNumber()
    x2 = randomNumber()
    x1b = x1
    x2b = x2
    best = evaluated (x1,x2)
    cartesian()
    wn.tracer(0, 1000)
    marker(x1b, x2b, best)
    total = 0
    while (Tawal > Takhir):
        L = 25
        while (L != 0):
            x1n = x1b + randomNumber()
            x2n = x2b + randomNumber()
            if ((10 > x1n > -10) and (10 > x2n > -10)):
                new = evaluated (x1n, x2n)
                if (new < best):
                    best = new
                    x1b = x1n
                    x2b = x2n
                    marker(x1b, x2b, best)
                    total += 1
                elif(math.exp( - ( new - best ) / Tawal ) > random.random()):
                    x1b = x1n
                    x2b = x2n
                    best = new
                    marker2(x1b, x2b, best)
                    total += 1
            L -= 1
        Tawal *= alpha
        if(total >= 200):
            t.reset()
            cartesian()
            total = 0
        print(best)
    screenboard(x1b, x2b, best)
    printb = 'Nilai x1 :'
    printc = 'Nilai x2 :'
    printd = 'Nilai optimum :'
    print (printb, x1b)
    print (printc, x2b)
    print(printd, best)
    print(evaluated(8.0502, 9.66459))

main()
wn.exitonclick()