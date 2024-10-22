# lib/cli.py

from helpers import (
    exit_program,
    animal_management,
    rating_management
)


from models.animal import Animal
from models.rating import Rating

def main_menu():
    print("\nHello, Welcome to the Animal Shelter Management System!\n")
    print("1. Manage Animals")
    print("2. Manage Ratings")
    print("0. Exit")
    return input("\nEnter your choice: ")


def main():
    Animal.create_table()
    Rating.create_table()

    while True:
        choice = main_menu()
        if choice == "1":
            animal_management()
        elif choice == "2":
            rating_management()
        elif choice == "0":
            exit_program()
            break
        else:
            print("\nNot a valid choice, please try again.\n")
        input("\nPress 'return' to continue... \n")


if __name__ == "__main__":
    main()
