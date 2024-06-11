from Crypto.Cipher import AES

def AESEncryption(text,key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext = cipher.encrypt(text)
    return cipher,ciphertext

def AESDEcryption(ctext,key,cipher):
    nonce = cipher.nonce
    cipher =  AES.new(key, AES.MODE_EAX, nonce)
    plaintext = cipher.decrypt(ctext)
    return plaintext.decode()