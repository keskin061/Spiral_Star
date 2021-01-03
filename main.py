import turtle

n = 60 # number of sizes

pen = turtle.Turtle()

for i in range(n):
    pen.forward(i * 10)
    pen.right(144) # degree
turtle.done()
