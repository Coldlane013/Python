from drawingpanel import *

panel = DrawingPanel(500,300)
panel.set_background("light grey")
panel.canvas.create_rectangle(0,0,500,300,fill = "light grey")
panel.canvas.create_rectangle(5,100,105,150,fill = "black")
panel.canvas.create_rectangle(75,115,105,135,fill = "cyan")
panel.canvas.create_oval(15,140,35,160,fill="red")
panel.canvas.create_oval(75,140,95,160,fill="red")