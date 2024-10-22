from models.__init__ import CONN, CURSOR

class Rating:
    all = []

    def __init__(self, animal_id, value, id=None):
        self.id = id
        self.animal_id = animal_id
        self.value = value

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS ratings 
            (id INTEGER PRIMARY KEY, 
            animal_id INTEGER,
            value REAL,
            FOREIGN KEY (animal_id) REFERENCES animals(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS ratings"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO ratings (animal_id, value)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.animal_id, self.value))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all.append(self)

    @classmethod
    def create(cls, animal_id, value):
        rating = cls(animal_id, value)
        rating.save()
        return rating

    def delete(self):
        sql = "DELETE FROM ratings WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        type(self).all = [rating for rating in type(self).all if rating.id != self.id]

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM ratings"
        CURSOR.execute(sql)
        
        return [cls(animal_id, value, id) for id, animal_id, value in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM ratings WHERE id = ?"
        CURSOR.execute(sql, (id,))

        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    @classmethod
    def find_by_animal_id(cls, animal_id):
        sql = "SELECT * FROM ratings WHERE animal_id = ?"
        CURSOR.execute(sql, (animal_id,))
        
        return [cls(animal_id, value, id) for id, animal_id, value in CURSOR.fetchall()]