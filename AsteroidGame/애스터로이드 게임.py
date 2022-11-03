import turtle, random

def makePlayer():       #우주선 생성
    player = turtle.Turtle()
    player.color("blue")
    player.shape("turtle")
    player.up()
    player.speed(0)
    return player

def makeAsteroid():     #소행성 생성
    ast = turtle.Turtle()
    ast.color(random.random(), random.random(), random.random())
    ast.moveSpeed = random.randrange(2,6)
    ast.left(random.randrange(0, 90))
    ast.shape("circle")
    ast.up()
    ast.speed(0)
    return ast

def collide(p, a):      #우주선p와 소행성a의 충돌 검사
    dx = a.xcor() - p.xcor()
    dy = a.ycor() - p.ycor()
    if dx < 0: dx = -dx
    if dy < 0: dy = -dy
    if dx < 10 and dy < 10:
        return True
    return False
    

def run():              #타이머 이벤트 콜백 함수
    player.fd(5)
    for z in a:
        z.fd(z.moveSpeed)
        if z.xcor() > screen.window_width()/2:
            z.setx(-screen.window_width()/2)
        if z.ycor() > screen.window_height()/2:
            z.sety(-screen.window_height()/2)
        if collide(player, z):
            z.hideturtle()
            a.remove(z)
    if a== []:
        return
    screen.ontimer(run, 10)

def turnleft():         #키보드 콜백함수
    player.left(30)

def turnright():       #키보드 콜백함수
    player.right(30)

def runStopwatch():
    global elapsedTime
    stopwatch.clear()
    stopwatch.home()
    stopwatch.write(str(elapsedTime), align="center")
    if a == []:
        stopwatch.clear()
        stopwatch.home()
        stopwatch.write("You win the game in" + str(elapsedTime) + "seconds.", align="center")
        return
    elapsedTime += 1
    screen.ontimer(runStopwatch, 1000)

#main program
turtle.setup(500, 400, 0, 0)
screen = turtle.Screen()
stopwatch = turtle.Turtle()
stopwatch.hideturtle()
stopwatch.up()
elapsedTime = 0


player = makePlayer()   #거북이 우주선
a = []                  #소행성 리스트

n = 5                   #소행성 개수
for i in range(n):
    a.append(makeAsteroid())   #소행성 추가
    a[i].goto(random.randrange(-230, 230), random.randrange(-180, 190))

screen.ontimer(run, 10)
runStopwatch()

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.listen()


turtle.exitonclick()
