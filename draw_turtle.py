import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("orange")
    anki=turtle.Turtle()
    anki.shape("turtle")
    anki.speed(10)
    
    for count in range(1,37):
        for i in range(4):
            
            anki.forward(100)
            anki.right(90)
        anki.right(10)
        
    window.exitonclick()

draw_square()
        
