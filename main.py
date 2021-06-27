#!/usr/bin/env python3

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition, SlideTransition
from kivy.uix.dropdown import DropDown


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
        custom_popup = CustomPopup(title="Conferma invio form", size_hint=(0.5, 0.5), invia_form=self.invia_form)
        custom_popup.open()

    def ottieni_data_nascita(self):
        return self.giorno.text + " " + self.mese.text + " " + self.anno.text

    def invia_form(self):
        patenti = "Patenti in possesso: "
        '''
        MODIFY: crea (o modifica) un file su desktop contenente le informazioni immesse nei campi
                modifica la schermata visualizzata passando alla SecondWindow
        '''
        form = open("/home/tobiac/Scrivania/form.txt", "w+")
        form.write("Nome: ")
        form.write(self.nome.text)
        form.write("\n")
        form.write("Cognome: ")
        form.write(self.cognome.text)
        form.write("\n")
        form.write("Data di nascita: ")
        form.write(self.ottieni_data_nascita())
        form.write("\n")
        form.write("Luogo di nascita: ")
        form.write(self.luogo_di_nascita.text)
        form.write("\n")
        form.write("professione: " + self.professione.text)
        form.write("\n")
        if self.patenteA.active:
            patenti = patenti + "A "
        if self.patenteB.active:
            patenti = patenti + "B "
        if self.patenteC.active:
            patenti = patenti + "C "
        form.write(patenti)
        sm.switch_to(screens[1], direction="left")


class SecondWindow(Screen):
    def go_back(self):
        '''
        MODIFY: cambia la finestra visualizzata passando alla MainWindow
        '''
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

