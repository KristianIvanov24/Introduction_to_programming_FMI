from graphics import *

# Създаване на прозорец
win = GraphWin("Chicken", 600, 400)

# Рисува тялото
body = Oval(Point(200, 200), Point(400, 300))
body.setFill("yellow")
body.draw(win)

# Рисува главата
head = Circle(Point(170, 200), 50)
head.setFill("yellow")
head.draw(win)

# Рисува човката
beak = Polygon(Point(100, 200), Point(120, 190), Point(120, 210))
beak.setFill("orange")
beak.draw(win)

# Рисува окото
eye = Circle(Point(170, 190), 10)
eye.setFill("black")
eye.draw(win)

# Рисува крилцето
wing = Polygon(Point(250, 220), Point(350, 220), Point(350, 290), Point(250, 250))
wing.setFill("yellow")
wing.draw(win)

# Рисува опашката
tail = Polygon(Point(400, 250), Point(450, 230), Point(430, 200))
tail.setFill("yellow")
tail.draw(win)

# Рисува краката
leg1 = Line(Point(260, 295), Point(240, 350))
leg1.setWidth(5)
leg1.draw(win)


leg2 = Line(Point(300, 300), Point(280, 355))
leg2.setWidth(5)
leg2.draw(win)

# Затваря прозореца с клик на мишката
win.getMouse()
win.close()
