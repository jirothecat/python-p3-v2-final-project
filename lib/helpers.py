# lib/helpers.py
from models.animal import Animal
from models.rating import Rating

def animal_management():
    while True:
        choice = animal_menu()
        if choice == "1":
            add_animal()
        elif choice == "2":
            list_animals()
        elif choice == "3":
            find_animal()
        elif choice == "4":
            find_animals_by_species()
        elif choice == "5":
            delete_animal()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def animal_menu():
    print("\nAnimal Management")
    print("1. Add new animal")
    print("2. List all animals")
    print("3. Find animal by ID")
    print("4. Find animals by species")
    print("5. Delete animal")
    print("0. Back to main menu")
    return input("\nEnter your choice: ")

def add_animal():
    name = input("Enter animal name: ")
    species = input("Enter animal species: ")
    animal = Animal.create(name, species)
    print(f"Animal {animal.name} (ID: {animal.id}) added successfully.")

def list_animals():
    animals = Animal.get_all()
    if animals:
        for animal in animals:
            print(f"ID: {animal.id}, Name: {animal.name}, Species: {animal.species}")
    else:
        print("No animals found.")

def find_animal():
    id = input("Enter animal ID: ")
    animal = Animal.find_by_id(int(id))
    if animal:
        print(f"ID: {animal.id}, Name: {animal.name}, Species: {animal.species}")
    else:
        print("Animal not found.")

def find_animals_by_species():
    species = input("Enter species to search for: ")
    animals = Animal.find_by_species(species)
    if animals:
        for animal in animals:
            print(f"ID: {animal.id}, Name: {animal.name}, Species: {animal.species}")
    else:
        print(f"No animals found for species: {species}")

def delete_animal():
    id = input("Enter animal ID to delete: ")
    animal = Animal.find_by_id(int(id))
    if animal:
        animal.delete()
        print(f"Animal {animal.name} (ID: {animal.id}) deleted successfully.")
    else:
        print("Animal not found.")


def rating_management():
    while True:
        choice = rating_menu()
        if choice == "1":
            add_rating()
        elif choice == "2":
            list_ratings()
        elif choice == "3":
            find_rating()
        elif choice == "4":
            find_ratings_by_animal()
        elif choice == "5":
            delete_rating()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


def rating_menu():
    print("\nRating Management")
    print("1. Add new rating")
    print("2. List all ratings")
    print("3. Find rating by ID")
    print("4. Find ratings by animal ID")
    print("5. Delete rating")
    print("0. Back to main menu")
    return input("Enter your choice: ")


def add_rating():
    animal_id = input("Enter animal ID to rate: ")
    animal = Animal.find_by_id(int(animal_id))
    if animal:
        value = input(f"Enter rating for {animal.name} (0-5): ")
        try:
            value = float(value)
            if 0 <= value <= 5:
                rating = Rating.create(animal.id, value)
                print(f"Rating {rating.value} added for animal {animal.name} (ID: {animal.id}).")
            else:
                print("Rating must be between 0 and 5.")
        except ValueError:
            print("Invalid rating value. Please enter a number between 0 and 5.")
    else:
        print("Animal not found.")

def list_ratings():
    ratings = Rating.get_all()
    if ratings:
        for rating in ratings:
            animal = Animal.find_by_id(rating.animal_id)
            print(f"Rating ID: {rating.id}, Animal: {animal.name}, Value: {rating.value}")
    else:
        print("No ratings found.")

def find_rating():
    id = input("Enter rating ID: ")
    rating = Rating.find_by_id(int(id))
    if rating:
        animal = Animal.find_by_id(rating.animal_id)
        print(f"Rating ID: {rating.id}, Animal: {animal.name}, Value: {rating.value}")
    else:
        print("Rating not found.")

def find_ratings_by_animal():
    animal_id = input("Enter animal ID to find ratings: ")
    animal = Animal.find_by_id(int(animal_id))
    if animal:
        ratings = Rating.find_by_animal_id(animal.id)
        if ratings:
            for rating in ratings:
                print(f"Rating ID: {rating.id}, Value: {rating.value}")
        else:
            print(f"No ratings found for animal {animal.name} (ID: {animal.id}).")
    else:
        print("Animal not found.")

def delete_rating():
    id = input("Enter rating ID to delete: ")
    rating = Rating.find_by_id(int(id))
    if rating:
        rating.delete()
        print(f"Rating (ID: {rating.id}) deleted successfully.")
    else:
        print("Rating not found.")




def exit_program():
    print("\nThank you for visiting the Animal Shelter Database, see you next time!\n")
    exit()
