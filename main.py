from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import ObjectProperty

from kivymd.navigationdrawer import NavigationDrawerIconButton
from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivymd.navigationdrawer import NavigationLayout 

main_kv = """
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDFloatingActionButton kivymd.button.MDFloatingActionButton
#:import MDCard kivymd.card.MDCard
#:import MDFlatButton kivymd.button.MDFlatButton
#:import MDTextField kivymd.textfields.MDTextField
#:import MDRaisedButton kivymd.button.MDRaisedButton


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
            text: "Conta"
            on_release: app.root.ids.scr_mngr.current = 'conta'
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
				name:'conta'
				id:conta
				TelaLogin:
			
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
						BoxLayout:
						MDFloatingActionButton:
							icon:'plus'
							on_release:app.root.ids.scr_mngr.current='adicionar'
						BoxLayout:
							size_hint_x:.05
					BoxLayout:
						size_hint_y:.1
					
					
			
			Screen:
				name:'adicionar'
				BoxLayout:
					ScrollView:
						BoxLayout:
							orientation:'vertical'
							size_hint_y:None
							height:self.minimum_height
			
			
						
					BoxLayout:
						
							
			
			Screen:
				name:'sobre'
				BoxLayout:
					Button:
					Button:
					Button:

<Futebol>:
	size_hint_y:None
	height:250
	padding:30
	MDCard:
		padding:0,20
		BoxLayout:
			Screen:
				MDFlatButton:
					id:btfut
					pos_hint:{"center_x":.65,"center_y":.5}
					size_hint:None,None
					size:dp(300),140
					text:'Futebol Fim de Semana'
			Screen:
				MDRaisedButton:
					id:btdel
					pos_hint:{"center_x":.65,"center_y":.5}
					size_hint_y:None
					height:140
					text:'X'
					on_release:app.remove(root)
<TelaLogin>:
	orientation:'vertical'
	BoxLayout:
		size_hint_y:.3
		Label:
			id:falha
			text:'ola'
			color:0,0,0,1
	BoxLayout:
		padding:90
		spacing:10
		size_hint_y:.3
		orientation:'vertical'
		MDTextField:
			hint_text:'Login'
			id:txtlogin
		MDTextField:
			hint_text:'Senha'
			password : True
			id:txtsenha
	Screen:
		MDRaisedButton:
			text:'Entrar'
			pos_hint:{'center_x':0.5,'center_y':.5}
			on_release:root.login()
			
			

				
"""

class TelaLogin(BoxLayout):
	def login(self,*args):
		self.ids.falha.text='oi'
		App.get_running_app().main_widget.ids.conta.clear_widgets()
	
class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = "Navigation Drawer"
    main_widget = None
    conectado = None
    tipo = {'adm':'admin','client':'fut'}
    alogin = 'admin'
    asenha = 'adm123'
    flogin = 'fut'
    fsenha = 'fut123'
    def verificas(self):
		self.main_widget.ids.box.add_widget(Futebol(
		))
	

    def build(self):
        self.main_widget = Builder.load_string(main_kv)
        return self.main_widget
    
    def remove(self,botao):
		self.main_widget.ids.box.remove_widget(botao)
	
	
    def login(self,*args): 
    	login=str(self.main_widget.ids.txtlogin.text)
    	senha=str(self.main_widget.ids.txtsenha.text)
    	adm=login == self.alogin and senha == self.asenha[0][1]
    	
    	clt=login == self.flogin and senha == self.fsenha
    	sm=ObjectProperty(self.main_widget.ids.scr_mngr)
    	if clt:
    		self.main_widget.ids.scr_mngr.current='inicio'
    		self.main_widget.ids.conta.clear_widgets()
    	else:
    		self.main_widget.ids.falha.text='erro login'
	
class Futebol(BoxLayout):
	def __init__(self,**kwargs):
		super(Futebol,self).__init__(**kwargs)
		

		
		
		
	




Example().run()
