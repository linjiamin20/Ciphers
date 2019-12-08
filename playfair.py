import re

def generateKey(key) -> str:
    
    alphabet = "abcdefghiklmnopqrstuvwxyz".upper()
    key = handleJchar(key)
    key = removeRepeats(key)
    key = key.upper()
    for i in key:
        if i in alphabet:
            alphabet = alphabet.replace(i, '')
    key = (key+alphabet).upper()
    j = 1
    for i in key:
        print(i, end=' ')
        
        if(j % 5 == 0):
            print()
        j = j + 1    
    
    return (key+alphabet)

#generateKey('monarch')

def removeRepeats(text) -> str:
    returnText = ""
    repeatedChars = ""
    for i in text:
        if i not in repeatedChars:
            returnText += i
            repeatedChars += i
    return returnText

#print(removeRepeats("smallest"))
        
def handleRepeats(text) -> str:
    text = list(text)
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            text[i+1] = 'X'
    return ''.join(text)

#print(handleRepeats('smallest'))

def checkEvenString(text) -> str:
    if len(text) % 2:
        text += 'X'
    return text


#print(checkEvenString('monarch'))

def xyToI(x, y) -> int:
    return (x-1)*5 + (y-1)

#print(xyToI(3,4))

def iToXY(i) -> [int, int]:
    return [(i//5)+1 ,(i%5)+1]

#print(iToXY(13))


def handleJchar(text) -> str:
    text = list(text)
    for i in range(len(text)):
        if text[i] == 'J' :
            text[i] = 'I'
    return ''.join(text)

#print(handleJchar('jackson'))

def splitToPairs(text):
    returnList = []
    i = 0
    while i < len(text):
        substr = text[i:i+2]
        returnList.append(substr)
        i += 2
    
    return returnList

#print(splitToPairs("mynameismahmoud"))
def removeSpecialCharacters(text) -> str:
    return re.sub('\W+','', text)

#print(removeWhitespaces("my name is mahmoud"))

def formatText(text):
    text = str(text).upper()
    text = removeSpecialCharacters(text)
    text = handleJchar(text)
    text = handleRepeats(text)
    text = checkEvenString(text)
    text = splitToPairs(text)
    return text

def Encrypt(plainText, key) -> str:
    X = 0
    Y = 1

    plainTextList = formatText(plainText)
    
    key = generateKey(key)
    #print(plainTextList)
    cipherTextList = []
    
    for i in plainTextList:
        

        plainChar1XY = iToXY(key.index(i[0]))
        plainChar2XY = iToXY(key.index(i[1]))
        print(plainChar1XY , plainChar2XY)
        
        cipherChar1XY = [0,0]
        cipherChar2XY = [0,0]
        
        # Same Row
        if plainChar1XY[X] == plainChar2XY[X]:
            print("Same row!")
            if plainChar1XY[Y] < 5:
                cipherChar1XY[Y] = plainChar1XY[Y] + 1
            else:
                cipherChar1XY[Y] = 1
            if plainChar2XY[Y] < 5:
                cipherChar2XY[Y] = plainChar2XY[Y] + 1
            else:
                cipherChar2XY[Y] = 1
            
            cipherChar1XY[X] = plainChar1XY[X]
            cipherChar2XY[X] = plainChar2XY[X]
        
        # Same Column
        elif plainChar1XY[Y] == plainChar2XY[Y]:
            print("Same column!")
            if plainChar1XY[X] < 5:
                cipherChar1XY[X] = plainChar1XY[X] + 1
            else:
                cipherChar1XY[X] = 1
            if plainChar2XY[X] < 5:
                cipherChar2XY[X] = plainChar2XY[X] + 1
            else:
                cipherChar2XY[X] = 1
            
            cipherChar1XY[Y] = plainChar1XY[Y]
            cipherChar2XY[Y] = plainChar2XY[Y]
        
        else:
            cipherChar1XY[X] = plainChar1XY[X]
            cipherChar2XY[X] = plainChar2XY[X]

            cipherChar1XY[Y] = plainChar2XY[Y]
            cipherChar2XY[Y] = plainChar1XY[Y]
        
        cipherChar1I = xyToI(cipherChar1XY[X], cipherChar1XY[Y])
        cipherChar2I = xyToI(cipherChar2XY[X], cipherChar2XY[Y])
        
        pair = ''.join([ key[cipherChar1I], key[cipherChar2I] ])
        print(i, ' -> ' , pair)
        cipherTextList.append(pair)


    return ''.join(cipherTextList)

def Decrypt(cipherText, key) -> str:
    X = 0
    Y = 1

    cipherTextList = formatText(cipherText)
    
    print(''.join(cipherTextList))
    key = generateKey(key)
    print(cipherTextList)
    plainTextList = []
    
    for i in cipherTextList:
        cipherChar1XY = iToXY(key.index(i[0]))
        cipherChar2XY = iToXY(key.index(i[1]))
        print(cipherChar1XY , cipherChar2XY)
        
        plainChar1XY = [0,0]
        plainChar2XY = [0,0]
        
        # Same Row
        if cipherChar1XY[X] == cipherChar2XY[X]:
            print("Same row!")
            if cipherChar1XY[Y] > 1:
                plainChar1XY[Y] = cipherChar1XY[Y] - 1
            else:
                plainChar1XY[Y] = 5
            if cipherChar2XY[Y] > 1:
                plainChar2XY[Y] = cipherChar2XY[Y] - 1
            else:
                plainChar2XY[1] = 5
            
            plainChar1XY[X] = cipherChar1XY[X]
            plainChar2XY[X] = cipherChar2XY[X]
        
        # Same Column
        elif cipherChar1XY[Y] == cipherChar2XY[Y]:
            # print("Same column!")
            if cipherChar1XY[X] > 1:
                plainChar1XY[X] = cipherChar1XY[X] - 1
            else:
                plainChar1XY[X] = 5
            if cipherChar2XY[X] > 1:
                plainChar2XY[X] = cipherChar2XY[X] - 1
            else:
                plainChar2XY[X] = 5
            
            plainChar1XY[Y] = cipherChar1XY[Y]
            plainChar2XY[Y] = cipherChar2XY[Y]
        
        else:
            plainChar1XY[X] = cipherChar1XY[X]
            plainChar2XY[X] = cipherChar2XY[X]

            plainChar1XY[Y] = cipherChar2XY[Y]
            plainChar2XY[Y] = cipherChar1XY[Y]
        
        plainChar1I = xyToI(plainChar1XY[X], plainChar1XY[Y])
        plainChar2I = xyToI(plainChar2XY[X], plainChar2XY[Y])
        
        pair = ''.join([ key[plainChar1I], key[plainChar2I] ])
        print(i, ' -> ' , pair)
        plainTextList.append(pair)


    return ''.join(plainTextList)


#output = Encrypt("mahmoud salah is going places", "monarch")
#print(output)

#output = Decrypt(output, "monarch")
#print(output)