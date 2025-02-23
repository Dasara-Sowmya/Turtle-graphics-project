import turtle  

# Set up the screen  
turtle.bgcolor("black")  
turtle.speed(0)  # Fastest speed  
turtle.pensize(1)  
turtle.tracer(0, 0)  # Turn off automatic updates for smooth drawing  

# Define Colors  
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]  

# Create pattern  
t = turtle.Turtle()  
t.speed(0)  

for i in range(360):  # Increase the range for more spirals  
    t.pencolor(colors[i % len(colors)])  
    t.forward(i * 2)  # Increase the distance for a larger pattern  
    t.right(91)  # Slightly more than 90° to create the spiral effect  

    if i % 10 == 0:  
        turtle.update()  # Update screen every 10 iterations to prevent freezing  

turtle.done()  # Finish drawing