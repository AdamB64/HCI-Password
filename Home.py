from guizero import App,PushButton,TextBox,Window,Text
from datetime import datetime
import random 

app = App(title="Passwords")

d = datetime.now()

l=[]

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

app3 = Window(app,title="Saved Passwords",width=1000)

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
    app4.show()
    global l
    h=[]
    o=[input.value,d,i.value]
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

app6=Window(app)

def toString():
    for u in range(0,14):
        u.value=i[u]

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

button7 = PushButton(app3,text="Display last passwords",command=toString)

time =Text(app4,text=d)

t = Text(app4,text="Type your description below")
i= TextBox(app4,width=50)

u =Text(app3)

app2.hide()
app3.hide()
app4.hide()
app6.hide()
app.display()