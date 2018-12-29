import mysql.connector

class Banco(object):
		
	def commit_close(func):
		def decorator(*args):
			con = mysql.connector.connect(
				host='mysql.uhserver.com',
				user='kmigo01',
				passwd='so@res11',
				database='futsemana')
				
			cur = con.cursor()
			sql = func(*args)
			cur.execute(sql)
			#print cur
			con.commit()
			con.close()
		return decorator
	
	@commit_close
	def createTable(self,tabela):
		return '''
		create table `{}`(id int NOT NULL AUTO_INCREMENT,
		`nome` varchar(20) NOT NULL,
		nascimento date,
		pos enum('ATA','MC','GL'),
		gols int,
		faltas int,
		primary key(id)
		)  ;
		'''.format(tabela)
	
	@commit_close
	def dropTable(self,table):
		return '''
		drop table {}'''.format(table)
	
	def showTable(self):
		l=[]
		con = mysql.connector.connect(
				host='mysql.uhserver.com',
				user='kmigo01',
				passwd='so@res11',
				database='futsemana')
		
		cur = con.cursor()
		cur.execute('show tables')
		for i in cur:
			for a in i:
				l.append(a)
			
		con.close()
		return l
	
	@commit_close
	def db_insert(self,tabela,nome,nascimento,pos,gols,faltas):
		return '''
		insert into {}(nome,nascimento,pos,gols,faltas)
		values("{}","{}","{}","{}",{})'''.format(tabela,nome,nascimento,pos,gols,faltas)
	
	def db_selectAll(self,tabela):
		con = mysql.connector.connect(
		host='mysql.uhserver.com',
		user='kmigo01',
		passwd='so@res11',
		database='futsemana')
		
		cur = con.cursor()
		cur.execute('select * from {}'.format(
		tabela))
		
		resultado = cur.fetchall()
		for i in resultado:
			print i
		con.close()
	
	def delete(self):
		pass
		
#Banco().dropTable('fds')
#Banco().createTable('fds')''
#Banco().db_selectAll('fds')
#Banco().db_insert('fds','patrick','1997-10-10','ATA','1','1')
#print Banco().showTable()
	
	
	
