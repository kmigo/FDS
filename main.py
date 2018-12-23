from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager

from kivymd.navigationdrawer import NavigationDrawerIconButton
from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivymd.navigationdrawer import NavigationLayout 

main_kv = """
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader


NavigationLayout
    id: nav_layout
    MDNavigationDrawer:
        id: nav_drawer
        NavigationDrawerToolbar:
            title: "Menu"
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Inicio"
            on_release: app.root.ids.scr_mngr.current = 'inicio'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Adicionar Futebol"
            on_release: app.root.ids.scr_mngr.current = 'adicionar'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Sobre"
            on_release: app.root.ids.scr_mngr.current = 'sobre'
       
    BoxLayout:
        orientation: 'vertical'
        Toolbar:
            id: toolbar
            title: 'Gestor de Futebol'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
            right_action_items: [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]
         
		ScreenManager:
			id:scr_mngr
			
			Screen:
				name:'inicio'
				BoxLayout:
					orientation:'vertical'
					BoxLayout:
						ScrollView:
							BoxLayout:
								orientation:'vertical'
								id:box
								size_hint_y:None
								height:self.minimum_height
					BoxLayout:
						size_hint_y:.1
						Button:
							on_release:app.verificas()
					
			
			Screen:
				name:'adicionar'
				BoxLayout:
					Button:
					Button:
			
			Screen:
				name:'sobre'
				BoxLayout:
					Button:
					Button:
					Button:

<Futebol>:
	size_hint_y:None
	height:200
	Button:
	Button:
		size_hint_x:None
		width:90
		text:'X'
		on_release:app.removeWidget(self)
				
"""

		
	
class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = "Navigation Drawer"
    main_widget = None

    def build(self):
        self.main_widget = Builder.load_string(main_kv)
        return self.main_widget
        
    def verificas(self):
		self.main_widget.ids.box.add_widget(Futebol(
		))
	
	
class Futebol(BoxLayout):
	def __init__(self,**kwargs):
		super(Futebol,self).__init__(**kwargs)
		
		
		
	




Example().run()
