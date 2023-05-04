from kivy.app import App
from kivy.uix.image import Image

class Imageviewer(App):
    def build(self):
        img = Image(source='abc.jpg')
        return img
    
Imageviewer().run()
