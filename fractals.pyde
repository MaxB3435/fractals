def setup():
    size(1000,800)
  sida.208  
def draw():
    background(255)
    translate(500,700)
    level = int(map(mouseX,0,width,0,15))
    y(150,level)
    
    
def y(sz,level):
    if level > 0:
        line(0,0,0,-sz)
        translate(0,-sz)
        rotate(radians(30))
        y(0.8*sz,level-1)
        rotate(radians(-60))
        y(0.8*sz,level-1)
        rotate(radians(30))
        translate(0,sz)
        
    
