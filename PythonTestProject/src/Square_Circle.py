'''
Created on 4 de mar de 2019

@author: bruno
'''
import turtle

def draw_square(some_turtle):
    square = 0
    for i in range (1,5):   
        some_turtle.forward(100)
        some_turtle.right(90)
        square = square + 1

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")    
    chuck = turtle.Turtle()
    chuck.shape("circle")
    chuck.color("white")
    chuck.speed(5)    
    chuck.right(10)
    for i in range (1,36):
        draw_square(chuck)
        chuck.right(10)
    window.exitonclick()

draw_art()