from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition


class CustomPopup(Popup):
    invia_form = ObjectProperty(None)

    def dismiss_popup(self):
        self.dismiss()


class MainWindow(Screen):
    submit_button = ObjectProperty(None)
    nome = ObjectProperty(None)
    cognome = ObjectProperty(None)
    data_di_nascita = ObjectProperty(None)
    luogo_di_nascita = ObjectProperty(None)

    def conferma_invio_form(self):
        custom_popup = CustomPopup(title="Conferma invio form", size_hint=(0.5, 0.5), invia_form=self.invia_form)
        custom_popup.open()

    def invia_form(self):
        form = open("/home/tobia/Desktop/form.txt", "w+")
        form.write("Nome: ")
        form.write(self.nome.text)
        form.write("\n")
        form.write("Cognome: ")
        form.write(self.cognome.text)
        form.write("\n")
        form.write("Data di nascita: ")
        form.write(self.data_di_nascita.text)
        form.write("\n")
        form.write("Luogo di nascita: ")
        form.write(self.luogo_di_nascita.text)
        form.write("\n")
        sm.current = "secondwindow"


class SecondWindow(Screen):
    def go_back(self):
        sm.current = "mainwindow"


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("style.kv")


sm = WindowManager(transition=WipeTransition())

screens = [MainWindow(name="mainwindow"), SecondWindow(name="secondwindow")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "mainwindow"


class MainApp(App):
    def build(self):
        return sm


sample_app = MainApp()
sample_app.run()

