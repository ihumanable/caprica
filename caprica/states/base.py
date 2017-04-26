from blessed.keyboard import Keystroke


class State(object):
    def keypress(self, key: Keystroke):
        raise NotImplementedError

    def render(self) -> str:
        raise NotImplementedError
