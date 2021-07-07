# -*- coding: utf-8 -*-
"""
Created on Sat July  5 20:08:58 2021

@author: Akash Chandra Behera
"""
import numpy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


#This is just a basic app made using Lagrange interpolation and Kivy.
#Special thanks to Kivy community and Kaustubh Gupta for his amazing online guide on how to make apps using Kivy.
#The following is in KivyMD language, it is the description of the GUI.


kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Estimator/Interpolator'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y': 0.9}
    MDTextField:
        id: text
        
        hint_text: 'Give x values (separated by comma)'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        
        size_hint_x: 0.5
        width: 300
        required: True
       
    MDTextField:
        id: xtt
        hint_text: 'Give respective f(x) values (separated by comma)'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        size_hint_x: 0.5
        width: 300
        required: True
    MDTextField:
        id: ott
        hint_text: 'Give x where f(x) is needed'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        max_text_length: 8
        size_hint_x: None
        width: 300
        required: True
        
    MDRectangleFlatButton:
        text: 'Estimate'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.lagrange_interpolator()
            
    MDLabel:
        text: ''
        id: output
        multiline: True
        halign: 'center'
        pos_hint: {'center_y': 0.2}
        
    MDIconButton:
        icon : "information"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        on_press:
            app.info()
    
"""
#pos_hint: {'center_x': 0.8, 'center_y': 0.2}

class ValueEstimator(MDApp):
    in_class = ObjectProperty(None) 

    def build(self):
        return Builder.load_string(kv)

    def lagrange_interpolator(self):
        
        #Let's do lagrange interpolation
        
        ll=(self.root.in_class.text).split(",")
        lx=(self.root.ids.xtt.text).split(",")
        #Now x points must be unique
        xx=numpy.array([float(i) for i in ll])
        x=numpy.intersect1d(xx,xx)
        y=numpy.array([float(i) for i in lx])
        
        
        k=float(self.root.ids.ott.text)
        if len(x)!=len(y):
            label = self.root.ids.output
            label.text = "Error! x-values must be unique (as f(x) is assumed to be a function)."
        else:
            #Lets calculate denominator
            denos=[]
            for j in range(len(x)):
                z=1.0
                for i in range(len(x)):
                    if j!=i:
                        z=z*(x[j]-x[i]) #Using formula given in slides
                denos.append(z) 
            #print(denos)
            #Now let's compute func at k
            ans=[]
            for i in range(len(x)):
                ans_i=y[i]
                for j in range(len(x)):
                    if j!=i:
                        ans_i=ans_i*(k-x[j]) #Using formula given in slides
                ans.append(ans_i/denos[i])
            #print(ans)
            pri=round(numpy.sum(numpy.array(ans)),5)
            label = self.root.ids.output
            label.text = "Estimated Value at "+str(k)+" is "+str(pri)+" (rounded to 5 decimal places)"
    
    def info(self):
        self.dialog = MDDialog(title="Info",
                                   text="Hello! This estimator uses Lagrange interpolation to approximate an unknown function by Lagrange polynomials, like any estimation the output of this estimator will have some error, which will depend on the quality of inputs (e.g. number of input points and how closely spaced they are).\nNote, the unknown function is assumed to be differentiable in the interval of data points. BEWARE! Failure to input numbers in the suggested method may lead to the app becoming unresponsive.\nThis is a basic app developed using Python and Kivy, by Akash Chandra Behera, 2nd-year Undergrad at IISER Kolkata. Special thanks to Kivy Community and Kaustubh Gupta of TowardsDataScience.com for his amazing tutorials!", size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
                               )
        self.dialog.open()
    
    def close_dialog(self, obj):
        self.dialog.dismiss()


ValueEstimator().run()
