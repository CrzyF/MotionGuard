from re import MULTILINE
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGrid(Widget):
    pass
    
class MyApp(App):
    def build(self):
        return MyGrid()

# class MyGrid(GridLayout):
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)

#         self.inside = GridLayout()
        
#         self.cols = 1
#         self.inside.cols = 2


#         self.inside.add_widget(Label(text="First Name : "))
#         self.name = TextInput(multiline=False)
#         self.inside.add_widget(self.name)

#         self.inside.add_widget(Label(text="Last Name : "))
#         self.lastname = TextInput(multiline=False)
#         self.inside.add_widget(self.lastname)

#         self.inside.add_widget(Label(text="Email : "))
#         self.email = TextInput(multiline=False)
#         self.inside.add_widget(self.email)

#         self.add_widget(self.inside)

#         self.next = Button(text="Next", font_size = 40)
#         self.next.bind(on_press=self.pressed)
#         self.add_widget(self.next)

#     def pressed(self, instance):
#         name = self.name.text
#         lastname = self.lastname.text
#         email = self.email.text
#         print('First Name:', name, 'Lastname:', lastname, 'Email:', email)
#         self.name.text = ""
#         self.lastname.text = ""
#         self.email.text = ""



# class MyApp(App):
#     def build(self):
#         # return Label(text='F is Crazy')
#         return MyGrid()


if __name__ == '__main__':
    MyApp().run()
