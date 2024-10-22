from models.__init__ import CONN, CURSOR

class Animal:
    all = []
    species_tuple = ('Dog', 'Cat', 'Bird', 'Rabbit', 'Hamster') 

    def __init__(self, name, species, id=None):
        self.id = id
        self.name = name
        self._species = species

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if type(value) == str:
            self._species = value
        else:
            raise TypeError("Species must be a string text value!")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS animals 
            (id INTEGER PRIMARY KEY, 
            name TEXT, 
            species TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS animals"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO animals (name, species)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.species))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all.append(self)

    @classmethod
    def create(cls, name, species):
        animal = cls(name, species)
        animal.save()
        return animal

    def delete(self):
        sql = "DELETE FROM animals WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        type(self).all = [animal for animal in type(self).all if animal.id != self.id]

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM animals"
        CURSOR.execute(sql)
        
        return [cls(name, species, id) for id, name, species in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM animals WHERE id = ?"
        CURSOR.execute(sql, (id,))

        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    @classmethod
    def find_by_species(cls, species):
        sql = "SELECT * FROM animals WHERE species = ?"
        CURSOR.execute(sql, (species,))
        
        return [cls(name, species, id) for id, name, species in CURSOR.fetchall()]