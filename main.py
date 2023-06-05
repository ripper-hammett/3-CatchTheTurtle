import turtle
import time

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Catch the Turtle")

turtle.hideturtle()
turtle.penup()
turtle.goto(0, 350)
turtle.color("black")
style = ("ariel", 20, "normal")
turtle.write("Score", font=style, align="center", move=True)
turtle.goto(0, 300)
turtle.color("black")
style = ("ariel", 20, "normal")
turtle.write("Time", font=style, align="center", move=True)



turtle.mainloop()
