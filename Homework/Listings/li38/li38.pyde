def setup():
    size(500,500)
    smooth()
    background(150)
    strokeWeight(1)
    
flug=1

def draw():
    stroke(flug,20)
    myY2=mouseY+random(-10,10)*10
    myX2=mouseX+random(10,10)*10
    line(mouseX,mouseY, myX2, myY2)
    
def keyPressed():
    if (key=='w'):
        flug=255
    if (key=='b'):
        flug=0
    if (key=='s'):
        saveFrame("myProcessing.png")