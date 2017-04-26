from blessed.keyboard import Keystroke

from caprica.states.base import State
from caprica.states.echo import Echo
from caprica.states.empty import Empty


class Application(object):
    def __init__(self):
        self.run = True
        self.states = []
        self.last_keypress = None
        self._empty = Empty()

    @property
    def top(self) -> State:
        if not self.states:
            return self._empty
        return self.states[-1]

    def push(self, state: State):
        self.states.append(state)

    def pop(self) -> State:
        if self.states:
            return self.states.pop()
        else:
            return self._empty

    def keypress(self, key: Keystroke):
        if key.name == 'KEY_TAB':
            self.push(Echo())
        elif key.name == 'KEY_DELETE':
            self.pop()
        elif key.name == 'KEY_ESCAPE':
            self.run = False
        else:
            self.last_keypress = key
            self.top.keypress(key)

    def render(self) -> str:
        stack_output = '[ {} ]'.format(' :: '.join([s.__class__.__name__ for s in self.states]))
        key_output = ('{} {} {}'.format(self.last_keypress, self.last_keypress.name, self.last_keypress.code)
                      if self.last_keypress else '')
        debug_output = '{} {}'.format(stack_output, key_output)
        state_output = self.top.render()
        return '\n'.join([debug_output, state_output])
