'''
Created on 4 de mar de 2019

@author: bruno
'''
import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")
    
    chuck = turtle.Turtle()
    chuck.shape("circle")
    chuck.color("white")
    chuck.speed(1)
    
    square = 0
    
    while square < 4:    
        chuck.forward(100)
        chuck.right(90)
        square = square + 1
                
def draw_circle():        
    window = turtle.Screen()
    window.bgcolor("green")
    
    leia = turtle.Turtle()
    leia.shape("turtle")
    leia.color("grey")
    leia.circle(100)
       
def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("green")
    
    jason = turtle.Turtle()
    jason.shape("arrow")
    jason.color("black")
    
    triangle = 0
    
    while triangle < 3:
        jason.forward(100)
        jason.right(120)
        triangle = triangle + 1
    window.exitonclick()
    
draw_square()     
draw_circle()
draw_triangle()
