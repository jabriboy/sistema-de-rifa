import functions as func
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    NumericProperty
)

class Menu(RelativeLayout):
    nome = StringProperty('')
    tel = StringProperty('')
    bilhete = NumericProperty('')

    def create_person(self):
        func.create_person(self.nome, self.tel)

class RifaApp(App):
    pass


rifa = RifaApp()
rifa.run()