from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = Storemodel.find_by_name(name)
        if store:
            return store.json()
        return {'message' : 'store not found' },404
    def post(self,name):
        if Storemodel.find_by_name(name):
            return {'message' : "Astore with name '{}' already exists.".format(name)}, 400
        store = Storemodel(name)

        try:
            store.save_to_db()

        except:
            return {'message' : 'an error occured while creating the store.'},500
        return store.json(),201

    def delete(self,name):
        store = Storemodel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores' : [x.json() for x in Storemodel.find_all()]}


