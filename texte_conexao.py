
# -*- coding: utf-8 -*-

from conexao import conectar

def main():
   with conectar() as conexao:
       cursor = conexao.cursor()
       cursor.execute("SELECT VERSION(), DATABASE()")
       versao, banco = cursor.fetchone()
       print("Conectado!")
       print("Servidor:", versao)
       print("Banco em uso:", banco)

if __name__ == "__main__":
   main()