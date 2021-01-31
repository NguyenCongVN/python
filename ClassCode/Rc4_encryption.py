from tkinter import *

def KSA(key):
    keylength = len(key)

    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)
def Encrypt(plainText , keystream):
    cipher = ''
    for i in plainText:
        cipher = cipher.join(("%02X" % (ord(i) ^ keystream.__next__())))
    return cipher

def Decrypt(cipherText , keystream):
    plainText = ''
    for i in cipherText:
        plainText = plainText.join(chr(int(i, 16) ^ keystream.__next__()))
    return plainText

def set_text(text , entry):
    entry.delete(0,END)
    entry.insert(0,text)
    return

if __name__ == '__main__':
    root = Tk()
    key = '738'
    def convert_key(s):
        return [ord(c) for c in s]
    key = convert_key(key)
    keystream = RC4(key)
    rangeInputFrame = Frame(root)
    rangeInputFrame.pack(fill='both', expand=FALSE)
    labelRange = Label(rangeInputFrame, text='plain text')
    inputRange = Entry(rangeInputFrame)
    labelRange.pack(side=LEFT, anchor=NW, padx=20)
    inputRange.pack(side=RIGHT, anchor=NE, padx=40)

    rangeInputFrame2 = Frame(root)
    rangeInputFrame2.pack(fill='both', expand=FALSE)
    labelPath = Label(rangeInputFrame2, text='cipher text')
    inputPath = Entry(rangeInputFrame2)
    labelPath.pack(side=LEFT, anchor=NW, padx=20)
    inputPath.pack(side=RIGHT, anchor=NE, padx=40)
    AddButton = Button(root, text='encrypt',
                       command=lambda: set_text(Encrypt(inputRange.get() , keystream) ,inputPath))
    AddButton.pack()

    rangeInputFrame3 = Frame(root)
    rangeInputFrame3.pack(fill='both', expand=FALSE)
    labelRange2 = Label(rangeInputFrame3, text='cipher text')
    inputRange2 = Entry(rangeInputFrame3)
    labelRange2.pack(side=LEFT, anchor=NW, padx=20)
    inputRange2.pack(side=RIGHT, anchor=NE, padx=40)

    rangeInputFrame4 = Frame(root)
    rangeInputFrame4.pack(fill='both', expand=FALSE)
    labelPath2 = Label(rangeInputFrame4, text='plain text')
    inputPath2 = Entry(rangeInputFrame4)
    labelPath2.pack(side=LEFT, anchor=NW, padx=20)
    inputPath2.pack(side=RIGHT, anchor=NE, padx=40)
    AddButton = Button(root, text='decrypt',
                       command=lambda: set_text(Decrypt(inputRange2.get(), keystream), inputPath2))
    AddButton.pack()

    root.mainloop()
    # plaintext = 'Hoc vien ky thuat quan su'
