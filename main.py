#coding=utf-8
import sys,json
reload(sys)
sys.setdefaultencoding('utf-8')

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
from kivymd.label import MDLabel 

main_kv = """
#coding:utf-8
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDFloatingActionButton kivymd.button.MDFloatingActionButton
#:import MDCard kivymd.card.MDCard
#:import MDFlatButton kivymd.button.MDFlatButton
#:import MDTextField kivymd.textfields.MDTextField
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem



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
			
			TelaInicio:
				name:'inicio'	
			
			TelaAdicionar:
				name:'adicionar'
				
			
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
					on_release:app.root.ids.scr_mngr.get_screen('inicio').removerWidget(root)
<TelaLogin>:
	orientation:'vertical'
	BoxLayout:
		size_hint_y:.3
		Label:
			id:falha
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
	BoxLayout:
		Screen:
			MDRaisedButton:
				text:'Entrar'
				pos_hint:{'center_x':0.5,'center_y':.5}
				on_release:root.login()
		
			
<TelaAdm>:
	orientation:'vertical'
	padding:100
	BoxLayout:
		size_hint_y:.1
	MDCard:
		MDList:
			OneLineListItem:
				text:'Status: Conectado'
			TwoLineListItem:
				text:'Usuario:  Administrador'
				secondary_text:'Usuario previlegiado'
			ThreeLineListItem:
				text:'Nivel de Permisão: Global'
				secondary_text:'Dentre suas permições esta o dominio geral ds criação e ediçao '
			OneLineListItem:
				text:'Versão: 1.0'
			ThreeLineListItem:
				text:'Finalidade: Uso Pessoal'
				secondary_text:'A criação e uso do aplicativo foi desenvolvida para fins pessoais.'
			BoxLayout:
				Screen:
				
					MDRaisedButton:
						text:'Sair'
						on_release:root.logout()
						pos_hint:{'center_x':.5,'center_y':.5}
				Screen:
					
					MDRaisedButton:
						text:'Ver Jogos'
						on_release:app.root.ids.scr_mngr.current='inicio'
						pos_hint:{'center_x':.5,'center_y':.5}
				
			
	BoxLayout:
		size_hint_y:.1


<TelaClt>:
	orientation:'vertical'
	padding:100
	BoxLayout:
		size_hint_y:.1
	MDCard:
		MDList:
			OneLineListItem:
				text:'Status: Conectado'
			TwoLineListItem:
				text:'Usuario:  Cliente'
				secondary_text:'Usuario limitado'
			ThreeLineListItem:
				text:'Nivel de Permisão: mediana'
				secondary_text:'Dentre suas permições esta a visualização de conteudo '
			OneLineListItem:
				text:'Versão: 1.0'
			ThreeLineListItem:
				text:'Finalidade: Uso Pessoal'
				secondary_text:'A criação e uso do aplicativo foi desenvolvida para fins pessoais.'
			BoxLayout:
				Screen:
					
					MDRaisedButton:
						text:'Sair'
						on_release:root.logout()
						pos_hint:{'center_x':.5,'center_y':.5}
				Screen:
					
					MDRaisedButton:
						text:'Ver Jogos'
						on_release:app.root.ids.scr_mngr.current='inicio'
						pos_hint:{'center_x':.5,'center_y':.5}
					
				
			
	BoxLayout:
		size_hint_y:.1

<TelaAdicionar>:
	BoxLayout:
		orientation:'vertical'
		ScrollView:
			BoxLayout:
				size_hint_y:None
				height:self.minimum_height
				orientation:'vertical'
				BoxLayout:
					orientation:'vertical'
					size_hint_y:None
					height:400
					padding:90
					spacing:10
					canvas:
						Color:
							rgba:.6,0.6,0,1
						Rectangle:
							size:self.size
							pos:self.pos
					Screen:
						MDTextField:
							hint_text:'Nome'
							id:futnome
					Screen:
						MDTextField:
							hint_text:'Descrição'
							helper_text:'Campo não obrigatorio!'
							helper_text_mode:'on_focus'
				OneLineListItem:
				Screen:
					MDRaisedButton:
						text:'Salvar'
						pos_hint:{'center_x':.5,'center_y':.5}
						on_release:root.salvar()
					
	
<TelaInicio>:
	id:telainicio
	name:'inicio'
	BoxLayout:
		orientation:'vertical'
		ScrollView:
			BoxLayout:
				orientation:'vertical'
				id:box
				size_hint_y:None
				height:self.minimum_height
		BoxLayout:
			size_hint_y:.1
			id:boxusuario
		
		BoxLayout:
			size_hint_y:.05
		
<BotaoPlus>:
	BoxLayout:
	BoxLayout:
	BoxLayout:
		size_hint_x:.48
		MDFloatingActionButton:
			icon:'plus'
			on_release:app.root.ids.scr_mngr.current='adicionar'
			
				
"""



