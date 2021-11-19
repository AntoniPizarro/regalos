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
        except:
            print("Error")
            
        return False

    @staticmethod
    def get_data(host, data_base, collection, query={}):
        cliente = MongoClient(host)
        db = cliente[data_base]
        res = {"data" : []}
        docs = db[collection].find(query)
        for doc in docs:
            res["data"].append(doc)
            
        return res
    
    @staticmethod
    def update_data(host, data_base, collection, data, query={}):
        cliente = MongoClient(host)
        db = cliente[data_base]
        docs = db[collection].find(query)
        if docs.count() > 0:
            for doc in docs:
                db[collection].update_one(doc, {"$set" : data})
            return True
        else:
            return False