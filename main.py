import PyGUIgame.PyGUIgame as pgg

win = pgg.init(512,256,"testwindow")

run = True
while run:
	win.update()
	win.background(pgg.BLACK)
	if win.isKeyDown("Escape"):
		run = False