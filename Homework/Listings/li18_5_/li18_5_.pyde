def setup():
    size(700,700)
    smooth()
    background(255)
    strokeWeight(30)
    noLoop()
    
def draw():
    stroke(20,100)
    i=1
    while i<8:
        i=i+2
        line(i*50,200,150+(i-1)*50,300)
        line(i*50+100,200,50+(i-1)*50,300)
