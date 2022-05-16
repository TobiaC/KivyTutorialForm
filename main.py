#!/usr/bin/env python3
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition, SlideTransition
from kivy.uix.dropdown import DropDown


from kivy.core.window import Window
Window.size = (1080, 1920)

from tinydb import TinyDB

db = TinyDB('db.json')

class CustomDropDown(DropDown):
    pass


class CustomPopup(Popup):
    invia_form = ObjectProperty(None)

    def dismiss_popup(self):
        '''
        MODIFY: chiusura del popup
        '''
        self.dismiss()


class MainWindow(Screen):
    submit_button = ObjectProperty(None)
    nome = ObjectProperty(None)
    cognome = ObjectProperty(None)
    giorno = ObjectProperty(None)
    mese = ObjectProperty(None)
    anno = ObjectProperty(None)
    luogo_di_nascita = ObjectProperty(None)
    professione = ObjectProperty(None)
    patenteA = ObjectProperty(None)
    patenteB = ObjectProperty(None)
    patenteC = ObjectProperty(None)


    def conferma_invio_form(self):
        '''
        MODIFY: crea una finestra popup per una conferma di invio del form compilato
        '''
        custom_popup = CustomPopup(title="Conferma invio form", size_hint=(0.9, 0.9), invia_form=self.invia_form)
        custom_popup.open()

    def ottieni_data_nascita(self):
        return self.giorno.text + " " + self.mese.text + " " + self.anno.text

    def invia_form(self):
        patenti = []

        if self.patenteA.active:
            patenti.append('A')
        if self.patenteB.active:
            patenti.append('B')
        if self.patenteC.active:
            patenti.append('C')

        db.insert({'nome':self.nome.text, 'cognome':self.cognome.text, 'data_di_nascita':self.ottieni_data_nascita(),'luogo di nascita':self.luogo_di_nascita.text,'professione':self.professione.text, 'patenti':patenti})
        print(db.all())
        sm.switch_to(screens[1], direction="left")

from kivy.uix.label import Label

class SecondWindow(Screen):
    data_riassunto = ObjectProperty(None)

    def ottieni_dati(self):
        for user in db:
            for key,value in user.items():
                text = str(key) + ": " + str(value) + "\n"
                self.data_riassunto.add_widget( Label(text="\n" + text, color=(0,0,0,1)) )
            self.data_riassunto.add_widget(Label(text="-----------------------", color=(0,0,0,1)))
            

    def go_back(self):
        '''
        MODIFY: cambia la finestra visualizzata passando alla MainWindow
        '''
        self.data_riassunto.clear_widgets()
        sm.switch_to(screens[0], direction="right")


class WindowManager(ScreenManager):
    pass


# caricamento del file kivy
kv = Builder.load_file("style.kv")

# creazione dello screen manager che viene usato per gestire gli Screen (schermate)
sm = WindowManager(transition=SlideTransition())

# lista degli screen (schermate)
screens = [MainWindow(name="mainwindow"), SecondWindow(name="secondwindow")]

for screen in screens:
    sm.add_widget(screen)

# definizione della schermata da visualizzare all'apertura dell'applicazione
sm.current = "mainwindow"


class MainApp(App):
    def build(self):
        return sm


sample_app = MainApp()
sample_app.run()

