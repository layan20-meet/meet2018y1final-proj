import turtle
turtle.tracer(0,1) #speed
x="Guess The Picture"  #headline
title=turtle.clone()
title.penup()
title.goto(0,300)
title.pendown()
title.hideturtle()
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


spliting2=turtle.Turtle()
spliting2.penup()
spliting2.goto(0, -177)
spliting2.pendown()



spliting2.shape("black.gif")
stamp2=spliting2.stamp()



spliting3=turtle.Turtle()
spliting3.penup()
spliting3.goto(280, -177)
spliting3.pendown()



spliting3.shape("black.gif")
stamp3=spliting3.stamp()


#second row

spliting4=turtle.Turtle()
spliting4.penup()
spliting4.goto(280, -1)
spliting4.pendown()

spliting4.shape("black.gif")
stamp4=spliting4.stamp()





spliting5=turtle.Turtle()
spliting5.penup()
spliting5.goto(0, -1)
spliting5.pendown()

spliting5.shape("black.gif")
stamp5=spliting5.stamp()




spliting6=turtle.Turtle()
spliting6.penup()
spliting6.goto(-280, -1)
spliting6.pendown()

spliting6.shape("black.gif")
stamp6=spliting6.stamp()


#3 row
spliting7=turtle.Turtle()
spliting7.penup()
spliting7.goto(-280, 175)
spliting7.pendown()

spliting7.shape("black.gif")
stamp7=spliting7.stamp()




spliting8=turtle.Turtle()
spliting8.penup()
spliting8.goto(0, 175)
spliting8.pendown()

spliting8.shape("black.gif")
stamp8=spliting8.stamp()




spliting9=turtle.Turtle()
spliting9.penup()
spliting9.goto(280, 175)
spliting9.pendown()

spliting9.shape("black.gif")
stamp9=spliting9.stamp()




#questions 
ques1=turtle.textinput("Question 1","when was the first earth day?\n A.1982\n B.1970\n C.2003\n D.1999")
answer1= "b"
if answer1 == ques1 :
    spliting3.clearstamp(stamp3)
    ques2=turtle.textinput("Question 2","what have roots as no body sees, is taller than trees, up up it goes and it never grows?")
    answer2="mountain"
    if answer2 == ques2 :
        spliting9.clearstamp(stamp9)
        ques3=turtle.textinput("Question 3","How much of our air pollution comes from motor vehicles, like cars and tracks?\n A.50%\n B.20%\n C.80%\n D.30%")
        answer3="a"
        if answer3 == ques3 :
            spliting7.clearstamp(stamp7)
            ques4=turtle.textinput("Question 4","Alive withot breath, as cold as death,never thirsty ,ever drinking,and it never blinking?")
            answer4="fish"
            if answer4 == ques4 :
                spliting1.clearstamp(stamp1)
                ques5=turtle.textinput("Question 5","The melting of the Greenland ice sheet poses in immediate threat to reach animal?\n A.Penguins\n B.Killer Whales\n C.Polar Bears\n D.Muskoxen")
                answer5="c"
                if answer5 == ques5 :
                    spliting4.clearstamp(stamp4)
                    ques6=turtle.textinput("Question 6","which of the following help reduse air pollution?\n A.Using cruise control\n B.Using fluorecent lights\n C.Using water-based product\n D.all of the above")
                    answer6="d"
                    if answer6 == ques6 :
                        spliting5.clearstamp(stamp5)
                    
                    

                

            












turtle.mainloop()

