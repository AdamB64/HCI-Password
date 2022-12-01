from guizero import App, PushButton
def do_nothing():
    print("A picture button was pressed")

app = App()
button = PushButton(app, text="t", command=do_nothing)
app.display()