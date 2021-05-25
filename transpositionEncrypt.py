import numpy as np 
import math 
import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8
    ciphertext = encryptMessage(myMessage, myKey)
    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message:
    print(ciphertext + '|')
    # Copy the encrypted string in ciphertext to the clipboard:
    pyperclip.copy(ciphertext)

def encryptMessage(message:str,key:int)->str:
    #this is the code for transposition cipher
    message = list(message)
    rows = int(len(message) % key)
    spaces = [' ' for i in range(((rows*key) - len(message)) % key) if (rows*key) != len(message)]
    '''if (rows*key) != len(message):
        for i in range(((rows*key) - len(message)) % key):
            message.append(' ')'''
    message = message + spaces
    arr = np.array(message)  
    box = arr.reshape(math.ceil(len(message)/key),key)
    translatedMessage = ''.join(list(box.transpose().flatten()))
    return translatedMessage + '|'

if __name__=='__main__':
    main()





