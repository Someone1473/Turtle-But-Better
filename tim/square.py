from turtle import *

def square(length, x, y):
    nx = x - length/2
    ny = y - length/2
    teleport(nx, ny)
    for i in range(4):
        forward(length)
        right(90)

    left(90)
    teleport(x, y)

def main():

    square()
    done()

if __name__ == "__main__":
    main()
