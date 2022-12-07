from guizero import App,PushButton,TextBox,Window,Text,ListBox
from datetime import datetime
import random 

app = App(title="Passwords")

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
    app4.show()

app3 = Window(app,title="Saved Passwords",width=1000)

def saved():
    app.hide()
    app2.hide()
    app3.show()
    app4.hide()

app4 =Window(app,title="Desription",height=150)

def description():
    while i.value =="":
        t2.show()
        return i
    t2.hide()
    app4.hide()
    return i


def save():
    while len(input.value) >8:
        input.clear()
        input.append("Only 8 numbers")
        return input.value
    app4.show()
    h=[]
    o=[input.value,datetime.now(),i.value]
    h.append(o)
    app.hide()
    i.clear()
    for n in h:
        u.append(n)
      

def generate():
    p= random.randint(11111111,99999999)
    input.value=p

app6=Window(app)

def toString():
    u.show()

def exit():
    app.destroy()


#buttons for home page
exits = PushButton(app,text="Exit",align="top",command=exit)
exits.text_color=255, 45, 0

time =Text(app,text=datetime.now())

button1 = PushButton(app,text="To See Saved Passwords",command=saved)

button2 = PushButton(app,text="Click here to generate new password",command=Generator)

#buttons for generator screen
time =Text(app2,text=datetime.now())

exits = PushButton(app2,text="Exit",align="top",command=exit)
exits.text_color=255, 45, 0

homes = PushButton(app2,text="Home",command=Password)

input = TextBox(app2,text="Type in password (Number only and only 8 numbers)",width=50)

button3 = PushButton(app2,text="save Password",command=save)

button4 = PushButton(app2,text="Find your Password here",command=saved)

button5 = PushButton(app2,text="Generate Password",command=generate)

#saves passwords screen buttons
time =Text(app3,text=datetime.now())

exits = PushButton(app3,text="Exit",align="top",command=exit)
exits.text_color=255, 45, 0

homes = PushButton(app3,text="Home",command=Password)

button6 = PushButton(app3,text="Click here to go to pass generator",command=Generator)

button7 = PushButton(app3,text="Display all passwords",command=toString)

time =Text(app4,text=datetime.now())

t = Text(app4,text="Type your description below")
i= TextBox(app4,width=50)
t2= Text(app4,text="password needs a secription")
t2.hide()

button8 =PushButton(app4,text="To save desription",command=description)

u =ListBox(app3,width=1000,height=500)

app2.hide()
app3.hide()
app4.hide()
app6.hide()
app.display()