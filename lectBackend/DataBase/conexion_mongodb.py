from pymongo import MongoClient


try:
    client = MongoClient('localhost',27017)

    database = client['lect-python']

    collection = database['books']

    documents = collection.find()

    for doc in documents:
        print(doc)
except Exception as ex:
    print("Error en la conexion: {}".format(ex))
finally:
    print("Conexion Exitosa")