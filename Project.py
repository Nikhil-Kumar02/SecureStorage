from time import time
 
timestamp = int(time() * 1000)
 
from Ceaser import *
from Vigenère import *
from aes import *
from des import *
from sha import *
from Tripledes import *

from tkinter import *
from tkinter import filedialog

def func(PlainText,VignerCipherKey,c,d):
    
    # PlainText = "I wandered lonely as a cloud That floats on."
    # VignerCipherKey = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd"
    # DesCipherKey = b'hello123'
    # AESCipherKey = b'Sixteen byte key'

    PlainText = PlainText
    VignerCipherKey = VignerCipherKey
    DesCipherKey = c.encode()
    AESCipherKey = d.encode()
    CeaserCipherKey = len(VignerCipherKey)//3

    def enc(PlainText,CeaserCipherKey,AESCipherKey,VignerCipherKey,DesCipherKey):
        # Step 1 Ceaser Cipher encryption
        arr = []

        CeaserEncryptedText =  CeaserEncrypt(PlainText,CeaserCipherKey)
        arr.append("---------------  ENCRYPTION  ---------------")
        arr.append("\n")
        arr.append("Time Stamp is :- ")
        arr.append(timestamp)
        arr.append("Plain Text after Ceaser Cipher Encryption : \n")
        arr.append("\n")
        arr.append("Time Stamp is :- ")
        arr.append(timestamp)
        arr.append("\n")
        arr.append(CeaserEncryptedText)
        
        # Step 2 AES encryption

        AesEncrypttedText=AESEncryption(CeaserEncryptedText.encode(),AESCipherKey)
        arr.append("\n\n")
        arr.append("Encrypted Plain Text obatined after AES encryption : \n")
        arr.append("\n")
        arr.append("Time Stamp is :- ")
        arr.append(timestamp)
        arr.append("\n")
        strg=str(AesEncrypttedText[1])
        arr.append(strg)
        arr.append("\n\n")
        arr.append("\n\n")
        arr.append("The sha for the aes encrypted text is")
        # print(AesEncrypttedText[1])
        print("\n\n\n")
        shaValue = sha(str(AesEncrypttedText[1]).encode())
        arr.append("\n")
        arr.append("Time Stamp is :- ")
        arr.append(timestamp)
        arr.append("\n")
        strSha = str(shaValue)
        arr.append(strSha)
        arr.append("\n\n")
        arr.append("\n\n")
        
        
        # Step 3 for key Encryption using Vigenere

        dec=vigenere_encrypt(AESCipherKey.decode(),VignerCipherKey)
        arr.append("\n\n")
        arr.append("Key after Vigenere Encryption: \n")
        arr.append("\n")
        arr.append("Time Stamp is :- ")
        arr.append(timestamp)
        arr.append("\n")
        arr.append(dec)

        # Step 4 for key Encryption using DES
        timeStampDesBegning =int(time() * 1000)

        dest =DesEncrryption(dec.encode(),DesCipherKey)
        arr.append("\n\n")
        arr.append("Key obtained from DES Encryption: \n")
        arr.append("\n")
        arr.append("\n")
        arr.append("Time Stamp is :- ")
        arr.append(timestamp)
        strg1=str(dest)
        arr.append("\n")
        arr.append(strg1)

        timeStampDesEnd =int(time() * 1000)
        timestampOfDes = timeStampDesEnd-timeStampDesBegning
        arr.append("\n\n")
        arr.append("Time taken in millisecond is ")
        arr.append(timestampOfDes)
        arr.append("\n\n")

        # Triple Des

        Tripdest = triipleDesEncode(dec)

        
        return dest,AesEncrypttedText,arr,Tripdest


    def dec(AesEncrypttedText,CeaserCipherKey,DesCipherKey,dest,VignerCipherKey,Tripdest):
        arrD = []
        arrD.append("---------------  DECRYPTION  ---------------\n")
        # Step 1 Decrypting received Plain text using AES
        arrD.append("The sha for the aes encrypted text is")
        shaValue = sha(str(AesEncrypttedText[1]).encode())
        arrD.append("\n")
        arrD.append(shaValue)
        arrD.append("\n")

        AesDecrypttedText = AESDEcryption(AesEncrypttedText[1],AESCipherKey,AesEncrypttedText[0])

        arrD.append("\n\n")
        arrD.append("Decrypting received Plain text using AES: \n")
        arrD.append("\n")
        arrD.append("Time Stamp is :- ")
        arrD.append(timestamp)
        arrD.append("\n")
        arrD.append(AesDecrypttedText)

        # Step 2 Decrypting output of AES with ceaser

        CeaserDecryptedText = CeaserCipherDecrypt(AesDecrypttedText,CeaserCipherKey)
        arrD.append("\n\n")
        arrD.append("Original Plain Text: \n")
        arrD.append("\n")
        arrD.append("Time Stamp is :- ")
        arrD.append(timestamp)
        arrD.append("\n")
        arrD.append(CeaserDecryptedText)

        # Step 3 for key Decrypt using DES

        dest1 =DesDecryption(dest,DesCipherKey)
        arrD.append("\n\n")
        arrD.append("Decrypting Key using DES: \n")
        arrD.append("\n")
        arrD.append("Time Stamp is :- ")
        arrD.append(timestamp)
        arrD.append("\n")
        strG =str(dest1)
        arrD.append(strG)

        DeTripDes =triipleDesDecode(Tripdest)

        # Step 4 for key Decryption of output of DES with vigenere

        dectxt=vigenere_decrypt(dest1.decode(),VignerCipherKey)
        arrD.append("\n\n")
        arrD.append("Secret Key: \n")
        arrD.append("\n")
        arrD.append("Time Stamp is :- ")
        arrD.append(timestamp)
        arrD.append("\n")
        arrD.append(dectxt)

        return dest1,arrD


    dest=enc(PlainText,CeaserCipherKey,AESCipherKey,VignerCipherKey,DesCipherKey)


    deDest=dec(dest[1],CeaserCipherKey,DesCipherKey,dest[0],VignerCipherKey,dest[3])

    return dest[2],deDest[1]


