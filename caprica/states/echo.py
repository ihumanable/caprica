from blessed.keyboard import Keystroke

from caprica.states.base import State


class Echo(State):
    def __init__(self):
        self.buffer = []

    def keypress(self, key: Keystroke):
        if key.name:
            self.buffer.append(key.name)
        else:
            self.buffer.append(key)

    def render(self) -> str:
        return ' '.join(self.buffer)
