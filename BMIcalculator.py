from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from ActivityOne import FirstApp

class BMIApp(App):
    def build(self):
        box = BoxLayout(orientation="vertical")
        self.height_input = TextInput(hint_text="Enter height in meters", multiline=False)
        self.weight_input = TextInput(hint_text="Enter weight in kilograms", multiline=False)
        self.result_label = Button(text="Calculate BMI",)
        my_label = Label(text="BMI: ", font_size=24, size_hint=(1, 0.2))
                              

        box.add_widget(self.height_input)
        box.add_widget(self.weight_input)
        box.add_widget(self.result_label)
        box.add_widget(my_label)



        return box
    
if __name__ == '__main__':
    BMIApp().run()

