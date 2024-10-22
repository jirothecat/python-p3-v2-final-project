from models.__init__ import CONN, CURSOR
from models.animal import Animal
from models.rating import Rating

def seed_database():
    Rating.drop_table()
    Animal.drop_table()

    Animal.create_table()
    Rating.create_table()

    Animal.create("Dog", "Golden Retriever",)

    Rating.create("Dog", 4, "Such a friendly animal!")
    Rating.create("Cat", 3, "Very cute but it did scratch me...")
    Rating.create("Capybara", 5, "So cute!")


seed_database()
print("🌱 Animals and Ratings successfully seeded! 🌱")