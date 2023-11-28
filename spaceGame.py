# Fill me in!
###Create Background
app.background = "black"

Label("Score: ", 360, 370, fill='white', size = 15)
Label("Lives: ", 360, 385, fill='white', size = 15)
score = Label(0, 388, 370, fill='white', size = 15)
lives = Label(3, 388, 385, fill='white', size = 15)

##Create the Stars
def drawStar (x, y):
    Star(x, y, 2, 7, fill="silver")

for r in range(300):
    u = 400
    v = 10
    x = random()*(u - v)
    y = random()*(u - v)
    
    drawStar(x, y)



###Create the star


cStar = Star(randrange(30, 350), randrange(30, 350), 20, 5, fill = "goldenrod")
aStar = Star(randrange(30, 350), randrange(30, 350), 20, 5, fill = "mediumVioletRed")

cNumber = randrange(1, 10)
aNumber = randrange(1, 10)

###Create the Rocket
rocket1 = Circle(200, 200, 23, fill="purple")
rocket2 = Oval(200, 200 + 18, 60, 30, fill = "purple")
rocket3 = Circle(200, 200 - 3, 13, fill = "lightSkyBlue", border = "grey")


def onMouseMove(mouseX, mouseY): 
    rocket1.centerX = mouseX
    rocket1.centerY = mouseY
    
    rocket2.centerX = mouseX
    rocket2.centerY = mouseY + 18
    
    rocket3.centerX = mouseX
    rocket3.centerY = mouseY - 3

def onMousePress(cStarcenterX, cStarcenterY):
    if (cNumber < 5) :
        score.value -= 1
        lives.value -= 1
        cStar.centerX = randrange(30, 350)
        cStar.centerY = randrange(30, 350)
    else:
        score.value += 1
        cStar.centerX = randrange(30, 350)
        cStar.centerY = randrange(30, 350)
    
def onKeyPress(a):
    if (aNumber >= 7) :
        score.value -= 1
        lives.value -= 1
        aStar.centerX = randrange(30, 350)
        aStar.centerY = randrange(30, 350)
    else:
        score.value += 1
        aStar.centerX = randrange(30, 350)
        aStar.centerY = randrange(30, 350)
        
        
cNumber = randrange(1, 10)
aNumber = randrange(1, 10)        
        
        
        
        
        
        
        
        
        
