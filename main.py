#coding=utf-8

from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager


class GerenciadorTela(ScreenManager):
	pass


class Tela(Screen):
	pass
	

class Aplicativo(App):
	def build(self):
		return GerenciadorTela()

Aplicativo().run()
