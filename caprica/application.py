from npyscreen import NPSAppManaged

from caprica.forms.main import MainForm


class Caprica(NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())
