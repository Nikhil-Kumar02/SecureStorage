from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

def triipleDesEncode(txt):
    cipher = DES3.new(key, DES3.MODE_CFB)
    plaintext = txt.encode()
    msg = cipher.iv + cipher.encrypt(plaintext)
    return msg

def triipleDesDecode(msg):
    cipher = DES3.new(key, DES3.MODE_CFB)
    decryptmsg = cipher.iv + cipher.decrypt(msg)
    return decryptmsg[16:]