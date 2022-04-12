
import view
import model


class Controller:
    def __init__(self):
        self.model = model.Model()
        self.view = view.View()

    def run(self):
         self.view.welcome()

         while True:
             Exit == False
             if Exit == False:  # Se o input nao for valido#
                 self.view.erro() # Mostra mensagem de erro#
                 continue
             else:
                 Exit = True




         self.view.goodbye()



if __name__ == '__main__':
    controller = Controller()
    controller.start()
