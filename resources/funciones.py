import random
from service.db import Data_Base as db

def id_coder(chars, lenght):
    res = ""
    for i in range(lenght):
        res += chars[random.randrange(0, len(chars))]
    return res

def check_id(data_base, host, collection, chars, lenght):
    '''
    INCOMPLETO: debe comprobar en una base de datos si
                el id existe y devolverlo si no es así
    '''
    id = id_coder(chars, lenght)
    while len(db.get_data(data_base, host, collection, {"id" : id})["data"]) != 0:
        id = id_coder(chars, lenght)

    return id

def check_user_schema(document):
    allowed_keys = ["name", "surname", "phone", "email", "password", "image", "budget", "id"]
    if len(document) != len(allowed_keys):
        return False
    for key in document:
        if key not in allowed_keys:
            return False
            
    return True

def check_present_schema(document):
    allowed_keys = ["participants", "present_to", "items", "id"]
    if len(document) != len(allowed_keys):
        return False
    for key in document:
        if key not in allowed_keys:
            return False
            
    return True

def check_item_schema(document):
    allowed_keys = ["name", "description", "price", "image", "link", "id"]
    if len(document) != len(allowed_keys):
        return False
    for key in document:
        if key not in allowed_keys:
            return False
            
    return True