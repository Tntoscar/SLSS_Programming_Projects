import turtle

def main():
    # create a turtle object
    sasuke = turtle.Turtle()
    sasuke.speed(0)

    screen = turtle.Screen()
    screen.colormode(255)

    sasuke.color((140, 50, 50))

    # Ask the turtle to move around the canvas
    for i in range(1000000):
        #sasuke.forward(50)
        #sasuke.right(90)
        #sasuke.back(90)
        #sasuke.left(50)
        sasuke.right(100 + i)
        sasuke.left(100)
        #sasuke.backward(100)
        #sasuke.forward(100)
        #for i in range(1000):
            #sasuke.forward(50 + i)
            #asuke.right(93)
            #sasuke.color((
               # (150 + i) % 255,
                #(50 + i) % 255,
                #(50 + i) % 255,
           # ))
    turtle.exitonclick()

if __name__ == "__main__":
    main()

