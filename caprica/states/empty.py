from blessed.keyboard import Keystroke

from caprica.states.base import State


class Empty(State):
    def keypress(self, key: Keystroke):
        pass

    def render(self) -> str:
        return ''
