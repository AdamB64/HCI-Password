from guizero import App,PushButton,TextBox,Window,Text
from datetime import datetime
import random 

app = App(title="Passwords")

d = datetime.now()

l=None

def Password():
    app.show()
    app2.hide()
    app3.hide()
    app4.hide()

app2 = Window(app,title="Password generator")

def Generator():
    app2.show()
    app.hide()
    app3.hide()
    app4.hide()

app3 = Window(app,title="Saved Passwords")

def saved():
    app.hide()
    app2.hide()
    app3.show()
    app4.hide()

def descriptim():
    i = input("What is the descrition you want for the password")
    return i

app4 =Window(app,title="Desription",height=75)

def save():
    global l
    h=[]
    o=[input.value,d,i.value]
    app4.show()
    h.append(o)
    app.hide()
    i.clear()
    l=h

def generate():
    p1=random.randint(1,10)
    p2=random.randint(1,10)
    p3=random.randint(1,10)
    p4=random.randint(1,10)
    p5=random.randint(1,10)
    p6=random.randint(1,10)
    p7=random.randint(1,10)
    p8=random.randint(1,10)
    p=[p1,p2,p3,p4,p5,p6,p7,p8]
    input.value=p

app5=Window(app,"Text search by date for password")

def search():
    app5.show()
    for h in range(0,14):
        if i2.value == save[h]:
            print(save[h])

app6=Window(app)

def toString():
    u.text(text=l)

def exit():
    app.destroy()


#buttons for home page
exits = PushButton(app,text="Exit",align="top",command=exit)
exits.text_color=255, 45, 0

time =Text(app,text=d)

button1 = PushButton(app,text="To See Saved Passwords",command=saved)

button2 = PushButton(app,text="Click here to generate new password",command=Generator)

#buttons for generator screen
time =Text(app2,text=d)

exits = PushButton(app2,text="Exit",align="top",command=exit)
exits.text_color=255, 45, 0

homes = PushButton(app2,text="Home",command=Password)

input = TextBox(app2,text="Type in password (Number only)",width=50)

button3 = PushButton(app2,text="save Password",command=save)

button4 = PushButton(app2,text="Find your Password here",command=saved)

button5 = PushButton(app2,text="Generate Password",command=generate)

#saves passwords screen buttons
time =Text(app3,text=d)

exits = PushButton(app3,text="Exit",align="top",command=exit)
exits.text_color=255, 45, 0

homes = PushButton(app3,text="Home",command=Password)

button6 = PushButton(app3,text="Click here to go to pass generator",command=Generator)

button7 = PushButton(app3,text="Click here to search by date and time saved",command=search)

button8 = PushButton(app3,text="Display last passwords",command=toString)

time =Text(app5,text=d)

t2 = Text(app5,text="Type your date and time below \n (how to type date and time in 2022-12-01 11:20:54)")
i2= TextBox(app5,width=50)

time =Text(app4,text=d)

t = Text(app4,text="Type your description below")
i= TextBox(app4,width=50)

u =Text(app3,text=l)

app2.hide()
app3.hide()
app4.hide()
app5.hide()
app6.hide()
app.display()