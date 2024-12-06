from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Carregar o arquivo .kv
Builder.load_file("main.kv")

class RPGApp(App):
    def build(self):
        return MainLayout()

class MainLayout(BoxLayout):
    pass

if __name__ == "__main__":
    RPGApp().run()
