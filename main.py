from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivymd.navigationdrawer import NavigationDrawerIconButton
from kivymd.theming import ThemeManager
from kivymd.toast import toast

main_kv = """
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader


<ContentNavigationDrawer@MDNavigationDrawer>:
    drawer_logo: 'demos/kitchen_sink/assets/drawer_logo.png'

    NavigationDrawerSubheader:
        text: "Menu:"

<Barra@NavigationLayout>:
	id: barra
	
	ContentNavigationDrawer:
	    id: nav_drawer
	
	BoxLayout:
	    orientation: 'vertical'
	
	    Toolbar:
	        id: toolbar
	        title: 'Gestor de Futebol'
	        md_bg_color: app.theme_cls.primary_color
	        background_palette: 'Primary'
	        background_hue: '500'
	        elevation: 10
	        left_action_items:[['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]
	    
	    BoxLayout:
	    	id:box
<Tela@BoxLayout>:
	name:'pelada'
	BoxLayout:
		Button:
			
<Tela2@BoxLayout>:
	name:'pm'
	BoxLayout:
		Button:
		Button:


Barra:
"""


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = "Navigation Drawer"
    main_widget = None
    opcoes=['pelada','pm','Carros liberados']

    def build(self):
        self.main_widget = Builder.load_string(main_kv)
        return self.main_widget

    def callback(self, instance, value):
        toast("%s" % value)
        #self.main_widget.ids.manager.current='%s'%value
        

    def on_start(self):
        for i in self.opcoes:
            self.main_widget.ids.nav_drawer.add_widget(
                NavigationDrawerIconButton(
                    icon='checkbox-blank-circle', text="%s" % i,on_release=lambda x, y=i: self.callback(x, y)))

	def troca(self):
		self.remove_widget(Tela())
Example().run()
