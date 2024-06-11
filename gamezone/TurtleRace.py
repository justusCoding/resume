import turtle
import random

def setup_turtle(color, y):
    t = turtle.Turtle()
    t.color(color)
    t.shape("turtle")
    t.penup()
    t.goto(-200, y)
    t.pendown()
    return t

def turtle_race():
    screen = turtle.Screen()
    screen.setup(width=500, height=400)
    screen.title("Turtle Race")

    colors = ['red', 'blue', 'green', 'yellow']
    y_positions = [-100, -50, 0, 50]
    turtles = []

    for color, y in zip(colors, y_positions):
        t = setup_turtle(color, y)
        turtles.append(t)

    race_on = True
    while race_on:
        for t in turtles:
            t.forward(random.randint(1, 10))
            if t.xcor() > 200:
                race_on = False
                winner = t.pencolor()
                print(f"The winner is the {winner} turtle!")
                break

    screen.mainloop()

if __name__ == "__main__":
    turtle_race()