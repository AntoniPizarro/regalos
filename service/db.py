from pymongo import MongoClient

class Data_Base:
    
    # OPEN CLOUSE
    @staticmethod
    def add_document(host, data_base, collection, document):
        cliente = MongoClient(host)
        db = cliente[data_base]
        try:
            db[collection].insert_one(document)
            return True
        except KeyError:
            print("The document hasn't any key")
            
        return False

    @staticmethod
    def get_data(host, data_base, collection, data={}):
        cliente = MongoClient(host)
        db = cliente[data_base]
        res = {"data" : []}
        docs = db[collection].find(data)
        for doc in docs:
            res["data"].append(doc)
            
        return res