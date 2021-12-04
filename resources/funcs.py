from random import randrange

def id_generaor(length, chars):
    res = ""
    for i in range(length):
        res += chars[randrange(0, len(chars))]
    
    return res

def check_id(id, to_check):
    for item in to_check:
        if item["id"] == id:
            return False

    return True

def check_item(item):
    allowed_keys = ["name", "description", "price", "link", "id"]
    if len(item) != allowed_keys:
        return False
    for key in item:
        if key not in allowed_keys:
            return False
    
    if type(item["name"]) != str and type(item["description"]) != str and type(item["price"]) != str and type(item["link"]) != str and type(item["id"]) != str:
        return False
            
    return True

def check_present(present):
    allowed_keys = ["participantes", "present_to", "items", "id"]
    if len(present) != allowed_keys:
        return False
    for key in present:
        if key not in allowed_keys:
            return False
    
    if type(present["participants"]) != list and type(present["present_to"]) != str and type(present["items"]) != list and type(present["id"]) != str:
            return False

    return True

def check_user(user):
    allowed_keys = ["name", "surname", "phone", "email", "password", "budget", "properties", "id"]
    if len(user) != allowed_keys:
        return False
    for key in user:
        if key not in allowed_keys:
            return False
    
    if type(user["name"]) != str and type(user["surname"]) != str and type(user["phone"]) != str and type(user["email"]) != str and type(user["password"]) != str and type(user["budget"]) != dict and type(user["properties"]) != dict and type(user["id"]) != str:
        return False
            
    return True

def encrypt_password(password):
    chars = {
        "1" : "5",
        "2" : "1",
        "3" : "8",
        "4" : "0",
        "5" : "6",
        "6" : "3",
        "7" : "9",
        "8" : "2",
        "9" : "4",
        "0" : "7",

        "a" : "u",
        "e" : "a",
        "i" : "o",
        "o" : "e",
        "u" : "i",

        "b" : "v",
        "c" : "z",
        "d" : "j",
        "f" : "b",
        "g" : "n",
        "h" : "p",
        "j" : "q",
        "k" : "m",
        "l" : "r",
        "m" : "h",
        "n" : "f",
        "ñ" : "s",
        "p" : "k",
        "q" : "x",
        "r" : "y",
        "s" : "c",
        "t" : "w",
        "v" : "l",
        "w" : "ñ",
        "x" : "d",
        "y" : "g",
        "z" : "t",

        "A" : "U",
        "E" : "A",
        "I" : "O",
        "O" : "E",
        "U" : "I",

        "B" : "V",
        "C" : "Z",
        "D" : "J",
        "F" : "B",
        "G" : "N",
        "H" : "P",
        "J" : "Q",
        "K" : "M",
        "L" : "R",
        "M" : "H",
        "N" : "F",
        "Ñ" : "S",
        "P" : "K",
        "Q" : "X",
        "R" : "Y",
        "S" : "C",
        "T" : "W",
        "V" : "L",
        "W" : "Ñ",
        "X" : "D",
        "Y" : "G",
        "Z" : "T"
    }

    res = ""
    for char in password:
        if char in chars:
            res += chars[char]
        else:
            res += char
            
    return res

def decrypt_password(password):
    chars = {
        "5" : "1",
        "1" : "2",
        "8" : "3",
        "0" : "4",
        "6" : "5",
        "3" : "6",
        "9" : "7",
        "2" : "8",
        "4" : "9",
        "7" : "0",

        "u" : "a",
        "a" : "e",
        "o" : "i",
        "e" : "o",
        "i" : "u",

        "v" : "b",
        "z" : "c",
        "j" : "d",
        "b" : "f",
        "n" : "g",
        "p" : "h",
        "q" : "j",
        "m" : "k",
        "r" : "l",
        "h" : "m",
        "f" : "n",
        "s" : "ñ",
        "k" : "p",
        "x" : "q",
        "y" : "r",
        "c" : "s",
        "w" : "t",
        "l" : "v",
        "ñ" : "w",
        "d" : "x",
        "g" : "y",
        "t" : "z",

        "U" : "A",
        "A" : "E",
        "O" : "I",
        "E" : "O",
        "I" : "U",

        "V" : "B",
        "Z" : "C",
        "J" : "D",
        "B" : "F",
        "N" : "G",
        "P" : "H",
        "Q" : "J",
        "M" : "K",
        "R" : "L",
        "H" : "M",
        "F" : "N",
        "S" : "Ñ",
        "K" : "P",
        "X" : "Q",
        "Y" : "R",
        "C" : "S",
        "W" : "T",
        "L" : "V",
        "Ñ" : "W",
        "D" : "X",
        "G" : "Y",
        "T" : "Z"
    }

    res = ""
    for char in password:
        if char in chars:
            res += chars[char]
        else:
            res += char
            
    return res

def check_password(password, espected):
    encrypted_password = encrypt_password(password)
    decripted_password = decrypt_password(espected)

    if encrypted_password == espected and decripted_password == password:
        return True
    else:
        return False

if __name__ == "__main__":
    def test_encrypt_decrypt_password():
        password = "ToniPizarro22"
        espected = "WefoKotuyye11"

        encrypted_password = encrypt_password(password)
        decripted_password = decrypt_password(espected)

        if encrypted_password == espected:
            print("Coincide!")
        else:
            print("No encripta correctamente")

        print("\n")

        if decripted_password == password:
            print("Coincide!")
        else:
            print("No desencripta correctamente")