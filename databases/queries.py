GET_CHARACTERS = '''SELECT * FROM charactercreator_character;'''


CREATE_TEST_TABLE = '''
    CREATE TABLE IF NOT EXISTS test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name"  VARCHAR(200) NOT NULL,
    "age" INT NOT NULL,
    "country_of_origin" VARCHAR(200) NOT NULL);
'''

# insert rows in th table

INSERT_TEST_TABLE = '''
    INSERT INTO test_table("name", "age", "country_of_origin")
    VALUES ('Rayn Allred', 30, 'Uganda');
'''

DROP_TEST_TABLE = '''
drop table if exists test_table'''


CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters
    (
    "character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dextrity" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
'''

INSERT_RYAN = '''
    INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dextrity", "wisdom")
    VALUES ('Ryan Allred', 50, 100, 1000, 9000, 4, -5, 12)
    '''

DROP_CHARACTER_TABLE = '''
    DROP TABLE IF EXISTS test_table
'''