class BotaoPlus(BoxLayout):
	pass


conectado=None
logado=''

class TelaUsuario(Screen):
	pass


class TelaInicio(Screen):
	dados=[]
	def on_pre_enter(self):
		self.carregar()
		self.ids.box.clear_widgets()
		global conectado,logado
		
		if conectado and logado == 'adm':
			self.ids.boxusuario.clear_widgets()
			self.ids.boxusuario.add_widget(BotaoPlus())
		else:
			self.ids.boxusuario.clear_widgets()
		
		for cada in self.dados:
			self.ids.box.add_widget(Futebol(cada))
	
	def carregar(self,*args):
		try:
			with open('lista.json','r') as file:
				self.dados=json.load(file)
		except:
			pass
	
	def removerWidget(self,botao):
		global logado,conectado
		if logado == 'adm':
			self.ids.box.remove_widget(botao)
			self.dados.remove(botao.ids.btfut.text)
			self.salvar()
		else:
			toast('Atitude negada, baixo nivel de autoridade!')
		
	def salvar(self,*args):
		try:
			with open('lista.json','w') as file:
				json.dump(self.dados,file)
		except:
			pass

class TelaAdicionar(Screen):
	dados=[]
	def on_pre_enter(self):
		self.carregar()
	def carregar(self,*args):
		try:
			with open('lista.json','r') as file:
				self.dados=json.load(file)
		except:
			pass
	
	def salvar(self,*args):
		futebol=self.ids.futnome.text
		self.dados.append(futebol)
		self.salvardados()
		
	def salvardados(self,*args):
	
		try:
			with open('lista.json','w') as file:
				json.dump(self.dados,file)
		except:
			pass
		

class TelaClt(BoxLayout):
	def logout(self,*args):
		global conectado,logado
		conectado=None
		logado=''
		App.get_running_app().main_widget.ids.conta.clear_widgets()
		App.get_running_app().main_widget.ids.conta.add_widget(TelaLogin())


class TelaAdm(BoxLayout):
	def logout(self,*args):
		global conectado,logado
		conectado=None
		logado=''
		App.get_running_app().main_widget.ids.conta.clear_widgets()
		App.get_running_app().main_widget.ids.conta.add_widget(TelaLogin())

class TelaLogin(BoxLayout):

	contas = [['admin','@adm321'],['fut','fut123']]
	
	def login(self,*args):
		global logado,conectado
		login=self.ids.txtlogin.text
		senha=self.ids.txtsenha.text
		adm= login == str(self.contas[0][0]) and senha == str(self.contas[0][1]) 
		
		clt= login == str(self.contas[1][0]) and senha == str(self.contas[1][1])
		
		if adm:
			self.ids.falha.text=''
			logado='adm'
			App.get_running_app().main_widget.ids.conta.clear_widgets()
			conectado=True
			App.get_running_app().main_widget.ids.scr_mngr.current='inicio'
			
			App.get_running_app().main_widget.ids.conta.add_widget(TelaAdm())
			
		elif clt:
			logado='clt'
			self.ids.falha.text=''
			App.get_running_app().main_widget.ids.conta.clear_widgets()
			App.get_running_app().main_widget.ids.scr_mngr.current='inicio'
			App.get_running_app().main_widget.ids.conta.add_widget(TelaClt())
			conectado=True
			
		else:
			self.ids.falha.text='erro login'
		#App.get_running_app().main_widget.ids.conta.clear_widgets()
	
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
	
	
   
class Futebol(BoxLayout):
	def __init__(self,texto,**kwargs):
		super(Futebol,self).__init__(**kwargs)
		self.ids.btfut.text=texto
		

		
		
		
	




Example().run()
