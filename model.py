import logging
import os
import sys
import time



class Model:

    def __init__(self):
        self.m = 0.0
        self.nif = []
        self.nome = []
        self.apelido = []
        self.localizacao = []
        self.area = []
        self.tipologia = []
        self.imovel = []
        self.ano = []
        self.valor = []
        self.comissao = []


    def RegistarConsultor(self, nome, apelido , nif):

        self.nome = nome
        self.apelido = apelido
        self.nif = nif
        logging.info("Registo de Consultor")
        logging.info("Nome: " + self.nome)
        logging.info("Apelido: " + self.apelido)
        logging.info("NIF: " + self.nif)





    def VerificarNIF(self):
        if self.nif == None:
            return False
        else:
            for nif in self.nif:
                if nif == self.nif:
                    return True
            return False


    def VerificarEntrada(self, RC, RI, LI, EI, EC):
        if RC == None or RI == None or LI == None or EI == None or EC == None:
            return print("Erro: Entrada Invalida")
        else:
            return print("Entrada Valida")


    

    def RegistarImovel(self, nome, localizacao, nif, area, tipologia, imovel, ano, valor, comissao):
        self.nome = nome
        self.localizacao = localizacao
        self.nif = nif
        self.area = area
        self.tipologia = tipologia
        self.imovel = imovel
        self.ano = ano
        self.valor = valor
        self.comissao = comissao
        logging.info("Registo de Imovel")
        logging.info("Nome: " + self.nome)
        logging.info("Localizacao: " + self.localizacao)
        logging.info("NIF: " + self.nif)
        logging.info("Area: " + self.area)
        logging.info("Tipologia: " + self.tipologia)
        logging.info("Imovel: " + self.imovel)
        logging.info("Ano: " + self.ano)
        logging.info("Valor: " + self.valor)
        logging.info("Comissao: " + self.comissao)




    def ListarImoveisConsultor(self, nif):
        if self.nif == nif:
            return print("Imoveis do Consultor: ", self.nome)
        else:
            return print("Nao existe Consultor com este NIF")


    def EliminarImovel(self, nif , consultor , imovel):
        if self.nif == nif and self.nome == consultor and self.imovel == imovel:
            self.nif.remove(nif)
            self.nome.remove(consultor)
            self.imovel.remove(imovel)

            return print("Imovel Eliminado com Sucesso")
        else:
            return print("Imovel nao existe")

    def EliminarConsultor(self, nif):
        if self.nif == nif:
            self.nif.remove(nif)

            return print("Consultor Eliminado com Sucesso")
        else:
            return print("Consultor nao existe")











