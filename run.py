from blessed import Terminal

from caprica.application import Application
from caprica.states.echo import Echo

app = Application()
app.push(Echo())
term = Terminal()

with term.fullscreen():
    while app.run:
        print(term.clear)
        print(app.render())
        with term.cbreak():
            app.keypress(term.inkey())
