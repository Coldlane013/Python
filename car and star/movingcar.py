from drawingpanel import *

def cmove(circles):
    panel = DrawingPanel(300,200)
    panel.set_background("light grey")
    for a in range(10,circles,10):
     panel.canvas.create_rectangle(0,0,500,300,fill = "light grey")	
     panel.canvas.create_rectangle(5+a,100,105+a,150,fill = "black")
     panel.canvas.create_rectangle(75+a,115,105+a,135,fill = "cyan")
     panel.canvas.create_oval(15+a,140,35+a,160,fill="red")
     panel.canvas.create_oval(75+a,140,95+a,160,fill="red")
     panel.sleep(600)

cmove(200)