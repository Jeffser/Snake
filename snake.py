from tkinter import *
from random import randint
size=[20, 20, 30]
pixel=[]
snake=[[5, 1]]
apple=[2, 2]
direction=[1, 0]
score=0
best=0
cBackg="LightBlue3"
cBordr="Gray20"
cSnake="Forest Green"
cApple="Brown1"
win = Tk()
win.title("Snake")
cvGame = Canvas(win, bg=cBackg)
cvGame.grid(row=0, column=0, columnspan=3)
for i in range(0, size[0]):
    pixel.append([])
    for a in range(0, size[1]):
        pixel[i].append(Canvas(cvGame, bg=cBackg, width=size[2], height=size[2], highlightthickness=0))
        if i == 0 or i == size[0]-1 or a == 0 or a == size[1]-1:
            pixel[i][a].config(bg=cBordr)
        pixel[i][a].grid(row=i, column=a) 
pixel[apple[1]][apple[0]].config(bg=cApple)
lblScore = Label(win, font="Arial, 14", text="Score: " + str(score))
lblScore.grid(row=1, column=0)
lblBest = Label(win, font="Arial, 14", text="Best: " + str(best))
lblBest.grid(row=1, column=1)
lblCred = Label(win, font="Arial, 14", text="Created by: Jeffry E.R").grid(row=1, column=2)
def act():
    global direction, score, best
    getApple = False
    pixel[snake[0][1]][snake[0][0]].config(bg=cBackg)
    prev = [snake[0][0], snake[0][1]]
    snake[0][0] = snake[0][0] + direction[0]
    snake[0][1] = snake[0][1] + direction[1]
    if pixel[snake[0][1]][snake[0][0]]["background"] != cBordr and pixel[snake[0][1]][snake[0][0]]["background"] != cSnake:
        if pixel[snake[0][1]][snake[0][0]]["background"] == cApple: getApple = True
        pixel[snake[0][1]][snake[0][0]].config(bg=cSnake)
    else:
        for i in range(1, len(snake)): pixel[snake[i][1]][snake[i][0]].config(bg=cBackg)
        snake.clear()
        snake.append([5, 1])
        apple = [2, 2]
        direction = [1, 0]
        if score > best: best=score; lblBest.config(text="Best: " + str(best))
        score = 0
        lblScore.config(text="Score: " + str(score))
    win.update()
    for i in range(1, len(snake)):  
        if i == len(snake)-1: pixel[snake[i][1]][snake[i][0]].config(bg=cBackg)
        prev2 = [snake[i][0], snake[i][1]]
        snake[i] = prev
        pixel[snake[i][1]][snake[i][0]].config(bg=cSnake)
        prev = [prev2[0], prev2[1]]
        win.update()
    if getApple: 
        score += 1
        lblScore.config(text="Score: " + str(score))
        while True:
            apple = [randint(0, size[0]-1), randint(0, size[1])-1]
            if pixel[apple[1]][apple[0]]["background"] != cBordr and pixel[apple[1]][apple[0]]["background"] != cSnake and apple != prev:
                pixel[apple[1]][apple[0]].config(bg=cApple)
                break
        snake.append([prev[0], prev[1]])
    def kUp(event): global direction; direction = [0, -1]
    def kDw(event): global direction; direction = [0, 1]
    def kRg(event): global direction; direction = [1, 0]
    def kLf(event): global direction; direction = [-1, 0]
    win.bind("<Up>", kUp)
    win.bind("<Down>", kDw)
    win.bind("<Right>", kRg)
    win.bind("<Left>", kLf)
    win.after(100, act)
win.after(100, act)
win.mainloop()