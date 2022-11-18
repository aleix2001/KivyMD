from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.clock import Clock
from kivymd.uix.datatables import MDDataTable #Para crear Tablas de datos
from kivy.metrics import dp #Para ver el display de pixels
from kivy.uix.anchorlayout import AnchorLayout

class ContentNavigationDrawer(MDBoxLayout):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()  

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color
        

class MyApp (MDApp):    
    def build(self):
        self.title = "PymeShield"
        Window.size = (400, 600)
        scroll = ScrollView()
        
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            size_hint=(0.7, 0.6),
            use_pagination=True,
            check=True,
            column_data=[]
        )
        
        list_view = MDList()
        for i in range(20):

            items = OneLineIconListItem(text=str(i) + ' item')
            list_view.add_widget(items)

        scroll.add_widget(list_view)
        layout.add_widget(self.data_tables)

        return Builder.load_file("main2.kv")


MyApp().run()
