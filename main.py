from tkinter import *
import funcionario as funcionario

class View_principal():
    def __init__(self, controle, root):
        self.root = root
        self.controle = controle
        
        self.menubar = Menu(self.root)
        self.menu_funcionario = Menu(self.menubar)
        
        self.root.config(menu=self.menubar)
        
        self.menubar.add_cascade(label='Opções', menu=self.menu_funcionario)
        self.menu_funcionario.add_command(label='Cadastrar Funcionário', command=controle.insere_funcionario)
        self.menu_funcionario.add_command(label='Consultar Funcionário', command=controle.consulta_funcionario)
        self.menu_funcionario.add_command(label='Definir Aumento', command=None)


class Controle_principal():
    def __init__(self):
        self.root = Tk()
        
        self.controle_funcionario = funcionario.Controle_funcionario()
        
        self.root.title('§')
        self.root.geometry('300x250')
        self.root.resizable(False, False)
        
        self.view = View_principal(self, self.root)
        
        self.root.mainloop()
        
    def insere_funcionario(self):
        self.controle_funcionario.insere_funcionario()
        
    def consulta_funcionario(self):
        self.controle_funcionario.consulta_funcionario()
        
if __name__ == '__main__':
    exec = Controle_principal()