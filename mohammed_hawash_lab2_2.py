import turtle

def test_drive():
    turtle.fd(100)
    turtle.left(87)
    turtle.setheading(90)
    turtle.up()
    turtle.goto(50,50)
    turtle.down()
    turtle.home()
    turtle.circle(25)
    
def test_state():
    print(turtle.isdown())
    print(turtle.heading())
    print(turtle.xcor(),turtle.ycor())
    
def main():
    test_state()
    test_drive()
    input("enter any thing")
    test_state()
main()