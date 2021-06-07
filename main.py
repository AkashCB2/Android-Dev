# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 20:08:58 2021

@author: User
"""
#import numpy as np
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

#x=int(self.root.in_class.text == 'root')
#z=[2]
#y=1
#for i in range(3,x,2):
 #   if x%2==0.0 or x%i==0.0:
  #      z.append(i)
   #     y=0.0
    #    label = self.root.ids.show
     #   label.text = "Not Prime"
      #  break
#if y==1:
#label = self.root.ids.show
#label.text = "Prime"+str(y)

#The following is in KivyMD language, it is the description of the GUI.

kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Welcome!'
        font_style: 'H2'
        pos_hint: {'center_x': 0.8, 'center_y': 0.8}
    MDTextField:
        id: text
        hint_text: 'Input a number here'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        max_text_length: 20
        size_hint_x: None
        width: 300
        required: True
        
    MDRectangleFlatButton:
        text: 'Check'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.auth()
            
    MDLabel:
        text: ''
        id: show
        halign: 'center'
        pos_hint: {'center_y': 0.2}
        
    MDIconButton:
        icon : "information"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_press:
            app.intro()
"""
#pos_hint: {'center_x': 0.8, 'center_y': 0.2}

class PrimeChecker(MDApp):
    in_class = ObjectProperty(None) 

    def build(self):
        return Builder.load_string(kv)

    def auth(self):
        x=int(self.root.in_class.text)
        z=[2]
        y=1
        for i in range(3,x,2):
            if x%2==0.0 or x%i==0.0:
                z.append(i)
                y=0.0
                label = self.root.ids.show
                label.text = "Not Prime, the smallest divisor is "+ str(z[0] if x%2==0.0 else z[-1]) +"."
                break
        if y==1:
            label = self.root.ids.show
            label.text = "It is a Prime."
    
    def intro(self):
        self.dialog = MDDialog(title="Intro",
                                   text="This is a basic app developed by Akash Chandra Behera, 2nd Year Undergrad at IISER-K. Special thanks Kaustabh Gupta for his amazing online guide on how to make apps using Kivy.", size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
                               )
        self.dialog.open()
    
    def close_dialog(self, obj):
        self.dialog.dismiss()


PrimeChecker().run()
