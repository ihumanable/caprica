from npyscreen import Form, TitleText

class MainForm(Form):
    def create(self):
        self.add(TitleText, name="Text:", value="Hellow World!")

    def afterEditing(self):
        self.parentApp.setNextForm(None)
