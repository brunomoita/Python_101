'''
Created on 4 de mar de 2019

@author: bruno
'''
import turtle



def draw_square():
    square_count = 0
    
    while square_count <4:
        window = turtle.Screen()
        window.bgcolor("green")
    
        chuck = turtle.Turtle()
        chuck.shape("circle")
        chuck.color("white")
        chuck.speed(1)
        
        chuck.forward(100)
        chuck.right(90)
    
        square_count = square_count + 1        

def draw_circle():        
    window = turtle.Screen()
    window.bgcolor("green")
    
    leia = turtle.Turtle()
    leia.shape("turtle")
    leia.color("grey")
    leia.circle(100)
       
def draw_triangle():
    triangle_count = 0
    
    while triangle_count < 3:
        window = turtle.Screen()
        window.bgcolor("green")
    
        jason = turtle.Turtle()
        jason.shape("arrow")
        jason.color("black")
        jason.forward(100)
        jason.right(135)
        
        triangle_count = triangle_count + 1
        
draw_square()
draw_circle()
draw_triangle()