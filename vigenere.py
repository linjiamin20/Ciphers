import re

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

def expandKey(key, length) -> str:
    expandedKey = ''
    if length < len(key):
        expandedKey = key[:length]
    else:
        for i in range( length // len(key) ):
            expandedKey = expandedKey + key

        expandedKey = expandedKey + key[:length % len(key)]
    return expandedKey.upper()

def removeSpecialCharacters(text) -> str:
    return re.sub('\W+','', text)

#print(removeSpecialCharacters("maahmoud\\Ah medy "))

def Encrypt(plainText, key):
    global alphabet
    plainText = removeSpecialCharacters(plainText).upper()
    cipherText = ''
    expandedKey = expandKey(key, len(plainText))
    for i in range(len(plainText)):
        index = alphabet.index(plainText[i])
        keyIndex = alphabet.index(expandedKey[i])
        cipherIndex = (index + keyIndex) % 26
        cipherChar = alphabet[cipherIndex]
        cipherText = cipherText + cipherChar
    
    return cipherText

#output = Encrypt("mahmoud ahmedy", "ramzy")

#print(output)

def Decrypt(cipherText, key):
    global alphabet
    plainText = ''
    cipherText = removeSpecialCharacters(cipherText).upper()
    expandedKey = expandKey(key, len(cipherText))
    for i in range(len(cipherText)):
        index = alphabet.index(cipherText[i])
        keyIndex = alphabet.index(expandedKey[i])
        plainIndex = (index - keyIndex + 26) % 26
        plainChar = alphabet[plainIndex]
        plainText = plainText + plainChar
    
    return plainText

#print(Decrypt(output, "ramzy"))