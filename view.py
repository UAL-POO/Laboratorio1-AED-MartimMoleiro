class View:
    def welcome(self):
        print ("Sistema de gestao de imoveis (RC)Registar Consultor, (RI)Registar Imovel,  (LI)Listar Imovel, (EI)Eliminar Imovel,  (EC)Eliminar Consultor, (S)Sair")



    def registar_consultor(self):
        print ("Introduza o nome do consultor: ")

    def registar_imovel(self):
        print ("Introduza o nome do imovel: ")

    def listar_imovel(self):
        print ("Imoveis registados: ")

    def eliminar_imovel(self):
        print ("Introduza o nome do imovel: ")

    def eliminar_consultor(self):
        print ("Introduza o nome do consultor: ")

    def sair(self):
        print ("Saindo...")

    def erro(self):
        print ("Opcao invalida")