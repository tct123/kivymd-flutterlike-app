import kivy
import kivymd
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.toolbar import MDTopAppBar

class MainApp(MDApp):
    def build(self):
        scr = MDScreen()
        self.lbl =MDLabel()
        toolbar = MDTopAppBar()
        toolbar.pos_hint = {"top":1}
        scr.add_widget(toolbar)
        self.count = 0
        self.lbl.text = f"You pressed this Button {self.count} times"
        self.lbl.halign = "center"
        scr.add_widget(self.lbl)
        addbtn = MDFloatingActionButton(icon = "android", on_release = self.btncounter)
        scr.add_widget(addbtn)
        return scr
    def btncounter(self,obj):
        self.count = self.count + 1
        self.lbl.text = f"You pressed this Button {self.count} times"

MainApp().run()