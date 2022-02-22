from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.core.window import Window
Window.clearcolor=(.8,.8,.8,1)
class MainWidget(BoxLayout):
    pass

class TitleWidget(BoxLayout):
    pass
class FoodCardWidget(GridLayout):
    pass
class FoodCardScroll(ScrollView):
    pass

class SplitItApp(App):
    pass

SplitItApp().run()
