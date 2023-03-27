# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

import ipdb

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('lib/resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

class Pet:
    
    # pass

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
        
        # We want Database to assign the id when we persist our records into our database
        # when we retrieve records from DB, we want the DB-assigned ID to take the place of "None"

    def __init__(self, name, species, breed, temperament, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist

    @classmethod
    def create_table(cls):
        # Write up SQL to Create Pets Table

        sql = '''
            CREATE TABLE IF NOT EXISTS pets
                (
                    id INTEGER PRIMARY KEY,
                    name STRING,
                    species STRING,
                    breed STRING,
                    temperament STRING
                )
        '''

        CURSOR.execute(sql)

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS pets
        '''

        CURSOR.execute(sql)

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB

    def save(self):

        # ipdb.set_trace()

        sql = '''
            INSERT INTO pets (name, species, breed, temperament)
            VALUES (?, ?, ?, ?)
        '''

        self.id = CURSOR.lastrowid

        CURSOR.execute(sql, (self.name, self.species, self.breed, self.temperament))


    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB

        # Instantiate Pet Class
        # Persist New Instance to Pets table
    @classmethod    
    def create(cls, name, species, breed, temperament):

        # Invoking our __init__ Method
        pet = cls(name, species, breed, temperament)

        # Invoking our save() Instance Method to Persist New Instance to DB
        pet.save()

        return pet

        # To verify persistance:
            # pets = CURSOR.execute('SELECT * FROM pets')
            # [ pet for pet in pets ]

    # ✅ 6. Add "get_newest_pet" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB

    @classmethod
    def get_newest_pet(cls, row):
        pet = cls(
            id=row[0],
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4]
        )

        return pet


    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB

    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM pets
        '''

        return [cls.get_newest_pet(row) for row in CURSOR.execute(sql)]

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

        # If No "pet" Found, return "None"
    
    @classmethod
    def find_by_name(cls, name):
        sql = '''
            SELECT * FROM pets
            WHERE name = ?
            LIMIT 1
        '''

        row = CURSOR.execute(sql, (name, )).fetchone()

        if not row:
            print("Pet not found")
            return None

        # Create Instance of Pet Class from Found Record

        else:
            return cls(
                id=row[0],
                name=row[1],
                species=row[2],
                breed=row[3],
                temperament=row[4]
            )

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

        # If No "pet" Found, return "None"
        # Invoke "__init__"
    
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM pets
            WHERE id = ?
            LIMIT 1
        '''

        row = CURSOR.execute(sql, (id, )).fetchone()

        if not row:
            print("Pet not found")
            return None
        else:
            return cls(
                id=row[0],
                name=row[1],
                species=row[2],
                breed=row[3],
                temperament=row[4]
            )

    # ✅ 10. Add "find_or_create_by" Class Method to:

    # fusion of CREATE and READ from CRUD

    @classmethod
    def find_or_create_by(cls, name=None, species=None, breed=None, temperament=None):
        sql = '''
            SELECT * FROM pets
            WHERE (name, species, breed, temperament) = (?, ?, ?, ?)
            LIMIT 1
        '''

        row = CURSOR.execute(sql, (name, species, breed, temperament, )).fetchone()

        if row:
            print("Conflict")
            return None
        
        if not row:
            sql = '''
                INSERT INTO pets(name, species, breed, temperament)
                VALUES(?, ?, ?, ?)
            '''

            pet = CURSOR.execute(sql, (name, species, breed, temperament, ))

        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # ✅ 11. Add "update" Instance Method to Find "pet" Instance by "id" and Update All Attributes

    def update(self):
        # Create SQL query to Update Particular Pet Record in DB

        sql = '''
            UPDATE pets
            SET name = ?,
                breed = ?
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.name, self.breed, self.id))