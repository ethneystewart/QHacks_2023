
import kivy
kivy.require('2.1.0')

from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.app import App
from connected import Connected
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

class Login(Screen):
    def do_login(self, homeText):
        # COLOUR CODE HERE, not doing anything?
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        app = App.get_running_app()

        app.welcome = homeText


        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""


## Sample Python application demonstrating the
## working with images in Kivy using .kv file

Config.set('graphics', 'resizable', True)

# creating the root widget used in .kv file
class Imagekv(BoxLayout):
    '''
        no need to do anything here as
        we are building things in .kv file
    '''
    pass


class HomeApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='home'))
        manager.add_widget(Connected(name='connected'))

        return manager

        # returning the instance of Imagekv class
        return Imagekv()

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(HomeApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    LoginApp().run()
