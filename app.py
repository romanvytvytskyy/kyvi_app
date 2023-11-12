from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
        
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical')
        hl = BoxLayout()
        btn_1 = ScrButton(self, direction='left', goal='first', text="1")
        vl.add_widget(btn_1)      
        btn_2 = ScrButton(self, direction='up', goal='second', text="2")
        vl.add_widget(btn_2)      
        btn_3 = ScrButton(self, direction='down', goal='third', text="3")
        vl.add_widget(btn_3)      
        btn_4 = ScrButton(self, direction='right', goal='fourth', text="4")
        vl.add_widget(btn_4)      
        self.add_widget(vl)
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', size_hint = (.5,.5), 
                       pos_hint={'centr_x': 0.5, 'centr_y': 0.5})
        btn = ScrButton(self, direction='right', goal='main', text='To main screen')
        vl.add_widget(btn)
        self.add_widget(vl)      
        
class SecondScreen(Screen):
    pass
class ThirdScreen(Screen):
    pass
class FourthScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        return sm
    
MyApp().run()
    
    
    
    