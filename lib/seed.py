from models.__init__ import CONN, CURSOR
from models.animal import Animal
from models.rating import Rating

def seed_database():
    Rating.drop_table()
    Animal.drop_table()

    Animal.create_table()
    Rating.create_table()

    dog = Animal.create("Jolly", "Dog")
    cat = Animal.create("Felix", "Cat")
    capybara = Animal.create("Cheesecake", "Capybara")

    Rating.create(dog.id, 4, "Such a friendly animal!")
    Rating.create(cat.id, 3, "Very cute but it did scratch me...")
    Rating.create(capybara.id, 5, "So cute!")
    Rating.create(capybara.id, 5, "It's so fun to watch her eat grass!")


seed_database()
print("🌱 Animals and Ratings successfully seeded! 🌱")