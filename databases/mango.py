import pymongo
import pymongo.mongo_client
from sqlite_connection import connect_to_db, execute_q
import queries as q


# How our request will come back from sqlite 
test_characters = [
    (1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1), 
    (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1)
]

# represent these characters as mongo documents
# How our data will be stored inside Mongo db
character_document = [{
    'character_id' : 1,
    'name': 'Aliquid iste optio reiciendi',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom':  1,
},
{

    'character_id' : 1,
    'name': 'Optio dolorem ex a',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom':  1,
}
]

# credentials 

DBNAME = 'test'
PASSWORD = 'Lord'

# connection 
def mongo_connect(password=PASSWORD, dbname= DBNAME, collection_name = 'characters'):
    client = pymongo.MongoClient(f'mongodb+srv://ishmo:{password}@learn.zzykr8l.mongodb.net/{dbname}?retryWrites=true&w=majority&appName=Learn')
    db = client[dbname]
    collection = db[collection_name]
    return collection

if __name__ == '__main__':
    # Get data from SQLite 
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, q.GET_CHARACTERS)
    # print(sl_characters[:3])

    # connect to specific mongodb collection
    collection = mongo_connect(collection_name = 'characters')

    for character in sl_characters:
        doc = {
        'character_id' : character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom':  character[8],
        }

        collection.insert_one(doc)

    # collection = mongo_connect(collection_name = 'characters')
    # result =  collection.find_one({'name': 'Ryan'})
    # print(result)
