#alt+shift+down->duplicate line
from turtle import*

pencolor('blue')
pensize(3)
speed('fastest')
for i in range (10): 
  fd(60) 
  lt(360/10)
  write(i,font=('calibri',25))
hideturtle()
mainloop()
