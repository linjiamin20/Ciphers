import re
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

def removeSpecialCharacters(text) -> str:
    return re.sub('\W+','', text)

def Encrypt(plainText, key):
    global alphabet

    key = int(key)
    plainText = removeSpecialCharacters(plainText).upper()
    cipherText = ''
    for i in range(len(plainText)):
        index = alphabet.index(plainText[i])
        cipherIndex = (index + key) % 26
        cipherChar = alphabet[cipherIndex]
        cipherText = cipherText + cipherChar
    return cipherText

def Decrypt(cipherText, key):
    global alphabet
    
    key = int(key)
    plainText = ''
    cipherText = removeSpecialCharacters(cipherText).upper()
    for i in range(len(cipherText)):
        index = alphabet.index(cipherText[i])
        modKey = key % 26
        plainIndex = (index - modKey + 26) % 26
        plainChar = alphabet[plainIndex]
        plainText = plainText + plainChar
    return plainText
