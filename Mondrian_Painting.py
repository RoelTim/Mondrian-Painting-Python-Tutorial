# -*- coding: utf-8 -*-
"""
Mondrian Painting
Combining the turtle module, functions and loops
@author: roelien_timmer
"""

import turtle #module to make drawings in Python

turtle.pencolor("black") #set the colour of the pen to black
turtle.pensize(6) #set the size of the pen to 6 

def rectangle(startx,starty,hor,ver,col):
    """
    This a function with as input:
    startx = start coordinate x-axis
    starty = start coordinate y-axis    
    hor = length horizontal side rectangle
    ver = length vertical side rectangle
    col = fill colour of rectangle
    """
    
    turtle.penup() #lift the pen off the 'paper' to stop drawing
    turtle.goto(startx,starty) #move the pen to the (startx,starty) coordinates
    turtle.pendown() #put the pen back down on the 'paper' to start drawing

    turtle.fillcolor(col) #colour with which we want to fill the shapes
    
    turtle.begin_fill() #call just before drawing a shape to be filled.
    
    for i in range(2): #loop to repeat the code below twice
        turtle.forward(hor) #move the pen/turtle forward by the hor length
        turtle.left(90) #move the pen/turtle with 90 degrees to the left
        turtle.forward(ver) #move the pen/turtle forward by the ver length
        turtle.left(90) #move the pen/turtle with 90 degrees to the left
        
    turtle.end_fill() #fill the shape drawn after the last call to begin_fill()
    
    
"""
Start drawing all the rectangles
Remember that the input refers to:
    startx = start coordinate x-axis
    starty = start coordinate y-axis    
    hor = length horizontal side rectangle
    ver = length vertical side rectangle
    col = fill colour of rectangle
"""   
rectangle(-200,160,90,40,"white")
rectangle(-200,50,40,110,"white")
rectangle(-160,-50,210,210,"red")
rectangle(-110,160,160,40,"white")
rectangle(50,160,130,40,"yellow")
rectangle(50,50,130,110,"yellow")
rectangle(180,-110,20,310,"white")
rectangle(50,-50,60,100,"white")
rectangle(110,-50,70,100,"white")
rectangle(50,-110,130,60,"white")
rectangle(-50,-110,100,60,"white")
rectangle(-50,-160,100,50,"white")
rectangle(-160,-160,110,110,"black")
rectangle(-200,-110,40,160,"white")
rectangle(-200,-200,40,90,"yellow")
rectangle(-160,-200,110,40,"white")
rectangle(-50,-190,100,30,"black")
rectangle(-50,-200,230,10,"white")
rectangle(50,-190,130,80,"blue")
rectangle(180,-200,20,90,"red")
