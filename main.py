from kivymd.app import MDApp
from kivy.lang import Builder

import cv2

class SampleApp(MDApp):
    
    def build(self):
        self.appKv='''
MDScreen:
    MDLabel:
        text:'Hello,World.'
        multiline:True
        halign:'center'         
'''
        AppScreen=Builder.load_string(self.appKv)
        return AppScreen

SampleApp().run()
