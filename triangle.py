from turtle import *

speed(0)
color('red')
bgcolor('black')
b = 200

while b > 0:
    left(120)  # Change the angle to create a better spiral --- try 470
    forward(b)
    b -= 1

mainloop()
