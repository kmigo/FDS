#coding=utf-8
import sqlite3,sys,os
reload(sys)
sys.setdefaultencoding('utf-8')


class Banco(object):
	def __init__(self):
		self.banco='banco.db'
		
		novo = not os.path.isfile('banco.db')
		
		if novo:
			self.createBanco()
		
		self.conexao = sqlite3.connect('banco.db')
	

