import sys
import os
import model
import view


def main():
    """
    Main function
    """
    c = model.Controller()
    v = view.View()



    while True:

        # Get user input
        user_input = input("Enter a command: ")

        # Split user input into a list
        user_input_list = user_input.split()

        # Check if user input is valid
        if user_input_list[0] == "RC":
            if len(user_input_list) == 2:
                v.registar_consultor(user_input_list[1])

                c.RegistarConsultor(user_input_list[1])
            else:
                print("Invalid input")

        elif user_input_list[0] == "RI":
            if len(user_input_list) == 2:
                v.registar_imovel(user_input_list[1])
                c.RegistarImovel(user_input_list[1])
            else:
                print("Invalid input")

        elif user_input_list[0] == "LI":
            if len(user_input_list) == 2:
                v.listar_imovel(user_input_list[1])
                c.ListarConsultores(user_input_list[1])
            else:
                print("Invalid input")

        elif user_input_list[0] == "EI":
            if len(user_input_list) == 2:
                c.eliminar_imovel(user_input_list[1])
                c.EliminarImovel(user_input_list[1])
            else:
                print("Invalid input")

        elif user_input_list[0] == "EC":
            if len(user_input_list) == 2:
                v.eliminar_consultor(user_input_list[1])
                c.EliminarConsultor(user_input_list[1])
            else:
                print("Invalid input")

    else:
        print("Invalid input")




