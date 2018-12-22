#coding=utf-8

from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager

from kivymd.theming import ThemeManager


class GerenciadorTela(ScreenManager):
	pass


class Tela(Screen):
	pass
	

class Aplicativo(App):
	theme_cls = ThemeManager()
	theme_cls.primary_palette = "Blue"
	title = "FDS"
	def build(self):
		return GerenciadorTela()

Aplicativo().run()
