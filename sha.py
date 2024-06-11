from hashlib import sha512

def sha(txt):
    m=sha512(txt)
    outp=m.hexdigest()
    print(outp,"\n\n")
    return outp
