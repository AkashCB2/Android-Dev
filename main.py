# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 20:08:58 2021

@author: User
"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


#This is just a basic app made using first principles and Kivy.
#Special thanks to Kivy community and Kaustubh Gupta for his amazing online guide on how to make apps using Kivy.
#The following is in KivyMD language, it is the description of the GUI.

kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Welcome!'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y': 0.8}
    MDTextField:
        id: text
        hint_text: 'Input a number here'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        max_text_length: 8
        size_hint_x: None
        width: 300
        required: True
        
    MDRectangleFlatButton:
        text: 'Check'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.prime_check()
            
    MDLabel:
        text: ''
        id: output
        multiline: True
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

    def prime_check(self):
        x=int(self.root.in_class.text)
        z=[2]
        y=1
        
        if x==1:
            y=0.0
            label = self.root.ids.output
            label.text = "It is NOT prime by definition. Fun fact, 1 is oddly happy yet is not weird."
            
        for i in range(3,x,2):
            if x%2==0.0 or x%i==0.0:
                z.append(i)
                y=2.0
                label = self.root.ids.output
                label.text = "Not prime, the smallest divisor is "+ str(z[0] if x%2==0.0 else z[-1]) +"."
                break
        if y==1:
            label = self.root.ids.output
            label.text = "It is a prime."
    
    def intro(self):
        self.dialog = MDDialog(title="Info",
                                   text="This is a basic app developed using Python and Kivy, by Akash Chandra Behera, 2nd-year undergrad at IISER Kolkata. Special thanks to Kivy Community and Kaustubh Gupta for his amazing online guide on how to make apps using Kivy. NOTE : For large 8 digit numbers, the checking process may take upto 1 minute and use 200MB of RAM.", size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
                               )
        self.dialog.open()
    
    def close_dialog(self, obj):
        self.dialog.dismiss()


PrimeChecker().run()