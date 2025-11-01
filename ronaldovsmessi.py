import pgzrun,random
WIDTH,HEIGHT = 600,540
TITLE="WHO WILL CEMENT THIERSELVES IN GREATNESS"
ronaldo = Actor("ronaldo.jpg")
ronaldo.pos = random.randint(50,550),random.randint(50,490)
messi = Actor("messi.jpg")
messi.pos = random.randint(50,550),random.randint(50,490)
def draw():
    screen.fill("blue")
    ronaldo.draw()
    messi.draw()


def update():
    if keyboard.left:
        ronaldo.x-=10
    if keyboard.right:
        ronaldo.x+=10

def on_key_down(key):
    print(key)  
    if key.up  
pgzrun.go()