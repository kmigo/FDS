#coding=utf-8
import sqlite3,sys,os
reload(sys)
sys.setdefaultencoding('utf-8')



def commit_close(func):
	def decorator(*args):
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		sql = func(*args)
		cur.execute(sql)
		con.commit()
		con.close()
	return decorator
	


class Banco:
	@commit_close
	def createBanco(self,tabela=''):
		return """
create table '{}'(id INTEGER PRIMARY KEY AUTOINCREMENT,
				nome text UNIQUE,
				pos text,
				gols text,
				faltas text,
				jogos text,
				expulso text,
				celular text);
""".format(tabela)

	@commit_close
	def deletarTabela(self,tabela=''):
		return """
		drop table {}""".format(tabela)
	
	@commit_close
	def inserirDados(self,tabela='',nome='',pos='',gols='',faltas='',jogos='',expulso='',celular=''):
		return """
		insert into '{}'(nome,pos,gols,faltas,jogos,expulso,celular)
		values('{}','{}','{}','{}','{}','{}','{}')""".format(
		tabela,nome,pos,gols,faltas,jogos,expulso,celular)
	
	@commit_close
	def update(self,tabela='',coluna='',atualiza='',onde='nome',igual=''):
		return """
		UPDATE {} SET {} = {} WHERE {} = {}
		""".format(tabela,coluna,atualiza,onde,igual)
		
	def dbselect(self,tabela='',onde='nome',igual=''):
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		cur.execute('select * from {} where {} = {} '.format(
		tabela,onde,igual))
		resultado = cur.fetchall()
		con.close()
		return resultado
	
	@commit_close
	def db_delete(self,tabela='',onde='nome',igual=''):
		return """
		DELETE FROM {} WHERE {} = {}""".format(
		tabela,onde,igual)
	
			
	def dbselect(self,tabela=''):
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		cur.execute('select * from {} '.format(
		tabela))
		resultado = cur.fetchall()
		con.close()
		for cada in resultado[0]:
			print cada
		return resultado
		
#Banco().createBanco('fds')
#Banco().inserirDados('fds','jfjf','djjd','fjfk','fjfj','hfjf','jdkf')

#Banco().dbselect('fds')

		
con =sqlite3.connect('banco.db')
cuu= con.cursor()
cuu.execute('select ')
for i in cuu:
	print i

	

