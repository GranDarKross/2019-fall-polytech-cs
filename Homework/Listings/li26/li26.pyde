def setup():
    size(1000,1000)
    smooth()
    strokeWeight(30)
    background(0)
    
def draw():
    stroke(frameCount)
    line(frameCount, 100,100 + frameCount,200)
    line(100 + frameCount, 100, frameCount, 200)