def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read().splitlines()
    newDAta=func(data[0],data[1],data[2],data[3])
    # newData1 = newDAta[0].split(",")
    things_To_add = newDAta[0]+newDAta[1]
    
    stringing =""
    for i in range(len(things_To_add)):
        
        stringing=stringing+ str(things_To_add[i])
    stringingEnc =""
    for i in range(len(newDAta[0])):
        
        stringingEnc=stringingEnc+ str(newDAta[0][i])
    stringingDec =""
    for i in range(len(newDAta[1])):
        
        stringingDec=stringingDec+ str(newDAta[1][i])
    my_file = open("enc.txt","w+")
    my_file.write(stringingEnc)
    my_file = open("dec.txt","w+")
    my_file.write(stringingDec)
    txtarea.insert(END, stringingEnc)
    txtarea1.insert(END, stringingDec)
    tf.close()
    return data


def saveFile():
    tf = filedialog.asksaveasfile(
        mode='w',

        title ="Save file",
        defaultextension=".txt"
        )
    # tf.config(mode='w')

    # pathh.insert(END, tf)
    if tf is None:
        return

    data = str(txtarea.get(1.0, END))
    tf.write(data)
   
    tf.close()


ws = Tk()
ws.title("Enigma")
ws.geometry("1000x500")
ws['bg']='#fb0'
# adding frame
frame = Frame(ws)
frame.pack(pady=20)

# adding scrollbars 
ver_sb = Scrollbar(frame, orient=VERTICAL )
ver_sb.pack(side=RIGHT, fill=BOTH)

hor_sb = Scrollbar(frame, orient=HORIZONTAL)
hor_sb.pack(side=BOTTOM, fill=BOTH)

# adding writing space
txtarea = Text(frame, width=40, height=20)
txtarea.pack(side=LEFT)
frame.pack(pady=20,padx=20)
# adding writing space
txtarea1 = Text(frame, width=40, height=20)
txtarea1.pack(side=LEFT)

# binding scrollbar with text area
txtarea.config(yscrollcommand=ver_sb.set)
ver_sb.config(command=txtarea.yview)

txtarea.config(xscrollcommand=hor_sb.set)
hor_sb.config(command=txtarea.xview)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Save File", 
    command=saveFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

ws.mainloop()

