from models.__init__ import CONN, CURSOR
from models.animal import Animal
from models.rating import Rating

def seed_database():
    Rating.drop_table()
    Animal.drop_table()

    Animal.create_table()
    Rating.create_table()

    turtle = Animal.create("Grandpa", "Turtle")
    bird = Animal.create("Toby", "Bird")
    dog = Animal.create("Jolly", "Dog")
    cat = Animal.create("Felix", "Cat")
    horse = Animal.create("Stalwart", "Horse")
    capybara = Animal.create("Cheesecake", "Capybara")

    Rating.create(bird.id, 4, "This bird talks back, kinda cool!")
    Rating.create(dog.id, 4, "Such a friendly animal!")
    Rating.create(cat.id, 3, "Very cute but it did scratch me...")
    Rating.create(horse.id, 5, "What a beautiful mane! I would love to look after him.")
    Rating.create(capybara.id, 5, "So cute!")
    Rating.create(capybara.id, 5, "It's so fun to watch her eat grass!")
    Rating.create(turtle.id, 2, "Nice shell, but it doesn't really do anything.")


seed_database()
print("🌱 Animals and Ratings successfully seeded! 🌱")