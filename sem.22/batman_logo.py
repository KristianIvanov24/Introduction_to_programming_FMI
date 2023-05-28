from graphics import *

win = GraphWin("Batman Logo", 600, 400)
win.setBackground("yellow")

body = Oval(Point(100, 100), Point(500, 300))
body.setFill("black")
body.draw(win)

head = Oval(Point(285, 70), Point(315, 120))
head.setFill("yellow")
head.setOutline("yellow")
head.draw(win)

earL = Circle(Point(220, 100), 65)
earL.setFill("yellow")
earL.setOutline("yellow")
earL.draw(win)

earR = Circle(Point(380, 100), 65)
earR.setFill("yellow")
earR.setOutline("yellow")
earR.draw(win)

wingL = Circle(Point(200, 290), 30)
wingL.setFill("yellow")
wingL.setOutline("yellow")
wingL.draw(win)

wingR = Circle(Point(400, 290), 30)
wingR.setFill("yellow")
wingR.setOutline("yellow")
wingR.draw(win)

tailL = Circle(Point(260, 300), 40)
tailL.setFill("yellow")
tailL.setOutline("yellow")
tailL.draw(win)

tailR = Circle(Point(340, 300), 40)
tailR.setFill("yellow")
tailR.setOutline("yellow")
tailR.draw(win)

win.getMouse()
win.close()
