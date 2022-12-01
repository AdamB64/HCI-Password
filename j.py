from guizero import App, Text, PushButton

def say_goodbye(first_name, last_name):
    text.value = first_name + " " + last_name


app = App()
text = Text(app)
button = PushButton(app, command=say_goodbye, args=['John', 'Doe'])
app.display()