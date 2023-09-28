# Imports Native Librarys
import os
# Operators
from src.controllers.operators.somar import Soma
from src.controllers.operators.subtrair import Subtrai
from src.controllers.operators.multiplicar import Multiplica
from src.controllers.operators.dividir import Divide
# View
from src.view.menu import Menu
# Ultils
from ultils import Ultils


def main():
    while True:
        Menu.show()

        menu_option = int(input())

        if menu_option >= 1 and menu_option <= 5:

            if menu_option == 1:  # Soma
                print("Digite sua expressão: ex> 1 + 2 || 1 + 2 + 3")
                user_expression = input().split()

            if menu_option == 5:  # Sair
                Ultils.clean_windows_terminal()
                return
        else:
            print("Entrada errada")


if __name__ == "__main__":
    main()
