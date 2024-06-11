from Crypto.Cipher import DES

def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)

def DesEncrryption(text,key):

    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

def DesDecryption(cipher,key):
    des = DES.new(key, DES.MODE_ECB)
    descryptedText = des.decrypt(cipher)
    return descryptedText