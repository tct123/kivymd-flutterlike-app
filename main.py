import kivy
import kivymd
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton

class MainApp(MDApp):
    def build(self):
        scr = MDScreen()
        self.lbl =MDLabel()
        self.count = 0
        self.lbl.text = f"You pressed this Button {self.count} times"
        scr.add_widget(self.lbl)
        addbtn = MDFloatingActionButton(icon = "android", on_release = self.btncounter)
        scr.add_widget(addbtn)
        return scr
    def btncounter(self,obj):
        self.count = self.count + 1
        self.lbl.text = f"You pressed this Button {self.count} times"

MainApp().run()