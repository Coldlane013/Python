from drawingpanel import *
panel = DrawingPanel(300,200)
panel.set_background("light grey")
def car(x,y):
       
    panel.canvas.create_rectangle(5+x,100+y,105+x,150+y,fill = "black")
    panel.canvas.create_rectangle(75+x,115+y,105+x,135+y,fill = "cyan")
    panel.canvas.create_oval(15+x,140+y,35+x,160+y,fill="red")
    panel.canvas.create_oval(75+x,140+y,95+x,160+y,fill="red")

car(0,5)
car(40,-70)
