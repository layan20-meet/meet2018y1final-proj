import turtle
import time
import random
import sys



#lists

ques_list = ["when was the first earth day?\n A.1982\n B.1970\n C.2003\n D.1999","what have roots as no body sees, is taller than trees, up up it goes and it never grows?","How much of our air pollution comes from motor vehicles, like cars and tracks?\n A.50%\n B.20%\n C.80%\n D.30%","Alive withot breath, as cold as death,never thirsty ,ever drinking,and it never blinking?","The melting of the Greenland ice sheet poses in immediate threat to reach animal?\n A.Penguins\n B.Killer Whales\n C.Polar Bears\n D.Muskoxen","which of the following help reduse air pollution?\n A.Using cruise control\n B.Using fluorecent lights\n C.Using water-based product\n D.all of the above","the population of the world is currently increasing at a rate of 8600 people per ________? \n A.month\n B.week \n C.day \n D.hour","The estimated world population in the year 2050 is about? \n A.3.4 billion \n B.6.8 billion \n C.9.3 billion \n D.11.5 billion","It cannot be seen, it cannot be felt, cannot be heard , cannot be smelt , it lies behind stars and under hills , and empty halls it fills , it comes first and follows after, ends life , kills laughter?"]
ans_list = ["b","mountain","a","fish","c","d","d","c","dark"]




#functions







turtle.tracer(0,1) #speed
x="Guess The Picture"  #headline
y="GAME OVER"
title=turtle.clone()
title.penup()
title.goto(0,300)
title.pendown()
title.hideturtle()
title.color("purple")
title.write(x, move=False, align="center", font=("Comic Sans Ms", 60, "normal"))


turtle.register_shape("teletubbies.gif") #picture
tele=turtle.clone()
tele.shape("teletubbies.gif")
tele.stamp()
tele.hideturtle()




#covering the 9 parts
#first row
spliting1=turtle.clone()
spliting1.shape("circle")
spliting1.penup()
spliting1.goto(-280, -177)
spliting1.pendown()



turtle.register_shape("black.gif") #black stamps
spliting1.shape("black.gif")
stamp1=spliting1.stamp()
spliting1.goto(0, -177)
stamp2=spliting1.stamp()
spliting1.goto(280, -177)
stamp3=spliting1.stamp()
#second row
spliting1.goto(280, -1)
stamp4=spliting1.stamp()
spliting1.goto(0, -1)
stamp5=spliting1.stamp()
spliting1.goto(-280, -1)
stamp6=spliting1.stamp()
#3 row
spliting1.goto(-280, 175)
stamp7=spliting1.stamp()
spliting1.goto(0, 175)
stamp8=spliting1.stamp()
spliting1.goto(280, 175)
stamp9=spliting1.stamp()

turtle.register_shape("error2.gif")
error=turtle.clone()
error.shape("error2.gif")

def q():
    #global title
    #title.clear()
    #title.write(y, move=False, align="center", font=("Comic Sans Ms", 60, "normal"))
    time.sleep(3)
    quit()


cleared_stamps= []
stamps = [stamp1,stamp2,stamp3,stamp4,stamp5,stamp6,stamp7,stamp8,stamp9]
#turtles = [spliting1,spliting2,spliting3,spliting4,spliting5,spliting6,spliting7,spliting8,spliting9]
p = -280

for i in range(len(ques_list)):
    ans = turtle.textinput("Question "+str(i),ques_list[i])
    wrong = 0
    while ans!=ans_list[i]:
        wrong +=1
        error.goto(p, -350)
        p+=60
        error.hideturtle()
        stamp10=error.stamp()
        ans = turtle.textinput("Question "+str(i),ques_list[i])
        if wrong >= 10:
            q()


    choice = random.choice(stamps)
    while choice in cleared_stamps:
        choice = random.choice(stamps)
    if choice not in cleared_stamps:
        spliting1.clearstamp(choice)
        cleared_stamps.append(choice)


    
    guess=turtle.textinput("guess ","did you guess the picture?? if you didn't type no")
    if guess ==("teletubbies"):
        for x in stamps:
            spliting1.clearstamp(x)
        break
turtle.ontimer(q, 3000)
   
       

   


turtle.mainloop()

