'''
Created on 4 de mar de 2019

@author: bruno
'''
import turtle

def draw_line(turtle_one):
    turtle_one.left(90)
    turtle_one.forward(100)

def draw_triangle(turtle_two):
    for i in range (1,4):
        turtle_two.left(120)
        turtle_two.forward(50)
        
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")
    
    ian = turtle.Turtle()
    ian.speed(3)
    ian.shape("turtle")
    ian.color("black")
    draw_line(ian)
    for i in range (1,75):
        draw_triangle(ian)
        ian.right(10)
    
    window.exitonclick()

draw_flower()