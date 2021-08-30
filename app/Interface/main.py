import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):


    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Hello World')
        btn1 = Button(text="Welcome to edureka")
        layout.add_widget(btn)
        layout.add_widget((btn1))
        return layout


if __name__ == '__main__':
    MyApp().run()
