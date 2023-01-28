from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

class LoginScreen(Screen):
    pass
class HomeScreen(Screen):
    pass
Builder.load_file('kv/checkboxscreen.kv')
class CheckBoxScreen(Screen):
    new_line = '\n'
    checks = []
    def checkbox_click(self, instance, value, problem):
        if value == True:
            new_line = '\n'
            CheckBoxScreen.checks.append(problem)
            output = ''
            for x in CheckBoxScreen.checks:
                output = f'{output} {x} ; {new_line}'
            self.ids.output_label.text = f'This is wrong with your waste: {output}'
        else:
            new_line = '\n'
            CheckBoxScreen.checks.remove(problem)
            output = ''
            for x in CheckBoxScreen.checks:
                output = f'{output} {x} ; {new_line}'
            self.ids.output_label.text = f'This is wrong with your waste: {output}'
        print(value)

    pass



GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name #change current screen name to other





if __name__ == '__main__':
    MainApp().run()
