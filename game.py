from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BALL_COLOR = "#FF0000"
BG_COLOR = "#000000"
PERSON_COLORS = ["#00FF00", "#FFFF00", "#FF00FF", "#00FFFF", "#FFA500", "#FFFFFF"]

class Person:
    def __init__(self):
        self.x = GAME_WIDTH / 2
        self.y = GAME_HEIGHT / 2
        self.color = random.choice(PERSON_COLORS)
        self.square = canvas.create_rectangle(self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE, fill=self.color, tag="person")

    def move(self):
        if direction == "up":
            self.y -= SPACE_SIZE
        elif direction == "down":
            self.y += SPACE_SIZE
        elif direction == "left":
            self.x -= SPACE_SIZE
        elif direction == "right":
            self.x += SPACE_SIZE

        canvas.coords(self.square, self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE)

    def changeColor(self):
        # this function will be called when the square touches the ball
        newColor = random.choice(PERSON_COLORS)
        self.color = newColor
        canvas.itemconfig(self.square, fill=newColor)

class Ball:
    def __init__(self):
        # the ball is going to spawn on a random place in the screen
        self.x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        self.y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        self.square = canvas.create_oval(self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE, fill=BALL_COLOR, tag="ball")

    def randomPosition(self):
        self.x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        self.y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        canvas.coords(self.square, self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE)


def nextTurn(person, ball):
    person.move()

    #this is when the square and ball make contact. The squares color will change and the ball will be moved
    if person.x == ball.x and person.y == ball.y:
        person.changeColor()
        ball.randomPosition()

    #if the square goes out of bounds its game over
    if person.x < 0 or person.x >= GAME_WIDTH or person.y < 0 or person.y >= GAME_HEIGHT:
        gameOver()
    else:
        window.after(SPEED, nextTurn, person, ball)

def changeDirection(newDir):
    global direction
    opposites = {"left": "right", "right": "left", "up": "down", "down": "up"}
    if newDir != opposites.get(direction):
        direction = newDir

def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text = "GAME OVER", fill="red", tag="gameover")


window = Tk()
window.title("Color Changing Character Game")
window.resizable(False, False)

direction = 'down'

label = Label(window, text="Touch the circle!", font=('consolas', 30))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (GAME_WIDTH / 2))
y = int((screen_height / 2) - (GAME_HEIGHT / 2))
window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}+{x}+{y}")

window.bind('<Left>', lambda event: changeDirection('left'))
window.bind('<Right>', lambda event: changeDirection('right'))
window.bind('<Up>', lambda event: changeDirection('up'))
window.bind('<Down>', lambda event: changeDirection('down'))

person = Person()
ball = Ball()
nextTurn(person, ball)

window.mainloop()





