import pgzrun, random
WIDTH, HEIGHT = 600, 700
TITLE = "Catch LeBron & Kobe"
lebron = Actor("lebron.jpg")
kobe = Actor("kobe.png")

lebron.pos = random.randint(50, 550), random.randint(50, 670)
kobe.pos = random.randint(50, 550), random.randint(50, 670)
message = "Catch LeBron or Kobe!"

def draw():
    screen.fill("orange")
    lebron.draw()
    kobe.draw()
    screen.draw.text(message, (20, 20), color="black", fontsize=36)

def on_mouse_down(pos):
    global message
    if lebron.collidepoint(pos):
        message = "Nice! You caught LeBron! 🏆"
    elif kobe.collidepoint(pos):
        message = "Mamba Mentality! You caught Kobe! 🐍" 
    else:
        message = "You missed! Stay sharp!"

    lebron.pos = random.randint(50, 550), random.randint(50, 670)
    kobe.pos = random.randint(50, 550), random.randint(50, 670)

pgzrun.go()

